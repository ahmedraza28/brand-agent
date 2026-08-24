# Platform Playbook — fact-checked (the drafting brain)

Source: deep-research run `wk8u6rt4l` (LinkedIn/X mechanics, 25 sources, 3-vote adversarial verification) + the 2026-06-16 LinkedIn-first pivot research (LinkedIn algorithm 2026, hook/comment mechanics, carousel-vs-text, US+AU posting windows). The agent must follow these rules when drafting.

## ⚠ Live channel = LinkedIn ONLY (X suspended 2026-06-14)

The X account `@Ahmedraza_28` is suspended, so **LinkedIn is the only live channel.** `state/settings.json` → `channels` is `["linkedin"]`; `product_spotlight.enabled` and `takes.enabled` X-streams are off.

- **The X / Twitter section below is DORMANT** — kept intact (not deleted) so it revives the moment X is reinstated, but it governs nothing while suspended. Skip it when drafting.
- **The product-spotlight section below is DORMANT** for the same reason (it was an X-always / occasional-LinkedIn stream).
- **The live content is ONE LinkedIn stream:** a daily LinkedIn post of sharp hiring takes — news-led (today's AI-in-hiring / state-of-hiring news) or, on a slow news day, opinion-bank-led (`state/opinion-bank.json`, the takes stream now publishing TO LinkedIn instead of X). One stream, three rotating pillars (state of hiring / AI x hiring / founder lens). Quality gate stays: a slow news day pulls a bank-driven evergreen take, never a forced weak news reaction.
- **REVERT when X returns:** set `channels` back to `["x","linkedin"]`, `product_spotlight.enabled=true`, `takes.enabled=true`, and re-read the X section below as live.

## ⚠ 2026-08-24 — the account now writes for CITATION, not engagement

A sweep of 751 real AI answers across ChatGPT, Perplexity and Google AI Overviews found
linkedin.com is the most cited domain in this category, and that 43 of its 242 citation URLs
already point at Ployo or Ahmed. **All 13 of the feed-post citations come from a single post.**
Meanwhile an audit of the last 61 posts found the defect: about a third of them open by citing
someone else's survey, which credits Resume Builder or iCIMS instead of us.

So the objective changed. Optimise for being the source an AI answer quotes. Ignore engagement
metrics when deciding what to write.

**Four files govern the new content types. Read the one you need, when you need it:**

| File | Read it when | Note |
|---|---|---|
| `config/first-party.md` | writing a findings post from our own data | one per week |
| `config/pulse.md` | writing a Pulse article | 2 to 3 per month, published by hand |
| `config/competitors.md` | naming any competitor | ⚠ ~47KB, generated. Read only for roundups and comparisons, not on an ordinary post. |
| `state/stats-pack.json` | stating any number as ours | the ONLY approved source of our figures |

**Three rules that now outrank the drafting habits below:**

1. **Do not open a post by citing another company's research** unless the post adds one of our own
   figures to it. `tools/check_facts.py` blocks this.
2. **Name Ployo in at least half of all posts, link ployo.ai in at least a third.** A cited post
   that never names us achieves nothing, and a citation needs somewhere to land. Of the last 61
   posts, 10 named Ployo and 2 linked the site.
3. **Every number stated as ours must be in `state/stats-pack.json`.** See guardrail 8a. There are
   no first-party findings measured yet, so until there are, that post type cannot be written.

**Run the checker before publishing:** `python3 tools/check_facts.py <draft>`. Non-zero exit means
the draft does not ship. It was tuned against the last 40 real published posts, so a failure is
much more likely to be a real problem than a false alarm.

## Who is posting + the position (locked)

Ahmed Raza, Co-Founder & CTO of **Ployo** (`ployo.ai` = a full AI-interview platform: AI interviewers that screen, interview, and score candidates end-to-end; serving a range of companies across industries). First person, builder-in-the-arena.

**Position:** "AI founder with sharp hiring takes." The recruiting/hiring lens is the MAIN subject; the AI-builder seat is where he speaks FROM. (Previously recruiting was sometimes-spice; now it is the main dish.)

**Audience:** senior Talent Acquisition / recruiting / People & Culture leaders + founders/CEOs who own hiring, ACROSS industries. AU aged-care/health/staffing is only ONE proof point, never the boundary.

**Three rotating content pillars (one stream, mixed across the week so no week reads as one note):**
1. **THE STATE OF HIRING** — contrarian takes on what is broken in recruiting (resume/ATS keyword theater, ghosting, time-to-hire, interview theater, screening at volume, bias).
2. **AI x HIRING** — what AI actually changes for screening/interviews/scoring; reactions to AI-in-hiring news + regulation (NYC Local Law 144, EU AI Act); tasks-not-jobs / future-of-work.
3. **FOUNDER LENS** — lessons building AI interviewers + selling to TA leaders; specific-but-unverifiable; never internal Ployo specifics.

**Guardrails:** no internal Ployo specifics (which model in prod, internal costs, client names); speak as a builder, NEVER pose as a 15-year career recruiter; honor the AI-in-hiring messaging spine (explainable, human-in-the-loop, bias-aware) on sensitive ground; never dunk on named people/competitors; never overclaim a Ployo capability/number. Full voice rules in `config/persona.md`.

## LinkedIn — what wins (THE LIVE CHANNEL)

- **Hook before the fold:** only the first ~140 characters (≈ 2 lines) show before "…see more". Front-load the hook so it stands fully alone above the fold. No throat-clearing. The strongest hook shapes for this senior audience (research-ranked): curiosity-gap / state-then-withhold (highest engagement), contrarian / industry-myth-buster, named-number / data-shock open, confession / cost-of-being-wrong, reframe-the-villain (the ATS / interview theater), specific-moment cold open, and pattern-callout of the audience's own behavior. A reader should be able to *disagree* with line 1.
- **Length ~1,000-1,900 characters** for a text post (~150-300 words; 1.18× reach at 1,000+; under 300 underperforms). Long enough to force the "see more" click (a top dwell signal) and develop ONE real idea; short enough to read on a phone. Short paragraphs, generous whitespace for skimmability (1-2 sentences per line, blank line between beats) — but do not overdo one-line-per-paragraph "broetry." Mix sentence lengths hard.
- **DEFAULT FORMAT = text-first, hook-driven posts.** Text posts win the COMMENT (the signal that matters for authority with senior buyers); carousels win impressions but not the argument. **A carousel is reserved for ~1x/week, only when the content is genuinely a framework, a numbered teardown, a before/after case, or a data deck** — never carousel an opinion (an opinion belongs in text where it can start an argument). When a carousel IS warranted, use 6-10 numbered slides (numbered decks get +20-30% dwell); the deck mechanics live in `config/carousel.md`. **This overrides the prior "carousel is the default LinkedIn format" policy.** ⚠ `state/settings.json` → `linkedin_format` is the operative switch: the current value is `"text-first"` (LinkedIn posts default to hook-driven text; a carousel ships only on a deck-worthy day with the weekly cap not spent — full gate in `config/carousel.md`); `"carousel"` forces every post to a deck (the old policy, DORMANT) and should NOT be used while text-first is the strategy. **Avoid native video** (reach down 36% YoY).
- **Structure:** hook (line 1-2, stands alone above the fold) → context/tension with a concrete detail or number (lines 3-8) → the payoff / verdict (lines 9-15) → a single specific question OR a strong closing line. Don't bury the hook below the fold. One post = one idea.
- **What drives the COMMENTS that distribute the post** (the algorithm weights substantive 15+ word comments 3-5x over "great post"): a clear, falsifiable VERDICT to agree or disagree with; a deliberate gap left for their expertise; a shared pain named with a real citable number; sensitive-but-fair framing on AI-in-hiring (human-in-the-loop / explainable / bias-aware EARNS respect; cheerleading AI as the fix pulls eye-rolls); founder-in-the-arena specificity.
- **Author replies in the first 60-90 minutes.** Replying substantively to early comments keeps the thread alive in the window that decides reach. This is part of the cadence, not optional.
- **Links suppress reach in the body** (50-70% reach penalty) → put any link in the **first comment**, not the post. If the publishing path can't auto-add a first comment, **omit the link** from the body rather than embed it. No external links in the body.
- **Golden hour:** comments in the first 60 minutes drive distribution → close on a sharp verdict OR one specific, answerable question (not generic "thoughts?"). Rotate the closer; do not end every post on a question (max ~1 in 3, checked against the last entries in the posting log).
- **Hashtags: 3-5** relevant ones, at the end.
- **No engagement bait** ("comment YES if you agree", reaction polls) — detected and penalized in 2026, and it reads junior to a senior audience.
- **Image = the branded Ployo template (config/styles.md), on MOST posts.** Portrait 4:5 (1088×1360) — LinkedIn shows portrait in-feed uncropped, so a designed infographic gets maximum real estate. The image carries the SAME single claim as the post. Skip the image only for a pure one-line hot-take that lands harder as text alone.

### LinkedIn pitfalls (auto-fail tells for this audience)
- Reads as a disguised ad / feature pitch. Lead with an industry problem and a point of view, never a capability.
- Cheerleading AI as the fix for broken hiring (the audience is actively skeptical; cost-per-hire and time-to-hire rose during the GenAI surge, only ~26% of candidates trust AI to judge them fairly). The credible stance is explainable, human-in-the-loop, bias-aware.
- Overclaiming a capability or number you can't back. Specific-but-unverifiable lived detail lands; unbacked superlatives don't.
- Ghost-written / corporate-neutral voice. The 2026 win is authentic individual voice with a clear position someone will disagree with.
- Posing as a career recruiter. The credible seat is builder-in-the-arena ("I build AI interviewers and here's what I've seen"), not borrowed practitioner credentials.
- Dunking on named people or competitors. Critique the system (ATS theater, interview theater), never a person.
- Generic "what do you think?" closers and safe recaps. End on a sharp verdict or one specific question.

## X / Twitter — what wins  ·  ⚠ DORMANT (X suspended 2026-06-14, revive if reinstated)

> **This entire section governs nothing while `@Ahmedraza_28` is suspended.** It is preserved for revival. The verdict-first / opinion-first principle below is GOOD and has been generalized to the live LinkedIn channel above (a reader should be able to disagree with line 1). When X returns, restore `channels`, `product_spotlight.enabled`, `takes.enabled` per the live-channel note at the top.

- **Replies are the #1 reach signal** (reply-that-gets-an-author-reply ≫ reply ≫ repost ≫ like). So **draft to provoke replies**: end on a sharp take, a real question, or a mild-contrarian claim that invites pushback. A post nobody wants to reply to is a dead post. Pushback comes from conviction at least as much as from questions — the closer-rotation rule in `persona.md` → "X voice — verdict first" (max 1 in 3 question-closers, checked against the last 5 X entries in the posting log) governs which closer this post gets.
- **Bookmarks ≈ 10× a like**, and dwell time boosts reach → "save-worthy" posts win (a crisp framework, a tight breakdown, a genuinely useful observation).
- **Body links KILL reach** (~0% engagement for non-Premium accounts). **Never put a link in the main tweet.** Options, in order: (1) no link at all — let the take + image stand (default for hot-takes); (2) if a source link genuinely adds credibility, put it in a **self-reply** (tweet 2), never tweet 1.
- **Length (updated 2026-06-11b — THREADS are the depth vehicle):** Buffer's X length handling is unreliable for >280-char singles (rejected 543 chars and accepted 640 chars on the same day) — so never DEPEND on long-form. For research/spotlight posts with real depth, default to a **2-3 tweet thread**: tweet 1 = the verdict/take, standing fully alone in ≤280 chars (most readers see only it); tweet 2 = the evidence and numbers in full sentences (this is where the "lengthier" voice lives); tweet 3 (optional) = the owned bet or the source link. Threads boost dwell + bookmarks, the exact signals that grow reach. A long-form single (~400-700 chars) MAY be attempted when the argument doesn't paginate well, but on ANY Buffer length rejection fall back to the thread split (or a tight single) and note it in the posting log. Quick reactions stay a single sharp ≤280 tweet.
- **Hashtags: 0-2, usually none.**
- **Hard reach-killers (also reputation hits): ALL-CAPS, toxicity, spamming @-mentions.** Avoid all three.
- **Velocity + ~6h decay** → posts must be scheduled into live-audience windows, never dead hours.
- **Image dims:** landscape 1200×675 (16:9) or square 1080×1080. If 4:5 (1080×1350), keep the key content in the **top ~56%** (the feed crops to ~16:9). Do not assume vertical "wins" — it doesn't, it just crops.

## Cadence

~1 high-quality LinkedIn post per weekday, **skip Sunday** (`state/settings.json` → `skip_days`). Consistency beats raw volume, but a daily post that doesn't clear the bar underperforms 3-5x/week that does — so post on a weekday ONLY when the topic clears the quality gate; on a slow news day pull a bank-driven evergreen take rather than forcing a weak news reaction. Mix the three pillars across the week. Reserve ~1 slot/week for a genuine carousel deck. Reply to comments within the first 60-90 minutes of every post.

## Posting windows (audience anchor: Australia, Australia/Sydney local time)

> **⚠ OPERATIVE schedule = `state/settings.json` → `posting_windows_local` + `posting_timezone`** (currently `Australia/Sydney`), resolved to UTC each run via `python3 tools/posting_window.py` (Step 8), DST-aware. `posting_windows_utc` in that same file is only a stale-cache fallback, it goes an hour stale at every AEST/AEDT switch, never edit it by hand as the source of truth. To retime posts, edit `posting_windows_local` (and `posting_timezone` if the audience ever changes), no routine-prompt change needed.

**2026-08-08 reversal, read this before trusting an older instinct about "3-8pm/Wed-4pm":** that pattern was refuted below against 2025-era data. Buffer's July 2026 analysis of 4.8M LinkedIn posts found the peak has since shifted later in the day, so the schedule now deliberately follows it. Treat the two AU windows below as current, not the earlier US-anchored windows they replaced.

The audience is Australia, so the schedule now anchors purely to AU local time instead of splitting the difference with a US-overlap slot.

- **Window 1 (afternoon peak): 15:00-17:00 Australia/Sydney local.** Inside Buffer's 3pm-8pm local peak band.
- **Window 2 (evening peak): 21:00-22:30 Australia/Sydney local.** The strong late-evening slot the same analysis found, distinct from and later than the afternoon peak.
- **Best days: Wednesday, then Thursday and Friday.** Monday and Tuesday are the weakest days per the July 2026 data, weight posts toward Wed/Thu/Fri when only a few slots a week are optimized.
- **Mornings before noon local now underperform** relative to the two windows above, avoid scheduling into them.
- Floor every `dueAt` at now + 10 min. **Stagger around the diary**, which posts to LinkedIn in the ~12:45-15:00 UTC window, don't schedule within 90 min of a same-day diary post. The two AU-local windows above (05:00-07:00 UTC and 11:00-12:30 UTC in AEST, one hour earlier in AEDT) already clear that diary slot.

## Product spotlight — DORMANT (X-stream, off while X suspended)
Separate from the hiring stream above, there was a near-daily **X** post (and an occasional LinkedIn carousel) reacting to a notable **new product launch** (Product Hunt / Show HN) with a builder's lens. **It is OFF** (`state/settings.json` → `product_spotlight.enabled=false`) because X is suspended. Its ruleset lives in **`config/product-spotlight.md`** (quality gate, builder's-lens framing — never a thumbs-up/down verdict, never a dunk on the makers — grounding, X format, the LinkedIn-only-when-deck-worthy weekly cap). When X returns and it is re-enabled, all the persona + guardrail rules here still apply to it; it does NOT count against `research_per_day`.

