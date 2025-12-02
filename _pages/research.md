---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
redirect_from:
  - /resume
---


Quasar Spectral Survey Analysis
------
Over the past decades, large-scale wide and deep field surveys with multi-wavelength coverage have facilitated the studies of quasars and AGNs. I have measured the spectral properties of millions of quasars and all data product are public to the community. 

### Sloan Digital Sky Survey (SDSS) quasars
#### SDSS-IV DR16Q
In [Wu & Shen (2022)](https://iopscience.iop.org/article/10.3847/1538-4365/ac9ead), we measured spectral properties for the 750,414 quasars included in the SDSS Data Release 16 Quasar (DR16Q) catalog (Lyke et al. 2020). These quasars cover broad ranges in redshift ($0.1\lesssim z\lesssim 6$) and luminosity ($44\lesssim \log{L_{\rm bol}/{\rm erg\, s^{-1}} \lesssim 48}$). Following established practice (e.g., Shen et al. 2011, 2019), we fit each spectrum with a global continuum–emission-line model using the public PyQSOFIT package (Guo et al. 2018), with minor, well-documented constraint adjustments. The input parameter file and reproducible workflow are available on [our GitHub repository](https://github.com/QiaoyaWu/sdss4_dr16q_tutorial).

#### SDSS-V DR19Q
We performed visual inspection and measured spectral properties for 82,363 quasars observed in the SDSS DR19. Public access for [the value-added catalog](https://www.sdss.org/dr19/data_access/value-added-catalogs/?vac_id=10009) is available.

### Dark Energy Spectroscopic Instrument (DESI) quasars
#### DESI EDR
[Wu & Shen (2023)](https://iopscience.iop.org/article/10.3847/2515-5172/acf580) provides improved systemic redshift estimates for $∼95$k quasars in the DESI Early Data Release (EDR) using refined emission-line fitting techniques. Similar methods will be applied to the DESI Data Release 1 upon its publication.

AGN Line-Emitting Region Photoionization
------
My recent publication ([Wu et al. 2025](https://iopscience.iop.org/article/10.3847/1538-4357/ada386)) statistically compares observed UV emission-line properties and BLR cloud distances with photoionization modeling for a subsample of quasars with reverberation mapping (RM) observations. These models successfully reproduce key trends in UV/optical line strengths and their dependence on accretion parameters, offering a new method to infer the unobservable ionizing continuum using optical/UV line flux ratios. Furthermore, my work qualitatively recovers the size-luminosity relation for the RM AGN sample, suggesting that BLR gas density and structure may evolve systematically with accretion rate. 


Black Hole Binary Dynamics
------
Stellar-mass black holes identified in X-ray binaries provide crucial insights into binary evolution and jet launching mechanisms. During my undergraduate studies, I collaborated with [Prof. Jianfeng Wu](https://astro.xmu.edu.cn/info/1036/1288.htm) on spectroscopic and photometric observations of black hole binary systems, including MAXI J1820+070 and [A0620-00](https://iopscience.iop.org/article/10.3847/1538-4357/ac4332). Our work focused on the dynamical analysis of the secondary star in these systems to refine mass estimates and investigate accretion properties.


Cosmological N-body Simulation
------
The large-scale structure (LSS) of the universe encodes key information about cosmology. One of the major goals of LSS studies is to reconstruct the initial conditions of the Universe from the present-day galaxy distribution. To explore the connection between cosmic initial conditions and present-day structure, I collaborated with [Prof. Haoran Yu](https://astro.xmu.edu.cn/info/1036/1292.htm) on cosmological N-body simulations using the [CUBE](https://ieeexplore.ieee.org/document/9139651) code. Our work examined the angular momentum evolution of dark matter halos and their connection to initial conditions. In [Wu et al. 2021](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.063522), we introduced a Lagrangian spin parameter and tidal twist parameters, quantifying their impact on spin conservation and predictability in N-body simulations ([Poster](http://qiaoyawu.github.io/files/QiaoyaWu_hangzhou_poster_show.pdf)).
