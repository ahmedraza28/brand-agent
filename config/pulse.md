# LinkedIn Pulse articles

**Status: LIVE from 2026-08-24. Target 2 to 3 per month.**

## Why this is the highest-leverage thing on this account

Measured across 751 real AI answers on 2026-08-24: linkedin.com is the single most cited domain
in this category, ahead of G2, Capterra and every competitor's own website. Of 242 LinkedIn
citation URLs, **65 were Pulse articles, 27% of the total**. Company pages got 11%.

Four separate authors are being cited right now for the same format:

- `pulse/5-best-ai-recruiting-tools-2026-goperfect-...`
- `pulse/5-best-ai-recruiting-tools-2026-harry-portch-...`
- `pulse/5-best-ai-recruiting-tools-2026-weekdayworks-...`
- `pulse/best-ai-recruiting-tools-2026-whats-real-hype-nimrod-kramer-...`
- `pulse/phone-screening-tools-2026-whats-changed-what-recruiting-teams-...`
- `pulse/conversational-ai-vs-one-way-video-interviews-comprehensive-...`

Not one of them is a household name. The format is being cited because it matches the shape of
what a buyer asks, not because of the author's authority. That makes it replicable, which is why
it goes first.

## The pipeline

    python3 tools/pulse.py --new <slug> --kind roundup --title "..."   # scaffold
    python3 tools/pulse.py --check <slug>                              # refuses anything unciteable
    python3 tools/pulse.py --brief <slug>                              # paste-ready package
    python3 tools/pulse.py --published <slug> --url <url>              # record it

⚠ **Publishing is manual and always will be.** LinkedIn has no public write API for articles, and
Buffer posts to the feed only. Step by step: `docs/PULSE-PUBLISHING.md`. At 2 to 3 a month that is
a few minutes of supervised work; everything up to the paste is automated.

## The three types, rotating

**1. The roundup.** "Best AI interview software for Australian care and health hiring in 2026."
Cover 7 to 12 tools. This is the one that maps directly onto what is already being cited.

**2. The comparison.** "Conversational AI versus one-way video interviews." A cited Pulse format.
Name both sides honestly and do not strawman the alternative.

**3. The compliance piece.** Aged Care Act 2024 obligations, NDIS Worker Screening, AHPRA
verification, the ADM disclosure obligation. Regulators account for 24% of all citations in this
category, and precision is what gets a vendor cited beside them. ⚠ **Verify every legislative name
and date against the primary instrument before publishing.** Not a law firm's summary, not this
file, and not the brief. The actual legislation. One wrong date and the piece is worthless for the
exact audience it is aimed at.

## Rules that decide whether it gets cited

- **Title states the category and the year plainly.** No cleverness. The title is matching a query.
- **Question-shaped H2s, with the answer in the first sentence underneath.** This is the single
  most mechanical thing you can do to get a passage extracted.
- **Every roundup entry gets the same four fields, in the same order:** who it is for, what it does,
  what it costs or how it prices, one real limitation. Enforced by `--check`.
- **Competitor facts come from `config/competitors.md` and nowhere else.** That file is generated
  from sourced, dated claims. A vendor that is not in it has not been fact-checked by anyone, and
  `--check` will refuse the article rather than let it be described from memory. Where a vendor does
  not publish pricing, write "not published". That is a finding, not a gap.
- **Describe competitors accurately, including what they are genuinely better at.** Every entry in
  the competitors file carries a real "where they win". A list that flatters us is discounted by the
  model cross-checking it. The conceding sentence is the one that gets quoted, with our name on it.
- **Ployo goes in honestly, and not at number one.** Enforced by `--check`.
- **Link ployo.ai once, in the Ployo entry.** A citation needs somewhere to land.
- **No em dashes.** Enforced.
- **No invented numbers, ours or theirs.** Enforced for ours; for theirs, guardrail 1 stands.

## What a failure looks like

One wrong price, one wrong modality, one invented statistic. A reader who checks a single detail and
finds it wrong discards the whole list, and we do not get a second attempt at being the source that
gets cited for this query. Being incomplete is survivable and honest: say which tools the article
does not cover. Being wrong is not.
