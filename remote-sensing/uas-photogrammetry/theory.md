# UAS Photogrammetry — Structure from Motion & Dense Matching

## Principles

UAS (Uncrewed Aerial System) photogrammetry reconstructs 3D geometry from overlapping 2D images using Structure from Motion (SfM) and Multi-View Stereo (MVS) algorithms. The workflow: capture overlapping images → detect feature points (SIFT/ORB) → match features between images → estimate camera positions via bundle adjustment → generate dense point cloud via MVS → mesh/DEM/orthomosaic.

### Ground Sample Distance (GSD)
GSD is the ground dimension represented by one pixel — the fundamental resolution metric:

GSD = (H × pixel_size) / focal_length

Lower GSD = higher resolution = lower flying height or longer focal length. Typical: 1–5 cm/px for engineering surveys; 0.5–1 cm/px for structural inspection.

### Overlap Requirements
- **Forward (endlap):** 75–85% minimum for SfM. 80% standard.
- **Side (sidelap):** 65–75% minimum. 70% standard.
- **Structural inspection / vertical faces:** 80%+ in all directions; oblique and convergent image geometry.

Higher overlap improves reconstruction completeness, reduces holes, and strengthens bundle adjustment. For challenging scenes (vegetation, water, uniform surfaces), increase to 85%+ endlap and 75%+ sidelap.

### Ground Control Points (GCPs)
GCPs are surveyed targets visible in imagery that constrain the photogrammetric solution to real-world coordinates. Without GCPs or RTK/PPK GNSS on the UAS, absolute accuracy is poor (meters).

**With GCPs:** 5–10 well-distributed GCPs for a typical site. Accuracy: 1–3× GSD achievable (e.g., 2 cm with 1 cm GSD). GCPs should not be collinear; distribute around perimeter and interior.

**With RTK/PPK GNSS:** Direct georeferencing from centimeter-level camera positions. Can achieve 2–5 cm accuracy without GCPs; GCPs still recommended as checkpoints for QA.

### Camera Calibration
Lens distortion parameters (radial k1/k2/k3, tangential p1/p2, principal point cx/cy, focal length f) are estimated during bundle adjustment (self-calibration) or from pre-calibration. Quality of self-calibration depends on image geometry — convergent images and varying distances improve calibration.

## Processing Workflow

1. **Image import and quality check:** Review for blur, exposure, coverage gaps
2. **Feature detection and matching:** SIFT/SURF/ORB algorithms identify and match keypoints across images
3. **Sparse point cloud / bundle adjustment:** Simultaneously solves camera positions and 3D point positions. With GCPs: constrained bundle adjustment.
4. **Dense matching (MVS):** Pixel-by-pixel matching produces dense point cloud (100–1000× more points than sparse). SGM, PMVS, or proprietary algorithms.
5. **Point cloud filtering:** Remove noise, outliers, vegetation (if bare-earth needed)
6. **Mesh generation:** Triangulated surface from point cloud (Delaunay, Poisson reconstruction)
7. **DEM/DSM extraction:** Rasterized elevation model from mesh or point cloud
8. **Orthomosaic:** Orthorectified mosaic of all images projected onto DEM — geometrically correct image map

## Accuracy Factors

**Systematic:** Camera calibration quality, GCP accuracy, GNSS accuracy, datum/projection errors.
**Random:** Image quality (blur, noise), texture/contrast, overlap adequacy, GSD, reconstruction algorithm.
**Environmental:** Vegetation movement, water/reflective surfaces, deep shadows, snow/uniform surfaces, thermal shimmer.

**Typical achievable accuracy:**
- Horizontal: 1–2× GSD (with GCPs or RTK)
- Vertical: 1.5–3× GSD (with GCPs or RTK)
- Volume accuracy: depends on surface area and point density; typically ±5–10% for stockpiles

## Flight Planning

**Key parameters:** GSD target, camera specs (sensor size, focal length, resolution), overlap, flying height, speed, wind conditions, airspace restrictions.

**Nadir flights:** Standard for topographic mapping. Grid pattern with parallel flight lines.
**Oblique flights:** 30–45° off-nadir for 3D structure capture. Cross-hatch or orbital patterns for structures.
**Terrain-following:** Maintains constant AGL in hilly terrain for uniform GSD.

## Software Ecosystem

**Processing:** Agisoft Metashape, Pix4Dmapper, DroneDeploy, OpenDroneMap, RealityCapture, ContextCapture.
**Flight planning:** DJI Pilot/FlightHub, Pix4Dcapture, Litchi, UgCS, DroneDeploy.
**Analysis:** CloudCompare, QGIS, ArcGIS, Global Mapper.
