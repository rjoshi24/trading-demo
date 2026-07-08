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
| `quant_core.py` | **Composite swing model** (Part 2): all indicators + a 0–100 score + a ≥10-day-hold swing backtest. |
| `quant_screener.py` | Per-ticker pipeline for the composite model → BUY NOW / CLOSE TO BUY / HOLD / SELL / WATCH buckets. |
| `quant_report.py` | Renders the composite-model Markdown report. |

---

## Part 2 — Composite Quant Swing Model (daily, hold ≥ 10 days)

A second, broader model that runs on **daily** candles (open it every day) and is tuned for a
swing horizon of **at least 10 trading days**. Instead of a per-ticker parameter sweep, it
applies **one fixed, research-grounded parameter set** to every ticker and blends a handful of
signals into a single transparent **0–100 score** — so it's simpler and much less curve-fit.

### What goes into the score (and why)

| Signal | Captures | Grounding |
|---|---|---|
| **Golden cross regime** (50/200 SMA) + price > 200-SMA | trade with the long-term trend | Faber (2007), *A Quantitative Approach to Tactical Asset Allocation* |
| **Bull Market Support Band** (20 SMA / 21 EMA) | short-term trend support / reclaim | same band as the weekly BMSB chart |
| **12-1 time-series momentum** | trend persistence over the past year | Moskowitz, Ooi & Pedersen (2012); Jegadeesh & Titman (1993) |
| **Volatility squeeze** (Bollinger inside Keltner) | coiled energy that precedes a big move | Bollinger; John Carter's TTM Squeeze |
| **20-day breakout + volume** | trend ignition on real participation | Turtle-style Donchian breakout |
| **RSI(14) & MACD(12,26,9)** | momentum confirmation / overbought guard | standard |

### Buckets

| Bucket | Meaning |
|---|---|
| `BUY NOW` | Regime bullish, score clears the buy threshold, **and** a fresh trigger fired today (20-day breakout, band reclaim, or squeeze firing up). Act at next open. |
| `CLOSE TO BUY` | Bullish + high score but **no trigger yet** — a squeeze is coiled, price is within a few % of the 20-day high, or it's hugging the band. Watch these. |
| `HOLD (UPTREND)` | Already above the band and trending; hold if long, a new buy is chasing. |
| `SELL / EXIT` | A **fresh** exit: just lost the 20/21 band (after being above it) or a fresh death cross below the 200-SMA. |
| `WATCH` | Regime and/or score too weak. Nothing to do. |
| `SKIPPED` | Not enough clean daily history. |

Each row also carries a **≥10-day-hold swing backtest** (win rate, expectancy per $1,000
trade, avg bars held) so you can gauge each name's historical quality. The backtest enters on
the trigger, holds **at least 10 bars**, then exits on a band loss / ATR trailing stop / max
hold (an emergency % stop can fire earlier).

Outputs land in `results/`:
- `wsb_quant_screen.csv` — full ranked table
- `wsb_quant_report.md` — grouped, human-readable report

## Caveat

The "best" config per ticker is the top of a parameter sweep, so it is **partly curve-fit** to the
test window. Treat the buckets as a research starting point, not trade instructions.
**Past performance does not guarantee future results — this is not financial advice.**
