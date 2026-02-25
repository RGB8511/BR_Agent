# Remote Fracture & Discontinuity Mapping from Point Clouds and Imagery

## Overview

Traditional discontinuity mapping (scanline, window mapping) requires direct physical access to rock faces, is time-consuming, exposes personnel to hazards (rockfall, unstable slopes), and is limited to accessible portions of the face. Remote sensing methods — primarily terrestrial LiDAR (TLS) and UAS photogrammetry — overcome these limitations by capturing dense 3D point clouds of entire rock faces from safe standoff distances.

**Key capability:** Extracting discontinuity orientation (dip/dip direction), spacing, persistence, roughness, and set identification from point cloud data, producing results equivalent to or exceeding traditional scanline surveys in quantity and spatial coverage.

## Principles of Discontinuity Extraction

### From Point Clouds to Planes

Rock face discontinuities (joints, faults, bedding, foliation) are locally planar surfaces. In a point cloud, a discontinuity surface appears as a cluster of points that can be fit with a mathematical plane. The orientation of that plane (normal vector) gives the dip and dip direction.

**Workflow:**
1. Acquire point cloud (TLS or UAS-SfM) with sufficient density and accuracy
2. Compute surface normals at each point (using k-nearest neighbors or radius search)
3. Segment the point cloud into planar facets (clusters of similarly-oriented points)
4. Fit planes to each facet; extract orientation (dip/dip direction)
5. Plot orientations on stereonet; identify joint sets
6. Extract spacing, persistence, and other parameters

### Normal Vector Computation

For each point, the local surface normal is estimated by fitting a plane to the k nearest neighbors (typically k = 10–30) or all points within a search radius. The eigenvalues of the covariance matrix of the neighborhood determine the normal direction and the planarity/linearity/scattering of the local surface.

**Planarity index:** P = (λ₂ - λ₃) / λ₁ where λ₁ ≥ λ₂ ≥ λ₃ are eigenvalues. High planarity (P → 1) indicates a well-defined planar surface (discontinuity). Low planarity indicates rough, curved, or noisy surfaces.

### Segmentation Algorithms

**Region growing:** Start from a seed point, iteratively add neighboring points whose normals are within a threshold angle. Simple, effective for well-exposed planar surfaces. Parameters: angle threshold (typically 10–30°), minimum cluster size.

**RANSAC (Random Sample Consensus):** Randomly selects 3 points, fits a plane, counts inliers within a distance threshold. Repeated many times; best plane accepted. Robust to noise and outliers. Used iteratively to extract multiple planes.

**Facets plugin (CloudCompare):** Combines kd-tree subdivision with planarity filtering and region merging. Produces planar facets with dip/dip direction exported directly.

**DSE (Discontinuity Set Extractor):** Riquelme et al. (2014) algorithm specifically designed for geotechnical discontinuity analysis. Uses kernel density estimation on normal vectors to identify clusters (joint sets) automatically, then assigns each facet to a set.

## Orientation Bias and Corrections

### Orientation Bias (Terzaghi Correction)

Point cloud surveys, like scanline surveys, are subject to orientation bias: discontinuities nearly parallel to the scanning direction (or rock face) are undersampled because they produce few visible traces. Discontinuities perpendicular to the line of sight are oversampled.

The Terzaghi correction factor for a discontinuity with normal **n** relative to the sampling direction (line of sight or face normal) **s**:

w = 1 / cos(δ)  (where δ = angle between discontinuity normal and sampling direction)

Weight is capped at a maximum (typically 1/cos(20°) ≈ 1.06 to avoid infinite weights for near-parallel discontinuities). Discontinuities with δ > 70–80° (nearly parallel to the face) cannot be reliably detected — this is a blind zone that requires scanning from multiple orientations or supplementary methods.

### Multi-View Scanning

Best practice: scan each rock face from at least 2–3 different orientations (separated by ≥ 30°) to minimize orientation bias. Point clouds are registered together before analysis. This is a major advantage of TLS and UAS over single-direction scanline surveys.

## Spacing and Persistence

### Spacing from Point Clouds

Once joint sets are identified, spacing is measured along a virtual scanline perpendicular to the mean set orientation:

1. Define a virtual borehole/scanline direction (perpendicular to the joint set)
2. Project each detected plane onto this line
3. Measure distances between successive plane intercepts

**True spacing** (perpendicular distance between adjacent parallel discontinuities) can be computed directly from the plane equations, eliminating the apparent-vs-true spacing correction needed in traditional scanline mapping.

### Persistence (Trace Length)

Discontinuity persistence = extent of the plane visible in the point cloud or imagery. Measured as the maximum dimension of each segmented facet. Subject to censoring bias: traces may extend beyond the visible face (right-censored) or be partially hidden (truncated).

**Digital trace mapping** on high-resolution orthophotos or textured meshes allows semi-automated trace length measurement with explicit recording of censoring type.

## Roughness from Point Clouds

### JRC from LiDAR Profiles

Joint Roughness Coefficient (JRC) can be estimated from point cloud profiles along discontinuity surfaces:

1. Extract a 2D profile along the discontinuity surface from the point cloud
2. Calculate roughness parameters (Z₂, SF, Rp) from the profile
3. Correlate to JRC using established relationships (Tse & Cruden 1979, Yu & Vayssade 1991)

**Resolution requirement:** Point spacing ≤ 1–5 mm for meaningful roughness measurement. Standard TLS (5–10 mm spacing at typical survey distances) captures large-scale roughness; close-range scanning or photogrammetry needed for small-scale roughness.

### 3D Surface Roughness

Beyond 2D profiles, 3D roughness can be characterized by:
- RMS deviation of points from the best-fit plane
- Fractal dimension of the surface
- Directional roughness (anisotropy) — important for shear strength

## Integration with Geotechnical Analysis

### Kinematic Analysis

Extracted orientations feed directly into kinematic analysis (planar sliding, wedge sliding, toppling) when combined with slope orientation:
- Plot discontinuity sets and slope face on stereonet
- Identify kinematically feasible failure modes
- Use extracted spacing and persistence to assess the size of potential failures

### Rock Mass Classification

Remote mapping provides input for rock mass classification:
- **RQD** from spacing: RQD = 100 × e^(-0.1λ) × (0.1λ + 1) where λ = discontinuity frequency (1/spacing)
- **GSI** from block size and joint condition visible in imagery
- **RMR** discontinuity components (spacing, persistence, roughness, condition)

### Rockfall Source Identification

Overhanging blocks, open joints, and differential weathering identified from point cloud analysis define rockfall source areas for hazard assessment and rockfall modeling (RocFall, RAMMS).
