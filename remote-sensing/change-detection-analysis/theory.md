# Change Detection & Volumetric Analysis

## Overview

Change detection compares multi-temporal geospatial datasets — point clouds, DEMs, orthoimagery, or raster surfaces — to quantify spatial and volumetric differences over time. In geotechnical and infrastructure engineering, this enables measurement of erosion, deposition, settlement, landslide displacement, stockpile volumes, excavation progress, and structural deformation without physical contact.

## Point Cloud Differencing (C2C and M3C2)

### Cloud-to-Cloud (C2C) Distance
Simplest approach: for each point in the reference cloud, find the nearest point in the comparison cloud. The Euclidean distance between matched points represents the change magnitude.

**Limitations:** Sensitive to point density variations, noise, and registration errors. Reports only unsigned distance (cannot distinguish erosion from deposition along complex surfaces). Best for quick screening.

### Multiscale Model-to-Model Cloud Comparison (M3C2)
Advanced algorithm (Lague et al., 2013) that computes distances along the local surface normal direction:
1. Estimates normal orientation at each core point using a neighborhood of radius D
2. Projects both clouds along the normal within a cylindrical search zone (radius d/2)
3. Computes signed distance between the two projected point distributions
4. Estimates confidence interval based on point density, roughness, and registration error

**Advantages over C2C:** Provides signed distance (positive = accretion/heave, negative = erosion/settlement), statistically robust uncertainty estimation, handles variable point density, works on rough surfaces.

**Level of Detection (LOD):** Minimum detectable change based on:
LOD_95% = ±1.96 × √(σ_reg² + σ₁²/n₁ + σ₂²/n₂)

where σ_reg = registration error, σ₁,₂ = surface roughness in each epoch, n₁,₂ = number of points in projection cylinder.

## DEM of Difference (DoD)

### Method
Subtract two co-registered Digital Elevation Models: DoD = DEM₂ - DEM₁. Each cell in the output raster contains the elevation change. Volume change = Σ(ΔZ × cell area) over the region of interest.

### Uncertainty Propagation
Each DEM has spatially variable uncertainty. The DoD uncertainty:
σ_DoD = √(σ_DEM1² + σ_DEM2²)

Only changes exceeding a threshold (typically LOD_95% = 1.96 × σ_DoD) are considered significant. Changes below this threshold may be real but are statistically indistinguishable from noise.

### Thresholding Approaches
- **Uniform threshold:** Single LOD value applied everywhere. Simple but ignores spatial variation in data quality.
- **Spatially variable threshold:** LOD varies cell-by-cell based on local point density, slope, roughness, and GPS accuracy. More accurate volumetric estimates.
- **Probabilistic thresholding:** Bayesian approach assigns probability of change being real for each cell, weighted by uncertainty. Integrates over all cells for best volume estimate.

## Volumetric Analysis

### Cut/Fill Volume Calculation
From DoD raster:
- **Cut volume** (material removed) = Σ(|ΔZ| × cell area) where ΔZ < 0
- **Fill volume** (material added) = Σ(ΔZ × cell area) where ΔZ > 0
- **Net volume** = Fill - Cut

### Stockpile Volume
Compute volume above a reference base plane (ground surface before stockpile placement):
V = Σ(Z_surface - Z_base) × cell area  for all cells where Z_surface > Z_base

**Accuracy considerations:** Base plane definition is critical. Methods: flat plane at toe elevation, TIN connecting toe points, pre-stockpile DEM if available. Vertical accuracy of LiDAR/photogrammetry (typically 2–10 cm) propagates directly to volume uncertainty.

### Reservoir/Pond Volume
Integrate elevation-area curve from DEM below a specified water surface elevation:
V = ∫₀ᴴ A(h) dh  (trapezoidal or Simpson's rule on area-elevation table)

## Displacement Vector Analysis

### 3D Displacement from Repeat Point Clouds
For surfaces with identifiable features (rock blocks, structures, texture), image correlation or point cloud registration can recover full 3D displacement vectors:

**Methods:**
- **ICP variants (Iterative Closest Point):** Align point cloud subsets; rigid body transformation = translation + rotation of that zone
- **Feature tracking:** Match identifiable objects (blocks, corners, texture patches) between epochs
- **Particle Image Velocimetry (PIV) adapted:** 2D correlation on orthoimages for horizontal displacement field

### Strain Analysis from Displacement Fields
Once displacement vectors are determined across a surface:
- **Strain tensor:** ε_ij = 0.5 × (∂u_i/∂x_j + ∂u_j/∂x_i) computed from spatial derivatives of displacement
- **Maximum shear strain:** Identifies zones of concentrated deformation (failure planes, shear zones)
- **Dilation/compression:** Volumetric strain indicates zones of expansion or contraction

## Applications

### Landslide Monitoring
Multi-epoch LiDAR or UAS photogrammetry captures progressive slope displacement. DoD maps identify active zones, head scarps, accumulation zones, and rate of movement. Repeat intervals: days (active crisis) to years (long-term monitoring).

### Erosion/Scour Measurement
River bank erosion, coastal cliff retreat, dam spillway erosion, bridge pier scour. Sub-decimeter accuracy enables quantification of erosion rates and scour depth that complement traditional cross-section surveys.

### Excavation Progress
Compare as-built excavation surface (daily UAS or terrestrial LiDAR survey) to design surface. Compute remaining cut volume, identify over/under-excavation, and track daily production rates.

### Settlement Monitoring
Repeat surveys of embankments, foundations, or fills. Requires high accuracy (<5 mm) and careful control/registration. Best achieved with terrestrial LiDAR or high-density UAS photogrammetry with precise ground control.

### Structural Change
Building facades, retaining walls, tunnel linings — compare to as-built or previous epoch to detect bulging, cracking displacement, settlement, or tilt.
