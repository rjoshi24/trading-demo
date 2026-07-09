"""
quant_screener.py
=================
Runs the **Dip-Buy Swing Model** (`quant_core.py`) across many tickers, daily.

Philosophy (what the user asked for):
  * Go IN on high-conviction dips only (BUY NOW is gated by a proven win rate).
  * Get OUT easy if wrong -> a hard stop = SELL "the buy was bad".
  * If right, RIDE the wave until the thesis/signal changes (adaptive z-target).
  * So there IS a SELL signal, but it only appears when a real model position
    actually exits (position-aware, off the backtest) - not a stateless "sell".

Buckets:
  BUY NOW        - flat + a dip fired today + this name's history clears the win-rate gate.
  SELL / EXIT    - a model position exited on the latest bar:
                     * stop hit  -> the buy was wrong, cut it (re-enter on next dip)
                     * z-target  -> mean-reversion thesis complete, take profit
  HOLDING (RIDE) - entered on a prior dip and still riding toward the target.
  CLOSE TO BUY   - flat, a dip fired with a moderate/unproven edge, or sliding into the zone.
  WATCH          - flat, no dip.
  SKIPPED        - not enough clean history.
"""
from __future__ import annotations
import pandas as pd

from .quant_core import (
    compute_features, live_signal, swing_backtest, compute_stats, position_state,
    NEAR_MIN, RSI_OS_SOFT, Z_BUY, SMA_FAST, VOL_N, STOP_PCT,
)

MIN_BARS = SMA_FAST + VOL_N + 15

MIN_BT_TRADES  = 8
STRONG_WINRATE = 55.0
OK_WINRATE     = 45.0
_STOP = int(round(STOP_PCT * 100))


def _dip_reasons(sig: dict) -> str:
    bits = []
    if sig["rsi2"] <= 10:
        bits.append(f"RSI-2 {sig['rsi2']:.0f} (oversold)")
    if (sig["z_band"] == sig["z_band"]) and sig["z_band"] <= Z_BUY:
        bits.append(f"{sig['z_band']:.1f} sigma below band")
    if (sig["vol_surge"] == sig["vol_surge"]) and sig["vol_surge"] >= 1.5:
        bits.append(f"vol {sig['vol_surge']:.1f}x")
    return ", ".join(bits or ["dip"])


def _bucket(sig: dict, st: dict, pos: dict) -> tuple[str, str]:
    score = sig["score"]
    if not (score == score):
        return "SKIPPED", "indicators not ready"

    # --- position-aware exits: SELL only when a real position actually closed ---
    if pos.get("state") == "SOLD":
        ret = pos.get("ret_%", 0.0); reason = pos.get("exit_reason", "")
        if reason == "stop":
            return "SELL / EXIT", f"SELL: {_STOP}% stop hit ({ret:+.1f}%) - buy was wrong, cut it; re-enter on the next dip"
        if reason == "z-target":
            return "SELL / EXIT", f"SELL: target reached ({ret:+.1f}%) - mean-reversion thesis complete, take profit"
        return "SELL / EXIT", f"SELL: time exit ({ret:+.1f}%)"

    if pos.get("state") == "HOLDING":
        return "HOLDING (RIDE)", (f"in since {pos['entry_date']} ({pos['gain_%']:+.1f}%): "
                                  f"riding to {sig['exit_plan']}, {_STOP}% stop")

    # --- FLAT: look for a fresh dip to BUY ---
    wr = st["Win Rate %"]; nt = st["Total Trades"]; proven = nt >= MIN_BT_TRADES
    if sig["trigger"]:
        reasons = _dip_reasons(sig)
        plan = f"exit {sig['exit_plan']}, {_STOP}% stop"
        if proven and wr >= STRONG_WINRATE:
            return "BUY NOW", f"dip buy ({wr:.0f}% hist win): {reasons} -> {plan}"
        if (not proven) or wr >= OK_WINRATE:
            edge = f"{wr:.0f}% hist win" if proven else "unproven"
            return "CLOSE TO BUY", f"dip fired ({edge}): {reasons} -> {plan}"
        return "WATCH", f"dip fired but weak edge ({wr:.0f}% hist win): {reasons}"

    getting_oversold = sig["rsi2"] <= RSI_OS_SOFT
    stretching = (sig["z_band"] == sig["z_band"]) and sig["z_band"] <= -1.0
    if (getting_oversold or stretching) and score >= NEAR_MIN:
        note = []
        if getting_oversold: note.append(f"RSI-2 {sig['rsi2']:.0f} sliding into oversold")
        if stretching:       note.append(f"{sig['z_band']:.1f} sigma below band")
        return "CLOSE TO BUY", "; ".join(note) + " -- waiting for the dip trigger"

    return "WATCH", "no dip"


