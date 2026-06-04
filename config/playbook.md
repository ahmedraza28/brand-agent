# Platform Playbook — fact-checked (the drafting brain)

Source: deep-research run `wk8u6rt4l` — 107 agents, 25 sources, 17/25 claims confirmed via 3-vote adversarial verification. X engagement weights are 2023-vintage (the Jan-2026 rewrite redacted exact numbers), so treat them as directional but reaffirmed by 2026 sources. The agent must follow these rules when drafting.

## X / Twitter — what wins

- **Replies are the #1 reach signal** (reply-that-gets-an-author-reply ≫ reply ≫ repost ≫ like). So **draft to provoke replies**: end on a sharp take, a real question, or a mild-contrarian claim that invites pushback. A post nobody wants to reply to is a dead post.
- **Bookmarks ≈ 10× a like**, and dwell time boosts reach → "save-worthy" posts win (a crisp framework, a tight breakdown, a genuinely useful observation).
- **Body links KILL reach** (~0% engagement for non-Premium accounts). **Never put a link in the main tweet.** Options, in order: (1) no link at all — let the take + image stand (default for hot-takes); (2) if a source link genuinely adds credibility, put it in a **self-reply** (tweet 2), never tweet 1.
- **Length:** punchy. Hook in the first line. ≤ 280 chars/tweet (URLs count as 23). Thread (2-5 tweets) only for a story that genuinely deserves depth — threads boost dwell + bookmarks. Single sharp tweet for quick reactions.
- **Hashtags: 0-2, usually none.**
- **Hard reach-killers (also reputation hits): ALL-CAPS, toxicity, spamming @-mentions.** Avoid all three.
- **Velocity + ~6h decay** → posts must be scheduled into live-audience windows, never dead hours.
- **Image dims:** landscape 1200×675 (16:9) or square 1080×1080. If 4:5 (1080×1350), keep the key content in the **top ~56%** (the feed crops to ~16:9). Do not assume vertical "wins" — it doesn't, it just crops.

## LinkedIn — what wins

- **Hook before the fold:** only the first ~140 characters (≈ 2 lines) show before "…see more". Front-load the hook. No throat-clearing.
- **Length ~1,000-1,900 characters** for a text post (1.18× reach at 1,000+; under 300 underperforms). Short paragraphs, generous whitespace for skimmability — but do not overdo one-line-per-paragraph "broetry."
- **Format leverage:** document/**carousel** posts are the single top format (+39% reach, +30% engagement, used by < 5% of creators). v1 ships text + a single image; a carousel-PDF path is a high-ROI later upgrade for framework/breakdown posts. **Avoid native video** (reach down 36% YoY).
- **Links suppress reach in the body** → put any link in the **first comment**, not the post. If the publishing path can't auto-add a first comment, **omit the link** from the body rather than embed it.
- **Golden hour:** comments in the first 60 minutes drive distribution → **end with a question** that invites comments.
- **Hashtags: 3-5** relevant ones, at the end.

## Posting windows (verified — defaults; tune to real analytics later)

Audience timezone default = **US Eastern (ET)** (where AI-Twitter/LinkedIn peaks). Change here if the audience shifts.

- **X:** Tue-Thu, 12:00-18:00 ET. Mon-Thu acceptable. **Never Saturday.**
- **LinkedIn:** Tue 11:00-17:00 ET (strongest); Mon 13:00-14:00; Wed 11:00-16:00; Thu 11:00 + 13:00-17:00; Fri 11:00 + 13:00-14:00. **No weekends.**
- Pick a **random** time inside the day's window, **independent per channel** (X and LinkedIn get different times — anti-pattern, anti-bot). Floor every `dueAt` at now + 10 min.
- **Stagger around the diary**, which already posts to these same channels in the ~12:45-15:00 UTC window. Don't schedule within 90 min of a same-day diary post on the same channel.

## Hard formatting limits to encode
- X: 280 chars/tweet (URL = 23). Thread max a few tweets; keep it tight.
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
