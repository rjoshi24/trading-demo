# WSB Composite Swing-Model Screen

_Generated 2026-07-08 17:56 | latest daily bar: **2026-07-08** | universe: top 200 r/wallstreetbets tickers by mention count_

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
| CLOSE TO BUY | 49 |
| HOLD (UPTREND) | 14 |
| SELL / EXIT | 56 |
| WATCH | 65 |
| SKIPPED | 4 |

## BUY NOW  (12)

Regime is bullish, a **fresh entry trigger fired on the latest daily bar** (20-day breakout, band reclaim, or a squeeze firing up) and the composite score clears the buy threshold. Act at next open, size with the ATR stop.

| group_rank | ticker | name | close | score | rsi | mom_12_1_% | squeeze_on | vol_ratio | band_bot | band_top | need_move_% | bt_trades | bt_winrate_% | bt_expectancy_$ | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ANET | Arista Networks | 177.35 | 93.20 | 55.20 | 52.00 | True | 0.85 | 164.72 | 165.21 | -1.57 | 28.00 | 50.00 | 17.62 | entry trigger: 20-day breakout, squeeze fired up (act at next open) |
| 2 | PENG | Penguin Solutions | 76.81 | 91.80 | 61.40 | 185.90 | True | 2.77 | 65.01 | 65.49 | -1.04 | 15.00 | 46.70 | 134.21 | entry trigger: 20-day breakout, reclaimed the band, squeeze fired up (act at next open) |
| 3 | DELL | Dell | 431.10 | 88.30 | 57.10 | 220.90 | True | 0.91 | 402.48 | 409.80 | 0.69 | 19.00 | 57.90 | 96.42 | entry trigger: squeeze fired up (act at next open) |
| 4 | AAPL | Apple | 314.27 | 84.30 | 60.00 | 47.00 | False | 0.34 | 295.68 | 298.96 | -0.51 | 19.00 | 57.90 | 19.92 | entry trigger: 20-day breakout (act at next open) |
| 5 | AVGO | Broadcom | 388.74 | 79.60 | 54.20 | 41.50 | True | 0.64 | 380.68 | 384.82 | 5.65 | 27.00 | 48.10 | 45.87 | entry trigger: reclaimed the band (act at next open) |
| 6 | ET | Energy Transfer Partners | 19.83 | 78.80 | 69.70 | 17.70 | False | 0.76 | 19.11 | 19.28 | -0.11 | 26.00 | 50.00 | 10.68 | entry trigger: 20-day breakout (act at next open) |
| 7 | WTI | W&T Offshore | 3.64 | 76.60 | 65.10 | 118.70 | False | 1.35 | 3.41 | 3.42 | 17.42 | 15.00 | 33.30 | 6.97 | entry trigger: reclaimed the band (act at next open) |
| 8 | XLE | SSgA Active Trust - SSgA Energy Select Sector SPDR | 55.28 | 75.70 | 52.00 | 37.00 | False | 0.81 | 54.61 | 54.71 | 4.76 | 23.00 | 21.70 | 5.52 | entry trigger: reclaimed the band (act at next open) |
| 9 | TXN | Texas Instruments | 304.92 | 72.70 | 49.70 | 37.30 | False | 0.36 | 299.96 | 301.32 | 8.97 | 21.00 | 52.40 | 29.21 | entry trigger: reclaimed the band (act at next open) |
| 10 | NVDA | NVIDIA | 202.08 | 64.40 | 44.30 | 29.60 | False | 0.58 | 201.59 | 201.86 | 5.13 | 27.00 | 40.70 | 27.70 | entry trigger: reclaimed the band (act at next open) |
| 11 | COP | ConocoPhillips | 109.76 | 62.80 | 46.30 | 30.80 | False | 0.57 | 109.29 | 109.42 | 9.25 | 18.00 | 22.20 | -13.85 | entry trigger: reclaimed the band (act at next open) |
| 12 | CVX | Chevron | 175.75 | 61.20 | 43.40 | 32.40 | False | 0.55 | 175.22 | 175.70 | 7.99 | 26.00 | 23.10 | -9.67 | entry trigger: reclaimed the band (act at next open) |

