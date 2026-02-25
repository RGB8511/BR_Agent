# Slope Stability & Mass Movement Monitoring Using Remote Sensing

## Overview

Remote sensing enables spatially comprehensive slope monitoring that transforms landslide hazard assessment from discrete-point measurement to full-field displacement mapping. Technologies include InSAR (satellite and ground-based), LiDAR (terrestrial and UAS), UAS photogrammetry, and multi-temporal satellite imagery. These methods detect pre-failure deformation, characterize slope geometry and geology, monitor active landslides, and support early warning systems.

## Landslide Detection and Inventory

### Regional Screening with InSAR
Satellite InSAR time-series analysis (PS-InSAR, SBAS) identifies active slope movement across entire regions at mm/year precision. Screening methodology:
1. Process multi-year SAR image stack (Sentinel-1: free, 6-day revisit, C-band)
2. Generate mean velocity map
3. Identify zones exceeding threshold velocity (e.g., > 5 mm/yr LOS)
4. Cross-reference with geological and topographic context
5. Prioritize for detailed investigation

### Landslide Inventory from LiDAR
Bare-earth LiDAR DEMs reveal morphological signatures of landslides even under forest canopy: head scarps, lateral flanks, hummocky terrain, displaced blocks, and toe bulges. LiDAR-based inventories routinely identify 5–20× more landslides than aerial photo interpretation in forested terrain.

**Key morphometric indicators:** Concave head region, convex toe, internal hummocks, disrupted drainage, tilted trees (visible in point cloud), scarps parallel to contours.

### Multi-Temporal Satellite Imagery
Optical satellite archives (Landsat: 1972–present, Sentinel-2: 2015–present) enable retrospective landslide detection from spectral and morphological changes. Change detection of bare-earth exposure (landslide scars) in otherwise vegetated terrain.

## Pre-Failure Detection and Early Warning

### Displacement Acceleration
Landslides typically exhibit three phases before failure (Saito, 1965):
1. **Primary creep:** Decreasing strain rate (may last years)
2. **Secondary creep:** Constant strain rate
3. **Tertiary creep:** Accelerating strain rate → failure

Remote sensing detects the transition from secondary to tertiary creep — the critical warning phase. Time-series analysis of InSAR or repeated LiDAR surveys reveals acceleration patterns.

### Inverse Velocity Method
Plot inverse of displacement velocity vs. time. Linear decrease in 1/v predicts failure time (where 1/v → 0). Requires minimum 3 measurement epochs showing acceleration. Applied to InSAR, GB-InSAR, TLS, and UAS data.

**Caution:** Not all slopes fail in this pattern. Rainfall-triggered failures may accelerate rapidly. Strain-softening materials (brittle rock) may show less warning than ductile (clay/debris).

### GB-InSAR for Critical Slopes
Ground-based radar provides sub-mm displacement maps every 2–5 minutes. Enables real-time early warning for:
- Open-pit mine slopes
- Rock slopes above infrastructure (highways, railways, towns)
- Dam abutments
- Slopes during construction (excavation, blasting)

**Alert threshold framework:**
- Attention: velocity > background + 2σ
- Pre-alert: acceleration detected (d²u/dt² > 0 sustained)
- Alert: inverse velocity trending toward zero, or absolute velocity exceeds critical threshold
- Alarm: failure imminent based on inverse velocity extrapolation

## Slope Characterization

### High-Resolution DEM Analysis
LiDAR or UAS-derived DEMs enable:
- **Slope angle mapping:** Pixel-by-pixel slope calculation; identify zones exceeding friction angle
- **Aspect analysis:** Identify structurally controlled failure directions
- **Curvature analysis:** Profile curvature (convex head scarp, concave toe) delineates landslide boundaries
- **Drainage analysis:** Flow accumulation, contributing area, topographic wetness index (TWI) identify zones of elevated pore pressure
- **Cross-section extraction:** Accurate profiles for limit-equilibrium stability analysis

### Discontinuity Mapping from Point Clouds
LiDAR and photogrammetric point clouds of rock slopes enable automated fracture mapping (see fracture-mapping-remote package). Combined with slope geometry, supports kinematic analysis (planar, wedge, toppling failure modes).

## Rockfall Hazard Assessment

### Rockfall Source Identification
High-resolution point clouds identify potential rockfall source zones: overhanging blocks, open fractures, differentially weathered zones, previous detachment scars.

### Trajectory Modeling
LiDAR-derived DEMs provide accurate slope geometry for rockfall simulation (RocFall, RAMMS::Rockfall, Trajecto). Critical parameters: slope angle, surface roughness (from point cloud analysis), restitution coefficients by surface type.

### Rockfall Event Detection
Multi-temporal TLS comparison (M3C2) detects individual rockfall events — source zone, volume, and runout. Automated change detection systems can operate continuously with permanent TLS installations.

## Debris Flow and Rapid Landslide Assessment

### Pre-Event Terrain Analysis
LiDAR DEMs identify debris flow hazards: steep channels, previous debris fan deposits, potential dam-break flood paths, and material source zones.

### Post-Event Mapping
UAS rapid deployment for emergency mapping:
- Source area delineation and volume estimation
- Runout distance and deposit extent
- Damage assessment
- Identification of secondary hazards (landslide dams, unstable deposits)
- Input to numerical back-analysis models

## Monitoring System Design

### Multi-Scale Approach
Effective slope monitoring combines multiple scales:
1. **Regional (satellite InSAR):** Identify active slopes across project area
2. **Site-scale (UAS/airborne LiDAR):** Characterize geometry and geology of identified slopes
3. **Structure-scale (TLS/GB-InSAR):** Detailed monitoring of critical slopes
4. **Point-scale (in-situ instruments):** Piezometers, inclinometers for subsurface data

### Integration with Geotechnical Assessment
Remote sensing provides surface displacement and geometry. Combine with:
- Subsurface data (borings, CPT, geophysics) for geological model
- Pore pressure data (piezometers) for effective stress analysis
- Laboratory strength data for stability analysis
- Numerical modeling (FEM, DEM) calibrated to observed displacements
