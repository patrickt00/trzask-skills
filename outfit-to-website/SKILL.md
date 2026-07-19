---
name: outfit-to-website
description: Convert a photo of an outfit (clothing, styling, a fashion look worn in an image) into a complete website design — a design-token spec plus a working demo landing page. Use whenever the user has an image of a person, outfit, or clothing AND wants a website, landing page, design system, color palette, typography, or visual identity DERIVED FROM that image. Trigger on phrases like "make a website in the style of this photo", "design inspired by this outfit / my look", "turn my outfit into a website", "build a page that matches this fit", "fashion to web design", or an attached outfit/OOTD photo in any web-design context — including other languages (e.g. Polish "zrób stronę w klimacie tej stylizacji") — even if the words "outfit" or "website design" never appear. Do NOT trigger when there is no source image (e.g. "design a minimalist fashion blog"), when the image is not clothing (interiors, landscapes, a site screenshot to clone), or for non-design tasks on a clothing photo (resizing, product copy, brand ID).
---

# Outfit to Website

Translate the visual language of an outfit into the visual language of a website. The outfit is the design brief: its colors become the palette, its fabrics become textures, its formality becomes typography, its silhouette becomes layout. The goal is a design that *feels* like the outfit, not one that merely samples its colors.

## Workflow

### 1. Analyze the photo

Look at the image carefully and identify:

- **Garments and layers** — every visible piece (jacket, shirt, trousers, shoes, bag…) and how they layer.
- **Colors** — the dominant color (largest visual area), secondary colors, accent colors (small pops: shoes, jewelry, bag, lipstick), and neutrals. Note *which garment* each color comes from — you will cite this in the tokens.
- **Materials and textures** — denim, linen, wool, knit, leather, satin, silk, technical/nylon, cotton. Matte vs. glossy.
- **Formality** — from black-tie/business through smart-casual to streetwear/loungewear.
- **Fit and silhouette** — oversized and flowing vs. tailored and fitted; structured vs. relaxed.
- **Accessories and details** — watches, glasses, jewelry, hardware (zips, buckles), stitching. Their shapes (round/angular) and finishes (gold/silver/matte).
- **Patterns** — plaid, stripes, florals, animal print, logos, color-blocking.
- **Overall style label** — e.g. business/elegant, streetwear, boho, minimalist, athleisure, avant-garde, vintage, preppy. One or two labels max.

For precise hex values, optionally run the bundled script (requires Pillow):

```bash
python scripts/extract_palette.py <image-path>
```

It prints the dominant colors as hex with coverage percentages. Treat the output as raw material, not gospel: it can't tell skin/background from clothing, so cross-check each hex against what you see and discard non-outfit colors. If the script or Pillow is unavailable, estimate hexes visually — that works fine.

### 2. Translate outfit → design

Read `references/mapping-guide.md` and apply its rules to convert your analysis into concrete design decisions: palette roles, font pairing, spacing scale, corner radii, shadows, textures, and decorative motifs. The guide also covers WCAG contrast checks — do them before committing to a text/background combination.

### 3. Write the design tokens

Create `design-tokens.md` following the exact template in `references/output-spec.md`. Every color must state which garment it came from — this traceability is what makes the result feel derived from the outfit rather than generic.

Compute every contrast ratio you document with the bundled script — `python scripts/extract_palette.py --contrast '#fg' '#bg'` — and copy its output verbatim. Mentally estimated ratios drift (a real run documented 5.0:1 where the true value was 4.6:1), and a wrong number in a spec undermines trust in the whole document. If Python is unavailable, label the values as estimates.

### 4. Build the demo page

Create a single self-contained `index.html` using the Tailwind CDN, following the page structure and technical setup in `references/output-spec.md`. The page must implement the tokens: custom colors in the inline Tailwind config, the chosen Google Fonts, the spacing/radius/shadow decisions, and at least one texture or motif from the mapping.

Page content: if the user named a business/purpose, write copy for that. Otherwise invent a brand that fits the outfit's vibe (a tailored navy suit might become a wealth-advisory firm; a streetwear fit might become a sneaker drop page) and say so.

### 5. Show the result

Open `index.html` in the browser preview (or send the file to the user) together with a short summary: the style label, the palette with garment attributions, and the one or two boldest design decisions you made. If anything in the photo was ambiguous (e.g. lighting distorting colors), mention how you resolved it.

## Output files

Write both files to the current working directory unless the user asks otherwise:

- `design-tokens.md` — the design system spec
- `index.html` — the demo landing page

If the user only wants one of the two (just a palette, or just a page), still do the full analysis and mapping — then deliver only what they asked for.
