#!/usr/bin/env python3
"""
make_carousel.py — build a LinkedIn document/carousel PDF (+ cover thumbnail PNG)
from a JSON spec. Used by the brand-agent routine for LinkedIn posts.

Usage:  python3 tools/make_carousel.py <spec.json> <out_dir>
Outputs: <out_dir>/<slug>.pdf  and  <out_dir>/<slug>.png  (cover, for the Buffer thumbnail)

Spec JSON:
{
  "slug": "anthropic-ipo-builders",
  "company": "Anthropic",
  "domain": "anthropic.com",          # for the logo (Google favicon, free); optional
  "title": "Why Anthropic's IPO actually matters if you build on Claude",
  "accent": "#CC785C",                # optional brand color; else derived from the logo
  "handle": "Ahmed Raza",
  "slides": [ {"heading": "...", "body": "..."}, ... ],   # 3-5 of these
  "outro": {"heading": "...", "body": "...", "cta": "Follow Ahmed Raza for more builder takes"},
  "theme": "blueprint"                # OPTIONAL: pin a theme; omit to auto-rotate (recommended)
}

VARIETY (2026-06-05): instead of one fixed dark look, the deck is rendered in one of
THEMES — each a distinct palette + layout treatment (cover composition, number style,
footer style). The theme is chosen by anti-repeat ROTATION so consecutive decks never
match (state in state/recent-carousel-themes.json). The per-company brand accent is
preserved in EVERY theme; the theme only controls background / text / layout.

Robust by design: missing logo / accent / network / state all degrade gracefully.
"""
import sys, os, json, io, hashlib, urllib.request
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
MARGIN = 96
FONT_PATH = os.path.join(os.path.dirname(__file__), "fonts", "Inter.ttf")

# repo root = parent of tools/ ; rotation state lives in state/
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_PATH = os.path.join(_ROOT, "state", "recent-carousel-themes.json")
AVOID = 4    # never reuse a theme that appears in the last AVOID picks
KEEP = 8     # how many recent picks to remember

# --- theme catalog -----------------------------------------------------------
# Each theme: name, bg, fg, cover layout, number style, footer style, light flag.
#   bg: (r,g,b) solid | ("grad", top, bot) vertical gradient | ("brand", base, t) blend(accent,base,t)
#   cover: kicker | centered | motif | sidebar
#   num:   bignum | chip | vside
#   footer: bar | dots | count
# `muted` (secondary text) is derived per theme so it always reads on the bg.
THEMES = [
    dict(name="midnight",  bg=(15, 17, 21),                  fg=(244, 244, 245), cover="kicker",   num="bignum", footer="bar",   light=False),
    dict(name="paper",     bg=(245, 241, 232),               fg=(28, 27, 25),    cover="centered", num="chip",   footer="count", light=True),
    dict(name="blueprint", bg=(11, 28, 52),                  fg=(226, 236, 250), cover="motif",    num="vside",  footer="dots",  light=False),
    dict(name="brandwash", bg=("brand", (10, 12, 14), 0.86), fg=(245, 247, 243), cover="sidebar",  num="bignum", footer="bar",   light=False),
    dict(name="slate",     bg=(32, 29, 27),                  fg=(236, 232, 228), cover="kicker",   num="chip",   footer="dots",  light=False),
    dict(name="ivory",     bg=(252, 252, 250),               fg=(18, 18, 20),    cover="centered", num="chip",   footer="count", light=True),
    dict(name="sand",      bg=(236, 226, 208),               fg=(43, 36, 32),    cover="sidebar",  num="chip",   footer="count", light=True),
    dict(name="carbon",    bg=("grad", (18, 20, 26), (8, 9, 12)), fg=(240, 242, 248), cover="motif", num="vside", footer="bar",   light=False),
]


# --- small helpers -----------------------------------------------------------
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


def blend(a, b, t):
    return tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3))


def luma(c):
    return (0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2])


def is_light(c):
    return luma(c) > 150


def contrast_text(bg):
    return (18, 18, 20) if is_light(bg) else (245, 245, 245)


def darken(c, t):
    return blend(c, (0, 0, 0), t)


# --- theme rotation (tested in tests/test_carousel_themes.py) -----------------
def load_recent(path=STATE_PATH):
    try:
        return list(json.load(open(path)).get("recent", []))
    except Exception:
        return []


def save_recent(path, name):
    recent = load_recent(path)
    recent.append(name)
    recent = recent[-KEEP:]
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        json.dump({"recent": recent}, open(path, "w"), indent=2)
    except Exception:
        pass
    return recent


def pick_theme(recent, seed):
    """Pick a theme not used within the last AVOID picks; deterministic per seed."""
    avail = [t for t in THEMES if t["name"] not in recent[-AVOID:]] or THEMES
    idx = int(hashlib.md5(str(seed).encode()).hexdigest(), 16) % len(avail)
    return avail[idx]


