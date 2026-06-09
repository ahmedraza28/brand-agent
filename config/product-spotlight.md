# Product spotlight — the builder's-lens second stream

A second, lighter content stream alongside the AI-trend posts: a near-daily **X** post (and an occasional LinkedIn carousel) where Ahmed reacts to a genuinely notable **new product launch** with a builder's eye. The goal is to make Ahmed read as someone with a sharp product sense who's paying attention to what's actually shipping — *not* a reviewer handing out scores.

Governed by `state/settings.json` → `product_spotlight`:
- `enabled` (bool) — master on/off for this whole stream. If false, skip it entirely.
- `run` — which daily run produces it (`"second"` = the 12:30 UTC run; the 00:30 run never does a spotlight). One spotlight per run-day, max.
- `linkedin_max_per_week` (int, default 2) — hard cap on product-spotlight **LinkedIn** carousels per ISO week (Mon–Sun UTC). X has no cap.

## Cadence & channels
- **X: every run-day.** X tolerates the volume; this is the primary channel for the stream.
- **LinkedIn: only when the launch genuinely merits a deck, AND only if this ISO-week's spotlight-LinkedIn count is under `linkedin_max_per_week`.** Count it by grepping `state/posting-log.md` for entries in the current ISO week that carry a `**Kind:** product_spotlight` line with a LinkedIn `LIVE` post. At/over the cap, or not deck-worthy → **X-only**. Most days are X-only; that is intended, not a failure.

## What to feature — the quality gate (this is most of the job)
Pull candidates from the last **24–48h**: Product Hunt RSS (top-voted) + Hacker News **"Show HN"** on the front page. Then be ruthless. Feature a launch only if at least one of these is clearly true:
- **Real traction** — high PH vote count, or HN front page with genuine discussion.
- **Genuinely novel** — a real new idea or a meaningfully better approach, not the Nth thin wrapper.
- **Credible signal** — known builders, a notable team/lab, or something the AI-builder crowd is actually talking about.

**Hard skips** (post nothing rather than feature these): derivative GPT-wrappers with no edge; low-vote / no-traction items; anything you can't actually load and verify; waitlist-only vaporware with no real product; anything spammy, scammy, or sketchy; NSFW; crypto/airdrop bait. **If nothing clears the bar, post no spotlight today** and log `spotlight: none (<reason>)`. A skipped spotlight is a normal, good outcome (guardrails §9 — quality over cadence).

## The framing — a builder's lens, never a verdict
This is the part that protects Ahmed's reputation. **You are not a judge handing out a thumbs-up/down or an "is it promising" score.** A founder publicly grading other founders' launches is a bad look and burns a small ecosystem. React like a curious builder instead. Pick the angles that are actually true for *this* product:
- **The real problem it's attacking** — what job is this for, in plain words.
- **The interesting bet / the wedge** — the non-obvious choice the makers made; the thing that could make it work.
- **What you'd watch** — the open question, the hard part, what would have to be true for it to win. Framed as honest curiosity, never a prediction of failure.
- **What it signals** — what this launch says about where the space is heading. (Ahmed's earned territory: tie to building / hiring / AI agents only when it's natural.)

**Hard rules:**
- **Never dunk on the makers or the product.** (guardrails §5 — spicy about ideas, never about people.) Skepticism about an *approach* or a *market* is fine, but framed as an open question ("the thing I'd want to see is…"), never a put-down or a "this will fail."
- **If your honest read is "this isn't interesting" or "this is bad" → don't post it.** Silence is free; a negative post under Ahmed's name is the worst outcome. There is zero obligation to spotlight anything on a given day.
- **Don't imply Ahmed used it.** He's reacting from the outside. Write "from the outside, the interesting thing is…", not "I tried it and…". Never claim hands-on testing, results, or that he's a user, unless that is actually true (guardrails §1–4 cover your own experience too — no fabrication).
- **Honest enthusiasm is welcome** when a launch is genuinely cool — be warm, specific, curious. The default tone is "oh, that's a clever bet," not "let me critique this."

## Grounding
Same rails as everything else (guardrails §1–4). **WebFetch the actual product / PH page this run** and state only what you can see there. No invented features, pricing, metrics, founders, or funding. If the product *claims* something you can't verify, write "they claim…" / "the pitch is…" — never assert it as fact. Double-check any number.

## Dedup
Never feature a product already in `ledger.json` within **14 days** (longer than the 7-day news window — a product doesn't re-become news). Add each spotlight to the ledger like any topic.

## X format (the default)
- **Lead tweet ≤280 chars:** open on the product + the one interesting thing (the bet or the problem it attacks), close on the open question that invites replies. **No link in the body.** Persona + every AI-tell ban applies (0 em dashes, no "here's the thing", no tidy triads, varied sentence length — sound like a person who just saw something clever and has a thought).
- **Self-reply (tweet 2):** the product / PH link + any extra context. Links never go in tweet 1.
- **Image:** a single on-brand cover via `tools/make_image.py` (styles.md art-direction rotation, anti-repeat) featuring the **product's actual name / wordmark** — use its logo/brand color if you can identify it from the PH page or site; otherwise set the product name cleanly inside the chosen art style.

## LinkedIn carousel (only when deck-worthy AND under the weekly cap)
- A **short caption** (hook + one line of context + a closing question) + an 8-theme carousel via `tools/make_carousel.py` (auto-rotated theme; see `config/carousel.md`). Source link in `firstComment`.
- Slide scaffold (cover + 3–4 slides + outro): **what it is → the bet / wedge → what I'd watch → what it signals → the open question.** Every slide grounded; honest, not gushing.

## Logging
Log spotlights in `state/posting-log.md` like any post, but slug them **`ps-<slug>`** and add a **`**Kind:** product_spotlight`** line under the heading so the weekly LinkedIn cap can be counted. Add each to `ledger.json` (`platform` = the channels you actually posted it to).
