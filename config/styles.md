# Image styles — rotate hard, never repeat

The explicit requirement: **images must NOT follow the same visual pattern.** The diary's covers all look alike and Ahmed dislikes it. So:

## Rules
1. Read `state/recent-styles.json` (`{"recent": [...]}`). **Pick a style NOT in the last 6 used.** Append your pick to the front of `recent` and trim to 6 before committing.
2. Beyond the named style, **diverge in composition, palette, and central metaphor every time.** Two "isometric 3D" images months apart should still look unrelated.
3. **Not every post gets an image.** For a pure one-line hot-take, text-only is often stronger. Aim for an image on ~70% of posts, text-only on the rest — and vary *that* too. Variety includes presence/absence.
4. **REQUIRED: feature the subject company's / brand's actual logo or wordmark + brand colors**, rendered cleanly and prominently, integrated into the chosen art style — e.g. the Anthropic radial-sunburst mark, the Uber wordmark, the OpenAI / Nvidia / Google / Microsoft / Tesla / Meta logo. A clearly-correct logo makes the post instantly legible. If a post is about several companies, feature the main one (or both if it composes well). Get the logo right.
5. **Short, accurate on-brand text is OK** — a 2-5 word headline (e.g. "NEARS $1 TRILLION") renders fine on the current model and reads like a real editorial cover. Keep it short and only if you're confident it spells correctly; the logo + the idea are the priority. **No real human faces or likenesses.** Avoid the robot / brain / glowing-orb clichés.
6. The logo requirement (4) and the on-brand text (5) layer **on top of** the rotating art-direction — every post still picks a *different, non-recent* style (rule 1) and just renders the subject's logo within it. Logos + style variety coexist.
7. Generate for clean cropping to 16:9 (X/LinkedIn landscape) or 1:1. Keep key content centered / high-in-frame.

## The palette (pick one NOT recently used; combine with a fresh subject metaphor)
1. **Swiss / International typographic** — bold grid, flat color blocks, one accent, lots of negative space.
2. **80s retro-futurism poster** — chrome, sunset gradients, gridlines to the horizon, airbrushed.
3. **Hand-drawn marker sketch** — loose ink + marker, whiteboard-explainer energy, imperfect lines.
4. **Isometric 3D render** — clean isometric scene, soft studio lighting, pastel-but-saturated.
5. **Editorial photo-collage** — torn-paper cutouts, mixed media, magazine art-desk feel.
6. **Blueprint / schematic** — cyan lines on dark navy, technical-drawing annotations (shapes, not real text).
7. **Claymation / soft 3D clay** — matte clay textures, tactile, playful, fingerprints-in-the-clay charm.
8. **Newspaper editorial cartoon** — single-panel ink wash, witty, crosshatching, old-print texture.
9. **Neon cyberpunk** — wet-street reflections, magenta/cyan neon, volumetric haze, night.
10. **Watercolor** — soft bleeds, paper texture, restrained palette, calm and human.
11. **Bauhaus geometric** — primary colors, circles/triangles/bars, constructivist composition.
12. **Low-poly** — faceted geometry, flat shading, early-3D-render nostalgia.
13. **Pixel art** — 16-bit scene, limited palette, dithering, retro-game framing.
14. **Surrealist** — dreamlike juxtaposition, Magritte/Dalí logic, uncanny scale.
15. **Risograph print** — 2-3 spot inks, halftone grain, slight misregistration, zine aesthetic.
16. **Brutalist / concrete** — raw concrete, hard shadows, monolithic forms, stark.
17. **Vaporwave** — pastel grids, classical busts, glitch, Y2K-adjacent.
18. **Ukiyo-e woodblock** — Japanese woodblock style applied to a modern-tech subject.

## Subject metaphor (fresh each time — examples, don't reuse)
Tie the image to the post's *idea*, abstractly: a model "waking up", a chip as a city, a benchmark as a race, agents as a swarm, an IPO as a rocket on a launchpad, a new tool as a key/door, "everyone posting about it" as a crowd/wave. Invent a new metaphor per post; never default to "robot" or "brain" or "glowing AI orb" (the most overused AI-image clichés — avoid them).
