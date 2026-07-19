# Outfit → Design Mapping Guide

The core idea: an outfit is already a designed artifact. Someone chose those colors, materials, and proportions to express something. Your job is to identify *what* it expresses and re-express it in web-design vocabulary. When two rules conflict, prefer the one that preserves the outfit's overall mood — mood coherence beats rule compliance.

## 1. Colors → Palette roles

| Outfit feature | Design role | Why |
|---|---|---|
| Dominant color (largest area: coat, dress, suit) | Background or primary brand color | It sets the mood of the outfit, so it should set the mood of the page |
| Secondary garment colors | Section backgrounds, cards, surfaces | They support the dominant color the same way on the page as on the body |
| Accent colors (shoes, bag, jewelry, lipstick, laces) | CTA buttons, links, hover states, highlights | Accents are where the eye goes — exactly what a CTA needs |
| Neutrals (white shirt, black jeans, grey knit) | Body text, borders, muted surfaces | Neutrals do the quiet structural work in both media |
| Metal hardware (gold/silver jewelry, zips, buckles) | Thin decorative lines, icon strokes, dividers | Hardware is jewelry for the page too — use sparingly |

Guidance:

- Aim for 4–6 colors total. An outfit with 10 colors still has a hierarchy — find it.
- **Decide light vs. dark theme from the dominant color**: a black leather outfit wants a dark page; a cream linen outfit wants a light one. Don't default to white.
- Photos lie about color: shadows desaturate, sunlight warms. Adjust hexes toward what the garment *would look like* in neutral light, and say you did.
- Derive tints/shades of palette colors freely (for hover states, subtle backgrounds) — that's not adding new colors.

### Contrast (do this before finalizing)

Check every text/background pair against WCAG AA: ≥ 4.5:1 for normal text, ≥ 3:1 for large headings. Always compute ratios with `python scripts/extract_palette.py --contrast '#fg' '#bg'` and record the script's output — estimated ratios are reliably off by enough to matter near the 4.5:1 boundary.

**Never fix contrast by muting the outfit's signature color.** A vivid accent is usually the most memorable thing about the outfit; darkening it to gain AA margin trades the design's soul for a number. When a vivid accent fails a pair, change the *role*, not the color:

1. Flip the pair — put white or ink text *on* the accent instead of accent text on a light background.
2. Reserve the accent for large display text (3:1 is enough) or purely decorative uses (no threshold at all).
3. Only if small accent-colored text is truly unavoidable, add a darkened `accent-text` variant token for that one role — and keep the original vivid hex as the main accent for everything else.

Passing AA with margin to spare is not a goal; 4.6:1 passes exactly as well as 6:1. Also: small distinctive colors (tinted sunglasses, a bright lining) make great micro-detail tokens — don't drop them just because they have no text role.

## 2. Materials → Textures and surface treatment

| Material | Surface treatment | Why |
|---|---|---|
| Linen, wool, tweed, knit | Subtle grain/noise texture, paper-like backgrounds, soft off-whites | These fabrics have visible texture; a flat background would feel synthetic |
| Leather, satin, silk | Smooth gradients, deeper shadows, slight sheen (gradient highlights) | Glossy materials reflect light; gradients are how screens do that |
| Denim | Slightly desaturated blues, visible "stitch" details (dashed borders, seam-like dividers) | Denim's charm is its utilitarian detail |
| Technical/nylon (windbreakers, puffers) | Crisp edges, high-contrast panels, no texture | Technical wear is clean and functional |
| Velvet, corduroy | Rich saturated darks, soft large shadows | These fabrics absorb light and feel deep |

Texture implementation: a CSS `radial-gradient` grain, an inline SVG noise filter (`feTurbulence`), or a very subtle repeating pattern. Keep opacity low (3–8%) — texture should be felt, not seen.

## 3. Formality → Typography and tone

| Formality | Typography | Layout tone |
|---|---|---|
| Formal / business / elegant | Refined serif for headings (Playfair Display, Cormorant, Libre Caslon) or a neo-grotesque (Neue Haas–style: Inter, Söhne-alikes), generous letter-spacing on small caps | Symmetry, lots of whitespace, restrained copy |
| Smart casual | Humanist sans (Source Sans 3, Work Sans) or a serif/sans pairing | Balanced grid, moderate whitespace |
| Streetwear / casual | Bold display faces (Archivo Black, Space Grotesk, Bebas Neue), tight leading, big sizes | Asymmetry, overlapping elements, oversized type, high contrast |
| Boho / romantic | Soft serifs (Fraunces, Lora), occasional italic accents | Organic shapes, flowing sections, warm whitespace |
| Athleisure / sporty | Geometric sans (Montserrat, Chivo), italics for motion | Diagonal cuts, dynamic angles, progress-bar motifs |
| Avant-garde | Unexpected pairing (mono + serif, e.g. Space Mono + Fraunces), experimental sizes | Broken grid, deliberate tension |

Use Google Fonts (they load from CDN in the demo). Pick exactly two families: one for headings, one for body. The pairing should have the same *relationship* as the outfit's pieces — a tailored blazer over a plain tee is a distinctive heading font over a quiet body font.

## 4. Fit and silhouette → Layout and spacing

| Silhouette | Layout decision | Why |
|---|---|---|
| Oversized, flowing, relaxed | Large section padding (py-24+), wide max-widths, airy line-height | The outfit breathes; the page should too |
| Tailored, fitted, structured | Tighter grid, precise alignment, thin rules/borders, denser sections | Tailoring is about precision — show it in alignment |
| Layered outfit (jacket over hoodie over tee) | Overlapping elements: cards over images, negative margins, stacked z-index, sticky elements | Layering is literally z-index |
| Monochrome/minimal outfit | Single-column focus, very few elements, type-driven design | Minimalism translates directly |

## 5. Accessories and details → Micro-design

- **Round accessories** (round glasses, hoop earrings, round watch) → larger border-radius (rounded-xl+, pill buttons).
- **Angular accessories** (square frames, angular bags) → small or zero radius, sharp cards.
- **Delicate jewelry** → thin borders (1px), fine hairline dividers, small refined icons.
- **Chunky hardware** (big buckles, chains, platform soles) → thick borders, heavy underlines, bold hover effects.
- **Watch/tech accessories** → monospace numerals for stats, precise data details.

## 6. Patterns → Decorative motifs

| Pattern on clothing | Page motif |
|---|---|
| Stripes | Repeating line dividers, striped section edges, striped accent behind headings |
| Plaid/check | Subtle grid background, checkered accents (small doses) |
| Floral | Organic SVG blob shapes, botanical corner decorations |
| Animal print | High-energy accent panels, textured hero background (very sparingly) |
| Logo/graphic prints | Bold typographic stamps, badge/sticker elements |
| Color-blocking | Full-bleed alternating section backgrounds in palette colors |

Use at most one or two motifs. A plaid-shirt outfit doesn't need a plaid page — it needs one tasteful plaid-derived detail.

## 7. Sanity check before writing tokens

1. Would someone seeing the outfit and the page side by side say "yes, same vibe"? That's the test.
2. Is there exactly one dominant mood? If the tokens feel like two different websites, re-read the outfit — you probably promoted an accent to a role it shouldn't have.
3. Does text pass contrast on every background it sits on?
4. Are you using at most 2 font families and 4–6 colors?
