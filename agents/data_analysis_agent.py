#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic CSV profiler: prints shape, missingness, numeric summaries.

Usage:
  python data_analysis_agent.py --csv path/to/file.csv
"""
import argparse, pandas as pd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    args = ap.parse_args()
    df = pd.read_csv(args.csv)
    print("# Shape:", df.shape)
    print("\n# Missingness (count):\n", df.isna().sum())
    num = df.select_dtypes(include="number")
    if not num.empty:
        print("\n# Numeric summary:\n", num.describe().T)

if __name__ == "__main__":
    main()
