# LinkedIn carousels (document posts) — the high-leverage format

Research: document/carousel posts are LinkedIn's **top format (+39% reach, +30% engagement) and <5% of creators use them.** This is the highest-ROI LinkedIn format, so it is now the **default** for every LinkedIn post.

## When to use a carousel — read `state/settings.json` → `linkedin_format`
**This setting governs the format decision (the routine's Step 6 defers the LinkedIn-format choice to this file).**

- **`linkedin_format: "carousel"` (current policy):** EVERY LinkedIn post ships as a carousel — **no exceptions, even for one-thought reactions.** The daily target is **one carousel per research topic**, so with `research_per_day: 2` you publish a **guaranteed 2 LinkedIn carousels per day.** This means every research topic must reach LinkedIn — honor Step 5's cross-post rule (each topic → ALL channels); do not split topics one-per-channel. X always uses a single image (X has no native carousel); only the LinkedIn version becomes a carousel.
  - **Thin / reaction topic?** Don't skip the carousel — structure it into the standard **3-5 slide scaffold**: what changed → why it matters → the nuance / counterpoint → what to do or watch → the open question. Every slide stays grounded (verified facts only; double-check $ figures). A real reaction still has 3-5 honest angles; find them rather than padding.
- **`linkedin_format: "auto"` (legacy conditional):** carousel only when the take is a genuine **framework / breakdown** with 3-5 discrete points; quick reactions use a single image. Use this only if the setting is flipped back.

## How (the routine runs the generator in the repo)
1. Write a spec JSON (see schema) capturing the cover title, 3-5 slides, and an outro. **All text is real and rendered cleanly — get the facts right** (same grounding rules; double-check $ figures).
2. Install Pillow if needed, then run the generator:
   ```bash
   pip install -q pillow 2>/dev/null
   python3 tools/make_carousel.py /tmp/spec.json docs/carousels
   ```
   It writes `docs/carousels/<slug>.pdf` (the deck) + `docs/carousels/<slug>.png` (cover thumbnail).
3. `git add` both, commit, push. Poll the PDF URL until HTTP 200 (Pages lag), same as images:
   `https://ahmedraza28.github.io/brand-agent/carousels/<slug>.pdf`
4. Publish the LinkedIn post with a **document asset** (Step 9):
   `assets:[{document:{url:"<pdf url>", title:"<deck title>", thumbnailUrl:"<png url>"}}]`
   plus a **short caption** (see below) and the `firstComment` source link.

## Spec JSON schema
```json
{
  "slug": "anthropic-ipo-builders",
  "company": "Anthropic",
  "domain": "anthropic.com",          // logo via Google favicon (free); the brand mark
  "accent": "#CC785C",                // the company's BRAND color hex (you know these:
                                      // Anthropic #CC785C, OpenAI #10A37F, Nvidia #76B900,
                                      // Google #4285F4, Microsoft #0078D4, Uber #000000→use #1A1A1A,
                                      // Meta #0866FF, xAI #111111→use a slate, Mistral #FA5212)
  "title": "What Anthropic's $965B IPO actually changes if you build on Claude",
  "handle": "Ahmed Raza",
  "slides": [
    {"heading": "short punchy point", "body": "1-2 sentences, concrete, specific"},
    {"heading": "...", "body": "..."},
    {"heading": "...", "body": "..."}
  ],
  "outro": {"heading": "the question / takeaway", "body": "a closing line", "cta": "Follow Ahmed Raza for builder takes on AI"}
  // NOTE: do NOT set "theme" — leave it out so the generator auto-rotates the look (see Themes below).
}
```
- 3-5 content slides (the deck is cover + slides + outro = 5-7 pages total).
- Headings ≤ ~6 words; bodies ≤ ~2 short sentences (they wrap on the slide).
- Pick a sensible `accent` brand hex; if you don't know it, omit it (the generator derives one).

## Caption (the LinkedIn post text for a carousel)
Short, NOT the full essay — the deck carries the substance. Hook line + one line of context + **end with a question** (golden-hour comments). The source link goes in `firstComment`. 1-3 hashtags. Still obey persona/guardrails (no em-dashes, human voice, verified facts).

## Themes — visual variety (auto-rotated, 2026-06-05)
The deck is no longer a single fixed black look. `tools/make_carousel.py` carries **8 themes**, each a distinct **palette + layout** (cover composition, number style, footer style):

`midnight` (near-black) · `paper` (warm cream) · `blueprint` (deep navy) · `brandwash` (a dark tint of the brand color) · `slate` (warm charcoal) · `ivory` (bright white) · `sand` (warm beige) · `carbon` (dark gradient).

- **The generator picks the theme by anti-repeat ROTATION** — it reads/writes `state/recent-carousel-themes.json` and never reuses a theme from the last 4 decks, so consecutive decks (incl. the 2/day) never match. This is automatic: **just omit `theme` from the spec.** `git add -A` in Step 10 commits the updated state file so the rotation persists across runs.
- The **per-company brand accent is preserved in every theme** (NVIDIA green, Anthropic rust, …); the theme only controls background / text / layout. Keep passing the right `accent`.
- *Within* a single deck the look stays consistent (one theme per deck) — that's intentional; variety is **across** decks.
- To pin a specific look for a one-off, set `"theme": "<name>"` in the spec (or `CAROUSEL_THEME=<name>` env). A forced theme is **not** recorded in the rotation history. Omit it in normal runs.
- Carousel-vs-single-image: with `linkedin_format: "carousel"` every LinkedIn post is a carousel (see top of this file); X still uses a rotating single image (`config/styles.md`).
- The **product-spotlight** stream (`config/product-spotlight.md`) reuses this exact generator + theme rotation for its occasional LinkedIn decks — same spec schema, same `make_carousel.py`, same auto-rotated themes.
