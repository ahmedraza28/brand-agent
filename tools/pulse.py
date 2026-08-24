#!/usr/bin/env python3
"""
pulse.py

WHY THIS EXISTS: 27% of every LinkedIn citation measured in the 2026-08-24
sweep went to Pulse articles, and four separate authors are being cited right
now for the same "best AI recruiting tools 2026" format. That is the single
most replicable finding in the brief. This tool is the pipeline for producing
those articles and getting them out the door at 2 to 3 a month.

WHY IT IS NOT FULLY AUTOMATED: LinkedIn has no public write API for articles.
Buffer, which the agent uses for everything else, posts to the feed only. So
the last step is a human pasting into LinkedIn's article editor, and `--brief`
exists to make that step mechanical. Publishing from Ahmed's own browser also
keeps it on a residential connection, which matters: the other brand agent
already hit the datacenter-IP wall.

THE DIVISION OF LABOUR:
  routine / author  ->  --new, writes docs/articles/<slug>.md
  this tool         ->  --check, refuses anything unciteable
  human             ->  --brief, paste, publish
  this tool         ->  --published, records the URL for the next sweep

THE CHECK IS THE POINT. A roundup with one invented price or one wrong
modality is discarded whole by the first reader who verifies it, and we do not
get a second attempt at being the cited source. So every vendor named in an
article must already exist in config/competitors.md, which is generated from
sourced, dated claims. A vendor nobody has fact-checked cannot appear.

Usage:
    python3 tools/pulse.py --new best-ai-interview-software-au-2026 --kind roundup \\
        --title "Best AI interview software for Australian care and health hiring in 2026"
    python3 tools/pulse.py --check best-ai-interview-software-au-2026
    python3 tools/pulse.py --list
    python3 tools/pulse.py --brief best-ai-interview-software-au-2026
    python3 tools/pulse.py --published best-ai-interview-software-au-2026 --url https://...
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import check_facts  # noqa: E402

ARTICLES_DIR = ROOT / "docs" / "articles"
QUEUE_PATH = ROOT / "state" / "pulse-queue.json"
COMPETITORS_PATH = ROOT / "config" / "competitors.md"

KINDS = ("roundup", "comparison", "compliance")
MONTHLY_TARGET = 2

MIN_VENDORS, MAX_VENDORS = 7, 12

REQUIRED_ENTRY_FIELDS = ["who it is for", "what it does", "pricing", "limitation"]

TEMPLATES = {
    "roundup": """# {title}

<!-- KIND: roundup. Cover {mn} to {mx} tools. Every vendor named here must already
     exist in config/competitors.md, with its modality and pricing taken from there,
     not from memory. Ployo goes in positioned honestly and NOT first. -->

Opening paragraph: answer the title question in the first two sentences. No throat clearing.

## What does "AI interview software" actually mean in 2026?

Answer in the first sentence underneath. Then explain the layers of the first round, because
the taxonomy is the part a model quotes.

## <Vendor name>

- **Who it is for:**
- **What it does:**
- **Pricing:**
- **One real limitation:**

<!-- Repeat the block above for every vendor, same four fields, same order. -->

## How do you choose between them?

## Sources

- Vendor claims checked against each vendor's own public pages. See config/competitors.md
  for the dates.
""",
    "comparison": """# {title}

<!-- KIND: comparison. Name both sides honestly. Do not strawman the alternative:
     a page that wins everywhere gets discounted by the model cross-checking it. -->

Answer the title question in the first two sentences.

## What is the actual difference?

## When is <option A> the right call?

## When is <option B> the right call?

## What does the evidence say?

## Sources
""",
    "compliance": """# {title}

<!-- KIND: compliance. Name the specific legislation and the specific date, and verify
     every one against the primary source before publishing. Regulators account for a
     quarter of citations in this category and precision is the whole reason a vendor
     page gets cited beside them. -->

Answer the title question in the first two sentences.

## What does the law actually require?

## When does it start?

## What does compliant AI screening look like in practice?

## Sources

