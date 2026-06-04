#!/usr/bin/env python3
"""
make_carousel.py — build a LinkedIn document/carousel PDF (+ cover thumbnail PNG)
from a JSON spec. Used by the brand-agent routine for framework/breakdown LinkedIn posts.

Usage:  python3 tools/make_carousel.py <spec.json> <out_dir>
Outputs: <out_dir>/<slug>.pdf  and  <out_dir>/<slug>.png  (cover, for the Buffer thumbnail)

Spec JSON:
{
  "slug": "anthropic-ipo-builders",
  "company": "Anthropic",
  "domain": "anthropic.com",          # for the logo (Clearbit, free); optional
  "title": "Why Anthropic's IPO actually matters if you build on Claude",
  "accent": "#CC785C",                # optional; else derived from the logo
  "handle": "Ahmed Raza",
  "slides": [ {"heading": "...", "body": "..."}, ... ],   # 3-5 of these
  "outro": {"heading": "...", "body": "...", "cta": "Follow Ahmed Raza for more builder takes"}
}

Design: premium dark theme, portrait 1080x1350, Inter (variable) font, a white logo
badge (always legible on dark), an accent kicker, generous type. Consistent across the
deck (one carousel = one look); variety across decks comes from the per-company accent.

Robust by design: missing logo / accent / network all degrade gracefully.
"""
import sys, os, json, io, urllib.request
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
MARGIN = 96
BG = (15, 17, 21)            # near-black
FG = (244, 244, 245)         # near-white
MUTED = (160, 165, 175)
FONT_PATH = os.path.join(os.path.dirname(__file__), "fonts", "Inter.ttf")


def font(size, weight=400):
    f = ImageFont.truetype(FONT_PATH, size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def hex_rgb(s, fallback=(59, 130, 246)):
    try:
        s = s.lstrip("#")
        return tuple(int(s[i:i+2], 16) for i in (0, 2, 4))
    except Exception:
        return fallback


def fetch_logo(domain):
    """Google's favicon service — free, no token, returns the brand mark up to 256px."""
    if not domain:
        return None
    try:
        url = f"https://www.google.com/s2/favicons?domain={domain}&sz=256"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 brand-agent/1.0"})
        data = urllib.request.urlopen(req, timeout=20).read()
        im = Image.open(io.BytesIO(data)).convert("RGBA")
        return im if im.width >= 48 else None   # reject tiny/empty fallbacks
    except Exception:
        return None


def accent_from_logo(logo, fallback):
    """Most saturated frequent color in the logo."""
    try:
        im = logo.convert("RGBA").resize((64, 64))
        best, best_score = None, -1
        for r, g, b, a in im.getdata():
            if a < 200:
                continue
            mx, mn = max(r, g, b), min(r, g, b)
            sat = (mx - mn)
            if mx < 40 or (r > 230 and g > 230 and b > 230):  # skip black/white
                continue
            if sat > best_score:
                best_score, best = sat, (r, g, b)
        return best or fallback
    except Exception:
        return fallback


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_multiline(draw, xy, lines, fnt, fill, leading):
    x, y = xy
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def logo_badge(slide, logo, x, y, size=92):
    """Rounded logo tile, white-backed so transparent/dark marks stay legible on the dark theme."""
    if logo is None:
        return 0
    lo = logo.convert("RGBA").resize((size, size), Image.LANCZOS)
    chip = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    chip.alpha_composite(lo)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size, size], radius=22, fill=255)
    chip.putalpha(mask)
    slide.alpha_composite(chip, (x, y))
    return size


def new_slide():
    return Image.new("RGBA", (W, H), BG + (255,))


