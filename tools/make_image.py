#!/usr/bin/env python3
"""
make_image.py — generate a post image with gpt-image-2, GUARANTEED opaque.

Usage:  OPENAI_API_KEY=... python3 tools/make_image.py "<image prompt>" <slug> <out_dir> [size]
Writes: <out_dir>/<slug>.png  (RGB, no alpha)  <- ALWAYS, this contract never changes

Size defaults to 1088x1360 (4:5 portrait — LinkedIn shows portrait in-feed without
cropping, so a designed infographic gets maximum vertical real estate and stays fully
legible). gpt-image-2 requires each edge to be a multiple of 16. Pass a 5th CLI arg
(e.g. "1200x1200" for square, "1536x1024" for landscape) to override.

Why the opaque handling exists: image models can return a TRANSPARENT PNG, which
renders black/checkered on dark feed UIs. gpt-image-2 does not support transparent
backgrounds (background:"opaque" only), and we ALSO flatten any alpha onto white as a
belt-and-suspenders. The images endpoint returns b64_json by default for gpt-image-2
(the response_format param is NOT accepted — passing it 400s).

QUALITY — measured, not assumed (2026-08-06)
--------------------------------------------
Default is "medium", NOT "high". The same real Ployo template prompt (serif headline +
teal underline, two columns of check/x rows, dark punchline pill, hairline divider,
"ployo" wordmark + "Ahmed Raza . Co-Founder & CTO" footer) was rendered 2x at high and
5x at medium at the production 1088x1360 size. Every word was spelled correctly in all
seven, including the small footer credit inspected at native resolution. Medium cost
1587 output tokens vs high's 6431 (4x) and took ~50s vs ~133s.

⚠ Before raising this back to "high", render the SAME prompt at both and compare the
footer strip at 1:1. Paying 4x for a difference nobody can see is the thing this
docstring exists to prevent. Valid values (the API rejects everything else, and the
400 helpfully lists them): low, medium, high, auto.

⚠ There is NO "thinking mode" on this endpoint. `mode`, `thinking` and `reasoning_effort`
each return 400 "Unknown parameter" — that is a ChatGPT product feature, not an API one.
Do not add it on the strength of a blog post or a third-party skill.

ENV LEVERS
----------
  IMAGE_QUALITY  low|medium|high|auto   (default "medium")
  IMAGE_N        integer >= 1           (default 1)

IMAGE_N > 1 asks for N variants in ONE request. Batching is linear in tokens but nearly
free in wall-clock: n=3 medium returned in 55s against 48s for n=1, because the images
are generated concurrently server-side. Candidate 1 is ALWAYS written to
<out_dir>/<slug>.png so the existing pipeline works untouched; the extras land in
.image-candidates/ (gitignored) for a caller that wants to look at all three and promote
a better one. A caller that ignores them gets exactly today's behaviour.
"""
import os, sys, io, json, base64, urllib.request
from PIL import Image

VALID_QUALITY = {"low", "medium", "high", "auto"}


def flatten(raw_b64):
    """Decode one API image and flatten any alpha onto white."""
    img = Image.open(io.BytesIO(base64.b64decode(raw_b64)))
    if img.mode in ("RGBA", "LA") or "transparency" in img.info:
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        bg.alpha_composite(img.convert("RGBA"))
        img = bg
    return img.convert("RGB")


def main():
    prompt = sys.argv[1]
    slug = sys.argv[2]
    out_dir = sys.argv[3] if len(sys.argv) > 3 else "."
    size = sys.argv[4] if len(sys.argv) > 4 else "1088x1360"  # 4:5 portrait, edges %16==0
    os.makedirs(out_dir, exist_ok=True)
    key = os.environ["OPENAI_API_KEY"]

    quality = os.environ.get("IMAGE_QUALITY", "medium").strip().lower()
    if quality not in VALID_QUALITY:
        sys.exit(f"IMAGE_QUALITY={quality!r} invalid; use one of {sorted(VALID_QUALITY)}")
    try:
        n = max(1, int(os.environ.get("IMAGE_N", "1")))
    except ValueError:
        sys.exit("IMAGE_N must be an integer")

    body = json.dumps({
        "model": "gpt-image-2",
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "background": "opaque",   # gpt-image-2: opaque or auto only (no transparent)
        "n": n,
    }).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    # n>1 generates concurrently server-side but still needs a longer ceiling than n=1.
    d = json.load(urllib.request.urlopen(req, timeout=180 + 60 * (n - 1)))

    # Candidate 1 always takes the canonical path, so a caller that knows nothing about
    # IMAGE_N still finds its image exactly where it has always been.
    path = os.path.join(out_dir, f"{slug}.png")
    flatten(d["data"][0]["b64_json"]).save(path, "PNG")
    print(path)

    if len(d["data"]) > 1:
        alt_dir = os.path.join(os.getcwd(), ".image-candidates")
        os.makedirs(alt_dir, exist_ok=True)
        for i, item in enumerate(d["data"][1:], start=2):
            alt = os.path.join(alt_dir, f"{slug}--cand{i}.png")
            flatten(item["b64_json"]).save(alt, "PNG")
            print(alt)


if __name__ == "__main__":
    main()
