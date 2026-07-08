"""
quant_report.py
===============
Render the composite-swing-model screen (`quant_screener.run_screener` output)
into a readable Markdown report grouped by bucket.
"""
from __future__ import annotations
import datetime as dt
import pandas as pd

GROUP_BLURB = {
    "BUY NOW": "Regime is bullish, a **fresh entry trigger fired on the latest daily bar** "
               "(20-day breakout, band reclaim, or a squeeze firing up) and the composite score "
               "clears the buy threshold. Act at next open, size with the ATR stop.",
    "CLOSE TO BUY": "Bullish regime and a **high score, but no trigger yet** -- the setup is "
                    "building: a volatility squeeze is coiled, price is a few percent under the "
                    "20-day high, or it's hugging the support band. These are the watch-closely names.",
    "HOLD (UPTREND)": "Already **above the band and trending**. Hold if you are long; a new buyer "
                      "here is chasing an extended move (wait for a pullback to the band).",
    "SELL / EXIT": "An **exit condition is present** -- price lost the 20/21 support band, or a "
                   "death cross with price below the 200-SMA. If you hold it, the model says exit.",
    "WATCH": "No setup: regime and/or composite score too weak. Nothing to do yet.",
    "SKIPPED": "Not enough clean daily history to run the model.",
}

BUY_COLS = ["group_rank", "ticker", "name", "close", "score", "rsi", "mom_12_1_%",
            "squeeze_on", "vol_ratio", "band_bot", "band_top", "need_move_%",
            "bt_trades", "bt_winrate_%", "bt_expectancy_$", "note"]
NEAR_COLS = ["group_rank", "ticker", "name", "close", "score", "pos_vs_band",
             "prox_high_%", "squeeze_on", "rsi", "mom_12_1_%", "band_bot", "band_top", "note"]
HOLD_COLS = ["group_rank", "ticker", "name", "close", "score", "rsi", "mom_12_1_%",
             "band_bot", "band_top", "bt_winrate_%", "bt_expectancy_$"]
SELL_COLS = ["group_rank", "ticker", "name", "close", "score", "pos_vs_band",
             "band_bot", "band_top", "rsi", "note"]
WATCH_COLS = ["group_rank", "ticker", "name", "close", "score", "regime_ok",
              "pos_vs_band", "rsi", "mom_12_1_%"]


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
    out.append("# WSB Composite Swing-Model Screen\n")
    out.append(f"_Generated {now} | latest daily bar: **{signal_date}** | "
               f"universe: top {universe_n} r/wallstreetbets tickers by mention count_\n")
    out.append("> **Research only, not financial advice.** A single fixed, research-grounded "
               "parameter set is applied to every ticker (no per-ticker curve-fitting). Signals are "
               "tuned for a swing horizon of **>= 10 trading days**.\n")

    out.append("## The model in one paragraph\n")
    out.append("Each ticker gets a transparent **0-100 composite score** blending: the **golden-cross "
               "regime** (50/200 SMA) + long-trend filter, the **Bull Market Support Band** (20 SMA / "
               "21 EMA), **12-1 time-series momentum**, **MACD** and **RSI**, a **volatility squeeze** "
               "(Bollinger inside Keltner -- fires *before* big moves), and a **20-day breakout + "
               "volume** check. A ticker becomes **BUY NOW** only when the regime is bullish, the score "
               "is high, and a fresh entry trigger fires on the latest bar.\n")

    out.append("## How to read this\n")
    out.append("- **score** 0-100 = overall attractiveness (regime + momentum + setup).\n"
               "- **need_move_%** / **prox_high_%** = % move to the nearest trigger (the 20-day high "
               "or a band reclaim).\n"
               "- **squeeze_on** = volatility is coiled (a big move tends to follow).\n"
               "- **bt_*** = a >=10-day-hold swing backtest on this ticker (win rate, expectancy per "
               "$1,000 trade) so you can gauge each name's historical quality.\n")

    out.append("## Summary\n")
    out.append("| Group | Count |\n| --- | --- |")
    for g in ["BUY NOW", "CLOSE TO BUY", "HOLD (UPTREND)", "SELL / EXIT", "WATCH", "SKIPPED"]:
        if g in counts:
            out.append(f"| {g} | {counts[g]} |")
    out.append("")

    sections = [
        ("BUY NOW", BUY_COLS),
        ("CLOSE TO BUY", NEAR_COLS),
        ("HOLD (UPTREND)", HOLD_COLS),
        ("SELL / EXIT", SELL_COLS),
        ("WATCH", WATCH_COLS),
    ]
    for g, cols in sections:
        sub = df[df["group"] == g]
        out.append(f"## {g}  ({len(sub)})\n")
        out.append(GROUP_BLURB.get(g, "") + "\n")
        if g == "WATCH" and len(sub) > 40:
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
