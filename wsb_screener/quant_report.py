"""Render the daily quant-model screen as a grouped Markdown research report."""
from __future__ import annotations
import datetime as dt
import pandas as pd

GROUP_BLURB = {
    "BUY NOW": "**The model produced an entry signal while flat.** The label describes simulated "
               "model state, not a recommendation. Any modeled entry occurs at the next open.",
    "EXIT PENDING": "**The latest close crossed an exit threshold.** The modeled position remains "
                    "open until the next available open, which can gap beyond the threshold.",
    "SELL / EXIT": "**A modeled position exited at the latest open.** Initial and trailing exit "
                   "thresholds are evaluated on the prior close; the next open can gap beyond them.",
    "HOLDING (RIDE)": "**The model already holds one position.** It does not pyramid, so a new dip "
                      "signal while holding is informational and never becomes another entry label.",
    "CLOSE TO BUY": "The model sees a dip signal with thinner or limited history, or price is moving "
                    "toward its dip zone.",
    "WATCH": "No current model entry signal.",
    "SKIPPED": "Price data was acquired, but the model could not run because history or indicators were insufficient.",
    "ERROR": "A data download/normalization/no-data failure or model error occurred. See `error_stage` for provenance.",
}

BUY_COLS = ["group_rank", "ticker", "name", "close", "score", "rsi2", "z_band",
            "bt_profit_factor", "bt_avg_win_%", "bt_winrate_%", "bt_max_win_%",
            "exit_plan", "band_read", "note"]
SELL_COLS = ["group_rank", "ticker", "name", "close", "entry_price", "pos_ret_%", "exit_reason",
             "z_band", "note"]
PENDING_COLS = ["group_rank", "ticker", "name", "close", "entry_price", "pos_gain_%",
                "exit_reason", "initial_close_level", "trailing_close_level", "note"]
HOLD_COLS = ["group_rank", "ticker", "name", "close", "entry_price", "pos_gain_%", "bars_held",
             "z_band", "exit_plan", "close_exit_threshold_%", "note"]
NEAR_COLS = ["group_rank", "ticker", "name", "close", "score", "rsi2", "z_band", "dist_band_%",
             "vol_surge", "bt_profit_factor", "bt_avg_win_%", "band_read", "note"]
WATCH_COLS = ["group_rank", "ticker", "name", "close", "score", "rsi2", "z_band", "above_50", "mom_63_%"]
ERROR_COLS = ["group_rank", "ticker", "name", "error_stage", "error_type", "error_message", "note"]


def _md_table(df: pd.DataFrame, cols) -> str:
    cols = [c for c in cols if c in df.columns]
    if df.empty:
        return "_none_\n"
    view = df[cols].copy()
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join("---" for _ in cols) + " |"
    lines = [header, sep]
    for _, row in view.iterrows():
        cells = []
        for col in cols:
            value = row[col]
            if isinstance(value, float):
                value = f"{value:,.2f}"
            cells.append(str(value).replace("|", "\\|"))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def build_markdown(df: pd.DataFrame, universe_n: int, signal_date: str,
                   portfolio: dict | None = None) -> str:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    counts = df["group"].value_counts().to_dict()

    out = ["# Dip-and-Ride Model Screen\n"]
    out.append(f"_Generated {now} | latest daily bar: **{signal_date}** | requested universe: "
               f"{universe_n} names_\n")
    out.append("> **Research software only; not financial advice or a trading recommendation.** "
               "Bucket names describe model output. Historical statistics are in-sample diagnostics, "
               "not evidence of future performance.\n")

    out.append("## Model and execution assumptions\n")
    out.append("A daily dip signal is based on RSI-2 and/or distance below the 20-SMA/21-EMA band. "
               "One position per ticker is entered at the following open. Initial and trailing exit "
               "thresholds are evaluated only on daily closes and filled at the next available open. "
               "They are **not hard or resting stop orders**: overnight gaps can make realized losses "
               "materially larger than the configured threshold. Fees, slippage, liquidity, taxes, "
               "corporate actions beyond the data vendor's adjustments, and market impact are omitted.\n")

    if portfolio:
        p = portfolio
        out.append("## $100 portfolio simulation\n")
        out.append(f"Across {p['tickers_backtested']}/{p['tickers_requested']} downloaded tickers "
                   f"(max {p['max_positions']} positions, {p['close_exit_pct']:.0%} close-exit threshold, "
                   f"ride={p['ride_mode']}), the simulation changes **${p['start_$']:.0f}** to "
                   f"**${p['final_$']:.2f}** ({p['return_%']:+.1f}%; CAGR {p['CAGR_%']}%; max drawdown "
                   f"{p['max_drawdown_%']}%; {p['trades']} completed trades; win rate "
                   f"{p['win_rate_%']}%). This is a simplified historical simulation, not an "
                   "investable performance record.\n")
        errors = p.get("model_errors", [])
        if errors:
            out.append(f"**Coverage warning:** {len(errors)} ticker(s) failed during portfolio modeling "
                       "and were excluded:\n")
            out.extend(f"- `{e['ticker']}` — {e['error_type']}: {e['error_message']}" for e in errors)
            out.append("")

    out.append("## Summary\n")
    out.append("| Group | Count |\n| --- | --- |")
    for group in ["BUY NOW", "EXIT PENDING", "SELL / EXIT", "HOLDING (RIDE)", "CLOSE TO BUY", "WATCH", "SKIPPED", "ERROR"]:
        if group in counts:
            out.append(f"| {group} | {counts[group]} |")
    out.append("")

    sections = [
        ("BUY NOW", BUY_COLS),
        ("EXIT PENDING", PENDING_COLS),
        ("SELL / EXIT", SELL_COLS),
        ("HOLDING (RIDE)", HOLD_COLS),
        ("CLOSE TO BUY", NEAR_COLS),
        ("WATCH", WATCH_COLS),
    ]
    for group, cols in sections:
        sub = df[df["group"] == group]
        out.append(f"## {group} ({len(sub)})\n")
        out.append(GROUP_BLURB[group] + "\n")
        if group in ("WATCH", "HOLDING (RIDE)") and len(sub) > 40:
            out.append(_md_table(sub.head(40), cols))
            out.append(f"\n_...and {len(sub) - 40} more._\n")
        else:
            out.append(_md_table(sub, cols))

    for group, cols in (("SKIPPED", ["group_rank", "ticker", "name", "bars", "note"]),
                        ("ERROR", ERROR_COLS)):
        sub = df[df["group"] == group]
        if not sub.empty:
            out.append(f"## {group} ({len(sub)})\n")
            out.append(GROUP_BLURB[group] + "\n")
            out.append(_md_table(sub, cols))

    return "\n".join(out)
