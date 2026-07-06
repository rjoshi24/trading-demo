"""
run.py
======
End-to-end runner for the WSB BMSB screener.

    python -m wsb_screener.run            # top 200, writes results/
    python -m wsb_screener.run --top 100  # smaller universe

Outputs (in results/):
  wsb_bmsb_screen.csv   - full ranked table
  wsb_bmsb_report.md    - grouped, human-readable report
"""
from __future__ import annotations
import argparse
import os
import time

from .data import get_wsb_tickers, download_history
from .screener import run_screener
from .report import build_markdown


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=200, help="how many WSB tickers")
    ap.add_argument("--outdir", default="results")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    t0 = time.time()

    print(f"[1/4] Fetching top {args.top} r/wallstreetbets tickers ...")
    tickers = get_wsb_tickers(args.top)
    metas = {t["ticker"]: t for t in tickers}
    print(f"      got {len(metas)} tickers")

    print("[2/4] Downloading 10y weekly history ...")
    hist = download_history(list(metas.keys()), period="10y", interval="1wk")
    print(f"      got price data for {len(hist)}/{len(metas)} tickers")

    print("[3/4] Screening (sweep + best config + live signal) ...")
    df = run_screener(hist, metas)

    # signal date = most common latest bar date across screened names
    sig_dates = df["signal_date"].dropna() if "signal_date" in df else []
    signal_date = sig_dates.mode().iloc[0] if len(sig_dates) else "n/a"

    print("[4/4] Writing outputs ...")
    csv_path = os.path.join(args.outdir, "wsb_bmsb_screen.csv")
    md_path = os.path.join(args.outdir, "wsb_bmsb_report.md")
    df.to_csv(csv_path, index=False)
    with open(md_path, "w") as f:
        f.write(build_markdown(df, len(metas), signal_date))

    dt = time.time() - t0
    print(f"\nDone in {dt:.0f}s. Signal date: {signal_date}")
    print("Group counts:")
    print(df["group"].value_counts().to_string())
    print(f"\nCSV : {csv_path}\nMD  : {md_path}")


if __name__ == "__main__":
    main()
