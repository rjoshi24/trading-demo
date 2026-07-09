"""
data.py
=======
Data acquisition for the WSB screener:
  * top-N most-mentioned tickers on r/wallstreetbets (ApeWisdom API)
  * 10y OHLCV history from Yahoo Finance (yfinance), batch-downloaded

Kept separate from the strategy math so the screener stays readable.
"""
from __future__ import annotations
import time
import html
import requests
import pandas as pd
import yfinance as yf

APEWISDOM_URL = "https://apewisdom.io/api/v1.0/filter/wallstreetbets/page/{page}"

# Tickers ApeWisdom sometimes lists that are not tradable single equities on
# Yahoo, or that are noise. We keep it minimal and let yfinance failures prune
# the rest.
_SKIP = {"CEO", "USA", "WSB", "YOLO", "FD", "FDA", "CPI", "DD", "EV", "AI",
         "IMO", "ATH", "US", "IV", "OP", "PM", "AH", "RH", "ER", "GDP"}


# The most popular / most liquid US names in general (mega-caps, popular retail
# stocks, and the big ETFs) - so the screener isn't limited to WSB chatter.
# Curated, deduped, roughly by liquidity/popularity.
POPULAR_TICKERS = [
    # mega / large cap tech + leaders
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "GOOG", "META", "TSLA", "AVGO", "ORCL",
    "AMD", "NFLX", "ADBE", "CRM", "CSCO", "QCOM", "TXN", "INTC", "IBM", "AMAT",
    "MU", "INTU", "NOW", "UBER", "SHOP", "PLTR", "SMCI", "ARM", "PANW", "SNOW",
    # financials
    "JPM", "V", "MA", "BAC", "WFC", "GS", "MS", "C", "AXP", "SCHW", "BLK", "SPGI",
    "PYPL", "SOFI", "COIN", "HOOD",
    # healthcare
    "LLY", "UNH", "JNJ", "MRK", "ABBV", "PFE", "TMO", "ABT", "DHR", "BMY", "AMGN", "GILD",
    # consumer / staples / retail
    "WMT", "COST", "HD", "LOW", "PG", "KO", "PEP", "MCD", "SBUX", "NKE", "TGT",
    "DIS", "CMG", "LULU",
    # industrials / energy / materials
    "CAT", "GE", "BA", "HON", "UPS", "DE", "LMT", "RTX", "XOM", "CVX", "COP",
    "OXY", "SLB", "FCX", "NEM",
    # autos / EV / popular momentum
    "F", "GM", "RIVN", "NIO", "MSTR", "MARA", "RIOT", "DKNG", "ABNB", "RBLX",
    # comms / other
    "T", "VZ", "TMUS", "CMCSA",
    # big ETFs (index / sector / thematic)
    "SPY", "QQQ", "IWM", "DIA", "VTI", "XLK", "XLF", "XLE", "XLV", "XLY",
    "SMH", "SOXX", "ARKK", "GLD", "SLV", "TLT",
]


def get_popular_tickers(top_n: int = 120):
    """Return [{rank, ticker, mentions, name}, ...] for the most popular / liquid
    US names in general (mega-caps + popular stocks + big ETFs). `mentions` is a
    synthetic popularity rank-score so it plays nicely with the WSB schema."""
    seen, out = set(), []
    for i, tk in enumerate(POPULAR_TICKERS[:top_n]):
        if tk in seen:
            continue
        seen.add(tk)
        out.append({"rank": i + 1, "ticker": tk,
                    "mentions": len(POPULAR_TICKERS) - i, "name": tk, "source": "popular"})
    return out


def get_universe(source: str = "both", top_n: int = 200, popular_n: int = 120):
    """Build the scan universe.
      source = "popular" -> most popular US names + ETFs (no network beyond prices)
      source = "wsb"     -> top-N r/wallstreetbets tickers
      source = "both"    -> popular first, then WSB names not already included (deduped)
    Returns a list of dicts with rank/ticker/mentions/name."""
    src = (source or "both").lower()
    if src == "popular":
        return get_popular_tickers(popular_n)
    if src == "wsb":
        return get_wsb_tickers(top_n)

    pop = get_popular_tickers(popular_n)
    have = {d["ticker"] for d in pop}
    combined = list(pop)
    try:
        wsb = get_wsb_tickers(top_n)
    except Exception as e:
        print(f"  (WSB fetch failed, using popular list only: {e!r})")
        wsb = []
    for d in wsb:
        if d["ticker"] not in have:
            have.add(d["ticker"])
            d = {**d, "source": "wsb"}
            combined.append(d)
    return combined


def get_wsb_tickers(top_n: int = 200):
    """Return a list of dicts: [{rank, ticker, mentions, name}, ...] for the
    top-N most-mentioned r/wallstreetbets tickers (by mention count)."""
    out = []
    page = 1
    while len(out) < top_n and page <= 12:
        r = requests.get(APEWISDOM_URL.format(page=page), timeout=30)
        r.raise_for_status()
        data = r.json()
        for row in data.get("results", []):
            tk = row["ticker"].strip().upper()
            if tk in _SKIP:
                continue
            out.append({
                "rank": int(row["rank"]),
                "ticker": tk,
                "mentions": int(row.get("mentions", 0) or 0),
                "name": html.unescape(row.get("name", "") or ""),
            })
        if page >= int(data.get("pages", 1)):
            break
        page += 1
    return out[:top_n]


def yf_symbol(ticker: str) -> str:
    """Yahoo uses '-' where tickers use '.' (e.g. BRK.B -> BRK-B).
    Also drop a leading '$' that ApeWisdom occasionally includes."""
    return ticker.lstrip("$").replace(".", "-").strip().upper()


def _tidy(df: pd.DataFrame) -> pd.DataFrame | None:
    if df is None or df.empty:
        return None
    df = df[["Open", "High", "Low", "Close", "Volume"]].dropna().reset_index()
    df.rename(columns={df.columns[0]: "Date"}, inplace=True)
    return df if len(df) else None


def download_history(tickers, period="10y", interval="1wk", chunk=40, pause=0.5):
    """Batch-download OHLCV for many tickers. Returns {ticker: tidy DataFrame}.
    Tickers with no data are simply omitted."""
    ymap = {yf_symbol(t): t for t in tickers}
    ysyms = list(ymap.keys())
    result = {}
    for i in range(0, len(ysyms), chunk):
        batch = ysyms[i:i + chunk]
        try:
            raw = yf.download(batch, period=period, interval=interval,
                              auto_adjust=True, progress=False,
                              group_by="ticker", threads=True)
        except Exception as e:
            print(f"  batch {i//chunk} download error: {e!r}")
            continue
        for ys in batch:
            try:
                if len(batch) == 1:
                    sub = raw.copy()
                    if isinstance(sub.columns, pd.MultiIndex):
                        # with group_by="ticker" the OHLCV fields can be on either
                        # level depending on yfinance version/shape -> pick the level
                        # that actually holds Open/High/Low/Close.
                        fields = {"Open", "High", "Low", "Close", "Volume"}
                        if fields & set(sub.columns.get_level_values(0)):
                            sub.columns = sub.columns.get_level_values(0)
                        else:
                            sub.columns = sub.columns.get_level_values(-1)
                else:
                    sub = raw[ys].copy()
                tidy = _tidy(sub)
                if tidy is not None:
                    result[ymap[ys]] = tidy
            except Exception:
                continue
        time.sleep(pause)
    return result
