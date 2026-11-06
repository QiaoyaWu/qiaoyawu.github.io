// The SVGs provide boundaries; places.csv provides the colors and captions.
(() => {
  const script = document.currentScript;
  const colors = { hometown: "#c96b5c", lived: "#4c9b9a", travel: "#d5a54f" };
  const priority = { travel: 1, lived: 2, hometown: 3 };
  const labels = { hometown: "Hometown", lived: "Lived", travel: "Traveled" };

  function parseLine(line) {
    const values = [];
    let value = "";
    let quoted = false;
    for (let index = 0; index < line.length; index += 1) {
      const char = line[index];
      if (char === '"' && quoted && line[index + 1] === '"') {
        value += '"';
        index += 1;
      } else if (char === '"') {
        quoted = !quoted;
      } else if (char === "," && !quoted) {
        values.push(value.trim());
        value = "";
      } else {
        value += char;
      }
    }
    values.push(value.trim());
    return values;
  }

  function parsePlaces(csv) {
    const lines = csv.replace(/^\uFEFF/, "").trim().split(/\r?\n/);
    const columns = parseLine(lines.shift());
    if (columns.join(",") !== "map,region,category") {
      throw new Error("places.csv needs map,region,category columns");
    }
    return lines.filter((line) => line.trim()).map((line) => {
      const values = parseLine(line);
      return Object.fromEntries(columns.map((column, index) => [column, values[index]]));
    });
  }

  async function paintMap(figure, places) {
    const image = figure.querySelector("img");
    const response = await fetch(image.src, { cache: "no-cache" });
    if (!response.ok) throw new Error(`Could not load ${image.src}`);
    const documentSvg = new DOMParser().parseFromString(await response.text(), "image/svg+xml");
    const svg = documentSvg.documentElement;
    if (svg.localName !== "svg" || svg.querySelector("parsererror")) {
      throw new Error(`Invalid SVG: ${image.src}`);
    }

    const categories = new Map();
    places.filter((place) => place.map === figure.dataset.map).forEach((place) => {
      if (!priority[place.category] || !place.region) return;
      const current = categories.get(place.region);
      if (!current || priority[place.category] > priority[current]) {
        categories.set(place.region, place.category);
      }
    });

    const available = new Set();
    svg.querySelectorAll("path[data-region]").forEach((path) => {
      const region = path.getAttribute("data-region");
      const category = categories.get(region);
      available.add(region);
      path.setAttribute("fill", category ? colors[category] : "#dce5e7");
    });

    const displayed = { hometown: [], lived: [], travel: [] };
    places.filter((place) => place.map === figure.dataset.map).forEach((place) => {
      const category = categories.get(place.region);
      if (available.has(place.region) && category && !displayed[category].includes(place.region)) {
        displayed[category].push(place.region);
      }
    });

    const caption = Object.keys(displayed)
      .filter((category) => displayed[category].length)
      .map((category) => `${labels[category]}: ${displayed[category].join(" · ")}`)
      .join("  |  ");
    figure.querySelector("figcaption").textContent = caption || "No places added yet";
    image.replaceWith(document.importNode(svg, true));
  }

  fetch(script.dataset.places, { cache: "no-cache" })
    .then((response) => {
      if (!response.ok) throw new Error("Could not load places.csv");
      return response.text();
    })
    .then((csv) => {
      const places = parsePlaces(csv);
      return Promise.all(
        [...document.querySelectorAll(".travel-map[data-map]")].map((figure) =>
          paintMap(figure, places).catch((error) => console.warn(error))
        )
      );
    })
    .catch((error) => console.warn(error));
})();