# --- logo + text -------------------------------------------------------------
def fetch_logo(domain):
    if not domain:
        return None
    try:
        url = f"https://www.google.com/s2/favicons?domain={domain}&sz=256"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 brand-agent/1.0"})
        data = urllib.request.urlopen(req, timeout=20).read()
        im = Image.open(io.BytesIO(data)).convert("RGBA")
        return im if im.width >= 48 else None
    except Exception:
        return None


def accent_from_logo(logo, fallback):
    try:
        im = logo.convert("RGBA").resize((64, 64))
        best, best_score = None, -1
        for r, g, b, a in im.getdata():
            if a < 200:
                continue
            mx, mn = max(r, g, b), min(r, g, b)
            if mx < 40 or (r > 230 and g > 230 and b > 230):
                continue
            if (mx - mn) > best_score:
                best_score, best = (mx - mn), (r, g, b)
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


def logo_badge(slide, logo, x, y, size=88, border=None):
    if logo is None:
        return 0
    lo = logo.convert("RGBA").resize((size, size), Image.LANCZOS)
    chip = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    chip.alpha_composite(lo)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size, size], radius=20, fill=255)
    chip.putalpha(mask)
    slide.alpha_composite(chip, (x, y))
    if border:
        ImageDraw.Draw(slide).rounded_rectangle([x, y, x + size, y + size], radius=20,
                                                outline=border + (255,), width=2)
    return size


# --- theme resolution --------------------------------------------------------
class Look:
    """Resolved, ready-to-draw appearance for one deck."""
    def __init__(self, theme, accent):
        self.theme = theme
        self.cover = theme["cover"]
        self.num = theme["num"]
        self.footer = theme["footer"]
        self.light = theme.get("light", False)
        self.accent = accent
        spec_bg = theme["bg"]
        if isinstance(spec_bg, tuple) and len(spec_bg) == 3 and isinstance(spec_bg[0], int):
            self.bg_solid, self.grad = spec_bg, None
        elif spec_bg[0] == "grad":
            self.grad, self.bg_solid = (spec_bg[1], spec_bg[2]), blend(spec_bg[1], spec_bg[2], 0.5)
        elif spec_bg[0] == "brand":
            self.bg_solid, self.grad = blend(accent, spec_bg[1], spec_bg[2]), None
        else:
            self.bg_solid, self.grad = (15, 17, 21), None
        self.fg = theme["fg"]
        self.muted = blend(self.fg, self.bg_solid, 0.45)
        # accent for thin text/rules: darken on light bg so it stays legible
        self.accent_line = darken(accent, 0.30) if self.light else accent
        self.logo_border = blend(self.fg, self.bg_solid, 0.72) if self.light else None
        self.on_accent = contrast_text(accent)   # text drawn on top of an accent fill

    def new_slide(self):
        if self.grad:
            top, bot = self.grad
            img = Image.new("RGB", (W, H), top)
            px = img.load()
            for y in range(H):
                c = blend(top, bot, y / H)
                for x in range(W):
                    px[x, y] = c
            return img.convert("RGBA")
        return Image.new("RGBA", (W, H), self.bg_solid + (255,))


