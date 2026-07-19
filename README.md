# trzask-skills

A collection of [Claude skills](https://docs.claude.com/en/docs/claude-code/skills).

## Skills

### [outfit-to-website](outfit-to-website/)

Convert a photo of an outfit into a complete website design. Given an image of a
person, outfit, or clothing, the skill produces:

- **`design-tokens.md`** — a design system traced back to the outfit: a color
  palette where every hex is attributed to a specific garment, typography, spacing,
  corner radii, textures, and WCAG contrast checks.
- **`index.html`** — a self-contained demo landing page (Tailwind CDN + Google
  Fonts) that implements those tokens.

The translation engine lives in [`references/mapping-guide.md`](outfit-to-website/references/mapping-guide.md)
(outfit → design rules: colors, materials, formality, silhouette, accessories,
patterns) and [`references/output-spec.md`](outfit-to-website/references/output-spec.md)
(output templates). [`scripts/extract_palette.py`](outfit-to-website/scripts/extract_palette.py)
extracts dominant colors and checks WCAG contrast.

**Install:** open `outfit-to-website.skill` in Claude, or copy the
`outfit-to-website/` folder into your skills directory.

**Validated** across business, streetwear, and boho test outfits (100% assertion
pass vs a no-skill baseline), including non-English prompts.
