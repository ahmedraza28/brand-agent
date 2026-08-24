"""
Tests for the Pulse article pipeline.

The checks here are the difference between a roundup that gets cited and one a
reader discards after verifying a single detail. Each test corresponds to a
mistake that would cost us the citation, so they are written as mutations of a
known-good article rather than as isolated fixtures.
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import pulse  # noqa: E402

SLUG = "unittest-roundup"
ARTICLE = ROOT / "docs" / "articles" / f"{SLUG}.md"


def entry(name, extra=""):
    return (
        f"## {name}\n\n"
        f"- **Who it is for:** stated\n"
        f"- **What it does:** stated\n"
        f"- **Pricing:** Not published\n"
        f"- **One real limitation:** stated\n{extra}\n"
    )


def build(vendors, ployo_at=4, ployo_body="high-volume frontline hiring", link=True):
    parts = [
        "# Best AI interview software for care and health hiring in 2026",
        "",
        "The short answer is in this sentence.",
        "",
        "## What does AI interview software actually mean in 2026?",
        "",
        "Answer in the first sentence underneath.",
        "",
    ]
    for i, v in enumerate(vendors):
        if i == ployo_at:
            parts.append(
                f"## Ployo\n\n- **Who it is for:** {ployo_body}\n"
                "- **What it does:** AI video interviewing\n"
                "- **Pricing:** Not published\n"
                "- **One real limitation:** no published independent audit\n"
                + ("\nMore at ployo.ai\n" if link else "\n")
            )
        parts.append(entry(v))
    parts += ["## How do you choose between them?", "", "Answer.", "", "## Sources", "", "Vendor pages."]
    return "\n".join(parts)


class TestRoundupChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.known = sorted(v for v in pulse.known_vendors() if v != "Ployo")
        if len(cls.known) < 8:
            raise unittest.SkipTest("config/competitors.md has too few vendors to build a fixture")
        cls.vendors = cls.known[:8]

    def setUp(self):
        ARTICLE.parent.mkdir(parents=True, exist_ok=True)
        q = pulse.load_queue()
        if not any(i["slug"] == SLUG for i in q["items"]):
            q["items"].insert(0, {"slug": SLUG, "kind": "roundup", "title": "t",
                                  "status": "drafting", "created": None,
                                  "published_url": None, "published_on": None})
            pulse.save_queue(q)

    def tearDown(self):
        ARTICLE.unlink(missing_ok=True)
        q = pulse.load_queue()
        q["items"] = [i for i in q["items"] if i["slug"] != SLUG]
        pulse.save_queue(q)

    def rules_for(self, text):
        ARTICLE.write_text(text, encoding="utf-8")
        return sorted({f["rule"] for f in pulse.check_article(SLUG)["failures"]})

    def test_a_well_formed_roundup_passes(self):
        self.assertEqual(self.rules_for(build(self.vendors)), [])

    def test_a_vendor_nobody_fact_checked_is_refused(self):
        text = build(self.vendors).replace(f"## {self.vendors[0]}", "## Wonderlic")
        self.assertIn("unchecked_vendor", self.rules_for(text))

    def test_ployo_cannot_be_listed_first(self):
        self.assertIn("ployo_first", self.rules_for(build(self.vendors, ployo_at=0)))

    def test_ployo_must_appear_at_all(self):
        self.assertIn("ployo_absent", self.rules_for(build(self.vendors, ployo_at=99)))

    def test_every_entry_needs_the_same_four_fields(self):
        text = build(self.vendors).replace("- **Pricing:** Not published\n", "", 1)
        self.assertIn("entry_structure", self.rules_for(text))

    def test_a_thin_roundup_is_refused(self):
        self.assertIn("too_few_vendors", self.rules_for(build(self.vendors[:3])))

    def test_a_citation_needs_somewhere_to_land(self):
        self.assertIn("no_ployo_link", self.rules_for(build(self.vendors, link=False)))

    def test_an_invented_statistic_about_us_is_refused(self):
        """The failure that would end the channel: a number we made up, in an
        article otherwise full of properly sourced competitor facts."""
        text = build(self.vendors, ployo_body="we screen 41% faster than the alternatives")
        self.assertIn("unapproved_own_number", self.rules_for(text))

    def test_an_approved_figure_is_allowed(self):
        text = build(self.vendors, ployo_body="high-volume hiring, across 30,000+ AI interviews")
        self.assertEqual(self.rules_for(text), [])

    def test_scaffold_alone_never_passes(self):
        text = pulse.TEMPLATES["roundup"].format(title="t", mn=7, mx=12)
        self.assertIn("template_left_in", self.rules_for(text))


class TestKnownVendors(unittest.TestCase):
    def test_unchecked_vendors_are_excluded_from_the_known_set(self):
        """Vendors listed under 'Named in the brief but NOT fact-checked' must
        not count as known, or the gate would wave them through."""
        known = pulse.known_vendors()
        self.assertNotIn("Hireflix", known)
        self.assertIn("HireVue", known)


if __name__ == "__main__":
    unittest.main()
