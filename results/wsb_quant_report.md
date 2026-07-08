# WSB Composite Swing-Model Screen

_Generated 2026-07-08 18:28 | latest daily bar: **2026-07-08** | universe: top 200 r/wallstreetbets tickers by mention count_

> **Research only, not financial advice.** A single fixed, research-grounded parameter set is applied to every ticker (no per-ticker curve-fitting). Signals are tuned for a swing horizon of **>= 10 trading days**.

## The model in one paragraph

Each ticker gets a transparent **0-100 composite score** blending: the **golden-cross regime** (50/200 SMA) + long-trend filter, the **Bull Market Support Band** (20 SMA / 21 EMA), **12-1 time-series momentum**, **MACD** and **RSI**, a **volatility squeeze** (Bollinger inside Keltner -- fires *before* big moves), and a **20-day breakout + volume** check. A ticker becomes **BUY NOW** only when the regime is bullish, the score is high, and a fresh entry trigger fires on the latest bar.

## How to read this

- **score** 0-100 = overall attractiveness (regime + momentum + setup).
- **need_move_%** / **prox_high_%** = % move to the nearest trigger (the 20-day high or a band reclaim).
- **squeeze_on** = volatility is coiled (a big move tends to follow).
- **bt_*** = a >=10-day-hold swing backtest on this ticker (win rate, expectancy per $1,000 trade) so you can gauge each name's historical quality.

## Summary

| Group | Count |
| --- | --- |
| BUY NOW | 12 |
| CLOSE TO BUY | 50 |
| HOLD (UPTREND) | 14 |
| SELL / EXIT | 54 |
| WATCH | 65 |
| SKIPPED | 5 |

## BUY NOW  (12)

Regime is bullish, a **fresh entry trigger fired on the latest daily bar** (20-day breakout, band reclaim, or a squeeze firing up) and the composite score clears the buy threshold. Act at next open, size with the ATR stop.

| group_rank | ticker | name | close | score | rsi | mom_12_1_% | squeeze_on | vol_ratio | band_bot | band_top | need_move_% | bt_trades | bt_winrate_% | bt_expectancy_$ | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ANET | Arista Networks | 178.32 | 93.10 | 55.60 | 52.00 | True | 0.91 | 164.77 | 165.29 | -2.11 | 28.00 | 50.00 | 17.83 | entry trigger: 20-day breakout, squeeze fired up (act at next open) |
| 2 | PENG | Penguin Solutions | 77.78 | 91.80 | 61.90 | 185.90 | True | 2.86 | 65.10 | 65.54 | -2.28 | 15.00 | 46.70 | 135.25 | entry trigger: 20-day breakout, reclaimed the band, squeeze fired up (act at next open) |
| 3 | DELL | Dell | 428.86 | 87.70 | 56.60 | 220.90 | True | 0.95 | 402.27 | 409.68 | 1.21 | 19.00 | 57.90 | 96.13 | entry trigger: squeeze fired up (act at next open) |
| 4 | AAPL | Apple | 314.24 | 84.30 | 60.00 | 47.00 | False | 0.37 | 295.68 | 298.96 | -0.50 | 19.00 | 57.90 | 19.91 | entry trigger: 20-day breakout (act at next open) |
| 5 | AVGO | Broadcom | 389.65 | 79.80 | 54.50 | 41.50 | True | 0.67 | 380.72 | 384.91 | 5.40 | 27.00 | 48.10 | 45.87 | entry trigger: reclaimed the band (act at next open) |
| 6 | WTI | W&T Offshore | 3.65 | 76.70 | 65.30 | 118.70 | False | 1.38 | 3.41 | 3.42 | 17.26 | 15.00 | 33.30 | 6.97 | entry trigger: reclaimed the band (act at next open) |
| 7 | XLE | SSgA Active Trust - SSgA Energy Select Sector SPDR | 55.38 | 75.90 | 52.60 | 37.00 | False | 0.85 | 54.62 | 54.72 | 4.57 | 23.00 | 21.70 | 5.52 | entry trigger: reclaimed the band (act at next open) |
| 8 | TXN | Texas Instruments | 305.58 | 72.70 | 50.00 | 37.30 | False | 0.38 | 300.02 | 301.35 | 8.74 | 21.00 | 52.40 | 29.32 | entry trigger: reclaimed the band (act at next open) |
| 9 | ET | Energy Transfer Partners | 19.90 | 72.10 | 70.50 | 17.70 | False | 0.79 | 19.11 | 19.28 | -0.43 | 26.00 | 50.00 | 10.81 | entry trigger: 20-day breakout (act at next open) |
| 10 | NVDA | NVIDIA | 202.66 | 71.70 | 45.00 | 29.60 | False | 0.62 | 201.62 | 201.92 | 4.83 | 27.00 | 40.70 | 27.70 | entry trigger: reclaimed the band (act at next open) |
| 11 | COP | ConocoPhillips | 109.84 | 62.80 | 46.50 | 30.80 | False | 0.60 | 109.30 | 109.43 | 9.18 | 18.00 | 22.20 | -13.85 | entry trigger: reclaimed the band (act at next open) |
| 12 | CVX | Chevron | 175.89 | 61.20 | 43.60 | 32.40 | False | 0.58 | 175.23 | 175.71 | 7.91 | 26.00 | 23.10 | -9.67 | entry trigger: reclaimed the band (act at next open) |

