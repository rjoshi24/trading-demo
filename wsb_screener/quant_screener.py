"""
quant_screener.py
=================
Runs the **Snap-Back Swing Model** (`quant_core.py`) across many tickers on
daily candles and sorts each name into an actionable bucket. Open it every day.

Per ticker:
  1. Compute all indicators + the 0-100 composite score  (compute_features)
  2. Read the live signal on the latest bar                (live_signal)
  3. Run the snap-back swing backtest for quality stats    (swing_backtest)
  4. Assign a bucket

Buckets (mean-reversion framing - no 200-SMA, no "must be above band"):
  BUY NOW           - a dip trigger fired today: oversold (RSI-2) and/or stretched
                      >=1.5 sigma below the band, confirmed by an up-close / volume
                      surge, with a high composite score
  CLOSE TO BUY      - getting oversold / stretched toward the buy zone, not fired yet
  HOLD              - constructive uptrend, not a fresh dip and not extended
  TAKE PROFIT / SELL- reverted (RSI-2 > 70) or extended >= +2 sigma above the band
  WATCH             - neutral / low score
  SKIPPED           - not enough clean price history
"""
from __future__ import annotations
import pandas as pd

from .quant_core import (
    compute_features, live_signal, swing_backtest, compute_stats,
    NEAR_MIN, RSI_OS_SOFT, Z_BUY, SMA_FAST, VOL_N,
)

MIN_BARS = SMA_FAST + VOL_N + 15     # ~85 bars: enough to warm up the indicators

# quality gate: only surface a fresh dip as BUY NOW if this name has historically
# snapped back reliably (enough trades + a high win rate). This is what makes the
# BUY list both frequent (dips fire often) AND high win rate (only proven names).
MIN_BT_TRADES   = 8
STRONG_WINRATE  = 58.0
OK_WINRATE      = 48.0


def _dip_reasons(sig: dict) -> str:
    bits = []
    if sig["rsi2"] <= 10:
        bits.append(f"RSI-2 {sig['rsi2']:.0f} (oversold)")
    if (sig["z_band"] == sig["z_band"]) and sig["z_band"] <= Z_BUY:
        bits.append(f"{sig['z_band']:.1f} sigma below band")
    if (sig["vol_surge"] == sig["vol_surge"]) and sig["vol_surge"] >= 1.5:
        bits.append(f"vol {sig['vol_surge']:.1f}x (buyers)")
    return ", ".join(bits or ["dip + reversal confirm"])


def _bucket(sig: dict, st: dict) -> tuple[str, str]:
    score = sig["score"]
    if not (score == score):        # NaN guard
        return "SKIPPED", "indicators not ready"

    wr = st["Win Rate %"]; nt = st["Total Trades"]
    proven = nt >= MIN_BT_TRADES

    # 1) fresh dip trigger today -> tier by this name's historical snap-back win rate
    if sig["trigger"]:
        reasons = _dip_reasons(sig)
        if proven and wr >= STRONG_WINRATE:
            return "BUY NOW", f"dip buy ({wr:.0f}% hist. win): {reasons} (act at next open)"
        if (not proven) or wr >= OK_WINRATE:
            edge = f"{wr:.0f}% hist. win" if proven else "unproven history"
            return "CLOSE TO BUY", f"dip fired ({edge}): {reasons} -- lower-conviction"
        return "WATCH", f"dip fired but weak edge ({wr:.0f}% hist. win): {reasons}"

    # 2) reverted / extended => take profit / trim
    if sig["exit_flag"]:
        why = f"RSI-2 {sig['rsi2']:.0f} reverted" if sig["rsi2"] > 70 else f"{sig['z_band']:.1f} sigma above band (extended)"
        return "TAKE PROFIT / SELL", f"exit signal: {why}"

    # 3) building toward a dip buy (approaching the zone, not fired yet)
    getting_oversold = sig["rsi2"] <= RSI_OS_SOFT
    stretching = (sig["z_band"] == sig["z_band"]) and sig["z_band"] <= -1.0
    if (getting_oversold or stretching) and score >= NEAR_MIN:
        note = []
        if getting_oversold: note.append(f"RSI-2 {sig['rsi2']:.0f} sliding into oversold")
        if stretching:       note.append(f"{sig['z_band']:.1f} sigma below band")
        return "CLOSE TO BUY", "; ".join(note) + " -- watch for the up-close/volume confirm"

    # 4) constructive but no fresh dip
    if sig["above_50"] or sig["sma20_up"]:
        return "HOLD", "constructive uptrend, no fresh dip; hold / wait for a pullback"

    return "WATCH", "neutral -- no dip, no trend edge"


