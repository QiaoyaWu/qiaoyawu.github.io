#!/usr/bin/env python3
"""Generate a research-buzzword cloud from Qiaoya Wu's ADS corpus.

The frequencies below were extracted from the titles and abstracts of the
20 records in the public ADS library linked from the website. Generic prose
terms were removed and closely related variants were consolidated.
"""

from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "images" / "research-buzzwords.png"

WIDTH = 1600
HEIGHT = 920
MARGIN = 26
SEED = 20260908

FONT_REGULAR = Path("/System/Library/Fonts/Supplemental/Verdana.ttf")
FONT_BOLD = Path("/System/Library/Fonts/Supplemental/Verdana Bold.ttf")

COLORS = (
    "#075985",  # observatory blue
    "#0891B2",  # cyan
    "#0F766E",  # teal
    "#4F46E5",  # indigo
    "#7C3AED",  # violet
    "#BE185D",  # magenta
    "#DC2626",  # red
    "#D97706",  # amber
    "#3F6212",  # green
)

# Title words were counted twice and abstract words once. Values retain the
# relative prominence of the ADS corpus after stopword removal and phrase
# consolidation; they are not citation weights.
FREQUENCIES = {
    "AGN": 79,
    "Black holes": 39,
    "X-ray": 34,
    "Quasars": 32,
    "Surveys": 25,
    "SDSS": 24,
    "Black-hole mass": 23,
    "eROSITA": 21,
    "Spectra": 20,
    "Optical": 19,
    "Redshifts": 18,
    "BLR": 17,
    "Outflows": 16,
    "eFEDS": 14,
    "Accretion disk": 13,
    "Galaxies": 13,
    "Stellar populations": 12,
    "Gas density": 12,
    "Emission": 11,
    "GRID": 11,
    "Soft excess": 11,
    "Universe": 10,
    "SDSS-V": 10,
    "Supermassive": 10,
    "Spectroscopy": 10,
    "Photoionization": 9,
    "Luminosity": 9,
    "Absorption": 9,
    "Host galaxies": 8,
    "Broad lines": 8,
    "Flux": 8,
    "Accretion": 8,
    "Ionized gas": 8,
    "Coronae": 8,
    "Spin": 8,
    "Velocity": 7,
    "Broad-line region": 7,
    "R–L relation": 7,
    "Sky": 7,
    "Transient": 7,
    "Relativistic": 7,
    "Little Red Dots": 7,
    "DESI": 7,
    "Gamma-ray": 7,
    "Continuum": 6,
    "Emission lines": 6,
    "SMBH": 6,
    "BLAGNs": 6,
    "All-sky": 6,
    "Variability": 6,
    "Simulations": 6,
    "Weak-line quasars": 6,
    "Catalogs": 6,
    "Lagrangian": 6,
    "CUBE": 6,
    "Scaling relations": 6,
    "Spectral fitting": 5,
    "Eddington ratio": 5,
    "Cosmology": 5,
    "Galaxy evolution": 5,
    "Reconstruction": 5,
    "Self-shadowing": 4,
    "Accretion rate": 4,
    "Decomposition": 4,
    "High redshift": 4,
    "Cosmic structure": 4,
    "N-body": 4,
    "Reverberation mapping": 4,
    "Gravitational waves": 3,
    "Spectral energy distribution": 6,
    "Multi-wavelength": 4,
    "Dark matter halos": 3,
}


def font_size(weight: int, minimum: int, maximum: int) -> int:
    low = min(FREQUENCIES.values())
    high = max(FREQUENCIES.values())
    scaled = (math.sqrt(weight) - math.sqrt(low)) / (
        math.sqrt(high) - math.sqrt(low)
    )
    return round(minimum + scaled * (maximum - minimum))


def boxes_overlap(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> bool:
    return not (a[2] <= b[0] or a[0] >= b[2] or a[3] <= b[1] or a[1] >= b[3])


def render_word(word: str, size: int, color: str, vertical: bool) -> Image.Image:
    font_path = FONT_BOLD if size >= 54 else FONT_REGULAR
    font = ImageFont.truetype(str(font_path), size=size)
    probe = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    bbox = probe.textbbox((0, 0), word, font=font, stroke_width=0)
    w = bbox[2] - bbox[0] + 10
    h = bbox[3] - bbox[1] + 10
    tile = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(tile)
    draw.text((5 - bbox[0], 5 - bbox[1]), word, font=font, fill=color)
    if vertical:
        tile = tile.rotate(90, expand=True, resample=Image.Resampling.BICUBIC)
    return tile


def main() -> None:
    random.seed(SEED)
    canvas = Image.new("RGB", (WIDTH, HEIGHT), "white")
    occupied: list[tuple[int, int, int, int]] = []

    ordered = sorted(FREQUENCIES.items(), key=lambda item: (-item[1], item[0]))
    for rank, (word, weight) in enumerate(ordered):
        size = font_size(weight, minimum=22, maximum=144)
        vertical = rank > 8 and weight <= 10 and random.random() < 0.20
        color = COLORS[(rank * 5 + random.randrange(len(COLORS))) % len(COLORS)]

        placed = False
        for shrink in (1.0, 0.90, 0.80, 0.70, 0.58, 0.48):
            tile = render_word(word, round(size * shrink), color, vertical)
            max_dx = (WIDTH - 2 * MARGIN - tile.width) / 2
            max_dy = (HEIGHT - 2 * MARGIN - tile.height) / 2
            if max_dx <= 0 or max_dy <= 0:
                continue

            # Try the center first, then expand a deterministic random search
            # over the full field. This keeps the visual dense without making
            # placement depend on an external word-cloud package.
            for step in range(5500):
                if step == 0:
                    x = round(WIDTH / 2 - tile.width / 2)
                    y = round(HEIGHT / 2 - tile.height / 2)
                else:
                    spread = min(1.0, 0.10 + step / 1800)
                    x = round(WIDTH / 2 - tile.width / 2 + random.uniform(-max_dx, max_dx) * spread)
                    y = round(HEIGHT / 2 - tile.height / 2 + random.uniform(-max_dy, max_dy) * spread)

                box = (x - 4, y - 3, x + tile.width + 4, y + tile.height + 3)
                if any(boxes_overlap(box, other) for other in occupied):
                    continue

                canvas.paste(tile, (x, y), tile)
                occupied.append(box)
                placed = True
                break

            if placed:
                break

        if not placed:
            print(f"Skipped {word!r}: no collision-free position")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUTPUT, optimize=True, dpi=(180, 180))
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
