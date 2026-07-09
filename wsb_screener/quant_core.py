"""
quant_core.py
=============
**Snap-Back Swing Model** for the WSB screener (daily bars).

Rebuilt from an empirical study of swing setups over 6 years on 45 liquid names
(see the notebook's "Why this model" section). The winners, by win rate +
consistency + upside capture, were **mean-reversion dip buys** - NOT trend-gated
breakouts. So this model:

* **Has no 200-SMA gate** (it made signals appear once in a blue moon).
* Doesn't require price to be *above* the Bull-Market Support Band. Instead it
  measures how **stretched** price is from the band in **standard deviations**
  (`z_band`) - because stocks retrace, a name stretched below the band tends to
  snap back toward it, and a name stretched far above it tends to test/return to
  it. (e.g. MSFT selling to ~348, then bouncing back toward the band.)
* Uses a **volume surge** (buying volume N-fold above its 20-day average on an
  up day) as a bottom / buying-power confirmation - this measurably improved
  returns and profit factor in testing.
* Computes **many variables** but the BUY decision only uses the handful that
  actually mattered in testing: **RSI-2 oversold, std-dev stretch from the band,
  volume surge, a reversal up-close, and a *soft* (non-gating) trend context.**

Empirical result of the trigger below (rsi-snap-back exit, 6y, 45 tickers):
~**68% win rate**, fires several times/yr/ticker, ~5-day average hold.

    Research only, not financial advice.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

# ----------------------------- fixed parameters -----------------------------
CAPITAL     = 1000.0

BAND_SMA    = 20        # Bull-Market Support Band = 20 SMA / 21 EMA
BAND_EMA    = 21
SMA_FAST    = 50        # soft trend context + backtest warm-up (NOT a gate)
RSI_FAST    = 2         # Connors RSI-2 (the mean-reversion oscillator)
RSI_SLOW    = 14        # informational
ATR_N       = 14
VOL_N       = 20        # volume average window
MOM_N       = 63        # ~3-month momentum (informational / soft)

# dip / stretch thresholds
Z_BUY       = -1.5      # >= this many std-devs below the band = a dip worth buying
Z_DEEP      = -2.5      # very stretched below the band
Z_EXTENDED  = 2.0       # this far ABOVE the band = extended, expect a retrace
RSI_OS      = 10.0      # RSI-2 oversold
RSI_OS_SOFT = 25.0      # "getting oversold" (close-to-buy)
RSI_EXIT    = 70.0      # RSI-2 reverted = take profit
VOL_SURGE   = 1.5       # volume >= 1.5x its 20-day average = buying-power surge
VOL_SOFT    = 1.2

# swing backtest exit
EXIT_MODE   = "snapback"   # "snapback" (high win rate) | "swing" (let winners run)
STOP_PCT    = 0.08
MAX_HOLD    = 20
SWING_TGT   = 0.10
SWING_STOP  = 0.07

# bucket thresholds
BUY_MIN     = 50.0
NEAR_MIN    = 42.0
NEAR_PCT    = 4.0          # kept for API compatibility

# component weights (sum to 1.0)
W_OVERSOLD  = 0.28
W_STRETCH   = 0.24
W_VOLUME    = 0.18
W_REVERSAL  = 0.12
W_TREND     = 0.18


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


def compute_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add every indicator + the composite score + trigger/exit columns. Rows
    are not dropped; NaNs are handled downstream."""
    d = df.copy().reset_index(drop=True)
    c = d["Close"]

    # --- moving averages + support band ---
    d["SMA5"]  = c.rolling(5).mean()
    d["SMA10"] = c.rolling(10).mean()
    d["SMA20"] = c.rolling(BAND_SMA).mean()
    d["EMA21"] = c.ewm(span=BAND_EMA, adjust=False).mean()
    d["SMA50"] = c.rolling(SMA_FAST).mean()
    d["band_mid"] = (d["SMA20"] + d["EMA21"]) / 2
    d["band_top"] = d[["SMA20", "EMA21"]].max(axis=1)
    d["band_bot"] = d[["SMA20", "EMA21"]].min(axis=1)

    # --- stretch from the band, in standard deviations (the key mean-reversion gauge) ---
    d["std20"] = c.rolling(BAND_SMA).std()
    d["z_band"] = (c - d["band_mid"]) / d["std20"].replace(0, np.nan)
    d["ATR"] = atr(d, ATR_N)
    d["dist_band_%"] = (c - d["band_mid"]) / c * 100.0
    d["dist_band_atr"] = (c - d["band_mid"]) / d["ATR"].replace(0, np.nan)

    # --- oscillators ---
    d["RSI2"] = rsi(c, RSI_FAST)
    d["RSI14"] = rsi(c, RSI_SLOW)

    # --- volume / buying power ---
    d["avg_vol20"] = d["Volume"].rolling(VOL_N).mean()
    d["vol_surge"] = d["Volume"] / d["avg_vol20"].replace(0, np.nan)
    d["OBV"] = _obv(c, d["Volume"])
    d["obv_rising"] = d["OBV"] > d["OBV"].shift(5)
    d["up_close"] = c > c.shift(1)

    # --- soft trend context (NOT a gate) ---
    d["above_50"] = c > d["SMA50"]
    d["sma20_up"] = d["SMA20"] > d["SMA20"].shift(5)
    d["above_band"] = c > d["band_bot"]
    d["mom_63_%"] = (c / c.shift(MOM_N) - 1.0) * 100.0

    # ---------------- component sub-scores (each 0..1) ----------------
    r2 = d["RSI2"]
    c_oversold = np.select(
        [r2 <= 5, r2 <= 10, r2 <= 20, r2 <= 30, r2 <= 45],
        [1.00, 0.85, 0.60, 0.40, 0.20], default=0.05)

    z = d["z_band"]
    c_stretch = np.select(
        [z <= Z_DEEP, z <= -2.0, z <= Z_BUY, z <= -1.0, z <= -0.5, z <= 1.0, z <= 1.75],
        [1.00, 0.90, 0.75, 0.55, 0.35, 0.18, 0.05], default=0.0)   # far above band => 0 (not a dip)

    vs = d["vol_surge"]
    vbase = np.select([vs >= 2.0, vs >= VOL_SURGE, vs >= VOL_SOFT], [1.0, 0.8, 0.5], default=0.2)
    c_volume = np.clip(vbase * np.where(d["up_close"], 1.0, 0.7), 0, 1)   # buying > selling volume

    c_reversal = 0.5 * d["up_close"].astype(float) + 0.5 * (r2 > r2.shift(1)).astype(float)

    c_trend = (0.4 * d["above_50"].astype(float)
               + 0.3 * d["sma20_up"].astype(float)
               + 0.3 * d["above_band"].astype(float)).clip(0, 1)

    for nm, arr in (("c_oversold", c_oversold), ("c_stretch", c_stretch), ("c_volume", c_volume),
                    ("c_reversal", c_reversal), ("c_trend", c_trend)):
        d[nm] = pd.Series(np.asarray(arr, dtype=float), index=d.index).fillna(0.0)

    d["score"] = 100.0 * (
        W_OVERSOLD * d["c_oversold"] + W_STRETCH * d["c_stretch"] + W_VOLUME * d["c_volume"]
        + W_REVERSAL * d["c_reversal"] + W_TREND * d["c_trend"])

    # ---------------- trigger / exit (no 200-SMA, no "must be above band") ----------------
    # A dip = oversold (RSI-2 < 10) OR stretched >= 1.5 sigma below the band.
    # That's the whole trigger -- Connors-style, we buy the oversold bar itself (enter
    # next open), no up-close/volume gate required (testing showed the edge holds ~68%
    # without it, and requiring a confirm bar is what made signals rare). Volume surge
    # and up-close still feed the score + ranking, they just don't BLOCK the trigger.
    # The screener then surfaces only names with a proven historical snap-back win rate,
    # so the BUY list is both frequent AND high win rate.
    dip = (d["RSI2"] < RSI_OS) | (d["z_band"] <= Z_BUY)
    d["dip"] = dip.fillna(False)
    d["trigger"] = d["dip"]

    # reverted / extended => take profit / exit
    d["exit_flag"] = (d["RSI2"] > RSI_EXIT) | (d["z_band"] >= Z_EXTENDED)

    return d


