"""
run_quant.py
============
End-to-end runner for the daily **dip-and-ride research model**.

    python -m wsb_screener.run_quant             # default universe, writes results/
    python -m wsb_screener.run_quant --top 100   # smaller WSB universe

Outputs (in results/):
  wsb_quant_screen.csv   - full ranked table
  wsb_quant_report.md    - grouped, human-readable report
"""
from __future__ import annotations
import argparse
import os
import time

from .data import get_universe, download_history
from . import quant_screener as qscr
from .quant_report import build_markdown
from .quant_core import QuantConfig, portfolio_backtest


def main():
    ap = argparse.ArgumentParser(
        description="Run the daily dip-and-ride research screener.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    ap.add_argument("--source", default="both", choices=["popular", "wsb", "both"],
                    help="universe: most popular US names, WSB, or both")
    ap.add_argument("--top", type=int, default=120, help="how many WSB tickers")
    ap.add_argument("--popular", type=int, default=120, help="how many popular tickers")
    ap.add_argument("--period", default="5y", help="daily history length")
    ap.add_argument("--stop", type=float, default=0.06,
                    help="close-below-entry fraction that triggers a next-open exit")
    ap.add_argument("--ride", default="chandelier",
                    choices=["chandelier", "chandelier_wide", "pct", "sma50"],
                    help="how winners ride (trailing exit)")
    ap.add_argument("--outdir", default="results")
    args = ap.parse_args()

    try:
        config = QuantConfig(close_exit_pct=args.stop, ride_mode=args.ride)
    except ValueError as exc:
        ap.error(str(exc))

    os.makedirs(args.outdir, exist_ok=True)
    t0 = time.time()

    print(f"[1/4] Building universe (source={args.source}) ...")
    uni = get_universe(source=args.source, top_n=args.top, popular_n=args.popular)
    metas = {t["ticker"]: t for t in uni}
    print(f"      got {len(metas)} tickers")

    print(f"[2/4] Downloading {args.period} daily history ...")
    hist, data_failures = download_history(
        list(metas.keys()), period=args.period, interval="1d", return_failures=True,
    )
    print(f"      got price data for {len(hist)}/{len(metas)} tickers")

    print("[3/4] Screening (dip -> conviction gate -> position-aware bucket) ...")
    df = qscr.run_screener(hist, metas, config=config, data_failures=data_failures)
    screen_errors = df[df["group"] == "ERROR"]
    if not screen_errors.empty:
        stages = screen_errors["error_stage"].fillna("unknown").value_counts()
        detail = ", ".join(f"{stage}={count}" for stage, count in stages.items())
        print(f"      WARNING: screening failed for {len(screen_errors)} ticker(s) "
              f"({detail}); see ERROR rows")

    sig_dates = df["signal_date"].dropna() if "signal_date" in df else []
    signal_date = sig_dates.mode().iloc[0] if len(sig_dates) else "n/a"

    print(f"      running $100 portfolio backtest (close exit {args.stop:.0%}, ride {args.ride}) ...")
    port = portfolio_backtest(hist, start_cash=100.0, max_positions=8, config=config)
    if port["model_errors"]:
        print(f"      WARNING: portfolio model failed for {len(port['model_errors'])} ticker(s):")
        for error in port["model_errors"][:10]:
            print(f"        {error['ticker']}: {error['error_type']}: {error['error_message']}")
        if len(port["model_errors"]) > 10:
            print(f"        ...and {len(port['model_errors']) - 10} more (see Markdown report)")

    print("[4/4] Writing outputs ...")
    csv_path = os.path.join(args.outdir, "wsb_quant_screen.csv")
    md_path = os.path.join(args.outdir, "wsb_quant_report.md")
    df.to_csv(csv_path, index=False)
    with open(md_path, "w") as f:
        f.write(build_markdown(df, len(metas), signal_date, portfolio=port))
    print(f"      $100 -> ${port['final_$']:.2f} ({port['return_%']:+.0f}%, {port['win_rate_%']}% win)")

    dt = time.time() - t0
    print(f"\nDone in {dt:.0f}s. Signal date: {signal_date}")
    print("Group counts:")
    print(df["group"].value_counts().to_string())
    print(f"\nCSV : {csv_path}\nMD  : {md_path}")


if __name__ == "__main__":
    main()
