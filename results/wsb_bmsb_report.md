# WSB Top-200 - BMSB Buy-Readiness Screen

_Generated 2026-07-06 20:06 | latest weekly bar: **2026-07-06** | universe: top 200 r/wallstreetbets tickers by mention count_

> **Research only, not financial advice.** Each ticker is scored with its own best-fitting BMSB config from a parameter sweep (ranked by Total P&L x Win Rate over ~10y of weekly data). Best-fit configs are partly curve-fit - treat as candidates.

## How to read this

- **BUY NOW** - a fresh entry signal on the latest weekly candle.
- **CLOSE TO ENTERING** - flat but within ~6% of the trigger, or in the anticipate buy-zone; these are the ones to watch this week.
- **IN POSITION** - already trending above the band (the strategy is holding); a new buyer is chasing.
- **SELL / EXIT** and **WATCH** are shown for completeness.
- `readiness` 0-100 = how close to a buy. `need_move_%` = % price move to reach the trigger (negative = price is already above it).

## Summary

| Group | Count |
| --- | --- |
| BUY NOW | 4 |
| CLOSE TO ENTERING | 17 |
| IN POSITION | 76 |
| SELL / EXIT | 18 |
| WATCH | 80 |
| SKIPPED | 5 |

## BUY NOW  (4)

Strategy fires a **fresh BUY** on the latest weekly bar. These are the actionable entries right now (act at next open, per the strategy).

| group_rank | ticker | name | close | readiness | recommendation | mode | band_bot | band_top | rsi | need_move_% | bt_trades | bt_winrate_% | bt_pnl_$ | bt_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | NU | Nu Holdings | 14.06 | 100.00 | BUY (entry signal - act at next open) | reclaim | 13.70 | 14.25 | 49.40 | -2.55 | 8.00 | 50.00 | 1,635.75 | 817.90 |
| 2 | OPEN | Opendoor | 5.09 | 100.00 | BUY (entry signal - act at next open) | breakout | 4.85 | 4.95 | 53.60 | -2.75 | 8.00 | 37.50 | 957.47 | 359.10 |
| 3 | TM | Toyota | 179.93 | 100.00 | BUY (entry signal - act at next open) | anticipate | 196.79 | 203.78 | 31.30 | 0.00 | 14.00 | 64.30 | 340.74 | 219.10 |
| 4 | GOAT | VanEck Vectors ETF Trust - VanEck Vectors Morningstar Global Wide Moat | 38.58 | 100.00 | BUY (entry signal - act at next open) | reclaim | 38.37 | 38.86 | 61.00 | -0.54 | 14.00 | 42.90 | 249.99 | 107.20 |

## CLOSE TO ENTERING  (17)

Flat and **almost** triggering: price is within a few percent of the entry trigger, or already sitting in the anticipate buy-zone below the band waiting on a momentum flip. These are the watch-closely names.

| group_rank | ticker | name | close | readiness | pos_vs_band | mode | band_bot | band_top | rsi | need_move_% | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | FANG | Diamondback Energy | 173.73 | 80.00 | below | anticipate | 181.74 | 183.31 | 41.40 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 2 | META | Meta Platforms (Facebook) | 600.29 | 77.70 | below | reclaim | 618.14 | 618.22 | 53.50 | 2.97 | 3.0% below the band bottom; a close above it triggers entry |
| 3 | ORCL | Oracle | 143.79 | 75.00 | below | anticipate | 175.04 | 181.44 | 49.50 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 4 | XOM | Exxon Mobil | 136.50 | 75.00 | below | anticipate | 143.04 | 148.06 | 34.50 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 5 | EU | enCore Energy | 1.33 | 75.00 | below | anticipate | 1.61 | 1.76 | 36.50 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 6 | SLV | iShares Silver Trust | 56.12 | 75.00 | below | anticipate | 60.41 | 68.58 | 38.10 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 7 | OKLO | Oklo | 51.84 | 75.00 | below | anticipate | 60.34 | 62.75 | 52.70 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 8 | NVDA | NVIDIA | 195.55 | 73.10 | inside | breakout | 193.51 | 202.88 | 58.00 | 3.75 | 3.8% below the band top; a close above it triggers entry |
| 9 | ASTS | AST SpaceMobile | 80.64 | 70.00 | below | anticipate | 84.67 | 88.20 | 45.40 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 10 | CC | Chemours | 18.19 | 70.00 | below | anticipate | 19.47 | 20.41 | 42.00 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 11 | DOW | Dow | 27.33 | 70.00 | below | anticipate | 31.81 | 33.78 | 24.80 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 12 | OR | Osisko Gold Royalties | 30.82 | 70.00 | below | anticipate | 35.30 | 38.06 | 30.50 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 13 | FOX | Fox Corporation | 49.90 | 70.00 | below | anticipate | 54.77 | 55.03 | 45.50 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 14 | WMT | Walmart | 110.65 | 70.00 | below | anticipate | 118.26 | 122.97 | 31.00 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 15 | PFE | Pfizer | 23.73 | 70.00 | below | anticipate | 25.26 | 26.05 | 22.40 | 0.00 | below band in RSI buy-zone; needs an up-close with RSI turning up |
| 16 | TIL | Instil Bio | 7.72 | 69.70 | below | reclaim | 7.99 | 8.58 | 45.40 | 3.48 | 3.5% below the band bottom; a close above it triggers entry |
| 17 | PLTR | Palantir | 132.54 | 62.20 | below | reclaim | 139.99 | 142.60 | 44.30 | 5.62 | 5.6% below the band bottom; a close above it triggers entry |

