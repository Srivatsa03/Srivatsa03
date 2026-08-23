#!/usr/bin/env python3
"""Render a year of GitHub contributions as a 3D isometric calendar SVG.

    python scripts/isocal.py --user Srivatsa03 -o assets/isocal

Writes <out>-dark.svg and <out>-light.svg. A token in $GITHUB_TOKEN / $GH_TOKEN
is used for the GraphQL contributions query (required by the API).
"""
import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

API = "https://api.github.com/graphql"
QUERY = """
query($login:String!){
  user(login:$login){
    contributionsCollection{
      contributionCalendar{
        totalContributions
        weeks{ contributionDays{ contributionCount weekday } }
      }
    }
  }
}
"""

# (empty, l1, l2, l3, l4) top-face colors, per theme
THEMES = {
    "dark":  ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"],
    "light": ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"],
}
TEXT = {"dark": "#7d8590", "light": "#57606a"}


def shade(hex_color, factor):
    r = int(hex_color[1:3], 16); g = int(hex_color[3:5], 16); b = int(hex_color[5:7], 16)
    return f"#{int(r*factor):02x}{int(g*factor):02x}{int(b*factor):02x}"


def fetch(login):
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("need GITHUB_TOKEN / GH_TOKEN for the contributions query")
    body = json.dumps({"query": QUERY, "variables": {"login": login}}).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Authorization": f"bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "isocal",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = [[d["contributionCount"] for d in w["contributionDays"]] for w in cal["weeks"]]
    return cal["totalContributions"], weeks


def level(count, mx):
    if count <= 0:
        return 0
    q = count / mx
    return 1 if q <= 0.25 else 2 if q <= 0.5 else 3 if q <= 0.75 else 4


def build(total, weeks, theme):
    cols = THEMES[theme]
    tw, th = 13.0, 6.5          # half-width / half-height of the rhombus top
    base = 3.0                  # flat tile thickness
    lift = 42.0                 # max extra height for the busiest day
    mx = max((c for wk in weeks for c in wk), default=1) or 1

    cells, xs, ys = [], [], []
    for wi, wk in enumerate(weeks):
        for di in range(7):
            count = wk[di] if di < len(wk) else 0
            lv = level(count, mx)
            top = cols[lv]
            h = base + (count / mx) * lift
            cx = (wi - di) * tw
            cy = (wi + di) * th
            # top rhombus (raised by h), then left + right vertical faces
            tp = f"{cx},{cy-h-th} {cx+tw},{cy-h} {cx},{cy-h+th} {cx-tw},{cy-h}"
            lf = f"{cx-tw},{cy-h} {cx},{cy-h+th} {cx},{cy+th} {cx-tw},{cy}"
            rf = f"{cx+tw},{cy-h} {cx},{cy-h+th} {cx},{cy+th} {cx+tw},{cy}"
            cells.append((cy, tp, lf, rf, top))
            xs += [cx - tw, cx + tw]
            ys += [cy - h - th, cy + th]

    # painter's order: back to front
    cells.sort(key=lambda c: c[0])
    pad = 26
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    w = maxx - minx + 2 * pad
    h = maxy - miny + 2 * pad + 30
    dx, dy = -minx + pad, -miny + pad

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" '
             f'width="{w:.0f}" height="{h:.0f}" role="img" aria-label="isometric contribution calendar">']
    parts.append("<style>@keyframes rise{from{opacity:0}to{opacity:1}}"
                 ".c{animation:rise .9s ease-out both}</style>")
    parts.append(f'<g transform="translate({dx:.1f},{dy:.1f})">')
    for i, (_, tp, lf, rf, top) in enumerate(cells):
        delay = i / len(cells) * 1.2
        parts.append(f'<g class="c" style="animation-delay:{delay:.2f}s">'
                     f'<polygon points="{lf}" fill="{shade(top,0.55)}"/>'
                     f'<polygon points="{rf}" fill="{shade(top,0.72)}"/>'
                     f'<polygon points="{tp}" fill="{top}"/></g>')
    parts.append(f'<text x="{w/2:.0f}" y="{maxy-miny+pad+22:.0f}" text-anchor="middle" '
                 f'font-family="JetBrains Mono, ui-monospace, monospace" font-size="15" '
                 f'font-weight="600" fill="{TEXT[theme]}">{total:,} contributions in the last year</text>')
    parts.append("</g></svg>")
    return "".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", required=True)
    ap.add_argument("-o", "--out", type=Path, default=Path("assets/isocal"))
    args = ap.parse_args()
    total, weeks = fetch(args.user)
    for theme in ("dark", "light"):
        dest = args.out.with_name(f"{args.out.name}-{theme}.svg")
        dest.write_text(build(total, weeks, theme))
        print(f"wrote {dest} ({total} contributions, {len(weeks)} weeks)")


if __name__ == "__main__":
    main()
