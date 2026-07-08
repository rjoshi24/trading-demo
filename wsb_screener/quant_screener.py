"""
quant_screener.py
=================
Runs the composite swing model from `quant_core.py` across many tickers (daily
candles) and sorts every name into an actionable bucket. Designed to be opened
**every day**: refresh the data, re-run, read the top of each bucket.

Per ticker (daily candles, ~3y history):
  1. Compute all indicators + the 0-100 composite score  (compute_features)
  2. Read the live signal on the latest bar                (live_signal)
  3. Run the >=10-day-hold swing backtest for quality stats (swing_backtest)
  4. Assign a bucket from regime / score / trigger / exit

Buckets:
  BUY NOW        - regime bullish, a fresh entry trigger fired today and score is high
  CLOSE TO BUY   - regime bullish, score high, setup building (squeeze / coiling
                   near the 20-day high / reclaiming the band) but not fired yet
  HOLD (UPTREND) - regime bullish, already trending above the band (no fresh entry)
  SELL / EXIT    - exit condition present (lost the support band, or death cross)
  WATCH          - everything else / low score
  SKIPPED        - not enough clean price history
"""
from __future__ import annotations
import pandas as pd

from .quant_core import (
    compute_features, live_signal, swing_backtest, compute_stats,
    BUY_MIN, NEAR_MIN, NEAR_PCT, SMA_SLOW, SMA_FAST, BAND_SMA,
)

MIN_BARS = SMA_FAST + BAND_SMA + 10     # need the core indicators warmed up (~80 bars)


def _bucket(sig: dict) -> tuple[str, str]:
    """Return (group, note) from the live signal dict."""
    score = sig["score"]
    if not (score == score):        # NaN guard
        return "SKIPPED", "indicators not ready"

    # 1) exit takes priority -- if you hold it, this says get out
    if sig["exit_flag"]:
        why = "lost the support band" if sig["pos_vs_band"] == "below" else "death cross / below 200-SMA"
        return "SELL / EXIT", f"exit signal: {why}"

    regime = sig["regime_ok"]

    # 2) fresh, high-quality entry today
    if regime and sig["trigger"] and score >= BUY_MIN:
        parts = []
        if sig["breakout"]:      parts.append("20-day breakout")
        if sig["reclaim"]:       parts.append("reclaimed the band")
        if sig["squeeze_break"]: parts.append("squeeze fired up")
        return "BUY NOW", "entry trigger: " + ", ".join(parts) + " (act at next open)"

    # 3) setup building but not fired yet
    if regime and score >= NEAR_MIN:
        near_high = (sig["prox_high_%"] == sig["prox_high_%"]) and (0 <= sig["prox_high_%"] <= NEAR_PCT)
        near_band = sig["pos_vs_band"] in ("inside",) or \
            (sig["pos_vs_band"] == "below" and 0 <= sig["need_move_%"] <= NEAR_PCT)
        if sig["squeeze_on"] or near_high or near_band:
            bits = []
            if sig["squeeze_on"]: bits.append("volatility squeeze (coiled)")
            if near_high:         bits.append(f"{sig['prox_high_%']:.1f}% under the 20-day high")
            if near_band:         bits.append("hugging the support band")
            return "CLOSE TO BUY", "; ".join(bits) + " -- watch for the trigger"

    # 4) already trending, no fresh entry
    if regime and sig["pos_vs_band"] == "above":
        return "HOLD (UPTREND)", "above the band and trending; hold if long, no fresh entry"

    return "WATCH", "no setup: regime and/or score too weak"


def screen_ticker(ticker: str, daily: pd.DataFrame, meta: dict | None = None) -> dict:
    meta = meta or {}
    base = {"ticker": ticker, "name": meta.get("name", ""),
            "wsb_rank": meta.get("rank"), "mentions": meta.get("mentions")}

    if daily is None or len(daily) < MIN_BARS:
        return {**base, "group": "SKIPPED",
                "note": "insufficient price history",
                "bars": 0 if daily is None else len(daily)}

    sig = live_signal(daily)
    group, note = _bucket(sig)

    # per-ticker swing quality (>=10-day hold backtest)
    try:
        _, trades = swing_backtest(daily)
        st = compute_stats(trades)
    except Exception as e:  # never let one ticker kill the run
        st = compute_stats(None)
        note = f"{note} | backtest error: {e!r}"

    return {
        **base,
        "group": group,
        "score": sig["score"],
        "close": sig["close"],
        "regime_ok": sig["regime_ok"],
        "golden": sig["golden"],
        "pos_vs_band": sig["pos_vs_band"],
        "band_bot": sig["band_bot"],
        "band_top": sig["band_top"],
        "rsi": sig["rsi"],
        "macd_hist": sig["macd_hist"],
        "mom_12_1_%": sig["mom_12_1_%"],
        "squeeze_on": sig["squeeze_on"],
        "vol_ratio": sig["vol_ratio"],
        "obv_rising": sig["obv_rising"],
        "trigger": sig["trigger"],
        "exit_flag": sig["exit_flag"],
        "prox_high_%": sig["prox_high_%"],
        "need_move_%": sig["need_move_%"],
        # component breakdown
        "s_regime": sig["s_regime"], "s_band": sig["s_band"], "s_mom": sig["s_mom"],
        "s_macd": sig["s_macd"], "s_rsi": sig["s_rsi"], "s_squeeze": sig["s_squeeze"],
        "s_breakout": sig["s_breakout"],
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


GROUP_ORDER = ["BUY NOW", "CLOSE TO BUY", "HOLD (UPTREND)", "SELL / EXIT", "WATCH", "SKIPPED"]


def rank_group(g_df: pd.DataFrame, group: str) -> pd.DataFrame:
    if group == "CLOSE TO BUY":
        return g_df.sort_values(["score", "need_move_%"], ascending=[False, True])
    if group == "SELL / EXIT":
        return g_df.sort_values("score", ascending=True)
    if group == "WATCH":
        return g_df.sort_values("score", ascending=False)
    if group == "SKIPPED":
        return g_df.sort_values("mentions", ascending=False, na_position="last")
    # BUY NOW / HOLD -> best score (with backtest expectancy as tiebreak)
    return g_df.sort_values(["score", "bt_expectancy_$"], ascending=[False, False])


def run_screener(history: dict, metas: dict, progress_every: int = 25) -> pd.DataFrame:
    """history: {ticker: daily df}, metas: {ticker: {rank, mentions, name}}.
    Returns a single ranked DataFrame."""
    rows = []
    tickers = list(metas.keys())
    for i, tk in enumerate(tickers, 1):
        try:
            rows.append(screen_ticker(tk, history.get(tk), metas.get(tk)))
        except Exception as e:
            m = metas.get(tk, {})
            rows.append({"ticker": tk, "name": m.get("name", ""), "wsb_rank": m.get("rank"),
                         "mentions": m.get("mentions"), "group": "SKIPPED",
                         "note": f"error: {e!r}"})
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
