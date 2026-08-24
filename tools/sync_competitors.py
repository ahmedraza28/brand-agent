#!/usr/bin/env python3
"""
sync_competitors.py

WHY THIS EXISTS: the Pulse roundup only gets cited if the competitor entries
are accurate. A list that flatters Ployo is skipped by a model cross-checking
it, and a list with a wrong price or a wrong modality is worse than no list.
So the brand agent does not describe competitors from memory. It reads a
generated file, and that file is derived from the /compare cluster in
ployo-landing, where every claim already traces to the vendor's own page with
the date it was checked.

HOW IT WORKS: dumps COMPARE_PAGES from ployo-landing via npx tsx, then writes
config/competitors.md. Run it locally when the compare cluster changes. It is
NOT part of the cloud routine: the routine only clones brand-agent and has no
access to the landing repo, which is exactly why the derived file is committed.

  python3 tools/sync_competitors.py
  python3 tools/sync_competitors.py --landing /path/to/ployo-landing

⚠ A competitor NOT in the output has not been fact-checked by anyone. Do not
let the agent write about it from general knowledge. Research it, add it to the
compare cluster with sources, and re-run this.
"""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = ROOT / "config" / "competitors.md"
DEFAULT_LANDING = Path("/Users/ahmed/Documents/Codes/all-Vettio/ployo-landing")

DUMP_TS = """
import {{ COMPARE_PAGES }} from "{data_path}";
const out = COMPARE_PAGES.map((p: any) => ({{
  slug: p.slug, layer: p.layer, stance: p.stance, kind: p.kind,
  competitor: p.competitor, competitorB: p.competitorB,
  verdict: p.verdict,
  whereTheyWin: p.whereTheyWin || [],
  theWedge: p.theWedge || "",
  atAGlance: (p.atAGlance || []).map((r: any) => ({{ dimension: r.dimension, cells: r.cells }})),
  sources: (p.sources || []).map((s: any) => ({{ label: s.label, url: s.url, verifiedOn: s.verifiedOn }})),
  updated: p.updated,
}}));
console.log(JSON.stringify(out));
"""


def dump_compare_pages(landing: Path):
    data_path = landing / "src/modules/PloyoLandingPageV3/data/comparePages"
    if not Path(str(data_path) + ".ts").exists():
        sys.exit(f"compare data not found at {data_path}.ts")
    with tempfile.NamedTemporaryFile("w", suffix=".ts", delete=False) as fh:
        fh.write(DUMP_TS.format(data_path=data_path))
        script = fh.name
    proc = subprocess.run(
        ["npx", "tsx", script], cwd=landing, capture_output=True, text=True
    )
    if proc.returncode != 0:
        sys.exit(f"tsx dump failed:\n{proc.stderr[:800]}")
    return json.loads(proc.stdout)


def first_cell(rows, *needles):
    """The competitor's cell for the first at-a-glance row matching a needle."""
    for row in rows:
        dim = (row.get("dimension") or "").lower()
        if any(n in dim for n in needles):
            cells = row.get("cells") or []
            if cells:
                return cells[0]
    return None


def two_sentences(text, limit=460):
    """The compare-cluster verdicts run long. The agent reads this file on every
    roundup, so keep the quotable core and leave the rest on the page."""
    text = " ".join(text.split())
    out = []
    for chunk in text.split(". "):
        out.append(chunk)
        joined = ". ".join(out)
        if len(out) >= 2 or len(joined) > limit:
            break
    joined = ". ".join(out).rstrip(".")
    return joined + ". Full reasoning on the compare page."


# Named in the LinkedIn brief but NOT in the compare cluster, so nobody has
# fact-checked them. Listed explicitly so the agent treats their absence as a
# blocker rather than an invitation to write from general knowledge.
BRIEF_NAMED_VENDORS = [
    "HireVue", "Sapia.ai", "Paradox", "Spark Hire", "Willo",
    "HeyMilo", "VidCruiter", "Humanly", "Hireflix", "Vervoe",
]