# ----------------------------- swing backtest -----------------------------
def swing_backtest(df: pd.DataFrame, capital: float = CAPITAL, exit_mode: str = EXIT_MODE):
    """Enter next open when `trigger` fires and flat. Exit per `exit_mode`:
      snapback - RSI2 reverts (> RSI_EXIT) or price closes back above the 5-SMA
                 (Connors-style mean-reversion exit; high win rate)
      swing    - fixed profit target / stop / time (lets winners run)
    A protective stop and a max-hold cap apply either way."""
    d = compute_features(df)
    n = len(d)
    C = d["Close"].to_numpy(float); O = d["Open"].to_numpy(float); Hg = d["High"].to_numpy(float)
    SMA5 = d["SMA5"].to_numpy(float); R2 = d["RSI2"].to_numpy(float)
    trig = d["trigger"].to_numpy(bool); date = d["Date"].to_numpy()

    trades = []; pos = None
    start = max(SMA_FAST, BAND_EMA) + 5
    for i in range(start, n - 1):
        if pos is None:
            if trig[i]:
                pos = {"entry_date": date[i + 1], "entry_price": O[i + 1], "entry_i": i + 1, "peak": C[i]}
        else:
            pos["peak"] = max(pos["peak"], Hg[i]); held = i - pos["entry_i"]
            ex, reason = False, ""
            if C[i] <= pos["entry_price"] * (1 - STOP_PCT):
                ex, reason = True, "stop"
            elif exit_mode == "swing":
                if C[i] >= pos["entry_price"] * (1 + SWING_TGT): ex, reason = True, "target"
                elif held >= MAX_HOLD: ex, reason = True, "time"
            else:  # snapback
                if held >= 1 and (R2[i] > RSI_EXIT or C[i] > SMA5[i]): ex, reason = True, "reverted"
                elif held >= MAX_HOLD: ex, reason = True, "time"
            if ex:
                ep = O[i + 1]; ret = (ep - pos["entry_price"]) / pos["entry_price"]
                trades.append({**pos, "exit_date": date[i + 1], "exit_price": ep, "ret": ret,
                               "pnl": ret * capital, "bars": (i + 1) - pos["entry_i"], "reason": reason})
                pos = None
    if pos is not None:
        last = C[n - 1]; ret = (last - pos["entry_price"]) / pos["entry_price"]
        trades.append({**pos, "exit_date": date[n - 1], "exit_price": last, "ret": ret,
                       "pnl": ret * capital, "bars": (n - 1) - pos["entry_i"], "reason": "open"})
    return d, pd.DataFrame(trades)


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
    if z <= Z_DEEP:   return f"{z:.1f} sigma below band - very stretched, snap-back likely"
    if z <= Z_BUY:    return f"{z:.1f} sigma below band - stretched, bounce zone"
    if z <= -0.5:     return f"{z:.1f} sigma below band - pulling back toward band"
    if z < 0.5:       return "at the band"
    if z < Z_EXTENDED:return f"+{z:.1f} sigma above band - riding above support"
    return f"+{z:.1f} sigma above band - extended, may retrace/test the band"


