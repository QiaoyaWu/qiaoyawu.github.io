---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
redirect_from:
  - /resume
---


Recent
======

Quasar Spectral Survey Analysis
------
Over the past decades, large-scale wide and deep field surveys such as the Sloan Digital Sky Survey (SDSS) with multi-wavelength coverage have facilitated the studies of quasars and AGNs. In essence, these large, homogeneous data sets allow statistical analysis of the phenomenological properties of quasars, offering new insights into how the central engine powers these objects and their connections to their host galaxies. Meanwhile, detailed investigations of fitting the quasar/AGN population into the cosmological context have become possible with these samples, i.e., how the supermassive black hole population evolves along with its host galaxy across cosmic time. Such survey data have led to a coherent picture of the cosmic evolution of the SMBH population within the concordance $\Lambda$CDM paradigm and will give us unique opportunities to measure quasar properties with unprecedented precision.

In [Wu & Shen (2022)](https://iopscience.iop.org/article/10.3847/1538-4365/ac9ead), we measured spectral properties for the 750,414 quasars included in the latest SDSS Data Release 16 Quasar (DR16Q) catalog (Lyke et al. 2020). These quasars cover broad ranges in redshift ($0.1\lesssim z\lesssim 6$) and luminosity ($44\lesssim \log{L_{\rm bol}/{\rm erg\, s^{-1}} \lesssim 48}$). Starting from this quasar catalog, we follow the practice in earlier work (e.g., Shen et al. 2011, 2019) to fit the SDSS spectra with a global continuum+emission lines model, using the public code PyQSOFIT (Guo et al. 2018) implemented minor custom adjustments to the fitting constraints. The input fitting parameter file is conveniently accessible online through our [GitHub repository](https://github.com/QiaoyaWu/sdss4_dr16q_tutorial).

With the upcoming Dark Energy Spectroscopic Instrument (DESI) survey that is expecting to provide optical spectra for $\sim3$ million quasars. Accurate redshifts for these quasars will facilitate a broad range of science applications. In [Wu & Shen (2023)](https://iopscience.iop.org/article/10.3847/2515-5172/acf580), we provide improved systemic redshift estimates for the $\sim95$k quasars included in the DESI Early Data Release (EDR), based on emission-line fits to the quasar spectra. We plan on applying similar method to the DESI Data Release 1 after the data are published. Please stay tuned! 

Broad-Line Region Photoionization Computation
------
Over three decades of reverberation mapping (RM) studies on local broad-line active galactic nuclei (AGNs) have measured reliable black-hole (BH) masses for $> 100$ AGNs. These RM measurements reveal a significant correlation between the Balmer broad-line region (BLR) size and the AGN optical luminosity (the $R-L$ relation). 
Recent RM studies for AGN samples with more diverse BH accretion parameters (e.g., mass and Eddington ratio) reveal a substantial intrinsic dispersion around the average $R-L$ relation, suggesting variations in the broad-band spectrum as functions of accretion parameters and other factors such as cloud geometry and transfer function significantly influence the BLR size.
In [Wu et al. 2024](https://arxiv.org/abs/2407.01737), we perform a detailed photoionization investigation of expected broad-line properties as functions of accretion parameters, using the latest AGN continuum models implemented in {\tt qsosed}. We compare theoretical predictions with observations of a sample of 67 $z\lesssim0.5$ reverberation-mapped AGNs with both rest-frame optical and UV spectra in the moderate-accretion regime (Eddington ratio $L/L_{\rm Edd}<0.5$). The UV/optical line strengths and their dependences on accretion parameters are reasonably well reproduced by the locally-optimally-emitting cloud (LOC) photoionization models. We provide quantitative recipes using optical/UV line flux ratios to infer the ionizing continuum, which is not directly observable. Additionally, photoionization models with universal values of ionization parameter ($\log U_{\rm H}=-2$) and hydrogen density ($\log n({\rm H})=12$) can qualitatively reproduce the observed global $R-L$ relation for the current AGN samples. However, such models fail to reproduce the observed decrease in BLR size with increasing $L/L_{\rm Edd}$ at fixed optical luminosity, implying that the gas density may increase with the accretion rate.  

Previous Work
=====

Black Hole Binary Dynamics
------
Stellar-mass black holes have long been identified in X-ray binaries, and accurate measurement of the black hole mass is essential to a variety of astrophysical topics, such as binary evolution and jet launching mechanisms. During my undergrad, I worked with [Prof. Jianfeng Wu](https://astro.xmu.edu.cn/info/1036/1288.htm), carring out simultaneous spectroscopic and photometric campaigns on black hole binary systems MAXIJ1820+070 and [A0620-00](https://iopscience.iop.org/article/10.3847/1538-4357/ac4332), and performed dynamical analysis on the secondary star of such systems.

Cosmological N-body Simulation
------
The large-scale structure (LSS) of the Universe contains plenty of cosmological information. One of the most important tasks of LSS studies is to use the distribution of galaxies to interpret the initial conditions of the Universe and cosmological parameters. To investigate the inner relations between the early universe and current LSS, I worked with [Prof. Haoran Yu](https://astro.xmu.edu.cn/info/1036/1292.htm) using cosmological N-body simulation code [CUBE](https://ieeexplore.ieee.org/document/9139651) to study the angular momentum of dark matter halos in $z=0$ and initial conditions. In [Wu et al. 2021](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.063522), we defined a Lagrangian spin parameter and tidal twist parameters and quantified their influence on the spin conservation and predictability in the spin mode reconstruction in N-body simulations([Poster of this work](http://qiaoyawu.github.io/files/QiaoyaWu_hangzhou_poster_show.pdf)).


