# Dip-and-Ride Swing Screen

_Generated 2026-07-09 19:07 | latest daily bar: **2026-07-09** | universe: 199 names (most popular US stocks + ETFs, plus WSB)_

> **Research only, not financial advice.** Buy dips, cut losers small with an initial stop, and RIDE winners with a trailing stop - small losses, big wins.

## The model in one paragraph

Buy a **dip** - RSI-2 oversold and/or price stretched **>= 1.5 std-devs below the 20/21 band** (`z_band`). **Cut it small** if wrong (initial stop). If it works, there is **no 1-2% take-profit** - a **trailing stop rides the trend** so the average win is large (often +15-50%) and the occasional monster runs. Because we ride, win rate is lower, so BUY signals are gated by **profit factor** (a proven money-maker), not win rate. SELL only shows when a real position exits (stop = small loss; trail = locked-in ride).

## $100 portfolio backtest

Giving the strategy **$100** across this universe (max 8 positions, 6% initial stop, ride=chandelier): **$238.85** (+139%, CAGR 20.5%/yr, max drawdown -33.8%, 398 trades, 37.2% win rate, avg win +17.7%).

## Summary

| Group | Count |
| --- | --- |
| BUY NOW | 3 |
| SELL / EXIT | 8 |
| HOLDING (RIDE) | 146 |
| CLOSE TO BUY | 3 |
| WATCH | 35 |
| SKIPPED | 4 |

## BUY NOW  (3)

**High-conviction dip buys firing today.** Oversold (RSI-2) and/or stretched >= 1.5 sigma below the 20/21 band, in names whose dip-and-ride history is a **proven money-maker (profit factor gate)** with a **big average win**. Buy at next open; cut small if wrong; ride the trend if right.

| group_rank | ticker | name | close | score | rsi2 | z_band | bt_profit_factor | bt_avg_win_% | bt_winrate_% | bt_max_win_% | exit_plan | band_read | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AZZ | AZZ | 137.49 | 64.40 | 4.20 | -2.08 | 2.05 | 10.20 | 55.60 | 37.10 | cut at 6%, then ride (trail 3xATR) | -2.1 sigma below band - stretched, buy zone | dip buy (PF 2.0, avg win +10%): RSI-2 4 (oversold), -2.1 sigma below band -> cut at 6%, then ride (trail 3xATR) |
| 2 | LUNR | Intuitive Machines | 16.92 | 46.50 | 2.10 | -1.37 | 1.61 | 29.10 | 34.00 | 109.40 | cut at 6%, then ride (trail 3xATR) | -1.4 sigma below band - pulling back toward band | dip buy (PF 1.6, avg win +29%): RSI-2 2 (oversold) -> cut at 6%, then ride (trail 3xATR) |
| 3 | COST | COST | 913.29 | 54.50 | 9.90 | -2.16 | 1.58 | 10.80 | 38.70 | 35.30 | cut at 6%, then ride (trail 3xATR) | -2.2 sigma below band - stretched, buy zone | dip buy (PF 1.6, avg win +11%): RSI-2 10 (oversold), -2.2 sigma below band -> cut at 6%, then ride (trail 3xATR) |

## SELL / EXIT  (8)

**A model position just exited on the latest bar.** Either the **stop hit** (loser cut small - re-enter on the next dip) or the **trailing stop hit** (trend broke - lock in the ride, usually a win).