- Primary legislation only. Link the actual instrument, not a law firm's summary.
""",
}


def load_queue():
    if QUEUE_PATH.exists():
        return json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    return {
        "_README": (
            "Pulse article queue. Status flow: drafting -> ready -> published. "
            "LinkedIn has no article API, so 'ready' means a human still has to paste it "
            "(see docs/PULSE-PUBLISHING.md). Target is 2 to 3 per month, rotating "
            "roundup, comparison, compliance."
        ),
        "monthly_target": MONTHLY_TARGET,
        "rotation": list(KINDS),
        "items": [],
    }


def save_queue(q):
    QUEUE_PATH.write_text(json.dumps(q, indent=2) + "\n", encoding="utf-8")


def article_path(slug):
    return ARTICLES_DIR / f"{slug}.md"


def known_vendors():
    """Vendor names that have been fact-checked, from the generated file."""
    if not COMPETITORS_PATH.exists():
        return set()
    text = COMPETITORS_PATH.read_text(encoding="utf-8")
    body = text.split("## Named in the brief but NOT fact-checked")[0]
    names = set()
    for line in body.splitlines():
        if line.startswith("## ") and not line.startswith("## How to use"):
            names.add(line[3:].strip())
    return names


def vendor_sections(text):
    """H2 headings that look like a vendor entry rather than a question."""
    out = []
    for m in re.finditer(r"^## (.+)$", text, re.M):
        heading = m.group(1).strip()
        if heading.endswith("?") or heading.lower() in ("sources", "how to use this"):
            continue
        out.append((heading, m.start()))
    return out


def section_body(text, start):
    nxt = text.find("\n## ", start + 1)
    return text[start:len(text) if nxt == -1 else nxt]


def check_article(slug):
    path = article_path(slug)
    if not path.exists():
        return {"ok": False, "failures": [{"rule": "missing", "detail": f"no draft at {path}"}], "warnings": []}

    text = path.read_text(encoding="utf-8")
    result = check_facts.check(text)
    failures, warnings = result["failures"], result["warnings"]

    queue = load_queue()
    item = next((i for i in queue["items"] if i["slug"] == slug), None)
    kind = item["kind"] if item else "roundup"

    if "<!--" in text:
        failures.append({
            "rule": "template_left_in",
            "detail": "The scaffold comments are still in the draft. Strip them before publishing.",
        })

    title_m = re.search(r"^# (.+)$", text, re.M)
    title = title_m.group(1).strip() if title_m else ""
    if not title:
        failures.append({"rule": "no_title", "detail": "Article has no H1."})
    elif kind in ("roundup", "comparison") and not re.search(r"\b20\d{2}\b", title):
        warnings.append({
            "rule": "title_year",
            "detail": "The cited examples all state the year in the title. Consider adding it.",
        })

    links = re.findall(r"ployo\.ai", text)
    if len(links) == 0:
        failures.append({"rule": "no_ployo_link", "detail": "A citation needs somewhere to land. Link ployo.ai once."})
    elif len(links) > 3:
        warnings.append({
            "rule": "many_ployo_links",
            "detail": f"{len(links)} references to ployo.ai. The brief asks for one, in the Ployo entry.",
        })

    if kind == "roundup":
        sections = vendor_sections(text)
        vendors = [h for h, _ in sections]
        known = known_vendors()

        if len(vendors) < MIN_VENDORS:
            failures.append({
                "rule": "too_few_vendors",
                "detail": f"{len(vendors)} vendor sections. The cited roundups cover {MIN_VENDORS} to {MAX_VENDORS}.",
            })
        elif len(vendors) > MAX_VENDORS:
            warnings.append({
                "rule": "many_vendors",
                "detail": f"{len(vendors)} vendor sections, more than the {MAX_VENDORS} the format usually runs.",
            })

        unchecked = [
            v for v in vendors
            if v.lower() != "ployo"
            and not any(v.lower() in k.lower() or k.lower() in v.lower() for k in known)
        ]
        if unchecked:
            failures.append({
                "rule": "unchecked_vendor",
                "detail": (
                    f"Named but never fact-checked: {', '.join(unchecked)}. Every vendor must exist in "
                    "config/competitors.md with sourced claims. Research it and re-run "
                    "tools/sync_competitors.py, or drop it from the article."
                ),
            })

        ployo_positions = [i for i, v in enumerate(vendors) if "ployo" in v.lower()]
        if not ployo_positions:
            failures.append({"rule": "ployo_absent", "detail": "Ployo is not in the roundup at all."})
        elif ployo_positions[0] == 0:
            failures.append({
                "rule": "ployo_first",
                "detail": "Ployo is listed first. A self-ranked list reads as marketing to a reader and to a model.",
            })

        for heading, start in sections:
            body = section_body(text, start).lower()
            missing = [f for f in REQUIRED_ENTRY_FIELDS if f.split()[0] not in body]
            if missing:
                failures.append({
                    "rule": "entry_structure",
                    "detail": f"'{heading}' is missing: {', '.join(missing)}. Every entry gets the same four fields.",
                })

        questions = sum(1 for m in re.finditer(r"^## .+\?$", text, re.M))
        if questions == 0:
            warnings.append({
                "rule": "no_question_headings",
                "detail": "No question-shaped H2s. They are what match a buyer's actual prompt.",
            })

    return {"ok": not failures, "failures": failures, "warnings": warnings, "kind": kind, "title": title}


def cmd_new(slug, kind, title):
    if kind not in KINDS:
        sys.exit(f"kind must be one of {KINDS}")
    path = article_path(slug)
    if path.exists():
        sys.exit(f"{path} already exists")
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(
        TEMPLATES[kind].format(title=title, mn=MIN_VENDORS, mx=MAX_VENDORS), encoding="utf-8"
    )
    q = load_queue()
    q["items"].insert(0, {
        "slug": slug, "kind": kind, "title": title,
        "status": "drafting", "created": None, "published_url": None, "published_on": None,
    })
    save_queue(q)
    print(f"scaffolded {path}\nqueued as '{kind}'. Write it, then: python3 tools/pulse.py --check {slug}")


def cmd_check(slug):
    r = check_article(slug)
    for f in r["failures"]:
        print(f"FAIL [{f['rule']}] {f['detail']}")
    for w in r["warnings"]:
        print(f"WARN [{w['rule']}] {w['detail']}")
    q = load_queue()
    for item in q["items"]:
        if item["slug"] == slug:
            item["status"] = "ready" if r["ok"] else "drafting"
    save_queue(q)
    if r["ok"]:
        print(f"\nPASS. Marked ready. Publish with: python3 tools/pulse.py --brief {slug}")
        return 0
    print("\nBLOCKED. Not publishable yet.")
    return 1


def cmd_list():
    q = load_queue()
    print(f"Pulse queue (target {q.get('monthly_target', MONTHLY_TARGET)} per month, "
          f"rotating {', '.join(q.get('rotation', KINDS))})\n")
    if not q["items"]:
        print("  empty. Start one with --new.")
        return 0
    for i in q["items"]:
        url = f"  {i['published_url']}" if i.get("published_url") else ""
        print(f"  [{i['status']:<9}] {i['kind']:<10} {i['slug']}{url}")
    published = sum(1 for i in q["items"] if i["status"] == "published")
    print(f"\n  published all time: {published}")
    return 0


def cmd_brief(slug):
    r = check_article(slug)
    if not r["ok"]:
        print("BLOCKED: run --check first and fix the failures.")
        return 1
    text = article_path(slug).read_text(encoding="utf-8")
    body = re.sub(r"^# .+\n", "", text, count=1).strip()
    print("=" * 78)
    print("PASTE INTO LINKEDIN'S ARTICLE EDITOR (linkedin.com/article/new/)")
    print("Publish from Ahmed's own browser. See docs/PULSE-PUBLISHING.md.")
    print("=" * 78)
    print(f"\nTITLE:\n{r['title']}\n")
    print("BODY:\n")
    print(body)
    print("\n" + "=" * 78)
    print(f"After publishing:\n  python3 tools/pulse.py --published {slug} --url <the article url>")
    return 0


def cmd_published(slug, url, today):
    q = load_queue()
    found = False
    for item in q["items"]:
        if item["slug"] == slug:
            item.update(status="published", published_url=url, published_on=today)
            found = True
    if not found:
        sys.exit(f"{slug} is not in the queue")
    save_queue(q)
    print(f"recorded {slug} as published at {url}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="LinkedIn Pulse article pipeline.")
    ap.add_argument("--new", metavar="SLUG")
    ap.add_argument("--kind", choices=KINDS, default="roundup")
    ap.add_argument("--title", default="")
    ap.add_argument("--check", metavar="SLUG")
    ap.add_argument("--brief", metavar="SLUG")
    ap.add_argument("--published", metavar="SLUG")
    ap.add_argument("--url", default="")
    ap.add_argument("--date", default="", help="ISO date for --published")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args(argv)

    if args.new:
        if not args.title:
            sys.exit("--new needs --title")
        return cmd_new(args.new, args.kind, args.title)
    if args.check:
        return cmd_check(args.check)
    if args.brief:
        return cmd_brief(args.brief)
    if args.published:
        if not args.url:
            sys.exit("--published needs --url")
        return cmd_published(args.published, args.url, args.date or None)
    return cmd_list()


if __name__ == "__main__":
    sys.exit(main())
