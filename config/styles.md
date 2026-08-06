# Image style — ONE locked Ployo template, rotate the LAYOUT

**Philosophy change (2026-07-20):** the old "rotate 18 random art-directions, never repeat" system is retired. Ahmed wants a **consistent, recognizable branded look** — the same visual system on every post, the way strong operator accounts do it (one editorial template you learn to recognize in the feed). Variety now comes from the **layout archetype** and the **content**, NOT from a different art style each time.

The look is Ployo's **signature editorial** aesthetic: warm cream paper, dark teal-black serif headline, one teal accent, a dark punchline strip, an "Ahmed Raza" footer. Think a sharp business-magazine cover, not an AI art piece.

Render with `tools/make_image.py` (gpt-image-2, portrait **1088x1360**, opaque). gpt-image-2 spells short text correctly — lean on that, but keep small-text density LOW (a few short rows, never paragraphs).

## The locked template (every image, no exceptions)

- **Canvas:** 4:5 portrait, warm cream paper background `#faf6ec` with a very subtle paper texture. Flat vector, generous negative space. NO photographs, NO real human faces/likenesses, NO robots, NO brains, NO glowing orbs.
- **Headline (top):** a bold, high-contrast **serif** headline in dark teal-black ink `#0c2422`, left-aligned, 2–4 short lines. Underline ONE key phrase with a hand-drawn **teal** stroke `#0D9488`. This is the post's core claim, compressed.
- **Body (middle):** the chosen **layout archetype** (see list) rendered in flat line icons + short text. Positives use teal `#0D9488` check icons; negatives use a soft red `#D83E3A` x icon. Keep rows short (2–5 words each), evenly spaced, tidy alignment.
- **Punchline strip (lower):** a full-width rounded pill filled dark teal-black `#0c2422` with centered cream text — one sharp line, with 2–4 words emphasized in teal `#0D9488`.
- **Footer (bottom):** a thin hairline divider, then the lowercase wordmark **"ployo"** set bold in teal `#0D9488` with tight letter-spacing, then muted dark-gray text **"Ahmed Raza  ·  Co-Founder & CTO"**. Always this exact footer.
- **Palette — use ONLY these:** cream `#faf6ec`, dark teal-ink `#0c2422`, brand teal `#0D9488`, soft red `#D83E3A` (negatives only), muted gray for secondary text. No other colors.
- **Typography feel:** serif display headline, clean sans for body/rows. Perfectly spelled, print-quality, clear hierarchy.

## Layout archetype — rotate this (anti-repeat)

1. Read `state/recent-styles.json` (`{"recent":[...]}`). **Pick an archetype NOT in the last 4.** Prepend your pick, trim to 4, commit.
2. The archetypes (pick by what the post's idea actually is — don't force it):
   - **`vs-comparison`** — two columns split by a small teal "VS" badge: a red-tagged wrong way vs a teal-tagged right way, 3 short rows each. (Best for "X isn't the problem, Y is" takes.)
   - **`numbered-list`** — a teal kicker label + 3 stacked rows, each an icon-in-circle + a short bold sub-head + one muted line. (Best for "3 things / 3 signs / 3 people" takes.)
   - **`funnel`** — a filter/funnel splitting inputs into kept vs dropped, showing what a bad filter silently loses. (Best for ATS / screening-volume takes.)
   - **`single-stat`** — one oversized number or ratio as the hero, a one-line frame under it, the punchline strip below. (Best for a data-shock take; only with a VERIFIED number from Step 4.)
   - **`before-after`** — two stacked panels, "what it looks like" vs "what's actually true". (Best for reframe-the-villain takes.)
   - **`quadrant`** — a 2x2 with one highlighted cell in teal. (Best for a framework take; use sparingly.)
3. Whatever the archetype, the template above (cream, serif headline, teal accent, dark punchline pill, ployo/Ahmed footer) stays identical. Two `vs-comparison` posts weeks apart should look like the SAME brand — that is the point now.

## Building the gpt-image-2 prompt (skeleton — fill with THIS post's content)

Compose the prompt in this order; keep it concrete and specify the hexes:

```
A premium editorial infographic poster for LinkedIn, 4:5 portrait, calm magazine-cover
style. Warm cream paper background (hex #faf6ec), subtle paper texture. Flat vector, lots
of negative space, no photographs, no real human faces, no robots, no glowing orbs.

TOP — a bold high-contrast SERIF headline in dark teal-black ink (hex #0c2422), left
aligned, on <N> lines: "<line 1>" / "<line 2>" / "<line 3>". Underline "<key phrase>"
with a hand-drawn teal stroke (hex #0D9488).

MIDDLE — <the chosen archetype, described concretely: columns / rows / funnel, each row's
short text, teal check icons for positives (#0D9488) and soft-red x icons for negatives
(#D83E3A), even spacing, tidy alignment>.

LOWER — a full-width rounded pill strip filled dark teal-black (hex #0c2422) with centered
cream text: "<one sharp punchline>". Emphasize "<2-4 words>" in teal (hex #0D9488).

FOOTER — a thin hairline divider, then the lowercase wordmark "ployo" bold in teal (hex
#0D9488) with tight letter spacing, followed by smaller muted dark-gray text
"Ahmed Raza  ·  Co-Founder & CTO".

Overall mood: sophisticated, editorial, trustworthy, tech-forward. Restrained palette of
cream, dark teal ink, teal accent<, and one soft red>. Crisp, perfectly spelled,
print-quality typography with clear hierarchy.
```

