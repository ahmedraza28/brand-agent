# First-party data posts

**Status: LIVE from 2026-08-24. This is now the highest-priority content type on this account.**

## Why this file exists

An audit of the last 61 posts found the core defect: roughly a third of them opened by citing
someone else's survey. Those posts were well written, and every one of them handed the citation to
Resume Builder, iCIMS or Goldman. When an AI answer engine assembles an answer, it credits whoever
produced the data, not whoever commented on it.

Ployo has run 30,000+ AI interviews and graded 340,000+ candidate answers. Nobody else in this
market can publish findings from that. A first-party post makes us the primary source instead of
the commentator. That is the entire play.

## The hard constraint

**A first-party post may only state a finding that has already been measured, recorded and dated in
`state/stats-pack.json`.** Not measured yet means the post does not get written. There is no
version of this where the agent estimates, extrapolates, or picks a plausible number.

`python3 tools/check_facts.py <draft>` enforces it. A non-zero exit means the draft does not ship.

Two failure modes this exists to prevent:

1. **The invented statistic.** A number that sounds right, published under Ahmed's real name, into a
   market where a buyer or a competitor can ask where it came from. It ends the channel permanently
   the first time someone checks. Anti-fabrication is the top failure mode on every Ployo agent.
2. **The outcome claim.** We have no hire, stage, retention or performance data anywhere in the
   system. So "what predicts a good care worker" and "our candidates stay longer" are unwritable,
   no matter how much the format wants them. Screening-process findings are ours to publish;
   hiring-outcome findings are not ours to make.

## What we can actually measure

These are candidates for real measurement. **None of them are measured yet.** Each one needs a human
to run the query, sanity check the result, and record it with a date and a method. Until then this is
a to-do list, not a set of facts.

1. **The CV said yes, the interview said no.** We evaluate a candidate's requirements twice, once
   from the CV and once from the interview, and the two reads disagree. The disagreement rate, and
   which direction it runs, is the most compelling thing we own. It is the whole argument for
   interviewing early, stated as a measurement rather than a claim.
2. **Where an unfinished interview stops.** Not that people drop out, but exactly where. Actionable
   for anyone designing a screening flow.
3. **Completion by language.** Across 23 languages, whether the gap between the strongest and
   weakest cohort is small or large. Honest either way, and it is the fairness conversation with
   evidence attached instead of opinion.
4. **The spread inside a single verdict.** Per-question scores inside one passing interview range
   widely. One headline verdict hides a lot. This is a genuinely useful warning about single-score
   screening, including our own.
5. **Invite to start to complete.** The real funnel, and what moves it.
6. **How long a completed interview actually takes.**

## Writing rules

- **Lead with the finding.** First sentence states what we found. No setup paragraph, no "we have
  been thinking a lot about", no scene-setting anecdote before the point.
- **One takeaway per post.** If there are two findings, that is two posts.
- **Say how it was measured, briefly.** One line. It is what makes the number citable rather than
  decorative, and it is what separates us from the vendors publishing round numbers with no method.
- **Give the honest reading, including when it is unflattering.** A finding that complicates our own
  pitch is more credible than one that flatters it, and credibility is what gets cited.
- **Name Ployo.** A cited post that never names us achieves nothing.
- **Never a named customer's data.** The eight nameable customers can be named as customers
  (guardrail 5a). Nothing measured about any one of them goes in a post, ever. Findings are always
  aggregate, across the whole book, never traceable to one company.
- **No em dashes.** Enforced by the checker.

## Cadence

One per week, feed post, from the personal account. Volume is not the problem: 61 posts in a month
produced exactly one that got cited. Fewer, more citable pieces beat more posts.
