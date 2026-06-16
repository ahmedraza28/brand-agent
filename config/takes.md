# Takes — the third stream (X-only, text-only)

## ⚠ DORMANT — standalone takes stream (X suspended 2026-06-14, revivable if X returns)

The standalone takes stream is **OFF** (`state/settings.json` → `takes.enabled=false`). X is suspended; this stream is X-only and has no live channel to publish to. **Do not produce standalone takes posts while X is dormant.** Keep this file intact: the stream revives as-is if the X account is reinstated and `takes.enabled` is set back to `true`.

**Important: the opinion bank (`state/opinion-bank.json`) is NOT dormant.** Even while this stream is off, the bank's entries are consumed by the **live LinkedIn research stream** as its slow-day fallback (see `config/sources.md` → "Slow-day fallback"). A slow-day bank take publishes to **LinkedIn** as a normal text post under the standard LinkedIn voice rules. The "TEXT-ONLY, X-ONLY. Never LinkedIn." line in the Drafting section below applies ONLY to the dormant standalone takes stream, NOT to the bank's current use as the LinkedIn slow-day fallback. For slow-day publishing mechanics and the LinkedIn publish target, read `config/sources.md`; read this file for the bank selection rules (LRU pick, 14-day reuse guard, fresh-angle-on-reuse).

---

Ahmed's strongest opinions, posted on their own. No news hook required, no image, no link, no thread. This stream exists to grow followers and build a community around a worldview: research posts and spotlights react to events; takes ARE the content. People follow a person with positions, not a news feed.

Governed by `state/settings.json` → `takes`:
- `enabled` (bool) — master on/off for this stream.
- `per_day` (int, default 1) — max take posts per UTC day.
- `run` — which daily run produces it: `"first"` (the 00:30 UTC run), `"second"` (the 12:30 UTC run), or `"any"` (both runs eligible; needed if per_day is 2).

## Source — the opinion bank (`state/opinion-bank.json`)

Every take starts from a real, pre-approved belief of Ahmed's stored in the bank. **NEVER invent a new opinion** — pick from the bank. Ahmed adds/edits entries by hand. If a genuinely great new opinion emerges from the day's events, SUGGEST it in the Step 11 run report; do not add it to the bank yourself.

- Pick the **least-recently-used** entry (oldest `last_used`; `null` = never used = highest priority). If today's AI-builder discourse genuinely connects to a different entry, prefer that one instead — but never force a connection.
- **Never reuse an entry within 14 days.** On any reuse, a FRESH angle is mandatory: the bank's `take` line is the belief, not the copy. Skim the entry's previous posts in `state/posting-log.md` (`tk-` slugs) and come at it from a different door.
- After posting, update the chosen entry's `last_used` (ISO date) and `times_used`, and commit the bank with the rest of the run.

## Drafting

- The bank entry is a **thesis, not copy**. Develop it: pick one angle, make the argument, land it. The persona's "X voice — verdict first" section applies in full (opinion-first opener a reader can disagree with, closer rotation against the posting log, banned tics).
- **Length: a single tight post, 180-280 chars. Never a thread, never long-form.** A take is one punch; pagination dilutes it, and the banger format is what gets screenshotted and quoted. If the draft runs long, the angle is too broad: cut to the sharpest claim. (Decided 2026-06-11 after the first take's 280-char fallback version beat its 543-char draft.)
- **TEXT-ONLY, X-ONLY** (for the standalone takes stream). No image (skip Step 7 for this post), no carousel, no link, no thread. This "never LinkedIn" rule applies to the standalone takes stream only. The opinion bank is separately consumed as the LinkedIn slow-day fallback (see `config/sources.md`); that path publishes to LinkedIn under the standard LinkedIn voice, not this stream's format. The words carry it.
- A take is opinion, owned in Ahmed's voice. Guardrails still bind every FACT: if the post cites a number, study, company, or event, verify it this run or cut it. An unverifiable supporting fact never survives; a good opinion doesn't need it.
- Anchors must be **honest-generic** ("I build agents for a living", "I review an agent's output before my first coffee"), never fabricated specifics: no invented client stories, fake numbers, or made-up incidents.

## ⚠ Privacy — this repo is PUBLIC

The bank and every post must stay public-safe: never client/customer/partner names, never internal Ployo metrics, costs, or model choices, never personal finance/family/visa details. If an entry seems to need any of that to work, it does not belong in the bank.

## Logging

Slug `tk-<slug>`; the posting-log entry carries a `**Kind:** take` line. This stream does NOT count against `research_per_day` and must never block or replace a research post or spotlight. **Daily guard:** skip the step if today's (UTC) `tk-` entry count in the posting log is already >= `per_day`. Schedule its `dueAt` into the current run's window at a random minute >= 30 min apart from any other X post in that window.
