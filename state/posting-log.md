# Posting log

Append-only. One entry per run. Newest at the top. A run that posts nothing still logs a line (`no-post: <reason>`).

Format per published post: date, platform, topic_key, the EXACT text published, image style (or `none`), Buffer post id (or 'FAILED: <reason>'), dueAt (or 'draft').

---

## 2026-06-06T12:40:00Z

### microsoft-mai-code | X | LIVE (customScheduled)

**Text (tweet 1):** Microsoft shipped a coding model this week. Built entirely in-house. Not on OpenAI.

In GitHub Copilot now. SWE-Bench Pro: 51.2% vs Claude Haiku 4.5's 35.2%.

They've put $13B into OpenAI and still built their own. Not sure what to make of the partnership after this.

**Thread tweet 2:** Announced at Microsoft Build on June 2. Full breakdown + model card: https://microsoft.ai/news/introducingmai-code-1-flash/

**Format:** text-only (OpenAI key returned 401 — image generation skipped; ~30% text-only variance intended)
**Buffer post id:** 6a2415ba8490187966a09692
**dueAt:** 2026-06-06T19:23:00Z

---

### microsoft-mai-code | LinkedIn | LIVE (customScheduled)

**Caption:** Microsoft shipped its own AI coding model this week.

MAI-Code-1-Flash. In GitHub Copilot now. SWE-Bench Pro: 51.2% vs Claude Haiku 4.5's 35.2%.

They built it end-to-end, without OpenAI. The same OpenAI they've put $13B into.

Deck covers what this actually changes for builders using Copilot or running agents.

Does a Microsoft-native model change which coding tool you reach for?

#AI #GitHub #Developers

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/microsoft-mai-code.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/microsoft-mai-code.png
**First comment (source):** https://microsoft.ai/news/introducingmai-code-1-flash/
**Buffer post id:** 6a2415baa1f61c27dba07c69
**dueAt:** 2026-06-06T16:47:00Z

---

## 2026-06-06T00:36:57Z

### chatgpt-dreaming-v3 | X | LIVE (customScheduled)

**Text (tweet 1):** 'Dreaming.' OpenAI's new ChatGPT memory system. Background synthesis from years of conversations, auto-updated. Factual recall up from 41% to 82% on their internal eval.

Catch: deleting a conversation doesn't erase what ChatGPT learned from it. What does that mean for trust?

**Thread tweet 2:** More on the architecture, the privacy controls, and the EU AI Act deadline: https://openai.com/index/chatgpt-memory-dreaming/

**Image style:** Swiss / International typographic
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/chatgpt-dreaming-v3.png
**Buffer post id:** 6a236c68556e567c77b9d9fd
**dueAt:** 2026-06-06T18:37:00Z

---

### chatgpt-dreaming-v3 | LinkedIn | LIVE (customScheduled)

**Caption:** OpenAI shipped a new memory architecture. They called it 'Dreaming.' Factual recall went from 41% to 82% on their internal eval.

There's a privacy catch buried in the docs most people skipped. The deck covers what changed and what it means if you're building on or with these systems.

Should 'smarter memory' and 'delete and it's gone' be the same toggle?

#AI #OpenAI #AIBuilders

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/chatgpt-dreaming-v3.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/chatgpt-dreaming-v3.png
**First comment (source):** https://openai.com/index/chatgpt-memory-dreaming/
**Buffer post id:** 6a236c69a0f5aeb6f4d841fc
**dueAt:** 2026-06-06T18:05:00Z

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
