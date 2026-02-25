# Bathymetric LiDAR — Topographic-Bathymetric Surveying

## Overview

Bathymetric LiDAR uses green-wavelength (532 nm) laser pulses that penetrate the water surface to measure both above-water topography and shallow submerged bathymetry in a single survey. The system simultaneously fires a near-infrared (NIR, 1064 nm) pulse for the water surface and topography, and a green (532 nm) pulse that penetrates water to reflect off the bottom.

**Key capability:** Seamless topo-bathy data collection across the land-water interface — critical for dam sites, reservoirs, river channels, coastal structures, and levee systems where the transition zone is important and difficult to survey by other means.

## Physical Principles

### Dual-Wavelength Operation
- **NIR (1064 nm):** Reflected at the water surface (water absorbs NIR strongly). Also measures dry-land topography. Standard LiDAR wavelength.
- **Green (532 nm):** Partially reflected at the water surface, partially penetrates. Reflects off the submerged bottom (sediment, rock, concrete). Travel time difference between surface and bottom returns gives water depth.

### Depth Calculation
Depth = (Δt × c_water) / 2

where Δt = time difference between surface and bottom returns, c_water = speed of light in water (≈ 0.225 m/ns vs 0.300 m/ns in air). Refraction at the air-water interface corrected using Snell's law.

### Depth Penetration
Maximum depth depends on water clarity (Secchi depth / diffuse attenuation coefficient Kd):
- Very clear water (Kd < 0.1/m): up to 50–70 m (tropical ocean, clear reservoirs)
- Clear water (Kd 0.1–0.3/m): 15–30 m (clear rivers, mountain lakes)
- Moderate clarity (Kd 0.3–1.0/m): 5–15 m (typical rivers, turbid lakes)
- Turbid water (Kd > 1.0/m): < 5 m (sediment-laden rivers, very productive lakes)
- Very turbid: 0–2 m or no penetration

**Rule of thumb:** Maximum depth ≈ 2–3 × Secchi depth.

### Bottom Reflectance
The bottom must provide sufficient return signal. Sand and light rock: good reflectance. Dark mud, organic material, dense vegetation: poor reflectance and may limit depth even in clear water.

## Systems and Platforms

### Airborne Systems
- **Leica Chiroptera / HawkEye:** Combined topo-bathy; up to 50 m depth in clear water
- **RIEGL VQ-880-G:** Topo-bathy scanner; high pulse rate
- **Optech CZMIL / Teledyne:** Large-area coastal and shallow-water systems
- **Typical specifications:** 500 kHz+ pulse rate, 1–4 pts/m² bathy density, 10–50+ pts/m² topo density, swath width 200–500 m from 300–600 m altitude

### UAS-Based
Emerging systems with green-wavelength LiDAR on UAS platforms. Limited to shallow depths (< 10 m) due to lower power and altitude constraints. Useful for river surveys, small reservoir bathymetry, and dam tailwater surveys.

## Applications for Water Infrastructure

### Reservoir Sedimentation Surveys
Repeat bathymetric LiDAR surveys quantify sediment accumulation in reservoirs. Compare current bathymetry to original (design) or previous survey to compute storage loss. Faster and more complete coverage than traditional boat-based hydrographic surveys.

### Dam and Spillway Surveys
Topo-bathy provides seamless surveying of: dam crest → upstream face → reservoir bottom → downstream face → tailwater → channel. Critical for dam safety: scour holes below stilling basins, erosion of channel downstream, tailwater rating curves.

### River Channel Surveys
Floodplain topography + channel bathymetry in one dataset. Input for hydraulic modeling (HEC-RAS, SRH-2D), bridge scour assessment, flood mapping, and habitat assessment.

### Coastal and Levee Surveys
Nearshore bathymetry + beach/dune topography + levee crest elevations. Seamless data for coastal flood modeling and levee certification.

## Data Processing

### Waveform Processing
Full-waveform bathymetric LiDAR records the complete return signal shape. Processing extracts the surface return, water column scattering, and bottom return. Bottom return may be weak in turbid water or deep — waveform processing improves detection over discrete-return systems.

### Refraction Correction
Raw green-wavelength ranges must be corrected for:
1. Change in speed of light at air-water interface
2. Refraction angle (Snell's law) changing the apparent bottom position
3. Dynamic water surface (waves, ripples) affecting instantaneous refraction geometry

### Point Classification
- Class 2: Ground (dry land)
- Class 9: Water surface (from NIR returns)
- Class 40: Bathymetric bottom
- Class 41: Water surface (from green returns)
- Class 45: Water column (noise/scatter)

### Integration with Multibeam
For deep water beyond bathymetric LiDAR penetration, acoustic multibeam echo sounder (MBES) data fills the gap. Data fusion at the overlap zone requires careful datum alignment and quality control.
