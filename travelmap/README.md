# Editing the Life page maps

Edit `places.csv` as a spreadsheet. Each row needs a map (`world`, `china`, or
`usa`), an exact region name, and a category (`hometown`, `lived`, or `travel`).
Add or remove rows, then push the CSV file to GitHub. The Life page reads it
when it loads, so the SVG maps and their captions update without regenerating
the SVG files. A region can have multiple rows; `hometown` takes priority over
`lived`, which takes priority over `travel`.

The `world` map uses country names; the `china` and `usa` maps use province and
state names from Natural Earth. Hover over a region on the Life page to see its
exact name. The three SVGs contain the boundaries and fallback colors. Only
regenerate them if the boundaries themselves need to change:

```sh
python3 -m pip install shapely
python3 scripts/generate_travel_maps.py
```

Boundary data: [Natural Earth](https://www.naturalearthdata.com/), public domain.
