"""Generate the three Life-page SVG maps from Natural Earth boundaries.

Install shapely, then run: python3 scripts/generate_travel_maps.py
Boundary data: https://www.naturalearthdata.com/ (public domain).
"""

import argparse
import csv
import json
from pathlib import Path
from urllib.request import urlopen
from xml.sax.saxutils import escape, quoteattr

from shapely.geometry import shape


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "travelmap"
SOURCE = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/"

COLORS = {"land": "#dce5e7", "hometown": "#c96b5c", "lived": "#4c9b9a", "travel": "#d5a54f"}
PRIORITY = {"travel": 1, "lived": 2, "hometown": 3}


def highlights_from_csv():
    highlights = {"world": {}, "china": {}, "usa": {}}
    with (OUTPUT / "places.csv").open(newline="", encoding="utf-8-sig") as source:
        for row in csv.DictReader(source):
            map_name, region, category = (row[column].strip() for column in ("map", "region", "category"))
            if map_name not in highlights or category not in PRIORITY:
                raise ValueError(f"Invalid map or category in places.csv: {row}")
            current = highlights[map_name].get(region)
            if current is None or PRIORITY[category] > PRIORITY[current]:
                highlights[map_name][region] = category
    return highlights


def data(name, local_path=None):
    if local_path:
        return json.loads(Path(local_path).read_text(encoding="utf-8"))["features"]
    with urlopen(SOURCE + name, timeout=30) as response:
        return json.load(response)["features"]


def geometry_path(geom, project):
    pieces = []
    if geom.geom_type == "Polygon":
        polygons = [geom]
    elif geom.geom_type == "MultiPolygon":
        polygons = geom.geoms
    else:
        return ""
    for polygon in polygons:
        for ring in [polygon.exterior, *polygon.interiors]:
            coords = [project(x, y) for x, y in ring.coords]
            pieces.append("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in coords) + "Z")
    return " ".join(pieces)


def map_svg(title, description, features, key, highlights, bounds, height=540):
    width = 1000
    left, bottom, right, top = bounds
    usable_width, usable_height = 920, height - 100
    scale = min(usable_width / (right - left), usable_height / (top - bottom))
    ox = (width - (right - left) * scale) / 2
    oy = 65 + (usable_height - (top - bottom) * scale) / 2

    def project(lon, lat):
        return ox + (lon - left) * scale, oy + (top - lat) * scale

    map_id = title.lower().replace(" ", "-")
    items = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{map_id}-title {map_id}-desc">',
        f'<title id="{map_id}-title">{escape(title)}</title>',
        f'<desc id="{map_id}-desc">{escape(description)}</desc>',
        '<rect width="1000" height="100%" rx="12" fill="#f5f9f9"/>',
        f'<text x="40" y="42" fill="#344b55" font-family="Arial,sans-serif" font-size="25" font-weight="600">{escape(title)}</text>',
    ]
    for feature in features:
        name = feature["properties"].get(key, "")
        geom = shape(feature["geometry"])
        # Keep the SVG light while preserving the outlines at this display size.
        geom = geom.simplify(0.08 if title == "World" else 0.018, preserve_topology=True)
        path = geometry_path(geom, project)
        if not path:
            continue
        fill = COLORS.get(highlights.get(name, "land"), COLORS["land"])
        stroke = "#fff" if title == "World" else "#f5f9f9"
        stroke_width = "0.7" if title == "World" else "1.2"
        items.append(
            f'<path data-region={quoteattr(name)} d="{path}" fill="{fill}" fill-rule="evenodd" '
            f'stroke="{stroke}" stroke-width="{stroke_width}" stroke-linejoin="round"><title>{escape(name)}</title></path>'
        )
    items.append('</svg>')
    return "\n".join(items) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--countries", help="Optional local Natural Earth country GeoJSON")
    parser.add_argument("--regions", help="Optional local Natural Earth admin-1 GeoJSON")
    parser.add_argument("--map-units", help="Optional local Natural Earth 10m map-unit GeoJSON")
    args = parser.parse_args()
    countries = data("ne_50m_admin_0_countries.geojson", args.countries)
    regions = data("ne_50m_admin_1_states_provinces.geojson", args.regions)
    map_units = data("ne_10m_admin_0_map_units.geojson", args.map_units)
    china_regions = [f for f in regions if f["properties"].get("admin") == "China"]
    for feature in map_units:
        name = feature["properties"].get("NAME")
        if name in {"Taiwan", "Hong Kong"}:
            china_regions.append({"properties": {"name": name}, "geometry": feature["geometry"]})
    highlights = highlights_from_csv()
    maps = [
        ("world.svg", "World", "Countries colored by hometown, lived, or travel category.",
         countries, "ADMIN", highlights["world"], (-170, -58, 190, 83), 490),
        ("china.svg", "China", "Provinces colored by hometown, lived, or travel category.",
         china_regions,
         "name", highlights["china"], (73, 18, 135, 54), 550),
        ("usa.svg", "United States", "States colored by hometown, lived, or travel category.",
         [f for f in regions if f["properties"].get("admin") == "United States of America"],
         "name", highlights["usa"], (-126, 24, -66, 50), 520),
    ]
    for filename, *args in maps:
        destination = OUTPUT / filename
        destination.write_text(map_svg(*args), encoding="utf-8")
        print(destination)


if __name__ == "__main__":
    main()