| group_rank | ticker | name | close | entry_price | pos_ret_% | exit_reason | z_band | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | KORU | Direxion Shares ETF Trust - Direxion Daily South Korea Bull 3X Shares | 567.51 | 625.63 | -23.08 | stop | -1.01 | SELL: 6% stop hit (-23.1%) - loser cut; re-enter on the next dip |
| 2 | MU | MU | 1,007.92 | 1,007.00 | -10.36 | stop | -0.26 | SELL: 6% stop hit (-10.4%) - loser cut; re-enter on the next dip |
| 3 | RMBS | Rambus | 115.58 | 115.81 | -9.55 | stop | -0.85 | SELL: 6% stop hit (-9.6%) - loser cut; re-enter on the next dip |
| 4 | WDC | Western Digital | 581.58 | 567.00 | -7.23 | stop | -0.31 | SELL: 6% stop hit (-7.2%) - loser cut; re-enter on the next dip |
| 5 | MP | MP Materials | 51.94 | 53.55 | -5.70 | trail | -1.32 | SELL: trailing stop hit (-5.7%) - trend broke, lock in the ride |
| 6 | WD | Walker & Dunlop | 50.34 | 47.78 | 3.67 | trail | -1.18 | SELL: trailing stop hit (+3.7%) - trend broke, lock in the ride |
| 7 | CAT | CAT | 942.48 | 663.96 | 41.20 | trail | -0.46 | SELL: trailing stop hit (+41.2%) - trend broke, lock in the ride |
| 8 | SNDK | Sandisk | 1,900.73 | 588.01 | 170.71 | trail | -0.11 | SELL: trailing stop hit (+170.7%) - trend broke, lock in the ride |

## HOLDING (RIDE)  (146)

**Entered on a prior dip and still riding the trend.** No fixed take-profit - it runs until the trailing stop; the initial stop protected the downside.

| group_rank | ticker | name | close | entry_price | pos_gain_% | bars_held | z_band | exit_plan | stop_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AMD | AMD | 545.56 | 197.13 | 176.75 | 104.00 | 0.82 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 2 | ASML | ASML | 1,810.98 | 1,281.99 | 41.26 | 84.00 | -0.08 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 3 | GO | Grocery Outlet | 10.27 | 7.32 | 40.37 | 35.00 | 1.41 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 4 | LLY | LLY | 1,212.20 | 870.40 | 39.27 | 49.00 | 1.00 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 5 | RDDT | Reddit | 198.64 | 143.49 | 38.43 | 30.00 | 1.32 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 6 | TSM | TSMC | 438.80 | 324.07 | 35.40 | 70.00 | -0.02 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 7 | BB | BlackBerry | 11.39 | 8.42 | 35.21 | 12.00 | 0.69 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 8 | BULL | Webull | 7.26 | 5.41 | 34.16 | 19.00 | 1.22 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 9 | DAL | Delta Air Lines | 88.62 | 66.52 | 33.22 | 48.00 | 0.24 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 10 | GE | GE | 359.79 | 283.04 | 27.12 | 35.00 | 0.16 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 11 | ABBV | ABBV | 248.40 | 198.93 | 24.87 | 51.00 | 0.56 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 12 | HOOD | HOOD | 115.62 | 93.21 | 24.04 | 8.00 | 1.44 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 13 | RIVN | RIVN | 18.10 | 14.64 | 23.67 | 9.00 | 1.08 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 14 | DELL | Dell | 452.71 | 368.68 | 22.79 | 18.00 | 2.30 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 15 | SOXL | Direxion Shares ETF Trust - Direxion Daily Semiconductor Bull 3X Share | 195.12 | 159.21 | 22.55 | 1.00 | -0.66 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 16 | ALL | Allstate | 249.29 | 207.40 | 20.20 | 27.00 | 1.18 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 17 | LOVE | LoveSac | 16.99 | 14.20 | 19.65 | 13.00 | 0.53 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 18 | OPEN | Opendoor | 5.21 | 4.36 | 19.50 | 20.00 | 1.95 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 19 | FOR | Forestar Group | 30.23 | 25.38 | 19.09 | 33.00 | 0.22 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 20 | GL | Globe Life | 178.84 | 150.48 | 18.84 | 33.00 | 1.02 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 21 | SCHW | SCHW | 102.18 | 86.00 | 18.82 | 27.00 | 1.74 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 22 | CMG | CMG | 34.31 | 29.10 | 17.89 | 23.00 | 0.97 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 23 | DHR | DHR | 194.43 | 165.95 | 17.16 | 38.00 | 0.92 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 24 | CIA | Citizens Inc | 5.58 | 4.77 | 16.98 | 32.00 | -0.66 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 25 | BAC | BAC | 59.31 | 50.86 | 16.60 | 39.00 | 1.32 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 26 | NOW | NOW | 108.54 | 93.30 | 16.33 | 12.00 | 1.00 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 27 | BABA | Alibaba | 111.51 | 96.14 | 15.99 | 7.00 | 0.92 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 28 | MRK | MRK | 124.86 | 107.77 | 15.85 | 48.00 | 0.38 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 29 | WULF | TeraWulf | 24.36 | 21.06 | 15.67 | 1.00 | -0.23 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 30 | JNJ | JNJ | 258.73 | 224.89 | 15.05 | 53.00 | 0.88 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 31 | WFC | WFC | 87.01 | 75.67 | 14.99 | 40.00 | 1.68 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 32 | C | C | 139.60 | 121.45 | 14.94 | 34.00 | -0.26 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 33 | NBIS | Nebius Group | 220.59 | 192.67 | 14.49 | 1.00 | -0.67 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 34 | LITE | Lumentum | 800.40 | 699.42 | 14.44 | 2.00 | -0.35 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 35 | MARA | MARA | 13.41 | 11.73 | 14.36 | 1.00 | -0.14 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 36 | XLV | XLV | 161.67 | 141.64 | 14.14 | 48.00 | 0.96 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 37 | AMC | AMC Entertainment | 1.91 | 1.68 | 13.99 | 1.00 | -0.45 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 38 | AXP | AXP | 346.32 | 304.94 | 13.57 | 23.00 | 0.79 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 39 | UPS | UPS | 110.49 | 97.29 | 13.56 | 43.00 | 1.00 | cut at 6%, then ride (trail 3xATR) | 6.00 |
| 40 | DIA | DIA | 524.00 | 461.59 | 13.52 | 74.00 | 0.71 | cut at 6%, then ride (trail 3xATR) | 6.00 |


