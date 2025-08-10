#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tiny formatter for APA/AMA-like references from simple CLI inputs.

Examples:
  python citation_reference_agent.py --style apa --author "Smith J" --year 2022 --title "Trial" --journal "Lancet" --volume 399 --issue 10332 --pages 123-130 --doi 10.1000/xyz
"""
import argparse

def fmt_apa(a, y, t, j, v=None, i=None, p=None, d=None):
    out = f"{a} ({y}). {t}. {j}"
    if v: out += f", {v}"
    if i: out += f"({i})"
    if p: out += f", {p}"
    out += "."
    if d: out += f" https://doi.org/{d}"
    return out

def fmt_ama(a, y, t, j, v=None, i=None, p=None, d=None):
    core = f"{a}. {t}. {j}. {y};"
    if v: core += f"{v}"
    if i: core += f"({i})"
    if p: core += f":{p}"
    if core.endswith(";"): core = core[:-1]
    core += "."
    if d: core += f" doi:{d}"
    return core

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", choices=["apa","ama"], default="apa")
    ap.add_argument("--author", required=True)
    ap.add_argument("--year", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--journal", required=True)
    ap.add_argument("--volume")
    ap.add_argument("--issue")
    ap.add_argument("--pages")
    ap.add_argument("--doi")
    args = ap.parse_args()
    kwargs = dict(a=args.author, y=args.year, t=args.title, j=args.journal, v=args.volume, i=args.issue, p=args.pages, d=args.doi)
    out = fmt_apa(**kwargs) if args.style=="apa" else fmt_ama(**kwargs)
    print(out)

if __name__ == "__main__":
    main()
