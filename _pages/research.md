---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
redirect_from:
  - /resume
---

<style>
  .research-section {
    border-top: 1px solid #d0d7de;
    margin-top: 2.4rem;
    padding-top: 1.8rem;
  }

  .research-section:first-of-type {
    border-top: 0;
    margin-top: 0;
    padding-top: 0;
  }

  .research-section > h2 {
    margin-top: 0;
  }

  .research-feature {
    --figure-width: 36%;
    display: flex;
    gap: 1.5rem;
    align-items: flex-start;
    margin: 0 0 2rem;
  }

  .research-feature__text {
    flex: 1 1 auto;
    min-width: 0;
  }

  .research-feature__figure {
    flex: 0 0 var(--figure-width);
    margin: 0;
  }

  .research-feature__figure img {
    display: block;
    width: 100%;
    height: auto;
    border: 1px solid #d0d7de;
    border-radius: 4px;
  }

  .research-feature__figure figcaption {
    margin-top: 0.45rem;
    color: #666;
    font-size: 0.8rem;
    line-height: 1.35;
  }

  .research-figure-strip {
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    margin: -0.75rem 0 2rem;
  }

  .research-figure-strip figure {
    margin: 0;
  }

  .research-figure-strip img {
    display: block;
    width: 100%;
    height: auto;
    border: 1px solid #d0d7de;
    border-radius: 4px;
  }

  .research-figure-strip figcaption {
    margin-top: 0.45rem;
    color: #666;
    font-size: 0.78rem;
    line-height: 1.35;
  }

  @media (max-width: 720px) {
    .research-feature {
      display: block;
    }

    .research-feature__figure {
      margin-top: 1rem;
    }

    .research-figure-strip {
      grid-template-columns: 1fr;
    }
  }
</style>

<section class="research-section" markdown="1">

Quasar Spectral Survey Analysis
------
<div class="research-feature" style="--figure-width: 36%;" markdown="1">
<div class="research-feature__text" markdown="1">

Large spectroscopic surveys have transformed the study of quasars and active galactic nuclei by providing uniform, multi-wavelength observations across cosmic time. My work develops and applies spectral-fitting methods to measure the physical properties of large quasar samples and produce value-added catalogs for the broader community.

