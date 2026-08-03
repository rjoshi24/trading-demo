"""
quant_screener.py
=================
Runs the **Dip-and-Ride Swing Model** (`quant_core.py`) across many tickers.

The output describes model states and historical diagnostics; it is not a set
of trade recommendations. The model supports one open position per ticker and
does not pyramid. Runtime exit configuration is passed explicitly with
`QuantConfig` so screening and portfolio simulation use identical settings.

Buckets:
  BUY NOW        - the one-position model is flat, a dip signal fired today,
                   and historical diagnostics clear the configured gate.
  EXIT PENDING   - the latest close crossed an exit threshold; the model waits
                   for the next open, which can gap beyond the threshold.
  SELL / EXIT    - a prior close threshold was breached and the model filled at
                   the latest open.
  HOLDING (RIDE) - entered on a prior dip and still holding; fresh dip signals
                   are informational because pyramiding is not modeled.
  CLOSE TO BUY   - a lower-confidence dip signal or movement toward the dip zone.
  WATCH          - flat, no current dip signal.
  SKIPPED        - not enough clean history.
  ERROR          - data acquisition/normalization or model failure.
"""
from __future__ import annotations
import pandas as pd

from .quant_core import (
    DEFAULT_CONFIG, QuantConfig, live_signal, swing_backtest, compute_stats,
    position_state, NEAR_MIN, RSI_OS_SOFT, Z_BUY, SMA_FAST, VOL_N, ride_plan,
)

MIN_BARS = SMA_FAST + VOL_N + 15

MIN_BT_TRADES = 8
STRONG_PF     = 1.4     # profit factor for a high-conviction entry signal
OK_PF         = 1.05    # thinner edge -> CLOSE TO BUY


def _dip_reasons(sig: dict) -> str:
    bits = []
    if sig["rsi2"] <= 10:
        bits.append(f"RSI-2 {sig['rsi2']:.0f} (oversold)")
    if (sig["z_band"] == sig["z_band"]) and sig["z_band"] <= Z_BUY:
        bits.append(f"{sig['z_band']:.1f} sigma below band")
    if (sig["vol_surge"] == sig["vol_surge"]) and sig["vol_surge"] >= 1.5:
        bits.append(f"vol {sig['vol_surge']:.1f}x")
    return ", ".join(bits or ["dip"])


def _bucket(sig: dict, st: dict, pos: dict,
            config: QuantConfig) -> tuple[str, str]:
    score = sig["score"]
    if not (score == score):
        return "SKIPPED", "indicators not ready"

    close_exit_pct = config.close_exit_pct

    # A final-bar close trigger cannot fill until the next open, so surface that
    # pending state before either holding or entry-signal classification.
    if pos.get("state") == "EXIT_PENDING":
        reason = pos.get("exit_reason")
        if reason == "initial_close":
            detail = (f"close breached {close_exit_pct:.0%} entry threshold "
                      f"({pos.get('initial_close_level')})")
        elif reason == "trailing_close":
            detail = f"close breached trailing threshold ({pos.get('trailing_close_level')})"
        else:
            detail = "maximum holding period reached"
        return "EXIT PENDING", f"{detail}; modeled exit at next open (gap risk)"

    # The backtest models one position, not pyramiding. A fresh dip while already
    # holding is informational and must not be presented as another entry.
    if pos.get("state") == "HOLDING":
        trigger_note = "; fresh dip signal observed, but no add-on is modeled" if sig["trigger"] else ""
        return ("HOLDING (RIDE)",
                f"in since {pos['entry_date']} ({pos['gain_%']:+.1f}%); "
                f"initial close-exit threshold {close_exit_pct:.0%}{trigger_note}")

    # A fresh dip is an entry signal only while the model is flat.
    pf = st["Profit Factor"]; nt = st["Total Trades"]; proven = nt >= MIN_BT_TRADES
    aw = st["Avg Win %"]
    if sig["trigger"]:
        reasons = _dip_reasons(sig)
        plan = ride_plan(config)
        if proven and pf >= STRONG_PF:
            return "BUY NOW", f"flat-model entry signal (PF {pf:.1f}, avg win {aw:+.0f}%): {reasons} -> {plan}"
        if (not proven) or pf >= OK_PF:
            edge = f"PF {pf:.1f}" if proven else "unproven"
            return "CLOSE TO BUY", f"flat-model dip signal ({edge}): {reasons} -> {plan}"
        return "WATCH", f"dip signal, but historical PF is {pf:.1f}"

    if pos.get("state") == "SOLD":
        ret = pos.get("ret_%", 0.0)
        if pos.get("exit_reason") == "initial_close":
            return ("SELL / EXIT",
                    f"EXIT: {close_exit_pct:.0%} close threshold breached; next-open return "
                    f"{ret:+.1f}% (gap risk)")
        if pos.get("exit_reason") == "trailing_close":
            return ("SELL / EXIT",
                    f"EXIT: trailing close threshold breached; next-open return {ret:+.1f}% "
                    "(gap risk)")
        return "SELL / EXIT", f"EXIT: time limit; next-open return {ret:+.1f}%"

    getting_oversold = sig["rsi2"] <= RSI_OS_SOFT
    stretching = (sig["z_band"] == sig["z_band"]) and sig["z_band"] <= -1.0
    if (getting_oversold or stretching) and score >= NEAR_MIN:
        note = []
        if getting_oversold: note.append(f"RSI-2 {sig['rsi2']:.0f} sliding into oversold")
        if stretching:       note.append(f"{sig['z_band']:.1f} sigma below band")
        return "CLOSE TO BUY", "; ".join(note) + " -- waiting for the dip signal"

    return "WATCH", "no dip signal"


