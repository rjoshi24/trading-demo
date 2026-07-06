"""
screener.py
===========
Runs the BMSB strategy from `bmsb_strategy.ipynb` across many tickers and
classifies each one by how ready it is to buy *right now*.

Per ticker (weekly candles, the standard BMSB timeframe, same as the
notebook's daily-signal cell):
  1. Sweep the W_GRID parameter grid  (bmsb_sweep_fast)
  2. Pick the best config with the notebook's rule: keep 8-15 trade configs,
     rank by Score = Total P&L x Win Rate  (filter_window)
  3. Evaluate the live BUY/SELL/HOLD signal for the latest bar (bmsb_live)
  4. Measure proximity-to-trigger and assign a buy-readiness bucket

Buckets:
  BUY NOW            - the strategy fires a fresh BUY on the latest bar
  CLOSE TO ENTERING  - flat, not firing yet, but price is within NEAR_PCT of
                       the entry trigger (or already in the anticipate zone)
  IN POSITION        - a position is open and the strategy says HOLD (riding)
  SELL / EXIT        - a position is open and the strategy says SELL
  WATCH              - flat and still far from any trigger
"""
from __future__ import annotations
import pandas as pd

from .bmsb_core import (
    bmsb_sweep_fast, filter_window, bmsb_live,
    MIN_TRADES, MAX_TRADES, RANK_BY,
)

# Weekly sweep grid -- identical to W_GRID in bmsb_strategy.ipynb
W_GRID = ([15, 20, 25], [21, 30, 40], ["anticipate", "breakout", "reclaim"],
          [40, 45, 50], [0.08, 0.12], [4, 6])

MIN_BARS = 35          # need enough weekly bars for the band + a few trades
NEAR_PCT = 6.0         # within this % of the trigger => "close to entering"


def _need_move_pct(mode, sig):
    """Signed % price move needed to reach the entry trigger boundary.
    >0 => price must rise, <0 => price must fall, ~0 => already at/through it."""
    if mode in ("breakout", "hybrid_e"):
        return sig["gap_top_pct"]            # rise to clear the band top
    if mode == "reclaim":
        return sig["gap_bot_pct"]            # rise to reclaim the band bottom
    # anticipate: buys while BELOW the band on a momentum flip
    if sig["pos_vs_band"] == "below":
        return 0.0                            # already in the zone, waiting on momentum
    return sig["gap_bot_pct"]                 # must fall back under the band (negative)


def classify(sig, mode, rsi_buy):
    """Return (group, readiness_score, need_move_pct, proximity_pct, note)."""
    rec = sig["recommendation"]
    need = _need_move_pct(mode, sig)
    prox = abs(need)

    # --- in a position already ---
    if sig["in_position"]:
        if rec.startswith("SELL"):
            return "SELL / EXIT", 0.0, need, prox, rec
        return "IN POSITION", 50.0, need, prox, rec

    # --- fresh buy signal on the latest bar ---
    if rec.startswith("BUY"):
        return "BUY NOW", 100.0, need, prox, rec

    # --- flat: how close is it to triggering? ---
    mom_bonus = (5 if sig["rsi_rising"] else 0) + (5 if sig["up_close"] else 0)

    if mode == "anticipate":
        # "close" = already below the band and inside (or just above) the RSI buy filter
        in_zone = (sig["pos_vs_band"] == "below" and sig["rsi"] < rsi_buy + 3)
        if in_zone:
            score = 70 + mom_bonus - min(prox, 10) * 1.0   # deeper below = a touch less ready
            return "CLOSE TO ENTERING", round(min(score, 98), 1), need, prox, \
                "below band in RSI buy-zone; needs an up-close with RSI turning up"
    else:
        # breakout / reclaim: close if within NEAR_PCT below the trigger
        if 0 <= need <= NEAR_PCT:
            score = 55 + (NEAR_PCT - need) / NEAR_PCT * 35 + mom_bonus
            trig = "band top" if mode in ("breakout", "hybrid_e") else "band bottom"
            return "CLOSE TO ENTERING", round(min(score, 98), 1), need, prox, \
                f"{need:.1f}% below the {trig}; a close above it triggers entry"

    # --- flat and far ---
    # readiness fades with distance from the trigger
    score = max(5.0, 45 - prox)
    return "WATCH", round(score, 1), need, prox, "flat, far from the entry trigger"


