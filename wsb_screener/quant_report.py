"""
quant_report.py
===============
Render the Snap-Back Swing Model screen (`quant_screener.run_screener` output)
into a readable Markdown report grouped by bucket.
"""
from __future__ import annotations
import datetime as dt
import pandas as pd

GROUP_BLURB = {
    "BUY NOW": "A **dip buy fired today**: price is oversold (RSI-2) and/or stretched >= 1.5 sigma "
               "below the 20/21 band, confirmed by an up-close / volume surge, with a high score. "
               "Mean-reversion swing (avg hold ~1 week). Act at next open, size with the stop.",
    "CLOSE TO BUY": "**Getting oversold / stretching toward the band** but no confirmed trigger yet. "
                    "Watch for the up-close + volume-surge that flips it to BUY NOW.",
    "HOLD": "Constructive uptrend, **no fresh dip and not extended**. Hold if long; wait for a "
            "pullback to buy.",
    "TAKE PROFIT / SELL": "**Reverted or extended** -- RSI-2 back above 70, or price is >= +2 sigma "
                          "above the band. The snap-back is done; trim / take profit if long.",
    "WATCH": "Neutral -- no dip and no trend edge. Nothing to do.",
    "SKIPPED": "Not enough clean daily history.",
}

BUY_COLS = ["group_rank", "ticker", "name", "close", "score", "rsi2", "z_band", "dist_band_%",
            "vol_surge", "up_close", "band_read", "bt_trades", "bt_winrate_%", "bt_expectancy_$", "note"]
NEAR_COLS = ["group_rank", "ticker", "name", "close", "score", "rsi2", "z_band", "dist_band_%",
             "vol_surge", "bt_winrate_%", "band_read", "note"]
HOLD_COLS = ["group_rank", "ticker", "name", "close", "score", "rsi2", "z_band", "mom_63_%",
             "bt_winrate_%", "bt_expectancy_$"]
SELL_COLS = ["group_rank", "ticker", "name", "close", "score", "rsi2", "z_band", "dist_band_%",
             "band_read", "note"]
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


def build_markdown(df: pd.DataFrame, universe_n: int, signal_date: str) -> str:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    counts = df["group"].value_counts().to_dict()

    out = []
    out.append("# WSB Snap-Back Swing Screen\n")
    out.append(f"_Generated {now} | latest daily bar: **{signal_date}** | "
               f"universe: top {universe_n} r/wallstreetbets tickers by mention count_\n")
    out.append("> **Research only, not financial advice.** A mean-reversion swing model: buy stretched / "
               "oversold dips confirmed by buying volume, sell when they revert or extend. No 200-SMA, "
               "no requirement to be above the band.\n")

    out.append("## The model in one paragraph\n")
    out.append("Each ticker gets a **0-100 score** from the signals that actually tested well: **RSI-2 "
               "oversold**, **stretch from the 20/21 band in standard deviations** (`z_band` -- because "
               "stocks retrace toward the band whether they're above or below it), a **volume surge** "
               "(buying-power confirmation), a **reversal up-close**, and a *soft* (non-gating) trend "
               "context. A name is **BUY NOW** when a dip trigger fires with a high score. Backtested "
               "~68% win rate over 6y on 45 liquid names.\n")

    out.append("## How to read this\n")
    out.append("- **score** 0-100 = how good the dip-buy setup is right now.\n"
               "- **z_band** = standard deviations from the band. Negative = stretched below (bounce "
               "zone); ~ +2 or more = extended above (retrace risk).\n"
               "- **vol_surge** = today's volume / 20-day average (>= 1.5x = buyers stepping in).\n"
               "- **bt_*** = the snap-back swing backtest on this ticker (win rate, expectancy per "
               "$1,000 trade).\n")

    out.append("## Summary\n")
    out.append("| Group | Count |\n| --- | --- |")
    for g in ["BUY NOW", "CLOSE TO BUY", "HOLD", "TAKE PROFIT / SELL", "WATCH", "SKIPPED"]:
        if g in counts:
            out.append(f"| {g} | {counts[g]} |")
    out.append("")

    sections = [
        ("BUY NOW", BUY_COLS),
        ("CLOSE TO BUY", NEAR_COLS),
        ("HOLD", HOLD_COLS),
        ("TAKE PROFIT / SELL", SELL_COLS),
        ("WATCH", WATCH_COLS),
    ]
    for g, cols in sections:
        sub = df[df["group"] == g]
        out.append(f"## {g}  ({len(sub)})\n")
        out.append(GROUP_BLURB.get(g, "") + "\n")
        if g in ("WATCH", "HOLD") and len(sub) > 40:
            out.append(_md_table(sub.head(40), cols))
            out.append(f"\n_...and {len(sub) - 40} more._\n")
        else:
            out.append(_md_table(sub, cols))

    skipped = df[df["group"] == "SKIPPED"]
    if not skipped.empty:
        out.append(f"## SKIPPED  ({len(skipped)})\n")
        out.append(GROUP_BLURB["SKIPPED"] + "\n")
        out.append(", ".join(f"{r.ticker}" for _, r in skipped.iterrows()) + "\n")

    return "\n".join(out)
