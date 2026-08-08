import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import posting_window as pw

try:
    from zoneinfo import ZoneInfo
    HAVE_ZONEINFO = True
except ImportError:  # pragma: no cover
    HAVE_ZONEINFO = False


class TestPostingWindowConversion(unittest.TestCase):
    def test_aest_conversion_2026_08_08(self):
        report = pw.build_report(
            "Australia/Sydney",
            ["15:00-17:00", "21:00-22:30"],
            ref_date=date(2026, 8, 8),
        )
        self.assertEqual(report["utc_offset_hours"], 10)
        self.assertFalse(report["is_dst"])
        self.assertEqual(report["windows_utc"], ["05:00-07:00", "11:00-12:30"])

    def test_aedt_conversion_2026_12_15(self):
        report = pw.build_report(
            "Australia/Sydney",
            ["15:00-17:00", "21:00-22:30"],
            ref_date=date(2026, 12, 15),
        )
        self.assertEqual(report["utc_offset_hours"], 11)
        self.assertTrue(report["is_dst"])
        self.assertEqual(report["windows_utc"], ["04:00-06:00", "10:00-11:30"])

    def test_dst_boundary_october_start(self):
        # 2026-10-04 is the first Sunday of October: AEDT starts.
        before = pw.build_report(
            "Australia/Sydney", ["15:00-17:00"], ref_date=date(2026, 10, 3)
        )
        on_day = pw.build_report(
            "Australia/Sydney", ["15:00-17:00"], ref_date=date(2026, 10, 4)
        )
        self.assertEqual(before["utc_offset_hours"], 10)
        self.assertFalse(before["is_dst"])
        self.assertEqual(on_day["utc_offset_hours"], 11)
        self.assertTrue(on_day["is_dst"])

    def test_dst_boundary_april_end(self):
        # 2026-04-05 is the first Sunday of April: AEST resumes.
        before = pw.build_report(
            "Australia/Sydney", ["15:00-17:00"], ref_date=date(2026, 4, 4)
        )
        on_day = pw.build_report(
            "Australia/Sydney", ["15:00-17:00"], ref_date=date(2026, 4, 5)
        )
        self.assertEqual(before["utc_offset_hours"], 11)
        self.assertTrue(before["is_dst"])
        self.assertEqual(on_day["utc_offset_hours"], 10)
        self.assertFalse(on_day["is_dst"])

    def test_first_sunday_helper(self):
        self.assertEqual(pw.first_sunday(2026, 10), date(2026, 10, 4))
        self.assertEqual(pw.first_sunday(2026, 4), date(2026, 4, 5))

    def test_brisbane_no_dst(self):
        summer = pw.build_report(
            "Australia/Brisbane", ["15:00-17:00"], ref_date=date(2026, 12, 15)
        )
        winter = pw.build_report(
            "Australia/Brisbane", ["15:00-17:00"], ref_date=date(2026, 8, 8)
        )
        self.assertEqual(summer["utc_offset_hours"], 10)
        self.assertFalse(summer["is_dst"])
        self.assertEqual(winter["utc_offset_hours"], 10)
        self.assertFalse(winter["is_dst"])

    @unittest.skipUnless(HAVE_ZONEINFO, "zoneinfo not available on this machine")
    def test_fallback_agrees_with_zoneinfo_across_the_year(self):
        sample_dates = [
            date(2026, 1, 15),
            date(2026, 3, 1),
            date(2026, 4, 4),
            date(2026, 4, 5),
            date(2026, 4, 6),
            date(2026, 6, 21),
            date(2026, 9, 30),
            date(2026, 10, 3),
            date(2026, 10, 4),
            date(2026, 10, 5),
            date(2026, 12, 31),
            date(2027, 4, 4),
        ]
        for d in sample_dates:
            with self.subTest(date=d):
                try:
                    zi = ZoneInfo("Australia/Sydney")
                except Exception:  # pragma: no cover - missing tzdata
                    self.skipTest("tzdata for Australia/Sydney not installed")
                from datetime import datetime

                probe = datetime(d.year, d.month, d.day, 12, tzinfo=zi)
                zoneinfo_offset = int(probe.utcoffset().total_seconds() / 3600)
                zoneinfo_is_dst = bool(probe.dst()) and probe.dst().total_seconds() != 0

                fallback_offset, fallback_is_dst = pw.sydney_offset_fallback(d)

                self.assertEqual(fallback_offset, zoneinfo_offset)
                self.assertEqual(fallback_is_dst, zoneinfo_is_dst)

    def test_settings_json_round_trip(self):
        # Exercises the real repo settings.json end to end (today's date),
        # just asserting it produces well-formed HH:MM-HH:MM UTC windows.
        settings = pw.load_settings()
        tz_name = settings["posting_timezone"]
        windows_local = settings["posting_windows_local"]
        report = pw.build_report(tz_name, windows_local)
        self.assertEqual(len(report["windows_utc"]), len(windows_local))
        for w in report["windows_utc"]:
            start, end = w.split("-")
            self.assertRegex(start, r"^\d{2}:\d{2}$")
            self.assertRegex(end, r"^\d{2}:\d{2}$")


if __name__ == "__main__":
    unittest.main()
