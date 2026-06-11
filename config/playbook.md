# Platform Playbook — fact-checked (the drafting brain)

Source: deep-research run `wk8u6rt4l` — 107 agents, 25 sources, 17/25 claims confirmed via 3-vote adversarial verification. X engagement weights are 2023-vintage (the Jan-2026 rewrite redacted exact numbers), so treat them as directional but reaffirmed by 2026 sources. The agent must follow these rules when drafting.

## X / Twitter — what wins

- **Replies are the #1 reach signal** (reply-that-gets-an-author-reply ≫ reply ≫ repost ≫ like). So **draft to provoke replies**: end on a sharp take, a real question, or a mild-contrarian claim that invites pushback. A post nobody wants to reply to is a dead post. Pushback comes from conviction at least as much as from questions — the closer-rotation rule in `persona.md` → "X voice — verdict first" (max 1 in 3 question-closers, checked against the last 5 X entries in the posting log) governs which closer this post gets.
- **Bookmarks ≈ 10× a like**, and dwell time boosts reach → "save-worthy" posts win (a crisp framework, a tight breakdown, a genuinely useful observation).
- **Body links KILL reach** (~0% engagement for non-Premium accounts). **Never put a link in the main tweet.** Options, in order: (1) no link at all — let the take + image stand (default for hot-takes); (2) if a source link genuinely adds credibility, put it in a **self-reply** (tweet 2), never tweet 1.
- **Length (updated 2026-06-11b — THREADS are the depth vehicle):** Buffer's X length handling is unreliable for >280-char singles (rejected 543 chars and accepted 640 chars on the same day) — so never DEPEND on long-form. For research/spotlight posts with real depth, default to a **2-3 tweet thread**: tweet 1 = the verdict/take, standing fully alone in ≤280 chars (most readers see only it); tweet 2 = the evidence and numbers in full sentences (this is where the "lengthier" voice lives); tweet 3 (optional) = the owned bet or the source link. Threads boost dwell + bookmarks, the exact signals that grow reach. A long-form single (~400-700 chars) MAY be attempted when the argument doesn't paginate well, but on ANY Buffer length rejection fall back to the thread split (or a tight single) and note it in the posting log. Quick reactions stay a single sharp ≤280 tweet.
- **Hashtags: 0-2, usually none.**
- **Hard reach-killers (also reputation hits): ALL-CAPS, toxicity, spamming @-mentions.** Avoid all three.
- **Velocity + ~6h decay** → posts must be scheduled into live-audience windows, never dead hours.
- **Image dims:** landscape 1200×675 (16:9) or square 1080×1080. If 4:5 (1080×1350), keep the key content in the **top ~56%** (the feed crops to ~16:9). Do not assume vertical "wins" — it doesn't, it just crops.

## LinkedIn — what wins

- **Hook before the fold:** only the first ~140 characters (≈ 2 lines) show before "…see more". Front-load the hook. No throat-clearing.
- **Length ~1,000-1,900 characters** for a text post (1.18× reach at 1,000+; under 300 underperforms). Short paragraphs, generous whitespace for skimmability — but do not overdo one-line-per-paragraph "broetry."
- **Format leverage:** document/**carousel** posts are the single top format (+39% reach, +30% engagement, used by < 5% of creators) — so they are now the **default LinkedIn format**, not just for framework/breakdown posts. The exact format rule lives in `config/carousel.md` and is driven by `state/settings.json` → `linkedin_format` (currently `"carousel"` = every LinkedIn post is a carousel deck; one per research topic). **Avoid native video** (reach down 36% YoY).
- **Links suppress reach in the body** → put any link in the **first comment**, not the post. If the publishing path can't auto-add a first comment, **omit the link** from the body rather than embed it.
- **Golden hour:** comments in the first 60 minutes drive distribution → **end with a question** that invites comments.
- **Hashtags: 3-5** relevant ones, at the end.

## Posting windows (verified — defaults; tune to real analytics later)

> **⚠ OPERATIVE schedule = `state/settings.json` → `posting_windows_utc`** (read by the runbook's Step 8). Currently `["04:00-05:00","15:00-17:00"]` UTC = **9-10am & 8-10pm Pakistan time** (one post per window: 00:30 UTC run → morning, 12:30 UTC run → evening). To retime, edit that array — no routine-prompt change. The ET windows below are the original engagement research and are kept for reference only; they are NOT what the routine schedules into right now.

Audience timezone default = **US Eastern (ET)** (where AI-Twitter/LinkedIn peaks). Change here if the audience shifts.

- **X:** Tue-Thu, 12:00-18:00 ET. Mon-Thu acceptable. **Never Saturday.**
- **LinkedIn:** Tue 11:00-17:00 ET (strongest); Mon 13:00-14:00; Wed 11:00-16:00; Thu 11:00 + 13:00-17:00; Fri 11:00 + 13:00-14:00. **No weekends.**
- Pick a **random** time inside the day's window, **independent per channel** (X and LinkedIn get different times — anti-pattern, anti-bot). Floor every `dueAt` at now + 10 min.
- **Stagger around the diary**, which already posts to these same channels in the ~12:45-15:00 UTC window. Don't schedule within 90 min of a same-day diary post on the same channel.

## Product spotlight — the second content stream
Separate from the AI-trend posts above, there is a near-daily **X** post (and an occasional LinkedIn carousel) reacting to a notable **new product launch** (Product Hunt / Show HN) with a builder's lens. It's governed by `state/settings.json` → `product_spotlight` and the full ruleset in **`config/product-spotlight.md`** (quality gate, the builder's-lens framing — never a thumbs-up/down verdict, never a dunk on the makers — grounding, X format, and the LinkedIn-only-when-deck-worthy weekly cap). It does NOT count against `research_per_day`. All the persona + guardrail rules here still apply to it.

## Hard formatting limits to encode
- X: every tweet ≤280 chars (URL = 23) — Buffer can't be trusted past 280. Depth = a 2-3 tweet thread (tweet 1 stands alone); takes = single tight post (config/takes.md). Long-form singles opportunistic only, with thread fallback.
- LinkedIn: 3,000 char limit; "see more" fold at ~140 chars (front-load).
- Image: X 16:9 (1200×675) or 1:1 (1080×1080); LinkedIn 1.91:1 (1200×627) or 1:1 (1200×1200). Generate at a size that crops cleanly to these.

## DO NOT encode — these sounded right but were REFUTED in verification
- "LinkedIn never penalizes over-posting / post unlimited" ✗ (keep 2-5/week).
- "LinkedIn best time = Wed 4pm / 3-8pm evening block" ✗ (use the late-morning/afternoon windows above).
- "Carousels get 596% more engagement than text" ✗ (top format, but not that number).
- "4-5×/week is the peak and 8+ hurts" ✗.
- "Link posts get a ~94% A/B view drop" ✗ (links hurt, but not that exact figure).
- "Vertical 4:5 images perform best on X" ✗ (they just crop to 16:9).

## Open items (stay conservative until validated)
- No verified figure for the X spam-detection ceiling on scheduled posts/day → stay at/under medium cadence (X 1-2/day).
- Premium *may* reduce the X link penalty (an Oct-2025 softening test) → still default to link-in-reply / no-body-link.
