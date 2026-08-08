#!/usr/bin/env python3
"""
posting_window.py

WHY THIS EXISTS: the LinkedIn posting schedule must track the audience's
wall clock, not ours. The audience is Australia (Sydney). state/settings.json
used to hardcode posting_windows_utc as a fixed UTC array, which silently
drifted an hour twice a year: whenever Australia/Sydney crosses a daylight
saving boundary (AEST UTC+10 <-> AEDT UTC+11), a UTC-fixed window quietly
stops landing at the intended local time until someone notices and hand-edits
the array. This script makes the schedule authoritative in LOCAL time
(posting_windows_local + posting_timezone in state/settings.json) and
computes the correct UTC window for TODAY, DST-aware, on every run.
posting_windows_utc in settings.json is kept only as a stale-cache fallback.

Dependency-free: stdlib only (datetime, json, argparse). Tries zoneinfo
first; a sandbox or minimal container can be missing the tzdata database,
so a pure-Python hardcoded fallback rule for Australian east-coast zones
covers that case too.

Usage:
    python3 tools/posting_window.py                # full JSON report
    python3 tools/posting_window.py --window 1      # just window 1's UTC "HH:MM-HH:MM"
"""

import argparse
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

try:
    from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
except ImportError:  # pragma: no cover - Python < 3.9 not expected here
    ZoneInfo = None
    ZoneInfoNotFoundError = Exception

SETTINGS_PATH = Path(__file__).resolve().parent.parent / "state" / "settings.json"

# Australian zones that observe the same east-coast DST transition dates as
# Sydney (first Sunday in October -> first Sunday in April).
_AU_DST_ZONES = {
    "Australia/Sydney",
    "Australia/Melbourne",
    "Australia/Canberra",
    "Australia/Hobart",
    "Australia/ACT",
    "Australia/NSW",
    "Australia/Victoria",
    "Australia/Tasmania",
}

# Australian zones that never observe daylight saving (fixed UTC+10).
_AU_NO_DST_ZONES = {
    "Australia/Brisbane",
    "Australia/Queensland",
    "Australia/Lindeman",
}


def first_sunday(year: int, month: int) -> date:
    """Return the date of the first Sunday of `month` in `year`."""
    d = date(year, month, 1)
    # Monday=0 ... Sunday=6
    offset_days = (6 - d.weekday()) % 7
    return d + timedelta(days=offset_days)


def sydney_offset_fallback(ref_date: date) -> "tuple[int, bool]":
    """
    Pure-Python DST rule for Australia/Sydney (and equivalent east-coast
    zones), used only when zoneinfo/tzdata is unavailable.

    AEDT (UTC+11) runs from the first Sunday in October (02:00 local, clocks
    forward to 03:00) through the first Sunday in April (03:00 local, clocks
    back to 02:00). AEST (UTC+10) covers the rest of the year.

    Because the actual transition happens in the very early morning and this
    script only ever converts afternoon/evening posting windows, comparing
    at date granularity (ignoring the hour of the transition) is safe: the
    transition day itself already belongs to the new offset by the time any
    posting window (15:00 onward local) occurs.
    """
    year = ref_date.year
    sun_apr = first_sunday(year, 4)
    sun_oct = first_sunday(year, 10)
    if sun_apr <= ref_date < sun_oct:
        return 10, False  # AEST
    return 11, True  # AEDT


def brisbane_offset_fallback(ref_date: date) -> "tuple[int, bool]":
    """Australia/Brisbane never observes daylight saving: fixed UTC+10."""
    return 10, False