## CLOSE TO BUY  (50)

Bullish regime and a **high score, but no trigger yet** -- the setup is building: a volatility squeeze is coiled, price is a few percent under the 20-day high, or it's hugging the support band. These are the watch-closely names.

| group_rank | ticker | name | close | score | pos_vs_band | prox_high_% | squeeze_on | rsi | mom_12_1_% | band_bot | band_top | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ADM | Archer Daniels Midland | 80.39 | 89.70 | above | 1.11 | False | 60.20 | 53.10 | 77.66 | 77.84 | 1.1% under the 20-day high -- watch for the trigger |
| 2 | ZETA | Zeta Global | 21.47 | 89.70 | above | 1.86 | False | 59.20 | 48.10 | 19.90 | 20.27 | 1.9% under the 20-day high -- watch for the trigger |
| 3 | YOU | CLEAR Secure | 55.44 | 86.20 | above | 2.35 | False | 59.70 | 92.80 | 53.41 | 54.61 | 2.4% under the 20-day high -- watch for the trigger |
| 4 | OUT | Outfront Media | 33.08 | 82.30 | above | 0.48 | False | 68.50 | 93.70 | 31.93 | 32.27 | 0.5% under the 20-day high -- watch for the trigger |
| 5 | CVS | CVS Health | 104.54 | 81.20 | above | 0.26 | False | 61.60 | 49.10 | 101.19 | 101.88 | 0.3% under the 20-day high -- watch for the trigger |
| 6 | MO | Altria Group | 73.10 | 80.10 | above | 1.30 | False | 62.10 | 26.10 | 71.50 | 71.69 | 1.3% under the 20-day high -- watch for the trigger |
| 7 | HUM | Humana | 397.00 | 79.00 | above | 3.13 | False | 67.20 | 49.40 | 373.07 | 377.78 | 3.1% under the 20-day high -- watch for the trigger |
| 8 | MS | Morgan Stanley | 218.54 | 78.80 | above | 3.91 | False | 47.60 | 51.00 | 215.43 | 217.29 | 3.9% under the 20-day high -- watch for the trigger |
| 9 | LLY | Eli Lilly | 1,226.50 | 78.30 | above | 0.74 | False | 69.00 | 47.40 | 1,159.84 | 1,161.65 | 0.7% under the 20-day high -- watch for the trigger |
| 10 | RY | Royal Bank Of Canada | 206.35 | 78.20 | above | 1.32 | False | 61.90 | 49.50 | 202.17 | 202.98 | 1.3% under the 20-day high -- watch for the trigger |
| 11 | UNH | UnitedHealth | 424.60 | 77.60 | above | 0.85 | False | 59.50 | 34.30 | 411.91 | 413.39 | 0.8% under the 20-day high -- watch for the trigger |
| 12 | KO | Coca-Cola | 84.01 | 77.40 | above | 0.15 | False | 66.90 | 14.40 | 81.62 | 81.62 | 0.1% under the 20-day high -- watch for the trigger |
| 13 | IBKR | Interactive Brokers | 93.62 | 76.60 | above | 3.42 | False | 50.90 | 46.60 | 91.28 | 91.93 | 3.4% under the 20-day high -- watch for the trigger |
| 14 | NET | Cloudflare | 268.60 | 75.50 | above | 0.09 | False | 75.40 | 29.70 | 236.14 | 241.26 | 0.1% under the 20-day high -- watch for the trigger |
| 15 | JUST | Goldman Sachs ETF Trust - Goldman Sachs Just Us Large Cap Equity ETF | 106.63 | 74.90 | above | 0.68 | False | 48.30 | 20.40 | 105.93 | 106.11 | 0.7% under the 20-day high -- watch for the trigger |
| 16 | GOOGL | Alphabet (Google) | 358.73 | 74.10 | inside | 4.05 | False | 41.40 | 108.90 | 357.95 | 360.45 | hugging the support band -- watch for the trigger |
| 17 | AM | Antero Midstream | 22.70 | 73.90 | above | 2.16 | False | 66.50 | 25.90 | 22.08 | 22.20 | 2.2% under the 20-day high -- watch for the trigger |
| 18 | VOO | Vanguard S&P 500 ETF | 684.94 | 73.80 | above | 1.00 | False | 47.70 | 19.90 | 680.96 | 682.24 | 1.0% under the 20-day high -- watch for the trigger |
| 19 | SPY | SPDR S&P 500 ETF Trust | 745.18 | 73.70 | above | 1.04 | False | 47.70 | 19.80 | 740.92 | 742.30 | 1.0% under the 20-day high -- watch for the trigger |
| 20 | RXT | Rackspace Technology | 6.26 | 72.00 | inside | 20.37 | False | 50.30 | 251.10 | 6.13 | 6.29 | hugging the support band -- watch for the trigger |
| 21 | LEVI | Levi Strauss | 24.24 | 70.10 | above | 2.46 | True | 55.60 | 18.30 | 23.95 | 24.03 | volatility squeeze (coiled); 2.5% under the 20-day high -- watch for the trigger |
| 22 | EA | Electronic Arts | 205.36 | 69.50 | above | 0.04 | False | 72.80 | 32.70 | 204.05 | 204.18 | 0.0% under the 20-day high -- watch for the trigger |
| 23 | CSCO | Cisco | 113.56 | 68.50 | below | 8.92 | False | 40.30 | 79.50 | 116.12 | 117.53 | hugging the support band -- watch for the trigger |
| 24 | USO | United States Commodity Funds LLC - United States Oil Fund | 111.34 | 68.30 | below | 21.38 | False | 43.30 | 73.90 | 113.80 | 114.20 | hugging the support band -- watch for the trigger |
| 25 | BAC | Bank of America | 58.47 | 68.00 | above | 2.44 | False | 59.60 | 12.50 | 57.08 | 57.24 | 2.4% under the 20-day high -- watch for the trigger |
| 26 | AIR | AAR | 133.67 | 67.70 | inside | 7.44 | False | 55.00 | 65.20 | 133.17 | 134.23 | hugging the support band -- watch for the trigger |
| 27 | JNJ | Johnson & Johnson | 266.16 | 67.30 | above | 0.41 | False | 74.50 | 53.70 | 246.06 | 248.33 | 0.4% under the 20-day high -- watch for the trigger |
| 28 | XOM | Exxon Mobil | 140.93 | 67.00 | inside | 7.67 | False | 47.60 | 39.20 | 140.44 | 140.96 | hugging the support band -- watch for the trigger |
| 29 | SO | Southern Company | 96.54 | 66.90 | above | 1.49 | False | 57.30 | 4.30 | 95.03 | 95.21 | 1.5% under the 20-day high -- watch for the trigger |
| 30 | DFTX | Definium Therapeutics | 45.93 | 66.70 | above | 2.42 | False | 86.20 | 227.10 | 35.63 | 37.48 | 2.4% under the 20-day high -- watch for the trigger |
| 31 | DTE | DTE Energy | 151.92 | 66.60 | above | 1.65 | False | 58.70 | 14.00 | 149.50 | 149.68 | 1.6% under the 20-day high -- watch for the trigger |
| 32 | ES | Eversource Energy | 74.07 | 66.20 | above | 0.92 | False | 66.90 | 14.70 | 71.33 | 71.78 | 0.9% under the 20-day high -- watch for the trigger |
| 33 | CL | Colgate-Palmolive | 93.41 | 66.00 | above | 1.84 | False | 58.30 | -2.70 | 91.34 | 91.61 | 1.8% under the 20-day high -- watch for the trigger |
| 34 | GD | General Dynamics | 372.64 | 65.90 | above | 1.14 | False | 57.00 | 19.10 | 355.50 | 356.59 | 1.1% under the 20-day high -- watch for the trigger |
| 35 | CI | Cigna | 291.01 | 65.00 | above | 2.40 | False | 49.20 | -6.20 | 284.31 | 286.09 | 2.4% under the 20-day high -- watch for the trigger |
| 36 | JPM | JPMorgan Chase | 332.60 | 64.90 | above | 1.99 | False | 52.90 | 8.50 | 326.21 | 326.92 | 2.0% under the 20-day high -- watch for the trigger |
| 37 | RTX | Raytheon Technologies | 195.85 | 64.60 | above | 2.82 | False | 60.00 | 26.00 | 188.47 | 189.36 | 2.8% under the 20-day high -- watch for the trigger |
| 38 | ED | Consolidated Edison | 112.64 | 63.40 | above | 1.20 | False | 63.00 | 10.10 | 109.64 | 110.07 | 1.2% under the 20-day high -- watch for the trigger |
| 39 | EW | Edwards Lifesciences | 93.81 | 62.70 | above | 1.46 | False | 66.20 | 12.10 | 89.40 | 90.11 | 1.5% under the 20-day high -- watch for the trigger |
| 40 | IBM | IBM | 302.08 | 62.40 | above | 1.34 | False | 66.30 | -0.10 | 275.03 | 279.31 | 1.3% under the 20-day high -- watch for the trigger |
| 41 | AMZN | Amazon | 241.95 | 61.80 | inside | 1.68 | False | 46.70 | 10.10 | 239.60 | 242.84 | 1.7% under the 20-day high; hugging the support band -- watch for the trigger |
| 42 | BP | BP | 39.24 | 61.10 | below | 11.43 | False | 40.30 | 49.70 | 39.33 | 39.40 | hugging the support band -- watch for the trigger |
| 43 | GO | Grocery Outlet | 10.23 | 61.10 | above | 1.61 | False | 56.00 | -35.40 | 9.65 | 9.72 | 1.6% under the 20-day high -- watch for the trigger |
| 44 | GL | Globe Life | 176.33 | 60.30 | above | 2.17 | False | 71.50 | 32.10 | 172.08 | 172.72 | 2.2% under the 20-day high -- watch for the trigger |
| 45 | EXC | Exelon Corporation | 47.36 | 58.60 | above | 1.10 | False | 55.10 | 8.80 | 46.52 | 46.60 | 1.1% under the 20-day high -- watch for the trigger |
| 46 | GE | General Electric | 355.63 | 57.70 | inside | 6.48 | False | 53.60 | 32.40 | 355.63 | 356.87 | hugging the support band -- watch for the trigger |
| 47 | ALL | Allstate | 250.93 | 55.00 | above | 0.21 | False | 79.40 | 15.30 | 232.59 | 234.85 | 0.2% under the 20-day high -- watch for the trigger |
| 48 | GM | General Motors | 75.68 | 54.30 | below | 11.09 | False | 25.20 | 59.60 | 78.31 | 79.07 | hugging the support band -- watch for the trigger |
| 49 | AMP | Ameriprise Financial | 492.88 | 52.90 | above | 3.04 | False | 59.80 | -14.10 | 468.36 | 472.35 | 3.0% under the 20-day high -- watch for the trigger |
| 50 | PEG | PSEG | 81.18 | 52.00 | above | 2.96 | False | 51.20 | -1.10 | 80.67 | 80.77 | 3.0% under the 20-day high -- watch for the trigger |

