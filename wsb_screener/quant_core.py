"""
quant_core.py
=============
**Dip-Buy Swing Model** - buy-only, mean-reversion + momentum, with a hard stop.

Rebuilt from an empirical stop/exit sweep (6y, 60 popular tickers). What actually
worked, and is baked in here:

* **Entry (BUY, high conviction):** buy a *dip* - price is oversold (RSI-2 < 10)
  and/or stretched **>= 1.5 standard deviations below the 20/21 band** (`z_band`).
  No 200-SMA, no "must be above the band" - stocks retrace, so we buy the stretch.
* **Exit = adaptive z-target (mean reversion + momentum):** we sell as price snaps
  back toward/through the band. The target *adapts to the name's regime* so we
  **ride momentum** in strong names and **snap back fast** in weak ones:
    - strong (above 50-SMA and positive 3-month momentum): ride to `z >= +1.5`
    - mixed  (one of the two): `z >= +0.5`
    - weak   (neither): `z >= 0.0`  (just take the bounce back to the band)
* **Hard stop on every trade** (default **5%**). The sweep showed 3% is too tight
  (~48-50% stopped out), 4-5% lifts win rate to ~56-61%. `STOP_PCT` is configurable;
  we can always re-enter on the next dip.
* **No SELL signals in the screener** - it only tells you what to BUY (and what's
  close). Exits are handled by the rules above once you're in a trade.

There's also a **$100 portfolio backtest** (`portfolio_backtest`) so you can see how
the whole thing does with real position sizing and the stop.

    Research only, not financial advice.
"""
from __future__ import annotations
import heapq
import numpy as np
import pandas as pd

# ----------------------------- fixed parameters -----------------------------
CAPITAL     = 1000.0

BAND_SMA    = 20        # Bull-Market Support Band = 20 SMA / 21 EMA
BAND_EMA    = 21
SMA_FAST    = 50        # regime context for the adaptive exit + warm-up
RSI_FAST    = 2         # Connors RSI-2
RSI_SLOW    = 14
ATR_N       = 14
VOL_N       = 20
MOM_N       = 63        # ~3-month momentum for the regime

# entry (dip)
Z_BUY       = -1.5      # >= this many std-devs below the band = buyable stretch
RSI_OS      = 10.0
RSI_OS_SOFT = 25.0      # "getting oversold" -> close to buy

# adaptive exit z-targets (mean reversion; ride momentum in strong names)
Z_EXIT_WEAK   = 0.0
Z_EXIT_MID    = 0.5
Z_EXIT_STRONG = 1.5

# risk
STOP_PCT    = 0.05      # hard stop per trade (tested 3/4/5/6% -> 3% too tight)
MAX_HOLD    = 40        # time cap (days)

# conviction score weights (sum to 1.0)
W_OVERSOLD  = 0.30
W_STRETCH   = 0.26
W_VOLUME    = 0.16
W_REVERSAL  = 0.10
W_TREND     = 0.18

NEAR_MIN    = 40.0      # score needed for CLOSE TO BUY (approaching)


# ----------------------------- indicators -----------------------------
def rsi(series: pd.Series, n: int) -> pd.Series:
    d = series.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn.replace(0, np.nan))


