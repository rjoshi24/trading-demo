# Dip-Buy Swing Screen

_Generated 2026-07-09 18:23 | latest daily bar: **2026-07-09** | universe: 200 names (most popular US stocks + ETFs, plus WSB)_

> **Research only, not financial advice.** Buy high-conviction dips (oversold / stretched below the band); cut fast with a hard stop if wrong; ride winners to an adaptive z-target.

## The model in one paragraph

Buy a **dip** - RSI-2 oversold and/or price stretched **>= 1.5 std-devs below the 20/21 band** (`z_band`) - only in names with a **proven historical win rate** (conviction). Exit is regime-adaptive: **ride momentum** in strong names (to `z>=+1.5`), take the quick bounce in weak ones (`z>=0`), and a **hard stop** cuts a bad buy fast (you can re-enter). SELL only shows when a position actually exits.

## $100 portfolio backtest

Giving the strategy **$100** across this universe (max 8 positions, 5% stop): **$219.95** (+120%, CAGR 18.2%/yr, max drawdown -36.9%, 1104 trades, 55.3% win rate).

## Summary

| Group | Count |
| --- | --- |
| BUY NOW | 2 |
| SELL / EXIT | 22 |
| HOLDING (RIDE) | 67 |
| CLOSE TO BUY | 9 |
| WATCH | 96 |
| SKIPPED | 4 |

## BUY NOW  (2)

**High-conviction dip buys firing today.** Oversold (RSI-2) and/or stretched >= 1.5 sigma below the 20/21 band, and this name has a **proven historical win rate**. Buy at next open; ride to the z-target; hard stop cuts it if wrong.

| group_rank | ticker | name | close | score | rsi2 | z_band | dist_band_% | vol_surge | bt_winrate_% | exit_plan | stop_% | band_read | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AZZ | AZZ | 139.90 | 56.00 | 5.70 | -1.78 | -7.07 | 1.20 | 69.40 | z>=+0.5 | 5.00 | -1.8 sigma below band - stretched, buy zone | dip buy (69% hist win): RSI-2 6 (oversold), -1.8 sigma below band -> exit z>=+0.5, 5% stop |
| 2 | CMCSA | CMCSA | 23.12 | 37.00 | 9.90 | -0.27 | -0.80 | 0.27 | 62.50 | z>=0 (quick bounce) | 5.00 | at the band | dip buy (62% hist win): RSI-2 10 (oversold) -> exit z>=0 (quick bounce), 5% stop |

## SELL / EXIT  (22)

**A model position just exited on the latest bar** - this is the only time SELL matters. Either the **stop hit** (the buy was wrong - cut it, you can re-enter on the next dip) or the **z-target was reached** (mean-reversion thesis complete - take profit).