def render(spec, out_dir):
    slug = spec["slug"]
    company = spec.get("company", "")
    handle = spec.get("handle", "Ahmed Raza")
    logo = fetch_logo(spec.get("domain"))
    accent = hex_rgb(spec["accent"]) if spec.get("accent") else accent_from_logo(logo, (59, 130, 246))

    f_kicker = font(34, 700)
    f_title = font(82, 800)
    f_head = font(60, 700)
    f_body = font(40, 400)
    f_small = font(30, 600)
    f_company = font(34, 700)

    pages = []

    def footer(d, idx, total):
        d.text((MARGIN, H - MARGIN - 8), handle, font=f_small, fill=MUTED)
        num = f"{idx:02d} / {total:02d}"
        d.text((W - MARGIN - d.textlength(num, font=f_small), H - MARGIN - 8), num, font=f_small, fill=MUTED)
        d.rectangle([0, H - 12, W * idx // total, H], fill=accent)  # progress bar

    n_content = len(spec["slides"])
    total = n_content + 2  # cover + content + outro

    # --- cover ---
    s = new_slide(); d = ImageDraw.Draw(s)
    bw = logo_badge(s, logo, MARGIN, MARGIN)
    if company:
        d.text((MARGIN + (bw + 24 if bw else 0), MARGIN + 30), company, font=f_company, fill=FG)
    d.rectangle([MARGIN, 470, MARGIN + 120, 478], fill=accent)
    title_lines = wrap(d, spec["title"], f_title, W - 2 * MARGIN)
    draw_multiline(d, (MARGIN, 510), title_lines, f_title, FG, 96)
    d.text((MARGIN, H - MARGIN - 70), "swipe →", font=f_small, fill=accent)
    footer(d, 1, total)
    pages.append(s.convert("RGB"))
    s.convert("RGB").save(os.path.join(out_dir, f"{slug}.png"), "PNG")  # thumbnail = cover

    # --- content slides ---
    for i, sl in enumerate(spec["slides"], start=1):
        s = new_slide(); d = ImageDraw.Draw(s)
        logo_badge(s, logo, MARGIN, MARGIN)
        d.text((MARGIN, 360), f"{i:02d}", font=font(120, 800), fill=accent)
        head_lines = wrap(d, sl["heading"], f_head, W - 2 * MARGIN)
        y = draw_multiline(d, (MARGIN, 520), head_lines, f_head, FG, 72)
        if sl.get("body"):
            body_lines = wrap(d, sl["body"], f_body, W - 2 * MARGIN)
            draw_multiline(d, (MARGIN, y + 36), body_lines, f_body, MUTED, 56)
        footer(d, i + 1, total)
        pages.append(s.convert("RGB"))

    # --- outro ---
    outro = spec.get("outro") or {}
    s = new_slide(); d = ImageDraw.Draw(s)
    logo_badge(s, logo, MARGIN, MARGIN)
    d.rectangle([MARGIN, 470, MARGIN + 120, 478], fill=accent)
    head_lines = wrap(d, outro.get("heading", "The takeaway"), f_head, W - 2 * MARGIN)
    y = draw_multiline(d, (MARGIN, 510), head_lines, f_head, FG, 72)
    if outro.get("body"):
        body_lines = wrap(d, outro["body"], f_body, W - 2 * MARGIN)
        y = draw_multiline(d, (MARGIN, y + 36), body_lines, f_body, MUTED, 56)
    d.text((MARGIN, H - MARGIN - 120), outro.get("cta", f"Follow {handle} for more."), font=f_small, fill=accent)
    footer(d, total, total)
    pages.append(s.convert("RGB"))

    pdf_path = os.path.join(out_dir, f"{slug}.pdf")
    pages[0].save(pdf_path, "PDF", save_all=True, append_images=pages[1:], resolution=150.0)
    if os.environ.get("DUMP_SLIDES"):
        for i, p in enumerate(pages):
            p.save(os.path.join(out_dir, f"{slug}_slide{i}.png"), "PNG")
    return pdf_path, os.path.join(out_dir, f"{slug}.png")


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    os.makedirs(out_dir, exist_ok=True)
    pdf, png = render(spec, out_dir)
    print("PDF:", pdf)
    print("THUMB:", png)
