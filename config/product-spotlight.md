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

## The framing — LEAD WITH A SHARP OPINION (this is the whole point)
Ahmed's audience follows him for his **take**, not a neutral recap. A spotlight with no opinion is a dead post — it won't get shared, replied to, or remembered. **Lead with a real, specific, shareable opinion**: the kind of line a smart person screenshots or argues with. Have a thesis and commit to it. Examples of the energy:
- "This is the one to watch, and here's the bet that actually makes it work."
- "Overhyped. The hard part is X and nobody, including them, has solved it."
- "Everyone's about to copy this. Remember who did it first."
- "Clever, but it dies the day [big lab] ships the same feature for free."
- "This is the obvious move dressed up as a breakthrough."

Pick the angle that's genuinely TRUE and interesting for this product, and say what you actually think. Spicy, specific, a little contrarian — make a thoughtful person stop and reply. A useful skeleton (don't follow it mechanically): **your take/verdict → the bet that makes it work OR the flaw that kills it → what it signals for where things are going → a sharp question or mic-drop line.**

**The lines that still hold** (these are the seatbelt — they protect Ahmed WITHOUT softening the take; strong opinions ARE the content):
1. **Spicy about the PRODUCT / the BET / the MARKET / the APPROACH — never a personal attack on the makers.** You can call a product overhyped or a strategy doomed; you cannot insult the founders or question their character or competence as people. (Persona + guardrails §5 — this is the ONE hard line on tone.)
2. **Own it as YOUR opinion, not fact.** Lead spicy takes with "my take:", "I think", "my bet", "hot take", "betting that…". An owned opinion that turns out wrong costs nothing; a confident *false statement of fact* is what actually burns you. So: opinions can be as strong as you want; **FACTS must be real** (grounded, fetched — see below).
3. **Don't punch down on tiny, no-name indie launches.** A sharp take on a big lab or a well-funded company (OpenAI, Google, Moonshot, a YC startup) is fair game and more shareable anyway. A brutal takedown of a solo dev's first weekend project is a bad look — for those, be encouraging or skip.
4. **Don't imply Ahmed used it.** The opinion is formed from the outside ("from what they're showing…", "on paper…", "the pitch is…"), not "I tried it and…", unless he actually has.

**Skip the post only if** you genuinely have no real opinion or the product is too boring to have one about — silence still beats filler. But "I don't want to judge" is NOT a reason to hedge: if it's worth posting, it's worth a real take.

## Grounding
Same rails as everything else (guardrails §1–4). **WebFetch the actual product / PH page this run** and state only what you can see there. No invented features, pricing, metrics, founders, or funding. If the product *claims* something you can't verify, write "they claim…" / "the pitch is…" — never assert it as fact. Double-check any number.

## Dedup
Never feature a product already in `ledger.json` within **14 days** (longer than the 7-day news window — a product doesn't re-become news). Add each spotlight to the ledger like any topic.

## X format (the default)
- **Lead tweet ≤280 chars:** open on the product + **your take** (the thesis — what you actually think), close on a sharp question or a mic-drop line that invites replies and arguments. **No link in the body.** Persona + every AI-tell ban applies (0 em dashes, no "here's the thing", no tidy triads, varied sentence length — sound like a person with a real opinion, not a press release).
- **Self-reply (tweet 2):** the product / PH link + any extra context. Links never go in tweet 1.
- **Image:** a single on-brand cover via `tools/make_image.py` (styles.md art-direction rotation, anti-repeat) featuring the **product's actual name / wordmark** — use its logo/brand color if you can identify it from the PH page or site; otherwise set the product name cleanly inside the chosen art style.

## LinkedIn carousel (only when deck-worthy AND under the weekly cap)
- A **short caption** (hook + one line of context + a closing question) + an 8-theme carousel via `tools/make_carousel.py` (auto-rotated theme; see `config/carousel.md`). Source link in `firstComment`.
- Slide scaffold (cover + 3–4 slides + outro): **the product + your verdict → the bet that makes it work OR the flaw that kills it → what it signals for where things go → a sharp closing question.** Every slide grounded (real facts), but carry a clear point of view — a neutral explainer deck is a miss.

## Logging
Log spotlights in `state/posting-log.md` like any post, but slug them **`ps-<slug>`** and add a **`**Kind:** product_spotlight`** line under the heading so the weekly LinkedIn cap can be counted. Add each to `ledger.json` (`platform` = the channels you actually posted it to).
