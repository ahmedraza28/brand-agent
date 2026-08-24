"""
Tests for the approved-facts pack and the publish gate.

The point of these is narrow and important: prove that an invented number
cannot pass the gate, and that an ordinary number like a year or a list size
does not trip it. A gate that fails constantly gets switched off, and a gate
that passes fabrications is worse than no gate at all.
"""

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import check_facts  # noqa: E402
import stats_pack  # noqa: E402


class TestStatsPack(unittest.TestCase):
    def setUp(self):
        self.pack = stats_pack.load_pack()

    def test_pack_is_valid(self):
        self.assertEqual(stats_pack.validate(self.pack), [])

    def test_the_four_headline_figures_are_present_and_exact(self):
        values = stats_pack.publishable_values(self.pack)
        self.assertEqual(values["interviews_completed"]["display"], "30,000+")
        self.assertEqual(values["answers_graded"]["display"], "340,000+")
        self.assertEqual(values["completion_rate"]["display"], "70%+")
        self.assertEqual(values["recruiter_hours_saved"]["display"], "15,000+")

    def test_no_findings_are_publishable_until_measured(self):
        findings = self.pack["findings"]["items"]
        self.assertEqual(findings, [], "a finding reached the pack without a real measurement")

    def test_unverified_status_is_rejected_by_validation(self):
        bad = json.loads(json.dumps(self.pack))
        bad["figures"].append({
            "id": "made_up",
            "kind": "numeric",
            "display": "99%",
            "value": 99,
            "label": "invented",
            "status": "mock",
            "source": "nowhere",
        })
        problems = stats_pack.validate(bad)
        self.assertTrue(any("made_up" in p for p in problems))


class TestPublishGate(unittest.TestCase):
    def setUp(self):
        self.pack = stats_pack.load_pack()

    def run_check(self, text):
        return check_facts.check(text, pack=self.pack)

    def test_approved_figures_pass(self):
        text = "We have run 30,000+ AI interviews across 23 languages. ployo.ai"
        result = self.run_check(text)
        self.assertTrue(result["ok"], result["failures"])

    def test_unapproved_percentage_stated_as_ours_is_blocked(self):
        result = self.run_check("Our completion rate is 91% and rising. Ployo, ployo.ai")
        self.assertFalse(result["ok"])
        self.assertIn("unapproved_own_number", [f["rule"] for f in result["failures"]])

    def test_years_and_small_counts_do_not_trip_the_gate(self):
        text = (
            "The Aged Care Act 2024 applies, and the ADM disclosure obligation starts "
            "10 December 2026. We compared 9 tools. Ployo, ployo.ai"
        )
        result = self.run_check(text)
        self.assertTrue(result["ok"], result["failures"])

    def test_em_dash_is_blocked(self):
        result = self.run_check("Hiring is broken — and AI did not fix it. Ployo ployo.ai")
        self.assertFalse(result["ok"])
        self.assertIn("em_dash", [f["rule"] for f in result["failures"]])

    def test_audio_product_language_about_us_is_blocked(self):
        result = self.run_check("Our phone screening tool is fast. Ployo ployo.ai")
        self.assertFalse(result["ok"])
        self.assertIn("banned_product_term", [f["rule"] for f in result["failures"]])

    def test_audio_language_describing_a_competitor_is_allowed(self):
        """A roundup has to describe a rival's phone screening accurately. The
        ban is on calling OUR product audio, not on the words existing."""
        text = (
            "Humanly added automated phone screening through an acquisition.\n\n"
            "Ployo runs a live video interview instead. ployo.ai"
        )
        result = self.run_check(text)
        self.assertTrue(result["ok"], result["failures"])
        self.assertIn("audio_term_elsewhere", [w["rule"] for w in result["warnings"]])

    def test_borrowed_opener_without_our_own_data_is_blocked(self):
        text = "A new iCIMS report says applications are up. My take: hiring teams are drowning."
        result = self.run_check(text)
        self.assertIn("borrowed_opener", [f["rule"] for f in result["failures"]])

    def test_borrowed_opener_is_allowed_when_we_add_our_own_figure(self):
        text = (
            "A new iCIMS report says applications are up. Across 30,000+ AI interviews we see "
            "the same thing from the other side. Ployo, ployo.ai"
        )
        result = self.run_check(text)
        self.assertNotIn("borrowed_opener", [f["rule"] for f in result["failures"]])

    def test_third_party_number_is_allowed_when_credited(self):
        """The distinction the whole gate rests on: someone else's published
        number, credited to them, is not a fabrication risk and must pass."""
        text = (
            "Across 30,000+ AI interviews we watch this from the other side.\n\n"
            "Resume Builder surveyed 1,000 recent grads. 34% had an offer pulled back after "
            "they had already said yes.\n\nThat number bothers me. Ployo, ployo.ai"
        )
        result = self.run_check(text)
        self.assertTrue(result["ok"], result["failures"])
        self.assertEqual(result["third_party_numbers"], 2)

    def test_same_number_claimed_as_ours_is_blocked(self):
        text = "In our data, 34% of candidates had an offer pulled back. Ployo, ployo.ai"
        result = self.run_check(text)
        self.assertFalse(result["ok"])
        self.assertIn("unapproved_own_number", [f["rule"] for f in result["failures"]])

    def test_unattributed_percentage_is_blocked(self):
        result = self.run_check("Roughly 47% of screening happens before a human looks.")
        self.assertFalse(result["ok"])
        self.assertIn("unattributed_percentage", [f["rule"] for f in result["failures"]])

    def test_borrowed_data_only_warns(self):
        text = "A Gartner study found 61% of teams use AI screening.\n\nMy read: that is early."
        result = self.run_check(text)
        self.assertIn("borrowed_data_only", [w["rule"] for w in result["warnings"]])

    def test_missing_ployo_mention_warns_but_does_not_block(self):
        result = self.run_check("Hiring is hard and getting harder.")
        self.assertTrue(result["ok"])
        self.assertIn("no_ployo_mention", [w["rule"] for w in result["warnings"]])


class TestMockFindingsCannotBePublished(unittest.TestCase):
    """The whole reason the mock file is allowed to exist."""

    @classmethod
    def setUpClass(cls):
        stats_pack.write_mock()

    def test_every_mock_value_is_blocked_by_the_gate(self):
        mock = stats_pack.load_mock()
        self.assertIsNotNone(mock)
        checked = 0
        for item in mock["items"]:
            if item.get("value") is None:
                continue
            checked += 1
            display = item["display"]
            text = f"In our data, {display} of candidates behave this way. Ployo, ployo.ai"
            result = check_facts.check(text)
            self.assertFalse(
                result["ok"],
                f"mock finding {item['id']} ({display}) passed the gate",
            )
            self.assertIn("mock_value", [f["rule"] for f in result["failures"]])
        self.assertGreater(checked, 0)

    def test_mock_file_is_gitignored(self):
        gitignore = (ROOT / ".gitignore").read_text()
        self.assertIn("state/stats-pack.mock.json", gitignore)

    def test_mock_items_are_all_marked_unpublishable(self):
        mock = stats_pack.load_mock()
        for item in mock["items"]:
            self.assertEqual(item["status"], "mock")
            self.assertFalse(item["publishable"])
            self.assertIsNone(item["measured_on"])


if __name__ == "__main__":
    unittest.main()