| group_rank | ticker | name | close | entry_price | pos_ret_% | exit_reason | z_band | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | KORU | Direxion Shares ETF Trust - Direxion Daily South Korea Bull 3X Shares | 573.35 | 625.63 | -23.08 | stop | -0.98 | SELL: 5% stop hit (-23.1%) - buy was wrong, cut it; re-enter on the next dip |
| 2 | MU | MU | 1,018.22 | 1,007.00 | -10.36 | stop | -0.16 | SELL: 5% stop hit (-10.4%) - buy was wrong, cut it; re-enter on the next dip |
| 3 | RMBS | Rambus | 116.94 | 115.81 | -9.55 | stop | -0.75 | SELL: 5% stop hit (-9.6%) - buy was wrong, cut it; re-enter on the next dip |
| 4 | SMCI | SMCI | 28.76 | 28.42 | -8.02 | stop | -0.64 | SELL: 5% stop hit (-8.0%) - buy was wrong, cut it; re-enter on the next dip |
| 5 | WDC | Western Digital | 586.83 | 567.00 | -7.23 | stop | -0.24 | SELL: 5% stop hit (-7.2%) - buy was wrong, cut it; re-enter on the next dip |
| 6 | WD | Walker & Dunlop | 50.62 | 52.85 | -6.28 | stop | -1.03 | SELL: 5% stop hit (-6.3%) - buy was wrong, cut it; re-enter on the next dip |
| 7 | MP | MP Materials | 52.15 | 53.55 | -5.70 | stop | -1.26 | SELL: 5% stop hit (-5.7%) - buy was wrong, cut it; re-enter on the next dip |
| 8 | CSCO | CSCO | 118.60 | 118.16 | -5.48 | stop | 0.56 | SELL: 5% stop hit (-5.5%) - buy was wrong, cut it; re-enter on the next dip |
| 9 | OR | Osisko Gold Royalties | 29.86 | 30.83 | -3.30 | stop | -1.17 | SELL: 5% stop hit (-3.3%) - buy was wrong, cut it; re-enter on the next dip |
| 10 | AGI | Alamos Gold | 29.79 | 30.81 | -3.28 | stop | -0.98 | SELL: 5% stop hit (-3.3%) - buy was wrong, cut it; re-enter on the next dip |
| 11 | ET | Energy Transfer Partners | 19.80 | 19.50 | 2.31 | z-target | 1.68 | SELL: target reached (+2.3%) - mean-reversion thesis complete, take profit |
| 12 | AM | Antero Midstream | 22.66 | 22.29 | 2.65 | z-target | 0.79 | SELL: target reached (+2.6%) - mean-reversion thesis complete, take profit |
| 13 | XOM | XOM | 138.01 | 139.46 | 2.85 | z-target | -0.56 | SELL: target reached (+2.9%) - mean-reversion thesis complete, take profit |
| 14 | XLE | XLE | 55.03 | 53.53 | 3.27 | z-target | 0.27 | SELL: target reached (+3.3%) - mean-reversion thesis complete, take profit |
| 15 | COP | COP | 108.51 | 104.12 | 5.67 | z-target | -0.14 | SELL: target reached (+5.7%) - mean-reversion thesis complete, take profit |
| 16 | CVX | CVX | 174.42 | 164.78 | 5.98 | z-target | -0.10 | SELL: target reached (+6.0%) - mean-reversion thesis complete, take profit |
| 17 | AVGO | AVGO | 404.73 | 373.62 | 7.67 | z-target | 1.63 | SELL: target reached (+7.7%) - mean-reversion thesis complete, take profit |
| 18 | INTU | INTU | 272.04 | 258.12 | 8.16 | z-target | -0.34 | SELL: target reached (+8.2%) - mean-reversion thesis complete, take profit |
| 19 | OXY | OXY | 52.54 | 48.38 | 9.28 | z-target | 0.17 | SELL: target reached (+9.3%) - mean-reversion thesis complete, take profit |
| 20 | IT | Gartner | 131.57 | 126.00 | 10.07 | z-target | -0.70 | SELL: target reached (+10.1%) - mean-reversion thesis complete, take profit |
| 21 | BABA | Alibaba | 111.96 | 96.14 | 13.50 | z-target | 0.97 | SELL: target reached (+13.5%) - mean-reversion thesis complete, take profit |
| 22 | SOXS | Direxion Shares ETF Trust - Direxion Daily Semiconductor Bear 3X Share | 3.92 | 3.59 | 38.72 | z-target | -0.76 | SELL: target reached (+38.7%) - mean-reversion thesis complete, take profit |

## HOLDING (RIDE)  (67)

**Entered on a prior dip and still riding** toward the target. If it's a strong name it rides to z>=+1.5 (momentum); the stop still protects it.

