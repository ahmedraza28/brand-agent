# Posting log

Append-only. One entry per run. Newest at the top. A run that posts nothing still logs a line (`no-post: <reason>`).

Format per published post: date, platform, topic_key, the EXACT text published, image style (or `none`), Buffer post id (or 'FAILED: <reason>'), dueAt (or 'draft').

---

## 2026-06-05T14:22:00Z

### nvidia-nemotron-3-ultra | X | DRAFT (addToQueue + saveToDraft)

**Text (tweet 1):** Nvidia shipped a 550B open-weight model yesterday. 1M token context, commercial license, 300+ tokens/sec.

For agents running over entire codebases, this isn't a press release thing.

Buried: Kimi K2.6 still scores higher. Best US open model. Not world's best.

**Thread tweet 2:** weights + full breakdown: https://davarion.com/en/blog/nvidia-nemotron-3-ultra-550b-open-weight-model-computex-2026/

**Image style:** isometric 3D render
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/nvidia-nemotron-3-ultra.png
**Buffer post id:** 6a231391bf58022d6075cc1b
**dueAt:** draft

---

### nvidia-nemotron-3-ultra | LinkedIn | DRAFT (addToQueue + saveToDraft)

**Caption:** Nvidia open-sourced a 550B model on June 4. Commercial license. 1 million token context window.

For agents doing multi-step reasoning over large codebases or documents, the context story here is real.

The performance gap with China's best open model is real too. Deck covers both sides.

What changes if a US frontier model is actually self-hostable?

#AI #Agents #Nvidia

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/nvidia-nemotron-3-ultra.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/nvidia-nemotron-3-ultra.png
**First comment (source):** https://davarion.com/en/blog/nvidia-nemotron-3-ultra-550b-open-weight-model-computex-2026/
**Buffer post id:** 6a231392bfc6cf5ee1e3e52d
**dueAt:** draft

---

## 2026-06-05T10:15:00Z

target-met: research_per_day=2 already reached this UTC day (topics: anthropic-ai-builds-itself [X], github-copilot-token-billing [LinkedIn]). No new posts this run.

---

## 2026-06-05T10:00:00Z

### anthropic-ai-builds-itself | X | LIVE (customScheduled)

**Text (tweet 1):** Claude wrote more than 80% of Anthropic's production code last month.

That number will probably have some asterisk I'm not seeing. But even half of it is wild.

Task horizons doubling every four months. At what point does the lab stop directing the work and start reviewing it?

**Thread tweet 2:** source: https://www.anthropic.com/institute/recursive-self-improvement

**Image style:** surrealist
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/anthropic-ai-builds-itself.png
**Buffer post id:** 6a221c9ac6e450c20fcd6c9b
**dueAt:** 2026-06-05T18:23:00Z

---

### github-copilot-token-billing | LinkedIn | LIVE (customScheduled)

**Text:** One developer reported their GitHub Copilot bill jumping from $29 to $750 last month. Same tools. New billing model.

GitHub switched from flat subscriptions to usage-based AI Credits on June 1. The logic makes sense from their side: agentic sessions and code review burn far more tokens than autocomplete. A fixed $19/month plan can't sustain that indefinitely.

The problem is the transition. Token consumption was invisible during flat-rate billing. Engineers optimized for heavy usage because the pricing rewarded it. Now the meter is suddenly visible, the baselines don't exist, and the bill can be genuinely surprising.

Autocomplete and Next Edit Suggestions are still free. AI Credits only kick in for chat, agent mode, and code review.

I use AI coding tools every day building Ployo. My read: if your workflow is mostly autocomplete, your bill doesn't move. If you're running multi-file agent tasks regularly, the math looks different. Worth checking your June statement.

What I'm watching longer term: whether metered pricing changes behavior, not just costs. Metering makes engineers think before they prompt. Could go either way.

What does your Copilot bill look like since June 1?

#GitHub #AITooling #Founders #AIBuilders #DeveloperExperience

