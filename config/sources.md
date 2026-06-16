# Trend sources — all free, all keyless

The agent gathers candidate moments from these, then ranks. Use several every run; redundancy means one dead feed doesn't blind the pass. **Never pay for a source.** No API keys, no paywalls, no pay-to-list directories — every source below is free and keyless, and it stays that way.

## Scope — what the agent is hunting for

The subject is **hiring**, spoken FROM the AI-builder seat. Ahmed is an AI founder with sharp hiring takes (Ployo = AI interviewers that screen, interview and score candidates end-to-end). The audience is senior **Talent Acquisition / recruiting / People & Culture leaders + founders/CEOs who own hiring**, across industries. So a "moment" is anything that would land on a TA leader's or CEO's desk today, across three pillars:

1. **The state of hiring** — what's broken in recruiting: resume/ATS keyword theater, ghosting, time-to-hire, interview theater, screening at volume, bias, the labor market itself.
2. **AI x hiring** — what AI actually changes for screening / interviews / scoring; new AI-hiring tools, funding, studies; AI-in-hiring regulation (NYC Local Law 144, EU AI Act); tasks-not-jobs / future-of-work.
3. **Founder lens** — lessons building AI interviewers and selling to TA leaders (mostly evergreen, but a news moment can spark it).

AU aged-care / health / staffing is **one proof point, never the boundary** — a moment doesn't have to be Australian or care-sector to count.

## Primary — the workhorses (every run)

- **Built-in `WebSearch`** — the main discovery engine for all three pillars. Run **4-6 of the ready-to-run queries below** each pass. Then `WebFetch` the actual article before drafting.
- **`WebFetch`** — fetch the real article / report / regulation page behind any candidate moment to **verify the claim, the number, and who said it before a post reacts to it**. Grounding is mandatory (see `guardrails.md`). Never react to a headline alone.

### Ready-to-run WebSearch queries (rotate 4-6 per run, mix the pillars)

- `site:hiringlab.org OR "jobs report" OR "labor market" hiring data this week`
- `"AI" (hiring OR recruiting OR "talent acquisition" OR interview OR screening) news today`
- `new AI recruiting tool OR AI interview OR AI screening launched this week`
- `AI hiring funding OR acquisition recruiting startup this week`
- `EU AI Act OR "Local Law 144" OR "AI in hiring" regulation OR bias OR audit this week`
- `monthly jobs report May 2026 OR June 2026 unemployment hiring reaction`
- `JOLTS job openings quits rate latest month labor market`
- `LinkedIn Workforce Report OR Global Talent Trends new data hiring`
- `Josh Bersin OR HR Dive OR HR Brew AI in hiring this week`
- `Recruiting Brainfood latest issue OR what recruiters are talking about this week`
- `company RTO mandate OR layoffs hiring impact this week`
- `time to hire OR ghosting OR ATS OR resume screening recruiting problem 2026`
- `site:ere.net OR site:shrm.org recruiting OR talent acquisition latest`
- `Stanford OR research study AI hiring bias OR resume screening findings`
- `future of work tasks not jobs AI labor market this week`

## RSS / direct feeds (keyless — fetch with WebFetch or curl)

Verified reachable 2026-06-16. These reach outlets that block direct scraping, and they're the backbone of the daily pass.

- **Google News RSS (the keyless backbone)** — `https://news.google.com/rss/search?q=<url-encoded query>+when:2d&hl=en-US&gl=US&ceid=US:en`. Free, no key, no rate limits, and it reaches outlets that 403/Cloudflare a bot directly (HR Brew, ERE, SHRM, Workology, TLNT). Swap the query for any topic/outlet; `when:2d` for breaking, `when:7d` for weekly outlets. Two daily catch-all heartbeats:
  - **AI x hiring (last 48h):** `…?q=%22AI%22+(hiring+OR+recruiting+OR+%22talent+acquisition%22+OR+interview+OR+screening)+when:2d&hl=en-US&gl=US&ceid=US:en`
  - **Regulation & bias (~2-3x/week):** `…?q=(%22EU+AI+Act%22+OR+%22Local+Law+144%22+OR+%22AI+hiring%22+OR+%22algorithmic+hiring%22)+(bias+OR+regulation+OR+audit+OR+discrimination)+when:14d&hl=en-US&gl=US&ceid=US:en`