### Sloan Digital Sky Survey (SDSS) quasars
#### SDSS-IV DR16Q
In [Wu & Shen (2022)](https://iopscience.iop.org/article/10.3847/1538-4365/ac9ead), we measured spectral properties for the 750,414 quasars in the SDSS Data Release 16 Quasar (DR16Q) catalog (Lyke et al. 2020). This sample spans broad ranges in redshift ($0.1\lesssim z\lesssim 6$) and luminosity ($44\lesssim \log{L_{\rm bol}/{\rm erg\, s^{-1}} \lesssim 48}$). Following established approaches (e.g., Shen et al. 2011, 2019), we fit each spectrum with a global continuum and emission-line model using the public PyQSOFIT package (Guo et al. 2018), with minor, well-documented adjustments to the fitting constraints. The input parameter file and reproducible workflow are available in [our GitHub repository](https://github.com/QiaoyaWu/sdss4_dr16q_tutorial).

#### SDSS-V DR19Q
We also performed visual inspection and measured spectral properties for 82,363 quasars observed in SDSS DR19. [The value-added catalog](https://www.sdss.org/dr19/data_access/value-added-catalogs/?vac_id=10009) is publicly available through SDSS.

### Dark Energy Spectroscopic Instrument (DESI) quasars
#### DESI EDR
[Wu & Shen (2023)](https://iopscience.iop.org/article/10.3847/2515-5172/acf580) provides improved systemic redshift estimates for approximately 95,000 quasars in the DESI Early Data Release (EDR) using refined emission-line fitting techniques. We are applying related methods to later DESI quasar samples.

</div>
<figure class="research-feature__figure">
  <img src="{{ '/images/sdss_dr16q_pyqsofit.png' | relative_url }}" alt="PyQSOFit on SDSS DR16Q">
  <figcaption>Example PyQSOFit decomposition for an SDSS DR16Q quasar spectrum.</figcaption>
</figure>
</div>

</section>

<section class="research-section" markdown="1">

AGN Line-Emitting Region Photoionization
------
<div class="research-feature" style="--figure-width: 36%;" markdown="1">
<div class="research-feature__text" markdown="1">

[Wu et al. (2025)](https://iopscience.iop.org/article/10.3847/1538-4357/ada386) compares observed UV emission-line properties and broad-line region (BLR) distances with photoionization models for a sample of reverberation-mapped quasars. These models reproduce key trends in UV and optical line strengths and their dependence on accretion properties, offering a way to infer the otherwise unobservable ionizing continuum from optical/UV line flux ratios. The same framework qualitatively recovers the radius-luminosity relation for the reverberation-mapped AGN sample, suggesting that BLR gas density and structure may evolve systematically with accretion rate.

[Wu et al. (2026)](https://arxiv.org/abs/2606.00992) extends this framework to high-accretion-rate AGNs using slim-disk SEDs and two-dimensional photoionization calculations. The models show that inner-disk self-shadowing reduces the ionizing flux reaching low-latitude BLR clouds and helps flatten the BLR radius-luminosity relation at high accretion rates. Additional accretion-rate-dependent BLR density evolution provides a compact explanation for the shortened reverberation lags observed in high-accretion-rate systems.

</div>
</div>

<div class="research-figure-strip">
  <figure>
    <a href="{{ '/images/self-shadow_fig3.png' | relative_url }}">
      <img src="{{ '/images/self-shadow_fig3.png' | relative_url }}" alt="Schematic of self-shadowing in a slim-disk AGN">
    </a>
    <figcaption>Fig. 3: slim-disk self-shadowing creates anisotropic illumination of the BLR.</figcaption>
  </figure>
  <figure>
    <a href="{{ '/images/self-shadow_fig5.png' | relative_url }}">
      <img src="{{ '/images/self-shadow_fig5.png' | relative_url }}" alt="Two-dimensional BLR photoionization emissivity map">
    </a>
    <figcaption>Fig. 5: two-dimensional BLR photoionization maps show how shielding changes the emitting region.</figcaption>
  </figure>
  <figure>
    <a href="{{ '/images/self-shadow_fig12.png' | relative_url }}">
      <img src="{{ '/images/self-shadow_fig12.png' | relative_url }}" alt="BLR size-luminosity relation with density-enhanced models">
    </a>
    <figcaption>Fig. 12: enhanced-density models help reproduce the observed BLR size-luminosity offsets.</figcaption>
  </figure>
</div>

</section>

<section class="research-section" markdown="1">

Black Hole Binary Dynamics
------
<div class="research-feature" style="--figure-width: 36%;" markdown="1">
<div class="research-feature__text" markdown="1">

Stellar-mass black holes in X-ray binaries provide important constraints on binary evolution, accretion physics, and jet launching. During my undergraduate studies, I collaborated with [Prof. Jianfeng Wu](https://astro.xmu.edu.cn/info/1036/1288.htm) on spectroscopic and photometric observations of black hole binary systems, including MAXI J1820+070 and A0620-00 ([Zheng et al. 2022](https://iopscience.iop.org/article/10.3847/1538-4357/ac4332)). Our work used dynamical measurements of the secondary star to refine black hole mass estimates and characterize the physical state of the accreting system.

</div>
<figure class="research-feature__figure">
  <img src="{{ '/images/blackholebinary_art.png' | relative_url }}" alt="Artist illustration of a black hole binary">
  <figcaption>Artist illustration of a black hole binary. Image credit: NASA/CXC/M. Weiss.</figcaption>
</figure>
</div>

</section>

<section class="research-section" markdown="1">

Cosmological N-body Simulation
------
<div class="research-feature" style="--figure-width: 42%;" markdown="1">
<div class="research-feature__text" markdown="1">

The large-scale structure (LSS) of the Universe encodes information about cosmology and the growth of structure. A central goal of LSS studies is to reconstruct the initial conditions of the Universe from the present-day galaxy distribution. To explore the connection between cosmic initial conditions and late-time structure, I collaborated with [Prof. Haoran Yu](https://astro.xmu.edu.cn/info/1036/1292.htm) on cosmological N-body simulations using the [CUBE](https://ieeexplore.ieee.org/document/9139651) code. Our work examined the angular-momentum evolution of dark matter halos and its connection to initial conditions. In [Wu et al. (2021)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.063522), we introduced a Lagrangian spin parameter and tidal-twist parameters to quantify spin conservation and predictability in N-body simulations.

</div>
<figure class="research-feature__figure">
  <a href="{{ '/files/QiaoyaWu_hangzhou_poster_show.pdf' | relative_url }}">
    <img src="{{ '/images/cosmology_poster_preview.png' | relative_url }}" alt="Preview of the cosmological N-body simulation poster">
  </a>
  <figcaption>Poster preview for the CUBE N-body simulation project on halo spin correlations and primordial perturbations.</figcaption>
</figure>
</div>

</section>