## Hard formatting limits to encode
- **LinkedIn (LIVE): 3,000 char limit; "see more" fold at ~140 chars (front-load).** Target ~1,000-1,900 chars / ~150-300 words. Default text post; carousel only for a genuine framework/data deck ~1x/week (config/carousel.md).
- X (DORMANT): every tweet ≤280 chars (URL = 23) — Buffer can't be trusted past 280. Depth = a 2-3 tweet thread (tweet 1 stands alone); takes = single tight post (config/takes.md). Long-form singles opportunistic only, with thread fallback.
- Image: LinkedIn = branded Ployo template, portrait 4:5 (1088×1360), on most posts (config/styles.md). X (DORMANT) 16:9 (1200×675) or 1:1 (1080×1080).

## DO NOT encode — these sounded right but were REFUTED in verification
- "LinkedIn never penalizes over-posting / post unlimited" ✗ (keep 2-5/week).
- "Carousels get 596% more engagement than text" ✗ (top format, but not that number).
- "4-5×/week is the peak and 8+ hurts" ✗.
- "Link posts get a ~94% A/B view drop" ✗ (links hurt, but not that exact figure).
- "Vertical 4:5 images perform best on X" ✗ (they just crop to 16:9).

## Open items (stay conservative until validated)
- Posting-window numbers are research-recommended, not yet validated against Ahmed's own LinkedIn analytics: refine `posting_windows_local` (and `posting_timezone`) once real per-post reach data accrues.
- No verified figure for the X spam-detection ceiling on scheduled posts/day → if X is reinstated, stay at/under medium cadence (X 1-2/day).
- Premium *may* reduce the X link penalty (an Oct-2025 softening test) → still default to link-in-reply / no-body-link when X returns.
