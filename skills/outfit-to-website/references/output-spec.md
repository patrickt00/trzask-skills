# Output Spec

Two deliverables: `design-tokens.md` (the spec) and `index.html` (the demo). Write the tokens first — the page implements them.

## design-tokens.md template

Use this exact structure:

```markdown
# Design Tokens — [style label, e.g. "Tailored Navy / Modern Business"]

## Concept
[2–3 sentences: what the outfit expresses and how the page re-expresses it.
Name the specific garments that drove the biggest decisions.]

## Palette
| Token | Hex | Role | Source garment |
|---|---|---|---|
| primary | #1B2A4A | Page background, brand color | Navy wool suit |
| accent | #B0703C | CTA, links, hover | Cognac leather brogues |
| ... | | | |

Theme: [light | dark] — [one line why]
Contrast: body text [#hex] on [#hex] = [ratio] (AA pass)
[List every text/background pair used on the page. Each ratio must come from
`python scripts/extract_palette.py --contrast '#fg' '#bg'` — copy the script's
numbers, don't estimate them.]

## Typography
- Headings: [Font Name] ([weight range]) — [one line: why it matches the outfit]
- Body: [Font Name] ([weight]) — [why]
- Scale: [e.g. 16px base, headings 1.25 ratio / display hero at clamp(...)]

## Shape & Space
- Radius: [e.g. 4px cards, 2px buttons] — [driven by which accessory/detail]
- Section rhythm: [e.g. py-24, max-w-6xl, airy] — [driven by silhouette]
- Borders/shadows: [e.g. 1px hairlines, no shadows] — [driven by what]

## Texture & Motifs
- [e.g. 5%-opacity grain overlay on hero — from the wool texture]
- [e.g. seam-style dashed divider between sections — from denim stitching]
```

## index.html requirements

One self-contained file. No build step, no external files except CDNs.

### Technical setup

- Tailwind via CDN: `<script src="https://cdn.tailwindcss.com"></script>`
- Define palette and fonts in an inline config **before** using the classes:

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: { primary: '#1B2A4A', accent: '#B0703C', surface: '#F5F2EC' /* ... all tokens */ },
        fontFamily: { display: ['"Playfair Display"', 'serif'], body: ['Inter', 'sans-serif'] },
      }
    }
  }
</script>
```

- Google Fonts `<link>` for exactly the two chosen families (with the weights you use).
- Textures/motifs as inline SVG or CSS in a `<style>` block — never external images.
- No stock photos. Where imagery would go, use styled placeholder blocks built from the palette (gradient panels, pattern swatches, big typographic compositions). They should look intentional, not missing.

### Page structure

Five sections minimum, in this order (adapt names to the invented brand):

1. **Nav** — brand wordmark + 3–4 links + small CTA.
2. **Hero** — headline in the display font, subline, primary CTA in the accent color. This section carries the outfit's mood hardest: dominant color, texture, boldest typography.
3. **Features / About** — 3-card or 2-column layout. This is where fit→spacing and accessory→radius decisions show.
4. **Showcase / Gallery** — grid of palette-derived placeholder panels; a natural home for the pattern motif.
5. **CTA band + Footer** — accent-colored call-to-action strip; footer in a neutral with hairline borders.

### Copy

Real copy, not lorem ipsum. 
If the user gave a business/purpose, write for it; otherwise invent a brand whose personality matches the outfit and note the choice in your summary. Keep copy short — this is a design demo, not a content site.

### Quality bar

- Every palette color from the tokens appears on the page; no colors outside the tokens (tints/shades of them are fine).
- Responsive: sections stack cleanly on mobile (use sm:/md:/lg: variants); no horizontal overflow.
- Hover states on links and buttons, using palette colors.
- The page must render correctly offline except for the two CDNs (Tailwind, Google Fonts).
