---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---
Hi, I am Qiaoya Wu (吴巧雅), a third-year graduate student in the Department of Astronomy at the University of Illinois, Urbana-Champaign.
I work with [Prof. Yue Shen](http://quasar.astro.illinois.edu/index.html#) on multi-wavelength observations on active galactic nuclei (AGNs/quasars), quasar spectral surveys, black hole binaries, and cosmological large-scale structure.

[View CV](http://qiaoyawu.github.io/files/CV_for_web.pdf)


Education
======
2017-2021: B.Sc. in Astronomy, Xiamen University, China \
2021-present: Graduate student in Astronomy, University of Illinois at Urbana-Champaign


Research
======

Quasar spectral survey analysis
------
Over the past decades, large-scale wide and deep field surveys such as the Sloan Digital Sky Survey (SDSS) with multi-wavelength coverage have facilitated the studies of quasars and AGNs. In essence, these large, homogeneous data sets allow statistical analysis of the phenomenological properties of quasars, offering new insights into how the central engine powers these objects and their connections to their host galaxies. Meanwhile, detailed investigations of fitting the quasar/AGN population into the cosmological context have become possible with these samples, i.e., how the supermassive black hole population evolves along with its host galaxy across cosmic time. Such survey data have led to a coherent picture of the cosmic evolution of the SMBH population within the concordance $\Lambda$CDM paradigm and will give us unique opportunities to measure quasar properties with unprecedented precision.

In my recent work [Wu & Shen (2022)](https://iopscience.iop.org/article/10.3847/1538-4365/ac9ead), we measured spectral properties for the 750,414 quasars included in the latest SDSS Data Release 16 Quasar (DR16Q) catalog (Lyke et al. 2020). These quasars cover broad ranges in redshift ($0.1\lesssim z\lesssim 6$) and luminosity ($44\lesssim \log{L_{\rm bol}/{\rm erg\, s^{-1}} \lesssim 48}$). Starting from this quasar catalog, we follow the practice in earlier work (e.g., Shen et al. 2011, 2019) to fit the SDSS spectra with a global continuum+emission lines model, using the public code PyQSOFIT (Guo et al. 2018) implemented minor custom adjustments to the fitting constraints. These modifications include the removal of absorption pixels within the emission line complex, the inclusion of saving more comprehensive fitting information, the addition of local fitting, and other fine-tuning measures. The input fitting parameter file is conveniently accessible online through our [GitHub repository](https://github.com/QiaoyaWu/sdss4_dr16q_tutorial).

Broad-line Region Study with UV Spectroscopy
------
Nearly two decades of reverberation mapping (RM) studies on nearby AGN have revealed a tight correlation between the size of the Hbeta broad-line region and the optical luminosity of the AGN, designated the R-L relation. However, recent RM studies targeting AGNs across broad ranges of luminosities and Eddington ratios have found evidence for increased scatter around the canonical R − L relation (Du et al. 2014; Grier et al. 2017; Shen et al. 2023). The most likely explanation of this offset is that these new RM samples explore AGNs that have different accretion rates and therefore different shapes of the continuum spectral energy distribution (SED), responsible for ionizing the line-emitting gas, than the nearby RM AGN sample. Therefore, I am modeling the UV spectra with detailed photoionization calculations to constrain the ionizing continuum directly incident on the broad-line region gas. The combination of UV and optical spectroscopy for AGN samples with direct RM-based black hole masses will enable better SED-fitting to constrain accretion parameters and better calibrations of single-epoch mass recipes based on UV broad emission lines.

Black Hole Binary Dynamics
------
Stellar-mass black holes have long been identified in X-ray binaries, and accurate measurement of the black hole mass is essential to a variety of astrophysical topics, e.g., supernova progenitors, binary evolution, and jet launching mechanisms (Remillard & McClintock 2006). Under the supervision of [Prof. Jianfeng Wu](https://astro.xmu.edu.cn/info/1036/1288.htm), we carried out simultaneous spectroscopic and photometric campaigns on black hole binary systems MAXIJ1820+070 and [A0620-00](https://iopscience.iop.org/article/10.3847/1538-4357/ac4332), and performed dynamical analysis on the secondary star of such systems.

Cosmological N-body Simulation
------
The large-scale structure (LSS) of the Universe contains plenty of cosmological information. One of the most important tasks of LSS studies is to use the distribution of galaxies to interpret the initial conditions of the Universe and cosmological parameters. To investigate the inner relations between the early universe and current LSS, I worked with [Prof. Haoran Yu](https://astro.xmu.edu.cn/info/1036/1292.htm) using cosmological N-body simulation code CUBE to study the angular momentum of dark matter halos in $z=0$ and initial conditions. In [Wu et al. 2021](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.063522), we defined a Lagrangian spin parameter and tidal twist parameters and quantified their influence on the spin conservation and predictability in the spin mode reconstruction in N-body simulations([Poster of this work](http://qiaoyawu.github.io/files/QiaoyaWu_hangzhou_poster_show.pdf)).


