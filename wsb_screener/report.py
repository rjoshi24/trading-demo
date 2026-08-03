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
    "BUY NOW": "**The simulated model produced a fresh weekly entry signal while flat.** This "
               "label describes model state, not a recommendation. Under the model's execution "
               "assumptions, any entry is filled at the next open.",
    "CLOSE TO ENTERING": "**The simulated model remains flat and is near an entry condition.** "
                         "Price is within a few percent of the trigger, or is in the anticipate "
                         "buy-zone below the band awaiting a momentum flip. This is a proximity "
                         "state, not a recommendation.",
    "IN POSITION": "**The simulated model already holds one position.** Price remains above the "
                   "band while the model continues its trend-holding state; this is not a fresh "
                   "entry signal or recommendation.",
    "SELL / EXIT": "**The simulated model produced an exit state** after a band loss or "
                   "close-threshold breach. Signals are evaluated on the close and modeled fills "
                   "occur at the next open, which can gap beyond the threshold.",
    "WATCH": "**The simulated model is flat with no current entry signal.** Price remains far "
             "from the model's entry conditions.",
    "SKIPPED": "The simulated strategy did not run because acquired price history was too short "
               "or no configuration produced a trade.",
    "ERROR": "The data or model pipeline failed for this row; see `error_stage` for provenance.",
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
    for g in ["BUY NOW", "CLOSE TO ENTERING", "IN POSITION", "SELL / EXIT", "WATCH", "SKIPPED", "ERROR"]:
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

    errors = df[df["group"] == "ERROR"]
    if not errors.empty:
        out.append(f"## ERROR  ({len(errors)})\n")
        out.append(GROUP_BLURB["ERROR"] + "\n")
        out.append(_md_table(errors, ["group_rank", "ticker", "name", "error_stage",
                                      "error_type", "error_message", "note"]))

    return "\n".join(out)