def render(pages):
    versus = [p for p in pages if p["kind"] == "versus" and p.get("competitor")]
    versus.sort(key=lambda p: p["competitor"]["name"].lower())
    others = [p for p in pages if p["kind"] != "versus"]

    stale = sorted({s["verifiedOn"] for p in pages for s in p["sources"] if s.get("verifiedOn")})

    out = []
    w = out.append
    w("# Competitors, as they actually are")
    w("")
    w("**GENERATED FILE. Do not hand-edit.** Produced by `tools/sync_competitors.py` from the")
    w("`/compare` cluster in ployo-landing, where every claim below traces to the vendor's own")
    w("public page with the date it was checked. Re-run the script after the cluster changes.")
    w("")
    w("## How to use this")
    w("")
    w("The Pulse roundup and every comparison post draw their competitor facts from here and")
    w("nowhere else. Three rules, and all three are about getting cited rather than about manners:")
    w("")
    w("1. **Describe them accurately, including what they are genuinely better at.** Every entry")
    w("   below carries a real \"where they win\". Use it. A model answering \"is Ployo better than X\"")
    w("   cross-checks, and a list that wins everywhere loses to one that concedes. The conceding")
    w("   sentence is the one that gets quoted, with our name attached to it.")
    w("2. **Never claim we have video and they do not.** Most of this market is voice-only and")
    w("   markets itself as \"AI video interviews\" because the candidate's camera is on. The")
    w("   distinction is real and worth drawing, which is exactly why it has to be accurate in both")
    w("   directions, including where a rival genuinely does have video. The modality line below is")
    w("   the checked answer.")
    w("3. **A vendor not listed here has not been fact-checked by anyone.** Do not write about it")
    w("   from general knowledge, and do not guess a price. Where a vendor does not publish pricing,")
    w("   say \"not published\". That is a finding, not a gap to fill.")
    w("")
    w("Ployo goes in the roundup positioned honestly, on what it actually does, and **not at number")
    w("one**. A self-ranked list reads as marketing to a reader and to a model.")
    w("")
    w(f"Vendors fact-checked here: **{len(versus)}**. Sources last verified between "
      f"{stale[0]} and {stale[-1]}." if stale else "")
    w("")
    w("---")
    w("")

    for p in versus:
        c = p["competitor"]
        rows = p["atAGlance"]
        w(f"## {c['name']}")
        w("")
        w(f"- **What it is:** {c.get('oneLiner', '').strip()}")
        w(f"- **Modality:** {c.get('modality', 'unknown')}")
        w(f"- **HQ:** {c.get('hq', 'unknown')}")
        w(f"- **Pricing:** {c.get('pricing', 'Not published')}")
        who = first_cell(rows, "who it", "best for", "buyer", "fit")
        if who:
            w(f"- **Who it is for:** {who}")
        w(f"- **Site:** {c.get('url', '')}")
        w("")
        if p.get("whereTheyWin"):
            w("**Where they genuinely win** (use at least one of these when you name them):")
            w("")
            for line in p["whereTheyWin"][:3]:
                w(f"- {line.strip()}")
            w("")
        if p.get("verdict"):
            w(f"**The honest bottom line:** {two_sentences(p['verdict'])}")
            w("")
        srcs = p["sources"][:3]
        if srcs:
            checked = srcs[0].get("verifiedOn", "")
            w(f"*Checked {checked}. Sources: " + ", ".join(s["url"] for s in srcs) + "*")
        w("")
        w(f"*Full comparison: https://ployo.ai/compare/{p['slug']}*")
        w("")

    covered = " ".join(p["competitor"]["name"].lower() for p in versus)
    missing = [v for v in BRIEF_NAMED_VENDORS if v.split()[0].lower() not in covered]
    if missing:
        w("---")
        w("")
        w("## Named in the brief but NOT fact-checked")
        w("")
        w("The LinkedIn brief asks the roundup to cover these, and no page in the compare cluster")
        w("carries sourced claims about them:")
        w("")
        for v in missing:
            w(f"- **{v}**")
        w("")
        w("**Do not write about them from general knowledge.** Either research each one against its")
        w("own public pages first and add it to the compare cluster, or ship the roundup covering only")
        w("the vendors above and say plainly which tools it does not cover. A roundup that is honest")
        w("about its scope is citable. One with an invented price or a wrong modality is not, and one")
        w("wrong detail is enough for a reader to discard the whole list.")
        w("")

    if others:
        w("---")
        w("")
        w("## Also covered by the compare cluster")
        w("")
        w("These are not head-to-head pages, so they carry no \"where they win\" block. Read the page")
        w("before writing about the vendor.")
        w("")
        for p in others:
            name = p["competitor"]["name"] if p.get("competitor") else p["slug"]
            second = f" vs {p['competitorB']['name']}" if p.get("competitorB") else ""
            w(f"- **{name}{second}** ({p['stance']}): https://ployo.ai/compare/{p['slug']}")
        w("")

    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Regenerate config/competitors.md from the compare cluster.")
    ap.add_argument("--landing", default=str(DEFAULT_LANDING), help="path to the ployo-landing repo")
    args = ap.parse_args(argv)

    pages = dump_compare_pages(Path(args.landing))
    OUT_PATH.write_text(render(pages), encoding="utf-8")
    versus = sum(1 for p in pages if p["kind"] == "versus")
    print(f"wrote {OUT_PATH} from {len(pages)} compare pages ({versus} fact-checked head-to-heads)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