## HOLD (UPTREND)  (14)

Already **above the band and trending**. Hold if you are long; a new buyer here is chasing an extended move (wait for a pullback to the band).

| group_rank | ticker | name | close | score | rsi | mom_12_1_% | band_bot | band_top | bt_winrate_% | bt_expectancy_$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | GEV | GE Vernova | 1,090.15 | 70.40 | 58.30 | 76.40 | 1,047.36 | 1,067.28 | 47.60 | 82.09 |
| 2 | SLS | Sellas Life Sciences | 12.47 | 69.20 | 67.20 | 279.30 | 10.48 | 11.19 | 31.20 | 34.59 |
| 3 | FOR | Forestar Group | 30.09 | 67.10 | 58.10 | 35.00 | 29.90 | 29.97 | 33.30 | -4.38 |
| 4 | BB | BlackBerry | 10.95 | 67.00 | 61.90 | 118.30 | 10.13 | 10.33 | 50.00 | 109.76 |
| 5 | RIVN | Rivian | 16.58 | 62.70 | 52.70 | 28.20 | 16.32 | 16.58 | 33.30 | -39.07 |
| 6 | RDDT | Reddit | 192.77 | 60.70 | 59.20 | 13.10 | 176.95 | 179.13 | 50.00 | 152.79 |
| 7 | BY | Byline Bancorp | 36.78 | 59.50 | 65.70 | 22.00 | 36.19 | 36.23 | 52.40 | 17.92 |
| 8 | LOVE | LoveSac | 16.56 | 57.60 | 64.10 | -15.30 | 16.12 | 16.40 | 25.00 | -8.48 |
| 9 | BA | Boeing | 224.21 | 57.30 | 46.70 | -1.50 | 221.44 | 222.61 | 56.20 | 7.78 |
| 10 | SGOV | iShares Trust - iShares 0-3 Month Treasury Bond ETF | 100.47 | 53.60 | nan | 3.30 | 100.32 | 100.34 | 100.00 | 2.45 |
| 11 | HOOD | Robinhood | 111.84 | 50.00 | 62.80 | -11.80 | 101.39 | 101.68 | 50.00 | 118.85 |
| 12 | NVO | Novo Nordisk | 49.31 | 49.60 | 77.90 | -35.00 | 46.36 | 47.02 | 50.00 | 1.13 |
| 13 | GRPN | Groupon | 25.63 | 44.60 | 79.90 | -55.20 | 20.47 | 21.80 | 29.40 | 46.51 |
| 14 | EVER | EverQuote | 24.51 | 43.30 | 72.70 | -21.80 | 22.01 | 22.46 | 50.00 | 44.08 |

