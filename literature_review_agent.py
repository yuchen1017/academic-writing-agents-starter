#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate search strings and an outline for a quick literature review.

Usage:
  python literature_review_agent.py --topic "metformin AND NAFLD" --db pubmed
"""
import argparse

DB_SYNONYMS = {
    "pubmed": ["(MeSH terms)", "Title/Abstract", "Last 5 years"],
    "scholar": ["allintitle:", "since 2019", "exclude patents"],
}

def build_queries(topic: str, db: str):
    if db not in DB_SYNONYMS:
        raise SystemExit(f"Unsupported db: {db}")
    base = topic.strip()
    extras = DB_SYNONYMS[db]
    return [base] + [f"{base} {tag}" for tag in extras]

def outline(topic: str):
    return [
        "Background and unresolved problem",
        "Recent progress (3–5 key studies)",
        "Methodological trends and controversies",
        "Gap and proposed question"
    ]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True)
    ap.add_argument("--db", choices=list(DB_SYNONYMS.keys()), default="pubmed")
    args = ap.parse_args()
    print("# Search strings:")
    for q in build_queries(args.topic, args.db):
        print("-", q)
    print("\n# Outline:")
    for i, h in enumerate(outline(args.topic), 1):
        print(f"{i}. {h}")
    print("\n# Screening criteria:")
    print("- English; human studies; last 5–10 years; relevant outcomes")

if __name__ == "__main__":
    main()