- **HR Dive** — `https://www.hrdive.com/feeds/news/` (direct, valid RSS). Daily HR/recruiting trade news: EEOC actions, AI-in-hiring legal exposure, RTO, layoffs, comp. Strong Pillar-1 and Pillar-2 feed.
- **Indeed Hiring Lab** — `https://hiringlab.org/feed/` (direct, valid RSS). The best free, data-rich labor-market source: original analysis on the monthly jobs report, time-to-hire, job-seeker behavior, sector hiring. Perfect for a numbers-backed contrarian "state of hiring" take. **Use this for jobs-report / JOLTS reactions** (BLS direct feeds are bot-blocked — see Avoid).
- **Josh Bersin** — `https://joshbersin.com/feed/` (direct, valid RSS). The most-cited HR analyst on AI in HR/recruiting and the future of work. React-to / push-back fodder for Pillar 2; he sets the agenda senior People leaders already discuss.
- **Recruiting Brainfood (Hung Lee)** — `https://recruitingbrainfood.substack.com/feed` (direct, valid + current). Weekly hand-curated digest read by 30k+ recruiters; one fetch = the week's recruiting conversation map and what the TA-leader audience is talking about. ⚠ Use the **Substack** feed; the old `recruitingbrainfood.com/feed/` is STALE (last item 2020).
- **LinkedIn Talent Blog** — `https://www.linkedin.com/business/talent/blog` (WebFetch the HTML; no RSS). First-party recruiting trend content + LinkedIn's own hiring-data drops, aimed at the TA-leader audience.
- **LinkedIn Economic Graph / Workforce data** — `https://economicgraph.linkedin.com/workforce-data` (WebFetch; for fresh drops also run a Google News query for `LinkedIn Workforce Report`). Hiring-rate / skills-demand / internal-mobility data; periodic drops are defensible "state of hiring" moments.
- **SHRM (via Google News)** — `https://news.google.com/rss/search?q=site:shrm.org+when:7d&hl=en-US&gl=US&ceid=US:en`. The largest HR body; its research/policy takes define the mainstream HR position to sharpen or push against. ⚠ Reach it through Google News — SHRM has no usable direct RSS.
- **HR Brew (via Google News)** — `https://news.google.com/rss/search?q=%22HR+Brew%22+when:7d&hl=en-US&gl=US&ceid=US:en`. Punchy daily HR newsletter; trend-y, audience-relevant angles on AI at work. ⚠ The direct `hr-brew.com/feed` 403s to bots — Google News only.
- **ERE (via Google News)** — `https://news.google.com/rss/search?q=site:ere.net+when:14d&hl=en-US&gl=US&ceid=US:en`. Long-running TA-practitioner publication (sourcing, recruiting strategy, metrics) for tactical Pillar-1 craft. ⚠ ERE has no working public RSS — Google News + a `site:` query is the only keyless path.

### Reddit (ground-level recruiter voice — keyless, but rate-limited)

The unfiltered voice of working recruiters and People teams. Their real frustrations (ghosting, ATS keyword theater, AI-tool ROI doubts) are gold for authentic, contrarian Pillar-1 hooks the audience instantly recognizes.

- **r/recruiting** — `https://old.reddit.com/r/recruiting/hot/.rss`
- **r/humanresources** — `https://old.reddit.com/r/humanresources/hot/.rss`
- **r/talentacquisition** — `https://old.reddit.com/r/talentacquisition/hot/.rss` (smaller; supplementary, sharper/more strategic)

⚠ Reddit rules: use the `old.reddit.com` host + the `.rss` path with a **real User-Agent** (`curl -sL -A 'Mozilla/5.0 (compatible; brand-agent/1.0)'`). The JSON endpoints 403 and WebFetch is blocked for reddit. **Space the calls out — one sub per run** (rapid repeats get 429). If reddit rate-limits, fall back to Google News.

## Recurring calendar moments (anticipate these)

Predictable, audience-native moments worth pre-loading a take for:

