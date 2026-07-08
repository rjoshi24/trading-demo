"""
quant_core.py
=============
A simple, research-grounded **composite swing model** for the WSB screener.

It runs on **daily** candles (so you can open it every day) and is tuned for a
**swing horizon of >= 10 trading days**. Every ticker gets a single transparent
0-100 score built from a handful of well-documented signals, plus a clear
BUY / CLOSE-TO-BUY / HOLD / SELL bucket and a swing backtest that *enforces the
>=10-day hold* so you can judge each name's historical quality.

Why these signals (the "quant paper" grounding)
------------------------------------------------
* **Golden Cross regime (50 / 200 SMA) + long-MA trend filter.**
  A price-above-long-moving-average filter historically cuts drawdowns and keeps
  you on the right side of the trend (Faber 2007, "A Quantitative Approach to
  Tactical Asset Allocation"). The 50>200 "golden cross" is the classic
  medium/long bullish regime.
* **Bull Market Support Band (20 SMA + 21 EMA).**
  The same support band used on the weekly BMSB chart; on daily bars it is a
  short-term trend-support that swing entries lean on. band_top = max(20SMA,21EMA),
  band_bot = min(...).
* **Time-series (trend) momentum, 12-1 month.**
  Past 1-12 month returns predict the next move (Moskowitz, Ooi & Pedersen 2012,
  "Time Series Momentum"; Jegadeesh & Titman 1993). We use the 12-month return
  skipping the most recent month.
* **Volatility squeeze (Bollinger inside Keltner = TTM Squeeze).**
  Volatility contraction precedes large directional moves (Bollinger; John
  Carter's TTM Squeeze). This is the "fire before the big move happens" piece.
* **Donchian 20-day breakout + volume confirmation.**
  Coiling just under a 20-day high that then breaks on rising volume is the
  classic trend-ignition setup (Turtle traders).
* **RSI(14) & MACD(12,26,9)** as momentum confirmation / overbought guard.

Nothing here is a big parameter sweep: it uses ONE fixed, sensible parameter set.
That keeps it simple and much less curve-fit than a per-ticker optimizer.

    Research only, not financial advice.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

# ----------------------------- fixed parameters -----------------------------
CAPITAL       = 1000.0

BAND_SMA      = 20      # bull-market support band
BAND_EMA      = 21
SMA_FAST      = 50      # golden cross
SMA_SLOW      = 200
RSI_N         = 14
MACD_FAST, MACD_SLOW, MACD_SIG = 12, 26, 9
BB_N, BB_K    = 20, 2.0
KC_N, KC_MULT = 20, 1.5     # Keltner channel for the TTM squeeze
ATR_N         = 14
DONCHIAN_N    = 20      # breakout channel (Turtle-style)
MOM_LOOKBACK  = 252     # 12-1 month time-series momentum
MOM_SKIP      = 21
MOM_FALLBACK  = 63      # 3-month momentum if <1y history
SQUEEZE_LB    = 126     # ~6 months for the bandwidth percentile

# swing backtest / hold horizon
MIN_HOLD      = 10      # >= 10 trading days, per the requirement
MAX_HOLD      = 60
ATR_TRAIL     = 3.0     # ATR-multiple trailing stop
HARD_STOP_PCT = 0.10    # emergency stop (can fire before MIN_HOLD)

# bucketing thresholds
BUY_MIN       = 60.0    # composite score needed for a fresh BUY
NEAR_MIN      = 52.0    # composite score needed for CLOSE-TO-BUY
NEAR_PCT      = 4.0     # within this % of the 20-day high => "coiling near breakout"

# component weights (sum to 1.0) -- keep transparent
W_REGIME   = 0.22
W_BAND     = 0.13
W_MOM      = 0.18
W_MACD     = 0.10
W_RSI      = 0.10
W_SQUEEZE  = 0.15
W_BREAKOUT = 0.12


# ----------------------------- indicators -----------------------------
def rsi(series: pd.Series, n: int = RSI_N) -> pd.Series:
    d = series.diff()
    up = d.clip(lower=0).rolling(n).mean()
    dn = (-d.clip(upper=0)).rolling(n).mean()
    rs = up / dn.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def atr(df: pd.DataFrame, n: int = ATR_N) -> pd.Series:
    h, l, c = df["High"], df["Low"], df["Close"]
    pc = c.shift(1)
    tr = pd.concat([(h - l), (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def _obv(close: pd.Series, vol: pd.Series) -> pd.Series:
    sign = np.sign(close.diff().fillna(0.0))
    return (sign * vol).cumsum()


def compute_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add every indicator + the composite score, entry trigger and exit flag
    as columns. Rows are NOT dropped (200-SMA would nuke the early history);
    NaNs are handled gracefully downstream."""
    d = df.copy().reset_index(drop=True)
    c = d["Close"]

    # --- support band (20 SMA / 21 EMA) ---
    d["SMA20"] = c.rolling(BAND_SMA).mean()
    d["EMA21"] = c.ewm(span=BAND_EMA, adjust=False).mean()
    d["band_top"] = d[["SMA20", "EMA21"]].max(axis=1)
    d["band_bot"] = d[["SMA20", "EMA21"]].min(axis=1)

    # --- golden cross regime ---
    d["SMA50"] = c.rolling(SMA_FAST).mean()
    d["SMA200"] = c.rolling(SMA_SLOW).mean()
    d["golden"] = d["SMA50"] > d["SMA200"]
    d["sma50_rising"] = d["SMA50"] > d["SMA50"].shift(10)
    # regime_ok: price above the long trend filter (fall back to 50 SMA if <200 bars)
    d["regime_ok"] = np.where(d["SMA200"].notna(), c > d["SMA200"], c > d["SMA50"])

    # --- RSI / MACD ---
    d["RSI"] = rsi(c, RSI_N)
    ema_fast = c.ewm(span=MACD_FAST, adjust=False).mean()
    ema_slow = c.ewm(span=MACD_SLOW, adjust=False).mean()
    d["MACD"] = ema_fast - ema_slow
    d["MACD_sig"] = d["MACD"].ewm(span=MACD_SIG, adjust=False).mean()
    d["MACD_hist"] = d["MACD"] - d["MACD_sig"]

    # --- Bollinger + Keltner => TTM squeeze ---
    mid = c.rolling(BB_N).mean()
    sd = c.rolling(BB_N).std()
    d["BB_up"] = mid + BB_K * sd
    d["BB_lo"] = mid - BB_K * sd
    d["bandwidth"] = (d["BB_up"] - d["BB_lo"]) / mid.replace(0, np.nan)
    d["ATR"] = atr(d, ATR_N)
    kc_mid = c.ewm(span=KC_N, adjust=False).mean()
    d["squeeze_on"] = (d["BB_up"] < (kc_mid + KC_MULT * d["ATR"])) & \
                      (d["BB_lo"] > (kc_mid - KC_MULT * d["ATR"]))

    # --- Donchian breakout channel (prior N-bar high/low, excludes today) ---
    d["hh20"] = c.rolling(DONCHIAN_N).max().shift(1)
    d["ll20"] = c.rolling(DONCHIAN_N).min().shift(1)

    # --- time-series momentum (12-1), fall back to 3-month if short history ---
    mom = c.shift(MOM_SKIP) / c.shift(MOM_LOOKBACK) - 1.0
    mom_fb = c / c.shift(MOM_FALLBACK) - 1.0
    d["mom_12_1"] = mom.fillna(mom_fb)

    # --- volume ---
    d["avg_vol20"] = d["Volume"].rolling(BB_N).mean()
    d["vol_ratio"] = d["Volume"] / d["avg_vol20"].replace(0, np.nan)
    d["OBV"] = _obv(c, d["Volume"])
    d["obv_rising"] = d["OBV"] > d["OBV"].shift(5)

    # ---------------- component sub-scores (each 0..1) ----------------
    gap_below = (d["band_bot"] - c) / c            # >0 when price is below the band

    c_regime = (0.45 * d["regime_ok"].astype(float)
                + 0.35 * d["golden"].astype(float)
                + 0.20 * d["sma50_rising"].astype(float)).clip(0, 1)

    c_band = np.select(
        [c >= d["band_top"], c >= d["band_bot"]],
        [1.0, 0.7],
        default=np.clip(0.6 - gap_below * 10.0, 0, 1),
    )

    c_mom = np.clip(d["mom_12_1"] / 0.5, 0, 1)     # +50% over the year => full marks

    c_macd = 0.5 * (d["MACD_hist"] > 0).astype(float) \
        + 0.5 * (d["MACD_hist"] > d["MACD_hist"].shift(1)).astype(float)

    c_rsi = np.select(
        [d["RSI"] >= 70, d["RSI"] >= 60, d["RSI"] >= 50, d["RSI"] >= 45, d["RSI"] >= 40],
        [0.25, 0.90, 1.00, 0.75, 0.55],
        default=0.35,
    )

    # squeeze: low bandwidth percentile over ~6 months => more stored energy
    bw_min = d["bandwidth"].rolling(SQUEEZE_LB, min_periods=20).min()
    bw_max = d["bandwidth"].rolling(SQUEEZE_LB, min_periods=20).max()
    bw_norm = (d["bandwidth"] - bw_min) / (bw_max - bw_min)
    c_squeeze = np.maximum(np.clip(1 - bw_norm, 0, 1),
                           np.where(d["squeeze_on"], 0.85, 0.0))
    c_squeeze = pd.Series(c_squeeze, index=d.index).fillna(0.3)

    # breakout proximity + volume confirmation
    prox_high = (d["hh20"] - c) / c                # >=0 when below the 20-day high
    prox_score = np.clip(1 - prox_high * 15.0, 0, 1)
    vol_score = np.clip((d["vol_ratio"] - 1.0) / 1.0, 0, 1).fillna(0)
    c_breakout = 0.6 * prox_score + 0.4 * vol_score

    for name in ("c_regime", "c_band", "c_mom", "c_macd", "c_rsi", "c_squeeze", "c_breakout"):
        d[name] = pd.Series(np.asarray(locals()[name], dtype=float), index=d.index)

    d["score"] = 100.0 * (
        W_REGIME * d["c_regime"] + W_BAND * d["c_band"] + W_MOM * d["c_mom"]
        + W_MACD * d["c_macd"] + W_RSI * d["c_rsi"] + W_SQUEEZE * d["c_squeeze"]
        + W_BREAKOUT * d["c_breakout"]
    )

    # ---------------- entry trigger / exit flag ----------------
    breakout = c > d["hh20"]                                    # new 20-day closing high
    reclaim = (c.shift(1) < d["band_bot"].shift(1)) & (c > d["band_bot"])
    squeeze_break = d["squeeze_on"].shift(1).fillna(False) & (c > d["band_top"]) \
        & (d["bandwidth"] > d["bandwidth"].shift(1))
    d["breakout"] = breakout.fillna(False)
    d["reclaim"] = reclaim.fillna(False)
    d["squeeze_break"] = squeeze_break.fillna(False)
    d["trigger"] = (d["regime_ok"] & (d["breakout"] | d["reclaim"] | d["squeeze_break"])
                    & (d["RSI"] < 80))

    # Exit = a *fresh* reason to leave a swing long, not merely "weak".
    #   (a) lost the support band after having been above it in the last ~10 bars, or
    #   (b) a fresh death cross (was golden ~15 bars ago) with price below the 200-SMA.
    above_top = (c > d["band_top"])
    recently_above = above_top.shift(1).rolling(10, min_periods=1).max().fillna(0) > 0
    fresh_band_loss = recently_above & (c < d["band_bot"])
    death = d["SMA50"] < d["SMA200"]
    was_golden = d["golden"].shift(15).fillna(False)
    fresh_death = death & was_golden & (c < d["SMA200"])
    d["exit_flag"] = fresh_band_loss | fresh_death

    return d


