#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CASP-style quick appraisal checklist from an abstract or summary (rule-based)."""
import argparse

TEMPLATE = [
    ("Clear focused question?", "Yes/No/Unclear"),
    ("Appropriate study design?", "Yes/No/Partial"),
    ("Bias risk addressed?", "Randomization/Allocation/Blinding"),
    ("Precision reported?", "CI/SD/SE"),
    ("Applicability to your setting?", "High/Moderate/Low"),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--abstract", required=True, help="Paste abstract text or a short summary")
    args = ap.parse_args()
    print("# CASP Quick Appraisal\n")
    for q, hint in TEMPLATE:
        print(f"- **{q}** (hint: {hint}) → ")
    print("\nAdd notes on strengths, limitations, and relevance.")

if __name__ == "__main__":
    main()