def atr(df: pd.DataFrame, n: int = ATR_N) -> pd.Series:
    h, l, c = df["High"], df["Low"], df["Close"]
    pc = c.shift(1)
    tr = pd.concat([(h - l), (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def _obv(close: pd.Series, vol: pd.Series) -> pd.Series:
    return (np.sign(close.diff().fillna(0.0)) * vol).cumsum()


def _adaptive_target(above50: bool, mom: float) -> float:
    """Exit z-target chosen at entry from the name's regime."""
    m = mom if mom == mom else 0.0   # NaN -> 0
    if above50 and m > 0:
        return Z_EXIT_STRONG
    if above50 or m > 0:
        return Z_EXIT_MID
    return Z_EXIT_WEAK


def compute_features(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy().reset_index(drop=True)
    c = d["Close"]

    d["SMA5"]  = c.rolling(5).mean()
    d["SMA20"] = c.rolling(BAND_SMA).mean()
    d["EMA21"] = c.ewm(span=BAND_EMA, adjust=False).mean()
    d["SMA50"] = c.rolling(SMA_FAST).mean()
    d["band_mid"] = (d["SMA20"] + d["EMA21"]) / 2
    d["band_top"] = d[["SMA20", "EMA21"]].max(axis=1)
    d["band_bot"] = d[["SMA20", "EMA21"]].min(axis=1)

    d["std20"] = c.rolling(BAND_SMA).std()
    d["z_band"] = (c - d["band_mid"]) / d["std20"].replace(0, np.nan)
    d["ATR"] = atr(d, ATR_N)
    d["dist_band_%"] = (c - d["band_mid"]) / c * 100.0

    d["RSI2"] = rsi(c, RSI_FAST)
    d["RSI14"] = rsi(c, RSI_SLOW)

    d["avg_vol20"] = d["Volume"].rolling(VOL_N).mean()
    d["vol_surge"] = d["Volume"] / d["avg_vol20"].replace(0, np.nan)
    d["OBV"] = _obv(c, d["Volume"])
    d["obv_rising"] = d["OBV"] > d["OBV"].shift(5)
    d["up_close"] = c > c.shift(1)

    d["above_50"] = c > d["SMA50"]
    d["sma20_up"] = d["SMA20"] > d["SMA20"].shift(5)
    d["mom_63_%"] = (c / c.shift(MOM_N) - 1.0) * 100.0

    # exit target that WOULD apply if bought now (regime-adaptive)
    d["exit_z_target"] = [
        _adaptive_target(bool(a), m) for a, m in zip(d["above_50"], d["mom_63_%"] / 100.0)
    ]

    # ---------------- conviction sub-scores (0..1) ----------------
    r2 = d["RSI2"]
    c_oversold = np.select([r2 <= 5, r2 <= 10, r2 <= 20, r2 <= 30, r2 <= 45],
                           [1.00, 0.85, 0.60, 0.40, 0.20], default=0.05)
    z = d["z_band"]
    c_stretch = np.select([z <= -2.5, z <= -2.0, z <= Z_BUY, z <= -1.0, z <= -0.5, z <= 1.0],
                          [1.00, 0.90, 0.75, 0.55, 0.35, 0.15], default=0.0)
    vs = d["vol_surge"]
    vbase = np.select([vs >= 2.0, vs >= 1.5, vs >= 1.2], [1.0, 0.8, 0.5], default=0.2)
    c_volume = np.clip(vbase * np.where(d["up_close"], 1.0, 0.7), 0, 1)
    c_reversal = 0.5 * d["up_close"].astype(float) + 0.5 * (r2 > r2.shift(1)).astype(float)
    c_trend = (0.4 * d["above_50"].astype(float) + 0.3 * d["sma20_up"].astype(float)
               + 0.3 * (c > d["band_bot"]).astype(float)).clip(0, 1)

    for nm, arr in (("c_oversold", c_oversold), ("c_stretch", c_stretch), ("c_volume", c_volume),
                    ("c_reversal", c_reversal), ("c_trend", c_trend)):
        d[nm] = pd.Series(np.asarray(arr, dtype=float), index=d.index).fillna(0.0)

    d["score"] = 100.0 * (W_OVERSOLD * d["c_oversold"] + W_STRETCH * d["c_stretch"]
                          + W_VOLUME * d["c_volume"] + W_REVERSAL * d["c_reversal"]
                          + W_TREND * d["c_trend"])

    # ---------------- entry trigger (buy-only; no sell signal) ----------------
    d["dip"] = ((d["RSI2"] < RSI_OS) | (d["z_band"] <= Z_BUY)).fillna(False)
    d["trigger"] = d["dip"]
    return d


# ----------------------------- single-name backtest -----------------------------
def swing_backtest(df: pd.DataFrame, capital: float = CAPITAL, stop_pct: float = STOP_PCT):
    """Buy next open when a dip triggers and we're flat. Exit on: hard stop
    (stop_pct), the regime-adaptive z-target, or the max-hold time cap."""
    d = compute_features(df)
    n = len(d)
    C = d["Close"].to_numpy(float); O = d["Open"].to_numpy(float); Z = d["z_band"].to_numpy(float)
    trig = d["trigger"].to_numpy(bool); tgt = d["exit_z_target"].to_numpy(float); date = d["Date"].to_numpy()

    trades = []; pos = None
    start = max(SMA_FAST, MOM_N) + 5
    for i in range(start, n - 1):
        if pos is None:
            if trig[i] and np.isfinite(Z[i]):
                pos = {"entry_date": date[i + 1], "entry_price": O[i + 1], "entry_i": i + 1,
                       "z_target": tgt[i]}
        else:
            held = i - pos["entry_i"]; ex, reason = False, ""
            if C[i] <= pos["entry_price"] * (1 - stop_pct):
                ex, reason = True, "stop"
            elif np.isfinite(Z[i]) and Z[i] >= pos["z_target"]:
                ex, reason = True, "z-target"
            elif held >= MAX_HOLD:
                ex, reason = True, "time"
            if ex:
                xp = O[i + 1]; ret = (xp - pos["entry_price"]) / pos["entry_price"]
                trades.append({**pos, "exit_date": date[i + 1], "exit_price": xp, "ret": ret,
                               "pnl": ret * capital, "bars": (i + 1) - pos["entry_i"], "reason": reason})
                pos = None
    if pos is not None:
        last = C[n - 1]; ret = (last - pos["entry_price"]) / pos["entry_price"]
        trades.append({**pos, "exit_date": date[n - 1], "exit_price": last, "ret": ret,
                       "pnl": ret * capital, "bars": (n - 1) - pos["entry_i"], "reason": "open"})
    return d, pd.DataFrame(trades)


def position_state(d: pd.DataFrame, trades: pd.DataFrame, stop_pct: float = STOP_PCT) -> dict:
    """Where does the MODEL stand on this name *right now*? Derived from the
    backtest so SELL/HOLD only mean something when there's an actual position.
      FLAT    - not in a trade (a fresh dip here => BUY)
      HOLDING - entered on a prior dip and still riding (winner or not yet stopped)
      SOLD    - a position just exited on the latest bar (stop = wrong buy; or
                z-target = thesis complete). This is the only time SELL matters.
    """
    if trades is None or len(trades) == 0:
        return {"state": "FLAT"}
    close = float(d["Close"].iloc[-1])
    zval = d["z_band"].iloc[-1]
    z = float(zval) if pd.notna(zval) else float("nan")
    last = trades.iloc[-1]

    if last["reason"] == "open":
        entry = float(last["entry_price"]); gain = (close - entry) / entry * 100.0
        return {"state": "HOLDING", "entry_price": round(entry, 2),
                "entry_date": str(pd.Timestamp(last["entry_date"]).date()),
                "gain_%": round(gain, 2), "bars_held": int(last["bars"]),
                "z_target": round(float(last["z_target"]), 1),
                "z_now": round(z, 2) if z == z else None}

    matches = d.index[d["Date"] == last["exit_date"]]
    sold_recently = len(matches) and matches[-1] >= len(d) - 2   # exited on last / 2nd-last bar
    if sold_recently:
        return {"state": "SOLD", "exit_reason": str(last["reason"]),
                "exit_date": str(pd.Timestamp(last["exit_date"]).date()),
                "ret_%": round(float(last["ret"]) * 100.0, 2),
                "entry_price": round(float(last["entry_price"]), 2)}
    return {"state": "FLAT"}


def compute_stats(t: pd.DataFrame, capital: float = CAPITAL) -> dict:
    z = {"Total Trades": 0, "Win Rate %": 0, "Total P&L $": 0, "Avg Win $": 0, "Avg Loss $": 0,
         "Profit Factor": 0, "Expectancy $": 0, "Avg Bars Held": 0, "Max Drawdown $": 0, "Return/Trade %": 0}
    if t is None or t.empty:
        return z
    w = t[t.pnl > 0]; l = t[t.pnl <= 0]
    gp = w.pnl.sum(); gl = abs(l.pnl.sum())
    eq = t.pnl.cumsum(); dd = (eq - eq.cummax()).min()
    return {"Total Trades": len(t),
            "Win Rate %": round(len(w) / len(t) * 100, 1),
            "Total P&L $": round(t.pnl.sum(), 2),
            "Avg Win $": round(w.pnl.mean(), 2) if len(w) else 0.0,
            "Avg Loss $": round(l.pnl.mean(), 2) if len(l) else 0.0,
            "Profit Factor": round(gp / gl, 2) if gl > 0 else float("inf"),
            "Expectancy $": round(t.pnl.mean(), 2),
            "Avg Bars Held": round(t.bars.mean(), 1),
            "Max Drawdown $": round(dd, 2),
            "Return/Trade %": round(t.ret.mean() * 100, 2)}


# ----------------------------- $100 portfolio backtest -----------------------------
def portfolio_backtest(history: dict, start_cash: float = 100.0, max_positions: int = 8,
                       stop_pct: float = STOP_PCT):
    """Give the strategy `start_cash` and trade it across the whole universe.
    Fixed-fraction sizing: each new trade gets 1/max_positions of current equity;
    at most `max_positions` concurrent positions. Uses each name's dip trades from
    swing_backtest (entry/exit dates + returns). Returns a summary + equity curve."""
    all_trades = []
    for tk, df in history.items():
        try:
            _, t = swing_backtest(df, stop_pct=stop_pct)
        except Exception:
            continue
        for _, r in t.iterrows():
            if r["reason"] == "open":
                continue   # ignore trades still open at the end
            all_trades.append((pd.Timestamp(r["entry_date"]), pd.Timestamp(r["exit_date"]),
                               float(r["ret"]), tk))
    all_trades.sort(key=lambda x: x[0])

    cash = start_cash; heap = []      # (exit_date, amount, ret, ticker)
    realized = []; curve = []
    def _equity():
        return cash + sum(a for _, a, _, _ in heap)

    for edt, xdt, ret, tk in all_trades:
        while heap and heap[0][0] <= edt:
            xd, amt, r, t2 = heapq.heappop(heap); cash += amt * (1 + r)
            realized.append({"ticker": t2, "exit": xd, "ret": r}); curve.append((xd, cash + sum(a for _, a, _, _ in heap)))
        if len(heap) < max_positions:
            amt = _equity() / max_positions
            if 0 < amt <= cash:
                cash -= amt; heapq.heappush(heap, (xdt, amt, ret, tk))
    while heap:
        xd, amt, r, t2 = heapq.heappop(heap); cash += amt * (1 + r)
        realized.append({"ticker": t2, "exit": xd, "ret": r}); curve.append((xd, cash + sum(a for _, a, _, _ in heap)))

    rr = pd.DataFrame(realized)
    eq = pd.DataFrame(curve, columns=["date", "equity"]).sort_values("date").reset_index(drop=True)
    final = round(float(eq["equity"].iloc[-1]), 2) if len(eq) else start_cash
    if len(eq) > 1:
        yrs = max((eq["date"].iloc[-1] - eq["date"].iloc[0]).days / 365.25, 0.25)
        cagr = round(((final / start_cash) ** (1 / yrs) - 1) * 100, 1)
        peak = eq["equity"].cummax(); maxdd = round(float(((eq["equity"] - peak) / peak).min() * 100), 1)
    else:
        cagr = 0.0; maxdd = 0.0
    return {
        "start_$": start_cash, "final_$": final,
        "return_%": round((final / start_cash - 1) * 100, 1),
        "CAGR_%": cagr, "max_drawdown_%": maxdd,
        "trades": len(rr), "win_rate_%": round((rr["ret"] > 0).mean() * 100, 1) if len(rr) else 0.0,
        "avg_trade_%": round(rr["ret"].mean() * 100, 2) if len(rr) else 0.0,
        "max_positions": max_positions, "stop_pct": stop_pct,
        "equity_curve": eq,
    }


# ----------------------------- live signal -----------------------------
def _fnum(v, nd=2, default=float("nan")):
    try:
        f = float(v)
        return round(f, nd) if np.isfinite(f) else default
    except (TypeError, ValueError):
        return default


def _band_read(z: float) -> str:
    if not np.isfinite(z):
        return "n/a"
    if z <= -2.5: return f"{z:.1f} sigma below band - very stretched, strong bounce zone"
    if z <= Z_BUY: return f"{z:.1f} sigma below band - stretched, buy zone"
    if z <= -0.5: return f"{z:.1f} sigma below band - pulling back toward band"
    if z < 0.5:   return "at the band"
    return f"+{z:.1f} sigma above band - riding above support"


def _target_label(t: float) -> str:
    if t >= Z_EXIT_STRONG: return "z>=+1.5 (ride momentum)"
    if t >= Z_EXIT_MID:    return "z>=+0.5"
    return "z>=0 (quick bounce)"


def live_signal(df: pd.DataFrame) -> dict:
    d = compute_features(df)
    r = d.iloc[-1]
    c = float(r["Close"]); bb = float(r["band_bot"]); bt = float(r["band_top"])
    z = float(r["z_band"]) if np.isfinite(r["z_band"]) else float("nan")

    if c < bb:   pos_vs_band = "below"
    elif c > bt: pos_vs_band = "above"
    else:        pos_vs_band = "inside"

    return {
        "date": str(pd.Timestamp(r["Date"]).date()),
        "close": _fnum(c), "band_bot": _fnum(bb), "band_top": _fnum(bt),
        "band_mid": _fnum(r["band_mid"]), "pos_vs_band": pos_vs_band,
        "score": _fnum(r["score"], 1),
        "rsi2": _fnum(r["RSI2"], 1), "rsi14": _fnum(r["RSI14"], 1),
        "z_band": _fnum(z, 2),
        "dist_band_%": _fnum(r["dist_band_%"], 2),
        "vol_surge": _fnum(r["vol_surge"], 2),
        "up_close": bool(r["up_close"]), "obv_rising": bool(r["obv_rising"]),
        "above_50": bool(r["above_50"]), "sma20_up": bool(r["sma20_up"]),
        "mom_63_%": _fnum(r["mom_63_%"], 1),
        "dip": bool(r["dip"]), "trigger": bool(r["trigger"]),
        "exit_z_target": _fnum(r["exit_z_target"], 1),
        "exit_plan": _target_label(float(r["exit_z_target"])),
        "band_read": _band_read(z),
        "s_oversold": _fnum(r["c_oversold"] * 100, 0), "s_stretch": _fnum(r["c_stretch"] * 100, 0),
        "s_volume": _fnum(r["c_volume"] * 100, 0), "s_reversal": _fnum(r["c_reversal"] * 100, 0),
        "s_trend": _fnum(r["c_trend"] * 100, 0),
    }
