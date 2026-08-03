# `wsb_screener` package

Reusable implementation behind this repository's weekly BMSB and daily dip-and-ride screeners. The canonical project overview, setup instructions, model assumptions, and research limitations are in the [root README](../README.md).

## Entry points

```bash
python -m wsb_screener.run --help
python -m wsb_screener.run_quant --help
```

- `run.py`: fetches the current WSB mention universe, downloads weekly history, runs the per-ticker BMSB parameter sweep, and writes CSV/Markdown output.
- `run_quant.py`: builds a popular/WSB/combined universe, downloads daily history, runs the fixed daily model, and writes screen plus simplified portfolio output.

## Modules

| Module | Responsibility |
| --- | --- |
| `data.py` | Universe construction, ApeWisdom access, Yahoo symbol normalization, and batched `yfinance` history. |
| `bmsb_core.py` | BMSB features, one-position backtest, parameter sweep, and latest model state. |
| `screener.py` | Weekly per-ticker configuration selection, classification, and ranking. |
| `report.py` | Weekly Markdown report. |
| `quant_core.py` | `QuantConfig`, daily features, one-position dip-and-ride backtest, state reconstruction, and simplified portfolio simulation. |
| `quant_screener.py` | Daily position-aware classification and error rows. |
| `quant_report.py` | Daily Markdown report, including portfolio coverage warnings. |

`QuantConfig` is immutable and passed explicitly through runner, screener, and core APIs. Its `close_exit_pct` is evaluated against a completed daily close and filled at the next open. It is not a hard stop order; overnight gaps and unmodeled slippage can produce worse exits.

The daily model does not pyramid. A trigger while already holding remains a holding state with an informational note, not a second entry label. A latest-close exit trigger is reported separately as `EXIT PENDING` until a next-open fill is available.

**Research software only; not financial advice or a trading recommendation.**
