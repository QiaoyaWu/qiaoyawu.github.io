---
layout: archive
title: "Life"
permalink: /life/
author_profile: true
---

<style>
  .life-section {
    margin-bottom: 2.5rem;
  }

  .life-section p {
    margin-bottom: 1rem;
  }

  .nova-gallery {
    display: flex;
    gap: 1rem;
    overflow-x: auto;
    padding: 0.25rem 0 1rem;
    scroll-snap-type: x proximity;
  }

  .nova-gallery figure {
    flex: 0 0 min(76vw, 360px);
    margin: 0;
    scroll-snap-align: start;
  }

  .nova-gallery img {
    display: block;
    width: 100%;
    aspect-ratio: 4 / 3;
    object-fit: cover;
    border: 1px solid #d0d7de;
    border-radius: 4px;
  }

  .nova-gallery figcaption,
  .travel-map__caption {
    margin-top: 0.45rem;
    color: #666;
    font-size: 0.8rem;
    line-height: 1.35;
  }

  .travel-map {
    border: 1px solid #d0d7de;
    border-radius: 4px;
    overflow: hidden;
    background: #f8fafc;
  }

  .travel-map svg {
    display: block;
    width: 100%;
    height: auto;
  }

  .travel-map .land {
    fill: #e7ecef;
    stroke: #c8d1d8;
    stroke-width: 1.2;
  }

  .travel-map .pin {
    fill: #bc4b51;
    stroke: #fff;
    stroke-width: 2;
  }

  .travel-map .pin-ring {
    fill: rgba(188, 75, 81, 0.14);
    stroke: rgba(188, 75, 81, 0.38);
    stroke-width: 1;
  }

  .travel-map__caption {
    padding: 0 0.85rem 0.85rem;
  }

  .travel-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-top: 0.9rem;
  }

  .travel-list span {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    border: 1px solid #d0d7de;
    border-radius: 4px;
    color: #444;
    font-size: 0.82rem;
    line-height: 1.2;
  }
</style>

<section class="life-section">
  <h2>Nova the cat</h2>
  <p>A small corner for Nova, who brings a different kind of gravity to daily life.</p>

  <div class="nova-gallery" aria-label="Horizontally scrollable photo gallery of Nova the cat">
    <figure>
      <img src="{{ '/images/nova/nova1.jpg' | relative_url }}" alt="Nova the cat">
      <figcaption>Nova.</figcaption>
    </figure>
    <figure>
      <img src="{{ '/images/nova/nova2.JPG' | relative_url }}" alt="Nova the cat">
      <figcaption>Nova.</figcaption>
    </figure>
    <figure>
      <img src="{{ '/images/nova/nova3.jpg' | relative_url }}" alt="Nova the cat">
      <figcaption>Nova.</figcaption>
    </figure>
  </div>
</section>

<section class="life-section">
  <h2>Travel</h2>
  <p>Places I have visited, marked at country scale.</p>

  <div class="travel-map" role="img" aria-label="World map highlighting countries visited: China including Taiwan, South Korea, Thailand, Malaysia, Singapore, Philippines, United States, United Kingdom, Germany, Bahamas, Turks and Caicos, and Dominican Republic.">
    <svg viewBox="0 0 1000 500" xmlns="http://www.w3.org/2000/svg">
      <rect width="1000" height="500" fill="#f8fafc"/>
      <path class="land" d="M105,155 C145,95 215,75 280,103 C330,125 340,175 303,215 C275,248 276,300 250,345 C223,390 158,370 142,315 C127,262 72,222 105,155 Z"/>
      <path class="land" d="M279,313 C325,306 362,338 374,386 C386,434 348,478 304,462 C262,447 255,401 268,363 C272,348 272,328 279,313 Z"/>
      <path class="land" d="M455,118 C503,78 602,72 680,104 C738,128 785,122 842,145 C914,174 905,236 839,244 C786,251 747,230 710,259 C664,294 612,275 586,238 C562,205 511,206 471,190 C434,175 422,145 455,118 Z"/>
      <path class="land" d="M506,222 C548,204 602,229 618,280 C638,342 603,395 557,387 C514,381 493,337 495,291 C496,264 487,238 506,222 Z"/>
      <path class="land" d="M688,303 C724,284 779,301 801,336 C824,372 800,412 754,411 C706,410 672,376 674,340 C675,323 677,311 688,303 Z"/>
      <path class="land" d="M843,289 C882,274 929,286 951,318 C970,346 955,380 915,381 C872,383 831,354 826,321 C824,307 830,295 843,289 Z"/>

      <g>
        <circle class="pin-ring" cx="789" cy="153" r="11"/><circle class="pin" cx="789" cy="153" r="5"><title>China</title></circle>
        <circle class="pin-ring" cx="836" cy="183" r="10"/><circle class="pin" cx="836" cy="183" r="5"><title>Taiwan</title></circle>
        <circle class="pin-ring" cx="856" cy="150" r="10"/><circle class="pin" cx="856" cy="150" r="5"><title>South Korea</title></circle>
        <circle class="pin-ring" cx="781" cy="208" r="10"/><circle class="pin" cx="781" cy="208" r="5"><title>Thailand</title></circle>
        <circle class="pin-ring" cx="783" cy="239" r="10"/><circle class="pin" cx="783" cy="239" r="5"><title>Malaysia</title></circle>
        <circle class="pin-ring" cx="789" cy="246" r="10"/><circle class="pin" cx="789" cy="246" r="5"><title>Singapore</title></circle>
        <circle class="pin-ring" cx="839" cy="217" r="10"/><circle class="pin" cx="839" cy="217" r="5"><title>Philippines</title></circle>
        <circle class="pin-ring" cx="228" cy="142" r="11"/><circle class="pin" cx="228" cy="142" r="5"><title>United States</title></circle>
        <circle class="pin-ring" cx="494" cy="100" r="10"/><circle class="pin" cx="494" cy="100" r="5"><title>United Kingdom</title></circle>
        <circle class="pin-ring" cx="528" cy="108" r="10"/><circle class="pin" cx="528" cy="108" r="5"><title>Germany</title></circle>
        <circle class="pin-ring" cx="286" cy="181" r="10"/><circle class="pin" cx="286" cy="181" r="5"><title>Bahamas</title></circle>
        <circle class="pin-ring" cx="300" cy="189" r="10"/><circle class="pin" cx="300" cy="189" r="5"><title>Turks and Caicos</title></circle>
        <circle class="pin-ring" cx="306" cy="197" r="10"/><circle class="pin" cx="306" cy="197" r="5"><title>Dominican Republic</title></circle>
      </g>
    </svg>
    <div class="travel-map__caption">Visited countries and regions, marked approximately on a stylized world map.</div>
  </div>

  <div class="travel-list" aria-label="Visited countries and regions">
    <span>China (including Taiwan)</span>
    <span>South Korea</span>
    <span>Thailand</span>
    <span>Malaysia</span>
    <span>Singapore</span>
    <span>Philippines</span>
    <span>United States</span>
    <span>United Kingdom</span>
    <span>Germany</span>
    <span>Bahamas</span>
    <span>Turks and Caicos</span>
    <span>Dominican Republic</span>
  </div>
</section>
