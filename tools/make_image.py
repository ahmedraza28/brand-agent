#!/usr/bin/env python3
"""
make_image.py — generate a single post image with gpt-image-1, GUARANTEED opaque.

Usage:  OPENAI_API_KEY=... python3 tools/make_image.py "<image prompt>" <slug> <out_dir>
Writes: <out_dir>/<slug>.png  (RGB, no alpha)

Why this exists: gpt-image-1 defaults to background:"auto" and sometimes returns a
TRANSPARENT PNG, which renders black/checkered on X's dark UI. We force
background:"opaque" AND flatten any alpha onto white as a belt-and-suspenders.
"""
import os, sys, io, json, base64, urllib.request
from PIL import Image

def main():
    prompt = sys.argv[1]
    slug = sys.argv[2]
    out_dir = sys.argv[3] if len(sys.argv) > 3 else "."
    os.makedirs(out_dir, exist_ok=True)
    key = os.environ["OPENAI_API_KEY"]

    body = json.dumps({
        "model": "gpt-image-1",
        "prompt": prompt,
        "size": "1536x1024",
        "quality": "high",
        "background": "opaque",   # never transparent
        "n": 1,
    }).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    d = json.load(urllib.request.urlopen(req, timeout=180))
    img = Image.open(io.BytesIO(base64.b64decode(d["data"][0]["b64_json"])))

    # belt-and-suspenders: flatten any alpha onto white
    if img.mode in ("RGBA", "LA") or "transparency" in img.info:
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        bg.alpha_composite(img.convert("RGBA"))
        img = bg
    path = os.path.join(out_dir, f"{slug}.png")
    img.convert("RGB").save(path, "PNG")
    print(path)


if __name__ == "__main__":
    main()
