# Band Trading Strategies — Backtesters

Four self-contained Jupyter notebooks that backtest long-only "support band" strategies on
**daily and weekly** candles over the **past 10 years**, using free `yfinance` data.

Each notebook:
- sweeps many parameter combinations (the "thresholds"),
- keeps **only configs that take 8–15 trades**,
- ranks survivors by a blended **Score = Total P&L × Win Rate**,
- charts **only the best** config per timeframe (green ▲ BUY / red ▼ SELL, cumulative P&L panel, full stats footer),
- assumes **$1,000 per trade**,
- ends with a **daily BUY / SELL / HOLD signal** cell you can run every day.

All charts and stats are reproducible — change `TICKER` in the config cell (works for stocks and crypto like `BTC-USD`).

## Notebooks

| File | Strategy |
|---|---|
| `bmsb_strategy.ipynb` | **Bull Market Support Band** with an early-entry "anticipate" mode (buy *below* the band when momentum turns up) + a fakeout filter (% stop, reclaim-timeout, band-loss). Also charts the canonical 20 SMA / 21 EMA band. |
| `bollinger_strategy.ipynb` | **Bollinger Bands** — buy the lower-band dip, sell the reversion to the middle band, fakeout stop. |
| `ichimoku_strategy.ipynb` | **Ichimoku Cloud** — buy above the Kumo (bull regime), sell below it, fakeout stop. |
| `hybrid_strategy.ipynb` | **Hybrid** — Ichimoku cloud regime filter + Bollinger mean-reversion entry + cloud-loss exit. |

## Setup

```bash
pip install -r requirements.txt
jupyter notebook
```

Open any notebook and run the cells top to bottom. Edit the **CONFIG** cell to change the
ticker, date range, capital, the 8–15 trade window, the ranking metric, and the sweep grids.

## Important caveat

The "best" config is the top of a parameter sweep, so it is partly curve-fit to the test
window. Treat the top-5 tables as candidates and re-test on other tickers and periods before
trusting any of them. Past performance does not guarantee future results — this is for research,
not financial advice.