## IN POSITION  (76)

The strategy would **already be long and holding** (price is above the band, riding the trend). Not a fresh entry - a new buyer here is chasing an extended move.

| group_rank | ticker | name | close | recommendation | mode | band_bot | band_top | rsi | need_move_% | bt_winrate_% | bt_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SNDK | Sandisk | 1,744.43 | HOLD (in position - riding the move) | breakout | 980.42 | 1,262.45 | 70.80 | -27.63 | 50.00 | 19,689.00 |
| 2 | SOXL | Direxion Shares ETF Trust - Direxion Daily Semiconductor Bull 3X Share | 194.77 | HOLD (in position - riding the move) | anticipate | 115.09 | 139.30 | 65.90 | -40.91 | 53.30 | 9,681.00 |
| 3 | LITE | Lumentum | 731.25 | HOLD (in position - riding the move) | anticipate | 623.15 | 753.70 | 42.60 | -14.78 | 63.60 | 8,791.10 |
| 4 | MU | Micron Technology | 984.75 | HOLD (in position - riding the move) | anticipate | 735.77 | 769.77 | 75.90 | -25.28 | 58.30 | 7,265.80 |
| 5 | WDC | Western Digital | 577.46 | HOLD (in position - riding the move) | anticipate | 400.11 | 401.89 | 69.20 | -30.71 | 50.00 | 7,134.70 |
| 6 | STX | Seagate Technology | 868.26 | HOLD (in position - riding the move) | anticipate | 617.66 | 704.51 | 71.90 | -28.86 | 61.50 | 6,892.60 |
| 7 | NVTS | Navitas Semiconductor | 15.23 | HOLD (in position - riding the move) | anticipate | 13.87 | 14.73 | 58.60 | -8.91 | 54.50 | 4,607.60 |
| 8 | DELL | Dell | 411.51 | HOLD (in position - riding the move) | anticipate | 258.55 | 306.44 | 82.10 | -37.17 | 69.20 | 4,519.40 |
| 9 | WULF | TeraWulf | 22.21 | HOLD (in position - riding the move) | breakout | 19.33 | 19.43 | 62.40 | -12.52 | 50.00 | 3,785.00 |
| 10 | TQQQ | ProShares Trust - ProShares UltraPro QQQ | 76.42 | HOLD (in position - riding the move) | breakout | 63.34 | 63.63 | 70.70 | -16.74 | 80.00 | 3,589.90 |
| 11 | CRWD | CrowdStrike | 199.38 | HOLD (in position - riding the move) | anticipate | 130.64 | 134.43 | 85.70 | -34.48 | 53.30 | 3,261.90 |
| 12 | CRDO | Credo Technology | 265.55 | HOLD (in position - riding the move) | anticipate | 168.20 | 197.45 | 73.80 | -36.66 | 66.70 | 2,952.60 |
| 13 | AMD | AMD | 552.05 | HOLD (in position - riding the move) | breakout | 328.34 | 427.93 | 81.30 | -22.48 | 60.00 | 2,843.00 |
| 14 | KEEL | Keel Infrastructure | 4.84 | HOLD (in position - riding the move) | breakout | 3.79 | 4.31 | 68.40 | -10.88 | 38.50 | 2,836.10 |
| 15 | LRCX | Lam Research | 350.20 | HOLD (in position - riding the move) | breakout | 269.69 | 307.61 | 73.50 | -12.16 | 53.30 | 2,790.80 |
| 16 | AMAT | Applied Materials | 592.79 | HOLD (in position - riding the move) | breakout | 387.87 | 423.45 | 82.10 | -28.57 | 60.00 | 2,612.00 |
| 17 | SOXX | BlackRock Institutional Trust Company N.A. - BTC iShares PHLX Semicond | 581.51 | HOLD (in position - riding the move) | anticipate | 419.81 | 514.35 | 75.70 | -27.81 | 62.50 | 2,473.70 |
| 18 | MRVL | Marvell Technology Group | 249.27 | HOLD (in position - riding the move) | breakout | 152.80 | 175.48 | 76.10 | -29.60 | 64.30 | 2,471.80 |
| 19 | SMH | VanEck Vectors ETF Trust - VanEck Vectors Semiconductor ETF | 604.30 | HOLD (in position - riding the move) | breakout | 461.72 | 489.07 | 74.90 | -19.07 | 70.00 | 2,463.00 |
| 20 | CAT | Caterpillar | 969.80 | HOLD (in position - riding the move) | anticipate | 745.69 | 838.95 | 84.80 | -23.11 | 72.70 | 2,389.40 |
| 21 | AAOI | Applied Optoelectronics | 123.36 | HOLD (in position - riding the move) | breakout | 102.45 | 120.35 | 53.70 | -2.44 | 30.80 | 2,294.50 |
| 22 | TSM | TSMC | 451.84 | HOLD (in position - riding the move) | reclaim | 357.01 | 408.64 | 77.80 | -20.99 | 57.10 | 2,183.00 |
| 23 | KORU | Direxion Shares ETF Trust - Direxion Daily South Korea Bull 3X Shares | 625.54 | HOLD (in position - riding the move) | breakout | 481.46 | 610.27 | 56.20 | -2.44 | 20.00 | 2,172.70 |
| 24 | GOOG | Alphabet (Google) | 364.90 | HOLD (in position - riding the move) | anticipate | 318.51 | 357.75 | 66.50 | -12.71 | 66.70 | 2,096.80 |
| 25 | BBC | ETFis Series Trust I - Virtus LifeSci Biotech Clinical Trials ETF | 52.92 | HOLD (in position - riding the move) | anticipate | 40.31 | 44.37 | 67.10 | -23.83 | 66.70 | 1,957.60 |
| 26 | MS | Morgan Stanley | 222.07 | HOLD (in position - riding the move) | anticipate | 187.13 | 188.90 | 84.80 | -15.74 | 70.00 | 1,957.40 |
| 27 | LLY | Eli Lilly | 1,202.56 | HOLD (in position - riding the move) | anticipate | 1,032.81 | 1,050.05 | 76.80 | -14.12 | 66.70 | 1,931.30 |
| 28 | CDNS | Cadence Design Systems | 375.77 | HOLD (in position - riding the move) | anticipate | 334.33 | 335.17 | 76.60 | -11.03 | 80.00 | 1,803.70 |
| 29 | QQQ | Invesco QQQ ETF | 722.82 | HOLD (in position - riding the move) | breakout | 660.48 | 664.90 | 75.10 | -8.01 | 91.70 | 1,781.10 |
| 30 | GOOGL | Alphabet (Google) | 366.46 | HOLD (in position - riding the move) | anticipate | 319.64 | 360.23 | 66.60 | -12.78 | 58.30 | 1,773.70 |
| 31 | BB | BlackBerry | 11.36 | HOLD (in position - riding the move) | anticipate | 6.07 | 7.56 | 87.20 | -46.59 | 63.20 | 1,769.30 |
| 32 | NOK | Nokia | 12.52 | HOLD (in position - riding the move) | anticipate | 9.78 | 11.47 | 65.00 | -21.89 | 75.00 | 1,746.70 |
| 33 | HOOD | Robinhood | 117.55 | HOLD (in position - riding the move) | anticipate | 84.27 | 92.29 | 68.40 | -28.31 | 53.80 | 1,614.20 |
| 34 | GE | General Electric | 378.70 | HOLD (in position - riding the move) | breakout | 309.11 | 317.49 | 77.70 | -16.16 | 44.40 | 1,453.20 |
| 35 | ANET | Arista Networks | 173.19 | HOLD (in position - riding the move) | breakout | 143.89 | 157.54 | 65.40 | -9.04 | 33.30 | 1,446.10 |
| 36 | AAPL | Apple | 312.66 | HOLD (in position - riding the move) | anticipate | 272.80 | 276.95 | 72.40 | -12.75 | 66.70 | 1,381.70 |
| 37 | IGV | BlackRock Institutional Trust Company N.A. - iShares Expanded Tech-Sof | 94.81 | HOLD (in position - riding the move) | breakout | 87.60 | 93.62 | 63.70 | -1.26 | 77.80 | 1,370.50 |
| 38 | ET | Energy Transfer Partners | 19.26 | HOLD (in position - riding the move) | anticipate | 18.51 | 19.07 | 56.30 | -3.91 | 71.40 | 1,359.00 |
| 39 | QCOM | QUALCOMM | 186.48 | HOLD (in position - riding the move) | anticipate | 173.54 | 188.44 | 61.10 | -6.94 | 82.40 | 1,354.30 |
| 40 | ALL | Allstate | 248.47 | HOLD (in position - riding the move) | anticipate | 213.24 | 217.97 | 75.20 | -14.18 | 78.60 | 1,284.70 |
| 41 | LIN | Linde | 540.52 | HOLD (in position - riding the move) | anticipate | 485.99 | 506.09 | 61.60 | -10.09 | 77.80 | 1,243.70 |
| 42 | RMD | ResMed | 218.40 | HOLD (in position - riding the move) | anticipate | 207.81 | 221.91 | 47.50 | -4.85 | 81.80 | 1,047.50 |
| 43 | SG | Sweetgreen | 8.04 | HOLD (in position - riding the move) | reclaim | 7.87 | 7.93 | 62.70 | -2.18 | 55.60 | 1,014.50 |
| 44 | EL | Estee Lauder | 84.89 | HOLD (in position - riding the move) | anticipate | 81.57 | 86.20 | 64.10 | -3.91 | 53.30 | 981.30 |
| 45 | VTI | Vanguard Total Stock Market ETF | 371.61 | HOLD (in position - riding the move) | breakout | 347.26 | 354.00 | 80.20 | -4.74 | 75.00 | 967.80 |
| 46 | VOO | Vanguard S&P 500 ETF | 690.58 | HOLD (in position - riding the move) | breakout | 648.22 | 667.23 | 78.60 | -3.38 | 71.40 | 953.90 |
| 47 | SPY | SPDR S&P 500 ETF Trust | 751.26 | HOLD (in position - riding the move) | breakout | 705.34 | 725.97 | 78.50 | -3.37 | 71.40 | 952.80 |
| 48 | JNJ | Johnson & Johnson | 259.29 | HOLD (in position - riding the move) | anticipate | 221.55 | 237.29 | 58.10 | -14.55 | 90.90 | 937.80 |
| 49 | SLS | Sellas Life Sciences | 13.94 | HOLD (in position - riding the move) | breakout | 5.93 | 7.15 | 80.00 | -48.69 | 20.00 | 868.10 |
| 50 | EWY | BlackRock Institutional Trust Company N.A. - iShares MSCI South Korea | 189.85 | HOLD (in position - riding the move) | breakout | 142.51 | 164.78 | 64.60 | -13.20 | 33.30 | 845.70 |
| 51 | IWM | BlackRock Institutional Trust Company N.A. - BTC iShares Russell 2000 | 298.90 | HOLD (in position - riding the move) | anticipate | 271.33 | 274.04 | 78.90 | -9.22 | 66.70 | 844.40 |
| 52 | WTI | W&T Offshore | 3.10 | HOLD (in position - riding the move) | breakout | 2.91 | 3.46 | 49.60 | 11.69 | 46.20 | 766.30 |
| 53 | PG | Procter & Gamble | 149.31 | HOLD (in position - riding the move) | anticipate | 147.99 | 149.14 | 62.40 | -0.89 | 77.80 | 737.90 |
| 54 | JUST | Goldman Sachs ETF Trust - Goldman Sachs Just Us Large Cap Equity ETF | 107.43 | HOLD (in position - riding the move) | anticipate | 100.55 | 103.74 | 81.60 | -6.40 | 72.70 | 732.90 |
| 55 | VSAT | ViaSat | 83.80 | HOLD (in position - riding the move) | breakout | 53.26 | 59.16 | 69.80 | -29.40 | 16.70 | 721.70 |
| 56 | IP | International Paper | 38.60 | HOLD (in position - riding the move) | anticipate | 34.68 | 36.59 | 60.40 | -10.17 | 58.80 | 585.50 |
| 57 | IBM | IBM | 299.49 | HOLD (in position - riding the move) | anticipate | 257.02 | 265.72 | 60.60 | -14.18 | 61.50 | 559.70 |
| 58 | DTE | DTE Energy | 151.43 | HOLD (in position - riding the move) | anticipate | 140.93 | 144.13 | 55.90 | -6.94 | 66.70 | 543.00 |
| 59 | SO | Southern Company | 96.00 | HOLD (in position - riding the move) | anticipate | 92.27 | 94.67 | 48.80 | -3.89 | 83.30 | 499.00 |
| 60 | BA | Boeing | 234.49 | HOLD (in position - riding the move) | breakout | 219.20 | 224.42 | 61.40 | -4.29 | 50.00 | 471.80 |
| 61 | AZZ | AZZ | 152.66 | HOLD (in position - riding the move) | anticipate | 137.22 | 139.79 | 70.40 | -10.11 | 61.50 | 443.20 |
| 62 | ATR | AptarGroup | 126.12 | HOLD (in position - riding the move) | breakout | 121.80 | 126.56 | 50.70 | 0.35 | 54.50 | 402.50 |
| 63 | RDDT | Reddit | 200.60 | HOLD (in position - riding the move) | breakout | 164.35 | 170.75 | 67.90 | -14.88 | 37.50 | 361.90 |
| 64 | MO | Altria Group | 71.89 | HOLD (in position - riding the move) | anticipate | 68.32 | 69.58 | 58.40 | -4.97 | 64.30 | 266.40 |
| 65 | YOU | CLEAR Secure | 56.73 | HOLD (in position - riding the move) | breakout | 45.39 | 52.28 | 57.30 | -7.85 | 22.20 | 174.70 |
| 66 | OI | O-I Glass | 10.04 | HOLD (in position - riding the move) | anticipate | 9.55 | 11.30 | 47.70 | -4.87 | 52.90 | 160.60 |
| 67 | AAA | Listed Funds Trust - AAF First Priority CLO Bond ETF | 25.10 | HOLD (in position - riding the move) | breakout | 24.71 | 24.76 | 79.50 | -1.37 | 60.00 | 154.10 |
| 68 | LINK | Interlink Electronics | 4.19 | HOLD (in position - riding the move) | anticipate | 3.67 | 4.08 | 61.60 | -12.46 | 45.00 | 54.30 |
| 69 | BAX | Baxter | 22.58 | HOLD (in position - riding the move) | breakout | 19.23 | 20.63 | 72.50 | -8.62 | 25.00 | 18.30 |
| 70 | MAN | ManpowerGroup | 38.44 | HOLD (in position - riding the move) | breakout | 31.83 | 33.32 | 66.30 | -13.32 | 27.80 | -6.60 |
| 71 | PATH | UiPath | 11.82 | HOLD (in position - riding the move) | reclaim | 11.25 | 11.71 | 53.50 | -4.83 | 27.30 | -22.00 |
| 72 | SMA | SmartStop Self Storage REIT | 32.80 | HOLD (in position - riding the move) | breakout | 31.78 | 31.96 | 58.30 | -2.56 | 12.50 | -40.60 |
| 73 | GRPN | Groupon | 26.57 | HOLD (in position - riding the move) | breakout | 17.73 | 17.91 | 80.30 | -32.58 | 29.40 | -55.30 |
| 74 | LB | L Brands | 74.99 | HOLD (in position - riding the move) | breakout | 68.34 | 69.25 | 56.40 | -7.66 | 37.50 | -58.90 |
| 75 | HOG | Harley-Davidson | 25.33 | HOLD (in position - riding the move) | breakout | 23.39 | 24.18 | 72.80 | -4.54 | 16.70 | -98.40 |
| 76 | GO | Grocery Outlet | 10.38 | HOLD (in position - riding the move) | breakout | 8.19 | 10.08 | 74.40 | -2.93 | 21.40 | -98.80 |

