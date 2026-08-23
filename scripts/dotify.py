#!/usr/bin/env python3
"""Render an image as a colored dot-matrix SVG.

One file serves both GitHub themes (colored dots on a transparent ground).
Generic image-processing, only dependency is Pillow.

    python scripts/dotify.py assets/profile.jpg -o assets/portrait.svg --cols 92
"""
import argparse
from PIL import Image, ImageOps


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("-o", "--out", default="portrait.svg")
    ap.add_argument("--cols", type=int, default=92)
    ap.add_argument("--step", type=int, default=12)
    ap.add_argument("--equalize", action="store_true")
    args = ap.parse_args()

    img = ImageOps.exif_transpose(Image.open(args.src)).convert("RGB")
    if args.equalize:
        img = ImageOps.equalize(img)
    w, h = img.size
    rows = max(1, round(args.cols * h / w))
    small = img.resize((args.cols, rows))

    step, r_base = args.step, args.step / 2
    vw, vh = args.cols * step, rows * step
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw} {vh}" '
           f'width="{vw}" height="{vh}">']
    for y in range(rows):
        for x in range(args.cols):
            r, g, b = small.getpixel((x, y))
            lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
            rad = r_base * (0.30 + 0.70 * (1 - lum))  # darker pixel, bigger dot
            if rad < 0.7:
                continue  # near-white ground stays transparent
            cx, cy = x * step + r_base, y * step + r_base
            out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{rad:.1f}" '
                       f'fill="#{r:02x}{g:02x}{b:02x}"/>')
    out.append("</svg>")
    with open(args.out, "w") as f:
        f.write("".join(out))
    print(f"wrote {args.out}: {vw}x{vh}, {args.cols}x{rows} grid, {len(out) - 2} dots")


if __name__ == "__main__":
    main()