## SELL / EXIT  (54)

An **exit condition is present** -- price lost the 20/21 support band, or a death cross with price below the 200-SMA. If you hold it, the model says exit.

| group_rank | ticker | name | close | score | pos_vs_band | band_bot | band_top | rsi | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CAVA | CAVA Group | 67.82 | 17.40 | below | 78.40 | 81.25 | 24.00 | exit signal: lost the support band |
| 2 | AGI | Alamos Gold | 29.06 | 19.20 | below | 32.84 | 32.93 | 17.40 | exit signal: lost the support band |
| 3 | LINK | Interlink Electronics | 4.05 | 24.70 | below | 4.29 | 4.31 | 46.10 | exit signal: lost the support band |
| 4 | EL | Estee Lauder | 81.46 | 25.20 | below | 83.30 | 84.17 | 36.50 | exit signal: lost the support band |
| 5 | SAP | SAP | 157.91 | 25.30 | below | 159.57 | 161.53 | 42.60 | exit signal: lost the support band |
| 6 | AVAV | AeroVironment | 159.29 | 26.90 | below | 163.12 | 166.10 | 47.00 | exit signal: lost the support band |
| 7 | CME | CME Group | 245.07 | 27.30 | above | 243.50 | 243.54 | 38.70 | exit signal: death cross / below 200-SMA |
| 8 | AVY | Avery Dennison | 157.11 | 27.40 | below | 161.28 | 161.58 | 42.10 | exit signal: lost the support band |
| 9 | DIS | Walt Disney | 97.43 | 27.60 | below | 98.93 | 99.08 | 42.50 | exit signal: lost the support band |
| 10 | AEM | Agnico Eagle Mines | 144.54 | 27.70 | below | 159.07 | 159.60 | 14.50 | exit signal: lost the support band |
| 11 | LOW | Lowe's Companies | 214.43 | 28.80 | below | 219.83 | 220.08 | 41.00 | exit signal: lost the support band |
| 12 | HD | Home Depot | 336.85 | 30.70 | below | 337.80 | 338.07 | 49.90 | exit signal: lost the support band |
| 13 | DC | Dakota Gold | 4.22 | 31.50 | below | 4.55 | 4.60 | 23.60 | exit signal: lost the support band |
| 14 | VZ | Verizon | 42.83 | 32.00 | below | 44.61 | 45.08 | 32.30 | exit signal: lost the support band |
| 15 | IT | Gartner | 135.52 | 32.50 | below | 137.31 | 139.11 | 44.20 | exit signal: lost the support band |
| 16 | NFLX | Netflix | 76.19 | 33.10 | below | 76.37 | 77.10 | 44.30 | exit signal: lost the support band |
| 17 | FOX | Fox Corporation | 48.51 | 33.50 | below | 49.90 | 50.12 | 51.90 | exit signal: lost the support band |
| 18 | RC | Ready Capital | 1.67 | 34.60 | below | 1.70 | 1.71 | 51.10 | exit signal: lost the support band |
| 19 | JD | Jingdong Mall | 27.68 | 35.30 | above | 27.01 | 27.17 | 44.70 | exit signal: death cross / below 200-SMA |
| 20 | GLD | SSgA SPDR Gold Shares | 373.63 | 36.80 | below | 379.90 | 382.73 | 32.10 | exit signal: lost the support band |
| 21 | ASTS | AST SpaceMobile | 74.71 | 42.50 | below | 80.97 | 82.59 | 43.90 | exit signal: lost the support band |
| 22 | TSLA | Tesla | 391.80 | 42.90 | below | 398.96 | 402.90 | 46.50 | exit signal: lost the support band |
| 23 | APLD | Applied Blockchain | 30.74 | 43.40 | below | 38.48 | 40.05 | 8.30 | exit signal: lost the support band |
| 24 | LMT | Lockheed Martin | 529.46 | 44.30 | above | 521.86 | 522.78 | 47.80 | exit signal: death cross / below 200-SMA |
| 25 | WDC | Western Digital | 535.92 | 45.80 | below | 590.16 | 613.77 | 36.90 | exit signal: lost the support band |
| 26 | GLW | Corning | 185.62 | 50.80 | below | 199.33 | 201.24 | 52.10 | exit signal: lost the support band |
| 27 | PEP | Pepsico | 144.17 | 51.60 | above | 142.45 | 142.90 | 46.80 | exit signal: death cross / below 200-SMA |
| 28 | EWY | BlackRock Institutional Trust Company N.A. - iShares MSCI South Korea | 180.90 | 52.30 | below | 192.93 | 196.42 | 38.40 | exit signal: lost the support band |
| 29 | MRVL | Marvell Technology Group | 233.21 | 54.10 | below | 260.46 | 274.27 | 38.30 | exit signal: lost the support band |
| 30 | SOXL | Direxion Shares ETF Trust - Direxion Daily Semiconductor Bull 3X Share | 175.01 | 54.90 | below | 214.79 | 226.00 | 43.50 | exit signal: lost the support band |
| 31 | WULF | TeraWulf | 22.16 | 55.10 | below | 24.43 | 25.43 | 30.40 | exit signal: lost the support band |
| 32 | DE | Deere & Company | 598.27 | 55.30 | below | 599.14 | 601.47 | 54.50 | exit signal: lost the support band |
| 33 | RTH | VanEck Vectors ETF Trust - VanEck Vectors Retail ETF | 257.06 | 55.80 | below | 257.41 | 257.52 | 42.30 | exit signal: lost the support band |
| 34 | BE | Bloom Energy | 244.33 | 55.90 | below | 282.22 | 283.72 | 44.40 | exit signal: lost the support band |
| 35 | SNDK | Sandisk | 1,671.19 | 56.00 | below | 1,868.96 | 1,955.32 | 43.20 | exit signal: lost the support band |
| 36 | INTC | Intel | 107.89 | 56.60 | below | 121.51 | 124.09 | 44.70 | exit signal: lost the support band |
| 37 | NBIS | Nebius Group | 210.50 | 57.10 | below | 235.41 | 244.77 | 36.40 | exit signal: lost the support band |
| 38 | QQQ | Invesco QQQ ETF | 709.77 | 57.50 | below | 718.54 | 719.80 | 43.50 | exit signal: lost the support band |
| 39 | TQQQ | ProShares Trust - ProShares UltraPro QQQ | 72.27 | 57.90 | below | 76.04 | 76.33 | 41.90 | exit signal: lost the support band |
| 40 | MU | Micron Technology | 940.98 | 58.00 | below | 1,013.11 | 1,045.87 | 45.40 | exit signal: lost the support band |
| 41 | SOXX | BlackRock Institutional Trust Company N.A. - BTC iShares PHLX Semicond | 562.30 | 59.80 | below | 585.90 | 596.81 | 45.90 | exit signal: lost the support band |
| 42 | AMAT | Applied Materials | 575.03 | 60.30 | below | 585.57 | 599.20 | 50.60 | exit signal: lost the support band |
| 43 | DAL | Delta Air Lines | 86.93 | 60.70 | below | 87.18 | 87.20 | 60.00 | exit signal: lost the support band |
| 44 | CAT | Caterpillar | 948.49 | 61.20 | below | 965.03 | 968.36 | 50.30 | exit signal: lost the support band |
| 45 | SMH | VanEck Vectors ETF Trust - VanEck Vectors Semiconductor ETF | 592.53 | 61.60 | below | 610.21 | 618.78 | 46.10 | exit signal: lost the support band |
| 46 | VT | Vanguard Group, Inc. - Vanguard Total World Stock ETF | 155.68 | 61.70 | below | 155.74 | 155.80 | 44.50 | exit signal: lost the support band |
| 47 | GS | Goldman Sachs | 1,027.27 | 62.50 | below | 1,040.06 | 1,052.72 | 33.20 | exit signal: lost the support band |
| 48 | FAST | Fastenal | 46.69 | 63.00 | below | 46.72 | 46.74 | 53.80 | exit signal: lost the support band |
| 49 | ASML | ASML | 1,777.94 | 65.90 | below | 1,796.09 | 1,835.53 | 48.70 | exit signal: lost the support band |
| 50 | TSM | TSMC | 437.41 | 66.00 | below | 438.21 | 439.31 | 52.70 | exit signal: lost the support band |
| 51 | IWM | BlackRock Institutional Trust Company N.A. - BTC iShares Russell 2000 | 293.54 | 66.50 | below | 294.40 | 294.69 | 52.50 | exit signal: lost the support band |
| 52 | HPE | Hewlett Packard Enterprise | 44.53 | 68.30 | below | 44.70 | 46.17 | 38.20 | exit signal: lost the support band |
| 53 | AMD | AMD | 513.28 | 68.50 | below | 518.78 | 521.91 | 51.00 | exit signal: lost the support band |
| 54 | GOOG | Alphabet (Google) | 355.35 | 72.40 | below | 355.87 | 357.93 | 41.30 | exit signal: lost the support band |

