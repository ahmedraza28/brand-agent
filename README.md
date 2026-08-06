# brand-agent

Config + memory + image host for an **automated personal-brand AI-trends poster** (Ahmed Raza). A Claude cloud routine runs ~2×/day, finds the biggest AI/tech moments from free sources, drafts a take in Ahmed's voice, generates a varied cover image, and publishes to his **X + LinkedIn** via Buffer. This repo is the routine's brain and memory; the routine is the runtime.

> Separate from the Ployo "Diary of an AI Recruiter" automation. They reuse the same Buffer account + OpenAI image key but are independent routines/repos.

## Layout

```
config/
  persona.md     # the voice (the #1 tuning knob)
  playbook.md    # fact-checked X + LinkedIn best-practices (drives format)
  guardrails.md  # full-auto safety rails (grounding, content-safety, kill switch)
  styles.md      # ONE locked Ployo template + layout-archetype rotation + image prompting
  sources.md     # free, keyless trend sources + ranking heuristics
state/
  settings.json      # { enabled, mode } — kill switch + soft-launch
  ledger.json        # topics already covered (7-day dedup)
  recent-styles.json # last 4 LAYOUT archetypes used (anti-repeat)
  posting-log.md     # append-only human-readable log of every run
docs/
  images/        # generated PNGs, served via GitHub Pages
  index.html     # Pages landing (noindex)
```

GitHub Pages serves `/docs`, so an image at `docs/images/<slug>.png` is public at
`https://ahmedraza28.github.io/brand-agent/images/<slug>.png` — that URL is what Buffer attaches.

## Operating it (no redeploy needed — just edit + commit)

- **Pause everything:** set `state/settings.json` → `"enabled": false`. The routine still researches/drafts but publishes nothing. Set back to `true` to resume.
- **Soft-launch / review mode:** set `"mode": "draft"` → posts go to Buffer as drafts for you to eyeball in the app. `"mode": "live"` schedules them for real (default).
- **Tune the voice:** edit `config/persona.md`. Tune format rules in `config/playbook.md`, safety in `config/guardrails.md`, image variety in `config/styles.md`. The routine reads all of these fresh every run.

## What the routine does each run
pull → gather (WebSearch + Google News / HN / Product Hunt / Reddit RSS) → dedup vs ledger → rank → **verify every claim against a fetched source** → draft per playbook → **humanizer pass** (`config/humanizer.md`, wired via `persona.md`) → pick a non-recent layout archetype → render 3 image candidates and promote the best → commit the winner → publish via Buffer (staggered, verified windows) → append ledger + recent-styles + posting-log → push.

A slow news day produces zero posts. Quality over cadence.