def screen_ticker(ticker: str, daily: pd.DataFrame, meta: dict | None = None) -> dict:
    meta = meta or {}
    base = {"ticker": ticker, "name": meta.get("name", ""),
            "wsb_rank": meta.get("rank"), "mentions": meta.get("mentions")}

    if daily is None or len(daily) < MIN_BARS:
        return {**base, "group": "SKIPPED", "note": "insufficient price history",
                "bars": 0 if daily is None else len(daily)}

    sig = live_signal(daily)
    try:
        _, trades = swing_backtest(daily)
        st = compute_stats(trades)
    except Exception:
        st = compute_stats(None)

    group, note = _bucket(sig, st)

    return {
        **base,
        "group": group,
        "score": sig["score"],
        "close": sig["close"],
        "rsi2": sig["rsi2"],
        "rsi14": sig["rsi14"],
        "z_band": sig["z_band"],
        "dist_band_%": sig["dist_band_%"],
        "dist_band_atr": sig["dist_band_atr"],
        "vol_surge": sig["vol_surge"],
        "up_close": sig["up_close"],
        "obv_rising": sig["obv_rising"],
        "above_50": sig["above_50"],
        "sma20_up": sig["sma20_up"],
        "mom_63_%": sig["mom_63_%"],
        "pos_vs_band": sig["pos_vs_band"],
        "band_bot": sig["band_bot"],
        "band_top": sig["band_top"],
        "band_read": sig["band_read"],
        "dip": sig["dip"],
        "trigger": sig["trigger"],
        "exit_flag": sig["exit_flag"],
        # component breakdown
        "s_oversold": sig["s_oversold"], "s_stretch": sig["s_stretch"], "s_volume": sig["s_volume"],
        "s_reversal": sig["s_reversal"], "s_trend": sig["s_trend"],
        # backtest quality
        "bt_trades": st["Total Trades"],
        "bt_winrate_%": st["Win Rate %"],
        "bt_pnl_$": st["Total P&L $"],
        "bt_profit_factor": st["Profit Factor"],
        "bt_expectancy_$": st["Expectancy $"],
        "bt_avg_bars": st["Avg Bars Held"],
        "signal_date": sig["date"],
        "bars": len(daily),
        "note": note,
    }


GROUP_ORDER = ["BUY NOW", "CLOSE TO BUY", "HOLD", "TAKE PROFIT / SELL", "WATCH", "SKIPPED"]


def rank_group(g_df: pd.DataFrame, group: str) -> pd.DataFrame:
    if group == "BUY NOW":
        # highest historical win rate first, then score, then a volume-surge tiebreak
        return g_df.sort_values(["bt_winrate_%", "score", "vol_surge"], ascending=[False, False, False])
    if group == "CLOSE TO BUY":
        return g_df.sort_values(["bt_winrate_%", "score"], ascending=[False, False])
    if group == "TAKE PROFIT / SELL":
        return g_df.sort_values("rsi2", ascending=False)
    if group == "WATCH":
        return g_df.sort_values("score", ascending=False)
    if group == "SKIPPED":
        return g_df.sort_values("mentions", ascending=False, na_position="last")
    # HOLD -> best score, then backtest expectancy
    return g_df.sort_values(["score", "bt_expectancy_$"], ascending=[False, False])


def run_screener(history: dict, metas: dict, progress_every: int = 25) -> pd.DataFrame:
    rows = []
    tickers = list(metas.keys())
    for i, tk in enumerate(tickers, 1):
        try:
            rows.append(screen_ticker(tk, history.get(tk), metas.get(tk)))
        except Exception as e:
            m = metas.get(tk, {})
            rows.append({"ticker": tk, "name": m.get("name", ""), "wsb_rank": m.get("rank"),
                         "mentions": m.get("mentions"), "group": "SKIPPED", "note": f"error: {e!r}"})
        if progress_every and i % progress_every == 0:
            print(f"  ...screened {i}/{len(tickers)}")
    df = pd.DataFrame(rows)

    parts = []
    for g in GROUP_ORDER:
        sub = df[df["group"] == g]
        if not sub.empty:
            parts.append(rank_group(sub, g))
    ordered = pd.concat(parts, ignore_index=True) if parts else df
    ordered.insert(0, "group_rank", ordered.groupby("group").cumcount() + 1)
    return ordered
