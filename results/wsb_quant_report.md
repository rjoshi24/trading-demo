# WSB Snap-Back Swing Screen

_Generated 2026-07-09 15:39 | latest daily bar: **2026-07-09** | universe: top 200 r/wallstreetbets tickers by mention count_

> **Research only, not financial advice.** A mean-reversion swing model: buy stretched / oversold dips confirmed by buying volume, sell when they revert or extend. No 200-SMA, no requirement to be above the band.

## The model in one paragraph

Each ticker gets a **0-100 score** from the signals that actually tested well: **RSI-2 oversold**, **stretch from the 20/21 band in standard deviations** (`z_band` -- because stocks retrace toward the band whether they're above or below it), a **volume surge** (buying-power confirmation), a **reversal up-close**, and a *soft* (non-gating) trend context. A name is **BUY NOW** when a dip trigger fires with a high score. Backtested ~68% win rate over 6y on 45 liquid names.

## How to read this

- **score** 0-100 = how good the dip-buy setup is right now.
- **z_band** = standard deviations from the band. Negative = stretched below (bounce zone); ~ +2 or more = extended above (retrace risk).
- **vol_surge** = today's volume / 20-day average (>= 1.5x = buyers stepping in).
- **bt_*** = the snap-back swing backtest on this ticker (win rate, expectancy per $1,000 trade).

## Summary

| Group | Count |
| --- | --- |
| BUY NOW | 7 |
| CLOSE TO BUY | 5 |
| HOLD | 62 |
| TAKE PROFIT / SELL | 64 |
| WATCH | 55 |
| SKIPPED | 7 |

## BUY NOW  (7)

A **dip buy fired today**: price is oversold (RSI-2) and/or stretched >= 1.5 sigma below the 20/21 band, confirmed by an up-close / volume surge, with a high score. Mean-reversion swing (avg hold ~1 week). Act at next open, size with the stop.

| group_rank | ticker | name | close | score | rsi2 | z_band | dist_band_% | vol_surge | up_close | band_read | bt_trades | bt_winrate_% | bt_expectancy_$ | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | WEN | Wendy’s Company | 7.45 | 48.60 | 8.20 | -0.04 | -0.42 | 0.11 | False | at the band | 64.00 | 70.30 | 11.84 | dip buy (70% hist. win): RSI-2 8 (oversold) (act at next open) |
| 2 | COST | Costco | 910.50 | 47.90 | 9.40 | -2.25 | -4.88 | 0.74 | False | -2.3 sigma below band - stretched, bounce zone | 49.00 | 67.30 | 7.20 | dip buy (67% hist. win): RSI-2 9 (oversold), -2.2 sigma below band (act at next open) |
| 3 | AZZ | AZZ | 138.35 | 53.90 | 4.60 | -1.98 | -8.20 | 0.65 | False | -2.0 sigma below band - stretched, bounce zone | 52.00 | 65.40 | 9.09 | dip buy (65% hist. win): RSI-2 5 (oversold), -2.0 sigma below band (act at next open) |
| 4 | CC | Chemours | 18.17 | 31.70 | 21.00 | -1.61 | -12.09 | 0.13 | False | -1.6 sigma below band - stretched, bounce zone | 69.00 | 63.80 | 10.03 | dip buy (64% hist. win): -1.6 sigma below band (act at next open) |
| 5 | FAST | Fastenal | 46.39 | 43.20 | 8.20 | -0.32 | -0.66 | 0.30 | False | at the band | 56.00 | 62.50 | 4.35 | dip buy (62% hist. win): RSI-2 8 (oversold) (act at next open) |
| 6 | PEP | Pepsico | 137.43 | 42.70 | 11.00 | -1.70 | -3.46 | 0.71 | False | -1.7 sigma below band - stretched, bounce zone | 55.00 | 61.80 | 0.64 | dip buy (62% hist. win): -1.7 sigma below band (act at next open) |
| 7 | ZROZ | Pimco Exchange Traded Fund - PIMCO 25+ Year Zero Coupon U.S. Treasury | 61.08 | 43.70 | 0.60 | -1.42 | -2.68 | 0.15 | False | -1.4 sigma below band - pulling back toward band | 64.00 | 59.40 | 0.49 | dip buy (59% hist. win): RSI-2 1 (oversold) (act at next open) |

## CLOSE TO BUY  (5)

**Getting oversold / stretching toward the band** but no confirmed trigger yet. Watch for the up-close + volume-surge that flips it to BUY NOW.

| group_rank | ticker | name | close | score | rsi2 | z_band | dist_band_% | vol_surge | bt_winrate_% | band_read | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TLT | BlackRock Institutional Trust Company N.A. - BTC iShares 20+ Year Trea | 84.43 | 51.00 | 15.60 | -1.36 | -1.41 | 0.27 | 65.60 | -1.4 sigma below band - pulling back toward band | RSI-2 16 sliding into oversold; -1.4 sigma below band -- watch for the up-close/volume confirm |
| 2 | RXT | Rackspace Technology | 4.84 | 53.50 | 8.60 | -1.92 | -27.81 | 1.40 | 53.50 | -1.9 sigma below band - stretched, bounce zone | dip fired (54% hist. win): RSI-2 9 (oversold), -1.9 sigma below band -- lower-conviction |
| 3 | REAL | The RealReal | 10.54 | 46.20 | 16.50 | -0.78 | -7.30 | 0.09 | 50.70 | -0.8 sigma below band - pulling back toward band | RSI-2 16 sliding into oversold -- watch for the up-close/volume confirm |
| 4 | LUNR | Intuitive Machines | 17.10 | 45.60 | 10.60 | -1.33 | -27.65 | 0.31 | 49.30 | -1.3 sigma below band - pulling back toward band | RSI-2 11 sliding into oversold; -1.3 sigma below band -- watch for the up-close/volume confirm |
| 5 | UP | Wheels Up | 7.97 | 49.10 | 23.40 | -0.08 | -0.68 | 0.13 | 40.70 | at the band | RSI-2 23 sliding into oversold -- watch for the up-close/volume confirm |

## HOLD  (62)

Constructive uptrend, **no fresh dip and not extended**. Hold if long; wait for a pullback to buy.

| group_rank | ticker | name | close | score | rsi2 | z_band | mom_63_% | bt_winrate_% | bt_expectancy_$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DE | Deere & Company | 599.60 | 43.70 | 29.10 | -0.05 | -1.30 | 69.20 | 5.84 |
| 2 | GE | General Electric | 360.45 | 43.50 | 36.70 | 0.20 | 17.20 | 77.50 | 19.48 |
| 3 | NVO | Novo Nordisk | 49.03 | 43.50 | 41.60 | 0.83 | 30.40 | 68.90 | 10.49 |
| 4 | MA | Mastercard | 521.61 | 43.50 | 31.70 | 0.83 | 3.00 | 66.00 | 6.57 |
| 5 | FCEL | FuelCell Energy | 23.91 | 43.50 | 36.40 | -0.01 | 273.00 | 52.50 | 2.96 |
| 6 | HD | Home Depot | 339.61 | 43.50 | 36.50 | 0.10 | 1.00 | 62.70 | 0.68 |
| 7 | LOVE | LoveSac | 17.04 | 43.50 | 37.60 | 0.56 | 9.70 | 60.60 | -5.74 |
| 8 | EW | Edwards Lifesciences | 92.27 | 41.60 | 13.00 | 0.70 | 12.90 | 72.90 | 11.47 |
| 9 | CIA | Citizens Inc | 5.52 | 40.30 | 18.70 | -0.88 | 1.10 | 64.60 | 13.71 |
| 10 | INTC | Intel | 112.55 | 39.80 | 41.10 | -1.02 | 90.90 | 62.50 | 8.08 |
| 11 | PG | Procter & Gamble | 147.14 | 39.50 | 23.30 | -1.06 | 2.30 | 64.20 | 4.66 |
| 12 | SOFI | SoFi | 18.03 | 39.30 | 60.30 | 0.65 | 9.30 | 71.40 | 16.68 |
| 13 | YOU | CLEAR Secure | 55.69 | 39.30 | 52.10 | 0.75 | 10.80 | 62.90 | 14.53 |
| 14 | TSM | TSMC | 443.88 | 39.30 | 64.50 | 0.27 | 21.60 | 71.20 | 14.46 |
| 15 | JPM | JPMorgan Chase | 335.32 | 39.30 | 57.60 | 0.96 | 9.40 | 66.70 | 11.15 |
| 16 | AIR | AAR | 136.15 | 39.30 | 48.10 | 0.29 | 12.70 | 63.80 | 9.51 |
| 17 | EA | Electronic Arts | 205.26 | 39.30 | 60.40 | 0.96 | 0.70 | 74.50 | 8.72 |
| 18 | RIVN | Rivian | 17.83 | 39.30 | 62.90 | 0.91 | 17.80 | 65.70 | 8.40 |
| 19 | IWM | BlackRock Institutional Trust Company N.A. - BTC iShares Russell 2000 | 296.82 | 39.30 | 61.80 | 0.41 | 14.20 | 75.00 | 6.89 |
| 20 | DAL | Delta Air Lines | 88.77 | 39.30 | 48.30 | 0.27 | 30.70 | 69.00 | 4.94 |
| 21 | PYPL | PayPal | 44.87 | 39.30 | 49.10 | 0.87 | -2.10 | 69.20 | 3.16 |
| 22 | CMG | Chipotle Mexican Grill | 34.18 | 39.30 | 59.00 | 0.90 | 1.20 | 63.80 | 1.11 |
| 23 | FOR | Forestar Group | 30.25 | 39.30 | 55.60 | 0.24 | 17.20 | 50.90 | -0.37 |
| 24 | SMA | SmartStop Self Storage REIT | 32.69 | 39.30 | 52.60 | 0.39 | 5.30 | 30.80 | -13.37 |
| 25 | NOW | ServiceNow | 107.79 | 38.10 | 44.40 | 0.90 | 10.60 | 71.40 | 5.03 |
| 26 | GRPN | Groupon | 26.08 | 36.20 | 55.30 | 1.06 | 117.90 | 52.20 | 10.64 |
| 27 | AMP | Ameriprise Financial | 502.99 | 36.20 | 65.10 | 1.55 | 11.40 | 65.50 | 9.32 |
| 28 | BAC | Bank of America | 59.16 | 36.20 | 57.10 | 1.23 | 14.00 | 64.00 | 5.18 |
| 29 | RY | Royal Bank Of Canada | 208.31 | 36.20 | 63.80 | 1.52 | 23.80 | 68.00 | 4.35 |
| 30 | CRWD | CrowdStrike | 195.58 | 36.20 | 64.90 | 1.27 | 83.40 | 65.40 | 4.11 |
| 31 | ES | Eversource Energy | 74.27 | 36.20 | 60.50 | 1.16 | 7.40 | 61.40 | -2.46 |
| 32 | GO | Grocery Outlet | 10.24 | 36.20 | 52.90 | 1.34 | 44.30 | 57.40 | -3.60 |
| 33 | DTE | DTE Energy | 150.39 | 36.00 | 24.30 | 0.20 | 1.90 | 62.50 | 4.24 |
| 34 | CL | Colgate-Palmolive | 92.09 | 36.00 | 21.60 | 0.29 | 8.30 | 64.20 | 4.21 |
| 35 | ABT | Abbott Laboratories | 94.43 | 36.00 | 23.10 | 0.91 | -8.20 | 64.20 | 1.25 |
| 36 | KO | Coca-Cola | 82.47 | 36.00 | 24.50 | 0.55 | 7.40 | 65.30 | 1.00 |
| 37 | GIS | General Mills | 36.03 | 36.00 | 27.60 | 0.52 | 0.10 | 59.00 | 0.92 |
| 38 | SO | Southern Company | 95.68 | 36.00 | 26.20 | 0.31 | -0.70 | 57.40 | 0.43 |
| 39 | EXC | Exelon Corporation | 46.69 | 36.00 | 21.50 | 0.15 | -5.00 | 58.30 | -2.56 |
| 40 | ED | Consolidated Edison | 111.26 | 36.00 | 23.30 | 0.53 | -1.20 | 58.30 | -3.08 |


_...and 22 more._

## TAKE PROFIT / SELL  (64)

**Reverted or extended** -- RSI-2 back above 70, or price is >= +2 sigma above the band. The snap-back is done; trim / take profit if long.

| group_rank | ticker | name | close | score | rsi2 | z_band | dist_band_% | band_read | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ADM | Archer Daniels Midland | 80.61 | 30.80 | 99.50 | 1.47 | 3.39 | +1.5 sigma above band - riding above support | exit signal: RSI-2 100 reverted |
| 2 | BABA | Alibaba | 111.87 | 26.70 | 98.50 | 0.96 | 6.16 | +1.0 sigma above band - riding above support | exit signal: RSI-2 98 reverted |
| 3 | NET | Cloudflare | 274.11 | 35.00 | 97.40 | 1.91 | 11.91 | +1.9 sigma above band - riding above support | exit signal: RSI-2 97 reverted |
| 4 | DFTX | Definium Therapeutics | 47.28 | 39.30 | 95.70 | 0.98 | 20.54 | +1.0 sigma above band - riding above support | exit signal: RSI-2 96 reverted |
| 5 | HPE | Hewlett Packard Enterprise | 47.53 | 33.90 | 94.50 | 0.85 | 4.16 | +0.9 sigma above band - riding above support | exit signal: RSI-2 94 reverted |
| 6 | EBAY | eBay | 117.07 | 35.00 | 94.10 | 1.89 | 5.21 | +1.9 sigma above band - riding above support | exit signal: RSI-2 94 reverted |
| 7 | DELL | Dell | 452.48 | 35.00 | 93.50 | 2.29 | 9.34 | +2.3 sigma above band - extended, may retrace/test the band | exit signal: RSI-2 94 reverted |
| 8 | AVGO | Broadcom | 401.23 | 23.60 | 93.30 | 1.41 | 4.36 | +1.4 sigma above band - riding above support | exit signal: RSI-2 93 reverted |
| 9 | API | Agora.io | 4.28 | 33.90 | 93.10 | 0.67 | 2.36 | +0.7 sigma above band - riding above support | exit signal: RSI-2 93 reverted |
| 10 | CBOE | Cboe | 265.93 | 26.70 | 92.90 | 0.17 | 1.26 | at the band | exit signal: RSI-2 93 reverted |
| 11 | OUT | Outfront Media | 33.81 | 36.20 | 92.50 | 1.55 | 4.61 | +1.5 sigma above band - riding above support | exit signal: RSI-2 92 reverted |
| 12 | SBUX | Starbucks | 106.80 | 35.00 | 92.10 | 2.23 | 3.95 | +2.2 sigma above band - extended, may retrace/test the band | exit signal: RSI-2 92 reverted |
| 13 | JD | Jingdong Mall | 27.86 | 26.70 | 92.00 | 0.63 | 2.75 | +0.6 sigma above band - riding above support | exit signal: RSI-2 92 reverted |
| 14 | PENG | Penguin Solutions | 88.64 | 35.00 | 90.70 | 3.03 | 24.29 | +3.0 sigma above band - extended, may retrace/test the band | exit signal: RSI-2 91 reverted |
| 15 | BULL | Webull | 7.39 | 36.20 | 90.20 | 1.55 | 6.86 | +1.6 sigma above band - riding above support | exit signal: RSI-2 90 reverted |
| 16 | ON | ON Semiconductor | 101.88 | 21.30 | 88.90 | -0.28 | -3.84 | at the band | exit signal: RSI-2 89 reverted |
| 17 | AAPL | Apple | 314.77 | 36.20 | 88.90 | 1.50 | 5.14 | +1.5 sigma above band - riding above support | exit signal: RSI-2 89 reverted |
| 18 | CSCO | Cisco | 118.43 | 33.90 | 87.30 | 0.51 | 1.28 | +0.5 sigma above band - riding above support | exit signal: RSI-2 87 reverted |
| 19 | WB | Weibo | 7.72 | 23.60 | 86.40 | 1.34 | 3.00 | +1.3 sigma above band - riding above support | exit signal: RSI-2 86 reverted |
| 20 | CI | Cigna | 291.31 | 39.30 | 86.10 | 0.89 | 2.05 | +0.9 sigma above band - riding above support | exit signal: RSI-2 86 reverted |
| 21 | GL | Globe Life | 179.66 | 36.20 | 85.60 | 1.15 | 3.54 | +1.1 sigma above band - riding above support | exit signal: RSI-2 86 reverted |
| 22 | ANET | Arista Networks | 185.37 | 35.00 | 85.60 | 2.31 | 9.93 | +2.3 sigma above band - extended, may retrace/test the band | exit signal: RSI-2 86 reverted |
| 23 | LITE | Lumentum | 789.01 | 21.30 | 85.60 | -0.49 | -4.42 | at the band | exit signal: RSI-2 86 reverted |
| 24 | OPEN | Opendoor | 5.22 | 35.00 | 85.60 | 1.96 | 10.65 | +2.0 sigma above band - riding above support | exit signal: RSI-2 86 reverted |
| 25 | TXN | Texas Instruments | 311.56 | 39.30 | 84.00 | 0.82 | 3.23 | +0.8 sigma above band - riding above support | exit signal: RSI-2 84 reverted |
| 26 | IQ | iQIYI | 1.12 | 29.60 | 83.50 | 2.52 | 7.61 | +2.5 sigma above band - extended, may retrace/test the band | exit signal: RSI-2 84 reverted |
| 27 | CRWV | CoreWeave | 93.02 | 21.30 | 82.70 | -0.45 | -5.28 | at the band | exit signal: RSI-2 83 reverted |
| 28 | HR | Healthcare Realty | 20.75 | 36.20 | 82.30 | 1.47 | 1.72 | +1.5 sigma above band - riding above support | exit signal: RSI-2 82 reverted |
| 29 | ARM | Arm Holdings | 333.74 | 28.50 | 82.00 | -0.32 | -4.00 | at the band | exit signal: RSI-2 82 reverted |
| 30 | ORCL | Oracle | 146.36 | 25.40 | 81.60 | -0.78 | -11.07 | -0.8 sigma below band - pulling back toward band | exit signal: RSI-2 82 reverted |
| 31 | SMCI | Supermicro | 28.71 | 25.40 | 81.50 | -0.66 | -5.36 | -0.7 sigma below band - pulling back toward band | exit signal: RSI-2 82 reverted |
| 32 | NOK | Nokia | 12.77 | 25.40 | 79.90 | -0.63 | -4.31 | -0.6 sigma below band - pulling back toward band | exit signal: RSI-2 80 reverted |
| 33 | WULF | TeraWulf | 24.16 | 21.30 | 79.80 | -0.30 | -3.19 | at the band | exit signal: RSI-2 80 reverted |
| 34 | MU | Micron Technology | 1,016.82 | 39.30 | 79.50 | -0.17 | -1.51 | at the band | exit signal: RSI-2 80 reverted |
| 35 | LEVI | Levi Strauss | 24.96 | 41.60 | 79.20 | 1.60 | 3.52 | +1.6 sigma above band - riding above support | exit signal: RSI-2 79 reverted |
| 36 | ATAI | Atai Life Sciences | 5.28 | 36.20 | 78.90 | 1.05 | 12.07 | +1.0 sigma above band - riding above support | exit signal: RSI-2 79 reverted |
| 37 | RMBS | Rambus | 118.07 | 25.40 | 78.80 | -0.67 | -7.06 | -0.7 sigma below band - pulling back toward band | exit signal: RSI-2 79 reverted |
| 38 | PFE | Pfizer | 24.29 | 21.30 | 78.60 | -0.47 | -1.74 | at the band | exit signal: RSI-2 79 reverted |
| 39 | AMD | AMD | 554.16 | 36.20 | 78.40 | 1.10 | 5.41 | +1.1 sigma above band - riding above support | exit signal: RSI-2 78 reverted |
| 40 | HOOD | Robinhood | 116.39 | 36.20 | 78.30 | 1.51 | 11.39 | +1.5 sigma above band - riding above support | exit signal: RSI-2 78 reverted |
| 41 | SNDK | Sandisk | 1,877.02 | 39.30 | 78.10 | -0.22 | -2.40 | at the band | exit signal: RSI-2 78 reverted |
| 42 | GS | Goldman Sachs | 1,059.99 | 33.90 | 77.60 | 0.36 | 1.12 | at the band | exit signal: RSI-2 78 reverted |
| 43 | UNH | UnitedHealth | 430.97 | 36.20 | 77.50 | 1.65 | 3.92 | +1.7 sigma above band - riding above support | exit signal: RSI-2 78 reverted |
| 44 | DJT | Trump Media & Technology Group | 8.70 | 36.20 | 77.10 | 1.28 | 6.64 | +1.3 sigma above band - riding above support | exit signal: RSI-2 77 reverted |
| 45 | AMC | AMC Entertainment | 1.91 | 15.40 | 76.40 | -0.46 | -7.98 | at the band | exit signal: RSI-2 76 reverted |
| 46 | SOXX | BlackRock Institutional Trust Company N.A. - BTC iShares PHLX Semicond | 589.97 | 33.90 | 76.40 | -0.08 | -0.38 | at the band | exit signal: RSI-2 76 reverted |
| 47 | SMH | VanEck Vectors ETF Trust - VanEck Vectors Semiconductor ETF | 613.24 | 33.90 | 76.30 | -0.08 | -0.32 | at the band | exit signal: RSI-2 76 reverted |
| 48 | IBKR | Interactive Brokers | 96.15 | 36.20 | 76.20 | 1.27 | 4.26 | +1.3 sigma above band - riding above support | exit signal: RSI-2 76 reverted |
| 49 | ADBE | Adobe | 220.99 | 26.70 | 76.20 | 0.73 | 3.78 | +0.7 sigma above band - riding above support | exit signal: RSI-2 76 reverted |
| 50 | WDC | Western Digital | 588.17 | 33.90 | 75.60 | -0.22 | -2.79 | at the band | exit signal: RSI-2 76 reverted |
| 51 | BB | BlackBerry | 11.59 | 39.30 | 75.10 | 0.81 | 10.57 | +0.8 sigma above band - riding above support | exit signal: RSI-2 75 reverted |
| 52 | ASML | ASML | 1,834.62 | 39.30 | 74.90 | 0.23 | 0.89 | at the band | exit signal: RSI-2 75 reverted |
| 53 | AMAT | Applied Materials | 608.91 | 39.30 | 74.50 | 0.25 | 2.14 | at the band | exit signal: RSI-2 74 reverted |
| 54 | SOXL | Direxion Shares ETF Trust - Direxion Daily Semiconductor Bull 3X Share | 199.85 | 25.40 | 74.00 | -0.54 | -9.91 | -0.5 sigma below band - pulling back toward band | exit signal: RSI-2 74 reverted |
| 55 | QQQ | Invesco QQQ ETF | 721.25 | 33.90 | 73.30 | 0.12 | 0.21 | at the band | exit signal: RSI-2 73 reverted |
| 56 | DC | Dakota Gold | 4.43 | 21.30 | 73.20 | -0.39 | -3.04 | at the band | exit signal: RSI-2 73 reverted |
| 57 | KEEL | Keel Infrastructure | 4.91 | 25.40 | 72.90 | -0.83 | -10.99 | -0.8 sigma below band - pulling back toward band | exit signal: RSI-2 73 reverted |
| 58 | TQQQ | ProShares Trust - ProShares UltraPro QQQ | 75.78 | 21.30 | 72.60 | -0.12 | -0.63 | at the band | exit signal: RSI-2 73 reverted |
| 59 | VOO | Vanguard S&P 500 ETF | 689.20 | 39.30 | 71.80 | 0.95 | 1.00 | +0.9 sigma above band - riding above support | exit signal: RSI-2 72 reverted |
| 60 | SPY | SPDR S&P 500 ETF Trust | 749.84 | 39.30 | 71.50 | 0.95 | 1.00 | +0.9 sigma above band - riding above support | exit signal: RSI-2 72 reverted |
| 61 | AG | First Majestic Silver | 17.22 | 26.70 | 70.80 | -0.10 | -0.60 | at the band | exit signal: RSI-2 71 reverted |
| 62 | ONDS | Ondas Holdings | 7.76 | 25.40 | 70.50 | -0.84 | -8.75 | -0.8 sigma below band - pulling back toward band | exit signal: RSI-2 70 reverted |
| 63 | AAOI | Applied Optoelectronics | 122.89 | 30.20 | 70.50 | -1.05 | -19.36 | -1.0 sigma below band - pulling back toward band | exit signal: RSI-2 70 reverted |
| 64 | VTI | Vanguard Total Stock Market ETF | 370.81 | 39.30 | 70.50 | 0.99 | 1.04 | +1.0 sigma above band - riding above support | exit signal: RSI-2 70 reverted |

## WATCH  (55)

Neutral -- no dip and no trend edge. Nothing to do.

| group_rank | ticker | name | close | score | rsi2 | z_band | above_50 | mom_63_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RKLB | Rocket Lab USA | 84.76 | 34.40 | 31.90 | -1.21 | False | 22.70 |
| 2 | UAMY | United States Antimony Corporation | 6.78 | 34.40 | 34.90 | -1.29 | False | -23.40 |
| 3 | RUN | Sunrun | 12.16 | 34.40 | 35.80 | -1.27 | False | -12.30 |
| 4 | DIS | Walt Disney | 95.94 | 32.50 | 15.00 | -1.28 | False | -2.50 |
| 5 | HBM | Hudbay Minerals | 21.42 | 30.20 | 49.00 | -1.11 | False | -9.90 |
| 6 | KORU | Direxion Shares ETF Trust - Direxion Daily South Korea Bull 3X Shares | 563.75 | 30.20 | 46.50 | -1.03 | False | 39.20 |
| 7 | OKLO | Oklo | 48.90 | 30.20 | 54.30 | -1.26 | False | -2.60 |
| 8 | APLD | Applied Blockchain | 32.79 | 30.20 | 65.40 | -1.11 | False | 18.00 |
| 9 | RDW | Redwire | 10.69 | 30.20 | 47.80 | -1.03 | False | 11.20 |
| 10 | OR | Osisko Gold Royalties | 30.08 | 30.20 | 54.80 | -1.08 | False | -25.10 |
| 11 | UUUU | Energy Fuels | 13.56 | 30.20 | 67.50 | -1.18 | False | -26.20 |
| 12 | AGI | Alamos Gold | 29.84 | 29.60 | 43.00 | -0.96 | False | -37.30 |
| 13 | PLTR | Palantir | 127.41 | 29.00 | 19.50 | 0.13 | False | -9.50 |
| 14 | GOOG | Alphabet (Google) | 350.82 | 27.70 | 11.40 | -0.61 | False | 11.50 |
| 15 | AVAV | AeroVironment | 150.93 | 27.70 | 11.00 | -0.79 | False | -19.30 |
| 16 | NFLX | Netflix | 74.64 | 27.70 | 19.30 | -0.51 | False | -24.90 |
| 17 | ASTS | AST SpaceMobile | 74.32 | 27.70 | 15.50 | -0.83 | False | -23.00 |
| 18 | GOOGL | Alphabet (Google) | 353.42 | 27.70 | 10.20 | -0.57 | False | 11.40 |
| 19 | FISV | Fiserv | 51.30 | 26.70 | 49.30 | 0.32 | False | -9.40 |
| 20 | TSLA | Tesla | 396.89 | 25.50 | 38.60 | -0.26 | False | 15.60 |
| 21 | EL | Estee Lauder | 82.29 | 25.50 | 36.30 | -0.43 | False | 15.60 |
| 22 | EU | enCore Energy | 1.32 | 25.40 | 64.80 | -0.64 | False | -27.70 |
| 23 | NBIS | Nebius Group | 217.02 | 25.40 | 61.70 | -0.79 | False | 73.60 |
| 24 | MSTR | MicroStrategy | 95.84 | 25.40 | 49.90 | -0.66 | False | -25.30 |
| 25 | EWY | BlackRock Institutional Trust Company N.A. - iShares MSCI South Korea | 183.89 | 25.40 | 51.30 | -0.85 | False | 31.30 |
| 26 | BE | Bloom Energy | 263.64 | 25.40 | 45.00 | -0.64 | False | 79.60 |
| 27 | LINK | Interlink Electronics | 4.16 | 25.40 | 60.40 | -0.53 | False | 33.80 |
| 28 | MSFT | Microsoft | 380.32 | 23.60 | 18.30 | -0.28 | False | 1.80 |
| 29 | LOT | Lotus Technology | 1.17 | 23.60 | 15.70 | -0.21 | False | -7.10 |
| 30 | CRM | Salesforce | 163.38 | 23.40 | 22.60 | 0.12 | False | -6.90 |
| 31 | AMZN | Amazon | 241.39 | 23.40 | 20.50 | 0.04 | False | 9.10 |
| 32 | TM | Toyota | 174.99 | 23.40 | 22.80 | 0.15 | False | -18.60 |
| 33 | SOXS | Direxion Shares ETF Trust - Direxion Daily Semiconductor Bear 3X Share | 3.86 | 22.10 | 20.70 | -0.83 | False | -85.50 |
| 34 | SNAP | Snap | 4.62 | 22.10 | 22.20 | -0.51 | False | -2.30 |
| 35 | XOM | Exxon Mobil | 138.17 | 22.10 | 29.10 | -0.53 | False | -11.00 |
| 36 | IT | Gartner | 132.21 | 22.10 | 23.30 | -0.63 | False | -11.50 |
| 37 | GLD | SSgA SPDR Gold Shares | 378.77 | 21.30 | 66.30 | -0.23 | False | -12.80 |
| 38 | VC | Visteon | 106.42 | 21.30 | 69.20 | -0.36 | False | 9.70 |
| 39 | BSX | Boston Scientific | 45.03 | 21.30 | 62.00 | -0.32 | False | -28.00 |
| 40 | SQQQ | ProShares Trust - ProShares UltraPro Short QQQ | 38.43 | 18.00 | 25.70 | -0.36 | False | -43.60 |


_...and 15 more._

## SKIPPED  (7)

Not enough clean daily history.

SPCX, PS, DAY, RE, OS, OG, GPS
