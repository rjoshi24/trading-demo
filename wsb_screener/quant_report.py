"""
quant_report.py
===============
Render the Dip-Buy Swing Model screen into a Markdown report grouped by bucket.
Buy-focused, with position-aware SELL / HOLDING sections.
"""
from __future__ import annotations
import datetime as dt
import pandas as pd

GROUP_BLURB = {
    "BUY NOW": "**High-conviction dip buys firing today.** Oversold (RSI-2) and/or stretched "
               ">= 1.5 sigma below the 20/21 band, in names whose dip-and-ride history is a **proven "
               "money-maker (profit factor gate)** with a **big average win**. Buy at next open; cut "
               "small if wrong; ride the trend if right.",
    "SELL / EXIT": "**A model position just exited on the latest bar.** Either the **stop hit** (loser "
                   "cut small - re-enter on the next dip) or the **trailing stop hit** (trend broke - "
                   "lock in the ride, usually a win).",
    "HOLDING (RIDE)": "**Entered on a prior dip and still riding the trend.** No fixed take-profit - it "
                      "runs until the trailing stop; the initial stop protected the downside.",
    "CLOSE TO BUY": "A dip fired with a **thinner/unproven** edge, or price is sliding into the buy "
                    "zone. Watch for a high-conviction trigger.",
    "WATCH": "No dip. Nothing to do.",
    "SKIPPED": "Not enough clean daily history.",
}

BUY_COLS  = ["group_rank", "ticker", "name", "close", "score", "rsi2", "z_band",
             "bt_profit_factor", "bt_avg_win_%", "bt_winrate_%", "bt_max_win_%",
             "exit_plan", "band_read", "note"]
SELL_COLS = ["group_rank", "ticker", "name", "close", "entry_price", "pos_ret_%", "exit_reason",
             "z_band", "note"]
HOLD_COLS = ["group_rank", "ticker", "name", "close", "entry_price", "pos_gain_%", "bars_held",
             "z_band", "exit_plan", "stop_%"]
NEAR_COLS = ["group_rank", "ticker", "name", "close", "score", "rsi2", "z_band", "dist_band_%",
             "vol_surge", "bt_profit_factor", "bt_avg_win_%", "band_read", "note"]
WATCH_COLS = ["group_rank", "ticker", "name", "close", "score", "rsi2", "z_band", "above_50", "mom_63_%"]


def _md_table(df: pd.DataFrame, cols) -> str:
    cols = [c for c in cols if c in df.columns]
    if df.empty:
        return "_none_\n"
    view = df[cols].copy()
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join("---" for _ in cols) + " |"
    lines = [header, sep]
    for _, r in view.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if isinstance(v, float):
                v = f"{v:,.2f}"
            cells.append(str(v))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def build_markdown(df: pd.DataFrame, universe_n: int, signal_date: str,
                   portfolio: dict | None = None) -> str:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    counts = df["group"].value_counts().to_dict()

    out = []
    out.append("# Dip-and-Ride Swing Screen\n")
    out.append(f"_Generated {now} | latest daily bar: **{signal_date}** | universe: {universe_n} names "
               "(most popular US stocks + ETFs, plus WSB)_\n")
    out.append("> **Research only, not financial advice.** Buy dips, cut losers small with an initial "
               "stop, and RIDE winners with a trailing stop - small losses, big wins.\n")

    out.append("## The model in one paragraph\n")
    out.append("Buy a **dip** - RSI-2 oversold and/or price stretched **>= 1.5 std-devs below the 20/21 "
               "band** (`z_band`). **Cut it small** if wrong (initial stop). If it works, there is **no "
               "1-2% take-profit** - a **trailing stop rides the trend** so the average win is large "
               "(often +15-50%) and the occasional monster runs. Because we ride, win rate is lower, so "
               "BUY signals are gated by **profit factor** (a proven money-maker), not win rate. SELL "
               "only shows when a real position exits (stop = small loss; trail = locked-in ride).\n")

    if portfolio:
        p = portfolio
        out.append("## $100 portfolio backtest\n")
        out.append(f"Giving the strategy **${p['start_$']:.0f}** across this universe "
                   f"(max {p['max_positions']} positions, {p['stop_pct']*100:.0f}% initial stop, "
                   f"ride={p['ride_mode']}): **${p['final_$']:.2f}** ({p['return_%']:+.0f}%, "
                   f"CAGR {p['CAGR_%']}%/yr, max drawdown {p['max_drawdown_%']}%, {p['trades']} trades, "
                   f"{p['win_rate_%']}% win rate, avg win +{p['avg_win_%']}%).\n")

    out.append("## Summary\n")
    out.append("| Group | Count |\n| --- | --- |")
    for g in ["BUY NOW", "SELL / EXIT", "HOLDING (RIDE)", "CLOSE TO BUY", "WATCH", "SKIPPED"]:
        if g in counts:
            out.append(f"| {g} | {counts[g]} |")
    out.append("")

    sections = [
        ("BUY NOW", BUY_COLS),
        ("SELL / EXIT", SELL_COLS),
        ("HOLDING (RIDE)", HOLD_COLS),
        ("CLOSE TO BUY", NEAR_COLS),
        ("WATCH", WATCH_COLS),
    ]
    for g, cols in sections:
        sub = df[df["group"] == g]
        out.append(f"## {g}  ({len(sub)})\n")
        out.append(GROUP_BLURB.get(g, "") + "\n")
        if g in ("WATCH", "HOLDING (RIDE)") and len(sub) > 40:
            out.append(_md_table(sub.head(40), cols))
            out.append(f"\n_...and {len(sub) - 40} more._\n")
        else:
            out.append(_md_table(sub, cols))

    skipped = df[df["group"] == "SKIPPED"]
    if not skipped.empty:
        out.append(f"## SKIPPED  ({len(skipped)})\n")
        out.append(", ".join(f"{r.ticker}" for _, r in skipped.iterrows()) + "\n")
    return "\n".join(out)
