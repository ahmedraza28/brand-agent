#!/usr/bin/env python3
"""
ratios.py

WHY THIS EXISTS: "name Ployo in at least half of posts, link ployo.ai in at
least a third" is a target the agent cannot hit by good intentions. It writes
one post per run with no memory of the ratio it is supposed to be holding, so
without a number in front of it every run drifts back to the comfortable
default, which is what produced 10 mentions and 2 links across 61 posts.

This reads the real posting log and reports where the account actually stands,
so the agent can be told what THIS post needs to include. Run it in Step 1.

Targets, from the 2026-08-24 brief:
    names Ployo        >= 50%
    links ployo.ai     >= 33%
    names a competitor >= 33%
    AU care / NDIS     >= 33%
    borrowed-data lead <= 15%

Usage:
    python3 tools/ratios.py            # last 30 posts
    python3 tools/ratios.py --last 61  # the window the audit used
    python3 tools/ratios.py --json
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import check_facts  # noqa: E402

LOG_PATH = ROOT / "state" / "posting-log.md"

TARGETS = {
    "names_ployo": 0.50,
    "links_site": 0.33,
    "names_competitor": 0.33,
    "au_care": 0.33,
}
MAX_BORROWED = 0.15

AU_CARE_TERMS = [
    "aged care", "ndis", "ahpra", "disability", "support worker", "carer",
    "home care", "australia", "australian", "nursing", "aged-care",
]


def published_posts(text, limit):
    posts = [
        (m.group(1), m.group(2).strip())
        for m in re.finditer(r"^### (\S+) \|.*?\n\n\*\*Text:\*\*\n(.*?)\n\*\*Format", text, re.S | re.M)
    ]
    return posts[:limit]


def competitor_names():
    path = ROOT / "config" / "competitors.md"
    if not path.exists():
        return []
    body = path.read_text(encoding="utf-8").split("## Named in the brief but NOT")[0]
    return [
        line[3:].strip()
        for line in body.splitlines()
        if line.startswith("## ") and not line.startswith("## How to use")
    ]


def measure(limit=30):
    if not LOG_PATH.exists():
        return None
    posts = published_posts(LOG_PATH.read_text(encoding="utf-8"), limit)
    if not posts:
        return None
    rivals = [c.lower() for c in competitor_names()]
    counts = dict.fromkeys(TARGETS, 0)
    borrowed = 0

    for _, text in posts:
        low = text.lower()
        if "ployo" in low:
            counts["names_ployo"] += 1
        if "ployo.ai" in low:
            counts["links_site"] += 1
        if any(r.split("(")[0].strip() in low for r in rivals):
            counts["names_competitor"] += 1
        if any(t in low for t in AU_CARE_TERMS):
            counts["au_care"] += 1
        result = check_facts.check(text)
        if any(f["rule"] == "borrowed_opener" for f in result["failures"]):
            borrowed += 1

    n = len(posts)
    return {
        "window": n,
        "rates": {k: counts[k] / n for k in counts},
        "counts": counts,
        "borrowed_opener_rate": borrowed / n,
        "borrowed_opener_count": borrowed,
    }


def needs(report):
    """What the NEXT post should include to pull the account back on target."""
    if not report:
        return []
    out = []
    for key, target in TARGETS.items():
        if report["rates"][key] < target:
            out.append(key)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="Where the account stands against the brief's ratios.")
    ap.add_argument("--last", type=int, default=30)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    report = measure(args.last)
    if not report:
        print("no published posts found in state/posting-log.md")
        return 0

    if args.json:
        print(json.dumps({**report, "next_post_should": needs(report)}, indent=2))
        return 0

    n = report["window"]
    print(f"Last {n} published posts\n")
    labels = {
        "names_ployo": "names Ployo",
        "links_site": "links ployo.ai",
        "names_competitor": "names a competitor",
        "au_care": "AU care / health / NDIS",
    }
    for key, target in TARGETS.items():
        rate = report["rates"][key]
        mark = "ok " if rate >= target else "LOW"
        print(f"  [{mark}] {labels[key]:<26} {report['counts'][key]:>3}/{n}  {rate:5.0%}  target {target:.0%}")
    br = report["borrowed_opener_rate"]
    mark = "ok " if br <= MAX_BORROWED else "HIGH"
    print(f"  [{mark}] {'opens with their data':<26} {report['borrowed_opener_count']:>3}/{n}  {br:5.0%}  max {MAX_BORROWED:.0%}")

    todo = needs(report)
    print()
    if todo:
        print("  THIS post should include: " + ", ".join(labels[t] for t in todo))
    else:
        print("  On target. Write the best post, not a checkbox.")
    if br > MAX_BORROWED:
        print("  And it should NOT open by citing someone else's survey.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