## CLOSE TO BUY  (49)

Bullish regime and a **high score, but no trigger yet** -- the setup is building: a volatility squeeze is coiled, price is a few percent under the 20-day high, or it's hugging the support band. These are the watch-closely names.

| group_rank | ticker | name | close | score | pos_vs_band | prox_high_% | squeeze_on | rsi | mom_12_1_% | band_bot | band_top | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ADM | Archer Daniels Midland | 79.79 | 90.10 | above | 1.87 | False | 58.10 | 53.10 | 77.63 | 77.78 | 1.9% under the 20-day high -- watch for the trigger |
| 2 | ZETA | Zeta Global | 21.42 | 89.50 | above | 2.12 | False | 58.80 | 48.10 | 19.90 | 20.27 | 2.1% under the 20-day high -- watch for the trigger |
| 3 | CVS | CVS Health | 104.80 | 86.40 | above | 0.01 | False | 62.20 | 49.10 | 101.21 | 101.90 | 0.0% under the 20-day high -- watch for the trigger |
| 4 | YOU | CLEAR Secure | 55.71 | 85.70 | above | 1.85 | False | 61.00 | 92.80 | 53.42 | 54.64 | 1.9% under the 20-day high -- watch for the trigger |
| 5 | OUT | Outfront Media | 33.10 | 82.30 | above | 0.42 | False | 68.70 | 93.70 | 31.93 | 32.27 | 0.4% under the 20-day high -- watch for the trigger |
| 6 | MO | Altria Group | 73.16 | 80.20 | above | 1.22 | False | 62.20 | 26.10 | 71.50 | 71.70 | 1.2% under the 20-day high -- watch for the trigger |
| 7 | HUM | Humana | 399.60 | 79.70 | above | 2.46 | False | 68.20 | 49.40 | 373.31 | 377.91 | 2.5% under the 20-day high -- watch for the trigger |
| 8 | RY | Royal Bank Of Canada | 206.32 | 78.20 | above | 1.33 | False | 61.90 | 49.50 | 202.17 | 202.97 | 1.3% under the 20-day high -- watch for the trigger |
| 9 | LLY | Eli Lilly | 1,223.49 | 78.10 | above | 0.99 | False | 68.20 | 47.40 | 1,159.69 | 1,161.38 | 1.0% under the 20-day high -- watch for the trigger |
| 10 | KO | Coca-Cola | 83.99 | 77.40 | above | 0.18 | False | 66.70 | 14.40 | 81.62 | 81.62 | 0.2% under the 20-day high -- watch for the trigger |
| 11 | UNH | UnitedHealth | 426.55 | 77.10 | above | 0.38 | False | 60.90 | 34.30 | 412.09 | 413.48 | 0.4% under the 20-day high -- watch for the trigger |
| 12 | IBKR | Interactive Brokers | 93.26 | 76.20 | above | 3.82 | False | 50.30 | 46.60 | 91.25 | 91.91 | 3.8% under the 20-day high -- watch for the trigger |
| 13 | JUST | Goldman Sachs ETF Trust - Goldman Sachs Just Us Large Cap Equity ETF | 106.63 | 74.90 | above | 0.68 | False | 48.30 | 20.40 | 105.93 | 106.11 | 0.7% under the 20-day high -- watch for the trigger |
| 14 | NET | Cloudflare | 265.76 | 74.50 | above | 1.16 | False | 72.60 | 29.70 | 236.00 | 241.00 | 1.2% under the 20-day high -- watch for the trigger |
| 15 | GOOGL | Alphabet (Google) | 359.07 | 74.20 | inside | 3.95 | False | 41.60 | 108.90 | 357.97 | 360.48 | 4.0% under the 20-day high; hugging the support band -- watch for the trigger |
| 16 | AM | Antero Midstream | 22.65 | 73.70 | above | 2.39 | False | 65.60 | 25.90 | 22.08 | 22.19 | 2.4% under the 20-day high -- watch for the trigger |
| 17 | VOO | Vanguard S&P 500 ETF | 683.89 | 73.60 | above | 1.16 | False | 46.90 | 19.90 | 680.91 | 682.15 | 1.2% under the 20-day high -- watch for the trigger |
| 18 | SPY | SPDR S&P 500 ETF Trust | 744.01 | 73.60 | above | 1.19 | False | 46.90 | 19.80 | 740.87 | 742.20 | 1.2% under the 20-day high -- watch for the trigger |
| 19 | RXT | Rackspace Technology | 6.26 | 72.00 | inside | 20.38 | False | 50.30 | 251.10 | 6.13 | 6.29 | hugging the support band -- watch for the trigger |
| 20 | EA | Electronic Arts | 205.35 | 69.50 | above | 0.05 | False | 72.60 | 32.70 | 204.05 | 204.18 | 0.1% under the 20-day high -- watch for the trigger |
| 21 | USO | United States Commodity Funds LLC - United States Oil Fund | 111.74 | 68.30 | below | 20.95 | False | 44.00 | 73.90 | 113.82 | 114.23 | hugging the support band -- watch for the trigger |
| 22 | BAC | Bank of America | 58.51 | 68.10 | above | 2.38 | False | 59.80 | 12.50 | 57.09 | 57.24 | 2.4% under the 20-day high -- watch for the trigger |
| 23 | AIR | AAR | 133.65 | 67.70 | inside | 7.46 | False | 55.00 | 65.20 | 133.16 | 134.23 | hugging the support band -- watch for the trigger |
| 24 | JNJ | Johnson & Johnson | 265.57 | 67.00 | above | 0.63 | False | 73.80 | 53.70 | 246.03 | 248.28 | 0.6% under the 20-day high -- watch for the trigger |
| 25 | XOM | Exxon Mobil | 140.52 | 67.00 | inside | 7.99 | False | 46.60 | 39.20 | 140.42 | 140.92 | hugging the support band -- watch for the trigger |
| 26 | SO | Southern Company | 96.61 | 66.90 | above | 1.42 | False | 57.50 | 4.30 | 95.03 | 95.22 | 1.4% under the 20-day high -- watch for the trigger |
| 27 | DTE | DTE Energy | 151.96 | 66.60 | above | 1.63 | False | 58.80 | 14.00 | 149.51 | 149.69 | 1.6% under the 20-day high -- watch for the trigger |
| 28 | DFTX | Definium Therapeutics | 45.87 | 66.50 | above | 2.55 | False | 86.20 | 227.10 | 35.62 | 37.47 | 2.5% under the 20-day high -- watch for the trigger |
| 29 | CSCO | Cisco | 113.34 | 66.30 | below | 9.13 | False | 39.90 | 79.50 | 116.10 | 117.51 | hugging the support band -- watch for the trigger |
| 30 | ES | Eversource Energy | 74.03 | 66.10 | above | 0.97 | False | 66.70 | 14.70 | 71.33 | 71.78 | 1.0% under the 20-day high -- watch for the trigger |
| 31 | CL | Colgate-Palmolive | 93.35 | 65.90 | above | 1.91 | False | 58.10 | -2.70 | 91.34 | 91.61 | 1.9% under the 20-day high -- watch for the trigger |
| 32 | GD | General Dynamics | 372.01 | 65.70 | above | 1.31 | False | 56.50 | 19.10 | 355.46 | 356.53 | 1.3% under the 20-day high -- watch for the trigger |
| 33 | CI | Cigna | 290.77 | 65.00 | above | 2.49 | False | 49.00 | -6.20 | 284.29 | 286.08 | 2.5% under the 20-day high -- watch for the trigger |
| 34 | JPM | JPMorgan Chase | 332.62 | 64.90 | above | 1.98 | False | 53.00 | 8.50 | 326.21 | 326.92 | 2.0% under the 20-day high -- watch for the trigger |
| 35 | RTX | Raytheon Technologies | 195.81 | 64.50 | above | 2.84 | False | 59.90 | 26.00 | 188.46 | 189.36 | 2.8% under the 20-day high -- watch for the trigger |
| 36 | ED | Consolidated Edison | 112.76 | 63.50 | above | 1.09 | False | 63.50 | 10.10 | 109.64 | 110.08 | 1.1% under the 20-day high -- watch for the trigger |
| 37 | EW | Edwards Lifesciences | 93.79 | 62.70 | above | 1.48 | False | 66.10 | 12.10 | 89.40 | 90.10 | 1.5% under the 20-day high -- watch for the trigger |
| 38 | IBM | IBM | 302.27 | 62.50 | above | 1.28 | False | 66.40 | -0.10 | 275.04 | 279.33 | 1.3% under the 20-day high -- watch for the trigger |
| 39 | AMZN | Amazon | 241.64 | 61.60 | inside | 1.81 | False | 46.50 | 10.10 | 239.58 | 242.81 | 1.8% under the 20-day high; hugging the support band -- watch for the trigger |
| 40 | GO | Grocery Outlet | 10.21 | 61.00 | above | 1.76 | False | 55.70 | -35.40 | 9.65 | 9.71 | 1.8% under the 20-day high -- watch for the trigger |
| 41 | GL | Globe Life | 176.74 | 60.60 | above | 1.94 | False | 73.00 | 32.10 | 172.11 | 172.74 | 1.9% under the 20-day high -- watch for the trigger |
| 42 | RIVN | Rivian | 16.55 | 58.80 | inside | 21.69 | False | 52.60 | 28.20 | 16.32 | 16.58 | hugging the support band -- watch for the trigger |
| 43 | EXC | Exelon Corporation | 47.40 | 58.70 | above | 1.00 | False | 55.50 | 8.80 | 46.52 | 46.60 | 1.0% under the 20-day high -- watch for the trigger |
| 44 | BP | BP | 39.07 | 58.60 | below | 11.90 | False | 39.30 | 49.70 | 39.32 | 39.39 | hugging the support band -- watch for the trigger |
| 45 | GE | General Electric | 355.80 | 57.80 | inside | 6.43 | False | 53.80 | 32.40 | 355.64 | 356.88 | hugging the support band -- watch for the trigger |
| 46 | ALL | Allstate | 251.17 | 55.10 | above | 0.12 | False | 79.80 | 15.30 | 232.60 | 234.87 | 0.1% under the 20-day high -- watch for the trigger |
| 47 | GM | General Motors | 75.58 | 54.10 | below | 11.23 | False | 25.00 | 59.60 | 78.30 | 79.07 | hugging the support band -- watch for the trigger |
| 48 | AMP | Ameriprise Financial | 491.68 | 52.70 | above | 3.29 | False | 59.20 | -14.10 | 468.30 | 472.24 | 3.3% under the 20-day high -- watch for the trigger |
| 49 | PEG | PSEG | 81.17 | 52.00 | above | 2.97 | False | 51.10 | -1.10 | 80.67 | 80.77 | 3.0% under the 20-day high -- watch for the trigger |

