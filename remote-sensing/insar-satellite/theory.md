# InSAR — Satellite Interferometric Synthetic Aperture Radar

## Principles

Interferometric Synthetic Aperture Radar (InSAR) measures ground surface displacement by comparing the phase of radar signals from repeat satellite passes over the same area. A single SAR image provides backscatter intensity (surface roughness/material); two images from slightly different positions or times produce an interferogram whose phase differences encode topography (DEM generation) or surface displacement (deformation monitoring).

### SAR Fundamentals
SAR uses microwave energy (C-band ~5.6 cm, L-band ~23.6 cm, X-band ~3.1 cm) transmitted as pulses and recorded as returns. Synthetic aperture processing uses satellite motion to synthesize a long antenna, achieving fine azimuth resolution (typically 3–20 m) independent of range. Key advantage: all-weather, day/night acquisition — clouds and darkness are transparent at radar wavelengths.

### Interferometry
Two SAR images of the same area are co-registered and differenced in phase. The phase difference (interferogram) contains contributions from:
- **Topography:** baseline geometry between two acquisition positions
- **Deformation:** line-of-sight (LOS) displacement between acquisitions
- **Atmospheric delay:** tropospheric and ionospheric path length variations
- **Orbital errors:** imprecise satellite position knowledge
- **Noise:** thermal noise, temporal decorrelation, geometric decorrelation

**Differential InSAR (DInSAR):** Removes topographic phase using a DEM, isolating the deformation signal. Detects displacement in the satellite line-of-sight direction with sensitivity of a fraction of the radar wavelength (mm-scale).

### Persistent Scatterer InSAR (PSInSAR / PS-InSAR)
Advanced time-series technique using many SAR images (typically 20–60+) to identify Persistent Scatterers — stable point-like reflectors (buildings, infrastructure, rock outcrops, utility structures) that maintain coherent phase over time. Benefits: overcomes atmospheric noise through statistical separation, provides time-series displacement history for each PS point, achieves sub-mm/year velocity precision. Limitations: requires sufficient PS density (works best in urban/infrastructure-rich areas), needs large image stacks.

### Small Baseline Subset (SBAS)
Alternative time-series approach that uses interferograms with small spatial and temporal baselines. Better for distributed scattering surfaces (agricultural areas, bare soil, sparse vegetation). Lower spatial resolution than PS-InSAR but works in areas with fewer point scatterers.

## Applications in Geotechnical/Infrastructure Engineering

### Dam Deformation Monitoring
- **Concrete dams:** PS-InSAR detects crest displacement, abutment movement, foundation settlement. Corner reflectors installed on dam improve PS density.
- **Embankment dams:** SBAS detects settlement of crest and downstream face. Seasonal thermal/moisture cycling must be separated from structural movement.
- **Reservoir-induced effects:** Monitors ground response to filling/drawdown cycles (reservoir slope instability, foundation compression).

### Ground Subsidence
- **Groundwater extraction:** Regional subsidence from aquifer decompaction. Classic application — InSAR has mapped cm-scale subsidence in Mexico City, Las Vegas, San Joaquin Valley, Jakarta.
- **Mining subsidence:** Detects subsidence bowls over underground mines, identifies active zones, tracks subsidence rates.
- **Tunneling-induced settlement:** Monitors surface settlement above advancing TBM. Near-real-time processing (days to weeks latency) enables adaptive construction management.
- **Consolidation:** Long-term settlement of fills, embankments, and reclaimed land.

### Slope Stability & Landslides
- **Pre-failure detection:** Accelerating displacement identified in PS/SBAS time series weeks to months before failure.
- **Landslide inventory mapping:** Regional-scale identification of slow-moving slopes.
- **Post-failure monitoring:** Continued movement of landslide deposits.
- **Rock slope creep:** Extremely slow (mm/yr) movements detectable with multi-year time series.

### Infrastructure Monitoring
- **Bridges:** Settlement of abutments and piers detectable from PS-InSAR.
- **Levees/flood walls:** Detects differential settlement along levee alignments.
- **Pipelines:** Ground movement along pipeline corridors (slope creep, frost heave, thaw settlement).
- **Buildings:** Foundation settlement, tilt, and differential movement — especially useful for monitoring impact zones around construction.

## Measurement Characteristics

### Line-of-Sight (LOS) Sensitivity
InSAR measures displacement only in the satellite-to-ground direction (LOS). Ascending and descending orbits view from different angles, enabling decomposition into vertical and east-west components. North-south displacement is poorly resolved due to near-polar orbit geometry.

**Typical LOS incidence angle:** 20–45° from vertical. Most sensitive to vertical displacement (~70–90% of LOS component), with some sensitivity to east-west horizontal (~30–70% depending on incidence angle).

### Displacement Precision
- **Single interferogram:** ±5–15 mm (limited by atmospheric noise)
- **PS-InSAR time series:** ±1–3 mm on individual measurements; velocity precision 0.5–1.5 mm/year
- **SBAS time series:** ±3–8 mm per measurement; velocity 1–3 mm/year
- **Corner reflector augmented:** < 1 mm precision achievable

### Spatial Resolution and Coverage
- **Sentinel-1 (C-band, free):** 5×20 m (IW mode), 250 km swath, 6-day revisit (constellation)
- **TerraSAR-X (X-band):** 1–3 m (Spotlight), 10 km swath, 11-day revisit
- **COSMO-SkyMed (X-band):** 1–3 m, 10 km, 4–16 day revisit (constellation)
- **ALOS-2 PALSAR-2 (L-band):** 3–10 m, 25–70 km, 14-day revisit
- **NISAR (L+S band, launching):** 3–10 m, 240 km, 12-day revisit

### Limitations
- **Temporal decorrelation:** Vegetation growth changes scattering surface — loss of coherence. C-band worst in forests (weeks); L-band maintains coherence longer (months-years in vegetated areas).
- **Atmospheric artifacts:** Tropospheric water vapor creates apparent deformation signals of ±10–20 mm. Mitigated by time-series analysis and external weather models.
- **Phase ambiguity:** Maximum unambiguous displacement = λ/2 per revisit period. C-band: 2.8 cm between passes. Rapid displacement exceeds this → phase unwrapping failure.
- **Geometric limitations:** Layover and shadow in steep terrain. Slope facing toward satellite is compressed; slope facing away is elongated or invisible.