# --- render ------------------------------------------------------------------
def footer(d, look, idx, total, handle):
    d.text((MARGIN, H - MARGIN - 8), handle, font=font(30, 600), fill=look.muted)
    num = f"{idx:02d} / {total:02d}"
    fs = font(30, 600)
    d.text((W - MARGIN - d.textlength(num, font=fs), H - MARGIN - 8), num, font=fs, fill=look.muted)
    style = look.footer
    if style == "dots" and total <= 9:
        for k in range(total):
            cx = MARGIN + k * 30
            d.ellipse([cx, H - 30, cx + 12, H - 18], fill=look.accent if k == idx - 1 else look.muted)
    else:  # bar (also the fallback when too many dots)
        if style != "count":
            d.rectangle([0, H - 12, W * idx // total, H], fill=look.accent)


def draw_number(d, look, n):
    """Content-slide index marker. Returns the y where the heading should start."""
    if look.num == "bignum":
        d.text((MARGIN, 360), f"{n:02d}", font=font(120, 800), fill=look.accent)
        return 520
    if look.num == "vside":
        d.text((W - MARGIN - 76, 300), f"{n:02d}", font=font(110, 800), fill=look.accent_line)
        return 360
    # chip
    d.rounded_rectangle([MARGIN, 360, MARGIN + 92, 444], radius=16, fill=look.accent)
    f = font(54, 800)
    d.text((MARGIN + (92 - d.textlength(str(n), font=f)) / 2, 374), str(n), font=f, fill=look.on_accent)
    return 504


def render(spec, out_dir):
    slug = spec["slug"]
    company = spec.get("company", "")
    handle = spec.get("handle", "Ahmed Raza")
    logo = fetch_logo(spec.get("domain"))
    accent = hex_rgb(spec["accent"]) if spec.get("accent") else accent_from_logo(logo, (59, 130, 246))

    # choose theme: explicit pin, env override, else anti-repeat rotation
    forced = spec.get("theme") or os.environ.get("CAROUSEL_THEME")
    recent = load_recent(STATE_PATH)
    theme = next((t for t in THEMES if t["name"] == forced), None) if forced else None
    if theme is None:
        theme = pick_theme(recent, seed=slug)
    look = Look(theme, accent)

    f_title = font(80, 800)
    f_co = font(34, 700)
    f_head = font(60, 700)
    f_body = font(40, 400)
    f_small = font(30, 600)

    n_content = len(spec["slides"])
    total = n_content + 2  # cover + content + outro
    pages = []

    # --- cover ---
    s = look.new_slide(); d = ImageDraw.Draw(s)
    bw = logo_badge(s, logo, MARGIN, MARGIN, border=look.logo_border)
    if company:
        d.text((MARGIN + (bw + 22 if bw else 0), MARGIN + 28), company, font=f_co, fill=look.fg)
    title_lines = wrap(d, spec["title"], f_title, W - 2 * MARGIN)
    if look.cover == "centered":
        ty = max(360, H // 2 - len(title_lines) * 47 - 30)
        d.rectangle([MARGIN, ty - 44, MARGIN + 260, ty - 36], fill=look.accent)
        draw_multiline(d, (MARGIN, ty), title_lines, f_title, look.fg, 94)
    elif look.cover == "motif":
        d.text((W - 360, 170), "01", font=font(420, 800), fill=blend(look.bg_solid, accent, 0.14))
        draw_multiline(d, (MARGIN, 560), title_lines, f_title, look.fg, 94)
    elif look.cover == "sidebar":
        d.rectangle([0, 0, 18, H], fill=look.accent)
        draw_multiline(d, (MARGIN, 520), title_lines, f_title, look.fg, 94)
    else:  # kicker
        d.rectangle([MARGIN, 470, MARGIN + 120, 478], fill=look.accent)
        draw_multiline(d, (MARGIN, 510), title_lines, f_title, look.fg, 94)
    d.text((MARGIN, H - MARGIN - 70), "swipe →", font=f_small, fill=look.accent_line)
    footer(d, look, 1, total, handle)
    pages.append(s.convert("RGB"))
    s.convert("RGB").save(os.path.join(out_dir, f"{slug}.png"), "PNG")  # thumbnail = cover

    # --- content slides ---
    for i, sl in enumerate(spec["slides"], start=1):
        s = look.new_slide(); d = ImageDraw.Draw(s)
        logo_badge(s, logo, MARGIN, MARGIN, border=look.logo_border)
        hy = draw_number(d, look, i)
        head_w = W - 2 * MARGIN - (110 if look.num == "vside" else 0)
        head_lines = wrap(d, sl["heading"], f_head, head_w)
        y = draw_multiline(d, (MARGIN, hy), head_lines, f_head, look.fg, 72)
        if sl.get("body"):
            body_lines = wrap(d, sl["body"], f_body, W - 2 * MARGIN)
            draw_multiline(d, (MARGIN, y + 36), body_lines, f_body, look.muted, 56)
        footer(d, look, i + 1, total, handle)
        pages.append(s.convert("RGB"))

    # --- outro ---
    outro = spec.get("outro") or {}
    s = look.new_slide(); d = ImageDraw.Draw(s)
    logo_badge(s, logo, MARGIN, MARGIN, border=look.logo_border)
    d.rectangle([MARGIN, 470, MARGIN + 120, 478], fill=look.accent)
    head_lines = wrap(d, outro.get("heading", "The takeaway"), f_head, W - 2 * MARGIN)
    y = draw_multiline(d, (MARGIN, 510), head_lines, f_head, look.fg, 72)
    if outro.get("body"):
        body_lines = wrap(d, outro["body"], f_body, W - 2 * MARGIN)
        y = draw_multiline(d, (MARGIN, y + 36), body_lines, f_body, look.muted, 56)
    d.text((MARGIN, H - MARGIN - 120), outro.get("cta", f"Follow {handle} for more."),
           font=f_small, fill=look.accent_line)
    footer(d, look, total, total, handle)
    pages.append(s.convert("RGB"))

    pdf_path = os.path.join(out_dir, f"{slug}.pdf")
    pages[0].save(pdf_path, "PDF", save_all=True, append_images=pages[1:], resolution=150.0)
    if os.environ.get("DUMP_SLIDES"):
        for i, p in enumerate(pages):
            p.save(os.path.join(out_dir, f"{slug}_slide{i}.png"), "PNG")

    # record the theme for anti-repeat (skip when a theme was forced, so manual
    # one-offs don't pollute the rotation history)
    if not forced:
        save_recent(STATE_PATH, theme["name"])
    return pdf_path, os.path.join(out_dir, f"{slug}.png")


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    os.makedirs(out_dir, exist_ok=True)
    pdf, png = render(spec, out_dir)
    print("PDF:", pdf)
    print("THUMB:", png)
    print("THEME:", spec.get("theme") or os.environ.get("CAROUSEL_THEME") or "(rotated)")