# ----------------------------- swing backtest -----------------------------
def swing_backtest(df: pd.DataFrame, capital: float = CAPITAL):
    """Enter at next open when `trigger` fires and we're flat. Then HOLD for at
    least MIN_HOLD bars before taking a band/trailing exit (a hard stop can fire
    earlier for risk control). Returns (features_df, trades_df)."""
    d = compute_features(df)
    n = len(d)
    C = d["Close"].to_numpy(float); O = d["Open"].to_numpy(float)
    bb = d["band_bot"].to_numpy(float); A = d["ATR"].to_numpy(float)
    trig = d["trigger"].to_numpy(bool)
    date = d["Date"].to_numpy()

    trades = []
    pos = None
    start = max(SMA_FAST, BAND_EMA) + 1     # need the core indicators warmed up
    for i in range(start, n - 1):
        if pos is None:
            if trig[i]:
                pos = {"entry_date": date[i + 1], "entry_price": O[i + 1],
                       "entry_i": i + 1, "peak": C[i]}
        else:
            pos["peak"] = max(pos["peak"], C[i])
            held = i - pos["entry_i"]
            trail = pos["peak"] - ATR_TRAIL * A[i]
            exit_now, reason = False, ""
            if C[i] <= pos["entry_price"] * (1 - HARD_STOP_PCT):
                exit_now, reason = True, "hard-stop"
            elif held >= MIN_HOLD and C[i] < bb[i]:
                exit_now, reason = True, "band-loss"
            elif held >= MIN_HOLD and C[i] < trail:
                exit_now, reason = True, "atr-trail"
            elif held >= MAX_HOLD:
                exit_now, reason = True, "max-hold"
            if exit_now:
                ep = O[i + 1]; ret = (ep - pos["entry_price"]) / pos["entry_price"]
                trades.append({**pos, "exit_date": date[i + 1], "exit_price": ep,
                               "ret": ret, "pnl": ret * capital,
                               "bars": (i + 1) - pos["entry_i"], "reason": reason})
                pos = None
    if pos is not None:
        last = C[n - 1]; ret = (last - pos["entry_price"]) / pos["entry_price"]
        trades.append({**pos, "exit_date": date[n - 1], "exit_price": last,
                       "ret": ret, "pnl": ret * capital,
                       "bars": (n - 1) - pos["entry_i"], "reason": "open"})
    return d, pd.DataFrame(trades)


