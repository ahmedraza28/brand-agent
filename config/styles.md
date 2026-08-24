# Image style — editorial PHOTOGRAPHY, one locked treatment

⚠⚠ **DIRECTION CHANGED 2026-08-24. The cream infographic template is DEAD. Do not render charts.**

Ahmed reviewed a month of posts in Buffer and rejected the whole look: cream background, serif
headline with a teal underline, funnel and check/x diagrams, big percentage, dark punchline pill.
His words: "I don't care about infographics." Every post rendered that way is retired as a template.
Do not revive it, do not produce a "lighter" version of it, do not fall back to it on a data post.

**What replaces it:** a real editorial PHOTOGRAPH with a restrained type treatment over it. The look
to match is the cover published on the 2026-08-24 Pulse article: a documentary photograph of an
aged-care worker mid-conversation, a dark teal panel over one third, a short white serif headline,
a two-line teal subline, the `ployo` wordmark small and quiet. It reads like a publication. The old
template read like a slide.

## The locked treatment (every image, no exceptions)

- **The photograph is the image.** Documentary, candid, natural light. Real texture, real faces,
  real rooms. Never a posed stock smile, never a corporate handshake, never a person pointing at a
  screen, never blue-tinted "tech" imagery, never an illustration of a robot.
- **The type panel:** a solid dark teal `#0c2422` panel at roughly 88 percent opacity covering about
  a third of the frame, inner edge softly feathered. Rotate WHERE it sits (see archetypes).
- **Headline:** white SERIF, large, tight, **2 to 5 words per line, 2 lines maximum**. This is the
  post's hook compressed to almost nothing. Not a sentence. Not a stat.
- **Subline:** teal `#0D9488` sans-serif, smaller, at most 2 short lines. This is where a specific
  claim goes if the post needs one.
- **Wordmark:** the lowercase `ployo` in teal `#0D9488`, small, inside the panel, comfortably clear
  of every edge.
- **Nothing else on the image.** No charts, no icons, no check marks, no x marks, no funnels, no
  quadrants, no percentage callouts, no punchline pill, no underline stroke, no borders, no
  "Ahmed Raza · Co-Founder & CTO" credit line. The old footer is retired with the old template.

## Scene archetype — rotate this (anti-repeat)

Variety now comes from the SCENE, not from a chart type.

1. Read `state/recent-styles.json` (`{"recent":[...]}`). **Pick a scene NOT in the last 4.** Prepend
   your pick, trim to 4, commit.
2. The scenes. Pick the one that actually fits the post; do not force it.
   - `care-worker` — a carer or nurse in soft scrubs, mid-conversation, listening. Warm interior.
   - `recruiter-desk` — someone at a desk late, screen glow, papers, coffee going cold.
   - `waiting` — a candidate waiting: a chair in a corridor, a bag, hands in lap, a lanyard.
   - `hands-detail` — a tight crop: hands on a phone, a form being signed, a badge, a keyboard.
   - `interview-room` — two people across a table, the near one out of focus from behind.
   - `night-shift` — a corridor or ward at night, warm lamps, a figure at the far end.
   - `commute` — someone outside a building checking a phone, early light, coat, breath.
   - `empty-room` — an empty interview room, two chairs, one table, nobody in it.
3. **The panel position rotates with the scene:** left third for a portrait subject on the right,
   bottom third for a wide or detail shot. Whatever keeps the face and the type from fighting.

## Building the gpt-image-2 prompt

Fill this with THIS post's content. Quote every string that must render verbatim.

```
A premium editorial photograph for a magazine article. Portrait orientation, cinematic.

Scene: <the chosen archetype, described concretely and specifically: who, what they are
doing, the room, the light>. Natural <window/lamp/early morning> light from the <left/right>,
shallow depth of field, warm neutral tones, real skin texture, candid documentary feel.
No posed smile, no stock-photo look. The subject occupies the <right/upper> two thirds.

Over the <left third / bottom third>, a solid dark teal #0c2422 panel at roughly 88 percent
opacity, its inner edge softly feathered. All text sits well inside this panel with generous
padding, never closer than 8 percent of the image height to any edge of the frame.

On the panel, in clean white serif type, large and tightly set, two lines:
"<3-5 words>"
"<3-5 words>"
Directly beneath it, smaller, in teal #0D9488 sans-serif, at most two lines:
"<the specific claim, short>"

Lower on the same panel, with clear space beneath it, the lowercase wordmark "ployo" in
teal #0D9488, small.

No quotation marks anywhere unless the headline is a real quote from a named source. No other
text anywhere. Photorealistic, restrained, editorial. No charts, no icons, no logos, no
collage, no borders, no illustration.
```

