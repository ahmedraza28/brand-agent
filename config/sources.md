# Trend sources — all free, all keyless

The agent gathers candidate moments from these, then ranks. Use several every run; redundancy means one dead feed doesn't blind the pass. **Never pay for a source.**

## Primary
- **Built-in `WebSearch`** — the main "search the internet" tool. Run several queries each pass:
  - `biggest AI news today`
  - `AI model launch this week` / `new AI model released <today's date>`
  - `new AI tool launched <today's date>`
  - `AI funding OR acquisition OR IPO this week`
  - `<big lab> announcement` rotating across: OpenAI, Anthropic, Google DeepMind, Meta AI, xAI, Mistral, Nvidia, Microsoft, Apple
  - one wildcard: `what is AI Twitter talking about today`
- **`WebFetch`** — fetch the actual article/announcement URL for any candidate to verify facts before drafting (grounding is mandatory; see guardrails).

## RSS / APIs (keyless — fetch with WebFetch or curl)
- **Google News RSS** — `https://news.google.com/rss/search?q=<url-encoded query>+when:1d&hl=en-US&gl=US&ceid=US:en`. Best for breaking news in the last 24h. Query AI terms + the big-co names above.
- **Hacker News (Algolia)** — front page: `https://hn.algolia.com/api/v1/search?tags=front_page`; recent AI: `https://hn.algolia.com/api/v1/search_by_date?query=AI&tags=story&numericFilters=points%3E50`. High points + many comments = builders are reacting.
- **Product Hunt RSS** — `https://www.producthunt.com/feed?category=artificial-intelligence` (or the homepage feed). Genuinely new tools.
- **Reddit RSS** — `https://www.reddit.com/r/LocalLLaMA/hot/.rss`, `https://www.reddit.com/r/artificial/hot/.rss`, `https://www.reddit.com/r/MachineLearning/hot/.rss`. (Set a UA header on curl: `-A "brand-agent/1.0"` — Reddit blocks empty UAs.)

## What counts as a "big enough" moment (ranking)
Rank candidates by how much a sharp AI-builder audience would care *today*. High signal:
- A major model / product launch (new frontier model, a capability jump, a widely-used tool shipping something big).
- A genuinely novel tool builders are flocking to (HN front page, high PH votes).
- Big-co AI moves: chips, major partnerships, notable acquisitions/funding/IPOs.
- A real debate AI-Twitter is actively having (a benchmark fight, a "is X overhyped" argument).

Low signal (skip): incremental version bumps no one's talking about, press releases with no traction, rumors with one flaky source, anything you can't verify, anything already covered in `ledger.json` within 7 days.

**Scope:** AI first; adjacent big tech (chips, major launches, notable IPOs/funding) when it's genuinely a moment. Tie to hiring / future-of-work only when natural (see persona).

**Per run:** pick the top **1-2** moments. On a slow day, 1 or 0. Quality over cadence — never force it.