def compute_stats(t: pd.DataFrame, capital: float = CAPITAL) -> dict:
    z = {"Total Trades": 0, "Win Rate %": 0, "Total P&L $": 0, "Avg Win $": 0,
         "Avg Loss $": 0, "Profit Factor": 0, "Expectancy $": 0, "Avg Bars Held": 0,
         "Max Drawdown $": 0, "Return/Trade %": 0}
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


def live_signal(df: pd.DataFrame) -> dict:
    """Evaluate the composite model on the latest daily bar and return a flat
    dict of everything the screener needs (score, components, trigger, exit,
    proximity to the nearest actionable trigger)."""
    d = compute_features(df)
    r = d.iloc[-1]
    c = float(r["Close"]); bb = float(r["band_bot"]); bt = float(r["band_top"])

    if c < bb:
        pos_vs_band = "below"
    elif c > bt:
        pos_vs_band = "above"
    else:
        pos_vs_band = "inside"

    prox_high = (float(r["hh20"]) - c) / c * 100.0 if np.isfinite(r["hh20"]) else float("nan")
    gap_bot = (bb - c) / c * 100.0                 # >0 => below the band bottom

    # % move to the nearest actionable long trigger (new 20-day high OR band reclaim)
    candidates = [x for x in (prox_high, gap_bot) if np.isfinite(x) and x >= 0]
    need_move = min(candidates) if candidates else (prox_high if np.isfinite(prox_high) else 0.0)

    return {
        "date": str(pd.Timestamp(r["Date"]).date()),
        "close": _fnum(c), "band_bot": _fnum(bb), "band_top": _fnum(bt),
        "pos_vs_band": pos_vs_band,
        "score": _fnum(r["score"], 1),
        "regime_ok": bool(r["regime_ok"]),
        "golden": bool(r["golden"]),
        "rsi": _fnum(r["RSI"], 1),
        "macd_hist": _fnum(r["MACD_hist"], 3),
        "mom_12_1_%": _fnum(r["mom_12_1"] * 100, 1),
        "squeeze_on": bool(r["squeeze_on"]),
        "vol_ratio": _fnum(r["vol_ratio"], 2),
        "obv_rising": bool(r["obv_rising"]),
        "trigger": bool(r["trigger"]),
        "breakout": bool(r["breakout"]),
        "reclaim": bool(r["reclaim"]),
        "squeeze_break": bool(r["squeeze_break"]),
        "exit_flag": bool(r["exit_flag"]),
        "prox_high_%": _fnum(prox_high, 2),
        "need_move_%": _fnum(need_move, 2),
        # component breakdown (0-100 each, for transparency)
        "s_regime": _fnum(r["c_regime"] * 100, 0),
        "s_band": _fnum(r["c_band"] * 100, 0),
        "s_mom": _fnum(r["c_mom"] * 100, 0),
        "s_macd": _fnum(r["c_macd"] * 100, 0),
        "s_rsi": _fnum(r["c_rsi"] * 100, 0),
        "s_squeeze": _fnum(r["c_squeeze"] * 100, 0),
        "s_breakout": _fnum(r["c_breakout"] * 100, 0),
    }
