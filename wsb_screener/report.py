"""
report.py
=========
Turn the screener DataFrame into a readable Markdown report grouped by
buy-readiness bucket.
"""
from __future__ import annotations
import datetime as dt
import pandas as pd

GROUP_BLURB = {
    "BUY NOW": "Strategy fires a **fresh BUY** on the latest weekly bar. These are the "
               "actionable entries right now (act at next open, per the strategy).",
    "CLOSE TO ENTERING": "Flat and **almost** triggering: price is within a few percent of the "
                         "entry trigger, or already sitting in the anticipate buy-zone below the "
                         "band waiting on a momentum flip. These are the watch-closely names.",
    "IN POSITION": "The strategy would **already be long and holding** (price is above the band, "
                   "riding the trend). Not a fresh entry - a new buyer here is chasing an extended move.",
    "SELL / EXIT": "The strategy would be **exiting** (lost the band or hit the fakeout stop).",
    "WATCH": "Flat and still **far** from any entry trigger. Nothing to do yet.",
    "SKIPPED": "Not enough clean price history to run the strategy.",
}

BUY_COLS = ["group_rank", "ticker", "name", "close", "readiness", "recommendation",
            "mode", "band_bot", "band_top", "rsi", "need_move_%",
            "bt_trades", "bt_winrate_%", "bt_pnl_$", "bt_score"]
CLOSE_COLS = ["group_rank", "ticker", "name", "close", "readiness", "pos_vs_band",
              "mode", "band_bot", "band_top", "rsi", "need_move_%", "note"]
POS_COLS = ["group_rank", "ticker", "name", "close", "recommendation", "mode",
            "band_bot", "band_top", "rsi", "need_move_%", "bt_winrate_%", "bt_score"]
WATCH_COLS = ["group_rank", "ticker", "name", "close", "readiness", "pos_vs_band",
              "mode", "band_bot", "band_top", "rsi", "need_move_%"]


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
    out.append("# WSB Top-200 - BMSB Buy-Readiness Screen\n")
    out.append(f"_Generated {now} | latest weekly bar: **{signal_date}** | "
               f"universe: top {universe_n} r/wallstreetbets tickers by mention count_\n")
    out.append("> **Research only, not financial advice.** Each ticker is scored with its own "
               "best-fitting BMSB config from a parameter sweep (ranked by Total P&L x Win Rate over "
               "~10y of weekly data). Best-fit configs are partly curve-fit - treat as candidates.\n")

    out.append("## How to read this\n")
    out.append("- **BUY NOW** - a fresh entry signal on the latest weekly candle.\n"
               "- **CLOSE TO ENTERING** - flat but within ~6% of the trigger, or in the anticipate "
               "buy-zone; these are the ones to watch this week.\n"
               "- **IN POSITION** - already trending above the band (the strategy is holding); a new "
               "buyer is chasing.\n"
               "- **SELL / EXIT** and **WATCH** are shown for completeness.\n"
               "- `readiness` 0-100 = how close to a buy. `need_move_%` = % price move to reach the "
               "trigger (negative = price is already above it).\n")

    out.append("## Summary\n")
    out.append("| Group | Count |\n| --- | --- |")
    for g in ["BUY NOW", "CLOSE TO ENTERING", "IN POSITION", "SELL / EXIT", "WATCH", "SKIPPED"]:
        if g in counts:
            out.append(f"| {g} | {counts[g]} |")
    out.append("")

    sections = [
        ("BUY NOW", BUY_COLS),
        ("CLOSE TO ENTERING", CLOSE_COLS),
        ("IN POSITION", POS_COLS),
        ("SELL / EXIT", POS_COLS),
        ("WATCH", WATCH_COLS),
    ]
    for g, cols in sections:
        sub = df[df["group"] == g]
        out.append(f"## {g}  ({len(sub)})\n")
        out.append(GROUP_BLURB.get(g, "") + "\n")
        out.append(_md_table(sub, cols))

    skipped = df[df["group"] == "SKIPPED"]
    if not skipped.empty:
        out.append(f"## SKIPPED  ({len(skipped)})\n")
        out.append(GROUP_BLURB["SKIPPED"] + "\n")
        out.append(", ".join(f"{r.ticker} ({r.note})" for _, r in skipped.iterrows()) + "\n")

    return "\n".join(out)
