# Takes — the third stream (X-only, text-only)

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

- The bank entry is a **thesis, not copy**. Develop it: pick one angle, make the argument, land it. The persona's "X voice — verdict first" section applies in full (opinion-first opener a reader can disagree with, closer rotation against the posting log, banned tics, long-form ~400-700 chars per playbook, occasional short banger).
- **TEXT-ONLY, X-ONLY.** No image (skip Step 7 for this post), no carousel, no link, no thread, never LinkedIn. The words carry it.
- A take is opinion, owned in Ahmed's voice. Guardrails still bind every FACT: if the post cites a number, study, company, or event, verify it this run or cut it. An unverifiable supporting fact never survives; a good opinion doesn't need it.
- Anchors must be **honest-generic** ("I build agents for a living", "I review an agent's output before my first coffee"), never fabricated specifics: no invented client stories, fake numbers, or made-up incidents.

## ⚠ Privacy — this repo is PUBLIC

The bank and every post must stay public-safe: never client/customer/partner names, never internal Ployo metrics, costs, or model choices, never personal finance/family/visa details. If an entry seems to need any of that to work, it does not belong in the bank.

## Logging

Slug `tk-<slug>`; the posting-log entry carries a `**Kind:** take` line. This stream does NOT count against `research_per_day` and must never block or replace a research post or spotlight. **Daily guard:** skip the step if today's (UTC) `tk-` entry count in the posting log is already >= `per_day`. Schedule its `dueAt` into the current run's window at a random minute >= 30 min apart from any other X post in that window.