- **Monthly US jobs report** (BLS Employment Situation, first Friday of most months, ~08:30 ET) — hiring/unemployment/wage numbers. React with a labor-market take grounded in **Indeed Hiring Lab's same-day analysis** + a WebSearch (`May 2026 jobs report`), NOT the bot-blocked BLS feed.
- **Monthly JOLTS** (mid-month, ~1 month lagged) — openings, quits, hires. Great for "is the labor market actually loosening" contrarian takes; reach via WebSearch + Indeed Hiring Lab.
- **ADP National Employment Report** (~first Wednesday monthly, two days before the jobs report) — private-payroll preview; reliable mid-week hiring moment.
- **Recruiting Brainfood weekly issue** (Hung Lee, drops Fri/Sat) — packaged map of the week's recruiting conversation; reliable Friday/weekend reaction fodder.
- **LinkedIn Workforce Report / Economic Graph drops + annual Global Talent Trends / Future of Recruiting reports** — scheduled, data-heavy, audience-native.
- **Q4/January hiring-outlook & predictions season** (Nov-Jan) — prime window for a sharp contrarian forecast on AI x hiring.
- **Seasonal hiring ramps** — January "new year, new job" surge + Q1 ramp; September post-summer ramp; spring (Mar-Apr) recruiting peak; grad / early-career season (Aug-Oct campus + spring internships). All good "state of hiring" / screening-at-volume hooks.
- **Big-co RTO mandates & layoff/workforce announcements** (clustered around earnings, late Jan / Apr / Jul / Oct) — react to the hiring/retention angle, **never dunk on the named company**.
- **AI-hiring product launches** (irregular but frequent) — a hiring-tech vendor ships an AI screener/sourcer, or a major lab ships something that changes hiring. React from the builder seat on **what it actually changes for hiring**, not the model spec.
- **AI-hiring regulation milestones** — NYC Local Law 144 enforcement/anniversary, EU AI Act phased obligations & deadline shifts, new US state AI-in-hiring disclosure laws, EEOC guidance. High-authority ground for the messaging spine (explainable, human-in-the-loop, bias-aware).
- **Major industry conferences** — SHRM Annual (~June), LinkedIn Talent Connect (~fall), ERE Recruiting Innovation Summit, UNLEASH, HR Tech (~Sept-Oct). Announcement clusters + a live audience of TA leaders; pre/during/post reaction windows.
- **Year-end "what broke in hiring this year" retrospective** (December) — annual reflective long-form or carousel moment.

## What counts as a "big enough" moment (ranking)

Rank candidates by **how much a senior HR/TA leader or a CEO who owns hiring would care about it TODAY** — recruiting signal, AI-in-hiring signal, labor-market signal. Not by how loud AI-Twitter is about it. The test for the opening line: a TA leader scrolling LinkedIn at their desk should feel "this is about my job," and want to argue back.