| group_rank | ticker | name | close | entry_price | pos_gain_% | bars_held | z_band | exit_plan | stop_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SOXL | Direxion Shares ETF Trust - Direxion Daily Semiconductor Bull 3X Share | 197.39 | 159.21 | 23.98 | 1.00 | -0.60 | z>=+0.5 | 5.00 |
| 2 | SNDK | Sandisk | 1,942.97 | 1,591.80 | 22.06 | 1.00 | 0.08 | z>=+1.5 (ride momentum) | 5.00 |
| 3 | MSTR | MSTR | 95.67 | 83.23 | 14.94 | 8.00 | -0.67 | z>=0 (quick bounce) | 5.00 |
| 4 | NBIS | Nebius Group | 220.64 | 192.67 | 14.52 | 1.00 | -0.67 | z>=+1.5 (ride momentum) | 5.00 |
| 5 | WULF | TeraWulf | 23.83 | 21.06 | 13.15 | 1.00 | -0.41 | z>=+0.5 | 5.00 |
| 6 | AMC | AMC Entertainment | 1.93 | 1.71 | 12.67 | 2.00 | -0.42 | z>=+1.5 (ride momentum) | 5.00 |
| 7 | DKNG | DKNG | 26.51 | 23.70 | 11.86 | 8.00 | 0.10 | z>=+1.5 (ride momentum) | 5.00 |
| 8 | ON | ON Semiconductor | 100.46 | 90.20 | 11.37 | 7.00 | -0.38 | z>=+0.5 | 5.00 |
| 9 | CRWV | CoreWeave | 91.18 | 83.01 | 9.84 | 3.00 | -0.61 | z>=+0.5 | 5.00 |
| 10 | AMAT | AMAT | 595.20 | 547.10 | 8.79 | 1.00 | 0.01 | z>=+1.5 (ride momentum) | 5.00 |
| 11 | WTI | W&T Offshore | 3.46 | 3.21 | 7.79 | 14.00 | 0.16 | z>=+0.5 | 5.00 |
| 12 | IBKR | Interactive Brokers | 96.00 | 90.34 | 6.26 | 7.00 | 1.23 | z>=+1.5 (ride momentum) | 5.00 |
| 13 | NOK | Nokia | 12.75 | 12.00 | 6.25 | 2.00 | -0.64 | z>=+0.5 | 5.00 |
| 14 | AG | First Majestic Silver | 17.34 | 16.35 | 6.06 | 0.00 | 0.01 | z>=0 (quick bounce) | 5.00 |
| 15 | AAOI | Applied Optoelectronics | 124.61 | 118.15 | 5.47 | 2.00 | -0.98 | z>=0 (quick bounce) | 5.00 |
| 16 | MARA | MARA | 13.32 | 12.63 | 5.46 | 3.00 | -0.24 | z>=+1.5 (ride momentum) | 5.00 |
| 17 | QCOM | QCOM | 191.50 | 182.17 | 5.12 | 4.00 | -0.43 | z>=+0.5 | 5.00 |
| 18 | NVDA | NVDA | 202.94 | 193.12 | 5.08 | 8.00 | 0.20 | z>=+0.5 | 5.00 |
| 19 | FCX | FCX | 60.77 | 57.92 | 4.92 | 1.00 | -0.66 | z>=0 (quick bounce) | 5.00 |
| 20 | IREN | Iris Energy | 42.61 | 40.74 | 4.59 | 1.00 | -0.93 | z>=+0.5 | 5.00 |
| 21 | PUMP | ProPetro | 12.84 | 12.30 | 4.39 | 2.00 | -1.13 | z>=0 (quick bounce) | 5.00 |
| 22 | MS | MS | 223.28 | 214.33 | 4.18 | 7.00 | 1.04 | z>=+1.5 (ride momentum) | 5.00 |
| 23 | ONDS | Ondas Holdings | 7.82 | 7.51 | 4.13 | 8.00 | -0.77 | z>=0 (quick bounce) | 5.00 |
| 24 | INTC | INTC | 112.43 | 108.30 | 3.82 | 1.00 | -1.03 | z>=+0.5 | 5.00 |
| 25 | RKLB | Rocket Lab USA | 83.86 | 81.11 | 3.40 | 8.00 | -1.29 | z>=+0.5 | 5.00 |
| 26 | JUST | Goldman Sachs ETF Trust - Goldman Sachs Just Us Large Cap Equity ETF | 107.26 | 104.01 | 3.13 | 18.00 | 1.08 | z>=+1.5 (ride momentum) | 5.00 |
| 27 | OKLO | Oklo | 49.28 | 47.85 | 2.99 | 0.00 | -1.19 | z>=0 (quick bounce) | 5.00 |
| 28 | SLV | SLV | 54.36 | 52.87 | 2.82 | 8.00 | -0.63 | z>=0 (quick bounce) | 5.00 |
| 29 | UUUU | Energy Fuels | 13.56 | 13.20 | 2.69 | 0.00 | -1.18 | z>=0 (quick bounce) | 5.00 |
| 30 | HR | Healthcare Realty | 20.86 | 20.32 | 2.65 | 13.00 | 1.83 | z>=+1.5 (ride momentum) | 5.00 |
| 31 | TGT | TGT | 133.77 | 130.74 | 2.32 | 4.00 | 0.47 | z>=+1.5 (ride momentum) | 5.00 |
| 32 | UP | Wheels Up | 8.06 | 7.90 | 2.09 | 0.00 | 0.05 | z>=+0.5 | 5.00 |
| 33 | NEM | NEM | 94.89 | 93.24 | 1.76 | 10.00 | -0.67 | z>=0 (quick bounce) | 5.00 |
| 34 | GLD | GLD | 378.40 | 372.27 | 1.65 | 8.00 | -0.27 | z>=0 (quick bounce) | 5.00 |
| 35 | VTI | VTI | 371.59 | 365.64 | 1.63 | 21.00 | 1.16 | z>=+1.5 (ride momentum) | 5.00 |
| 36 | SPY | SPY | 751.44 | 741.45 | 1.35 | 21.00 | 1.12 | z>=+1.5 (ride momentum) | 5.00 |
| 37 | VOO | Vanguard S&P 500 ETF | 690.71 | 681.49 | 1.35 | 21.00 | 1.12 | z>=+1.5 (ride momentum) | 5.00 |
| 38 | APLD | Applied Blockchain | 32.60 | 32.23 | 1.15 | 2.00 | -1.14 | z>=+0.5 | 5.00 |
| 39 | T | T | 20.93 | 20.70 | 1.14 | 4.00 | -1.02 | z>=0 (quick bounce) | 5.00 |
| 40 | QQQ | QQQ | 723.34 | 717.02 | 0.88 | 21.00 | 0.27 | z>=+1.5 (ride momentum) | 5.00 |


