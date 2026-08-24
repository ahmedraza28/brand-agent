#!/usr/bin/env python3
"""
check_facts.py

WHY THIS EXISTS: "never publish a number that is not on the approved list" is
an instruction, and an instruction in a prompt is not a guardrail. This agent
posts unsupervised under Ahmed's real name, into a market where the whole
strategy depends on our numbers being checkable by a stranger. So the rule is
enforced here, in code, on the draft, before it reaches Buffer. A draft that
fails this check does not ship.

WHAT IT BLOCKS (exit code 1):
  1. Any em dash. Absolute rule for published copy.
  2. "voice screening" / "audio screening" / "phone screening" for the core
     product. Ployo is an AI VIDEO interviewer.
  3. Any value that came from the mock findings file. Invented numbers cannot
     reach LinkedIn by any path that does not involve deleting this check.
  4. Any numeric claim that is not in state/stats-pack.json. Percentages and
     large figures always require approval. Years and small counts are allowed
     by construction so that "10 December 2026" and "7 tools" do not fail.
  5. An opener that leads with another company's research without adding one of
     our own figures. That single defect is why our citations have been going
     to Resume Builder and iCIMS instead of to us.

WHAT IT WARNS ABOUT (exit code 0, but reported): no mention of Ployo, no link
to ployo.ai, a figure written in a different surface form than the canonical
one on ployo.ai.

Dependency-free: stdlib only.

Usage:
    python3 tools/check_facts.py draft.md
    cat draft.txt | python3 tools/check_facts.py -
    python3 tools/check_facts.py draft.md --json
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import stats_pack  # noqa: E402

OPENER_CHARS = 400

BANNED_PRODUCT_TERMS = [
    "voice screening",
    "voice screen",
    "audio screening",
    "audio screen",
    "phone screening",
    "phone screen",
]

# Research houses and data publishers whose findings we have been handing our
# citations to. Leading with one of these is only allowed when the post also
# states one of our own approved figures.
BORROWED_RESEARCH_SOURCES = [
    "resume builder", "resumebuilder", "icims", "goldman sachs", "goldman",
    "gartner", "forrester", "mckinsey", "deloitte", "pwc", "kpmg", "accenture",
    "shrm", "korn ferry", "josh bersin", "bersin", "lever", "greenhouse",
    "workday", "indeed", "seek", "glassdoor", "linkedin's", "harvard business review",
    "stanford", "mit", "world economic forum", "wef",
]

NUMBER_RE = re.compile(
    r"""(?<![\w.])            # not mid-word
        (\d{1,3}(?:,\d{3})+   # 30,000
        |\d+(?:\.\d+)?)       # 70 or 11.5
        \s*
        (%|percent|k\b|m\b|x\b)?   # optional unit
        (\+)?                      # optional plus
    """,
    re.VERBOSE | re.IGNORECASE,
)


def normalize_number(raw, unit):
    """Return a float in base units, or None if it cannot be read."""
    try:
        n = float(raw.replace(",", ""))
    except ValueError:
        return None
    if unit:
        u = unit.lower().strip()
        if u == "k":
            n *= 1_000
        elif u == "m":
            n *= 1_000_000
    return n


def approved_number_set(pack):
    """Numeric values a post is allowed to state, plus their canonical display."""
    out = {}
    for fid, fig in stats_pack.publishable_values(pack).items():
        if fig.get("kind") == "numeric" or fig.get("unit"):
            val = fig.get("value")
            if val is not None:
                out[float(val)] = fig
    return out


def mock_number_set():
    """Numeric values known to be invented. Their presence is a hard failure."""
    mock = stats_pack.load_mock()
    if not mock:
        return {}
    out = {}
    for item in mock.get("items", []):
        val = item.get("value")
        if val is not None:
            out[float(val)] = item
    return out


def is_safe_by_construction(value, unit, context):
    """
    True for numbers that carry no claim about the business: years, small
    counts, and ordinary list sizes. Percentages are NEVER safe by
    construction, because a percentage is the shape a fabricated statistic
    almost always takes.
    """
    if unit and unit.lower().strip() in ("%", "percent"):
        return False
    if value is None:
        return False
    # A bare four-digit year.
    if float(value).is_integer() and 1900 <= value <= 2100 and "," not in context:
        return True
    # Small counts: "3 things", "7 to 12 tools", "10 December".
    if float(value).is_integer() and 0 <= value <= 12:
        return True
    return False


def check(text, pack=None):
    pack = pack or stats_pack.load_pack()
    approved = approved_number_set(pack)
    mocks = mock_number_set()
    failures = []
    warnings = []

    if "—" in text:
        count = text.count("—")
        failures.append({
            "rule": "em_dash",
            "detail": f"{count} em dash(es) in the draft. Hard rule: none in published copy.",
        })

    lowered = text.lower()
    # Longest first, then skip a shorter term that is only matching inside a
    # longer one already flagged ("voice screen" inside "voice screening").
    hit_terms = []
    for term in sorted(BANNED_PRODUCT_TERMS, key=len, reverse=True):
        if term in lowered and not any(term in seen for seen in hit_terms):
            hit_terms.append(term)
            failures.append({
                "rule": "banned_product_term",
                "detail": f"'{term}' describes the core product as audio. Ployo is an AI video interviewer.",
            })

    for match in NUMBER_RE.finditer(text):
        raw, unit, plus = match.group(1), match.group(2), match.group(3)
        value = normalize_number(raw, unit)
        surface = match.group(0).strip()
        start = max(0, match.start() - 40)
        context = text[start:match.end() + 40].replace("\n", " ")

        if value is None:
            continue

        if value in mocks:
            failures.append({
                "rule": "mock_value",
                "detail": (
                    f"'{surface}' matches the INVENTED mock finding "
                    f"'{mocks[value].get('id')}'. Mock numbers are for pipeline testing only "
                    "and must never be published."
                ),
                "context": context.strip(),
            })
            continue

        if value in approved:
            fig = approved[value]
            canonical = fig.get("display", "")
            if canonical and canonical.replace(" ", "") != surface.replace(" ", ""):
                warnings.append({
                    "rule": "surface_form",
                    "detail": f"'{surface}' should be written exactly as '{canonical}' to match ployo.ai.",
                })
            continue

        if is_safe_by_construction(value, unit, surface):
            continue

        failures.append({
            "rule": "unapproved_number",
            "detail": (
                f"'{surface}' is not in state/stats-pack.json. Either it is wrong, or it is a "
                "real finding that nobody has measured and recorded yet. Do not publish it."
            ),
            "context": context.strip(),
        })

    opener = lowered[:OPENER_CHARS]
    borrowed = [s for s in BORROWED_RESEARCH_SOURCES if s in opener]
    if borrowed:
        states_own_figure = any(
            str(int(v)) in text.replace(",", "") or fig.get("display", "") in text
            for v, fig in approved.items()
        )
        if not states_own_figure:
            failures.append({
                "rule": "borrowed_opener",
                "detail": (
                    f"The opener leads with {borrowed[0]}'s research and the post adds none of our "
                    "own figures. That hands the citation to them. Lead with our finding, or cut it."
                ),
            })

    if "ployo" not in lowered:
        warnings.append({
            "rule": "no_ployo_mention",
            "detail": "Post never names Ployo. Target is at least half of all posts.",
        })
    if "ployo.ai" not in lowered:
        warnings.append({
            "rule": "no_link",
            "detail": "Post does not link ployo.ai. Target is at least a third of all posts.",
        })

    return {"ok": not failures, "failures": failures, "warnings": warnings}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Block a draft that states an unapproved fact.")
    ap.add_argument("draft", help="path to the draft, or - for stdin")
    ap.add_argument("--json", action="store_true", help="machine-readable result")
    args = ap.parse_args(argv)

    text = sys.stdin.read() if args.draft == "-" else Path(args.draft).read_text(encoding="utf-8")
    result = check(text)

    if args.json:
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1

    for f in result["failures"]:
        print(f"FAIL [{f['rule']}] {f['detail']}")
        if f.get("context"):
            print(f"       ...{f['context']}...")
    for w in result["warnings"]:
        print(f"WARN [{w['rule']}] {w['detail']}")
    print("\nPASS: draft may ship." if result["ok"] else "\nBLOCKED: fix the failures above. Do not publish.")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
