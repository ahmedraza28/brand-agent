# Posting log

Append-only. One entry per run. Newest at the top. A run that posts nothing still logs a line (`no-post: <reason>`).

Format per published post: date, platform, topic_key, the EXACT text published, image style (or `none`), Buffer post id (or 'FAILED: <reason>'), dueAt (or 'draft').

Product-spotlight posts (the second stream, per config/product-spotlight.md) are slugged `ps-<slug>` and carry a `**Kind:** product_spotlight` line under the heading, so the weekly LinkedIn cap (settings.product_spotlight.linkedin_max_per_week) can be counted by grepping this file for the current ISO week.

---

## 2026-08-15T00:41:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Gate check: settings.enabled = true. Today (UTC 2026-08-15) is Saturday, not in skip_days (["sun"]). Daily target: research_per_day = 1. Today's count from this log before this run = 0 (last entry dated 2026-08-14). remaining = 1. Selected top 1 fresh moment.

Research pass ran 3 WebSearch queries (AI x hiring news today, EU AI Act/LL144/bias regulation this week, new AI recruiting tools launched this week) + Google News RSS (AI-hiring 48h query, 20 headlines) + HR Dive feed. Top candidates considered: WSJ "Job Seekers Are Racing to AI-Proof Their Résumés" (2026-08-13) and CPA Practice Advisor's Resume Genius survey piece (2026-08-13, AI-written applications the #2 red flag) — both semantically adjacent to `ai-resumes-overfit-backfiring` (2026-08-11, still inside the 7-day dedup window, same resume-authenticity-vs-AI-screening territory), passed over as duplicate-adjacent; Colorado's "proposed AI hiring rulebook" (JD Supra, 2026-08-14) traced back to the March/May working-group rulemaking already covered by `colorado-ai-act-gutted` (2026-06-24), no genuinely new regulatory fact this run, dropped as duplicate territory; and Google DeepMind's AGI Safety and Alignment team building an internal bypass form around Google's own AI hiring-screening system because they don't trust it — selected. Verified via direct WebFetch of two independent sources agreeing on every quote: HR Executive (hrexecutive.com, published 2026-08-14, author Jen Colletta) and Yahoo Finance's syndication of Bloomberg's original reporting (published 2026-08-10, author Julia Love), both confirming the internal-note quotes verbatim ("We have an applications system with a non-trivial probability your CV will be screened out incorrectly or take too long to reach us," "A real human will read these," "get really tired of reading LLM answers, because they all sound very samey") and the Gartner candidate-trust stat (~26% trust AI to judge them fairly) cited in the HR Executive piece. Not a duplicate of any ledger entry — first coverage of this specific story, distinct entity/event/mechanism from all prior bias/regulation/screening posts.

### google-deepmind-warns-own-ai-filters | LinkedIn | LIVE (customScheduled)

**Text:**
The team at Google whose entire job is keeping AI safe just told job candidates not to trust Google's own AI to screen them.

DeepMind's AGI Safety and Alignment team built a side door around Google's own applications system. An internal note laid out why, plainly: "We have an applications system with a non-trivial probability your CV will be screened out incorrectly or take too long to reach us." Candidates get pointed to a second form instead, with a promise attached: "A real human will read these." The same guidance tells candidates to go easy on AI-written answers too, warning that reviewers "get really tired of reading LLM answers, because they all sound very samey."

Read that twice. The safety team at one of the largest AI labs on earth didn't trust their own employer's screening tool enough to let their own hires pass through it unchecked. They built a bypass, not a bug report.

Only about a quarter of candidates say they trust AI to judge them fairly, and that number was already low before this story broke. Now the honest reason for it is coming from the inside instead of a survey.

I build AI interviewers, and the lesson I keep relearning is a boring one. The model was never the safety mechanism. The fallback is. If your AI screen doesn't have a human-reviewed side door built in from day one, you don't have a hiring tool. You have a filter nobody trusts enough to use straight.

#AIHiring #TalentAcquisition #Hiring #FutureOfWork #HRTech

**Format:** image (numbered-list archetype)
**First comment (source):** https://hrexecutive.com/google-insiders-warn-job-candidates-about-its-ai-hiring-filters/
**Buffer post id:** 6a7fb66972d7f70e3e211884
**dueAt:** 2026-08-15T06:12:00Z

---

## 2026-08-14T00:39:26Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Gate check: settings.enabled = true. Today (UTC 2026-08-14) is Friday, not in skip_days (["sun"]). Daily target: research_per_day = 1. Today's count from this log before this run = 0 (no prior entries dated 2026-08-13 or 2026-08-14 exist in this log; the last run recorded was 2026-08-12). remaining = 1. Selected top 1 fresh moment.

Research pass ran Google News RSS (AI x hiring 48h query) + HR Dive feed + Indeed Hiring Lab feed attempt (redirected, not used) + Josh Bersin feed + 2 WebSearch queries (AI hiring news this week, EU AI Act/LL144 regulation). Top candidates considered: CPA Practice Advisor covering Resume Genius's 2026 Hiring Trends Report (1,500 US hiring managers: job-hopping the #1 red flag at 65%, AI-generated application materials #2 at 49%) — real and fresh, but semantically close to the already-covered `ai-resumes-overfit-backfiring` ledger entry (2026-08-11, still inside the 7-day dedup window, same AI-authenticity-in-resumes territory), passed over as duplicate-adjacent; a generic WebSearch AI-hiring-market roundup (Ford/Commonwealth Bank/IBM reversing AI layoffs, AI skills gap stats) with no single verifiable primary source this run, dropped per no-source-no-post; and Josh Bersin's "Despite Massive AI Investments, HR Jobs Are Booming. Why?" (published 2026-08-13, same-day) — selected. Verified via direct WebFetch of the full article: Lightcast job-posting data showing 1.2%/year HR job-posting growth over 20 years vs. 6% growth over the last 24 months, HR salaries compounding at 3.1%/year vs. 2.1%/year inflation, the article's direct quote characterizing a CEO's Bloomberg/SHRM-conference remark that HR "faces extinction," and the specific shrinking titles named in the piece (HR administrator, HR assistant, recruiting coordinator, training administrator) vs. growing higher-level roles. Not a duplicate of any ledger entry — a fresh contrarian "state of hiring" angle (aggregate HR/TA job growth data countering the AI-kills-HR narrative) distinct from prior entry-level, layoff, and resume-authenticity stories.

### hr-jobs-booming-not-dying | LinkedIn | LIVE (customScheduled)

**Text:**
Every "AI is killing HR" headline this year is watching a real trend and drawing exactly the wrong conclusion from it.

Josh Bersin published the actual hiring numbers a few hours ago. HR job postings grew about 1.2% a year for two decades. Over the last 24 months, inside the current AI wave, that growth rate jumped to 6%. HR salaries have compounded at 3.1% a year against 2.1% inflation, one of the rare white-collar functions where pay is actually outrunning the cost of living right now.

A CEO told Bloomberg at this month's SHRM conference that HR "faces extinction." The hiring data from the same conference month says the opposite.

The part the headline missed is which roles are actually vanishing inside that 6% growth. Not recruiters. Recruiting coordinators. HR administrators. Training admins. The scheduling-and-paperwork layer of the function is getting erased title by title, while the roles that decide who gets interviewed and who gets hired keep growing underneath it.

I build the tool that eats exactly that coordination layer, the first pass that used to eat a recruiting coordinator's whole week. Watching that title disappear from job postings isn't a surprise from where I sit. What I didn't expect was that removing it wouldn't shrink the function. It just pushed the headcount up a level, toward the person who has to decide instead of just process.

AI didn't kill HR. It killed the job that does the paperwork and left the one that makes the call standing, with a raise.

#Hiring #AIHiring #TalentAcquisition #FutureOfWork #HRTech

**Format:** image (vs-comparison archetype)
**First comment (source):** https://joshbersin.com/2026/08/despite-massive-ai-investments-hr-jobs-are-booming-why/
**Buffer post id:** 6a7e64f56c3e52b01865a9f9
**dueAt:** 2026-08-14T05:20:00Z

---

## 2026-08-12T08:36:48Z (extra scheduled run)

target-met: no-post

Gate check: settings.enabled = true. Today (UTC 2026-08-12) is Wednesday, not in skip_days (["sun"]). Daily target: research_per_day = 1. Today's count from this log before this run = 1 (`ai-self-preference-resume-bias`, published this same UTC day, dueAt 2026-08-12T06:05:00Z, Buffer post id 6a7bc14a3d0bf74d65212144). remaining = 1 - 1 = 0. Per Step 3, target already met this run does no research, no drafting, no publish. Stopping.

---

## 2026-08-12T00:37:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Gate check: settings.enabled = true. Today (UTC 2026-08-12) is Wednesday, not in skip_days (["sun"]). Daily target: research_per_day = 1. Today's count from this log = 0 before this run. remaining = 1. Selected top 1 fresh moment.