## HOLD (UPTREND)  (14)

Already **above the band and trending**. Hold if you are long; a new buyer here is chasing an extended move (wait for a pullback to the band).

| group_rank | ticker | name | close | score | rsi | mom_12_1_% | band_bot | band_top | bt_winrate_% | bt_expectancy_$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MS | Morgan Stanley | 218.21 | 78.60 | 47.20 | 51.00 | 215.40 | 217.27 | 45.00 | 37.12 |
| 2 | GEV | GE Vernova | 1,084.24 | 70.50 | 57.90 | 76.40 | 1,047.07 | 1,066.74 | 47.60 | 81.81 |
| 3 | SLS | Sellas Life Sciences | 12.34 | 69.20 | 66.60 | 279.30 | 10.47 | 11.18 | 31.20 | 34.06 |
| 4 | BB | BlackBerry | 10.89 | 67.00 | 61.40 | 118.30 | 10.13 | 10.32 | 50.00 | 109.12 |
| 5 | FOR | Forestar Group | 29.99 | 66.70 | 57.20 | 35.00 | 29.89 | 29.97 | 33.30 | -4.59 |
| 6 | RDDT | Reddit | 192.90 | 60.80 | 59.30 | 13.10 | 176.96 | 179.14 | 50.00 | 152.84 |
| 7 | BY | Byline Bancorp | 36.79 | 59.50 | 65.90 | 22.00 | 36.19 | 36.23 | 52.40 | 17.94 |
| 8 | LOVE | LoveSac | 16.64 | 57.60 | 64.70 | -15.30 | 16.12 | 16.41 | 25.00 | -8.06 |
| 9 | BA | Boeing | 224.36 | 57.40 | 46.90 | -1.50 | 221.45 | 222.62 | 56.20 | 7.82 |
| 10 | SGOV | iShares Trust - iShares 0-3 Month Treasury Bond ETF | 100.47 | 53.70 | nan | 3.30 | 100.32 | 100.34 | 100.00 | 2.44 |
| 11 | HOOD | Robinhood | 111.36 | 49.50 | 62.30 | -11.80 | 101.37 | 101.63 | 50.00 | 118.66 |
| 12 | NVO | Novo Nordisk | 49.17 | 49.30 | 77.00 | -35.00 | 46.35 | 47.01 | 50.00 | 0.90 |
| 13 | GRPN | Groupon | 25.95 | 46.00 | 81.80 | -55.20 | 20.49 | 21.83 | 29.40 | 47.58 |
| 14 | EVER | EverQuote | 24.56 | 43.20 | 73.20 | -21.80 | 22.01 | 22.47 | 50.00 | 44.08 |

