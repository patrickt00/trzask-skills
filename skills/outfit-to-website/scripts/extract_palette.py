#!/usr/bin/env python3
"""Extract dominant colors from an outfit photo, or check WCAG contrast.

Usage:
    python extract_palette.py <image-path> [--colors N]
    python extract_palette.py --contrast '#rrggbb' '#rrggbb'

Prints hex values with coverage percentages. The clustering can't tell
clothing from skin/background, so cross-check results against the photo.
Requires Pillow (pip install Pillow) for image mode; contrast mode has
no dependencies.
"""
import argparse
import random
import sys


def srgb_to_linear(c: float) -> float:
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb) -> float:
    r, g, b = (srgb_to_linear(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(rgb1, rgb2) -> float:
    l1, l2 = sorted((relative_luminance(rgb1), relative_luminance(rgb2)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def parse_hex(s: str):
    s = s.lstrip("#")
    if len(s) == 3:
        s = "".join(ch * 2 for ch in s)
    if len(s) != 6:
        raise ValueError(f"invalid hex color: {s!r}")
    return tuple(int(s[i : i + 2], 16) for i in (0, 2, 4))


def kmeans(pixels, k, iterations=20, seed=42):
    rng = random.Random(seed)
    centers = [list(p) for p in rng.sample(pixels, k)]
    assignment = [0] * len(pixels)
    for _ in range(iterations):
        changed = False
        for i, p in enumerate(pixels):
            best = min(
                range(k),
                key=lambda c: sum((p[d] - centers[c][d]) ** 2 for d in range(3)),
            )
            if best != assignment[i]:
                assignment[i] = best
                changed = True
        for c in range(k):
            members = [pixels[i] for i in range(len(pixels)) if assignment[i] == c]
            if members:
                centers[c] = [sum(m[d] for m in members) / len(members) for d in range(3)]
        if not changed:
            break
    counts = [assignment.count(c) for c in range(k)]
    return centers, counts


def extract(image_path: str, n_colors: int):
    try:
        from PIL import Image
    except ImportError:
        sys.exit("Pillow is not installed (pip install Pillow). Estimate colors visually instead.")
    img = Image.open(image_path).convert("RGB")
    img.thumbnail((150, 150))
    pixels = list(img.getdata())
    sample = random.Random(42).sample(pixels, min(4000, len(pixels)))
    centers, counts = kmeans(sample, n_colors)
    total = sum(counts)
    results = sorted(zip(centers, counts), key=lambda x: -x[1])
    print(f"Dominant colors in {image_path} (verify against the photo — includes skin/background):")
    for center, count in results:
        rgb = tuple(round(v) for v in center)
        print(f"  #{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}  {100 * count / total:5.1f}%")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("args", nargs="+", help="image path, or two hex colors with --contrast")
    ap.add_argument("--colors", type=int, default=6, help="number of colors to extract")
    ap.add_argument("--contrast", action="store_true", help="check WCAG contrast of two hex colors")
    opts = ap.parse_args()

    if opts.contrast:
        if len(opts.args) != 2:
            ap.error("--contrast needs exactly two hex colors")
        ratio = contrast_ratio(parse_hex(opts.args[0]), parse_hex(opts.args[1]))
        verdict = "AA pass (normal text)" if ratio >= 4.5 else (
            "AA pass (large text only)" if ratio >= 3.0 else "FAIL"
        )
        print(f"{opts.args[0]} on {opts.args[1]}: {ratio:.2f}:1 — {verdict}")
    else:
        extract(opts.args[0], opts.colors)


if __name__ == "__main__":
    main()
