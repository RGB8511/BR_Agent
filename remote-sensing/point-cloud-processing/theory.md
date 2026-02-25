# Point Cloud Processing — Filtering, Registration & Analysis

## Data Formats

**LAS/LAZ:** Standard binary format (ASPRS). LAS stores XYZ, intensity, return info, classification, GPS time, color. LAZ is compressed LAS (~5–10× smaller). Universal for airborne and terrestrial LiDAR.

**E57:** ASTM standard for 3D imaging data. Supports structured scans, panoramic images, and point clouds. XML header + binary data. Preferred for TLS data exchange between platforms (Leica, FARO, Trimble).

**PLY/OBJ:** Mesh and point cloud formats common in computer graphics. PLY supports per-vertex attributes (color, normals). OBJ supports meshes with texture.

**COPC:** Cloud-Optimized Point Cloud — LAZ with spatial indexing for HTTP range requests. Enables streaming visualization of massive datasets without local download.

**PCD:** Point Cloud Data format from PCL (Point Cloud Library). Common in robotics and open-source processing.

## Registration (Alignment)

### Target-Based Registration
Place physical targets (spheres, checkerboards, tilt-and-turn targets) visible from multiple scan positions. Software automatically detects targets and computes rigid transformation. Accuracy: sub-mm with well-distributed targets.

### Cloud-to-Cloud Registration (ICP)
Iterative Closest Point aligns two point clouds without targets. Iterates: find closest point pairs → compute optimal transformation → apply → repeat until convergence. Requires reasonable initial alignment (~10% overlap minimum).

**Variants:** Point-to-plane ICP (faster convergence on planar surfaces), Generalized ICP (G-ICP), Normal Distributions Transform (NDT). RANSAC preprocessing removes outlier correspondences.

### SLAM-Based Registration
Simultaneous Localization and Mapping — real-time registration for mobile scanning (backpack, UAV, vehicle). Combines IMU data with scan matching. Drift accumulates over distance; loop closure corrects.

### Georeferencing
Tying the registered point cloud to a real-world coordinate system. Methods: GNSS-surveyed targets/control points, direct georeferencing (GNSS+IMU on scanner), or registration to existing georeferenced data.

## Filtering and Classification

### Ground Filtering
Separating ground points from above-ground objects (vegetation, structures). Critical for DTM extraction.

**Cloth Simulation Filter (CSF):** Simulates a cloth draped over the inverted point cloud. Cloth resting position approximates ground surface. Two parameters: cloth resolution and classification threshold.

**Progressive Morphological Filter:** Iteratively opens (erodes then dilates) the point cloud with increasing window size to separate ground from non-ground.

**TIN-based refinement:** Builds initial ground surface from seed points (lowest in grid cells), then iteratively adds points within angle/distance thresholds.

### Noise Removal
**Statistical Outlier Removal (SOR):** For each point, compute mean distance to k nearest neighbors. Remove points where distance exceeds mean + n×σ. Typical: k=6–12, n=1.0–2.0.

**Radius Outlier Removal:** Remove points with fewer than n neighbors within radius r. Effective for isolated noise.

### Segmentation
Grouping points into meaningful subsets: planar surfaces, cylindrical features, vegetation clusters, structural elements.

**RANSAC:** Random sample consensus fits geometric primitives (planes, cylinders, spheres) to point subsets. Robust to outliers. Widely used for plane extraction (walls, floors, geological surfaces).

**Region Growing:** Groups neighboring points with similar normals and/or curvature. Good for segmenting smooth surfaces.

**Deep Learning:** PointNet, PointNet++, RandLA-Net for semantic segmentation (classifying each point). Requires training data; increasingly available for infrastructure applications.

## Surface Reconstruction

### Meshing
**Delaunay Triangulation (2.5D):** Projects points to XY, triangulates, lifts to 3D. Fast, preserves all points. Good for terrain (single Z per XY). Fails for overhangs and vertical surfaces.

**Poisson Surface Reconstruction:** Fits a smooth implicit surface to oriented point cloud (requires normals). Produces watertight mesh. Good for smooth objects; can over-smooth sharp features.

**Ball-Pivoting Algorithm:** Rolls a virtual ball over the point cloud; triangle formed when ball contacts three points. Preserves sharp features. Sensitive to point density variations.

### DEM Generation
Rasterize point cloud to regular grid. Methods: lowest point, average, IDW interpolation, TIN interpolation. Resolution should match point density (rule of thumb: cell size ≈ 2–3× average point spacing).

## Normal Estimation
Surface normals at each point — required for many algorithms (Poisson mesh, M3C2, lighting).

**PCA method:** Fit plane to k nearest neighbors using principal component analysis. Normal = eigenvector with smallest eigenvalue. Choice of k controls smoothness: small k → noisy normals; large k → over-smoothed.

**Normal orientation:** PCA gives normal direction but not sign (inward vs. outward). Orient consistently using viewpoint (scanner position), minimum spanning tree, or propagation from seed points.
