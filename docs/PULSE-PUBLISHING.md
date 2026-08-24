# Publishing a Pulse article

## Why this is not automated

LinkedIn publishes articles through its own editor and exposes no public write API for them. The
Marketing API posts text, images, documents and video to the feed; articles are not in it. Buffer,
which the brand agent uses for every feed post, is subject to the same limit.

So the last step is a person pasting into the editor. Two consequences worth knowing:

1. **Publish from Ahmed's own browser, on his own connection.** The other brand agent already hit
   the datacenter-IP wall, and LinkedIn treats article publishing from an unfamiliar network far
   more suspiciously than an API-scheduled feed post.
2. **The routine cannot mark an article published.** Record it yourself with `--published` so the
   monthly count and the next citation sweep are accurate.

## Steps

1. **Check it.** `python3 tools/pulse.py --check <slug>`. A non-zero exit means it does not ship.
   Fix the failures rather than arguing with them; every one of them exists because it was measured.

2. **Get the paste package.** `python3 tools/pulse.py --brief <slug>`. This prints the title and the
   body, with the H1 stripped since LinkedIn's editor holds the title separately.

3. **Open the editor.** `https://www.linkedin.com/article/new/` while signed in as Ahmed.

4. **Paste the title, then the body.** LinkedIn's editor keeps markdown headings as plain text, so
   re-apply H2s with the editor's own heading control. It is the headings that get extracted, so
   this step is not cosmetic.

5. **Cover image.** Optional. `tools/make_image.py` can render one in the locked Ployo template if
   you want it consistent with the feed.

6. **Publish**, then copy the article URL.

7. **Record it.** `python3 tools/pulse.py --published <slug> --url <the url> --date YYYY-MM-DD`

8. **Announce it in the feed the next day**, as a normal post that links the article in the first
   comment. The article is the asset that gets cited; the feed post is what sends the first readers
   to it.

## Cadence

Two to three a month, rotating roundup, comparison, compliance. `python3 tools/pulse.py --list`
shows the queue and what has shipped.