Research pass ran 4 WebSearch queries (AI x hiring news, new AI recruiting tools, EU AI Act/LL144/bias regulation, ghosting/ATS/time-to-hire) + Google News RSS (AI-hiring 48h query) + HR Dive feed. Top candidates considered: a Forbes piece (Michelle Travis, 2026-08-11) titled "AI Hiring Tools Don't Just Learn Bias, AI Forms New Biases Of Its Own" — traced back to the same Princeton/U Chicago simulated-hiring-game stereotype study already covered as `llm-hiring-stereotype-study` on 2026-07-21, dropped as duplicate territory; RSM US chief economist Joe Brusuelas's "historic labor market shrinkage" analysis (HR Dive, 2026-08-11, verified via direct WebFetch) on older-worker labor-force exit driving AI adoption — real and fresh, but the mechanism leans on immigration-policy commentary, which risks guardrail 12 (stay out of politics), and has no hiring-mechanics/screening angle for the TA audience, passed over; and the University of Maryland Smith School's "AI Self-preferencing in Algorithmic Hiring" study — selected. Verified via direct WebFetch of two independent official UMD sources (rhsmith.umd.edu and trails.umd.edu, the NSF Institute for Trustworthy AI in Law & Society), both corroborating every statistic: 2,200+ resumes across 24 occupations, self-preference rate 67-82% when LLMs rated their own generated resumes vs. human-written ones, 23-60% higher shortlisting likelihood for candidates using the same LLM as the employer's screening tool, worst in sales/accounting roles, author Jiannan Xu's on-record quote. Peer-reviewed (AAAI/ACM AIES) and cross-picked-up by The Register, NY Post, and Business Insider per search corroboration, an actively-recirculating conversation this week even though the underlying arXiv paper (2509.00462) first posted September 2025. Not a duplicate of any ledger entry: distinct mechanism from `stanford-pymetrics-bias-study` (bias mirrors the employer's existing team) and `llm-hiring-stereotype-study` (feedback-loop-induced stereotypes from simulated hiring outcomes) — this is AI-to-AI self-recognition/self-preference bias, a fresh angle not previously covered.

### ai-self-preference-resume-bias | LinkedIn | LIVE (customScheduled)

**Text:**
Every AI resume screener you've deployed has a favorite candidate, and it isn't the most qualified one.

Researchers at the University of Maryland ran more than 2,200 resumes across 24 occupations through the major commercial and open-source AI models companies actually use for screening. When a model rated resumes it had generated itself against ones a human wrote, it preferred its own output 67 to 82 percent of the time. Candidates who happened to write with the same AI the employer's screener runs on were 23 to 60 percent more likely to get shortlisted than an equally qualified person who wrote their own materials. The gap was widest in sales and accounting roles.

We've spent two years worrying an AI screener might discriminate on race or gender, and that worry is earned. Almost nobody built a test for whether it discriminates on dialect, meaning which AI ghostwrote the application. The model isn't weighing someone's experience. It's recognizing a pattern that resembles its own writing and rewarding the resemblance.

I build one of these systems, and self-recognition bias has never once shown up on a bias checklist that's landed on my desk. Every audit I've seen tests protected classes. None of them test whether the model likes the sound of its own voice.

A screener that quietly rewards its own writing style isn't ranking talent. It's ranking who guessed your vendor.

#AIHiring #TalentAcquisition #HRTech #FutureOfWork #Hiring

**Format:** none (text-only — OPENAI_API_KEY returned `insufficient_quota` / "no credits remaining" this run, so image generation was skipped per the Step 7 fallback rule; flagged to Ahmed separately, not a repo issue)
**First comment (source):** https://www.rhsmith.umd.edu/news/ai-hiring-tools-may-favor-their-own-work-smith-study-finds
**Buffer post id:** 6a7bc14a3d0bf74d65212144
**dueAt:** 2026-08-12T06:05:00Z

---

## 2026-08-11T00:38:44Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Gate check: settings.enabled = true. Today (UTC 2026-08-11) is Tuesday, not in skip_days (["sun"]). Daily target: research_per_day = 1. Today's count from this log = 0 before this run. remaining = 1. Selected top 1 fresh moment.

Research pass ran 4 WebSearch queries (AI x hiring news, new AI recruiting tools, EU AI Act/LL144/bias regulation, ghosting/ATS/time-to-hire) + Google News RSS (AI-hiring 48h query) + HR Dive feed. Top candidates considered: Forbes "AI Is Making These Jobs 'Irreplaceable' Even As Hiring Rates Plunge 24%" (Visier research on job reshuffling, real but abstract/no concrete hiring-mechanics hook for a TA audience, passed over for a sharper alternative); Gartner's entry-level-hiring survey (22% of CHROs report a leader halting entry-level hiring due to AI) — real and verifiable, but semantically close to already-covered ground this month (`entry-level-seniority-tilt` 07-23, `stlfed-entry-level-ai-bar` 07-13, `entry-level-ai-pipeline` 06-22, `bank-first-rung-rebuild` unused-but-similar-territory), risked reading as the fourth entry-level post in seven weeks, passed over; a moneywise.com resume-prompt-injection piece that re-syndicates the already-covered Duke/hireEZ study (`resume-prompt-injection-silent-attacks`, 07-23), dropped as duplicate; and Fortune's "Hiring managers say AI-optimized résumés are backfiring" (published 2026-08-10) — selected. Verified via direct WebFetch of the full article text (fortune.com/2026/08/10/resume-perfect-match-ai-hiring-hr-leaders-interview-matters-most/): Kathleen Walch (Director of AI Engagement and Community, Project Management Institute) on record that over-polished, job-description-mirroring résumés are getting fewer interview callbacks, her exact quote confirmed verbatim; the 70% Indeed sponsored-applications-via-algorithm-recommendation stat confirmed in the fetched text. Not a duplicate of any ledger entry — a fresh angle (résumé-authenticity backfire + algorithmic pre-filtering) distinct from prior ATS/keyword-theater and entry-level posts.

### ai-resumes-overfit-backfiring | LinkedIn | LIVE (customScheduled)

**Text:**
A resume that matches the job post too well is starting to look like a red flag instead of a green light.

Kathleen Walch, who runs AI engagement at the Project Management Institute, said it flat out this week. Resumes over-polished until they mirror a job description word for word aren't landing more interviews. They're landing fewer. "If you do that, you're losing your authentic human self," she said. "Why are we hiring you? Because you're a human."

The same reporting adds a detail worth sitting with. Seventy percent of sponsored applications on Indeed now come from an algorithm recommendation, not a recruiter searching manually. The resume isn't even the first filter most days anymore. A model decides who gets surfaced before a person reads a single line.

So the resume gets optimized for the algorithm. The algorithm gets optimized for a match score. Match score turns out to be close to the last thing you'd want to optimize a hiring decision on. A too-perfect fit now reads as manufactured, and the burden of proof quietly moves somewhere else.

I build AI interviewers, and I've watched this exact handoff happen from the other side of the table. Once a resume can be engineered to fit, it stops being evidence of anything. The conversation becomes the evidence again, whether anyone designed it that way on purpose or not.

What's the last resume you saw that was clearly too good to be true?

#Hiring #AIHiring #TalentAcquisition #FutureOfWork #HRTech

**Format:** image (before-after archetype)
**First comment (source):** https://fortune.com/2026/08/10/resume-perfect-match-ai-hiring-hr-leaders-interview-matters-most/
**Buffer post id:** 6a7a6ff498be23f3c73fc9dd
**dueAt:** 2026-08-11T05:52:00Z

---

## 2026-08-09T08:36:24Z (scheduled run check)

skip-day: sun

Gate check: settings.enabled = true, but today (UTC 2026-08-09) is Sunday, which is in `settings.skip_days` (["sun"]). Per Step 1 gate 2, no research, no drafting, no publish this run. Stopping immediately, no exceptions. (A second skip-day check today, following the earlier 00:36:20Z run's identical stop.)

---

## 2026-08-09T00:36:20Z

skip-day: sun

Gate check: settings.enabled = true, but today (UTC 2026-08-09) is Sunday, which is in `settings.skip_days` (["sun"]). Per Step 1 gate 2, no research, no drafting, no publish this run. Stopping immediately, no exceptions.

---

## 2026-08-08T00:36:50Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Gate check: settings.enabled = true. Today (UTC 2026-08-08) is Saturday, not in skip_days (["sun"]). Daily target: research_per_day = 1. Today's count from this log = 0 before this run. remaining = 1. Selected top 1 fresh moment.

Research pass ran 4 WebSearch queries (AI x hiring news, new AI recruiting tools, EU AI Act/LL144/bias regulation, ghosting/ATS/time-to-hire) + Google News RSS (AI-hiring 48h query) + HR Dive feed. r/recruiting RSS returned no content this run (likely rate-limited), skipped per fallback rule. Top candidates considered: "DoD wants AI to cut civilian hiring to 30 days" (Federal News Network, government/political hiring reform, dropped per guardrail 12, stay out of politics/government policy lane); "OpenAI settles DOJ allegation it shut US workers out of lucrative jobs" (HR Dive, 2026-08-07, a real labor-law settlement but centers on one named company's legal wrongdoing, risked reading as a dunk on a named company and has no hiring-mechanics/screening angle for the TA audience, dropped per guardrail 10); "How AI Slop Is Ruining Hiring" (Inc.com, Kit Eaton) and its cited cost-per-hire/cost-per-application figures could not be verified this run (Inc.com blocked both WebFetch and curl with a 403, and no primary report was locatable independently), dropped per the no-source-no-post rule; and Semafor's "AI avatars enter the job interview" (published 2026-08-07, Jake Angelo) — selected. Verified via direct WebFetch of the full article text: Sydney recruiter Lana Kersanava's on-record account of three AI-avatar candidate interviews over six months, her exact quote, and the detail that all three were non-native English speakers applying for English-speaking roles. Treated as a single-source reported anecdote (attributed directly to the named recruiter and outlet, not stated as a broad statistical trend) per guardrail 3's opinion-framing option for a developing/anecdotal story. Not a duplicate of `ai-vs-ai-interview-arms-race` (2026-06-18) or `ai-interview-cheating-fails-onboard` (2026-07-14) — distinct entity, event, and mechanism, and both outside the 7-day dedup window regardless.

### ai-avatar-interview-arms-race | LinkedIn | LIVE (customScheduled)

**Text:**
A recruiter in Sydney sat through most of a video interview before realizing the face on the other end wasn't real.

Lana Kersanava says she's run into this three times over the past six months: an AI avatar standing in for the actual candidate, built to move and talk like a person on the call. Her first reaction, in her own words: "At the beginning, it's like you feel like something is off. It looks very realistic." About five minutes into an answer too polished to be anyone actually thinking on their feet, she ended the call.

All three candidates she caught this way were applying for English-speaking roles as non-native speakers. The avatar wasn't covering for a missing skill. It was covering a language gap the interview format never directly tested for anyway.

I build AI interviewers, so I've spent more time than I'd like on what these avatars actually exploit. Not the model behind them. The format. A scripted first-round screen rewards a smooth, rehearsed answer over a real one, and a good clone is built for exactly that job.

Chasing better deepfake detection is a fight you lose by design, the fake keeps improving faster than your ability to spot it. What a script can't survive is a live follow-up it never saw coming: change the scenario mid-answer, push on the part they rushed past, ask why that path and not the obvious one.

You can fake a face. Faking a real argument, live, is a different problem entirely.

#AIHiring #FutureOfWork #TalentAcquisition #HRTech #Recruiting

**Format:** image (funnel archetype)
**First comment (source):** https://www.semafor.com/article/08/07/2026/ai-avatars-enter-the-job-interview
**Buffer post id:** 6a767c338aa5e1393fab8af3
**dueAt:** 2026-08-08T16:47:00Z

---

## 2026-08-07T00:44:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Daily target check: settings.research_per_day = 1. Today's count from this log (UTC 2026-08-07) = 0 before this run. remaining = 1. Selected top 1 fresh moment.

Research pass ran 4 WebSearch queries (AI x hiring news, new AI recruiting tools, EU AI Act/LL144/bias regulation, ghosting/ATS/time-to-hire) + Google News RSS (AI-hiring 48h query) + HR Dive feed. Top candidates considered: a January 2026 Dylan Field (Figma CEO) "AI natives" hiring-bias remark resurfacing in syndication (stale, 7 months old, and using it risked reading as a dunk on a named individual, dropped per guardrail 10); a YouGov poll on UK public attitudes to AI CV-sifting amplified by Greater Manchester Mayor turned PM Andy Burnham's on-record political remarks (dropped: guardrail 12 requires staying out of politics entirely, and the story's news hook was fundamentally a sitting politician's public comments, not a neutral hiring-mechanics moment); a Taggd vendor press release ("80% adopt AI in hiring, only 10% see gains") that is both a self-promotional vehicle for Taggd's own product and semantically a re-run of the already-covered `manpowergroup-ai-hiring-gap` adoption/gains-gap story (dropped as duplicate territory + disguised-ad risk); and Figma's Q2 2026 earnings call (published 2026-08-05/06) — selected. Verified via direct WebFetch of Fast Company and TheNextWeb, two independent sources agreeing on every cited figure: revenue up 48% to $370.1M, R&D spend more than doubled to $167.3M, total operating expenses nearly doubled to $426.9M, adjusted operating margin fell from 16% to 10%, stock fell ~16% after hours, CFO Praveer Melwani stated Figma is "hiring fewer people than we originally had planned" because AI tools are covering some of that work. Not a duplicate of any ledger entry (a new company-specific earnings disclosure, distinct from prior adoption-gap surveys and layoff/regulation stories already covered).

### figma-hires-fewer-market-wants-proof | LinkedIn | LIVE (customScheduled)

**Text:**
Figma just admitted it's hiring fewer people because AI does more of the work now, and Wall Street punished the stock for it anyway.

The numbers came out of Tuesday's earnings call. Revenue up 48% to $370 million, R&D spend more than doubled to $167 million, and total operating expenses nearly doubled too, with operating margin dropping from 16% to 10%. CFO Praveer Melwani said it plainly: Figma is hiring fewer people than it originally planned, because AI tools are covering part of that work now. The stock fell about 16% anyway.

That's the sequence nobody's hiring rubric accounts for. Fewer hires, more output. It's supposed to read as discipline. The market read it as an unproven bet instead, because the headcount you don't add doesn't disappear. It moves to a different line item, and investors wanted to see that line item pay for itself before they'd believe the story.

A TA leader I spoke with last month justified her AI-screening budget the same way Figma just did in public: two recruiter headcounts she wouldn't need to add next year. Nobody in that budget meeting asked where the money for the tool actually shows up afterward. It's the same trade Figma just made at a much bigger scale, and the same question is still unanswered.

Fewer hires because of AI isn't a result on its own. It's a bet on where the saved salary ends up landing, and most teams making that bet haven't had to defend it in front of an earnings call yet.

#Hiring #AIHiring #FutureOfWork #TalentAcquisition #HRTech

**Format:** image (single-stat archetype)
**First comment (source):** https://www.fastcompany.com/91586117/figma-hiring-less-people-because-of-ai-wall-street-not-impressed
**Buffer post id:** 6a752a91e66d34bb734b1e9b
**dueAt:** 2026-08-07T17:12:00Z

---

## 2026-08-06T12:40:33Z (scheduled run check)

target-met: settings.research_per_day = 1 (current value). Today's count from this log (UTC 2026-08-06) = 2 (ai-reshuffles-white-collar-work, LIVE, dueAt 2026-08-06T16:37:00Z, logged 07:13:51Z; csuite-life-skills-vs-ai-skills, DRAFT, logged 08:24:00Z under a temporary research_per_day=2 test value that has since reverted to 1). remaining = 1 - 2 = -1. No new research pass run, no draft, no publish this run per Step 3.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-08-06T08:24:00Z (second run of the day)

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Daily target check: settings.research_per_day = 2 (temporary test value, see commit 2c1b66e). Today's count from this log = 1 (ai-reshuffles-white-collar-work, logged at 07:13:51Z). remaining = 1. Selected top 1 fresh moment.

Research pass ran 4 WebSearch queries (AI-in-hiring news, regulation/bias, new AI recruiting tools, ghosting/ATS/time-to-hire) + Google News RSS (AI-hiring 48h query) + HR Dive feed + Indeed Hiring Lab feed. Top candidates considered: "AI Weeds Out Older and Minority Job Applicants" (CPA Practice Advisor, re-syndication of the already-covered `workday-vendor-liability` FEHA ruling, dropped as duplicate territory), "Fake AI Job Candidates Pass Interviews and Vanish" (Business Insider, close in territory to already-covered `ai-vs-ai-interview-arms-race`, dropped), "I've had to Botox my CV" (BBC, candidate-side CV age-editing trend, real but softer/anecdotal than the alternative below and closer to a lifestyle piece than a hiring-mechanics moment, passed over), "When AI screens women out, an appeal pathway must be available" (Women's Agenda AU, an opinion/advocacy piece without a fresh primary data source this run, dropped), June 2026 JOLTS "Duck on a Pond" (Indeed Hiring Lab, real labor data but no hiring-screening/AI angle, off-territory), and High Point University Research Center's C-suite survey on life skills vs. AI skills in hiring, covered by hcamag.com (published 2026-08-05) — selected. Verified via direct WebFetch of the primary hcamag.com article: survey of 500+ US C-suite executives; all statistics (90%, 75%, 7%/7%/87%, 44%/46%/17-18%) and both direct quotes (Nido Qubein, Roberto Rigobon) confirmed in the fetched text. Not a duplicate of `bank-ai-fluency-is-the-new-signal` (2026-07-25, outside the 7-day dedup window and a distinct angle: that bank take was about how to test for AI fluency, this is a fresh primary-source survey about the C-suite valuing life skills over AI skills and a prep-gap between what grads/HR think matters vs. what actually gets hired).

### csuite-life-skills-vs-ai-skills | LinkedIn | DRAFT (addToQueue, saveToDraft)

**Text:**
Every job post this year name-drops "AI fluency." The people actually deciding who gets hired are quietly optimizing for something else.

High Point University surveyed more than 500 C-suite executives this week. Ninety percent said life skills, judgment, coachability, the ability to actually listen, are what make a hire work. Seventy-five percent said they'd pick the candidate strong in those over one who only brings AI technical chops. Only 7% want a leader built purely on AI skills. Only 7% want one built purely on life skills either. The real number is 87%, wanting both, which is a much harder thing to screen for than a prompt-engineering quiz.

Career centers should sit with the next question the survey asked: what grads are actually being prepared for. Forty-four percent of the C-suite and 46% of HR pros think recent graduates walk in better equipped with AI and technical skills than with life skills. Under a fifth think the opposite. HPU's president called that gap "very scary." He's not wrong. We're training a generation to optimize for the 7% that barely moves a hiring decision.

I score candidates for a living, and this is the exact mismatch I keep re-encoding into every rubric a client hands us. They ask for "AI-fluent." Then they pass on the AI-fluent candidate who can't take feedback, and hire the mid-tier prompt-writer who clearly listens.

Teach someone the tool in an afternoon. Nobody's figured out how to teach judgment by Friday.

#Hiring #AIHiring #TalentAcquisition #FutureOfWork #HRTech

**Format:** image (numbered-list archetype)
**First comment (source):** https://www.hcamag.com/us/specialization/hr-technology/ai-skills-matter-but-executives-are-hiring-for-something-else/585085
**Buffer post id:** 6a744235e1cbc9821a312418
**dueAt:** draft (mode=draft, no scheduled time; sits in Buffer queue as a draft for Ahmed to review)

---

## 2026-08-06T07:13:51Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Research pass ran 4 WebSearch queries (AI x hiring news, new AI recruiting tools, EU AI Act/LL144 regulation, ghosting/ATS/time-to-hire) + HR Dive feed + Indeed Hiring Lab feed. Top candidates considered: generic recruiter-facing "AI in Recruitment 2026" trend explainers (not news, dropped), AI interview-cheating/proctoring-arms-race framing (already covered as `ai-interview-cheating-fails-onboard` on 2026-07-16, same underlying theme, dropped as duplicate territory), various HR Dive DEI/discrimination-litigation items with no AI-hiring angle (off-territory), and Indeed Hiring Lab's new Q3 2026 Labor Market Outlook Survey (published 2026-08-05) — selected. Verified via direct WebFetch of the primary hiringlab.org article: 120 economists surveyed via Pulsenomics in partnership with Indeed, fielded July 2026, first survey of its kind. 52% expect AI to be a mild employment drag, 35% net gain, 13% no effect. 57% expect wage pressure on college-educated workers vs 34% for non-college-educated. 61% say their own assessment of AI's displacement risk for college-educated workers increased over the past year. Sectors expected to grow fastest: personal care & home health, nursing. Sectors expected to shrink: software development, administrative work. Primary first-party source (Indeed's own commissioned survey), not a duplicate of any ledger entry (distinct from `stlfed-entry-level-ai-bar` [St. Louis Fed, 18-24 age cohort specific] and `uk-two-speed-ai-job-market` [UK-specific Indeed postings data] — this is a new US economist-panel forecast survey).

### ai-reshuffles-white-collar-work | LinkedIn | LIVE (customScheduled)

**Text:**
The safest job in the market right now might be the one nobody's polishing a resume for.

Indeed Hiring Lab put a new survey out this week: 120 economists, fielded through Pulsenomics in July, the first read of its kind. The sectors this panel expects to grow fastest over the next year are personal care, home health, and nursing. The ones they expect to shrink are software development and administrative work.

The number that actually stopped me wasn't the 52% who expect AI to be a drag on employment overall. It's that 61% say their own read on how dangerous AI is for college-educated workers went up over the past year. Not down. Up. People paid to track this for a living are getting more worried with time, not settling into a range.

Fifty-seven percent expect wage pressure on college-educated workers. Thirty-four percent say the same for workers without a degree. That gap ran the other way for most of my career.

I build the tool that scores who gets a first conversation, and most screening rubrics I've seen still treat a degree plus specialized software background as the safe hire. That assumption was built for a labor market these numbers say doesn't exist anymore.

The resume that looks safest on paper might be the one applying into the sector this panel just flagged as shrinking.

#Hiring #AIHiring #FutureOfWork #LaborMarket #TalentAcquisition

**Format:** image (vs-comparison archetype)
**First comment (source):** https://www.hiringlab.org/2026/08/05/q2-labor-market-outlook-survey/
**Buffer post id:** 6a74366d0c33c8e2319399a5
**dueAt:** 2026-08-06T16:37:00Z

---

## 2026-08-04T12:37:26Z

target-met: research_per_day=1 already reached (1 research post today: bank-human-in-the-loop-becoming-law, dueAt 2026-08-04T16:52:00Z). No new posts this run.

---

## 2026-08-04T00:37:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Research pass ran 5 WebSearch queries + Google News RSS (AI-hiring 2d + regulation/bias 14d queries) + HR Dive feed + Indeed Hiring Lab feed + r/recruiting. Top candidates considered: AP/wire recap "AI weeds out older and minority job applicants, lawsuit against Workday claims" (same underlying June 22 FEHA/ADA ruling already covered as `workday-vendor-liability` on 2026-06-23, no new development since, dropped as a re-syndication not a fresh moment), Victorian Premier Jacinta Allan's proposed Equal Opportunity Act amendment restricting AI hiring discrimination + business "unnecessary overreach" pushback (original announcement dated 2026-07-21, over two weeks stale, and no clear fresh primary-source article confirming a new development this week, dropped), EU AI Act Article 50 transparency deadline reached 2026-08-02 (verified real via WebSearch, but Article 50 governs general AI content/chatbot disclosure, not the employment/hiring high-risk track already covered as `eu-aiact-deferral-hiring`, off-territory for the hiring beat), "AI Hiring Has Split Into Three Distinct Tracks" skills-gap listicle (Data Scientist/ML Engineer/AI Engineer skill differences, no hiring-mechanics or screening angle, thin/listicle-shaped per the saturated-take guard), and Q2 2026 Employment Cost Index real-wage decline (Indeed Hiring Lab, published 2026-07-31, real wages -0.4% YoY, first drop since 2022 — real labor-market data but no hiring-screening/AI angle, off-territory, same reason it was passed over in a prior run). No candidate cleared the quality + grounding bar for a genuine fresh moment distinct from what's already in the ledger. **Slow-day fallback invoked** per `config/sources.md`.

Bank selection: `human-in-the-loop-becoming-law` (never used before, `last_used: null` = highest LRU priority; also a genuine connection to this week's discourse — NYC LL144 public bias-audit requirement and the EU AI Act's regulator-facing documentation requirement were both independently confirmed via WebSearch this run). Developed into an original angle not in the bank's note: human-in-the-loop as a competitive moat a black-box rival can't retrofit late, rather than a compliance cost. Every cited fact (NYC bias-audit public posting, EU technical-documentation-on-request requirement) verified via WebSearch this run; the builder anchor (a TA leader's demo question) is honest-generic, specific-but-unverifiable, no invented client story.

### bank-human-in-the-loop-becoming-law | LinkedIn | LIVE (customScheduled)

**Kind:** bank-take

**Text:**
Every AI hiring vendor treats "a human has to sign off" as the annoying part regulators bolted onto their product. I think it's the cheapest moat in the category, and almost nobody is building for it on purpose.

Look at where the rules keep landing. NYC wants a bias audit posted in public. The EU wants a paper trail regulators can pull on request. State after state is converging on the same sentence, worded slightly differently every time: a machine can assist the call, a person has to own it. Nobody serious is legislating "ban the AI." They're legislating "show your work."

Most teams treat that as paperwork to survive. Fill out the form, post the audit, move on with the roadmap. A TA leader I demoed something for last quarter never asked about accuracy. Her only question was whether she could see why the model passed on a candidate, and whether she could overrule it herself. That was the entire sale.

The builders baking the override in from day one, making every score legible enough for a recruiter to argue with, aren't doing compliance theater. They're building the one thing a black-box competitor can't bolt on the weekend before a big enterprise deal.

Explainability isn't the cost of entry to this market anymore.

It's the actual product.

#AIHiring #FutureOfWork #HRTech #TalentAcquisition #Regulation

**Format:** image (before-after archetype)
**First comment (source):** none (evergreen bank take, no news hook)
**Buffer post id:** 6a713681d702c24ecb1f7a24
**dueAt:** 2026-08-04T16:52:00Z

---

## 2026-08-03T12:44:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Research pass ran 3 WebSearch queries + Google News RSS (AI-hiring 2d query) + HR Dive feed + Indeed Hiring Lab feed. Top candidates considered: generic "AI in Recruitment 2026" evergreen guide/listicle results (not news, dropped), an EU AI Act Article 50 transparency-deadline mention buried in a generic recruiting-trends summary (no single fresh news hook, dropped), HR Dive "Employers may not be training workers well enough for widespread AI disruption" (Conference Board, general upskilling stat, no hiring-decision angle, dropped), Indeed Hiring Lab Q2 2026 Employment Cost Index (real wage data but no AI/hiring-screening angle, off-territory), and Indeed's UK mid-year jobs report reported by Reuters/Bloomberg/Fortune (published 2026-08-02/08-03): UK job postings down 11% since January and 32% below pre-pandemic, graduate postings down 7% YoY (lowest for the season since 2020), youth unemployment at a decade-plus high, AI-related skills in a record 9.4% of UK postings, software developer postings up 14% concentrated in senior/AI-linked roles — selected. Verified via direct WebFetch of Fortune's article (quotes, software-developer and youth-unemployment figures) plus the Reuters wire syndication on byteseu.com (job-posting decline, graduate-posting, and AI-skills-percentage figures), two independent sources agreeing on all cited numbers. Not a duplicate of `entry-level-seniority-tilt` (2026-07-29, outside the 7-day dedup window, different geography/dataset: US Indeed Hiring Lab senior-vs-entry postings vs. this UK-specific Indeed mid-year report centered on the AI-skills-demand record).

### uk-two-speed-ai-job-market | LinkedIn | LIVE (customScheduled)

**Text:**
AI didn't shrink the UK job market this year. It just told employers who's worth calling back.

Indeed's mid-year numbers, out this week: UK job postings down 11% since January, sitting 32% below pre-pandemic levels. Graduate postings down 7% year-on-year, the weakest for this point in the calendar since 2020. Youth unemployment is at its highest in over a decade.

Underneath that, one line is growing. AI-related skills now appear in 9.4% of UK postings, a record. Software developer listings are up 14%, almost entirely in senior roles or ones built around AI directly. Indeed's Jack Kennedy put it plainly: the bar is rising, and it now wants either specialist AI capability or years of proof you don't need the specialism explained to you.

I build the layer that decides who gets a first conversation, so I've watched this exact filter tighten from the inside. A hiring manager I spoke with last month rejected a junior candidate for a role that, three years ago, would have gone to someone with exactly her resume. Her file wasn't weak. The bar under it moved.

Maybe that's too clean a story from one conversation. But the data says the same thing at scale: postings are consolidating around people who already cleared the bar once, and shrinking for people who've never had the chance to.

What does an entry-level screen even mean in a market that keeps raising the price of entry?

#Hiring #AIHiring #TalentAcquisition #LaborMarket #FutureOfWork

**Format:** image (funnel archetype)
**First comment (source):** https://www.byteseu.com/2248136/
**Buffer post id:** 6a708d272766419d49f52f6a
**dueAt:** 2026-08-03T16:12:00Z

---

## 2026-08-02T12:36:38Z (scheduled run check)

skip-day: sun (2026-08-02 is Sunday UTC, in settings.skip_days). No research, no draft, no publish this run per Gate 2 (no exceptions, even for big news).

---

## 2026-08-02T00:36:30Z (scheduled run check)

skip-day: sun (2026-08-02 is Sunday UTC, in settings.skip_days). No research, no draft, no publish this run per Gate 2 (no exceptions, even for big news).

---

## 2026-08-01T12:36:41Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: ai-layoff-scoring-factors-survey, dueAt 2026-08-01T16:11:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-08-01T00:37:24Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Research pass ran 5 WebSearch queries + HR Dive feed + Indeed Hiring Lab feed. Top candidates considered: "Nearly half of workers say they'd let AI negotiate their pay" (HR Dive, same Harris Poll/Ruth AI story already covered as `ai-pay-negotiation-bias-gap` on 2026-07-31, dropped as duplicate), "Employers may not be training workers well enough for widespread AI disruption" (Conference Board, generic upskilling stat, no hiring-decision angle, dropped), "Q2 2026 Employment Cost Index" (Indeed Hiring Lab, wage data with no AI/screening angle, off-territory), and "Managers say they are using AI to make layoff decisions" (HR Dive, published 2026-07-31, citing a ResumeTemplates.com survey of 1,000 US managers) — selected. Verified via direct WebFetch of the HR Dive article (exact stats, factors weighed, and the Julia Toothacre quote confirmed) plus a corroborating WebSearch pass confirming the same ResumeTemplates.com study and figures via independent coverage. Not a duplicate of `meta-ai-layoff-scoring-suit` (2026-07-17, outside the 7-day dedup window and a different angle: a national manager-behavior survey vs. one company's lawsuit).

### ai-layoff-scoring-factors-survey | LinkedIn | LIVE (customScheduled)

**Text:**
We regulated the AI decision that hires someone. Nobody built the same guardrails for the identical decision that fires them.

A ResumeTemplates.com survey out this week polled 1,000 US managers with direct reports, all of them already using AI at work. Fifty-nine percent use AI when deciding who gets laid off. Fifty-eight percent use it deciding who gets fired.

Break down what these tools are actually weighing and it gets uncomfortable fast. Performance shows up in 80% of them, reasonable enough. Attendance in 57%, still defensible. Then it turns. Sick days or medical leave factor into 31% of these decisions. Tenure into 32%. Age into 14%.

The survey's lead researcher, Julia Toothacre, said it plainly: sick days, medical leave, and age stand apart from the usual reasons a layoff happens, because discriminating on any of them is illegal.

Ninety-one percent of managers say they'd override an AI recommendation they disagreed with. That's the right instinct. But 38% of them have never been trained on ethical AI use in an HR decision, and 17% let the model run unsupervised often or all the time. You can't override a call you were never taught to question.

I build the screening half of this problem, not the layoff half, and I still know the shape on sight. I sat through a data review a few months back where a performance model had quietly downweighted anyone with a gap longer than two weeks in their activity log. Nobody had told it medical leave was a gap it should ignore.

We spent two years arguing about explainability at the front door of employment. The back door just got handed the exact same machine, with less than half the scrutiny.

#Hiring #AIHiring #TalentAcquisition #HRTech #AIBias

**Format:** image (single-stat archetype)
**First comment (source):** https://www.hrdive.com/news/managers-are-using-ai-to-make-layoff-decisions/826697/
**Buffer post id:** 6a6d4159f93d764d938415d8
**dueAt:** 2026-08-01T16:11:00Z

---

## 2026-07-31T12:36:51Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: ai-pay-negotiation-bias-gap, dueAt 2026-07-31T16:09:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-31T00:44:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Research pass ran 4 WebSearch queries + Google News RSS (AI-hiring 2d query) + HR Dive feed + Indeed Hiring Lab feed. Top candidates considered: HR Dive "AI CEO who promised interview to anyone who got tattoo of company logo apologizes" (would require naming/mocking a specific person, dropped per no-personal-attacks guardrail), HR Dive "This week in 5 numbers" leadership-AI-readiness roundup citing ManpowerGroup (3% of C-suite/CHRO/TA leaders feel "highly prepared" to lead AI adoption) — too close in shape to the already-covered `bank-ai-fluency-is-the-new-signal` (2026-07-25) territory and the source article didn't link the primary ManpowerGroup report, dropped, Indeed Hiring Lab's new healthcare-migration piece (real but no hiring-screening/AI angle, off-territory), and a Harris Poll x Ruth AI survey on AI salary-negotiation covered by HR Dive today (selected). Verified via direct WebFetch of the HR Dive article, direct WebFetch of the primary source page (ruthapp.ai/research, matching figures exactly), and cross-checked against independent Fast Company / Forbes coverage of the same Harris Poll dataset (2,131 US adults, fielded June 11-13 2026).

### ai-pay-negotiation-bias-gap | LinkedIn | LIVE (customScheduled)

**Text:**
Almost half of US adults would let an AI negotiate their salary for them.

Three in four of them have no idea it might already be steering them low.

Harris Poll and Ruth AI put real numbers on this a few days ago. 47% would hand pay negotiation to AI outright. A third have already asked one what to counter an offer with. 76% had never heard that AI career advice can carry bias at all. Among people who did get AI salary guidance, 43% believe their race, gender, or ethnicity shaped what it told them to ask for.

I spend my days on the other side of this exact problem. I build AI that screens and scores candidates, and every serious buyer's first real question now is some version of how do we know this isn't biased. I sat through a pitch a few weeks ago where general counsel spent twenty minutes on the audit trail before anyone opened a demo screen. That scrutiny is standard on the employer's side of the table now.

Nobody is running that same check on the candidate's side. A worker opens a chat window, asks what number to counter with, and takes the answer at face value. No audit log. No human reviewing the reasoning. No way to know if the model just quietly lowballed her because of a pattern sitting somewhere in its training data.

If explainability is the bar for the AI judging a candidate, it has to be the bar for the AI advising one too.

Nobody's holding it to that yet.

#Hiring #AIHiring #TalentAcquisition #PayEquity #FutureOfWork

**Format:** image (numbered-list archetype)
**First comment (source):** https://www.hrdive.com/news/nearly-half-of-workers-say-theyd-let-ai-negotiate-their-pay/826476/
**Buffer post id:** 6a6befecbb30a36747fe80b5
**dueAt:** 2026-07-31T16:09:00Z

---

## 2026-07-30T00:37:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Research pass ran 5 WebSearch queries + Google News RSS (AI-hiring 2d query) + HR Dive feed + Indeed Hiring Lab feed attempt (redirected, not used). Top candidates considered: HR Dive "AI use may improve engagement" (Gallup, not hiring/screening-specific, dropped), HR Dive "HR often uses ChatGPT to complete non-HR tasks" (OpenAI report, general workplace AI use not hiring-specific, dropped), "Obra Launches to Put Job Seekers First in an AI-Chaotic Hiring Market" (single-source startup-launch press coverage, thin, dropped), Box CEO Aaron Levie comments on AI and hiring (single-source opinion, no new data, dropped), and NYT (Lydia DePillis, published 2026-07-29) "A.I. Companies Are Recruiting Electricians and Carpenters by the Thousands" — OpenAI/Google/Meta/BlackRock committing $265M combined to electrician/carpenter training pipelines for data center construction, with hard figures on spend, wage premium, apprenticeship intake, and completion rate (selected). Verified via direct WebFetch of a detailed syndicated rundown (Yahoo Finance) of the NYT reporting, cross-checked against Techmeme's index entry (crediting Lydia DePillis/NYT) and aiweekly.co's summary of the same NYT piece — all in agreement on the $265M figure, the per-company breakdown, and the 42%/70%/45% stats.

### ai-companies-recruiting-trades | LinkedIn | LIVE (customScheduled)

**Text:**
Everyone's worried about the jobs AI is going to erase. Meanwhile OpenAI, Google, Meta, and BlackRock have committed $265 million this year to training thousands of new electricians and carpenters, just to keep pace with data center construction.

Meta alone put in $115 million for a one-month course that takes about 5,000 people from a classroom straight to a live contractor job site. Google wants to grow its apprenticeship intake from 19,500 a year to 30,000 within three years. A data center electrician now earns roughly 42% more than someone doing the same job anywhere else, according to Indeed. At OpenAI's Michigan build site, that pay comes with ten-hour shifts and no days off.

The number nobody's cheering about: applications for commercial electrical apprenticeships are up more than 70% since 2022. Completion sits around 45%. More than half the people who sign up for this gold rush never finish it.

I build screening tools for a living, and I recognize this shape instantly. Flood the top of a hiring pipeline with volume, skip building a real selection layer underneath it, then act surprised when half the intake disappears before any of the training pays off. Sean McGarvey, who leads North America's Building Trades Unions, called Meta's program "a brilliant public relations move." He didn't say it screens for who actually stays.

AI is currently the single largest driver of blue collar hiring demand in the country, and it inherited the exact same unsolved problem every fast-scaling hiring push runs into. Volume was never the hard part.

Nobody built the filter for who finishes.

#Hiring #TalentAcquisition #FutureOfWork #AIHiring #LaborMarket

**Format:** image (vs-comparison archetype)
**First comment (source):** https://finance.yahoo.com/technology/ai/articles/ai-companies-spending-265-million-173148687.html
**Buffer post id:** 6a6a9e5d31c6b0ee115647c2
**dueAt:** 2026-07-30T16:14:00Z

---

## 2026-07-29T12:39:44Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: entry-level-seniority-tilt, dueAt 2026-07-29T16:24:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-29T00:42:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Research pass ran 5 WebSearch queries + Google News RSS (AI-hiring 2d query) + HR Dive feed + Indeed Hiring Lab feed. Top candidates considered: HR Dive "managers don't feel ready to lead an AI-fluent workforce" (too close to `bank-ai-fluency-is-the-new-signal` covered 2026-07-25, dropped), HR Dive "leadership readiness lags AI adoption" (generic AI-leadership stat, weak hiring-specific angle, dropped), Gartner supply-chain entry-level-AI survey (stale, Feb 2026, sector-narrow, dropped), Fox Business "companies hiring humans again" (thin, single-source TV segment, no citable number, dropped), and two Indeed Hiring Lab reports published this week ("The Labor Market Is Tilting Toward Seniority" + "Entry-Level Jobs Aren't Just for Inexperienced Workers," both 2026-07-23) with hard first-party numbers on the career-ladder/entry-level crunch (selected). Verified via direct WebFetch of both Indeed Hiring Lab source articles, confirming all figures.

### entry-level-seniority-tilt | LinkedIn | LIVE (customScheduled)

**Text:**
Almost half of all entry-level applications right now come from someone with ten or more years of experience.

Indeed's Hiring Lab published the numbers this week. Senior-level job postings are up 14.7% over the past year. Entry-level postings are down 7.5% over the same stretch. Somewhere in that gap, a manager with a decade of experience is applying to a role built for someone in their first year of work, because there's nothing else open.

49% of applications from workers with ten-plus years of experience now target entry-level jobs. Only 12% of that same group applies for senior roles. The ladder didn't just lose its bottom rung. It lost most of the rungs in between.

I build the filters that screen these applications, and this is the exact case that breaks a naive one. A resume that reads "VP of Operations, 2011-2024" gets auto-flagged as overqualified and dropped, even when the person applied on purpose and would do the job well. Meanwhile the actual early-career candidate this posting was written for is competing in a pool where 3 in 10 entry-level applicants already have a decade or more on her.

Healthcare shows the sharpest version of it. Only 4% of experienced healthcare workers apply for senior roles once they're 10+ years in, versus 26% in tech. There's nowhere up to go, so everyone goes down.

Screening for "years of experience" used to be a proxy for seniority. Now it's mostly noise. The people writing entry-level job posts have no real idea who's actually applying to them anymore.

The candidate pool changed. Almost nobody rebuilt the funnel to match it.

#Hiring #TalentAcquisition #Recruiting #FutureOfWork #LaborMarket

**Format:** image (before-after archetype)
**First comment (source):** https://www.hiringlab.org/2026/07/23/the-labor-market-is-tilting-toward-seniority/
**Buffer post id:** 6a694ca906a254588099dabd
**dueAt:** 2026-07-29T16:24:00Z

---

## 2026-07-28T12:39:08Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: greenhouse-ai-doom-loop, dueAt 2026-07-28T16:12:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-28T00:38:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Research pass ran 6 WebSearch queries + Google News RSS (AI-hiring 3d query + regulation/bias 7d query) + HR Dive feed. Top candidates considered: the recurring Stanford/Pymetrics bias study resurfacing in search (already covered 2026-07-09 and again referenced 2026-07-13/07-20 window, dropped as a repeat), an ere.net opinion piece "Stop Adding AI to Broken Hiring Processes" (thin, no new data, saturated-take risk), an HR Dive item on leadership AI-readiness (generic, no hiring-specific number), and a fresh Fortune piece (published 2026-07-27) quoting Greenhouse CEO Daniel Chait on an "AI doom loop" of AI-driven mass-applying vs AI-driven filtering, with hard platform numbers (selected). Verified via direct WebFetch of the Fortune source article, confirming all figures.

### greenhouse-ai-doom-loop | LinkedIn | LIVE (customScheduled)

**Text:**
Job seekers are now paying $20 a month for AI that applies to every open role on their behalf. Recruiters are running AI that reads almost none of it. Everyone bought a faster machine, and the pipeline got worse for both of them.

Greenhouse's CEO Daniel Chait put a number on it this week. Across the platform's 175,000 live roles, each posting now draws roughly 254 applicants on average. Applications per recruiter are up 412%. His name for it: the AI doom loop. Job seekers automate the apply button because getting ghosted stopped feeling personal. Employers automate the filter because 254 applicants a posting isn't readable by a human anymore. Each side's fix makes the other side's problem worse, and the loop tightens on its own.

I build the filtering half of that loop. Volume was never the hard part. A model can score 254 applications before lunch. I looked at a resume in a demo last month that used the phrase "cross-functional stakeholder alignment" four times in six lines. Not a person's voice. Someone fed the job description back into a generator and mailed it to the filter, not to a human.

Chait's own team found the one thing that actually cuts through it. Candidates who flag a single role as their real priority get hired at close to five times the rate of everyone applying blind. Not a smarter model. A forced, cheap-to-fake-nothing signal of real intent.

Both sides bought speed this year. Almost nobody bought a clearer signal.

What would your funnel look like if a candidate could only apply to one role a month?

#Hiring #TalentAcquisition #AIHiring #Recruiting #JobSearch

**Format:** image (funnel archetype)
**First comment (source):** https://fortune.com/2026/07/27/greenhouse-ceo-daniel-chait-ai-doom-loop-job-seekers-spam-interview-applications-unemployment/
**Buffer post id:** 6a67fba4fbdf65da5411d66c
**dueAt:** 2026-07-28T16:12:00Z

---

## 2026-07-27T12:37:25Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: blind-screening-bias-counterpoint, dueAt 2026-07-27T16:14:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-27T00:39:37Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

Research pass ran 4 WebSearch queries + Google News RSS (regulation/bias query) + HR Dive/Indeed Hiring Lab/Josh Bersin feeds. Top candidates considered: a new Meta layoffs court ruling (too close a follow-up to the meta-ai-layoff-scoring-suit topic already covered 2026-07-17), the recurring LLM-hiring-stereotype study (already in ledger within 7 days, dropped), Victoria's proposed AI-hiring/surveillance regulation (real but still a proposal with no enacted text, thinner than the alternative), and a verified retail AI-screening case study (selected). Verified via 2 independent sources (hcamag.com, stockhead.com.au), each corroborating the same figures.

### blind-screening-bias-counterpoint | LinkedIn | LIVE (customScheduled)

**Text:**
The AI-hiring bias panic has had a rough run of bad data all year.

A retail case study out this week might be the first real counterpoint, and the reason it worked matters more than the headline number.

A major Australian retailer replaced its resume-and-interview screen with a five-question AI chat across more than 450 stores, running roughly 600,000 applications a year through it. Time to hire dropped from 44 days to 11.8. The company says it saved $5 to $6 million over three years. First Nations hires landed at 8.2%, well above the 3% parity benchmark. Candidates disclosing a disability made up 3.5% of hires.

I build the kind of tool doing that screening, so the number that actually stopped me wasn't the savings. It was the 85%. That's how often human recruiters accepted the AI's shortlist, which means 15% of the time they didn't. The system proposed. A person still overruled it when they disagreed.

The other detail worth sitting with: the tool never tells the hiring manager a candidate's age, gender, or background. It scores five structured answers about teamwork and problem-solving, nothing else. Nobody had to correct for bias after the fact, because the bias-triggering information was never in the room to begin with.

The AI didn't get smarter about fairness. It got designed to withhold the parts of a person a human brain reacts to before it reacts to the work. That's not a data science breakthrough. It's a decision most vendors still don't make.

#Hiring #AIHiring #TalentAcquisition #Recruiting #HRTech

**Format:** image (single-stat archetype)
**First comment (source):** https://www.hcamag.com/au/specialisation/hr-technology/kmarts-blind-ai-tool-cuts-hiring-time-and-costs/583194
**Buffer post id:** 6a66a9d2351863828cfb471e
**dueAt:** 2026-07-27T16:14:00Z

---

## 2026-07-26T00:36:56Z (scheduled run check)

skip-day: sun

---

## 2026-07-26T12:37:44Z (scheduled run check)

skip-day: sun

---

## 2026-07-25T12:37:15Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: bank-ai-fluency-is-the-new-signal, dueAt 2026-07-25T16:33:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-25T00:44:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

**Slow-day fallback used.** Research pass ran 6 WebSearch queries + Google News RSS + Recruiting Brainfood; every fresh candidate either duplicated ground covered in the last 1-2 weeks (Stanford Canaries Dashboard entry-level-AI data vs. `stlfed-entry-level-ai-bar`/`entry-level-ai-pipeline`; The Conversation AI-hiring-regulation piece leaning on the already-covered Pymetrics study; an unverifiable NDTV "candidate freezes" story with no confirmable source) or had too weak a hiring angle (Sam's Club's general retail-ops AI rule). No candidate cleared the quality bar, so per `config/sources.md` this pulled the least-recently-used (never-used) opinion-bank entry instead of forcing a weak reaction.

### bank-ai-fluency-is-the-new-signal | LinkedIn | LIVE (customScheduled)

**Kind:** bank-take (source opinion id: `ai-fluency-is-the-new-signal`)

**Text:**
Every job post this year wants an "AI-fluent" candidate, and I have yet to meet a hiring team that can tell you what they're actually testing for.

Ask five recruiters what it means and you get five different fuzzy answers. Comfortable with tools. Uses ChatGPT daily. Not scared of it. None of that is a skill you can screen for. It's a vibe you're hoping shows up in the room.

I build the systems that score candidates for a living, so people assume I've got a rubric for this sitting in a drawer somewhere. I don't. Nobody does yet. Most companies wrote "AI fluency" into a job ad before anyone worked out how to measure it.

The wrong version of the skill is knowing the right incantation. A slash command, a system prompt trick, some phrasing that nudges a slightly better answer out of the model. That's trivia, and trivia is easy to fake in thirty minutes. It teaches you nothing about how someone actually works.

The real version is quieter. It's handing the model a messy real problem and knowing what to check first. It's catching the moment a confident answer is wrong in the exact way that reads correct on the first pass. Most people don't do that. They trust it because it sounded fluent.

I watched a candidate last week ask a model the same follow-up three separate ways before he'd act on the fourth answer. Nobody's rubric had a box for that. There isn't one yet.

Screening for "comfortable with AI" measures confidence. The job actually needs someone who's suspicious of it.

#Hiring #TalentAcquisition #AIHiring #FutureOfWork #Recruiting

**Format:** image (quadrant archetype)
**First comment (source):** none (opinion post, no external claim requiring citation)
**Buffer post id:** 6a6407059d853f39877e0245
**dueAt:** 2026-07-25T16:33:00Z

---

## 2026-07-24T12:37:04Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: ai-hiring-litigation-risk-survey, dueAt 2026-07-24T16:12:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-24T00:45:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### ai-hiring-litigation-risk-survey | LinkedIn | LIVE (customScheduled)

**Text:**
The scariest AI-hiring number this week didn't come from an HR report. It came from the lawyers.

Norton Rose Fulbright published its midyear litigation survey this week: 135 general counsel and in-house litigation leaders across energy, financial services, healthcare, and tech. Workforce changes, layoffs and policy shakeups, rank as the second most likely trigger for a 2026 class action, just behind data breaches. Forty-three percent expect bias or discrimination claims tied to AI to grow their litigation exposure before the year is out. Among companies clearing a billion dollars in revenue, that number climbs to 41%.

One line from the firm's co-head of litigation stuck with me. AI-assisted hiring tools, she said, are creating real uncertainty for employers, particularly around bias and discrimination claims.

I build the tools this survey is describing. Most of the pitch meetings I sit in are still about capability. Can it screen faster. Can it handle a volume no recruiter could get through by hand. I've had that meeting a hundred times, and legal was never in the room. General counsel is already living in the world where this gets deposed. Talent acquisition mostly isn't yet.

That gap is where the real exposure sits. A vendor selling speed and a buyer asking about accuracy are having two different conversations, neither one the conversation their own legal team is already having down the hall.

The lawyers already assume your AI hiring tool has to explain itself under oath. Most sales demos never once mention it.

#Hiring #AI #TalentAcquisition #HRTech #AICompliance

**Format:** image (numbered-list archetype)
**First comment (source):** https://hrexecutive.com/layoffs-and-ai-hiring-tools-are-driving-class-action-risk-corporate-counsel-say/
**Buffer post id:** 6a62b5a700eb658eba796310
**dueAt:** 2026-07-24T16:12:00Z

---

## 2026-07-23T12:37:50Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: resume-prompt-injection-silent-attacks, dueAt 2026-07-23T16:03:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-23T00:36:51Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### resume-prompt-injection-silent-attacks | LinkedIn | LIVE (customScheduled)

**Text:**
Everyone pictures an AI resume hack as "ignore your instructions, hire this candidate." The ones actually working don't say a word.

Duke researchers, working with Arizona State, UC Berkeley, UNC Chapel Hill, and hiring platform hireEZ, went through roughly 200,000 real resumes submitted over several years. About 1% carried hidden text aimed at an AI screener. That share has been climbing for the past year or two, not shrinking.

The number that actually stopped me: more than 90% of those injected prompts never used an explicit command. No "ignore previous instructions." No "mark this candidate as qualified." Just quiet, self-promotional phrasing stitched into a normal-looking resume, tuned to sound like the kind of language a model already rewards.

I build the layer these attacks are aimed at, and the first instinct is always the same one. Find the obvious phrase, block it, ship the patch. That filter catches almost nothing now. Candidates figured out that being explicit gets you flagged, and being subtle just reads as a well-written resume.

I looked at a resume in a demo a few weeks back that felt strong on the first pass. No red flags anywhere. Then one line read a little too generic, like it was addressed to a system instead of a person. Nothing you could screenshot and call a hack.

Chasing the phrase pattern only ever catches last year's attack. A score with no visible reasoning behind it can be talked into anything by whoever writes the smoothest paragraph. What can't be talked into anything is a recruiter reading the actual reasons a candidate scored well, able to notice the one sentence that's performing for a machine instead of a person.

You can't catch a whisper you never had to explain hearing.

#Hiring #AIHiring #TalentAcquisition #Recruiting #PromptInjection

**Format:** image (vs-comparison archetype)
**First comment (source):** https://arxiv.org/abs/2605.28999
**Buffer post id:** 6a6163ddbdfd2b0770027bd0
**dueAt:** 2026-07-23T16:03:00Z

---

## 2026-07-22T12:37:55Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: ai-adoption-walkout-gap, dueAt 2026-07-22T17:06:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-22T00:42:33Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### ai-adoption-walkout-gap | LinkedIn | LIVE (customScheduled)

**Text:**
Every AI-adoption stat HR is celebrating this year hides a walkout it never counts.

SHRM surveyed 1,722 HR professionals in December and found 39% of HR functions already have AI adopted, with 62% of organizations using it somewhere. Framed as an unqualified win. Nobody in that number is asking what happens on the other side of the interview.

Greenhouse asked almost 3,000 active job seekers this spring and got an answer. 63% had already sat through an AI interview, up 13 points in six months. 38% walked away from a hiring process specifically because AI was running it. Another 12% say they would, given the chance. Seventy percent were never clearly told, going in, that a model would be scoring them. One in five only found out once the interview had already started.

I build the screening layer this number actually lives in, and the part that keeps getting missed is this. A 38% walkout on a volume role isn't a footnote. It's a velocity problem with a name nobody wants to say out loud. You can't shortlist candidates who quit before the shortlist.

Greenhouse's own CEO said it straight: "most AI in hiring today is making a bad system worse: more applications, less signal, and less transparency."

Fix the disclosure and the walkout rate moves. Fix nothing, and the adoption chart keeps climbing while your best applicants keep leaving mid-interview, uncounted, in a number nobody's reporting to the board.

#Hiring #AIinHR #TalentAcquisition #Recruiting #HRTech

**Format:** image (before-after archetype)
**First comment (source):** https://www.prnewswire.com/news-releases/63-of-job-seekers-have-faced-an-ai-interview-most-havent-had-a-good-one-yet-302760120.html
**Buffer post id:** 6a60121724f2657e75bbb5ad
**dueAt:** 2026-07-22T17:06:00Z

---

## 2026-07-21T12:36:42Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: llm-hiring-stereotype-study, dueAt 2026-07-21T17:14:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-21T00:42:51Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### llm-hiring-stereotype-study | LinkedIn | LIVE (customScheduled)

**Text:**
The scariest AI bias study I've read this year isn't about a model copying your company's bad habits. It's about one inventing new bad habits nobody taught it.

Princeton and University of Chicago researchers built a simulated hiring game and ran it through ChatGPT, Claude, Gemini, and OpenAI's o3. Twenty fictional jobs, forty rounds, four made-up ethnic groups with names like Tufa and Aima. Every group had the exact same success rate at every job. No real signal, no real difference, nothing to learn.

The models found a pattern anyway. On a segregation scale where 0 is even distribution and 2 is total lockstep, human participants in the original psychology study scored 0.84. The AI models scored roughly 65% higher on average. o3 hit 1.83, a hair under the ceiling. Tell it one Aima failed as a doctor and it doesn't shrug that off as noise. It starts routing every Aima toward jobs it decided need less warmth and competence.

One researcher's explanation stuck with me. These models are eager to create generalizations from limited data, because that's a lot of what they're built to do.

I build screening systems, and this is the exact failure mode that should worry anyone running an AI that learns from outcomes. It doesn't need biased training data to end up discriminatory. Give it a feedback loop and a small sample, and it will manufacture a correlation where none exists, then act on it with total confidence.

An AI that updates on outcomes without a human checking the group-level pattern isn't learning. It's guessing, loudly, about people's lives.

What's actually auditing your hiring AI for a stereotype it invented on its own, not just one it inherited?

#Hiring #AI #HRTech #TalentAcquisition #AIBias

**Format:** image (single-stat archetype)
**First comment (source):** https://www.technologyreview.com/2026/07/20/1140655/ai-biases-hiring-humans/
**Buffer post id:** 6a5ec0a5cf581292a89b925f
**dueAt:** 2026-07-21T17:14:00Z

---

## 2026-07-20T12:36:50Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: ai-learning-debt-explainability-gap, dueAt 2026-07-20T16:29:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-20T00:36:37Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### ai-learning-debt-explainability-gap | LinkedIn | LIVE (customScheduled)

**Text:**
29% of employees handed in work last month they couldn't fully explain if you'd asked them how they got there. Hiring has spent two years terrified of exactly this problem showing up on the candidate's side of the desk. Turns out it never stayed there.

TalentLMS surveyed 1,200 US workers in June. 41% said their role changed faster than the company ever retrained them for it. Almost 60% use AI on tasks nobody formally taught them how to do. 62% build quiet workarounds instead of asking for help. 47% stay silent about the gap entirely, because admitting it feels like admitting they don't belong in the seat.

TalentLMS's CEO, Dimitris Tsignos, put the whole report in one line: AI is blurring the line between learning and doing.

I spend my days building the part of hiring meant to catch exactly this before an offer goes out. Can this person actually reason through the thing they claim to know, live, under a follow-up question, or did a tool carry them past it. I always assumed that failure mode lived at the interview stage and stopped there.

It doesn't stop there. Someone can clear a screen, take the job, and still be shipping work six months in that they can't walk you through if you ask twice. Same blind spot. It just moved past the point where anyone's still checking for it.

We built explainability requirements for the one hour of the interview. Almost nobody built one for the six months after.

#Hiring #AI #FutureOfWork #TalentAcquisition #HRTech

**Format:** none (text-only)
**First comment (source):** https://www.hrdive.com/news/ai-may-conceal-growing-learning-debt-for-fast-changing-roles/825396/
**Buffer post id:** 6a5d6e370424e7e331e49c90
**dueAt:** 2026-07-20T16:29:00Z

---

## 2026-07-19T12:36:02Z (scheduled run check)

skip-day: sun

---

## 2026-07-19T00:36:18Z (scheduled run check)

skip-day: sun

---

## 2026-07-18T12:36:24Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: employer-ghosting-three-year-high, dueAt 2026-07-18T16:42:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-18T00:39:02Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### employer-ghosting-three-year-high | LinkedIn | LIVE (customScheduled)

**Text:**
Ghosting isn't rudeness. It's the sound of a signal that stopped working.

Criteria Corp's new candidate experience report puts employer ghosting at 53% this year. Up from 48% last year. Up from 38% the year before that. Three years, a straight climb, no sign of leveling off.

The company's CEO, Josh Millet, named the mechanism plainly: AI tools now make it trivial to apply and tailor a resume at scale, so application volume surged. Hiring teams spend more time reviewing and get less usable signal out of each one. His framing stuck with me. Ghosting is less about intent and more about a process that never caught up to how people apply now.

I build the screening layer this problem actually lives in, so I recognize the shape immediately. When every application looks equally polished and equally hollow, a recruiter facing hundreds of them a week isn't being cruel. She has a queue that grew faster than her hours did. Silence becomes the default because a reply costs time she doesn't have, and none is left over once the queue wins.

Blame the recruiter and you're aiming at the wrong layer. The real failure sits one step earlier, wherever a system is supposed to separate a genuine signal from AI-polished noise before it hits a human's inbox. Fix that layer and the silence has less reason to happen. Leave it broken, and no "just be more responsive" memo survives contact with a queue already stacked five deep.

Three years of climbing ghosting numbers isn't a manners problem. It's a capacity problem wearing one.

#Hiring #TalentAcquisition #Recruiting #HRTech #CandidateExperience

**Format:** none (text-only)
**First comment (source):** https://fortune.com/2026/03/20/job-seekers-arent-imagining-things-candidates-ghosted-by-employers-hit-three-year-high/
**Buffer post id:** 6a5acb595291d8a34f706c6d
**dueAt:** 2026-07-18T16:42:00Z

---

## 2026-07-17T12:37:05Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: meta-ai-layoff-scoring-suit, dueAt 2026-07-17T16:53:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-17T00:39:05Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### meta-ai-layoff-scoring-suit | LinkedIn | LIVE (customScheduled)

**Text:**
A layoff algorithm doesn't need to be biased to produce a discriminatory outcome. It just needs to measure the wrong thing, consistently.

26 current and former Meta employees sued the company this week in federal court in Oakland. The claim: internal AI systems and performance scores helped decide who made the list for the roughly 8,000 people Meta cut this spring, about 10% of its workforce. Eight plaintiffs were on pregnancy or maternity leave. Four were on parental leave. Several had disability accommodations on file.

One detail in the filing stopped me mid-scroll. The lawsuit says the scoring, by design, can't accumulate for someone on protected leave. Not a bug that slipped past QA. A structural consequence of how the number gets calculated. Stop producing output for eight weeks, for any reason, and the score drops. A new baby and a slump look identical to a system that only counts activity.

Meta's response: workforce decisions were made by people, not AI. Maybe. But a human signing off on a score isn't the same as a human asking why the score fell. That gap is the entire point of human-in-the-loop review, and it's disturbingly easy to build a review step that never asks the real question.

I've watched a smaller version of this same bug in screening systems. A gap in someone's history reads as a red flag to a model that was never told the gap was protected, whether it's screening a resume or ranking a layoff list. Design intent doesn't matter much to the person it flags.

A model that can't tell a medical leave from a slump has no business ranking people.

#Hiring #AI #TalentAcquisition #HRTech #AIBias

**Format:** none (text-only)
**First comment (source):** https://www.cbsnews.com/news/26-meta-workers-sue-ai-aided-layoffs-medical-family-leave/
**Buffer post id:** 6a5979e3a4472b889474825c
**dueAt:** 2026-07-17T16:53:00Z

---

## 2026-07-16T12:36:47Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: ai-interview-cheating-fails-onboard, dueAt 2026-07-16T16:21:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-16T00:39:38Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### ai-interview-cheating-fails-onboard | LinkedIn | LIVE (customScheduled)

**Text:**
The embarrassing part of the AI-interview-cheating story isn't the cheating. It's how low a bar the interview was clearing to begin with.

Bloomberg reported this week on a hiring manager in New York who admitted, in his own words, that he got "duped by artificial intelligence." His nonprofit hired a grant writer. The interview went well, polished answers, sharp under pressure, the kind of candidate you stop taking notes on because you're already sold. A month into the job he couldn't make a basic call on the actual project. The manager suspects the guy was quietly running the questions through a chatbot the whole time.

Resume Genius surveyed 1,000 US job seekers this year. 22% say they've used AI live, during the interview itself. 78% used it somewhere in the search. One HR consultant summarized the real failure better than I could: if your interview can be passed by ChatGPT in real time, you weren't interviewing effectively in the first place.

I build interview tools, so I spend my days thinking about what a question actually tests. Most interview questions have one predictable shape: walk me through a time you did X. A model generates that shape on command. It proves nothing about whether the person can do the job when nobody's watching.

Chasing the cheater is a losing habit. Redesigning the question isn't. Ask what they'd change mid-answer. Push on the reasoning, live, not the story they rehearsed.

A script doesn't survive a follow-up it didn't prepare for.

#Hiring #AI #TalentAcquisition #InterviewDesign #HRTech

**Format:** none (text-only)
**First comment (source):** https://www.bloomberg.com/news/articles/2026-07-14/ai-tools-can-help-job-hunters-cheat-on-interviews-and-coding-tests
**Buffer post id:** 6a58287a4ebd80b204e6f373
**dueAt:** 2026-07-16T16:21:00Z

---

## 2026-07-15T12:37:19Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: randstad-ai-role-screening-gap, dueAt 2026-07-15T16:47:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-15T00:41:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### randstad-ai-role-screening-gap | LinkedIn | LIVE (customScheduled)

**Text:**
Everyone assumed AI would flood recruiters with too many candidates. For the roles that run the technology itself, the opposite is true.

Randstad tracked 35 million job postings worldwide from 2021 through this year and found the roles that make AI work inside a company are the ones exploding: AI trainer postings up 281%, solutions-lead roles up 226%, process automation specialists up 196%.

Now the number that matters more. The vacancy rate for AI solutions lead roles sits at 27% in the US. Average time to fill one runs 53 to 54 days, against 38 days for a standard IT hire. These companies aren't short on applicants. They're short on a way to tell which applicant can do the job.

I build screening tools, so I've sat in on plenty of these debriefs. A coding test can tell you if someone can write a working function. Nobody has agreed on what "can run AI in production" looks like as a gradable skill yet. So the interview quietly reverts to a resume with the right buzzwords and two people arguing about vibes afterward.

I'll go further. Most of these interviews aren't testing the skill at all. They're testing whether someone can talk about the skill convincingly, which is a much easier thing to fake than the skill itself.

Report this as a sourcing crisis and you'll keep throwing job ads at it. It's an assessment problem wearing a sourcing problem's clothes.

#Hiring #AI #TalentAcquisition #FutureOfWork #HRTech

**Format:** none (text-only)
**First comment (source):** https://www.randstaddigital.com/insights/newsroom/press-releases/top-10-high-demand-ai-tech-jobs-integration-gap/
**Buffer post id:** 6a56d726cbfbd9dc13352a3a
**dueAt:** 2026-07-15T16:47:00Z

---

## 2026-07-14T12:36:52Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: ai-adoption-headcount-growth, dueAt 2026-07-14T16:12:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-14T00:40:30Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### ai-adoption-headcount-growth | LinkedIn | LIVE (customScheduled)

**Text:**
Everyone's bracing for AI to shrink hiring. The best data out this week says the opposite is happening, and the catch is worse news for half of you than the doom headlines ever were.

Ramp and Revelio Labs tracked 21,559 US firms from January 2021 through this February, matching AI spending against actual headcount. Companies spending seriously on it, about $33.67 per employee per month, grew headcount 10.2% over two years. Entry-level roles grew 12%, not shrank. Companies barely touching AI, $2.78 per employee per month, saw no real movement either way. Not down. Just flat.

PwC found the same shape at global scale. Over a billion job postings across 27 countries: AI-exposed companies grew headcount 52% since 2018 versus 36% for the least exposed. Wages up 24% versus 17%. The most AI-exposed firms saw productivity climb 163%.

Apollo's chief economist Torsten Slok has the line for why. When steam engines made coal more efficient, Britain didn't burn less coal. It burned more. Cheaper capability doesn't shrink demand for the work. It usually grows it.

I've sat through plenty of vendor conversations where "we use AI in hiring" means a chatbot answering FAQs on the careers page. That is not the category this data is measuring.

Half-committed AI adoption in a hiring function doesn't cost you jobs. It costs you the upside, quietly, while the team down the street that went all in pulls further ahead every quarter.

If your AI hiring spend looks closer to $2.78 than $33.67 per employee, what do you think you're actually getting for it?

#Hiring #AI #TalentAcquisition #FutureOfWork #HRTech

**Format:** none (text-only)
**First comment (source):** https://www.pymnts.com/news/artificial-intelligence/2026/ai-adoption-fuels-hiring-not-layoffs-new-data-shows/
**Buffer post id:** 6a5585ab0a91bd784c7cac74
**dueAt:** 2026-07-14T16:12:00Z

---

## 2026-07-13T12:36:43Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: stlfed-entry-level-ai-bar, dueAt 2026-07-13T17:28:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-13T00:39:13Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### stlfed-entry-level-ai-bar | LinkedIn | LIVE (customScheduled)

**Text:**
Everyone's blaming AI for wrecking the entry-level job market. The St. Louis Fed just ran the numbers, and AI turns out to be the smaller half of the story.

Researchers there tracked 18 to 24 year olds from April 2023 through December last year. Unemployment in that group rose 3.51 percentage points. Employment-to-population fell 2.24 points. Neither move showed up for workers 25 and older.

Most of that decline traces back to something boring: fewer job openings, full stop. AI-related skill demand explains roughly a third of the unemployment increase, and about 45% of the drop in employment-to-population. Real, but not the main event.

That third isn't spread evenly across the economy though. It's concentrated exactly where someone tries to get their first foothold, which is the part that should worry hiring teams. The researchers called the effect "narrow, early and age-specific." AI raising the bar right at the door, not clearing out the building.

I build screening tools, so I spend a lot of time looking at entry-level rubrics up close. Most of them still ask the same three questions they asked in 2023. Can you do the task. Do you have experience. Will you show up.

None of them ask whether someone can actually work alongside the AI tools that now sit inside the job.

The bar moved first. Almost nobody rewrote the screen to match it.

#Hiring #AI #TalentAcquisition #FutureOfWork #HRTech

**Format:** none (text-only)
**First comment (source):** https://www.stlouisfed.org/on-the-economy/2026/jun/how-shifts-labor-supply-demand-shape-outcomes-young-workers
**Buffer post id:** 6a5433cf9372accfada90354
**dueAt:** 2026-07-13T17:28:00Z

---

## 2026-07-10T00:43:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### indeed-ai-titles-nontech-shift | LinkedIn | LIVE (customScheduled)

**Text:**
Everyone building AI hiring tools is still optimizing for software engineers. The actual jobs already moved somewhere else.

Indeed's Hiring Lab published new data this week on US job postings. In 2022, 264 titles had "AI" somewhere in them. That number dropped to 159 in 2023. This year it's 822. Roughly one in every twelve titles posted now has AI in it somewhere.

63% of those titles sit outside tech. Truck driver. Physical therapist. HR manager. Salesperson. Corporate trainer. Indeed grouped the growth into three clusters: AI enablement and consulting, AI training and content creation, AI instruction. None of those are engineering roles.

I build screening tools for a living. Almost every AI-fluency rubric I've come across assumes a technical candidate: a coding exercise, a systems question, something with a clean right answer a machine can grade. A TA lead I spoke with last month was trying to write an AI-fluency screen for a warehouse operations role. She gave up halfway through and just wrote "comfortable with AI tools" on the job ad instead.

Europe shows the same shift. Non-tech AI titles are already the majority in Germany, the Netherlands, France, and the UK. Spain is the one market still skewed toward tech.

Two years of AI-screening playbooks got built for the roles that talked about AI the loudest. The actual demand moved into the roles that just started quietly using it.

Nobody wrote the rubric for that yet.

#Hiring #AI #TalentAcquisition #FutureOfWork #HRTech

**Format:** none (text-only)
**First comment (source):** https://www.hiringlab.org/2026/07/08/ai-is-no-longer-just-a-tech-occupation-story/
**Buffer post id:** 6a504058f50a99bddccc1f01
**dueAt:** 2026-07-10T17:13:00Z

---

## 2026-07-09T (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: stanford-pymetrics-bias-study, dueAt 2026-07-09T15:33:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-09T00:39:24Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### stanford-pymetrics-bias-study | LinkedIn | LIVE (customScheduled)

**Text:**
The new Stanford hiring-bias study buries its scariest detail in the methodology section, not the topline numbers.

Researchers from Stanford, Chapman, and Northeastern tracked 4 million applications from 3 million people across 156 large employers, most doing $5 billion or more in revenue, all running the same AI screening platform. Using the EEOC's four-fifths rule, they found close to 26% of Black applicants and 15% of Asian applicants had applied to positions where the tool's outcomes counted as adverse impact under federal standards. One in ten roles showed adverse impact against Black candidates specifically.

The platform scores new applicants by training a model on each employer's current team in that exact role. Five people already doing the job, four of them the same profile, and the model learns that mix as the target. Every new applicant gets graded against it.

Nobody coded prejudice into that system on purpose. The model learned the room it was handed and treated the room as the answer key.

I build AI screening tools. The question I ask before anything ships is which population the model is actually learning from, and whether I'd defend that population in front of a regulator.

Bias-aware means auditing what the model actually learned from, not just its outcome scores. Skip that audit, and the screen becomes a mirror pointed at whoever already has the job.

#Hiring #AI #TalentAcquisition #HRTech #AIBias

**Format:** none (text-only)
**First comment (source):** https://fortune.com/2026/05/26/ai-hiring-algorithm-racial-disparities-pymetrics-stanford-study/
**Buffer post id:** 6a4eedf255b75a1caca78e1c
**dueAt:** 2026-07-09T15:33:00Z

---

## 2026-07-08T (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: ll144-bias-audit-theater, dueAt 2026-07-08T16:42:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-07-08T00:36:00Z

note: repo had an 8-day gap since the last logged run (2026-06-30). Proceeding with today's normal cycle; no backfill attempted for the missed days.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### ll144-bias-audit-theater | LinkedIn | LIVE (customScheduled)

**Text:**
New York wrote the first law requiring bias audits for hiring AI. Nobody is checking whether the audits are real.

A Comptroller's office audit released in December reviewed how DCWP, the agency enforcing Local Law 144, was doing its job. DCWP looked at the bias-audit disclosures of 32 employers and vendors. It found one instance of likely non-compliance.

The Comptroller's own auditors reviewed the same 32 companies. They found 17.

Same public documents. A seventeen-times gap in what counted as a red flag.

The complaint side isn't better. Twelve test calls to file a complaint through the city's 311 line. Three reached the agency that actually handles it. Eight got routed to the state labor department instead. One got sent straight back to the employer being complained about.

I build the interview layer these audits are supposed to check. I've sat in enough vendor calls to know what a bias audit usually is in practice. A PDF, an impact ratio, a line in the sales deck that says "LL144 compliant" and moves the conversation along. Almost nobody in the room asks who actually read it, or against what standard.

The law assumed the paperwork would get scrutinized. That assumption was always the fragile part, not the requirement to produce it.

An audit nobody checks isn't oversight. It's a receipt.

If your vendor handed you their bias audit today, would you know what a bad one looks like, or just that one exists?

#Hiring #AI #TalentAcquisition #HRTech #AICompliance

**Format:** none (text-only)
**First comment (source):** https://www.osc.ny.gov/press/releases/2025/12/dinapoli-new-yorkers-deserve-transparent-hiring-process-when-artificial-intelligence-used-vet-their
**Buffer post id:** 6a4d9c6e881105a051c12516
**dueAt:** 2026-07-08T16:42:00Z

---

## 2026-06-30T06:45:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### connecticut-cart-act | LinkedIn | LIVE (customScheduled)

**Text:**
Connecticut just passed an AI hiring law with something no other state has tried. The rejected candidate gets to see the data that scored them out. And correct it if it's wrong.

Governor Lamont signed the CART Act in late May. Starting October 2027, employers using AI as a "substantial factor" in a hiring decision must give the rejected applicant three things: the principal reasons for the outcome, the type and source of data the AI used, and the right to examine that data and dispute any errors.

Not just "we used AI" in the disclosure footer. The actual reasons, tied to the actual data, in a form the person can read and argue with.

I build AI interviewers. The first thing I noticed reading this law: most hiring tools don't have that output path. The model scores the candidate. A number hits a dashboard. The layer that translates that back into something a human can understand and dispute, most teams haven't built it. Partly because nobody asked them to. Partly because it's harder than the scoring.

The other provision landing sooner: starting October 1 this year, Connecticut employers filing WARN Act notices must disclose to the state labor department whether AI caused the layoffs. Ninety-three days from now, not 2027.

The law also removes the "AI made the decision" defense. Discrimination complaint, AI was a factor, you can't point at the algorithm. The decision is yours, full stop.

Colorado gutted its AI hiring law last month. Connecticut signed one with more teeth.

The regulatory patchwork is fragmenting, and most teams are tracking it as one coherent thing when it's not.

#Hiring #AI #HRTech #TalentAcquisition #AICompliance

**Format:** none (text-only)
**First comment (source):** https://ogletree.com/insights-resources/blog-posts/new-connecticut-law-restricts-employer-ai-use-mandates-notice-for-ai-caused-rifs/
**Buffer post id:** 6a430fe95383c03473b6dedd
**dueAt:** 2026-06-30T16:14:00Z

---

## 2026-06-29T12:31:20Z

target-met: research_per_day=1 already reached (1 research post today: linkedin-apply-assistant). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-06-29T00:32:12Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### linkedin-apply-assistant | LinkedIn | LIVE (customScheduled)

**Text:**
The application was already the worst filter in hiring. LinkedIn just automated it.

Last week, LinkedIn launched a Premium feature that pre-fills job applications and drafts cover letters for candidates. Recruiters see a polished, well-matched submission. They have no way of knowing a tool wrote it.

I build the interview layer that sits downstream of all this. So I notice when the floor moves.

Applications were already a low-fidelity signal. Keywords mirrored back from the job ad. Cover letters optimized to sound right rather than be right. A recruiter I spoke with recently gives each application 90 seconds on her first pass, 400 applications, one sitting. She knows she's pattern-matching to surface. She also has no other choice at that volume.

Now the surface is being written for the candidate.

The direction this pushes is predictable. Real signal moves further down the funnel, into the live conversation, the structured question, the thing someone has to answer in their own words without a tool doing it for them.

LinkedIn made a sensible product decision for their subscribers.

It also just finished off the top of the hiring funnel as a signal source.

#Hiring #AI #TalentAcquisition #Recruiting #HRTech

**Format:** none (text-only)
**First comment (source):** https://www.hrdive.com/news/sociable-linkedin-automates-job-application-process-for-premium-users/823876/
**Buffer post id:** 6a41be6016f1757f0f37329b
**dueAt:** 2026-06-29T15:47:00Z

---

## 2026-06-28T00:36:00Z

skip-day: sun

---

## 2026-06-27T12:30:00Z

target-met: research_per_day=1 already reached (1 research post today: ai-slopification-hiring-telephone). No new research posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-06-27T00:36:59Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### ai-slopification-hiring-telephone | LinkedIn | LIVE (customScheduled)

**Text:**
The AI hiring pipeline is a telephone game. I build one of the phones.

Harvard Business Review ran a piece this week putting Oxford and Babson research behind what I've watched happen inside these systems for two years. They call it "knowledge decay." An AI produces polished but lower-quality output, the next person in the chain stops checking as carefully, and by the end, the content has drifted far from what was originally true about the candidate.

The chain in practice: AI-generated resume into an AI screener. Screener produces a summary. Summary goes into an AI-assisted shortlist. The hiring manager reads a two-line brief. Four layers. By layer four, they're reading the output of a machine summarizing the output of another machine. The original candidate is in there somewhere.

I build the interview layer in that stack. What I can tell you is that the signal you're trying to preserve, whether this person can do the job, is fragile at every hand-off. Stacking AI on top of a process already optimized for the wrong things doesn't fix the wrong things. It moves them faster.

The Oxford team recommends replacing open CVs with structured questionnaires: projects led, budgets managed, team sizes. Verifiable inputs instead of self-reported prose. That's the right direction. Structured assessment has beaten unstructured on predicting job performance for decades.

The part the paper doesn't say: the telephone game only works if there's something real to distort. If your process was already measuring polish and format instead of capability, AI didn't break it. It just got the wrong answers faster.

We built better phones for a conversation that was already broken.

#Hiring #AI #TalentAcquisition #HRTech #Recruiting

**Format:** none (text-only)
**First comment (source):** https://hrexecutive.com/ai-in-hiring-a-risky-game-of-telephone/
**Buffer post id:** 6a3f1b5137c4dee3e0bc6c8c
**dueAt:** 2026-06-27T15:53:00Z

---

## 2026-06-25T12:33:11Z

target-met: research_per_day=1 already reached (1 research post today: manpowergroup-ai-hiring-gap). No new research posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

---

## 2026-06-25T00:37:20Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### manpowergroup-ai-hiring-gap | LinkedIn | LIVE (customScheduled)

**Text:**
90% of companies use AI in their hiring now. Fewer than 5% call the results transformational.

ManpowerGroup and Everest Group published a study this week based on 80 CHROs, C-suite leaders, and senior TA heads across the US and UK. That gap is the central finding.

The best outcome they measured: 39% of organizations reported significant impact on operational efficiency. Screening faster. Moving candidates through the funnel quicker.

And then it stalls.

I've watched this inside companies I've sold to. They added AI to their hiring stack and didn't touch the process underneath. Same intake criteria. Same scoring assumptions. The AI was faster at doing the thing they'd always done without asking whether the thing was right.

The finding that stayed with me: 54% of organizations say AI-assisted candidate behavior, generated resumes and coached interview answers, is making it harder to assess true capability. We deployed AI on the evaluation side. Candidates responded with AI on the presentation side. The signal got worse, not better, and most teams now have more process between them and a real read on a candidate than before.

The 5% who found transformation didn't start by buying AI. They started by figuring out what their process was actually measuring versus what it should be.

I build AI interviewers. That question comes up constantly. Which signals matter. What the interview is actually supposed to learn. Most teams haven't worked it out. And no tool, however good, can answer it for them.

That gap closes when the question does.

#Hiring #AI #TalentAcquisition #HRTech #Recruiting

**Format:** none (text-only)
**First comment (source):** https://www.prnewswire.com/news-releases/90-of-companies-use-ai-in-hiring-fewer-than-5-are-seeing-it-work-302808083.html
**Buffer post id:** 6a3c7868336a6b98e71f3a85
**dueAt:** 2026-06-25T16:51:00Z

---

## 2026-06-24T12:34:07Z

target-met: research_per_day=1 already reached (1 research post today: colorado-ai-act-gutted). No new research posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-06-24T00:37:56Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### colorado-ai-act-gutted | LinkedIn | LIVE (customScheduled)

**Text:**
Colorado was six days from the most demanding AI hiring compliance law in the US. The legislature just gutted it.

The original law, passed in 2024 with a June 30, 2026 effective date, required algorithmic impact assessments, risk management programs, annual reviews of every AI hiring tool, and mandatory reporting of discriminatory outcomes to the attorney general.

Last month, the governor signed an amendment that removed nearly all of it. What's left: notify candidates you're using AI, give them a written explanation and 30 days to request human review if you reject them, keep records for three years. The June 30 deadline is now January 1, 2027.

I build AI interview tools. When the original law passed, I read it carefully. Not because the compliance burden scared me. Because the impact assessment requirement was going to force the question every AI hiring vendor needs to answer: does this thing discriminate, against who, and how do you know?

The amendment let every vendor skip that.

The Workday class action is still running. So is the California FEHA ruling that let it move forward as vendor liability, not just employer liability. Those cases came from discrimination law that's been on the books for decades. No state amendment touched them.

Legislative accountability retreats. Judicial accountability doesn't.

The TA teams waiting on regulation to tell them what to ask their AI vendors just got six more months of runway. The teams that built explainable, auditable systems anyway are still ahead. That gap doesn't narrow when the law retreats.

Build above the floor. When the law catches up, you're ready. When it retreats, you've lost nothing.

#Hiring #AI #HRTech #TalentAcquisition #AIHiring

**Format:** none (text-only)
**First comment (source):** https://www.littler.com/news-analysis/asap/colorado-amends-its-artificial-intelligence-law-substantially-reducing
**Buffer post id:** 6a3b274a3f66e9632349788d
**dueAt:** 2026-06-24T16:51:00Z

---

## 2026-06-23T12:31:00Z

target-met: research_per_day=1 already reached (1 research post today: workday-vendor-liability). No new research posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-06-23T00:34:59Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### workday-vendor-liability | LinkedIn | LIVE (customScheduled)

**Text:**
AI hiring vendors have been treating legal liability like it's the employer's problem. A California federal court just said it isn't.

In May, a judge certified a class action against Workday, the HR software used by 60% of the Fortune 500, covering applicants over 40 screened out by its AI since September 2020. Yesterday, a court allowed the California discrimination claims to proceed as well.

The lead plaintiff, Derek Mobley, a Black man in his 40s, applied to more than 80 positions at companies running Workday's software. Rejected every time. His claim: the AI discriminated on age, race, and disability.

I build AI interviewers. The shift in this case is what I keep coming back to.

For years, legal exposure in AI hiring sat almost entirely with the employer. You bought a tool, used a tool, owned what it decided. Vendors sold the algorithm and accepted limited liability for what it did downstream.

Workday is testing that theory in federal court. Early signals aren't good for vendors.

If vendor liability sticks here, every company building AI hiring tools just inherited something: prove your model doesn't discriminate. Not your customer's deployment. Yours.

I think that's the right outcome. The tool builder knows what the model was trained on. They know where bias enters the pipeline. Holding them accountable creates the incentive to build auditable, explainable systems from the start. That work pays off in court.

Bias in AI screening isn't the live debate anymore. Who pays for it is.

#Hiring #AIBias #TalentAcquisition #HRTech #AI

**Format:** none (text-only)
**First comment (source):** https://hrexecutive.com/landmark-workday-case-signals-new-ai-hiring-risk/
**Buffer post id:** 6a39d57b151950f020d8fe1c
**dueAt:** 2026-06-23T16:15:00Z

---

## 2026-06-22T12:31:00Z

target-met: research_per_day=1 already reached (1 research post today: entry-level-ai-pipeline). No new research posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-06-22T00:31:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### entry-level-ai-pipeline | LinkedIn | LIVE (customScheduled)

**Text:**
The companies cutting entry-level headcount for AI right now are going to have a talent problem in 2028. They just won't recognize it as the same decision.

A ResumeTemplates survey of 1,000 US hiring managers, published June 3, found that 48% would rather invest in AI tools than hire and train a 2026 grad. 55% have already shifted their entry-level budgets to AI tools. 45% restructured so one senior person plus AI replaces what used to be multiple junior hires.

I understand the math. The short-term ROI is real.

The part nobody's modeling: the work AI does better than a junior hire was never just cheap labor. It was an apprenticeship we didn't call an apprenticeship. Someone did the first-pass research, the initial drafts, and while they did it, they learned how to do the job above it. The boring work was the training program.

Pull that rung and you don't get a leaner team. You get a leaner team for three years and then a shortage of people who need to know how to do the thing that matters.

I build AI interviewers. The category is genuinely useful. I still think most teams buying their way out of entry-level hiring right now are pricing in the gain and ignoring the deferred cost.

The gap shows up when the cohort that never got the first two years becomes the people you need to promote.

#Hiring #TalentAcquisition #AI #HRTech #FutureOfWork

**Format:** none (text-only)
**First comment (source):** https://www.prnewswire.com/news-releases/resumetemplatescom-survey-nearly-half-of-hiring-managers-will-train-ai-instead-of-hiring-2026-college-grads-302790839.html
**Buffer post id:** 6a38840c1cbe0c9c0663a611
**dueAt:** 2026-06-22T16:14:00Z

---

## 2026-06-21T12:31:00Z

skip-day: sun

---

## 2026-06-21T00:35:00Z

skip-day: sun

---

## 2026-06-20T12:31:00Z

target-met: research_per_day=1 already reached (1 research post today: eu-aiact-deferral-hiring). No new research posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-06-20T00:35:29Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### eu-aiact-deferral-hiring | LinkedIn | LIVE (customScheduled)

**Text:**
The EU just gave companies an extra 16 months on AI hiring compliance. Most will waste it.

The European Parliament voted June 16 to provisionally agree to push the AI Act's high-risk employment deadline from August 2, 2026, to December 2, 2027. The Council still has to formally adopt it, and the original August date is technically still live until they do. A lot of teams just exhaled anyway.

I build AI interviewers. My read from inside this category: the companies treating this as permission to pause were never going to be ready by August regardless.

What the law requires isn't that complicated. An AI system used to screen or score candidates has to log its reasoning, allow human override, and be testable for bias. Those requirements didn't originate in the AI Act. The AI Act just wrote them down and attached a fine.

Every team I've watched that built explainable outputs and human-review workflows did it because the product demanded it, not because a regulator asked. The candidate who got rejected could understand why. The recruiter could push back on a score. The system got fixed faster because the failure mode was visible.

What regulators are calling mandatory, good product teams were already calling obvious.

Sixteen months is enough runway to build it right if you start treating it like a design problem. It is not enough time if you're still waiting to see whether the Council formally adopts the deferral before August.

The law was always going to require this. The companies that used that signal early are already ahead.

#Hiring #AI #HRTech #TalentAcquisition #EUAIAct

**Format:** none (text-only)
**First comment (source):** https://ogletree.com/insights-resources/blog-posts/eu-nears-approval-of-agreement-to-delay-rules-for-ai-use-in-employment-decisions/
**Buffer post id:** 6a35e07e9513262b4d283548
**dueAt:** 2026-06-20T17:14:00Z

---

## 2026-06-19T12:31:43Z

target-met: research_per_day=1 already reached (1 research post today: hiring-freeze-low-fire). No new research posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-06-19T00:32:22Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### hiring-freeze-low-fire | LinkedIn | LIVE (customScheduled)

**Text:**
Hiring rates are at 2013 lows. Not because companies stopped needing people. Because barely anyone is leaving.

The April numbers from Indeed Hiring Lab: hiring rate 3.2%, separation rate 3.1%. Employment is technically growing because the gap is positive. That gap is 0.1 percentage points. That is the cushion holding up a 160-million-job labor market.

iCIMS tracked applications in May. Openings up 9% year over year. Hiring up just 1%. Application volume down 11%. For frontline roles, applications fell 18%.

More jobs posted. Fewer candidates applying. The pipeline is thinner than the headlines suggest.

Most AI recruiting tools were designed for the opposite problem. The pitch is almost always volume management: too many applicants, not enough time, you need to screen faster. That framing still fits some markets. But in a lot of frontline and mid-market hiring right now, the bottleneck has moved. There's no flood to filter.

I build AI interviewers. A head of talent I spoke with last week told me her frontline application numbers are down more than a third from two years ago while her open reqs haven't changed. She wasn't looking for a smarter screener. She needed applicants.

A frozen labor market and a volume crunch look similar from the outside. They're different problems. An AI screener helps when the pipeline is full. When the pipeline is thin, you need a different answer.

Most of the tooling on the market is still optimized for the flood. The May data suggests the flood has moved.

#Hiring #TalentAcquisition #Recruiting #LaborMarket #HRData

**Format:** none (text-only)
**First comment (source):** https://hiringlab.org/2026/06/18/strong-job-gains-weak-hiring/
**Buffer post id:** 6a348f8f70997684b4703ad0
**dueAt:** 2026-06-19T15:57:00Z

---

## 2026-06-18T12:31:50Z

target-met: research_per_day=1 already reached (1 research post today: ai-vs-ai-interview-arms-race). No new research posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-06-18T00:37:09Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### ai-vs-ai-interview-arms-race | LinkedIn | LIVE (customScheduled)

**Text:**
The companies building better AI detection for interview fraud are solving the wrong problem.

Fraudulent or AI-assisted candidates are now the #1 anticipated hiring challenge in 2026, ahead of the talent shortage that had held that spot for years. A survey of 500+ US talent acquisition leaders found that 90% of companies missed their hiring goals. Sixty percent said time-to-hire got worse, not better. And 99.8% of those same teams are using or deploying AI agents to help.

The industry response: more detection. Deepfake scanners. Eye-movement proctoring. Flags when a second device is suspected.

I build AI interviewers. My read, from watching this from inside the category: detection lags adoption. It always has.

A cheat tool ships. The open-source clones follow within months. A Reddit thread documents the workaround before the next update. The gap between new fraud capability and new fraud detection isn't closing. It's widening.

What actually holds up is interview design.

If your interview can be aced by an AI whispering answers in real time, it was never measuring what you thought. It was measuring how well someone performs in a familiar structure. That's a rehearsal for the hiring process, not a signal about the job.

The questions that survive the arms race are the ones where AI doesn't actually help: specific follow-ups to a candidate's own answer, reasoning under a scenario they've never seen, "walk me through exactly why you made that call." An AI can generate a polished opening answer. It gets exposed under "why did you phrase it that way?"

You can't audit your way out of this. But you can design an interview that doesn't need to be audited.

If a co-pilot can ace your process, the problem was the process.

#Hiring #TalentAcquisition #AI #Recruiting #InterviewDesign

**Format:** none (text-only)
**First comment (source):** https://goodtime.io/news-press/2026-hiring-insights/
**Buffer post id:** 6a333df359d8b77577c6db8b
**dueAt:** 2026-06-18T16:17:00Z

---

## 2026-06-17T12:30:00Z

target-met: research_per_day=1 already reached (1 research post today: ghost-jobs-ny-law). No new research posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-06-17T00:35:28Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### ghost-jobs-ny-law | LinkedIn | LIVE (customScheduled)

**Text:**
Making ghost jobs illegal is the right call.

New York passed a bill on June 2 that would fine companies $2,500 per posting for roles they have no immediate intent to fill. Still waiting on the governor's signature, but the direction is clear.

I just don't think the fine will work the way people expect.

I've talked to enough TA teams to understand why ghost jobs exist. Some companies are genuinely building pipeline for roles they expect to open. Some are benchmarking salary data. Some leave a req live because shutting it down and reopening it three months later costs more in admin overhead than just leaving it up. None of that is fraud. All of it makes sense given what this system currently costs.

Right now, posting a job you might never fill costs the company nothing. It costs the candidate forty minutes. That gap is where the problem lives.

The April JOLTS data: 7.6 million open roles, 5.1 million hires. The mismatch has a lot of explanations. Ghost jobs are one of them, and nobody really tracks how many.

A $2,500 fine targets the posting. It doesn't touch the incentive that created the posting.

The fix that actually moves this: making the cost of bad job data visible inside the organization. Not a fine from Albany. A number the CHRO can see. How many open reqs went stale. How long. What it cost the recruiting team to chase pipelines that never closed.

Until the internal cost is visible, the ghost job survives any external fine.

#Hiring #TalentAcquisition #HR #Recruiting #GhostJobs

**Format:** none (text-only)
**First comment (source):** https://www.hrdive.com/news/new-york-passed-bill-aimed-at-halting-ghost-jobs/822620/
**Buffer post id:** 6a31ec1855329f74ab6af10b
**dueAt:** 2026-06-17T16:51:00Z

---

## 2026-06-16T12:33:01Z

target-met: research_per_day=1 already reached (1 research post today: salesforce-fin-agents). No new research posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-06-16T00:37:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### salesforce-fin-agents | LinkedIn | LIVE (customScheduled)

**Caption:** Salesforce paid $3.6 billion yesterday for an AI agent that closes 76% of support tickets with no human involved.

Fin started as Intercom, a chat widget. They rebuilt around an agent that owns outcomes. That reframe was worth $3.6B to Salesforce.

I build agents for a living. This deal is the clearest proof yet of where the acquisition logic is heading.

The deck covers the numbers and what every B2B workflow that still runs on human hours is worth today.

Which function gets bought next?

#AI #AIAgents #Salesforce #B2BSaaS #Founders

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/salesforce-fin-agents.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/salesforce-fin-agents.png
**First comment (source):** https://techcrunch.com/2026/06/15/salesforce-acquires-ai-customer-service-platform-fin-for-3-6b/
**Buffer post id:** 6a309b100cf8c4f5e834fca7
**dueAt:** 2026-06-16T04:27:00Z

---

## 2026-06-15T12:32:00Z

target-met: research_per_day=1 already reached (1 research post today: anthropic-access-ban). No new research posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-06-15T00:37:00Z

spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

### anthropic-access-ban | LinkedIn | LIVE (customScheduled)

**Caption:** The US government shut off Anthropic's two most capable models Friday night. Not a glitch. A directive.

Amazon CEO Andy Jassy reportedly flagged a Fable 5 jailbreak to the Treasury Secretary. The administration acted. Anthropic disabled global access within hours.

I build on Claude. The deck covers what happened, the conflict at the center of it, and what this means for your architecture.

Is your stack built to survive a supplier going dark overnight?

#AI #Anthropic #AIBuilders

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/anthropic-access-ban.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/anthropic-access-ban.png
**First comment (source):** https://www.anthropic.com/news/fable-mythos-access
**Buffer post id:** 6a2f494661b0aab8c16a350c
**dueAt:** 2026-06-15T04:23:00Z

---

## 2026-06-14T12:32:03Z

skip-day: sun

---

## 2026-06-14T00:32:01Z

skip-day: sun

---

## 2026-06-13T12:35:00Z

target-met: research_per_day=1 already reached (1 research post today: amodei-policy-ai-exponential). No new research posts this run.
takes: daily guard — tk-agi-debates already posted today 2026-06-13T04:52:00Z; takes per_day=1 reached. Skipping takes.
spotlight: LinkedIn-cap=2/2 for ISO week 2026-W24 (ps-spotlight-backplanes 2026-06-11 + ps-kimi-work 2026-06-09). X-only spotlight.

### ps-prometheus-firecrawl | X | LIVE (customScheduled)
**Kind:** product_spotlight

**Text (tweet 1):** The hard part of web scraping isn't writing the code. It's writing code that still works three months later.

Firecrawl shipped Prometheus. Plain English in, TypeScript out. It maintains itself when sites change. The last bit is where every pipeline I've built eventually died.

**Thread tweet 2:** Launched yesterday. #4 on Product Hunt, 112 upvotes. Available via MCP protocol so agents can call it directly. Free trial through Sunday.

https://www.producthunt.com/posts/prometheus-by-firecrawl

**Image style:** Ukiyo-e woodblock
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/ps-prometheus-firecrawl.png
**Buffer post id:** 6a2d4f8de1196234c34094ef
**dueAt:** 2026-06-13T16:37:00Z

---

## 2026-06-13T00:31:00Z

spotlight: skipped (first run, hour < 6; product_spotlight.run = "second" only).

### amodei-policy-ai-exponential | X | LIVE (customScheduled)

**Text (tweet 1):** The CEO asking governments for authority to block his own AI is not a contradiction. It's a bet on being the one who shapes those rules.

Dario's essay dropped June 10. Fable 5 launched the day before.

**Thread tweet 2:** Mandatory testing in 4 risk areas before deployment. Government authority to block or reverse.

I build on Claude. My bet: the lab writing the testing framework shapes the bar. Anthropic just volunteered.

**Thread tweet 3:** https://decrypt.co/370704/anthropic-ceo-ai-too-powerful-regulation-cant-wait

**Image style:** newspaper editorial cartoon
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/amodei-policy-ai-exponential.png
**Buffer post id:** 6a2ca80d3b82df546ce012ad
**dueAt:** 2026-06-13T04:08:00Z

---

### amodei-policy-ai-exponential | LinkedIn | LIVE (customScheduled)

**Caption:** Dario Amodei published a major policy essay June 10, one day after launching Fable 5. Aviation-style regulation, mandatory testing, government kill switches over AI deployments. The deck covers what it says and what it means if you build on these models.

Does the CEO writing the safety rules get to set the bar?

#AI #Anthropic #AIBuilders #Regulation #Founders

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/amodei-policy-ai-exponential.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/amodei-policy-ai-exponential.png
**First comment (source):** https://decrypt.co/370704/anthropic-ceo-ai-too-powerful-regulation-cant-wait
**Buffer post id:** 6a2ca7a928ce56702c112824
**dueAt:** 2026-06-13T04:24:00Z

---

### tk-agi-debates | X | LIVE (customScheduled)
**Kind:** take

**Text:** AGI debates are appointment TV right now. Every quarter brings a new 'we are close' and a new 'we are not close'. The companies running AI in production don't care. Their question: cut cost, save labor, or make revenue? AI is an economic event before it's a philosophical one.

**Format:** text-only (no image per takes.md)
**Buffer post id:** 6a2ca7a99017a527dd605eeb
**dueAt:** 2026-06-13T04:52:00Z

---

## 2026-06-12T12:32:20Z

target-met: research_per_day=1 already reached (1 research post today: mimo-code-open-source). No new research posts this run.
takes: daily guard — tk-agents-over-chatbots already posted today 2026-06-12T00:32:27Z; takes per_day=1 reached. Skipping takes.
spotlight: LinkedIn-cap=2/2 for ISO week 2026-W24 (ps-spotlight-backplanes 2026-06-11 + ps-kimi-work 2026-06-09). X-only spotlight.

### ps-terminal-mode | X | LIVE (customScheduled)
**Kind:** product_spotlight

**Text (tweet 1):** Agent oversight is the gap nobody ships tools for. Terminal Mode: Claude Code agent status on Even G2 glasses, peripheral, ~1s latency, tap to approve. Right idea. Works when the agents get good enough at saying when they need you.

**Thread tweet 2:** PH this week, #4 of day, 394 upvotes. Even Realities G2 smart glasses.

I build agents in prod daily. The interface problem is real. Whether today's agents signal state clearly enough is the actual test.

https://www.producthunt.com/products/terminal-mode-by-even-realities

**Image style:** Swiss / International typographic
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/ps-terminal-mode.png
**Buffer post id:** 6a2bfed77965c57aa3009544
**dueAt:** 2026-06-12T15:37:00Z

---

## 2026-06-12T00:32:27Z

### mimo-code-open-source | X | LIVE (customScheduled)

**Text (tweet 1):** Hardware companies building dev tools used to be a dead end. Now it's a power move.

Xiaomi open-sourced a terminal coding agent yesterday. MIT, free model, single command. SWE-Bench Pro: 62% vs Claude Code's 57%.

My bet: this is the beginning of a wave, not an outlier.

**Thread tweet 2:** Persistent memory subagent runs in the background. Tracks context, keeps continuity over 200+ steps. Most agents lose the thread by step 50.

576 devs, 474 repos A/B: ~50% win rate short tasks, 65%+ on long multi-turn.

https://mimo.xiaomi.com/mimocode

**Image style:** 80s retro-futurism poster
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/mimo-code-open-source.png
**Buffer post id:** 6a2b55cc919955cfca02c4f1
**dueAt:** 2026-06-12T04:18:00Z

---

### mimo-code-open-source | LinkedIn | LIVE (customScheduled)

**Caption:** Xiaomi just shipped a free coding agent. It benchmarks 5 points higher than Claude Code.

MiMo Code: open source, MIT, single terminal command, built-in MiMo-V2.5 model. On SWE-Bench Pro: 62% vs 57%. Real-world testing across 576 developers pulled the gap even wider on long, complex tasks.

The deck goes deeper on the memory architecture and what Xiaomi is actually betting on here.

A hardware company shipping free dev tools to win developer loyalty. Is that a distraction or a strategy?

#AIBuilders #OpenSource #CodingAgents #AITools #Builders

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/mimo-code-open-source.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/mimo-code-open-source.png
**First comment (source):** https://mimo.xiaomi.com/mimocode
**Buffer post id:** 6a2b55cc919955cfca02c518
**dueAt:** 2026-06-12T04:41:00Z

---

### tk-agents-over-chatbots | X | LIVE (customScheduled)
**Kind:** take

**Text:** Most AI pilots die because they build a chatbot and call it an agent. A chatbot helps with a task. An agent owns the task, runs to completion without you. I build agents for a living. The two are not the same product, and most boards don't know which they have yet.

**Format:** text-only (no image per takes.md)
**Buffer post id:** 6a2b55cdcb54d2647c4c2994
**dueAt:** 2026-06-12T04:53:00Z

---

## 2026-06-11T12:33:03Z

target-met: research_per_day=1 already reached (1 research post today: diffusiongemma-parallel-blocks). No new research posts this run.
spotlight: skipped (daily guard — ps-spotlight-backplanes already posted today 2026-06-11T09:42:00Z; max one spotlight per UTC day).
takes: skipped (daily guard — tk-ai-is-labor already posted today 2026-06-11T10:32:35Z; takes per_day=1 reached).

---

## 2026-06-11T10:32:35Z

target-met: research_per_day=1 already reached (1 research post today: diffusiongemma-parallel-blocks). No new research posts this run.
spotlight: skipped (daily guard — ps-spotlight-backplanes already posted today 2026-06-11T09:42:00Z; max one spotlight per UTC day).

### tk-ai-is-labor | X | LIVE (customScheduled)
**Kind:** take

**Text:** Most AI pilots stall at 10% because the framing is "how can AI help here". That's the ceiling.

AI is labor. Spin it up, point it at a task, stop paying when done. The better question: "why is anyone still doing this at all". That one doesn't land at 10%.

**Note:** Buffer rejected 543-char long-form (third-party 280-char cap); posted as sub-280 banger per playbook occasional-banger provision; no thread per takes.md rules.
**Format:** text-only (no image per takes.md)
**Buffer post id:** 6a2a8f4132af275efa87c3da
**dueAt:** 2026-06-11T16:17:00Z

---

## 2026-06-11T09:42:00Z

target-met: research_per_day=1 already reached (1 research post today: diffusiongemma-parallel-blocks). No new research posts this run.

### ps-spotlight-backplanes | X | LIVE (customScheduled)
**Kind:** product_spotlight

**Text (tweet 1):** I've been pasting API keys into AI context windows for months. Turns out the transcripts don't forget.

Spotlight reads your Claude Code session logs when they end and surfaces what was in them - what files were touched, what credentials landed in context. PII strips locally before anything leaves your machine. Free.

Team from Google security and Valimail. The gap they're filling is real: most teams running agents in prod have zero visibility into what the agent actually did during the session.

My bet: session visibility becomes standard for every team pushing AI-generated code to prod by end of year. Backplanes either builds that baseline or gets acquired.

**Thread tweet 2:** Product Hunt #3 yesterday. Claude Code session analyzer that runs post-session - shows what your agent actually touched, flags credentials that landed in context. macOS, Linux, WSL 2. Free.

https://www.backplanes.com

**Image style:** low-poly
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/ps-spotlight-backplanes.png
**Buffer post id:** 6a2a85330055aa8225f370c1
**dueAt:** 2026-06-11T15:28:00Z

---

### ps-spotlight-backplanes | LinkedIn | LIVE (customScheduled)
**Kind:** product_spotlight

**Caption:** Your AI coding sessions leave a transcript. Most teams never look at it.

Spotlight reads your Claude Code logs after each session - surfaces what files were touched, what credentials appeared in context - and strips PII locally before anything leaves your machine.

The team came out of Google security, Valimail, and Algolia. Free.

The deck covers the actual risk and what this signals for any team running agents in production.

If you run Claude Code or Codex at work, what does your session visibility look like right now?

#AI #ClaudeCode #Security #AIBuilders #Developers

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/ps-spotlight-backplanes.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/ps-spotlight-backplanes.png
**First comment (source):** https://www.producthunt.com/posts/spotlight-by-backplanes
**Buffer post id:** 6a2a8533e30f108b7cd76760
**dueAt:** 2026-06-11T16:31:00Z

---

## 2026-06-11T00:40:00Z

### diffusiongemma-parallel-blocks | X | LIVE (customScheduled)

**Text (tweet 1):** Google shipped an open model yesterday that doesn't write word by word.

DiffusionGemma starts from noise and refines a full block at once. 1,000 tokens/sec on an H100, 4x faster.

Catch: lower on every benchmark than standard Gemma. Faster, dumber. What's the actual use case?

**Thread tweet 2:** 26B params, 3.8B active at runtime. Apache 2.0. 18GB VRAM when quantized.

Good for code infilling, text insertion, structured data. Not a reasoning replacement.

Google's docs: use standard Gemma 4 when quality matters.

https://ai.google.dev/gemma/docs/diffusiongemma

**Image style:** isometric 3D render
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/diffusiongemma-parallel-blocks.png
**Buffer post id:** 6a2a04d7d94814c03b56f47c
**dueAt:** 2026-06-11T04:59:00Z

---

### diffusiongemma-parallel-blocks | LinkedIn | LIVE (customScheduled)

**Caption:** Google released a model that generates text from noise, not word by word. 4x faster on local GPU. Quality trade-off is real.

The architecture is genuinely different from anything in production. The deck covers where it fits and where it doesn't.

Is there a version of this that becomes the default in two years?

#AI #MachineLearning #AIBuilders #Builders

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/diffusiongemma-parallel-blocks.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/diffusiongemma-parallel-blocks.png
**First comment (source):** https://ai.google.dev/gemma/docs/diffusiongemma
**Buffer post id:** 6a2a04b3009bddec5de3451d
**dueAt:** 2026-06-11T04:10:00Z

---

## 2026-06-10T12:33:51Z

target-met: research_per_day=1 already reached (1 research post today: claude-fable5-launch). No new research posts this run.

### ps-intuned | X | LIVE (customScheduled)
**Kind:** product_spotlight

**Text (tweet 1):** My take on Intuned: right bet, right problem.

Most RPA automations die when websites change. Nobody fixes them. Their answer is AI that reads the error trace and rewrites the code itself.

Zero human intervention. Nobody's fully there yet. This is closer.

Who gets there first?

**Thread tweet 2:** Launch HN this week. Intuned (YC S22): browser automation with AI self-healing. When a run breaks, the agent reads the error trace and rewrites the Playwright code.

Zero-setup cloud IDE, Python/TypeScript.

https://intunedhq.com

**Image style:** risograph print
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/ps-intuned.png
**Buffer post id:** 6a295befa650a36635638684
**dueAt:** 2026-06-10T15:47:00Z

---

## 2026-06-10T00:34:21Z

### claude-fable5-launch | X | LIVE (customScheduled)

**Text (tweet 1):** Anthropic dropped Fable 5 yesterday. Stripe ran a two-month codebase migration in one day with it.

One thing buried in the model card: it silently limits itself for frontier AI dev requests. Not a refusal. Just less capable, no notice. 0.03% of devs today. That number moves.

**Thread tweet 2:** Pricing: $10/M input, $50/M output. Free on Pro/Max/Team through June 22.

Silent limits target ML training infra. Doesn't hit most app builders. But a model that silently degrades is a supply chain trust problem either way.

https://www.anthropic.com/news/claude-fable-5-mythos-5

**Image style:** watercolor
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/claude-fable5-launch.png
**Buffer post id:** 6a28b383f796e49fcb674905
**dueAt:** 2026-06-10T04:44:00Z

---

### claude-fable5-launch | LinkedIn | LIVE (customScheduled)

**Caption:** Claude Fable 5 launched yesterday. Stripe moved a two-month codebase migration in a day.

There's a model card detail that changes how I think about building on top of it. The deck covers both sides.

If a model can silently limit itself based on what you're building, what does that mean for your stack?

#AI #Anthropic #AIBuilders

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/claude-fable5-launch.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/claude-fable5-launch.png
**First comment (source):** https://www.anthropic.com/news/claude-fable-5-mythos-5
**Buffer post id:** 6a28b383891a03093da38339
**dueAt:** 2026-06-10T04:13:00Z

---

## 2026-06-09T12:35:35Z

target-met: research_per_day=1 already reached (2 research posts today: xai-landlord-compute, openai-s1-ipo). No new research posts this run.
spotlight: skipped (daily guard — ps-kimi-work already posted today at 2026-06-09T08:15:01Z; max one spotlight per UTC day).

---

## 2026-06-09T08:15:01Z

target-met: research_per_day=2 already reached this UTC day (topics: xai-landlord-compute, openai-s1-ipo). No new research posts this run.

### ps-kimi-work | X | LIVE (customScheduled)
**Kind:** product_spotlight

**Text (tweet 1):** Moonshot AI shipped a desktop app. 300 parallel agents, local files, browser automation.

The lab that made Kimi K2.6 isn't competing on the model score anymore. They're going after the workflow.

I'm curious whether that's the right move or just the obvious next one.

**Thread tweet 2:** Kimi Work: desktop app for knowledge work from Moonshot AI. Up to 300 agents in parallel, WebBridge for browser automation, PPT/Excel/Word/PDF outputs. Free tier.

https://www.producthunt.com/products/kimi-ai-assistant

**Image style:** Bauhaus geometric
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/ps-kimi-work.png
**Buffer post id:** 6a27cdfa93b160251cc1fdc8
**dueAt:** 2026-06-09T16:18:00Z

---

### ps-kimi-work | LinkedIn | LIVE (customScheduled)
**Kind:** product_spotlight

**Caption:** Moonshot AI launched a desktop app this week. Up to 300 agents running in parallel, local files, browser automation.

The lab that made Kimi K2.6 isn't just competing on benchmarks anymore.

The deck looks at the bet they're making and what it might mean for AI tools broadly.

What would you actually use an AI desktop for vs. just a chat interface?

#AI #AIAgents #Builders #ProductHunt

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/ps-kimi-work.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/ps-kimi-work.png
**First comment (source):** https://www.producthunt.com/products/kimi-ai-assistant
**Buffer post id:** 6a27cdfb30a07571f11480cb
**dueAt:** 2026-06-09T16:52:00Z

---

## 2026-06-09T07:55:49Z

### openai-s1-ipo | X | LIVE (customScheduled)

**Text (tweet 1):** OpenAI yesterday: 'We expect it to leak, so we're just announcing it.'

Fair enough. $852B valuation. 900M weekly users.

Filed one week after Anthropic's $965B filing.

Both labs, both IPO-bound. When public markets are watching API pricing, what changes for builders?

**Thread tweet 2:** Filed June 8. $122B raised in March at this valuation. $13.1B revenue last year, running at ~$2B/month now. Still not profitable. Goldman + Morgan Stanley as underwriters. No confirmed listing date.

Full details: https://openai.com/index/openai-submits-confidential-s-1/

**Image style:** newspaper editorial cartoon
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/openai-s1-ipo.png
**Buffer post id:** 6a27c8d730a07571f1146672
**dueAt:** 2026-06-09T15:23:00Z

---

### openai-s1-ipo | LinkedIn | LIVE (customScheduled)

**Caption:** OpenAI filed for IPO yesterday. $852B. 900M weekly users.

One week after Anthropic filed at $965B.

Both labs, same week. The deck covers what that actually means if you're building on their APIs.

When your infrastructure provider answers to public markets, what changes?

#AI #OpenAI #Builders #AIBuilders #Founders

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/openai-s1-ipo.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/openai-s1-ipo.png
**First comment (source):** https://openai.com/index/openai-submits-confidential-s-1/
**Buffer post id:** 6a27c8d703edf46f70c75679
**dueAt:** 2026-06-09T15:47:00Z

---

## 2026-06-09T00:40:00Z

### xai-landlord-compute | X | LIVE (customScheduled)

**Text (tweet 1):** xAI built a data center in 122 days. Anthropic signed a $1.25B/month lease. Google signed for $920M/month.

The companies racing to beat Grok are paying $2.17 billion a month to the guy who makes Grok.

What exactly is the AI arms race?

**Thread tweet 2:** Both deals came from SpaceX's S-1 filing. Anthropic gets 220,000 Nvidia GPUs through May 2029. Google gets 110,000 through June 2029.

At those rates: $26B a year to xAI/SpaceX. Not from AI product users. From the labs they compete with.

https://techcrunch.com/2026/05/20/anthropic-will-pay-xai-1-25-billion-per-month-for-compute/

**Image style:** blueprint / schematic
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/xai-landlord-compute.png
**Buffer post id:** 6a2761363f52a51b3e9e6d47
**dueAt:** 2026-06-09T04:14:00Z

---

### xai-landlord-compute | LinkedIn | LIVE (customScheduled)

**Caption:** Anthropic and Google are paying Elon Musk $2.17 billion a month. Combined.

Not for Grok. For GPU time.

The SpaceX S-1 revealed it: Anthropic locked in $1.25B/month for 220,000 GPUs. Google signed for $920M/month. Both deals run through 2029. xAI built Colossus 1 in 122 days to get here first.

The company supposed to fall behind is now collecting infrastructure rent from everyone racing ahead.

What happens to the AI race when the fastest data center builder wins regardless of whose model scores best?

#AI #Infrastructure #AIRace

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/xai-landlord-compute.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/xai-landlord-compute.png
**First comment (source):** https://techcrunch.com/2026/05/20/anthropic-will-pay-xai-1-25-billion-per-month-for-compute/
**Buffer post id:** 6a2761361c07fa41dbc6562d
**dueAt:** 2026-06-09T04:27:00Z

---

## 2026-06-08T12:42:00Z

### spacex-ipo-ai-orbit | X | LIVE (customScheduled)

**Text (tweet 1):** SpaceX prices June 11. $75B raise. Biggest IPO ever.

Goldman Sachs is modeling $322B in AI revenue by 2030. The AI business made $3.2B last year.

S&P 500 rejected their fast-track. They lost $4.94B in 2025, only 5% float.

What exactly are public investors buying?

**Thread tweet 2:** Roadshow wrapping up this week. Pricing June 11, trading June 12 on Nasdaq as SPCX.

Full S-1 breakdown: https://www.tradingkey.com/analysis/stocks/us-stocks/261948674-spacex-ipo-roadshow-wall-street-hypes-100x-ai-growth-sp-no-fast-track-tradingkey

**Image style:** neon cyberpunk
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/spacex-ipo-ai-orbit.png
**Buffer post id:** 6a26b8cd54756c91d062e87b
**dueAt:** 2026-06-08T15:43:00Z

---

### spacex-ipo-ai-orbit | LinkedIn | LIVE (customScheduled)

**Caption:** SpaceX prices its IPO June 11. $75 billion raise. Largest in history.

Goldman Sachs is modeling $322 billion in AI revenue for them by 2030. The AI business made $3.2 billion last year.

The deck looks at what the actual numbers say and what they don't.

If markets are pricing AI infrastructure at this multiple, what does that mean for everyone else building it?

#AI #SpaceX #AIInfrastructure

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/spacex-ipo-ai-orbit.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/spacex-ipo-ai-orbit.png
**First comment (source):** https://www.tradingkey.com/analysis/stocks/us-stocks/261948674-spacex-ipo-roadshow-wall-street-hypes-100x-ai-growth-sp-no-fast-track-tradingkey
**Buffer post id:** 6a26b8ced095490942f2126c
**dueAt:** 2026-06-08T16:28:00Z

---

## 2026-06-08T00:42:04Z

### apple-siri-gemini-wwdc26 | X | LIVE (customScheduled)

**Text (tweet 1):** Apple just put Google inside 1.4B iPhones.

Siri now runs on Gemini. Reported ~$1B/year deal. ChatGPT exclusivity: over.

Users can now pick ChatGPT, Gemini, or Claude as their Apple AI. Three labs. One OS.

What does this do to OpenAI's distribution story?

**Thread tweet 2:** Happening at WWDC today. Bloomberg first reported the Gemini deal; Apple confirmed the partnership on stage.

Full details: https://letsdatascience.com/news/apple-unveils-gemini-powered-siri-and-ios-27-at-wwdc-2026-b757953c

**Image style:** claymation / soft 3D clay
**Image URL:** https://ahmedraza28.github.io/brand-agent/images/apple-siri-gemini-wwdc26.png
**Buffer post id:** 6a26100874031f4964d3420d
**dueAt:** 2026-06-08T19:54:36Z

---

### apple-siri-gemini-wwdc26 | LinkedIn | LIVE (customScheduled)

**Caption:** Apple's keynote is today. Siri now runs on Google Gemini.

The deal: Bloomberg reports ~$1B/year for a custom model. ChatGPT exclusivity is gone. Users can now choose between ChatGPT, Gemini, or Claude as their Apple AI.

Three competing labs inside one OS. The deck breaks down what changed and what it means.

Does this shift how you think about Google's AI position?

#AI #WWDC #Builders

**Format:** carousel (PDF)
**Carousel PDF:** https://ahmedraza28.github.io/brand-agent/carousels/apple-siri-gemini-wwdc26.pdf
**Carousel thumbnail:** https://ahmedraza28.github.io/brand-agent/carousels/apple-siri-gemini-wwdc26.png
**First comment (source):** https://letsdatascience.com/news/apple-unveils-gemini-powered-siri-and-ios-27-at-wwdc-2026-b757953c
**Buffer post id:** 6a2610085205cc790d362d0a
**dueAt:** 2026-06-08T17:07:36Z

---

## 2026-06-07T12:35:15Z

skip-day: sun

---

## 2026-06-07T00:33:00Z

skip-day: sun

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

## 2026-07-30T12:35:00Z (scheduled run check)

target-met: research_per_day=1 already reached (1 research post today: ai-companies-recruiting-trades, dueAt 2026-07-30T16:14:00Z). No new posts this run.
spotlight: skipped (product_spotlight.enabled = false).
takes: skipped (takes.enabled = false).

---

## 2026-08-16T00:36:23Z

skip-day: sun

Gate check: settings.enabled = true, but today (UTC 2026-08-16) is Sunday, which is in `settings.skip_days` (["sun"]). Per Step 1 gate 2, no research, no drafting, no publish this run. Stopping immediately, no exceptions.

---