_...and 106 more._

## CLOSE TO BUY  (3)

A dip fired with a **thinner/unproven** edge, or price is sliding into the buy zone. Watch for a high-conviction trigger.

| group_rank | ticker | name | close | score | rsi2 | z_band | dist_band_% | vol_surge | bt_profit_factor | bt_avg_win_% | band_read | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LEVI | Levi Strauss | 24.02 | 58.60 | 7.70 | 0.02 | 0.04 | 2.12 | 1.29 | 10.50 | at the band | dip fired (PF 1.3): RSI-2 8 (oversold), vol 2.1x -> cut at 6%, then ride (trail 3xATR) |
| 2 | LOW | LOW | 213.43 | 56.10 | 16.00 | -1.52 | -2.82 | 0.30 | 1.15 | 8.50 | -1.5 sigma below band - stretched, buy zone | dip fired (PF 1.1): -1.5 sigma below band -> cut at 6%, then ride (trail 3xATR) |
| 3 | PEP | PEP | 137.31 | 45.10 | 10.80 | -1.73 | -3.54 | 1.15 | 1.15 | 5.30 | -1.7 sigma below band - stretched, buy zone | dip fired (PF 1.1): -1.7 sigma below band -> cut at 6%, then ride (trail 3xATR) |

## WATCH  (35)

No dip. Nothing to do.