_...and 27 more._

## CLOSE TO BUY  (9)

A dip fired with a **moderate/unproven** edge, or price is sliding into the buy zone. Watch for a high-conviction trigger.

| group_rank | ticker | name | close | score | rsi2 | z_band | dist_band_% | vol_surge | bt_winrate_% | band_read | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RTX | RTX | 195.10 | 47.10 | 25.00 | 0.87 | 2.90 | 0.28 | 78.80 | +0.9 sigma above band - riding above support | RSI-2 25 sliding into oversold -- waiting for the dip trigger |
| 2 | V | V | 346.89 | 42.10 | 17.50 | 0.69 | 2.53 | 0.37 | 69.60 | +0.7 sigma above band - riding above support | RSI-2 18 sliding into oversold -- waiting for the dip trigger |
| 3 | PG | PG | 146.64 | 41.10 | 21.20 | -1.29 | -1.61 | 0.26 | 68.80 | -1.3 sigma below band - pulling back toward band | RSI-2 21 sliding into oversold; -1.3 sigma below band -- waiting for the dip trigger |
| 4 | ABBV | ABBV | 249.05 | 42.10 | 11.20 | 0.60 | 3.54 | 0.26 | 68.30 | +0.6 sigma above band - riding above support | RSI-2 11 sliding into oversold -- waiting for the dip trigger |
| 5 | DE | DE | 597.98 | 41.70 | 21.60 | -0.11 | -0.44 | 0.27 | 67.30 | at the band | RSI-2 22 sliding into oversold -- waiting for the dip trigger |
| 6 | MA | MA | 520.42 | 47.10 | 22.90 | 0.77 | 2.63 | 0.24 | 65.40 | +0.8 sigma above band - riding above support | RSI-2 23 sliding into oversold -- waiting for the dip trigger |
| 7 | AMGN | AMGN | 363.19 | 42.10 | 18.10 | 0.71 | 2.05 | 0.22 | 65.40 | +0.7 sigma above band - riding above support | RSI-2 18 sliding into oversold -- waiting for the dip trigger |
| 8 | ABT | ABT | 94.12 | 42.10 | 19.10 | 0.81 | 2.39 | 0.20 | 63.80 | +0.8 sigma above band - riding above support | RSI-2 19 sliding into oversold -- waiting for the dip trigger |
| 9 | LEVI | Levi Strauss | 24.20 | 48.90 | 11.20 | 0.34 | 0.71 | 1.94 | 53.40 | at the band | RSI-2 11 sliding into oversold -- waiting for the dip trigger |

## WATCH  (96)

No dip. Nothing to do.