## Rendering

Feed posts are **portrait 1088x1360** (LinkedIn shows portrait uncropped in feed).
Article covers are **landscape 1920x1088** — ⚠ LinkedIn crops article covers to 16:9, and a 3:2
cover gets the wordmark sliced off the bottom. That happened on 2026-08-24; render 16:9 for covers.

Render three candidates and ship the best one:

```
IMAGE_N=3 python3 tools/make_image.py "$IMAGE_PROMPT" "$SLUG" docs/images
```

⚠ **The routine prompt's Step 7 gives you this command WITHOUT the `IMAGE_N=3` prefix.** Add the
prefix. The output path is unchanged, so this is safe.

Candidate 1 is always `docs/images/<SLUG>.png`; the others land in `.image-candidates/` (gitignored).
**Read all three and promote the best**, by `cp`-ing it over `docs/images/<SLUG>.png`. With
photography, judge on: a mangled face or hand, text overlapping the subject's face, a misspelling in
the headline, a clipped wordmark, a panel that swallows the photograph. Then commit **only**
`docs/images/<SLUG>.png`. Never `git add` `.image-candidates/` — the repo is public and each loser is
~2MB.

Image URL = `https://ahmedraza28.github.io/brand-agent/images/<SLUG>.png`.

### What was measured (2026-08-06) — don't re-litigate this from a blog post

- **`quality` is "medium", deliberately.** Rendered 2x at `high` and 5x at `medium` at production
  size: all seven spelled every word correctly. Medium costs a **quarter** of high (1587 vs 6431
  output tokens) and takes ~50s vs ~133s.
- **Three medium candidates cost less than one high image** and take about the same wall clock
  (55s for n=3 vs 48s for n=1, generated concurrently server-side).
- **There is no "thinking mode" on this API.** `mode`, `thinking` and `reasoning_effort` all return
  400 "Unknown parameter". Any skill telling you to pass it is wrong and will break this step.

### Prompt habits that actually improve rendering

- **Quote every string verbatim**, with the line breaks you want. The model renders what you quote
  and invents when you describe.
- **Fewer words beats higher quality.** The headline is 2 lines of 3 to 5 words. Anything longer is
  what gets squashed, at any quality.
- **Name the hex every time** you name a colour.
- **Describe the photograph like a photographer**, not like a brief: name the light source and
  direction, the depth of field, the crop. "Natural window light from the left, shallow depth of
  field, warm neutral tones" does more work than "professional and modern".

## Rules that keep it on-brand

1. **The headline = the post's hook, compressed to almost nothing.** Same single claim as the text
   post, never a second idea.
2. **Two lines, 3 to 5 words each.** If it does not fit, the hook is not sharp enough yet.
3. **Perfect spelling.** Re-read every quoted word; simplify anything easy to mis-render.
4. **Honor the guardrails on the image too** (`config/guardrails.md`): no internal Ployo specifics,
   no number that is not in `state/stats-pack.json` or verified this run, hold the explainable /
   human-in-the-loop / bias-aware line, never name or dunk a competitor.
5. **No em dashes anywhere on the image.**
6. ⚠ **The people in these photographs are AI-generated and are not real.** Never write or imply
   that the person shown is a Ployo candidate, customer, employee or interviewee. Never put quotation
   marks around a headline unless it is a real quote from a named source that was verified this run:
   a quoted sentence nobody said is a fabrication, on an account whose whole position is that its
   claims are checkable. Where the platform offers an image caption, use
   "AI-generated illustration. Not a real candidate, customer or interview."
7. **No charts. No infographics.** If a post's idea seems to need a diagram, it needs a sharper hook
   instead. This rule is the reason this file was rewritten.
