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

  .travel-gallery {
    display: flex;
    gap: 1rem;
    overflow-x: auto;
    padding: 0.25rem 0 1rem;
    scroll-snap-type: x proximity;
  }

  .travel-map {
    flex: 0 0 min(88%, 720px);
    margin: 0;
    scroll-snap-align: start;
    border: 1px solid #d0d7de;
    border-radius: 4px;
    overflow: hidden;
    background: #f8fafc;
  }

  .travel-map img,
  .travel-map svg {
    display: block;
    width: 100%;
    height: auto;
  }

  .travel-map figcaption {
    padding: 0.55rem 0.85rem 0.7rem;
    color: #555;
    font-size: 0.85rem;
    line-height: 1.4;
  }

  .travel-key {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem 1.25rem;
    margin: 0 0 1rem;
    font-size: 0.85rem;
  }

  .travel-key span {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
  }

  .travel-key i {
    width: 0.8rem;
    height: 0.8rem;
    border-radius: 2px;
    display: inline-block;
  }
</style>

<section class="life-section">
  <h2>Nova the cat</h2>
  <p>A small corner for my cat Nova, who brings a different kind of gravity to my life.</p>

  <div class="nova-gallery" aria-label="Horizontally scrollable photo gallery of Nova the cat">
    <figure>
      <img src="{{ '/images/nova/nova1.jpg' | relative_url }}" alt="Nova the cat">
    </figure>
    <figure>
      <img src="{{ '/images/nova/nova2.JPG' | relative_url }}" alt="Nova the cat">
    </figure>
    <figure>
      <img src="{{ '/images/nova/nova3.jpeg' | relative_url }}" alt="Nova the cat">
    </figure>
    <figure>
      <img src="{{ '/images/nova/nova4.JPG' | relative_url }}" alt="Nova the cat">
    </figure>
  </div>
</section>

<section class="life-section">
  <h2>Travel</h2>
  <p>A few places that have been part of my story. More to come!</p>

  <div class="travel-key" aria-label="Map color key">
    <span><i style="background: #c96b5c"></i>Hometown</span>
    <span><i style="background: #4c9b9a"></i>Lived</span>
    <span><i style="background: #d5a54f"></i>Traveled</span>
  </div>

  <div class="travel-gallery" aria-label="Horizontally scrollable travel map gallery">
    <figure class="travel-map" data-map="world">
      <img src="{{ '/travelmap/world.svg' | relative_url }}" alt="World map with colored countries">
      <figcaption>Hometown: China | Lived: United States of America | Traveled: Singapore · Germany · South Korea · Malaysia · United Kingdom</figcaption>
    </figure>

    <figure class="travel-map" data-map="china">
      <img src="{{ '/travelmap/china.svg' | relative_url }}" alt="China map with colored provinces">
      <figcaption>Hometown: Sichuan | Lived: Fujian | Traveled: Hubei · Yunnan · Beijing</figcaption>
    </figure>

    <figure class="travel-map" data-map="usa">
      <img src="{{ '/travelmap/usa.svg' | relative_url }}" alt="United States map with colored states">
      <figcaption>Lived: Illinois · New York | Traveled: California · Florida</figcaption>
    </figure>
  </div>
</section>

<script defer src="{{ '/travelmap/paint.js' | relative_url }}" data-places="{{ '/travelmap/places.csv' | relative_url }}"></script>
