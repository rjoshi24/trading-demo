# WSB Top-200 BMSB Buy-Readiness Screener

Applies the **Bull Market Support Band** strategy from [`bmsb_strategy.ipynb`](../bmsb_strategy.ipynb)
across the **top 200 most-mentioned r/wallstreetbets tickers** and groups/ranks every name by how
ready it is to buy *right now*.

## What it does

For each ticker (weekly candles, 10 years — the standard BMSB timeframe):

1. **Sweep** the same `W_GRID` parameter grid as the notebook.
2. Pick the **best config** with the notebook rule: keep configs that take 8–15 trades, rank by
   `Score = Total P&L × Win Rate`.
3. Evaluate the **live BUY / SELL / HOLD** signal on the latest bar (the notebook's `bmsb_live`).
4. Measure **proximity-to-trigger** and drop the ticker into a bucket.

### Buckets

| Bucket | Meaning |
|---|---|
| `BUY NOW` | Fresh entry signal fires on the latest weekly bar — actionable (act at next open). |
| `CLOSE TO ENTERING` | Flat but within ~6% of the entry trigger, or already in the `anticipate` buy-zone below the band waiting on a momentum flip. Watch these. |
| `IN POSITION` | Price is above the band and the strategy is already long and holding. A new buyer here is chasing an extended move. |
| `SELL / EXIT` | The strategy would be exiting (lost the band or hit the fakeout stop). |
| `WATCH` | Flat and still far from any trigger. |
| `SKIPPED` | Not enough clean price history. |

Key columns: `readiness` (0–100, how close to a buy), `need_move_%` (% price move to hit the
trigger; negative = price is already past it), plus the chosen config and its backtest quality
(`bt_trades`, `bt_winrate_%`, `bt_pnl_$`, `bt_score`).

## Data sources

- **WSB mentions** — [ApeWisdom](https://apewisdom.io) `wallstreetbets` filter (free, ranked by mention count).
- **Prices** — Yahoo Finance via `yfinance` (10y weekly, auto-adjusted).

## Run it

```bash
pip install -r ../requirements.txt

# command line
python -m wsb_screener.run --top 200

# or interactively
jupyter notebook ../wsb_bmsb_screener.ipynb
```

Outputs land in `results/`:
- `wsb_bmsb_screen.csv` — full ranked table
- `wsb_bmsb_report.md` — grouped, human-readable report

## Files

| File | Purpose |
|---|---|
| `bmsb_core.py` | Faithful port of the notebook's BMSB math + a numpy fast-path sweep (~200× faster, identical results) used to score 200 tickers quickly. |
| `data.py` | Fetch WSB tickers (ApeWisdom) and batch-download price history (yfinance). |
| `screener.py` | Per-ticker pipeline: sweep → best config → live signal → proximity → bucket. |
| `report.py` | Renders the grouped Markdown report. |
| `run.py` | End-to-end CLI runner. |

## Caveat

The "best" config per ticker is the top of a parameter sweep, so it is **partly curve-fit** to the
test window. Treat the buckets as a research starting point, not trade instructions.
**Past performance does not guarantee future results — this is not financial advice.**