def resolve_offset(tz_name: str, ref_date: date) -> "tuple[int, bool]":
    """
    Resolve (utc_offset_hours, is_dst) for `tz_name` on `ref_date`.

    Tries zoneinfo.ZoneInfo first (the correct, general answer). Falls back
    to a hardcoded rule for known Australian zones if zoneinfo/tzdata is
    missing. Raises ValueError if the zone is unknown and zoneinfo failed.
    """
    if ZoneInfo is not None:
        try:
            zi = ZoneInfo(tz_name)
            probe = datetime(ref_date.year, ref_date.month, ref_date.day, 12, tzinfo=zi)
            offset = probe.utcoffset()
            if offset is None:
                raise ValueError(f"zoneinfo returned no UTC offset for {tz_name}")
            total_hours = offset.total_seconds() / 3600
            if total_hours != int(total_hours):
                raise ValueError(
                    f"non-whole-hour UTC offset for {tz_name}: {total_hours} "
                    "(not supported by this script)"
                )
            dst = probe.dst()
            is_dst = bool(dst) and dst != timedelta(0)
            return int(total_hours), is_dst
        except (ZoneInfoNotFoundError, KeyError):
            pass  # fall through to hardcoded fallback below

    if tz_name in _AU_DST_ZONES:
        return sydney_offset_fallback(ref_date)
    if tz_name in _AU_NO_DST_ZONES:
        return brisbane_offset_fallback(ref_date)

    raise ValueError(
        f"unable to resolve timezone {tz_name!r}: zoneinfo/tzdata unavailable "
        "and no hardcoded fallback rule exists for this zone"
    )


def _parse_hhmm(value: str) -> "tuple[int, int]":
    hh, mm = value.split(":")
    return int(hh), int(mm)


def convert_window_to_utc(window_str: str, ref_date: date, offset_hours: int) -> str:
    """Convert one 'HH:MM-HH:MM' local window to its UTC 'HH:MM-HH:MM' string."""
    start_str, end_str = window_str.split("-")
    start_h, start_m = _parse_hhmm(start_str)
    end_h, end_m = _parse_hhmm(end_str)

    start_local = datetime(ref_date.year, ref_date.month, ref_date.day, start_h, start_m)
    end_local = datetime(ref_date.year, ref_date.month, ref_date.day, end_h, end_m)

    delta = timedelta(hours=offset_hours)
    start_utc = start_local - delta
    end_utc = end_local - delta

    return f"{start_utc:%H:%M}-{end_utc:%H:%M}"


def build_report(tz_name: str, windows_local: "list[str]", ref_date: date = None) -> dict:
    """Build the JSON-able report dict for the given timezone/windows/date."""
    if ref_date is None:
        ref_date = datetime.now(timezone.utc).date()

    offset_hours, is_dst = resolve_offset(tz_name, ref_date)
    windows_utc = [convert_window_to_utc(w, ref_date, offset_hours) for w in windows_local]

    return {
        "timezone": tz_name,
        "utc_offset_hours": offset_hours,
        "is_dst": is_dst,
        "windows_local": windows_local,
        "windows_utc": windows_utc,
        "date_utc": ref_date.isoformat(),
    }


def load_settings(settings_path: Path = SETTINGS_PATH) -> dict:
    if not settings_path.exists():
        raise FileNotFoundError(f"settings file not found: {settings_path}")
    with settings_path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert Australia/Sydney local LinkedIn posting windows to UTC, DST-aware."
    )
    parser.add_argument(
        "--window",
        type=int,
        default=None,
        help="1-based index: print only that window's UTC 'HH:MM-HH:MM' string.",
    )
    args = parser.parse_args(argv)

    try:
        settings = load_settings()
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"posting_window.py: failed to read settings.json: {exc}", file=sys.stderr)
        return 1

    tz_name = settings.get("posting_timezone")
    windows_local = settings.get("posting_windows_local")

    if not tz_name:
        print("posting_window.py: settings.json is missing 'posting_timezone'", file=sys.stderr)
        return 1
    if not windows_local or not isinstance(windows_local, list):
        print("posting_window.py: settings.json is missing 'posting_windows_local'", file=sys.stderr)
        return 1

    try:
        report = build_report(tz_name, windows_local)
    except ValueError as exc:
        print(f"posting_window.py: {exc}", file=sys.stderr)
        return 1

    if args.window is not None:
        idx = args.window - 1
        if idx < 0 or idx >= len(report["windows_utc"]):
            print(
                f"posting_window.py: --window {args.window} out of range "
                f"(1..{len(report['windows_utc'])})",
                file=sys.stderr,
            )
            return 1
        print(report["windows_utc"][idx])
        return 0

    print(json.dumps(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