| group_rank | ticker | name | close | score | rsi2 | z_band | above_50 | mom_63_% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | RXT | Rackspace Technology | 4.53 | 63.30 | 7.50 | -2.20 | False | 366.60 |
| 2 | PENG | Penguin Solutions | 86.99 | 42.30 | 89.90 | 2.92 | True | 293.20 |
| 3 | LOVE | LoveSac | 16.92 | 41.10 | 31.20 | 0.47 | True | 8.90 |
| 4 | DIA | DIA | 524.52 | 41.10 | 42.60 | 0.78 | True | 9.90 |
| 5 | PEP | PEP | 138.51 | 39.90 | 12.90 | -1.38 | False | -10.50 |
| 6 | DTE | DTE Energy | 149.43 | 36.70 | 19.10 | -0.07 | True | 1.20 |
| 7 | AMD | AMD | 545.63 | 36.60 | 74.30 | 0.82 | True | 135.40 |
| 8 | TXN | TXN | 311.13 | 36.60 | 83.60 | 0.79 | True | 49.70 |
| 9 | DHR | DHR | 194.75 | 36.60 | 66.20 | 0.96 | True | -0.50 |
| 10 | UPS | UPS | 110.36 | 36.60 | 48.60 | 0.95 | True | 11.70 |
| 11 | UBER | UBER | 74.10 | 36.60 | 62.40 | 0.67 | True | 2.40 |
| 12 | PANW | PANW | 335.50 | 36.60 | 55.30 | 0.90 | True | 93.10 |
| 13 | C | C | 139.57 | 36.60 | 51.50 | -0.26 | True | 13.60 |
| 14 | AXP | AXP | 346.54 | 36.60 | 57.70 | 0.81 | True | 9.80 |
| 15 | ASML | ASML | 1,822.42 | 36.60 | 71.90 | 0.07 | True | 28.50 |
| 16 | BB | BlackBerry | 11.44 | 36.60 | 67.50 | 0.72 | True | 223.90 |
| 17 | AIR | AAR | 138.24 | 36.60 | 60.20 | 0.59 | True | 14.50 |
| 18 | ARKK | ARKK | 81.78 | 36.60 | 63.00 | 0.94 | True | 16.20 |
| 19 | RBLX | RBLX | 55.78 | 36.60 | 49.90 | 0.94 | True | 0.60 |
| 20 | ABNB | ABNB | 146.43 | 36.60 | 56.10 | 0.72 | True | 11.40 |
| 21 | YOU | CLEAR Secure | 56.27 | 36.60 | 68.30 | 0.99 | True | 11.90 |
| 22 | TSM | TSMC | 438.68 | 36.60 | 50.50 | -0.02 | True | 20.20 |
| 23 | IBM | IBM | 294.40 | 36.10 | 26.10 | 0.99 | True | 22.70 |
| 24 | BA | BA | 224.19 | 36.10 | 24.70 | 0.29 | True | 2.90 |
| 25 | KO | KO | 82.61 | 36.10 | 26.50 | 0.64 | True | 7.60 |
| 26 | SO | Southern Company | 95.42 | 36.10 | 23.10 | 0.15 | True | -1.00 |
| 27 | MRK | MRK | 125.16 | 36.10 | 23.00 | 0.43 | True | 2.30 |
| 28 | CAT | CAT | 949.22 | 35.70 | 36.80 | -0.34 | True | 23.30 |
| 29 | COIN | COIN | 160.28 | 33.90 | 38.30 | -0.01 | False | -8.50 |
| 30 | HON | HON | 222.21 | 33.50 | 38.10 | -1.05 | False | -8.40 |
| 31 | SNOW | SNOW | 265.46 | 32.70 | 86.20 | 1.48 | True | 77.00 |
| 32 | JPM | JPM | 335.82 | 32.70 | 59.50 | 1.01 | True | 9.50 |
| 33 | ANET | Arista Networks | 184.87 | 32.70 | 85.10 | 2.27 | True | 27.40 |
| 34 | SLS | Sellas Life Sciences | 14.68 | 32.70 | 80.00 | 1.10 | True | 202.00 |
| 35 | DELL | Dell | 457.43 | 32.70 | 94.30 | 2.47 | True | 147.40 |
| 36 | ES | Eversource Energy | 74.12 | 32.70 | 56.60 | 1.10 | True | 7.20 |
| 37 | GRPN | Groupon | 26.35 | 32.70 | 62.10 | 1.12 | True | 120.20 |
| 38 | OPEN | Opendoor | 5.21 | 32.70 | 85.50 | 1.95 | True | 12.30 |
| 39 | BULL | Webull | 7.32 | 32.70 | 85.20 | 1.37 | True | 44.00 |
| 40 | RDDT | Reddit | 198.48 | 32.70 | 64.50 | 1.31 | True | 36.90 |


_...and 56 more._

## SKIPPED  (4)

SPCX, OS, PS, DAY
