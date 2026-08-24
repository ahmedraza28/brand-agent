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

# A number is only a fabrication risk when the post presents it as OURS. A
# number attributed to an outside study is governed by guardrail 1 (trace it to
# a fetched source) and is not this checker's job. Getting this distinction
# wrong in either direction is fatal: too loose and invented statistics ship,
# too strict and the gate blocks every commentary post and gets switched off.
# Measured against the last 40 real published posts when this was written.
# MEASURED against the last 40 real published posts. A first cut used bare "we"
# and "our" and flagged rhetorical usage ("we all know", "our industry") as a
# data claim. These are ownership phrases only: a number attached to one of
# these is being presented as something Ployo measured.
OWN_DATA_MARKERS = [
    "in our data", "our data", "across our", "from our", "on our platform",
    "our platform", "our interviews", "our candidates", "our customers",
    "we ran", "we run", "we've run", "we have run", "we see", "we've seen",
    "we measured", "we found", "at ployo", "in ployo", "ployo's data",
]

# Attribution is assessed across the WHOLE post, not the paragraph. These posts
# introduce a source in the opening paragraph and then discuss its numbers for
# three more, so paragraph scope produced false failures on properly credited
# third-party figures (Fabric, Ramp/Revelio, Greenhouse were all hand-checked).
ATTRIBUTION_MARKERS = [
    "survey", "surveyed", "study", "studies", "report", "reported", "researchers",
    "according to", "poll", "polled", "analysis", "analysed", "analyzed",
    "found that", "data from", "respondents", "paper", "index", "economists",
    "figures from", "cited", "estimates", "estimated", "forecast", "filing",
    "lawsuit", "court", "regulator", "census", "audit of", "review of",
    "'s data", "their data", "sample of", "review found", "tracked", "track",
    "ran ", "put a number on", "published", "researcher", "dataset", "platform called",
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


# Below this, a mock value collides with ordinary counts ("4 of 9 tools"), so
# small mock figures are caught by their display STRING at document level
# instead of by their bare value.
MOCK_VALUE_FLOOR = 13


def mock_number_set():
    """Invented values large enough to be matched by value without collisions."""
    mock = stats_pack.load_mock()
    if not mock:
        return {}
    out = {}
    for item in mock.get("items", []):
        val = item.get("value")
        if val is not None and float(val) >= MOCK_VALUE_FLOOR:
            out[float(val)] = item
    return out


def mock_display_strings():
    """
    Mock findings whose written form is a distinctive PHRASE ("question 4 of 9",
    "11.5 minutes"), matched across the whole document. Bare figures like "58%"
    are excluded on purpose: measured against the real posting log, a bare
    percentage collides with ordinary third-party statistics and produced two
    false failures. Those are caught by value, in an ownership context, instead.
    """
    mock = stats_pack.load_mock()
    if not mock:
        return []
    return [
        (item["display"], item)
        for item in mock.get("items", [])
        if item.get("display") and " " in item["display"].strip()
    ]


def paragraph_for(text, index):
    """The paragraph a character index sits in. Attribution is usually one
    sentence away from the number it introduces, so sentence scope is too
    narrow and whole-post scope is too wide."""
    start = text.rfind("\n\n", 0, index)
    start = 0 if start == -1 else start + 2
    end = text.find("\n\n", index)
    end = len(text) if end == -1 else end
    return text[start:end]


def post_has_external_attribution(text):
    """Does the post credit an outside source anywhere? Assessed across the
    whole post on purpose (see ATTRIBUTION_MARKERS)."""
    t = text.lower()
    return any(m in t for m in ATTRIBUTION_MARKERS) or any(x in t for x in BORROWED_RESEARCH_SOURCES)


def sentence_for(text, index):
    """The sentence a character index sits in."""
    start = max(text.rfind(". ", 0, index), text.rfind("\n", 0, index))
    start = 0 if start == -1 else start + 1
    end = text.find(". ", index)
    end = len(text) if end == -1 else end + 1
    return text[start:end]


def claims_as_ours(paragraph, sentence):
    """
    Is this number presented as something Ployo measured? Two ways it can be:
    an explicit ownership phrase anywhere in the paragraph, or a first-person
    sentence in a paragraph that credits nobody. The second clause is what
    catches "Our completion rate is 91%", which names no marker phrase but is
    unmistakably a claim about us.
    """
    p, sent = paragraph.lower(), sentence.lower()
    if any(m in p for m in OWN_DATA_MARKERS):
        return True
    paragraph_credits_someone = (
        any(m in p for m in ATTRIBUTION_MARKERS)
        or any(x in p for x in BORROWED_RESEARCH_SOURCES)
    )
    if paragraph_credits_someone:
        return False
    return bool(re.search(r"\b(our|we|we've|i've)\b", sent))


def is_safe_by_construction(value, unit, trailing):
    """`trailing` is the text immediately after the number, used to spot a
    duration ("18-month", "54 days")."""
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
    if float(value).is_integer() and 1900 <= value <= 2100:
        return True
    # Small counts: "3 things", "7 to 12 tools", "10 December".
    if float(value).is_integer() and 0 <= value <= 12:
        return True
    # Durations. "an 18-month countdown" and "53 to 54 days" are time spans, not
    # claims about the business. Hand-judged from the real posting log.
    if re.search(
        r"^\s*[-\u2013]?\s*(second|minute|hour|day|week|month|quarter|year)s?\b",
        trailing,
        re.IGNORECASE,
    ):
        return True
    return False


def check(text, pack=None):
    pack = pack or stats_pack.load_pack()
    approved = approved_number_set(pack)
    mocks = mock_number_set()
    failures = []
    warnings = []
    third_party_numbers = 0
    has_external_source = post_has_external_attribution(text)

    if "—" in text:
        count = text.count("—")
        failures.append({
            "rule": "em_dash",
            "detail": f"{count} em dash(es) in the draft. Hard rule: none in published copy.",
        })

    lowered = text.lower()

    for display, item in mock_display_strings():
        if display.lower() in lowered:
            failures.append({
                "rule": "mock_value",
                "detail": (
                    f"'{display}' is the INVENTED mock finding '{item.get('id')}'. Mock findings "
                    "exist to exercise the drafting pipeline and must never be published."
                ),
            })

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

        if value in approved:
            fig = approved[value]
            canonical = fig.get("display", "")
            if canonical and canonical.replace(" ", "") != surface.replace(" ", ""):
                warnings.append({
                    "rule": "surface_form",
                    "detail": f"'{surface}' should be written exactly as '{canonical}' to match ployo.ai.",
                })
            continue

        trailing = text[match.end():match.end() + 24]
        if is_safe_by_construction(value, unit, trailing):
            continue

        paragraph = paragraph_for(text, match.start())

        if claims_as_ours(paragraph, sentence_for(text, match.start())):
            if value in mocks:
                failures.append({
                    "rule": "mock_value",
                    "detail": (
                        f"'{surface}' is the INVENTED mock finding '{mocks[value].get('id')}' and is "
                        "written as our own data. Mock findings exist to exercise the drafting "
                        "pipeline and must never be published."
                    ),
                    "context": context.strip(),
                })
                continue
            failures.append({
                "rule": "unapproved_own_number",
                "detail": (
                    f"'{surface}' is stated as Ployo's own data but is not in "
                    "state/stats-pack.json. Either it is wrong, or it is a real finding nobody "
                    "has measured and recorded yet. Do not publish it."
                ),
                "context": context.strip(),
            })
            continue

        if has_external_source:
            # Someone else's number, credited somewhere in the post. Whether it
            # was actually verified this run is guardrail 1's job, not this
            # checker's. Counted so the borrowed-data ratio stays visible.
            third_party_numbers += 1
            continue

        # No source anywhere in the post and no ownership phrase. A bare figure
        # under Ahmed's real name reads as his. Percentages are the shape a
        # fabricated statistic takes, so they block; anything else is reported.
        if unit and unit.lower().strip() in ("%", "percent"):
            failures.append({
                "rule": "unattributed_percentage",
                "detail": (
                    f"'{surface}' has no source anywhere in the post. Under Ahmed's name that "
                    "reads as our figure. Credit the source, or cut it."
                ),
                "context": context.strip(),
            })
        else:
            warnings.append({
                "rule": "unattributed_number",
                "detail": f"'{surface}' has no visible attribution anywhere in the post.",
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

    if third_party_numbers and not any(
        str(int(v)) in text.replace(",", "") or fig.get("display", "") in text
        for v, fig in approved.items()
    ):
        warnings.append({
            "rule": "borrowed_data_only",
            "detail": (
                f"{third_party_numbers} number(s) in this post belong to someone else and none "
                "belong to us. This is the post type that has been sending our citations to "
                "other companies. Target is under 15% of posts."
            ),
        })

    return {
        "ok": not failures,
        "failures": failures,
        "warnings": warnings,
        "third_party_numbers": third_party_numbers,
    }


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
