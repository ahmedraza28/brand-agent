#!/usr/bin/env python3
"""
stats_pack.py

WHY THIS EXISTS: the LinkedIn brief of 2026-08-24 asks for two things that
contradict each other unless something reconciles them. It says "never publish
a number that is not on the approved list", and it also says the highest-value
posts are first-party findings from our own operations, which by definition are
numbers that are not yet on any list. This tool is the reconciliation. There is
exactly one file of publishable numbers (state/stats-pack.json), a finding only
enters it once a human has run a real query and dated the result, and every
draft is checked against it before it ships (tools/check_facts.py).

WHAT IT DELIBERATELY DOES NOT DO: touch a database. This tool has no
credentials, no connection string, no network call, and no import of any
database driver. That is a design decision, not an omission. The agent that
runs this is a full-auto poster on a public repo; giving it a read path into
production so it can autonomously mint statistics about the business is a
much larger blast radius than the posts are worth. Real findings are produced
by a human running a query, eyeballing the result, and pasting it in with a
date and a description of how it was measured.

MOCK MODE: --mock writes state/stats-pack.mock.json, a set of realistic but
INVENTED findings whose only purpose is to exercise the drafting pipeline end
to end before any real number exists. The mock file is gitignored so it never
reaches the public repo, every entry carries status "mock", and check_facts.py
hard-fails any draft containing a mock value. A mock number cannot reach
LinkedIn by any path that does not involve someone deliberately disabling the
check.

Dependency-free: stdlib only, matching tools/posting_window.py.

Usage:
    python3 tools/stats_pack.py                 # human-readable report
    python3 tools/stats_pack.py --list          # every publishable value, one per line
    python3 tools/stats_pack.py --json          # machine-readable, for the routine
    python3 tools/stats_pack.py --mock          # (re)generate the gitignored mock findings
    python3 tools/stats_pack.py --validate      # exit 1 if the pack is malformed
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACK_PATH = ROOT / "state" / "stats-pack.json"
MOCK_PATH = ROOT / "state" / "stats-pack.mock.json"

PUBLISHABLE_STATUSES = {"approved_public", "verified_query"}
BLOCKED_STATUSES = {"mock", "draft", "unverified"}

REQUIRED_FIGURE_KEYS = {"id", "kind", "display", "label", "status", "source"}


# Realistic-looking findings used ONLY to exercise the pipeline. Every one of
# these is invented. The measurement notes are written in plain English on
# purpose: this file lives in a public repo, so it must not describe internal
# schema, table names, model names or infrastructure.
MOCK_FINDINGS = [
    {
        "id": "cv_vs_interview_disagreement",
        "label": "Share of screened candidates where the CV read and the interview read disagree",
        "display": "31%",
        "value": 31,
        "unit": "percent",
        "how_measured": "Compare the requirement verdict derived from the CV against the requirement verdict derived from the interview transcript, same candidate, same role. Count the candidates where they differ.",
    },
    {
        "id": "cv_pass_interview_fail_share",
        "label": "Of those disagreements, the share where the CV said yes and the interview said no",
        "display": "68%",
        "value": 68,
        "unit": "percent",
        "how_measured": "Of the disagreeing candidates above, the directional split.",
    },
    {
        "id": "median_dropoff_point",
        "label": "Where an unfinished interview typically stops",
        "display": "question 4 of 9",
        "value": 4,
        "unit": "question index",
        "how_measured": "For interviews that started and did not complete, the median index of the last question asked.",
    },
    {
        "id": "completion_spread_by_language",
        "label": "Completion-rate gap between the strongest and weakest language cohort",
        "display": "12 points",
        "value": 12,
        "unit": "percentage points",
        "how_measured": "Completion rate per interview language, highest cohort minus lowest, cohorts under a minimum sample size excluded.",
    },
    {
        "id": "within_verdict_grade_spread",
        "label": "Range of per-question scores inside a single passing verdict",
        "display": "20 to 80",
        "value": None,
        "unit": "score range",
        "how_measured": "For candidates who passed, the min and max per-question grade within the same interview. Shows that one headline verdict hides a wide spread.",
    },
    {
        "id": "invite_to_start_rate",
        "label": "Share of invited candidates who start the interview",
        "display": "58%",
        "value": 58,
        "unit": "percent",
        "how_measured": "Interviews started divided by invitations sent, over a fixed window.",
    },
    {
        "id": "median_time_to_complete",
        "label": "Median length of a completed interview",
        "display": "11.5 minutes",
        "value": 11.5,
        "unit": "minutes",
        "how_measured": "Median wall-clock duration of completed interviews.",
    },
]


def load_pack(path=PACK_PATH):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def load_mock(path=MOCK_PATH):
    if not Path(path).exists():
        return None
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def validate(pack):
    """Return a list of problems. Empty list means the pack is well formed."""
    problems = []
    seen_ids = set()

    figures = pack.get("figures")
    if not isinstance(figures, list) or not figures:
        problems.append("pack has no 'figures' list")
        return problems

    for i, fig in enumerate(figures):
        missing = REQUIRED_FIGURE_KEYS - set(fig)
        if missing:
            problems.append(f"figure {i} ({fig.get('id', '?')}) missing keys: {sorted(missing)}")
        fid = fig.get("id")
        if fid in seen_ids:
            problems.append(f"duplicate figure id: {fid}")
        seen_ids.add(fid)
        status = fig.get("status")
        if status in BLOCKED_STATUSES:
            problems.append(
                f"figure {fid} has status '{status}' but lives in the publishable pack; "
                "unverified numbers belong in the mock file, not here"
            )
        elif status not in PUBLISHABLE_STATUSES:
            problems.append(f"figure {fid} has unknown status '{status}'")
        if fig.get("kind") == "numeric" and fig.get("value") is None:
            problems.append(f"numeric figure {fid} has no 'value'")

    findings = pack.get("findings", {}).get("items", [])
    for f in findings:
        if f.get("status") != "verified_query":
            problems.append(
                f"finding {f.get('id', '?')} is in the publishable pack with status "
                f"'{f.get('status')}'. A finding is only publishable once a real query "
                "has been run and recorded (status 'verified_query')."
            )
        if not f.get("measured_on"):
            problems.append(f"finding {f.get('id', '?')} has no 'measured_on' date")
        if not f.get("how_measured"):
            problems.append(f"finding {f.get('id', '?')} does not say how it was measured")

    return problems


def publishable_values(pack):
    """Every string a post is allowed to state as a fact, keyed by figure id."""
    out = {}
    for fig in pack.get("figures", []):
        if fig.get("status") in PUBLISHABLE_STATUSES:
            out[fig["id"]] = fig
    for f in pack.get("findings", {}).get("items", []):
        if f.get("status") == "verified_query":
            out[f["id"]] = f
    return out


def write_mock(path=MOCK_PATH):
    payload = {
        "_README": (
            "INVENTED NUMBERS. NOT REAL. Generated by tools/stats_pack.py --mock so the "
            "drafting pipeline can be exercised before any real measurement exists. Every "
            "value here is made up. tools/check_facts.py hard-fails any draft containing "
            "one of these values, and this file is gitignored so it never reaches the "
            "public repo or the cloud routine. Do not promote a value out of this file "
            "into state/stats-pack.json. Replace it with the result of a real query."
        ),
        "generated_by": "tools/stats_pack.py --mock",
        "status": "mock",
        "items": [
            dict(item, status="mock", publishable=False, measured_on=None)
            for item in MOCK_FINDINGS
        ],
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2)
        fh.write("\n")
    return payload


def main(argv=None):
    ap = argparse.ArgumentParser(description="Approved-facts pack for the brand agent.")
    ap.add_argument("--list", action="store_true", help="one publishable value per line")
    ap.add_argument("--json", action="store_true", help="machine-readable publishable set")
    ap.add_argument("--mock", action="store_true", help="regenerate the gitignored mock findings")
    ap.add_argument("--validate", action="store_true", help="exit 1 if the pack is malformed")
    args = ap.parse_args(argv)

    if args.mock:
        payload = write_mock()
        print(f"wrote {MOCK_PATH} with {len(payload['items'])} INVENTED findings (gitignored, unpublishable)")
        return 0

    pack = load_pack()
    problems = validate(pack)

    if args.validate:
        for p in problems:
            print(f"FAIL: {p}", file=sys.stderr)
        print("stats pack OK" if not problems else f"{len(problems)} problem(s)")
        return 1 if problems else 0

    values = publishable_values(pack)

    if args.json:
        print(json.dumps(values, indent=2))
        return 0

    if args.list:
        for fid, fig in values.items():
            print(f"{fig['display']}\t{fig.get('label', '')}")
        return 0

    print(f"Approved facts pack v{pack.get('version')} (updated {pack.get('updated')})")
    print(f"Source of truth: {pack.get('source_of_truth')}\n")
    for fid, fig in values.items():
        print(f"  {fig['display']:<12} {fig.get('label', '')}")
    findings = pack.get("findings", {}).get("items", [])
    print(f"\nFirst-party findings measured so far: {len(findings)}")
    if not findings:
        print("  none yet. Until a real query is run and recorded here, no post may state")
        print("  a first-party finding. `--mock` generates fake ones for pipeline testing only.")
    mock = load_mock()
    if mock:
        print(f"\n  (mock file present with {len(mock['items'])} invented findings, blocked from publishing)")
    if problems:
        print(f"\n{len(problems)} validation problem(s). Run --validate.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