**Image style:** 80s retro-futurism poster
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/github-copilot-token-billing.png
**First comment (source):** https://techcrunch.com/2026/05/30/what-a-joke-github-copilots-new-token-based-billing-spurs-consternation-among-devs/
**Buffer post id:** 6a221c9c73651bfe9d4add3e
**dueAt:** 2026-06-05T17:41:00Z

---

## 2026-06-04T11:30:00Z

### gemma-4-12b-local-multimodal | X | LIVE (customScheduled)

**Text (tweet 1):** Google shipped Gemma 4 12B yesterday. Text, images, audio natively in a 12B model. Apache 2.0. Runs on a 16GB laptop. HN noticed before most did (885 upvotes this morning). For anyone building agents off-cloud or on a tight API budget, this is worth knowing about.

**Thread tweet 2:** source: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/

**Image style:** blueprint / schematic
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/gemma-4-12b-local-multimodal.png
**Buffer post id:** 6a21734c46810dc859683eee
**dueAt:** 2026-06-04T18:47:00Z

---

### deepseek-7b-first-raise | LinkedIn | LIVE (customScheduled)

**Caption:** DeepSeek is raising $7 billion. First external round ever.

The lab that built its entire reputation on efficiency with less is now on the same capital escalator as OpenAI and Anthropic.

The round isn't closed yet. Term sheets being signed as of yesterday.

A few thoughts on what this means for open-source AI. Swipe through.

Once institutional money is in, do the open weights stay open?

#AI #OpenSource #DeepSeek #Founders #AIBuilders

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/deepseek-7b-first-raise.pdf
**First comment (source):** https://technode.com/2026/06/04/deepseek-in-talks-to-raise-7-billion-from-tencent-catl-and-other-investors/
**Buffer post id:** 6a21734dd0444b5c34df689f
**dueAt:** 2026-06-04T17:23:00Z

---

## 2026-06-04T10:19:38Z

### uber-ai-budget-cap | X | DRAFT (addToQueue + saveToDraft)

**Text (tweet 1):** Uber burned its entire 2026 AI coding budget in four months. Then capped Cursor and Claude Code at $1,500/month per dev. Finance noticed. The tools weren't failing, they were running nonstop. I wonder how many other companies are quietly in the same place right now.

**Thread tweet 2:** source: https://simonwillison.net/2026/Jun/3/uber-caps-usage/

**Image style:** pixel art
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/uber-ai-budget-cap.png
**Buffer post id:** 6a21512f81ad2375077da842
**dueAt:** draft

---

### anthropic-965b-ipo | LinkedIn | DRAFT (addToQueue + saveToDraft)

**Text:** Anthropic's revenue went from $9 billion to $47 billion in five months.

I had to look at that number twice.

Last week they filed confidentially for an IPO at a $965 billion valuation, surpassing OpenAI's $852 billion. The same company that a lot of people wrote off two years ago as the safety lab that wasn't going to compete commercially.

I build Ployo on top of Claude. Watched this from a small angle. The enterprise adoption in the last six months felt different. Not incremental. Something shifted in Q1 and I couldn't put my finger on exactly when.

The valuation is a headline. What I can't stop thinking about is the revenue number. It implies that somewhere in early 2026, enterprises stopped piloting AI and started just buying it. Not pilots. Actual purchase orders.

For founders building on top of these models: this IPO matters. Public companies manage pricing, SLAs, and roadmaps differently than private labs burning VC runway. What Anthropic commits to in its S-1 will shape what Claude costs and what it guarantees in 2027.

I don't know if that's net-good for builders yet. Still figuring it out.

What's your read? Does an Anthropic IPO make you more or less confident building on their APIs?

#AI #Anthropic #Founders #AIBuilders #Claude

**First comment (source link):** https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/

**Image style:** risograph print
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/anthropic-965b-ipo.png
**Buffer post id:** 6a21512fbaeed9f9a50b2b23
**dueAt:** draft

---