def screen_ticker(ticker: str, daily: pd.DataFrame, meta: dict | None = None) -> dict:
    meta = meta or {}
    base = {"ticker": ticker, "name": meta.get("name", ""),
            "wsb_rank": meta.get("rank"), "mentions": meta.get("mentions"),
            "source": meta.get("source", "")}

    if daily is None or len(daily) < MIN_BARS:
        return {**base, "group": "SKIPPED", "note": "insufficient price history",
                "bars": 0 if daily is None else len(daily)}

    sig = live_signal(daily)
    try:
        d, trades = swing_backtest(daily)
        st = compute_stats(trades)
        pos = position_state(d, trades)
    except Exception:
        st = compute_stats(None); pos = {"state": "FLAT"}

    group, note = _bucket(sig, st, pos)

    return {
        **base,
        "group": group,
        "score": sig["score"],
        "close": sig["close"],
        "rsi2": sig["rsi2"], "rsi14": sig["rsi14"],
        "z_band": sig["z_band"], "dist_band_%": sig["dist_band_%"],
        "vol_surge": sig["vol_surge"], "up_close": sig["up_close"], "obv_rising": sig["obv_rising"],
        "above_50": sig["above_50"], "sma20_up": sig["sma20_up"], "mom_63_%": sig["mom_63_%"],
        "pos_vs_band": sig["pos_vs_band"], "band_bot": sig["band_bot"], "band_top": sig["band_top"],
        "band_read": sig["band_read"],
        "exit_z_target": sig["exit_z_target"], "exit_plan": sig["exit_plan"], "stop_%": _STOP,
        "dip": sig["dip"], "trigger": sig["trigger"],
        # position state
        "pos_state": pos.get("state", "FLAT"),
        "entry_price": pos.get("entry_price"),
        "pos_gain_%": pos.get("gain_%"),
        "pos_ret_%": pos.get("ret_%"),
        "exit_reason": pos.get("exit_reason"),
        "entry_date": pos.get("entry_date"),
        "bars_held": pos.get("bars_held"),
        # conviction breakdown
        "s_oversold": sig["s_oversold"], "s_stretch": sig["s_stretch"], "s_volume": sig["s_volume"],
        "s_reversal": sig["s_reversal"], "s_trend": sig["s_trend"],
        # this name's backtest
        "bt_trades": st["Total Trades"], "bt_winrate_%": st["Win Rate %"],
        "bt_expectancy_$": st["Expectancy $"], "bt_avg_bars": st["Avg Bars Held"],
        "bt_profit_factor": st["Profit Factor"],
        "signal_date": sig["date"], "bars": len(daily), "note": note,
    }


GROUP_ORDER = ["BUY NOW", "SELL / EXIT", "HOLDING (RIDE)", "CLOSE TO BUY", "WATCH", "SKIPPED"]


def rank_group(g_df: pd.DataFrame, group: str) -> pd.DataFrame:
    if group == "BUY NOW":
        return g_df.sort_values(["bt_winrate_%", "score", "vol_surge"], ascending=[False, False, False])
    if group == "SELL / EXIT":
        return g_df.sort_values("pos_ret_%", ascending=True, na_position="last")
    if group == "HOLDING (RIDE)":
        return g_df.sort_values("pos_gain_%", ascending=False, na_position="last")
    if group == "CLOSE TO BUY":
        return g_df.sort_values(["bt_winrate_%", "score"], ascending=[False, False])
    if group == "WATCH":
        return g_df.sort_values("score", ascending=False)
    return g_df.sort_values("mentions", ascending=False, na_position="last")


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