**High signal (lead with these):**
- A **labor-market data drop** that changes the hiring picture — jobs report, JOLTS, time-to-hire / cost-per-hire trends, sector hiring data, entry-level collapse numbers. A clean, citable figure that lets you take a contrarian "here's what's actually happening" position.
- A **new AI-hiring tool, funding round, or study** that reshapes how screening / interviewing / sourcing gets done — and what it really changes for a hiring team (not the vendor's press release).
- An **AI-in-hiring regulation or bias moment** — LL144 / EU AI Act / state disclosure laws / a credible bias study (e.g. Stanford HAI). Earned, high-authority ground for the explainable / human-in-the-loop / bias-aware spine.
- A **live recruiting debate** a TA-leader audience is actively having — fake/AI-generated candidates, the AI-vs-AI interview arms race, candidates bailing on one-way AI interviews, "rejected without a word," agentic sourcing running the top of funnel, "AI fluency" as a screening criterion.
- A **named hiring pain with a number behind it** — ghosting, ATS keyword theater, interview theater, screening at volume, bias — that the audience lives daily and a citable stat makes undeniable.

**Low signal (skip):**
- A pure AI-model / chip / lab launch with **no hiring angle** (this is no longer the beat — don't force a model launch into a hiring post unless it genuinely changes how people get hired).
- Incremental version bumps, vendor press releases with no traction, rumors with one flaky source.
- Anything you can't verify this run.
- Anything already covered in `state/ledger.json` within 7 days.
- A **saturated take** that adds nothing: "AI won't replace recruiters, it'll make them better," "AI is transforming recruitment," "5 ways AI saves recruiters time," "skills-based hiring is the future" stated as a slogan, "beat the ATS with keywords," "be human / bring empathy" as a bare platitude, or pure doom / pure hype. If the angle is one of these, either find the contrarian mechanism underneath it or pass.

**Tie-breaker:** prefer the moment with (a) a hard, citable number, (b) a stake a senior reader can publicly disagree with, and (c) a natural seat for the builder lens. A moment that has all three beats a louder one that has none.

## Slow-day fallback — a bank take, never a forced reaction

**Quality over cadence — never force a weak news reaction.** If a run surfaces nothing that clears the "big enough" bar, do **not** stretch a thin headline into a post. Instead, fall back to an **opinion-bank take**: pull Ahmed's least-recently-used pre-approved belief from `state/opinion-bank.json` and develop it into a standalone post. An evergreen hiring take in his own voice beats a limp news reaction every time, and it keeps the daily cadence honest without lowering the bar.

**Bank selection rules:** see `config/takes.md` (pick the oldest `last_used`, never reuse within 14 days, never invent a new opinion, fresh angle on any reuse). Those mechanics apply here.

**Publish target for the slow-day fallback: LinkedIn.** The slow-day bank take publishes to **LinkedIn** as a normal text post under the standard LinkedIn voice rules (persona.md + playbook.md: opinion-first opener, ~150-300 words, text-first format, rationed question-closer, no em dashes). This overrides `config/takes.md`'s "X-ONLY / never LinkedIn" line, which applies only to the dormant standalone takes stream (off while X is suspended), NOT to this slow-day LinkedIn fallback path. `takes.enabled=false` does not block the slow-day fallback; it only disables the standalone takes stream.

## Per run

Pick the top **1-2 moments**. On a genuinely slow day, **1 or 0 news moments + a bank take** is the right answer — quality over cadence, always. Spread the three pillars across the week so no single week reads as one note.

---

## DORMANT — X (Twitter) sourcing

⚠ **X / Twitter is the suspended channel — LinkedIn is the only LIVE channel right now.** The hooks and feeds in this file feed the **LinkedIn-first hiring brand**. Do NOT delete this section: if X is reinstated, the AI-builder discovery feeds below can be revived as a *secondary* stream. They are NOT the active beat — when X returns, hiring stays the main subject and these become supporting color, not the headline.

The verdict-first / opinion-first principle is **not X-specific** — it now governs LinkedIn too (open with the take, facts as evidence, rotate the closer, ration questions). Keep that habit on LinkedIn regardless of X's status.

Revivable AI-builder discovery feeds (keyless), for if/when X returns:
- **Hacker News (Algolia)** — front page `https://hn.algolia.com/api/v1/search?tags=front_page`; recent AI `https://hn.algolia.com/api/v1/search_by_date?query=AI&tags=story&numericFilters=points%3E50`.
- **Product Hunt RSS** — `https://www.producthunt.com/feed?category=artificial-intelligence` (genuinely new tools — still useful for the AI-hiring-*tool* angle even now, when the launch is a hiring product).
- **AI-builder Reddit** — `https://old.reddit.com/r/LocalLLaMA/hot/.rss`, `https://old.reddit.com/r/artificial/hot/.rss`, `https://old.reddit.com/r/MachineLearning/hot/.rss` (same UA + rate-limit rules as the recruiting subs above).
- **WebSearch wildcards** — `biggest AI news today`, `new AI model released <date>`, `<big lab> announcement`. These were the old beat; under the new position they only matter when the AI story **directly changes hiring**.

## Avoid (verified dead / blocked / low-signal 2026-06-16)

- **BLS direct RSS** (`empsit.rss`, `jolts.rss`, `news_release.rss`) — Akamai 403s all scripted user-agents. Get jobs/JOLTS data via WebSearch + Indeed Hiring Lab's same-day analysis.
- **`hr-brew.com/feed` / `hrbrew.com/feed`** — 404/403 to bots. Pull HR Brew via Google News only.
- **`ere.net` direct RSS** (`/feed`, `/rss`, `/articles/rss`) — headless site, no working public RSS. Use Google News `site:ere.net`.
- **`workology.com/feed`, `tlnt.com/feed`** — Cloudflare JS challenge, 403/404 to scripts. Reach via Google News if needed.
- **`recruitingbrainfood.com/feed/`** (non-Substack) — STALE, last item 2020. Use the Substack feed.
- **`shrm.org` direct RSS** — 404, no usable feed. Use Google News `site:shrm.org`.
- **reddit.com JSON endpoints (`/hot.json`) and WebFetch on reddit** — JSON 403s, WebFetch blocked. Only `old.reddit.com` `.rss` + real UA works, and it 429s on rapid repeats (space them out).
- **Paywalled / pay-to-list sources** — Feedspot "Top 100" lists (directory, not a source), HBR (paywall), email-gated vendor "state of recruiting" PDFs. Skip — free first-party feeds + Google News only.
- **Aggregator / SEO stat-listicles** (amraandelma, salesso "LinkedIn statistics" posts) — recycled, often unverifiable numbers. Never react without confirming the primary source via WebFetch.
