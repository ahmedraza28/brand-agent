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
}
```
- 3-5 content slides (the deck is cover + slides + outro = 5-7 pages total).
- Headings ≤ ~6 words; bodies ≤ ~2 short sentences (they wrap on the slide).
- Pick a sensible `accent` brand hex; if you don't know it, omit it (the generator derives one).

## Caption (the LinkedIn post text for a carousel)
Short, NOT the full essay — the deck carries the substance. Hook line + one line of context + **end with a question** (golden-hour comments). The source link goes in `firstComment`. 1-3 hashtags. Still obey persona/guardrails (no em-dashes, human voice, verified facts).

## Anti-repeat
The carousel template is intentionally consistent *within* a deck. Variety across posts comes from the per-company **accent + logo**, and from alternating carousel vs single-image vs text. Don't make every LinkedIn post a carousel.