| group_rank | ticker | name | close | score | rsi2 | z_band | above_50 | mom_63_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RXT | Rackspace Technology | 4.39 | 65.50 | 7.10 | -2.32 | False | 352.20 |
| 2 | PENG | Penguin Solutions | 83.54 | 42.30 | 87.70 | 2.65 | True | 277.60 |
| 3 | CC | Chemours | 17.45 | 39.70 | 11.20 | -2.00 | False | -18.30 |
| 4 | ARKK | ARKK | 81.61 | 36.60 | 61.00 | 0.89 | True | 16.00 |
| 5 | PANW | PANW | 337.43 | 36.60 | 58.00 | 0.96 | True | 94.20 |
| 6 | TGT | TGT | 133.06 | 36.60 | 84.50 | 0.31 | True | 9.10 |
| 7 | TXN | TXN | 309.58 | 36.60 | 82.10 | 0.68 | True | 48.90 |
| 8 | DJT | Trump Media & Technology Group | 8.52 | 36.60 | 67.40 | 0.95 | True | -10.90 |
| 9 | NIO | NIO | 4.80 | 33.70 | 21.20 | -1.59 | False | -24.80 |
| 10 | AAPL | AAPL | 314.78 | 32.70 | 89.00 | 1.51 | True | 21.70 |
| 11 | VTI | VTI | 371.34 | 32.70 | 73.80 | 1.10 | True | 11.60 |
| 12 | SLS | Sellas Life Sciences | 14.47 | 32.70 | 76.70 | 1.04 | True | 197.70 |
| 13 | RBLX | RBLX | 56.22 | 32.70 | 58.70 | 1.02 | True | 1.40 |
| 14 | IBKR | Interactive Brokers | 95.64 | 32.70 | 73.20 | 1.13 | True | 32.30 |
| 15 | GRPN | Groupon | 26.40 | 32.70 | 63.00 | 1.12 | True | 120.50 |
| 16 | SOFI | SOFI | 18.53 | 32.70 | 78.20 | 1.29 | True | 12.40 |
| 17 | UNH | UNH | 430.83 | 32.70 | 77.20 | 1.64 | True | 41.60 |
| 18 | SHOP | SHOP | 122.61 | 32.70 | 73.60 | 1.47 | True | 2.10 |
| 19 | META | META | 617.51 | 32.70 | 73.00 | 1.47 | True | 0.90 |
| 20 | IBM | IBM | 294.64 | 32.20 | 26.60 | 1.01 | True | 22.80 |
| 21 | XLK | XLK | 185.68 | 31.20 | 78.80 | 0.32 | True | 31.20 |
| 22 | DKNG | DKNG | 26.55 | 30.10 | 37.30 | 0.12 | True | 10.90 |
| 23 | CMCSA | CMCSA | 23.16 | 29.50 | 11.20 | -0.23 | False | -16.10 |
| 24 | BE | Bloom Energy | 259.85 | 28.30 | 36.70 | -0.75 | False | 77.00 |
| 25 | HPE | Hewlett Packard Enterprise | 49.08 | 27.30 | 96.00 | 1.43 | True | 97.00 |
| 26 | IQ | iQIYI | 1.12 | 27.30 | 83.50 | 2.52 | True | -15.40 |
| 27 | ARM | ARM | 331.71 | 25.80 | 81.10 | -0.37 | True | 122.80 |
| 28 | GOOG | GOOG | 354.21 | 24.10 | 15.80 | -0.27 | False | 12.60 |
| 29 | GOOGL | GOOGL | 357.20 | 24.10 | 14.60 | -0.20 | False | 12.60 |
| 30 | TMUS | TMUS | 180.78 | 24.00 | 48.90 | -0.07 | False | -8.00 |
| 31 | LULU | LULU | 116.00 | 24.00 | 67.60 | 0.09 | False | -27.00 |
| 32 | EU | enCore Energy | 1.33 | 23.80 | 71.50 | -0.54 | False | -26.90 |
| 33 | PLTR | PLTR | 128.72 | 23.50 | 23.70 | 0.28 | False | -8.60 |
| 34 | NFLX | NFLX | 74.85 | 18.10 | 21.60 | -0.46 | False | -24.70 |
| 35 | USO | United States Commodity Funds LLC - United States Oil Fund | 108.61 | 17.30 | 43.70 | -0.54 | False | -12.80 |

## SKIPPED  (4)

SPCX, OS, DAY, PS