## SELL / EXIT  (56)

An **exit condition is present** -- price lost the 20/21 support band, or a death cross with price below the 200-SMA. If you hold it, the model says exit.

| group_rank | ticker | name | close | score | pos_vs_band | band_bot | band_top | rsi | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CAVA | CAVA Group | 67.36 | 17.30 | below | 78.36 | 81.23 | 23.70 | exit signal: lost the support band |
| 2 | AGI | Alamos Gold | 29.06 | 19.20 | below | 32.84 | 32.93 | 17.40 | exit signal: lost the support band |
| 3 | LINK | Interlink Electronics | 4.05 | 24.70 | below | 4.29 | 4.31 | 46.10 | exit signal: lost the support band |
| 4 | HD | Home Depot | 335.87 | 25.00 | below | 337.75 | 337.98 | 49.30 | exit signal: lost the support band |
| 5 | EL | Estee Lauder | 81.39 | 25.00 | below | 83.30 | 84.17 | 36.40 | exit signal: lost the support band |
| 6 | SAP | SAP | 157.81 | 25.20 | below | 159.57 | 161.52 | 42.50 | exit signal: lost the support band |
| 7 | AVAV | AeroVironment | 157.83 | 25.70 | below | 163.05 | 165.97 | 46.40 | exit signal: lost the support band |
| 8 | AVY | Avery Dennison | 157.02 | 27.20 | below | 161.27 | 161.57 | 42.00 | exit signal: lost the support band |
| 9 | CME | CME Group | 244.71 | 27.30 | above | 243.46 | 243.52 | 38.40 | exit signal: death cross / below 200-SMA |
| 10 | DIS | Walt Disney | 97.37 | 27.50 | below | 98.93 | 99.08 | 42.30 | exit signal: lost the support band |
| 11 | AEM | Agnico Eagle Mines | 144.29 | 27.70 | below | 159.06 | 159.58 | 14.50 | exit signal: lost the support band |
| 12 | LOW | Lowe's Companies | 213.66 | 27.80 | below | 219.76 | 220.04 | 40.40 | exit signal: lost the support band |
| 13 | IP | International Paper | 36.49 | 29.90 | below | 36.80 | 36.93 | 52.30 | exit signal: lost the support band |
| 14 | DC | Dakota Gold | 4.21 | 31.40 | below | 4.55 | 4.60 | 23.40 | exit signal: lost the support band |
| 15 | VZ | Verizon | 42.90 | 32.20 | below | 44.61 | 45.09 | 32.70 | exit signal: lost the support band |
| 16 | IT | Gartner | 135.82 | 32.70 | below | 137.33 | 139.14 | 44.40 | exit signal: lost the support band |
| 17 | FOX | Fox Corporation | 48.26 | 32.90 | below | 49.89 | 50.10 | 51.10 | exit signal: lost the support band |
| 18 | NFLX | Netflix | 76.21 | 33.20 | below | 76.37 | 77.10 | 44.30 | exit signal: lost the support band |
| 19 | RC | Ready Capital | 1.67 | 34.60 | below | 1.70 | 1.71 | 51.10 | exit signal: lost the support band |
| 20 | JD | Jingdong Mall | 27.52 | 34.70 | above | 27.00 | 27.15 | 43.30 | exit signal: death cross / below 200-SMA |
| 21 | GLD | SSgA SPDR Gold Shares | 373.03 | 36.40 | below | 379.87 | 382.68 | 31.80 | exit signal: lost the support band |
| 22 | APLD | Applied Blockchain | 30.31 | 38.30 | below | 38.44 | 40.03 | 8.00 | exit signal: lost the support band |
| 23 | ASTS | AST SpaceMobile | 73.46 | 42.50 | below | 80.91 | 82.48 | 42.90 | exit signal: lost the support band |
| 24 | TSLA | Tesla | 392.34 | 43.10 | below | 398.99 | 402.95 | 46.60 | exit signal: lost the support band |
| 25 | LMT | Lockheed Martin | 529.75 | 44.30 | above | 521.87 | 522.81 | 47.90 | exit signal: death cross / below 200-SMA |
| 26 | WDC | Western Digital | 534.24 | 45.80 | below | 590.01 | 613.69 | 36.70 | exit signal: lost the support band |
| 27 | GLW | Corning | 184.61 | 50.80 | below | 199.28 | 201.14 | 51.80 | exit signal: lost the support band |
| 28 | PEP | Pepsico | 143.63 | 51.20 | above | 142.42 | 142.85 | 46.00 | exit signal: death cross / below 200-SMA |
| 29 | EWY | BlackRock Institutional Trust Company N.A. - iShares MSCI South Korea | 179.86 | 52.20 | below | 192.83 | 196.37 | 38.00 | exit signal: lost the support band |
| 30 | MRVL | Marvell Technology Group | 232.35 | 54.10 | below | 260.38 | 274.22 | 38.00 | exit signal: lost the support band |
| 31 | DE | Deere & Company | 596.27 | 54.50 | below | 599.04 | 601.29 | 53.80 | exit signal: lost the support band |
| 32 | SOXL | Direxion Shares ETF Trust - Direxion Daily Semiconductor Bull 3X Share | 172.23 | 54.80 | below | 214.54 | 225.86 | 43.10 | exit signal: lost the support band |
| 33 | WULF | TeraWulf | 21.72 | 54.90 | below | 24.39 | 25.40 | 28.30 | exit signal: lost the support band |
| 34 | RTH | VanEck Vectors ETF Trust - VanEck Vectors Retail ETF | 257.06 | 55.80 | below | 257.41 | 257.52 | 42.30 | exit signal: lost the support band |
| 35 | SNDK | Sandisk | 1,654.54 | 55.90 | below | 1,867.45 | 1,954.49 | 42.80 | exit signal: lost the support band |
| 36 | BE | Bloom Energy | 245.32 | 56.00 | below | 282.31 | 283.77 | 44.50 | exit signal: lost the support band |
| 37 | MU | Micron Technology | 932.66 | 56.00 | below | 1,012.35 | 1,045.46 | 44.90 | exit signal: lost the support band |
| 38 | INTC | Intel | 107.08 | 56.50 | below | 121.44 | 124.05 | 44.20 | exit signal: lost the support band |
| 39 | TQQQ | ProShares Trust - ProShares UltraPro QQQ | 71.77 | 56.90 | below | 75.99 | 76.31 | 41.40 | exit signal: lost the support band |
| 40 | NBIS | Nebius Group | 207.62 | 57.00 | below | 235.15 | 244.63 | 35.40 | exit signal: lost the support band |
| 41 | QQQ | Invesco QQQ ETF | 708.15 | 57.00 | below | 718.39 | 719.72 | 43.00 | exit signal: lost the support band |
| 42 | GS | Goldman Sachs | 1,025.46 | 57.30 | below | 1,039.90 | 1,052.63 | 32.90 | exit signal: lost the support band |
| 43 | FAST | Fastenal | 46.58 | 57.40 | below | 46.71 | 46.73 | 53.10 | exit signal: lost the support band |
| 44 | CAT | Caterpillar | 940.29 | 57.60 | below | 964.29 | 967.95 | 49.40 | exit signal: lost the support band |
| 45 | SOXX | BlackRock Institutional Trust Company N.A. - BTC iShares PHLX Semicond | 559.43 | 59.10 | below | 585.64 | 596.67 | 45.50 | exit signal: lost the support band |
| 46 | AMAT | Applied Materials | 570.73 | 59.40 | below | 585.18 | 598.98 | 50.20 | exit signal: lost the support band |
| 47 | PL | Planet Labs | 27.07 | 60.20 | below | 29.68 | 31.37 | 46.40 | exit signal: lost the support band |
| 48 | DAL | Delta Air Lines | 86.89 | 60.70 | below | 87.18 | 87.20 | 59.80 | exit signal: lost the support band |
| 49 | SMH | VanEck Vectors ETF Trust - VanEck Vectors Semiconductor ETF | 589.93 | 61.00 | below | 609.98 | 618.65 | 45.60 | exit signal: lost the support band |
| 50 | VT | Vanguard Group, Inc. - Vanguard Total World Stock ETF | 155.41 | 61.30 | below | 155.73 | 155.78 | 43.80 | exit signal: lost the support band |
| 51 | ASML | ASML | 1,770.00 | 65.30 | below | 1,795.37 | 1,835.13 | 48.30 | exit signal: lost the support band |
| 52 | TSM | TSMC | 435.81 | 65.60 | below | 438.07 | 439.23 | 52.30 | exit signal: lost the support band |
| 53 | IWM | BlackRock Institutional Trust Company N.A. - BTC iShares Russell 2000 | 292.84 | 65.90 | below | 294.33 | 294.65 | 51.20 | exit signal: lost the support band |
| 54 | AMD | AMD | 511.07 | 68.00 | below | 518.58 | 521.80 | 50.60 | exit signal: lost the support band |
| 55 | HPE | Hewlett Packard Enterprise | 44.71 | 68.70 | below | 44.72 | 46.18 | 38.80 | exit signal: lost the support band |
| 56 | GOOG | Alphabet (Google) | 355.74 | 72.60 | below | 355.89 | 357.97 | 41.50 | exit signal: lost the support band |

