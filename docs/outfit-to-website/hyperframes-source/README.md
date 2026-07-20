# preview.mp4 — hyperframes source

The 15-second promo at `../preview.mp4` was rendered from `index.html` (plus the outfit photos in `assets/`) with [HyperFrames](https://github.com/heygen-com/hyperframes) — a real, deterministic HTML → MP4 pipeline.

## Reproduce

Requires Node 22+ and FFmpeg.

```bash
cd docs/outfit-to-website/hyperframes-source
npx --yes hyperframes@latest init temp --example blank    # scaffolds hyperframes.json + package.json
cp -r assets temp/
cp index.html temp/
cd temp
npx --yes hyperframes@latest check     # validates lint, layout, motion, contrast
npx --yes hyperframes@latest render    # writes MP4 into renders/
```

Rendering takes about 30–60 s on a laptop (450 frames, 6 workers, ~50% dedupe on static regions).

## Composition

- One 15 s composition, three sequential case clips (5 s each), plus a persistent masthead.
- GSAP timeline animates elements inside each clip; HyperFrames handles clip visibility.
- Photos are Unsplash (license permits redistribution); every hex in the palette callouts is traced back to a specific garment in the shot.