def screen_ticker(ticker: str, daily: pd.DataFrame, meta: dict | None = None,
                  config: QuantConfig = DEFAULT_CONFIG) -> dict:
    meta = meta or {}
    base = {"ticker": ticker, "name": meta.get("name", ""),
            "wsb_rank": meta.get("rank"), "mentions": meta.get("mentions"),
            "source": meta.get("source", "")}

    if daily is None or len(daily) < MIN_BARS:
        return {**base, "group": "SKIPPED", "note": "insufficient price history",
                "bars": 0 if daily is None else len(daily)}

    sig = live_signal(daily, config=config)
    d, trades = swing_backtest(daily, config=config)
    st = compute_stats(trades)
    pos = position_state(d, trades, config=config)

    group, note = _bucket(sig, st, pos, config)

    return {
        **base,
        "group": group,
        "score": sig["score"], "close": sig["close"],
        "rsi2": sig["rsi2"], "rsi14": sig["rsi14"],
        "z_band": sig["z_band"], "dist_band_%": sig["dist_band_%"],
        "vol_surge": sig["vol_surge"], "up_close": sig["up_close"], "obv_rising": sig["obv_rising"],
        "above_50": sig["above_50"], "sma20_up": sig["sma20_up"], "mom_63_%": sig["mom_63_%"],
        "pos_vs_band": sig["pos_vs_band"], "band_bot": sig["band_bot"], "band_top": sig["band_top"],
        "band_read": sig["band_read"], "exit_plan": sig["exit_plan"],
        "close_exit_threshold_%": round(config.close_exit_pct * 100, 2),
        "dip": sig["dip"], "trigger": sig["trigger"],
        "pos_state": pos.get("state", "FLAT"), "entry_price": pos.get("entry_price"),
        "pos_gain_%": pos.get("gain_%"), "pos_ret_%": pos.get("ret_%"),
        "exit_reason": pos.get("exit_reason"), "entry_date": pos.get("entry_date"),
        "initial_close_level": pos.get("initial_close_level"),
        "trailing_close_level": pos.get("trailing_close_level"),
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


GROUP_ORDER = ["BUY NOW", "EXIT PENDING", "SELL / EXIT", "HOLDING (RIDE)", "CLOSE TO BUY", "WATCH", "SKIPPED", "ERROR"]


def rank_group(g_df: pd.DataFrame, group: str) -> pd.DataFrame:
    if group == "BUY NOW":
        return g_df.sort_values(["bt_profit_factor", "bt_expectancy_%", "score"], ascending=[False, False, False])
    if group in ("EXIT PENDING", "SELL / EXIT"):
        return g_df.sort_values("pos_ret_%", ascending=True, na_position="last")
    if group == "HOLDING (RIDE)":
        return g_df.sort_values("pos_gain_%", ascending=False, na_position="last")
    if group == "CLOSE TO BUY":
        return g_df.sort_values(["bt_profit_factor", "score"], ascending=[False, False])
    if group == "WATCH":
        return g_df.sort_values("score", ascending=False)
    return g_df.sort_values("mentions", ascending=False, na_position="last")


def _data_error_row(ticker: str, meta: dict, failure: dict) -> dict:
    stage = failure.get("error_stage", "data")
    error_type = failure.get("error_type", "DataError")
    message = failure.get("error_message", "price data unavailable")
    return {
        "ticker": ticker, "name": meta.get("name", ""),
        "wsb_rank": meta.get("rank"), "mentions": meta.get("mentions"),
        "source": meta.get("source", ""), "group": "ERROR",
        "error_stage": stage, "error_type": error_type,
        "error_message": message,
        "note": f"data-stage failure ({stage}): {error_type}: {message}",
    }


def run_screener(history: dict, metas: dict, config: QuantConfig = DEFAULT_CONFIG,
                 progress_every: int = 25, data_failures: dict | None = None) -> pd.DataFrame:
    """Screen each ticker, preserving optional per-symbol data failures as ERROR rows."""
    rows = []
    tickers = list(metas.keys())
    data_failures = data_failures or {}
    for i, tk in enumerate(tickers, 1):
        failure = data_failures.get(tk)
        if failure is not None:
            rows.append(_data_error_row(tk, metas.get(tk, {}), failure))
        else:
            try:
                rows.append(screen_ticker(tk, history.get(tk), metas.get(tk), config=config))
            except Exception as exc:
                m = metas.get(tk, {})
                rows.append({"ticker": tk, "name": m.get("name", ""), "wsb_rank": m.get("rank"),
                             "mentions": m.get("mentions"), "source": m.get("source", ""),
                             "group": "ERROR", "error_stage": "model",
                             "error_type": type(exc).__name__, "error_message": str(exc),
                             "note": f"model error: {type(exc).__name__}: {exc}"})
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