def live_signal(df: pd.DataFrame) -> dict:
    d = compute_features(df)
    r = d.iloc[-1]
    c = float(r["Close"]); bb = float(r["band_bot"]); bt = float(r["band_top"])
    z = float(r["z_band"]) if np.isfinite(r["z_band"]) else float("nan")

    if c < bb:      pos_vs_band = "below"
    elif c > bt:    pos_vs_band = "above"
    else:           pos_vs_band = "inside"

    return {
        "date": str(pd.Timestamp(r["Date"]).date()),
        "close": _fnum(c), "band_bot": _fnum(bb), "band_top": _fnum(bt),
        "band_mid": _fnum(r["band_mid"]), "pos_vs_band": pos_vs_band,
        "score": _fnum(r["score"], 1),
        "rsi2": _fnum(r["RSI2"], 1),
        "rsi14": _fnum(r["RSI14"], 1),
        "z_band": _fnum(z, 2),
        "dist_band_%": _fnum(r["dist_band_%"], 2),
        "dist_band_atr": _fnum(r["dist_band_atr"], 2),
        "vol_surge": _fnum(r["vol_surge"], 2),
        "up_close": bool(r["up_close"]),
        "obv_rising": bool(r["obv_rising"]),
        "above_50": bool(r["above_50"]),
        "sma20_up": bool(r["sma20_up"]),
        "mom_63_%": _fnum(r["mom_63_%"], 1),
        "dip": bool(r["dip"]),
        "trigger": bool(r["trigger"]),
        "exit_flag": bool(r["exit_flag"]),
        "band_read": _band_read(z),
        # component breakdown (0-100 each)
        "s_oversold": _fnum(r["c_oversold"] * 100, 0),
        "s_stretch": _fnum(r["c_stretch"] * 100, 0),
        "s_volume": _fnum(r["c_volume"] * 100, 0),
        "s_reversal": _fnum(r["c_reversal"] * 100, 0),
        "s_trend": _fnum(r["c_trend"] * 100, 0),
    }
