"""
quant_screener.py
=================
Runs the **Dip-and-Ride Swing Model** (`quant_core.py`) across many tickers.

Buy dips, cut losers small, ride winners big. Because we RIDE, win rate is lower
but the average win is large - so BUY signals are gated by **profit factor**
(proven money-maker), not win rate.

Buckets:
  BUY NOW        - flat + a dip fired today + this name's history is a proven
                   money-maker (>= MIN_BT_TRADES trades and profit factor >= gate).
  SELL / EXIT    - a model position exited on the latest bar:
                     * stop  -> loser cut (small loss)
                     * trail -> trend broke, lock in the ride (usually a win)
  HOLDING (RIDE) - entered on a prior dip and still riding the trend.
  CLOSE TO BUY   - a dip fired with a thinner/unproven edge, or sliding into the zone.
  WATCH          - flat, no dip.
  SKIPPED        - not enough clean history.
"""
from __future__ import annotations
import pandas as pd

from .quant_core import (
    compute_features, live_signal, swing_backtest, compute_stats, position_state,
    NEAR_MIN, RSI_OS_SOFT, Z_BUY, SMA_FAST, VOL_N, STOP_PCT, ride_plan,
)

MIN_BARS = SMA_FAST + VOL_N + 15

MIN_BT_TRADES = 8
STRONG_PF     = 1.4     # profit factor for a high-conviction BUY
OK_PF         = 1.05    # thinner edge -> CLOSE TO BUY
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

    # 1) a fresh dip TODAY is the actionable buy signal -> it takes priority so BUY NOW
    #    fires even if an older ride is still open on the same name.
    pf = st["Profit Factor"]; nt = st["Total Trades"]; proven = nt >= MIN_BT_TRADES
    aw = st["Avg Win %"]
    if sig["trigger"]:
        reasons = _dip_reasons(sig)
        plan = ride_plan()
        if proven and pf >= STRONG_PF:
            return "BUY NOW", f"dip buy (PF {pf:.1f}, avg win +{aw:.0f}%): {reasons} -> {plan}"
        if (not proven) or pf >= OK_PF:
            edge = f"PF {pf:.1f}" if proven else "unproven"
            return "CLOSE TO BUY", f"dip fired ({edge}): {reasons} -> {plan}"
        return "WATCH", f"dip fired but no edge (PF {pf:.1f}): {reasons}"

    # 2) no fresh dip today -> position-aware state (SELL only when a position actually closed)
    if pos.get("state") == "SOLD":
        ret = pos.get("ret_%", 0.0)
        if pos.get("exit_reason") == "stop":
            return "SELL / EXIT", f"SELL: {_STOP}% stop hit ({ret:+.1f}%) - loser cut; re-enter on the next dip"
        if pos.get("exit_reason") == "trail":
            return "SELL / EXIT", f"SELL: trailing stop hit ({ret:+.1f}%) - trend broke, lock in the ride"
        return "SELL / EXIT", f"SELL: time exit ({ret:+.1f}%)"

    if pos.get("state") == "HOLDING":
        return "HOLDING (RIDE)", f"in since {pos['entry_date']} ({pos['gain_%']:+.1f}%): riding the trend, {_STOP}% stop"

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
        "score": sig["score"], "close": sig["close"],
        "rsi2": sig["rsi2"], "rsi14": sig["rsi14"],
        "z_band": sig["z_band"], "dist_band_%": sig["dist_band_%"],
        "vol_surge": sig["vol_surge"], "up_close": sig["up_close"], "obv_rising": sig["obv_rising"],
        "above_50": sig["above_50"], "sma20_up": sig["sma20_up"], "mom_63_%": sig["mom_63_%"],
        "pos_vs_band": sig["pos_vs_band"], "band_bot": sig["band_bot"], "band_top": sig["band_top"],
        "band_read": sig["band_read"], "exit_plan": sig["exit_plan"], "stop_%": _STOP,
        "dip": sig["dip"], "trigger": sig["trigger"],
        "pos_state": pos.get("state", "FLAT"), "entry_price": pos.get("entry_price"),
        "pos_gain_%": pos.get("gain_%"), "pos_ret_%": pos.get("ret_%"),
        "exit_reason": pos.get("exit_reason"), "entry_date": pos.get("entry_date"),
        "bars_held": pos.get("bars_held"),
        "s_oversold": sig["s_oversold"], "s_stretch": sig["s_stretch"], "s_volume": sig["s_volume"],
        "s_reversal": sig["s_reversal"], "s_trend": sig["s_trend"],
        # this name's dip-and-ride backtest
        "bt_trades": st["Total Trades"], "bt_winrate_%": st["Win Rate %"],
        "bt_avg_win_%": st["Avg Win %"], "bt_avg_loss_%": st["Avg Loss %"],
        "bt_max_win_%": st["Max Win %"], "bt_profit_factor": st["Profit Factor"],
        "bt_expectancy_%": st["Expectancy %"], "bt_avg_bars": st["Avg Bars Held"],
        "signal_date": sig["date"], "bars": len(daily), "note": note,
    }


GROUP_ORDER = ["BUY NOW", "SELL / EXIT", "HOLDING (RIDE)", "CLOSE TO BUY", "WATCH", "SKIPPED"]


def rank_group(g_df: pd.DataFrame, group: str) -> pd.DataFrame:
    if group == "BUY NOW":
        return g_df.sort_values(["bt_profit_factor", "bt_expectancy_%", "score"], ascending=[False, False, False])
    if group == "SELL / EXIT":
        return g_df.sort_values("pos_ret_%", ascending=True, na_position="last")
    if group == "HOLDING (RIDE)":
        return g_df.sort_values("pos_gain_%", ascending=False, na_position="last")
    if group == "CLOSE TO BUY":
        return g_df.sort_values(["bt_profit_factor", "score"], ascending=[False, False])
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
