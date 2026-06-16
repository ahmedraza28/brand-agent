# LinkedIn carousels (document posts): the OCCASIONAL framework format

**Default LinkedIn format is now TEXT-FIRST (2026-06-16 pivot).** Hook-driven text posts win the thing that matters most for a senior-buyer audience: substantive comments. Carousels win impressions, but a comment is the authority signal, and an opinion belongs in text where someone can argue with it. So the carousel is no longer the default. It is the rare, earned exception, roughly **1x/week MAX**, and ONLY when the content is a genuine framework, a data breakdown, or a step-by-step on a hiring / AI-hiring topic.

The day-to-day default lives in `config/persona.md` + `config/playbook.md` (text-first, hook-driven, ~150-300 words). This file governs the narrow case where a deck is actually the right call, plus the full production recipe for when it is.

## When to ship a carousel: read `state/settings.json` -> `linkedin_format`
**This setting governs the format decision (the routine's Step 6 defers the LinkedIn-format choice to this file).**

### `linkedin_format: "text-first"` (current policy, the default)
Most days = **no carousel**. The post is text. A carousel ships ONLY when a topic clears the **deck-worthy gate** below, AND the **once-a-week cap** is not already spent. Both must be true; when in doubt, ship text. A weak deck is worse than a strong text post, and the bias is hard toward text.

**Deck-worthy gate (ALL must hold):**
1. **It's a genuine framework, a numbered data breakdown, or a step-by-step.** Something with 4+ discrete, ordered points that a reader would actually want to save and scroll through. Not an opinion. Not a single reaction. An opinion goes in text where it can start an argument; a carousel that's really just a hot take with slide breaks is a miss.
2. **The topic is hiring or AI-x-hiring.** The state of hiring (resume/ATS theater, ghosting, time-to-hire, interview theater, screening at volume, bias), what AI actually changes for screening/interviews/scoring, or a regulation/data breakdown (NYC Local Law 144, EU AI Act, structured-vs-unstructured validity numbers, the entry-level crunch). The recruiting/hiring lens is the main subject; the AI-builder seat is where Ahmed speaks FROM. A deck on something off-topic is not deck-worthy here.
3. **Every slide is real and grounded.** Verified facts only, $ and % figures double-checked against a source fetched this run. A framework deck lives or dies on the numbers being right.

**Once-a-week cap (conservative):** at most **1 carousel per ISO week (Mon-Sun UTC)**. Before shipping a deck, grep `state/posting-log.md` for LinkedIn `LIVE` entries in the current ISO week that carry a carousel (a `document` asset / `**Kind:**` carousel marker). If one already shipped this week, the topic ships as **text**, no matter how deck-worthy. Most weeks should have zero or one carousel, never two.

**Default decision when unsure:** text. The gate is meant to fail closed. If you're talking yourself into "this could be a deck," it's a text post.

### `linkedin_format: "auto"` (legacy conditional, flippable)
Carousel whenever the take is a genuine **framework / breakdown** with 3-5 discrete points, regardless of the once-a-week cap; quick reactions stay text. Functionally close to `"text-first"` minus the weekly cap and the hiring-topic narrowing. Use only if the setting is flipped back to `"auto"`.

### `linkedin_format: "carousel"` (legacy carousel-always, DORMANT, do not assume)
The old policy where EVERY LinkedIn post shipped as a carousel deck (one per research topic, no exceptions). **Superseded by the 2026-06-16 text-first pivot.** Documented here so a flip back is one settings edit, but it is NOT the current mode; do not treat carousels as the default. If `linkedin_format` is set to `"carousel"`, every research topic becomes a deck via the standard 3-5 slide scaffold (what changed, why it matters, the nuance, what to do or watch, the open question).

## How (the routine runs the generator in the repo): UNCHANGED
The production path is the same on the rare deck day. Nothing about `make_carousel.py`, the theme rotation, or the Pages -> Buffer document-asset flow changed; only when you reach for it did.

1. Write a spec JSON (see schema) capturing the cover title, 3-5 slides, and an outro. **All text is real and rendered cleanly, get the facts right** (same grounding rules; double-check $ and % figures).
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
  "slug": "structured-interview-validity-breakdown",
  "company": null,                     // usually null for a hiring framework deck (no single company);
                                       // set it only when the deck genuinely reacts to one named org
  "domain": null,                      // logo via Google favicon (free); the brand mark, omit if no company
  "accent": "#0D9488",                 // accent hex; with no company, use a sensible brand-neutral hex
                                       // (e.g. a teal/slate). When a deck IS about one company, use its
                                       // brand color (Anthropic #CC785C, OpenAI #10A37F, Google #4285F4,
                                       // Microsoft #0078D4, Meta #0866FF, Nvidia #76B900).
  "title": "What actually predicts a good hire: the validity numbers nobody screens on",
  "handle": "Ahmed Raza",
  "slides": [
    {"heading": "short punchy point", "body": "1-2 sentences, concrete, specific"},
    {"heading": "...", "body": "..."},
    {"heading": "...", "body": "..."}
  ],
  "outro": {"heading": "the question / takeaway", "body": "a closing line", "cta": "Follow Ahmed Raza for sharp takes on hiring + AI"}
  // NOTE: do NOT set "theme", leave it out so the generator auto-rotates the look (see Themes below).
}
```
- 3-5 content slides (the deck is cover + slides + outro = 5-7 pages total). For a numbered framework, 6-10 numbered slides also reads well (numbered decks earn ~20-30% more dwell); cap around 15.
- Headings <= ~6 words; bodies <= ~2 short sentences (they wrap on the slide).
- Pick a sensible `accent`; if the deck is about a specific company, use its brand hex. If you don't know it, omit it (the generator derives one).
- Persona + guardrail rules apply to every slide: no em dashes, no bolded list labels, human voice, verified facts, never overclaim a Ployo capability or number, never internal Ployo specifics.

## Caption (the LinkedIn post text for a carousel)
Short, NOT the full essay; the deck carries the substance. Hook line (front-load it, it must stand alone above the ~140-char "see more" fold) + one line of context + a single closing line or one specific question (golden-hour comments; honor the rationed-question-closer rule from `persona.md`, max ~1 in 3). The source link goes in `firstComment`, never the body (body links cost 50-70% reach). 3-5 hashtags at the end. Still obey persona/guardrails (no em dashes, no "it's not X it's Y", human voice, verified facts).

## Themes: visual variety (auto-rotated, 2026-06-05)
The deck is not a single fixed look. `tools/make_carousel.py` carries **8 themes**, each a distinct **palette + layout** (cover composition, number style, footer style):

`midnight` (near-black), `paper` (warm cream), `blueprint` (deep navy), `brandwash` (a dark tint of the brand/accent color), `slate` (warm charcoal), `ivory` (bright white), `sand` (warm beige), `carbon` (dark gradient).

- **The generator picks the theme by anti-repeat ROTATION.** It reads/writes `state/recent-carousel-themes.json` and never reuses a theme from the last 4 decks, so consecutive decks never match. This is automatic: **just omit `theme` from the spec.** `git add -A` in Step 10 commits the updated state file so the rotation persists across runs. (Carousels are now rare, so the rotation history advances slowly; that's fine, it still guarantees the next deck differs from the last 4.)
- The **per-company / accent brand color is preserved in every theme**; the theme only controls background / text / layout. Keep passing the right `accent`.
- *Within* a single deck the look stays consistent (one theme per deck); that's intentional, variety is **across** decks.
- To pin a specific look for a one-off, set `"theme": "<name>"` in the spec (or `CAROUSEL_THEME=<name>` env). A forced theme is **not** recorded in the rotation history. Omit it in normal runs.
- The **product-spotlight** stream (`config/product-spotlight.md`) reuses this exact generator + theme rotation for its occasional LinkedIn decks: same spec schema, same `make_carousel.py`, same auto-rotated themes, same once-deck-worthy discipline.

## DORMANT: X note (revive if X returns)
X has no native document/carousel asset, so a "carousel" never applied to X; the X version of any topic always used a single rotating image (`config/styles.md`). **X is currently suspended (2026-06-14), so LinkedIn is the only live channel** and this whole file is about LinkedIn only. None of this X logic is deleted: if X is reinstated, the single-image-on-X behavior revives unchanged. Until then, ignore X here.
