#!/usr/bin/env python3
"""Tests for the carousel theme-rotation logic (the anti-repeat selector + state I/O).
Rendering itself is verified visually; this covers the deterministic selection rules.

Run:  python3 tests/test_carousel_themes.py
"""
import os, sys, json, tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
import make_carousel as mc


def check(name, cond):
    print(("PASS" if cond else "FAIL"), name)
    if not cond:
        raise SystemExit(f"FAILED: {name}")


# --- theme catalog sanity ---
names = [t["name"] for t in mc.THEMES]
check("at least 8 themes", len(mc.THEMES) >= 8)
check("theme names unique", len(names) == len(set(names)))
check("every theme has bg/fg/cover/num/footer", all(
    all(k in t for k in ("name", "bg", "fg", "cover", "num", "footer")) for t in mc.THEMES))

# --- anti-repeat: never pick a theme inside the avoid window ---
recent = names[:mc.AVOID]                      # last AVOID themes used
picks = {mc.pick_theme(recent, seed=f"slug-{i}")["name"] for i in range(40)}
check("pick avoids the recent window", picks.isdisjoint(set(recent)))

# --- deterministic for a given seed (idempotent re-runs) ---
a = mc.pick_theme([], seed="nvidia-open-model")["name"]
b = mc.pick_theme([], seed="nvidia-open-model")["name"]
check("pick is deterministic per seed", a == b)

# --- different seeds spread across themes (not all identical) ---
spread = {mc.pick_theme([], seed=f"topic-{i}")["name"] for i in range(60)}
check("pick spreads across multiple themes", len(spread) >= 4)

# --- degrade gracefully when the whole catalog is in the recent window ---
got = mc.pick_theme(names, seed="x")           # everything recently used
check("falls back to a valid theme when all recent", got["name"] in names)

# --- state I/O: missing file -> [], save trims to the window ---
with tempfile.TemporaryDirectory() as d:
    p = os.path.join(d, "recent-carousel-themes.json")
    check("missing state -> empty recent", mc.load_recent(p) == [])
    for nm in names + names:                   # write more than the keep window
        mc.save_recent(p, nm)
    kept = mc.load_recent(p)
    check("state persists last entries", kept[-1] == names[-1])
    check("state trims to keep window", len(kept) <= mc.KEEP)
    check("state file is valid json", isinstance(json.load(open(p)).get("recent"), list))

# --- corrupt state file -> [] (never crashes the render) ---
with tempfile.TemporaryDirectory() as d:
    p = os.path.join(d, "recent-carousel-themes.json")
    open(p, "w").write("{ not json")
    check("corrupt state -> empty recent", mc.load_recent(p) == [])

print("\nALL THEME-ROTATION TESTS PASSED")
