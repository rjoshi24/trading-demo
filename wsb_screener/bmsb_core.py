"""
bmsb_core.py
============
Faithful port of the BMSB (Bull Market Support Band) engine from
`bmsb_strategy.ipynb`, packaged for reuse by the WSB screener.

The band = SMA(sma_len) + EMA(ema_len); band_top = max(SMA,EMA),
band_bot = min(SMA,EMA). Entry modes: anticipate / reclaim / breakout /
hybrid_e. Exits: fakeout-stop, confirm-fail, band-loss.

Nothing here changes the strategy math from the notebook -- it is copied
so the screener produces the same signals the notebook would.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

CAPITAL = 1000.0
MIN_TRADES = 8
MAX_TRADES = 15
RANK_BY = "Score"


# ----------------------------- indicators -----------------------------
def rsi(series: pd.Series, n: int = 14) -> pd.Series:
    d = series.diff()
    up = d.clip(lower=0).rolling(n).mean()
    dn = (-d.clip(upper=0)).rolling(n).mean()
    rs = up / dn.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def bmsb_prep(df: pd.DataFrame, sma_len: int, ema_len: int, fast_ema: int = 10) -> pd.DataFrame:
    d = df.copy()
    d["SMA"] = d["Close"].rolling(sma_len).mean()
    d["EMA"] = d["Close"].ewm(span=ema_len, adjust=False).mean()
    d["band_top"] = d[["SMA", "EMA"]].max(axis=1)
    d["band_bot"] = d[["SMA", "EMA"]].min(axis=1)
    d["RSI"] = rsi(d["Close"], 14)
    d["fast"] = d["Close"].ewm(span=fast_ema, adjust=False).mean()
    return d.dropna().reset_index(drop=True)


# ----------------------------- backtest --------------------------------
def bmsb_backtest(df, sma_len, ema_len, mode="anticipate", rsi_buy=45,
                  stop_pct=0.12, confirm_bars=6, capital=CAPITAL):
    d = bmsb_prep(df, sma_len, ema_len)
    trades = []
    pos = None
    for i in range(1, len(d) - 1):
        r = d.iloc[i]; p = d.iloc[i - 1]; nxt = d.iloc[i + 1]
        if pos is None:
            ant = (r.Close < r.band_bot and r.RSI < rsi_buy and r.RSI > p.RSI and r.Close > p.Close)
            brk = r.Close > r.band_top
            rec = (p.Close < p.band_bot and r.Close > r.band_bot)
            fire = {"anticipate": ant, "breakout": brk, "reclaim": rec, "hybrid_e": ant or brk}[mode]
            if fire:
                pos = {"entry_date": nxt.Date, "entry_price": nxt.Open, "entry_i": i + 1,
                       "reclaimed": bool(r.Close > r.band_bot)}
        else:
            if r.Close > r.band_bot:
                pos["reclaimed"] = True
            held = i - pos["entry_i"]
            exit_now, reason = False, ""
            if r.Close <= pos["entry_price"] * (1 - stop_pct):
                exit_now, reason = True, "fakeout-stop"
            elif (not pos["reclaimed"]) and held >= confirm_bars:
                exit_now, reason = True, "confirm-fail"
            elif pos["reclaimed"] and r.Close < r.band_bot:
                exit_now, reason = True, "band-loss"
            if exit_now:
                ep = nxt.Open; ret = (ep - pos["entry_price"]) / pos["entry_price"]
                trades.append({**pos, "exit_date": nxt.Date, "exit_price": ep, "ret": ret,
                               "pnl": ret * capital, "bars": (i + 1) - pos["entry_i"], "reason": reason})
                pos = None
    if pos is not None:
        last = d.iloc[-1]; ret = (last.Close - pos["entry_price"]) / pos["entry_price"]
        trades.append({**pos, "exit_date": last.Date, "exit_price": last.Close, "ret": ret,
                       "pnl": ret * capital, "bars": (len(d) - 1) - pos["entry_i"], "reason": "open"})
    return d, pd.DataFrame(trades)


def compute_stats(t, capital=CAPITAL):
    z = {"Total Trades": 0, "Win Rate %": 0, "Total P&L $": 0, "Avg Win $": 0, "Avg Loss $": 0,
         "Profit Factor": 0, "Expectancy $": 0, "Avg Bars Held": 0, "Max Drawdown $": 0, "Return/Trade %": 0}
    if t.empty:
        return z
    w = t[t.pnl > 0]; l = t[t.pnl <= 0]
    gp = w.pnl.sum(); gl = abs(l.pnl.sum())
    eq = t.pnl.cumsum(); dd = (eq - eq.cummax()).min()
    return {"Total Trades": len(t),
            "Win Rate %": round(len(w) / len(t) * 100, 1),
            "Total P&L $": round(t.pnl.sum(), 2),
            "Avg Win $": round(w.pnl.mean(), 2) if len(w) else 0.0,
            "Avg Loss $": round(l.pnl.mean(), 2) if len(l) else 0.0,
            "Profit Factor": round(gp / gl, 2) if gl > 0 else float("inf"),
            "Expectancy $": round(t.pnl.mean(), 2),
            "Avg Bars Held": round(t.bars.mean(), 1),
            "Max Drawdown $": round(dd, 2),
            "Return/Trade %": round(t.ret.mean() * 100, 2)}


def filter_window(res, lo=MIN_TRADES, hi=MAX_TRADES, rank_by=RANK_BY):
    w = res[(res["Total Trades"] >= lo) & (res["Total Trades"] <= hi)].copy()
    fell_back = False
    if w.empty:
        mid = (lo + hi) / 2
        res = res.assign(_d=(res["Total Trades"] - mid).abs())
        w = res.sort_values("_d").head(8).drop(columns="_d").copy()
        fell_back = True
    w["Score"] = w["Total P&L $"] * (w["Win Rate %"] / 100.0)
    asc = rank_by in ("Max Drawdown $",)
    w = w.sort_values(rank_by, ascending=asc).reset_index(drop=True)
    return w, fell_back


def bmsb_sweep(df, sma_grid, ema_grid, modes, rsi_grid, stop_grid, cbar_grid):
    rows = []
    for sma in sma_grid:
        for ema in ema_grid:
            for m in modes:
                for rb in rsi_grid:
                    for st in stop_grid:
                        for cb in cbar_grid:
                            _, t = bmsb_backtest(df, sma, ema, m, rb, st, cb)
                            s = compute_stats(t)
                            if s["Total Trades"] == 0:
                                continue
                            rows.append({"SMA": sma, "EMA": ema, "Mode": m, "RSIbuy": rb,
                                         "Stop": st, "Cbars": cb, **s})
    return pd.DataFrame(rows)


# ----------------------------- live signal -----------------------------
def bmsb_live(df, sma_len, ema_len, mode, rsi_buy, stop_pct, confirm_bars):
    """Same as the notebook's bmsb_live, but also returns proximity features
    so the screener can rank 'close to entering' names."""
    d, t = bmsb_backtest(df, sma_len, ema_len, mode, rsi_buy, stop_pct, confirm_bars)
    r = d.iloc[-1]; p = d.iloc[-2]

    close = float(r.Close); band_bot = float(r.band_bot); band_top = float(r.band_top)
    rsi_now = float(r.RSI); rsi_prev = float(p.RSI)
    rsi_rising = rsi_now > rsi_prev
    up_close = close > float(p.Close)

    if close < band_bot:
        pos_vs_band = "below"
    elif close > band_top:
        pos_vs_band = "above"
    else:
        pos_vs_band = "inside"

    gap_top_pct = (band_top - close) / close * 100.0   # >0 => below the top
    gap_bot_pct = (band_bot - close) / close * 100.0   # >0 => below the bottom

    in_pos = (not t.empty) and (t.iloc[-1]["reason"] == "open")
    if in_pos:
        ep = float(t.iloc[-1]["entry_price"])
        if close <= ep * (1 - stop_pct):
            rec = "SELL (fakeout stop hit)"
        elif close < band_bot:
            rec = "SELL (lost the band)"
        else:
            rec = "HOLD (in position - riding the move)"
        state = "IN position"
    else:
        ant = (close < band_bot and rsi_now < rsi_buy and rsi_rising and up_close)
        brk = close > band_top
        rec_ = (float(p.Close) < float(p.band_bot) and close > band_bot)
        fire = {"anticipate": ant, "breakout": brk, "reclaim": rec_, "hybrid_e": ant or brk}[mode]
        rec = "BUY (entry signal - act at next open)" if fire else "HOLD (flat - waiting for entry)"
        state = "FLAT"

    return {"date": str(pd.Timestamp(r.Date).date()), "close": round(close, 2),
            "band_bot": round(band_bot, 2), "band_top": round(band_top, 2),
            "rsi": round(rsi_now, 1), "rsi_rising": rsi_rising, "up_close": up_close,
            "pos_vs_band": pos_vs_band, "gap_top_pct": round(gap_top_pct, 2),
            "gap_bot_pct": round(gap_bot_pct, 2), "state": state, "recommendation": rec,
            "in_position": in_pos}



# ============================================================================
# FAST PATH -- numpy port of the backtest for the sweep only.
# Produces identical trade P&L / returns / bars to bmsb_backtest, but avoids
# per-row .iloc access and caches the band prep per (sma,ema) pair.
# Used purely to score configs quickly; the final chosen config is always
# re-run through the exact notebook bmsb_backtest / bmsb_live above.
# ============================================================================
def _prep_arrays(df, sma_len, ema_len):
    d = bmsb_prep(df, sma_len, ema_len)
    return {
        "Close": d["Close"].to_numpy(dtype=float),
        "Open": d["Open"].to_numpy(dtype=float),
        "band_bot": d["band_bot"].to_numpy(dtype=float),
        "band_top": d["band_top"].to_numpy(dtype=float),
        "RSI": d["RSI"].to_numpy(dtype=float),
        "n": len(d),
    }


def _backtest_fast(a, mode, rsi_buy, stop_pct, confirm_bars, capital=CAPITAL):
    Close = a["Close"]; Open = a["Open"]; bb = a["band_bot"]; bt = a["band_top"]; RSI = a["RSI"]
    n = a["n"]
    pnl = []; ret = []; bars = []
    pos = None  # (entry_price, entry_i, reclaimed)
    for i in range(1, n - 1):
        c = Close[i]; cp = Close[i - 1]
        if pos is None:
            if mode == "anticipate":
                fire = (c < bb[i] and RSI[i] < rsi_buy and RSI[i] > RSI[i - 1] and c > cp)
            elif mode == "breakout":
                fire = c > bt[i]
            elif mode == "reclaim":
                fire = (cp < bb[i - 1] and c > bb[i])
            else:  # hybrid_e
                fire = ((c < bb[i] and RSI[i] < rsi_buy and RSI[i] > RSI[i - 1] and c > cp) or c > bt[i])
            if fire:
                pos = [Open[i + 1], i + 1, bool(c > bb[i])]
        else:
            if c > bb[i]:
                pos[2] = True
            held = i - pos[1]
            exit_now = False
            if c <= pos[0] * (1 - stop_pct):
                exit_now = True
            elif (not pos[2]) and held >= confirm_bars:
                exit_now = True
            elif pos[2] and c < bb[i]:
                exit_now = True
            if exit_now:
                ep = Open[i + 1]; rr = (ep - pos[0]) / pos[0]
                ret.append(rr); pnl.append(rr * capital); bars.append((i + 1) - pos[1])
                pos = None
    if pos is not None:
        last = Close[n - 1]; rr = (last - pos[0]) / pos[0]
        ret.append(rr); pnl.append(rr * capital); bars.append((n - 1) - pos[1])
    return np.array(pnl), np.array(ret), np.array(bars)


def _stats_fast(pnl, ret, bars):
    if len(pnl) == 0:
        return None
    wins = pnl[pnl > 0]; losses = pnl[pnl <= 0]
    gp = wins.sum(); gl = abs(losses.sum())
    return {"Total Trades": int(len(pnl)),
            "Win Rate %": round(len(wins) / len(pnl) * 100, 1),
            "Total P&L $": round(float(pnl.sum()), 2),
            "Profit Factor": round(gp / gl, 2) if gl > 0 else float("inf"),
            "Expectancy $": round(float(pnl.mean()), 2),
            "Avg Bars Held": round(float(bars.mean()), 1),
            "Return/Trade %": round(float(ret.mean()) * 100, 2)}


def bmsb_sweep_fast(df, sma_grid, ema_grid, modes, rsi_grid, stop_grid, cbar_grid):
    """Same result columns as bmsb_sweep (minus a couple of unused stats),
    but caches the band prep per (sma,ema) and loops on numpy arrays."""
    rows = []
    prep_cache = {}
    for sma in sma_grid:
        for ema in ema_grid:
            key = (sma, ema)
            if key not in prep_cache:
                prep_cache[key] = _prep_arrays(df, sma, ema)
            a = prep_cache[key]
            if a["n"] < 5:
                continue
            for m in modes:
                for rb in rsi_grid:
                    for st in stop_grid:
                        for cb in cbar_grid:
                            pnl, ret, bars = _backtest_fast(a, m, rb, st, cb)
                            s = _stats_fast(pnl, ret, bars)
                            if s is None:
                                continue
                            rows.append({"SMA": sma, "EMA": ema, "Mode": m, "RSIbuy": rb,
                                         "Stop": st, "Cbars": cb, **s})
    return pd.DataFrame(rows)
