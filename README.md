# Trading Strategy Research Demo

A small, inspectable Python/Jupyter project for exploring long-only technical-analysis models on stocks, ETFs, and Yahoo Finance-compatible symbols. It includes four single-symbol parameter-sweep notebooks, two universe screeners, reusable model code, and command-line entry points.

This repository is presented as research software, not as a trading system. Labels such as `BUY NOW`, `SELL / EXIT`, and `HOLDING` are model-state names inherited by the reports; they are **not recommendations**. Historical results are in-sample simulations and do not establish a future edge.

## Project map

### Notebooks

| File | Scope |
| --- | --- |
| [`bmsb_strategy.ipynb`](bmsb_strategy.ipynb) | Single-symbol Bull Market Support Band variants on daily and weekly bars. Sweeps band lengths, entry mode, RSI threshold, close-exit threshold, and confirmation window. |
| [`bollinger_strategy.ipynb`](bollinger_strategy.ipynb) | Single-symbol Bollinger lower-band entry / middle-band reversion model, daily and weekly. |
| [`ichimoku_strategy.ipynb`](ichimoku_strategy.ipynb) | Single-symbol long-only Ichimoku cloud-regime model, daily and weekly. |
| [`hybrid_strategy.ipynb`](hybrid_strategy.ipynb) | Single-symbol Ichimoku regime filter plus Bollinger pullback entry, daily and weekly. |
| [`wsb_bmsb_screener.ipynb`](wsb_bmsb_screener.ipynb) | Notebook frontend for the weekly WSB BMSB screener, with an optional section for the current daily dip-and-ride model. |
| [`daily_screener.ipynb`](daily_screener.ipynb) | Notebook frontend for the daily dip-and-ride universe screen and simplified portfolio simulation. |

The four strategy notebooks are intentionally self-contained for readability. The two screener notebooks use the `wsb_screener` package and therefore reflect the reusable CLI implementation.

### Package and CLIs

`wsb_screener/` separates data access, model calculations, cross-sectional classification, reporting, and command orchestration:

```text
run.py / run_quant.py       command orchestration and file output
        |
data.py                     WSB/popular universes + Yahoo history
        |
bmsb_core.py                weekly BMSB model and parameter sweep
quant_core.py               daily features, one-position backtest, portfolio simulation
        |
screener.py                 weekly BMSB model-state buckets
quant_screener.py           daily position-aware model-state buckets
        |
report.py / quant_report.py Markdown rendering
```

Two module CLIs are available:

```bash
# Weekly BMSB: current WSB mention universe, 10 years of weekly data
python -m wsb_screener.run --top 200 --outdir results

# Daily dip-and-ride: popular, WSB, or combined universe
python -m wsb_screener.run_quant --source both --top 120 --popular 120 \
  --period 5y --stop 0.06 --ride chandelier --outdir results
```

After installation, equivalent console commands are `trading-bmsb-screen` and `trading-quant-screen`. Run either command with `--help` for the complete option list.

`--stop` is retained as the CLI option name for compatibility, but it configures a **close-exit trigger**, not a hard stop order. `QuantConfig` is passed explicitly from the CLI through the screener and core simulation, so per-ticker screens and the portfolio use the same exit and ride settings.

## Model behavior

### Weekly BMSB sweep

For each ticker, the BMSB screener evaluates a fixed grid of band lengths, entry modes, RSI filters, close-exit thresholds, and reclaim windows. It prefers configurations producing 8–15 historical trades and ranks them by `Total P&L × Win Rate`; if none meet the trade-count window, it falls back to configurations nearest its midpoint. This is per-ticker in-sample optimization and is especially exposed to curve fitting.

### Daily dip-and-ride model

The daily model uses one fixed feature set across tickers:

- dip trigger: RSI-2 below 10 and/or price at least 1.5 standard deviations below the 20-SMA/21-EMA band midpoint;
- descriptive score: oversold, band stretch, volume, reversal, and trend components;
- entry: next open after a dip trigger, while flat;
- management: one open position per ticker—**no pyramiding or add-on sizing**;
- exits: an entry-relative close threshold, a selected trailing close threshold (`chandelier`, `chandelier_wide`, `pct`, or `sma50`), or a 250-bar time cap.

A fresh dip while the model is already holding remains `HOLDING (RIDE)` and is noted as informational. It is never labeled as a new entry because the backtest does not model pyramiding. If the latest close crosses an active exit threshold, the row becomes `EXIT PENDING` until the next open rather than remaining a holding row.

Unexpected per-ticker model failures are emitted as `ERROR` rows. Portfolio results include requested/backtested ticker counts and structured model failures instead of silently treating failures as normal flat rows.

## Execution assumptions and gap risk

All notebook and package strategies decide from completed bars and simulate fills at the **next available open**. Percentage and trailing thresholds are therefore close-triggered next-open exits—not hard, fixed-price, intraday, or exchange-resting stop orders. Overnight gaps can make the realized exit substantially worse than the configured threshold.

The simulations also omit commissions, spread, slippage, liquidity constraints, taxes, borrow constraints, market impact, order rejection, and intrabar path. Open trades may be marked at the final close for per-ticker diagnostics but are excluded from completed-trade portfolio results.

## Setup

Python 3.10 or newer is required.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e ".[notebooks]"
```

For the original requirements workflow:

```bash
pip install -r requirements.txt
```

Then launch `jupyter notebook` from the repository root, or run either CLI. Both screeners use live external data and may take several minutes; they were not executed as part of the offline project cleanup.

## Data and outputs

- WSB mentions: [ApeWisdom](https://apewisdom.io/) public API.
- General universe: a checked-in curated list of popular/liquid US names and ETFs.
- Prices: Yahoo Finance via `yfinance`, requested with `auto_adjust=True`.
- Generated CSV and Markdown reports: `results/` (ignored by Git).

ApeWisdom and Yahoo Finance can change, rate-limit, omit, revise, or delist data. The current-universe screen applies today's membership/attention list to historical bars, introducing selection and survivorship effects. Symbols also have unequal history. Consequently, reruns on different dates, provider versions, or environments are not expected to reproduce identical tables.

`requirements.txt` and `pyproject.toml` specify compatible dependency ranges, not a lockfile. For a frozen experiment, record the run date, universe response, raw price data, Python version, and resolved package versions.

## Research limitations

- Parameter sweeps select winners on the same history used to report them; there is no train/validation/test split.
- Profit factor, expectancy, win rate, and rankings are descriptive and can be unstable with small samples.
- The simplified portfolio simulation is not an execution engine and does not enforce every real-world capital, scheduling, or venue constraint.
- Corporate-action handling depends on Yahoo's adjusted data.
- Stored notebook outputs, where present, are snapshots from earlier runs and may not match current market data; rerun deliberately when network access is acceptable.
- No claim of profitability, robustness, or suitability is made.

## Disclaimer

**For educational and research use only. Nothing in this repository is financial advice, an offer, or a solicitation. Do not use model labels or historical results as the sole basis for an investment decision. Past performance does not predict future results, and loss of principal is possible.**