def screen_ticker(ticker, weekly, meta=None):
    """Full pipeline for one ticker. Returns a flat dict row (or an error row)."""
    meta = meta or {}
    base = {"ticker": ticker, "name": meta.get("name", ""),
            "wsb_rank": meta.get("rank"), "mentions": meta.get("mentions")}

    if weekly is None or len(weekly) < MIN_BARS:
        return {**base, "group": "SKIPPED", "note": "insufficient price history",
                "bars": 0 if weekly is None else len(weekly)}

    sw = bmsb_sweep_fast(weekly, *W_GRID)
    if sw.empty:
        return {**base, "group": "SKIPPED", "note": "no trades in any config",
                "bars": len(weekly)}

    w, fell_back = filter_window(sw, MIN_TRADES, MAX_TRADES, RANK_BY)
    b = w.iloc[0]
    cfg = dict(sma=int(b.SMA), ema=int(b.EMA), mode=b.Mode, rsi=int(b.RSIbuy),
               stop=float(b.Stop), cbars=int(b.Cbars))

    sig = bmsb_live(weekly, cfg["sma"], cfg["ema"], cfg["mode"],
                    cfg["rsi"], cfg["stop"], cfg["cbars"])

    group, readiness, need, prox, note = classify(sig, cfg["mode"], cfg["rsi"])

    return {
        **base,
        "group": group,
        "readiness": readiness,
        "recommendation": sig["recommendation"],
        "close": sig["close"],
        "band_bot": sig["band_bot"],
        "band_top": sig["band_top"],
        "pos_vs_band": sig["pos_vs_band"],
        "rsi": sig["rsi"],
        "need_move_%": round(need, 2),
        "proximity_%": round(prox, 2),
        "mode": cfg["mode"],
        "sma": cfg["sma"], "ema": cfg["ema"], "rsi_buy": cfg["rsi"],
        "stop": cfg["stop"], "cbars": cfg["cbars"],
        "bt_trades": int(b["Total Trades"]),
        "bt_winrate_%": float(b["Win Rate %"]),
        "bt_pnl_$": float(b["Total P&L $"]),
        "bt_profit_factor": float(b["Profit Factor"]),
        "bt_score": round(float(b["Score"]), 1),
        "bt_in_window": not fell_back,
        "signal_date": sig["date"],
        "bars": len(weekly),
        "note": note,
    }


# group ordering + within-group sort keys
GROUP_ORDER = ["BUY NOW", "CLOSE TO ENTERING", "IN POSITION", "SELL / EXIT", "WATCH", "SKIPPED"]


def rank_group(df_group, group):
    if group == "BUY NOW":
        return df_group.sort_values("bt_score", ascending=False)
    if group == "CLOSE TO ENTERING":
        return df_group.sort_values(["readiness", "proximity_%"], ascending=[False, True])
    if group == "IN POSITION":
        return df_group.sort_values("bt_score", ascending=False)
    if group == "SELL / EXIT":
        return df_group.sort_values("need_move_%", ascending=True)
    if group == "WATCH":
        return df_group.sort_values("proximity_%", ascending=True)
    return df_group.sort_values("mentions", ascending=False)


def run_screener(history: dict, metas: dict, progress_every: int = 25):
    """history: {ticker: weekly df}, metas: {ticker: {rank,mentions,name}}.
    Returns a single ranked DataFrame."""
    rows = []
    tickers = list(metas.keys())
    for i, tk in enumerate(tickers, 1):
        try:
            row = screen_ticker(tk, history.get(tk), metas.get(tk))
        except Exception as e:
            row = {"ticker": tk, "name": metas.get(tk, {}).get("name", ""),
                   "wsb_rank": metas.get(tk, {}).get("rank"),
                   "mentions": metas.get(tk, {}).get("mentions"),
                   "group": "SKIPPED", "note": f"error: {e!r}"}
        rows.append(row)
        if progress_every and i % progress_every == 0:
            print(f"  ...screened {i}/{len(tickers)}")
    df = pd.DataFrame(rows)

    # order by group then within-group rank
    parts = []
    for g in GROUP_ORDER:
        sub = df[df["group"] == g]
        if not sub.empty:
            parts.append(rank_group(sub, g))
    ordered = pd.concat(parts, ignore_index=True) if parts else df
    ordered.insert(0, "group_rank", ordered.groupby("group").cumcount() + 1)
    return ordered