Render three candidates and ship the best one:

```
IMAGE_N=3 python3 tools/make_image.py "$IMAGE_PROMPT" "$SLUG" docs/images
```

It prints one path per candidate. Candidate 1 is always `docs/images/<SLUG>.png`; the other two land in `.image-candidates/` (gitignored). **Read all three images, then promote the best-rendered one** by `cp`-ing it over `docs/images/<SLUG>.png`. Judge on rendering only, not on taste — the prompt is the same for all three, so the differences are misspellings, a clipped or squashed word, a crooked pill, uneven rows, a mangled `ployo` wordmark. If candidate 1 is already clean, keep it and move on.

Then commit **only** `docs/images/<SLUG>.png`. Never `git add` `.image-candidates/` — the repo is public and GitHub-Pages served, and each losing candidate is ~2MB.

Image URL = `https://ahmedraza28.github.io/brand-agent/images/<SLUG>.png`.

### What was actually measured (2026-08-06) — don't re-litigate this from a blog post

- **`quality` is "medium", and that is deliberate.** The same real template prompt was rendered 2x at `high` and 5x at `medium` at the production 1088x1360. All seven spelled every word correctly, footer credit included, checked at 1:1. Medium costs a **quarter** of high (1587 vs 6431 output tokens) and takes ~50s vs ~133s. Override with `IMAGE_QUALITY=high` if you ever see the difference, but render both and compare the footer strip before you believe it.
- **Three medium candidates cost less than one high image** and take about the same wall-clock as one (55s for n=3 vs 48s for n=1 — they generate concurrently server-side). That is why the pick-the-best step above is affordable at all.
- **There is no "thinking mode" on this API.** `mode`, `thinking` and `reasoning_effort` all return 400 "Unknown parameter". It is a ChatGPT product feature. Any skill or article telling you to pass it is wrong about the API and will break this step.

### Prompt habits that actually improve rendering

These matter far more than the quality knob:

- **Quote every string verbatim** in the prompt, exactly as it must appear, with the line breaks you want (`on 3 lines: "..." / "..." / "..."`). The model renders what you quote; it invents when you describe.
- **Fewer words beats higher quality.** Rows of ≤5 words render cleanly at medium; a row that runs long is the thing that gets squashed or clipped, at any quality.
- **Name the hex every time** you name a colour, and say where the emphasis goes ("emphasize `<2-4 words>` in teal `#0D9488`") rather than trusting it to choose.
- **Avoid words that are easy to mis-render** (long compound words, unusual proper nouns). If a word is risky, pick a shorter synonym — rule 3 below.

## Rules that keep it on-brand

1. **The headline = the post's hook, compressed.** The image must carry the SAME single claim as the text post — never a second unrelated idea. One post, one claim, echoed in the image.
2. **Short text only.** A 2–4 line headline, ≤5 rows of ≤5 words, one punchline. No paragraphs on the image — dense small text is the one thing gpt-image-2 still fumbles.
3. **Perfect spelling.** Re-read every word in the prompt; if a word is easy to mis-render, simplify it.
4. **Honor the guardrails on the image too** (`config/guardrails.md`): no internal Ployo specifics, no unverified number (a `single-stat` needs a Step-4-verified figure), hold the explainable / human-in-the-loop / bias-aware line, never name/dunk a competitor.
5. **No em dashes anywhere on the image** (use a middot ·, comma, or period).
6. **Footer is fixed:** the ployo wordmark + "Ahmed Raza · Co-Founder & CTO", every time.

## Proven examples (the look to match)

- `vs-comparison`: headline "AI can screen 1,000 resumes a minute. It still can't tell you who can do the job." → left "RESUME KEYWORD MATCH" (3 red x rows) vs right "STRUCTURED EVIDENCE" (3 teal check rows) → strip "Screening at volume isn't the problem. Screening for the wrong signal is."
- `numbered-list`: headline "Your ATS rejected your best candidate. It just doesn't know it." → kicker "3 PEOPLE YOUR KEYWORD FILTER SILENTLY DROPS" → 3 rows (the career-changer / the self-taught builder / the returner) → strip "Hiring for keywords is how you miss the person who would have been great."
