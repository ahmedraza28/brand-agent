#!/usr/bin/env python3
"""
make_image.py — generate a single post image with gpt-image-2, GUARANTEED opaque.

Usage:  OPENAI_API_KEY=... python3 tools/make_image.py "<image prompt>" <slug> <out_dir> [size]
Writes: <out_dir>/<slug>.png  (RGB, no alpha)

Size defaults to 1088x1360 (4:5 portrait — LinkedIn shows portrait in-feed without
cropping, so a designed infographic gets maximum vertical real estate and stays fully
legible). gpt-image-2 requires each edge to be a multiple of 16. Pass a 5th CLI arg
(e.g. "1200x1200" for square, "1536x1024" for landscape) to override.

Why the opaque handling exists: image models can return a TRANSPARENT PNG, which
renders black/checkered on dark feed UIs. gpt-image-2 does not support transparent
backgrounds (background:"opaque" only), and we ALSO flatten any alpha onto white as a
belt-and-suspenders. The images endpoint returns b64_json by default for gpt-image-2
(the response_format param is NOT accepted — passing it 400s).
"""
import os, sys, io, json, base64, urllib.request
from PIL import Image

def main():
    prompt = sys.argv[1]
    slug = sys.argv[2]
    out_dir = sys.argv[3] if len(sys.argv) > 3 else "."
    size = sys.argv[4] if len(sys.argv) > 4 else "1088x1360"  # 4:5 portrait, edges %16==0
    os.makedirs(out_dir, exist_ok=True)
    key = os.environ["OPENAI_API_KEY"]

    body = json.dumps({
        "model": "gpt-image-2",
        "prompt": prompt,
        "size": size,
        "quality": "high",
        "background": "opaque",   # gpt-image-2: opaque or auto only (no transparent)
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