## WATCH  (65)

No setup: regime and/or composite score too weak. Nothing to do yet.

| group_rank | ticker | name | close | score | regime_ok | pos_vs_band | rsi | mom_12_1_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | GOAT | VanEck Vectors ETF Trust - VanEck Vectors Morningstar Global Wide Moat | 38.58 | 57.10 | False | above | 52.70 | 8.00 |
| 2 | KORU | Direxion Shares ETF Trust - Direxion Daily South Korea Bull 3X Shares | 527.43 | 56.40 | True | below | 34.40 | 721.90 |
| 3 | OPEN | Opendoor | 4.74 | 55.80 | False | above | 49.90 | 606.10 |
| 4 | AAOI | Applied Optoelectronics | 114.36 | 55.10 | True | below | 24.10 | 569.40 |
| 5 | IQ | iQIYI | 1.06 | 54.00 | False | above | 52.10 | -40.70 |
| 6 | ON | ON Semiconductor | 92.57 | 53.30 | True | below | 35.90 | 114.70 |
| 7 | ARM | Arm Holdings | 296.54 | 52.90 | True | below | 29.30 | 133.50 |
| 8 | RKLB | Rocket Lab USA | 81.75 | 52.80 | True | below | 34.20 | 183.10 |
| 9 | CBOE | Cboe | 268.15 | 52.60 | False | above | 51.50 | 20.40 |
| 10 | NOK | Nokia | 11.76 | 51.50 | True | below | 31.70 | 183.40 |
| 11 | AXTI | AXT Inc | 59.24 | 51.00 | True | below | 26.40 | 3,805.30 |
| 12 | BKR | Baker Hughes | 56.87 | 50.90 | True | below | 34.90 | 62.90 |
| 13 | LITE | Lumentum | 700.21 | 50.60 | True | below | 29.20 | 848.20 |
| 14 | CC | Chemours | 18.49 | 50.40 | True | below | 31.30 | 68.70 |
| 15 | PUMP | ProPetro | 12.77 | 49.80 | True | below | 31.60 | 138.90 |
| 16 | META | Meta Platforms (Facebook) | 604.68 | 48.10 | False | above | 51.00 | -17.30 |
| 17 | KWEB | Krane Shares Trust - KraneShares CSI China Internet ETF | 26.42 | 47.40 | False | above | 55.00 | -17.40 |
| 18 | PG | Procter & Gamble | 148.95 | 47.10 | True | inside | 44.10 | -6.10 |
| 19 | IGV | BlackRock Institutional Trust Company N.A. - iShares Expanded Tech-Sof | 92.08 | 47.00 | False | above | 51.80 | -13.40 |
| 20 | CAN | Canaan | 0.33 | 46.20 | False | above | 46.10 | -48.40 |
| 21 | GIS | General Mills | 36.70 | 45.00 | False | above | 59.80 | -32.40 |
| 22 | BABA | Alibaba | 109.15 | 45.00 | False | above | 47.30 | 13.90 |
| 23 | PYPL | PayPal | 44.22 | 44.60 | False | above | 52.50 | -45.50 |
| 24 | SQQQ | ProShares Trust - ProShares UltraPro Short QQQ | 40.63 | 44.50 | False | above | 56.10 | -53.70 |
| 25 | LOT | Lotus Technology | 1.22 | 44.40 | False | above | 54.50 | -43.70 |
| 26 | TM | Toyota | 176.93 | 44.30 | False | above | 48.30 | 5.50 |
| 27 | ONDS | Ondas Holdings | 7.40 | 44.20 | False | below | 28.20 | 496.00 |
| 28 | NOW | ServiceNow | 107.18 | 44.00 | False | above | 56.70 | -45.70 |
| 29 | COST | Costco | 954.03 | 43.70 | False | below | 38.30 | -1.50 |
| 30 | ABT | Abbott Laboratories | 95.22 | 43.30 | False | above | 62.60 | -30.50 |
| 31 | CRM | Salesforce | 166.27 | 43.10 | False | above | 55.10 | -30.80 |
| 32 | ADBE | Adobe | 220.67 | 41.20 | False | above | 62.30 | -33.30 |
| 33 | DJT | Trump Media & Technology Group | 8.20 | 40.80 | False | above | 50.50 | -55.80 |
| 34 | PLTR | Palantir | 129.79 | 39.40 | False | above | 47.00 | -2.60 |
| 35 | SOXS | Direxion Shares ETF Trust - Direxion Daily Semiconductor Bear 3X Share | 4.60 | 38.20 | False | inside | 50.20 | -95.50 |
| 36 | ICE | Intercontinental Exchange | 138.13 | 38.10 | False | above | 45.70 | -22.00 |
| 37 | MA | Mastercard | 518.64 | 37.80 | False | above | 58.30 | -12.60 |
| 38 | SE | Sea (Garena) | 104.81 | 37.70 | False | above | 78.60 | -42.70 |
| 39 | DOW | Dow | 29.28 | 36.90 | False | below | 29.50 | 30.10 |
| 40 | IREN | Iris Energy | 40.60 | 36.60 | False | below | 22.70 | 220.60 |


_...and 25 more._

## SKIPPED  (4)

Not enough clean daily history to run the model.

SPCX, DAY, AVEX, GPS