## SELL / EXIT  (18)

The strategy would be **exiting** (lost the band or hit the fakeout stop).

| group_rank | ticker | name | close | recommendation | mode | band_bot | band_top | rsi | need_move_% | bt_winrate_% | bt_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | IT | Gartner | 135.11 | SELL (lost the band) | anticipate | 151.80 | 194.84 | 40.70 | 0.00 | 60.00 | 371.50 |
| 2 | AB | AllianceBernstein | 36.68 | SELL (lost the band) | anticipate | 37.23 | 37.37 | 41.70 | 0.00 | 85.70 | 2,251.60 |
| 3 | DJT | Trump Media & Technology Group | 8.66 | SELL (lost the band) | anticipate | 8.77 | 10.35 | 47.20 | 0.00 | 46.70 | 784.60 |
| 4 | BMNR | Bitmine Immersion Technologies | 15.54 | SELL (lost the band) | anticipate | 18.63 | 22.92 | 38.30 | 0.00 | 25.00 | -125.80 |
| 5 | MCD | McDonald | 279.47 | SELL (lost the band) | anticipate | 286.46 | 294.04 | 33.70 | 0.00 | 69.20 | 657.20 |
| 6 | PEP | Pepsico | 143.29 | SELL (lost the band) | anticipate | 147.18 | 148.39 | 30.20 | 0.00 | 60.00 | 408.20 |
| 7 | UBER | Uber | 72.43 | SELL (lost the band) | anticipate | 73.77 | 77.10 | 51.00 | 0.00 | 46.70 | 684.50 |
| 8 | GLD | SSgA SPDR Gold Shares | 382.06 | SELL (lost the band) | anticipate | 406.41 | 420.04 | 31.20 | 0.00 | 61.50 | 870.50 |
| 9 | BSX | Boston Scientific | 44.60 | SELL (lost the band) | anticipate | 52.99 | 64.34 | 24.40 | 0.00 | 66.70 | 187.20 |
| 10 | QXO | QXO, Inc. | 15.80 | SELL (lost the band) | anticipate | 19.55 | 20.04 | 42.30 | 0.00 | 40.00 | -207.90 |
| 11 | T | AT&T | 20.58 | SELL (lost the band) | anticipate | 24.84 | 25.49 | 21.60 | 0.00 | 66.70 | 189.00 |
| 12 | ABT | Abbott Laboratories | 95.64 | SELL (lost the band) | anticipate | 95.70 | 104.39 | 41.50 | 0.00 | 81.80 | 1,424.20 |
| 13 | ICE | Intercontinental Exchange | 134.93 | SELL (lost the band) | anticipate | 147.22 | 150.33 | 24.10 | 0.00 | 78.60 | 707.50 |
| 14 | LMT | Lockheed Martin | 537.70 | SELL (lost the band) | anticipate | 544.61 | 566.14 | 32.90 | 0.00 | 72.70 | 525.00 |
| 15 | LOW | Lowe's Companies | 223.77 | SELL (lost the band) | anticipate | 227.05 | 235.69 | 46.20 | 0.00 | 80.00 | 1,392.90 |
| 16 | KR | Kroger | 58.24 | SELL (lost the band) | anticipate | 64.46 | 66.14 | 25.00 | 0.00 | 53.30 | 172.00 |
| 17 | JACK | Jack in the Box | 15.82 | SELL (fakeout stop hit) | breakout | 12.84 | 16.39 | 65.20 | 3.62 | 11.10 | -62.60 |
| 18 | SOLS | Solstice Advanced Materials | 68.05 | SELL (fakeout stop hit) | breakout | 72.79 | 78.82 | 41.30 | 15.83 | 0.00 | -0.00 |

