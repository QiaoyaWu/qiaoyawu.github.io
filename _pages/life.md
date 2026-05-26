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

  .travel-map {
    border: 1px solid #d0d7de;
    border-radius: 4px;
    overflow: hidden;
    background: #f8fafc;
  }

  .travel-map iframe {
    display: block;
    width: 100%;
    height: min(72vh, 620px);
    min-height: 420px;
    border: 0;
  }

  .travel-map__caption {
    margin-top: 0;
    padding: 0 0.85rem 0.85rem;
    color: #666;
    font-size: 0.8rem;
    line-height: 1.35;
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
  <p>Travel map</p>

  <div class="travel-map">
    <iframe src="{{ '/travelmap/map.html' | relative_url }}" title="Interactive travel map"></iframe>
    <div class="travel-map__caption">Visited countries and regions. Drag, zoom, and click markers for labels.</div>
  </div>

</section>