## WATCH  (65)

No setup: regime and/or composite score too weak. Nothing to do yet.

| group_rank | ticker | name | close | score | regime_ok | pos_vs_band | rsi | mom_12_1_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | GOAT | VanEck Vectors ETF Trust - VanEck Vectors Morningstar Global Wide Moat | 38.58 | 57.10 | False | above | 52.70 | 8.00 |
| 2 | KORU | Direxion Shares ETF Trust - Direxion Daily South Korea Bull 3X Shares | 535.80 | 56.60 | True | below | 34.60 | 721.90 |
| 3 | NOK | Nokia | 11.81 | 56.60 | True | below | 32.00 | 183.40 |
| 4 | OPEN | Opendoor | 4.74 | 56.40 | False | above | 49.70 | 606.10 |
| 5 | AAOI | Applied Optoelectronics | 114.86 | 55.10 | True | below | 24.40 | 569.40 |
| 6 | IQ | iQIYI | 1.07 | 54.90 | False | above | 53.10 | -40.70 |
| 7 | ON | ON Semiconductor | 93.09 | 53.30 | True | below | 36.20 | 114.70 |
| 8 | ARM | Arm Holdings | 295.49 | 52.90 | True | below | 29.10 | 133.50 |
| 9 | RKLB | Rocket Lab USA | 82.53 | 52.90 | True | below | 34.50 | 183.10 |
| 10 | CBOE | Cboe | 267.95 | 52.60 | False | above | 51.40 | 20.40 |
| 11 | BKR | Baker Hughes | 56.99 | 51.20 | True | below | 35.50 | 62.90 |
| 12 | AXTI | AXT Inc | 59.84 | 51.10 | True | below | 27.00 | 3,805.30 |
| 13 | LITE | Lumentum | 700.29 | 50.60 | True | below | 29.20 | 848.20 |
| 14 | CC | Chemours | 18.50 | 50.40 | True | below | 31.40 | 68.70 |
| 15 | LOT | Lotus Technology | 1.23 | 50.40 | False | above | 56.00 | -43.70 |
| 16 | PUMP | ProPetro | 12.84 | 49.90 | True | below | 32.50 | 138.90 |
| 17 | TM | Toyota | 177.35 | 49.50 | False | above | 48.90 | 5.50 |
| 18 | META | Meta Platforms (Facebook) | 605.45 | 48.30 | False | above | 51.20 | -17.30 |
| 19 | KWEB | Krane Shares Trust - KraneShares CSI China Internet ETF | 26.48 | 47.70 | False | above | 55.40 | -17.40 |
| 20 | DOW | Dow | 29.45 | 47.50 | True | below | 30.80 | 30.10 |
| 21 | PG | Procter & Gamble | 149.02 | 47.20 | True | inside | 44.10 | -6.10 |
| 22 | IGV | BlackRock Institutional Trust Company N.A. - iShares Expanded Tech-Sof | 92.26 | 47.20 | False | above | 52.30 | -13.40 |
| 23 | CAN | Canaan | 0.33 | 46.20 | False | above | 45.40 | -48.40 |
| 24 | BABA | Alibaba | 109.64 | 45.00 | False | above | 48.10 | 13.90 |
| 25 | PYPL | PayPal | 44.30 | 44.80 | False | above | 52.80 | -45.50 |
| 26 | SQQQ | ProShares Trust - ProShares UltraPro Short QQQ | 40.35 | 44.50 | False | above | 55.60 | -53.70 |
| 27 | GIS | General Mills | 36.81 | 44.30 | False | above | 60.30 | -32.40 |
| 28 | ONDS | Ondas Holdings | 7.50 | 44.30 | False | below | 29.90 | 496.00 |
| 29 | NOW | ServiceNow | 107.38 | 44.20 | False | above | 56.90 | -45.70 |
| 30 | COST | Costco | 954.65 | 43.90 | False | below | 38.60 | -1.50 |
| 31 | ABT | Abbott Laboratories | 95.41 | 43.50 | False | above | 63.30 | -30.50 |
| 32 | CRM | Salesforce | 166.44 | 43.00 | False | above | 55.30 | -30.80 |
| 33 | DJT | Trump Media & Technology Group | 8.24 | 41.40 | False | above | 51.00 | -55.80 |
| 34 | ADBE | Adobe | 221.01 | 41.20 | False | above | 62.70 | -33.30 |
| 35 | SOUN | SoundHound AI | 6.79 | 40.80 | False | inside | 45.40 | -35.10 |
| 36 | PLTR | Palantir | 130.32 | 39.90 | False | above | 47.40 | -2.60 |
| 37 | MCD | McDonald | 278.24 | 38.40 | False | above | 42.20 | -3.00 |
| 38 | ICE | Intercontinental Exchange | 138.27 | 38.20 | False | above | 45.90 | -22.00 |
| 39 | MA | Mastercard | 519.99 | 38.00 | False | above | 59.10 | -12.60 |
| 40 | SE | Sea (Garena) | 105.19 | 37.80 | False | above | 78.80 | -42.70 |


_...and 25 more._

## SKIPPED  (5)

Not enough clean daily history to run the model.

SPCX, DAY, RE, AVEX, GPS