## WATCH  (80)

Flat and still **far** from any entry trigger. Nothing to do yet.

| group_rank | ticker | name | close | readiness | pos_vs_band | mode | band_bot | band_top | rsi | need_move_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MSTR | MicroStrategy | 100.77 | 45.00 | below | anticipate | 139.20 | 172.08 | 45.20 | 0.00 |
| 2 | IREN | Iris Energy | 43.91 | 45.00 | below | anticipate | 47.63 | 48.68 | 54.70 | 0.00 |
| 3 | ONDS | Ondas Holdings | 7.82 | 45.00 | below | anticipate | 9.07 | 9.63 | 44.70 | 0.00 |
| 4 | CMG | Chipotle Mexican Grill | 33.99 | 45.00 | below | anticipate | 34.37 | 36.24 | 52.40 | 0.00 |
| 5 | MP | MP Materials | 53.00 | 45.00 | below | anticipate | 58.29 | 58.44 | 53.50 | 0.00 |
| 6 | LUNR | Intuitive Machines | 18.89 | 45.00 | below | anticipate | 23.82 | 27.22 | 44.90 | 0.00 |
| 7 | AVAV | AeroVironment | 176.84 | 45.00 | below | anticipate | 178.42 | 195.62 | 48.50 | 0.00 |
| 8 | HBM | Hudbay Minerals | 23.35 | 45.00 | below | anticipate | 23.85 | 24.85 | 53.20 | 0.00 |
| 9 | SA | Seabridge Gold | 27.40 | 45.00 | below | anticipate | 29.18 | 30.03 | 45.60 | 0.00 |
| 10 | PUMP | ProPetro | 12.28 | 45.00 | below | anticipate | 13.85 | 14.99 | 43.90 | 0.00 |
| 11 | POET | POET Technologies | 8.95 | 45.00 | below | anticipate | 9.68 | 10.69 | 54.20 | 0.00 |
| 12 | CI | Cigna | 281.98 | 44.60 | above | anticipate | 280.97 | 281.35 | 57.40 | -0.36 |
| 13 | GM | General Motors | 77.86 | 44.60 | inside | anticipate | 77.56 | 78.21 | 57.10 | -0.38 |
| 14 | IG | Principal Exchange-Traded Funds - Principal Investment Grade Corporate | 20.56 | 44.50 | above | anticipate | 20.46 | 20.53 | 53.90 | -0.49 |
| 15 | MLM | Martin Marietta | 605.28 | 44.40 | inside | anticipate | 601.40 | 611.36 | 51.70 | -0.64 |
| 16 | EA | Electronic Arts | 205.21 | 43.40 | above | anticipate | 201.86 | 201.91 | 57.10 | -1.63 |
| 17 | AVGO | Broadcom | 373.90 | 42.80 | above | anticipate | 365.52 | 367.25 | 59.20 | -2.24 |
| 18 | AMZN | Amazon | 244.16 | 42.60 | above | anticipate | 238.42 | 239.44 | 62.40 | -2.35 |
| 19 | LOT | Lotus Technology | 1.26 | 41.90 | above | anticipate | 1.22 | 1.26 | 55.00 | -3.11 |
| 20 | PR | Permian Resources | 18.19 | 40.90 | inside | anticipate | 17.43 | 18.92 | 37.90 | -4.15 |
| 21 | ED | Consolidated Edison | 111.94 | 40.70 | above | anticipate | 107.10 | 109.16 | 45.90 | -4.32 |
| 22 | MA | Mastercard | 533.20 | 40.30 | above | anticipate | 508.12 | 511.29 | 66.30 | -4.70 |
| 23 | ES | Eversource Energy | 73.23 | 40.10 | above | anticipate | 69.65 | 69.89 | 58.80 | -4.89 |
| 24 | AM | Antero Midstream | 22.08 | 39.80 | above | anticipate | 20.94 | 21.79 | 47.50 | -5.16 |
| 25 | RKLB | Rocket Lab USA | 93.09 | 39.60 | inside | anticipate | 88.07 | 93.16 | 57.10 | -5.39 |
| 26 | ST | Sensata Technologies | 46.12 | 39.10 | above | anticipate | 43.40 | 45.20 | 76.10 | -5.89 |
| 27 | TSLA | Tesla | 419.77 | 39.10 | above | anticipate | 395.04 | 397.51 | 60.30 | -5.89 |
| 28 | HR | Healthcare Realty | 20.40 | 39.10 | above | anticipate | 19.19 | 19.50 | 73.40 | -5.91 |
| 29 | DIS | Walt Disney | 97.42 | 38.80 | below | breakout | 100.38 | 103.45 | 51.90 | 6.19 |
| 30 | WEN | Wendy’s Company | 7.90 | 38.70 | above | anticipate | 7.40 | 7.77 | 58.60 | -6.30 |
| 31 | CL | Colgate-Palmolive | 93.39 | 38.60 | above | anticipate | 87.42 | 89.54 | 72.90 | -6.39 |
| 32 | KO | Coca-Cola | 82.96 | 38.00 | above | anticipate | 77.15 | 78.14 | 64.60 | -7.01 |
| 33 | WAY | Waystar | 23.91 | 37.80 | above | anticipate | 22.19 | 22.98 | 50.30 | -7.19 |
| 34 | UP | Wheels Up | 9.23 | 37.50 | inside | breakout | 8.05 | 9.92 | 47.10 | 7.50 |
| 35 | BR | Broadridge Financial Solutions | 144.79 | 37.30 | below | reclaim | 155.93 | 168.36 | 39.10 | 7.69 |
| 36 | SOFI | SoFi | 18.61 | 37.00 | inside | anticipate | 17.12 | 19.31 | 59.30 | -8.00 |
| 37 | WD | Walker & Dunlop | 52.67 | 36.40 | inside | breakout | 51.68 | 57.20 | 69.10 | 8.62 |
| 38 | MSFT | Microsoft | 386.74 | 35.70 | below | breakout | 398.73 | 422.62 | 53.40 | 9.28 |
| 39 | DE | Deere & Company | 635.71 | 35.60 | above | anticipate | 575.99 | 581.34 | 62.10 | -9.39 |
| 40 | ALK | Alaska Airlines | 50.40 | 35.20 | above | anticipate | 45.45 | 46.42 | 63.60 | -9.82 |
| 41 | SOUN | SoundHound AI | 6.96 | 35.00 | below | reclaim | 7.66 | 8.99 | 51.00 | 9.99 |
| 42 | KSS | Kohl's | 16.92 | 34.70 | above | anticipate | 15.18 | 15.99 | 62.90 | -10.28 |
| 43 | GS | Goldman Sachs | 1,055.06 | 33.50 | above | anticipate | 934.21 | 983.22 | 77.30 | -11.45 |
| 44 | APLD | Applied Blockchain | 33.50 | 33.10 | below | breakout | 33.93 | 37.50 | 58.30 | 11.93 |
| 45 | EW | Edwards Lifesciences | 95.17 | 32.80 | above | anticipate | 83.57 | 83.66 | 72.40 | -12.18 |
| 46 | AMC | AMC Entertainment | 1.74 | 32.20 | inside | breakout | 1.54 | 1.96 | 57.60 | 12.79 |
| 47 | PYPL | PayPal | 45.09 | 31.80 | below | breakout | 45.23 | 51.03 | 49.80 | 13.16 |
| 48 | BAC | Bank of America | 59.90 | 31.80 | above | anticipate | 52.01 | 52.31 | 74.70 | -13.17 |
| 49 | NBIS | Nebius Group | 213.02 | 31.50 | above | reclaim | 184.27 | 198.08 | 68.10 | -13.50 |
| 50 | EC | Ecopetrol | 14.48 | 31.50 | above | anticipate | 12.52 | 14.28 | 50.30 | -13.50 |
| 51 | DEI | Douglas Emmett | 12.57 | 30.70 | above | anticipate | 10.78 | 11.51 | 77.00 | -14.30 |
| 52 | NOW | ServiceNow | 107.91 | 30.60 | inside | breakout | 104.64 | 123.48 | 52.60 | 14.43 |
| 53 | NVO | Novo Nordisk | 49.26 | 30.20 | above | anticipate | 41.96 | 46.34 | 75.70 | -14.83 |
| 54 | MGM | MGM Resorts | 46.88 | 29.60 | above | anticipate | 39.67 | 40.51 | 70.60 | -15.38 |
| 55 | CMI | Cummins | 678.36 | 29.60 | above | anticipate | 573.67 | 654.20 | 68.30 | -15.43 |
| 56 | GL | Globe Life | 176.89 | 29.40 | above | anticipate | 149.20 | 154.54 | 83.70 | -15.65 |
| 57 | HAS | Hasbro | 77.98 | 28.40 | below | breakout | 85.09 | 90.93 | 32.30 | 16.61 |
| 58 | IBKR | Interactive Brokers | 95.99 | 27.40 | above | anticipate | 79.15 | 79.98 | 71.00 | -17.55 |
| 59 | CVS | CVS Health | 102.08 | 26.90 | above | anticipate | 83.66 | 91.08 | 76.30 | -18.05 |
| 60 | HPE | Hewlett Packard Enterprise | 43.13 | 26.90 | above | anticipate | 35.34 | 36.63 | 77.10 | -18.06 |
| 61 | LOVE | LoveSac | 18.04 | 26.70 | above | anticipate | 14.74 | 15.76 | 63.00 | -18.30 |
| 62 | FAS | Direxion Shares ETF Trust - Direxion Daily Financial Bull 3x Shares | 168.60 | 26.20 | above | anticipate | 136.94 | 142.81 | 78.90 | -18.78 |
| 63 | CRWV | CoreWeave | 86.46 | 25.40 | below | breakout | 97.56 | 103.36 | 51.60 | 19.55 |
| 64 | CME | CME Group | 234.76 | 25.30 | below | breakout | 269.46 | 281.11 | 29.90 | 19.74 |
| 65 | NFLX | Netflix | 76.02 | 24.60 | below | breakout | 88.79 | 91.50 | 23.20 | 20.36 |
| 66 | GLW | Corning | 194.77 | 24.50 | above | anticipate | 154.85 | 182.26 | 63.00 | -20.49 |
| 67 | AIR | AAR | 143.52 | 24.10 | above | anticipate | 113.54 | 121.68 | 68.40 | -20.89 |
| 68 | RIVN | Rivian | 20.14 | 23.60 | above | anticipate | 15.84 | 15.88 | 67.10 | -21.37 |
| 69 | CBOE | Cboe | 244.86 | 23.10 | below | breakout | 281.02 | 298.38 | 40.30 | 21.86 |
| 70 | SMCI | Supermicro | 27.19 | 21.60 | below | breakout | 31.27 | 33.56 | 53.60 | 23.44 |
| 71 | ADBE | Adobe | 218.07 | 18.90 | below | breakout | 239.15 | 274.89 | 42.10 | 26.06 |
| 72 | LULU | lululemon athletica | 115.64 | 17.20 | below | breakout | 138.77 | 147.73 | 31.70 | 27.75 |
| 73 | KLAC | KLA | 233.31 | 16.70 | above | anticipate | 167.26 | 188.20 | 71.60 | -28.31 |
| 74 | BE | Bloom Energy | 295.18 | 16.60 | above | anticipate | 211.30 | 233.69 | 67.50 | -28.42 |
| 75 | IQ | iQIYI | 1.07 | 15.30 | below | breakout | 1.15 | 1.39 | 34.10 | 29.74 |
| 76 | UI | Ubiquiti | 539.44 | 10.40 | below | breakout | 660.01 | 726.18 | 32.50 | 34.62 |
| 77 | INTC | Intel | 122.20 | 6.30 | above | anticipate | 74.86 | 104.02 | 70.80 | -38.74 |
| 78 | INTU | Intuit | 272.14 | 5.00 | below | breakout | 381.27 | 443.66 | 23.90 | 63.03 |
| 79 | SQQQ | ProShares Trust - ProShares UltraPro Short QQQ | 38.28 | 5.00 | below | breakout | 46.63 | 62.87 | 17.90 | 64.24 |
| 80 | SOXS | Direxion Shares ETF Trust - Direxion Daily Semiconductor Bear 3X Share | 4.16 | 5.00 | below | breakout | 10.90 | 35.22 | 5.30 | 745.59 |

## SKIPPED  (5)

Not enough clean price history to run the strategy.

SPCX (insufficient price history), OG (insufficient price history), DS (insufficient price history), RE (insufficient price history), DAY (insufficient price history)
