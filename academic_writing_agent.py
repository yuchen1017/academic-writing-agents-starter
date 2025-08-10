#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate structured sections (Intro/Methods/Discussion) with a 4-part template.

Usage:
  python academic_writing_agent.py --title "Topic" --template intro --citations "Smith 2022; Lee 2021" --outfile out.md
"""
import argparse
from datetime import date

TEMPLATES = {
    "intro": [
        "Known facts and unresolved problems",
        "Brief subject review with recent citations",
        "Research gap",
        "This study: methods and contents"
    ],
    "methods": [
        "Experimental design",
        "Interventions or treatments",
        "Measurements and observations",
        "Statistical procedures"
    ],
    "discussion": [
        "Key results (3–4 items)",
        "Relation to literature",
        "Main academic contributions",
        "Limitations and future work"
    ],
}

def build_paragraph(header: str, topic: str, citations: str) -> str:
    core = {
        "Known facts and unresolved problems":
            f"{topic}: key facts are established, yet important uncertainties remain. We summarize what is known and clarify the outstanding problem motivating this study.",
        "Brief subject review with recent citations":
            f"Recent work has advanced the field; representative reports include {citations if citations else 'recent studies'}. We highlight trends and methodological shifts within the last 5–10 years.",
        "Research gap":
            "Despite progress, a specific gap persists in scope, population, comparator, outcomes, timing, or setting. Precisely defining this gap informs our objectives.",
        "This study: methods and contents":
            "Here we outline the approach, datasets/participants, primary endpoints, and planned analyses to address the gap.",
        "Experimental design":
            "We used a prospective design with predefined eligibility, outcomes, and power assumptions.",
        "Interventions or treatments":
            "Intervention details (dose, timing, delivery) and control conditions are specified to enable replication.",
        "Measurements and observations":
            "Primary/secondary outcomes, covariates, timepoints, and quality control are described.",
        "Statistical procedures":
            "We predefined the analysis set, handled missingness, and applied appropriate models with sensitivity analyses.",
        "Key results (3–4 items)":
            "We summarize only the most decision-relevant findings with effect estimates and uncertainty.",
        "Relation to literature":
            "We compare magnitudes and directions with recent studies and explain divergences.",
        "Main academic contributions":
            "We articulate what is genuinely new: method, dataset, theory, or clinical implication.",
        "Limitations and future work":
            "We acknowledge internal/external validity limits and propose targeted next steps."
    }
    return f"**{header}.** {core.get(header, '')}\n\n"

def generate_section(template: str, title: str, citations: str) -> str:
    template = template.lower()
    if template not in TEMPLATES:
        raise SystemExit(f"Unknown template: {template}. Choose from {list(TEMPLATES)}")
    lines = [f"# {title}", f"_Generated on {date.today().isoformat()}_", ""]
    for h in TEMPLATES[template]:
        lines.append(build_paragraph(h, title, citations))
    if citations:
        lines.append(f"**References (indicative):** {citations}")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True, help="Topic or working title")
    ap.add_argument("--template", required=True, choices=list(TEMPLATES.keys()))
    ap.add_argument("--citations", default="", help="Recent citations, e.g., 'Smith 2022; Lee 2021'")
    ap.add_argument("--outfile", default="", help="Write Markdown to this file")
    args = ap.parse_args()
    md = generate_section(args.template, args.title, args.citations)
    if args.outfile:
        with open(args.outfile, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Written: {args.outfile}")
    else:
        print(md)

if __name__ == "__main__":
    main()
