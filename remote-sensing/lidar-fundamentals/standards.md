# Standards Reference — LiDAR Fundamentals

## ASPRS LAS Specification (v1.4 R15)
**Scope:** American Society for Photogrammetry and Remote Sensing standard file format for LiDAR point cloud data. Defines binary file structure, point record formats (0–10), classification codes, coordinate reference system metadata, and extra bytes records. The universal exchange format for LiDAR data.

## USGS Lidar Base Specification (v2.1, 2023)
**Scope:** Minimum requirements for USGS-contracted LiDAR data collection and processing. Quality levels (QL0–QL2), point density, accuracy, classification requirements, deliverables (classified LAS, bare-earth DEM, breaklines, metadata). Widely adopted as the de facto standard for government LiDAR projects in the US.

## ASPRS Positional Accuracy Standards for Digital Geospatial Data (2023)
**Scope:** Framework for specifying and reporting positional accuracy of geospatial data including LiDAR. Defines RMSE, NVA (Non-Vegetated Vertical Accuracy), VVA (Vegetated Vertical Accuracy), and horizontal accuracy classes. Replaces legacy NSSDA for LiDAR accuracy reporting.

## IEC 60825-1 — Safety of Laser Products
**Scope:** International standard for laser safety classification (Class 1 through Class 4). Defines Maximum Permissible Exposure (MPE) limits by wavelength and exposure duration. All LiDAR systems must be classified per this standard. Most modern survey-grade TLS systems are Class 1 (eye-safe) at 1550 nm.

## ISO 17123-9 — Optics and Optical Instruments — Field Procedures for Testing Geodetic and Surveying Instruments — Part 9: Terrestrial Laser Scanners
**Scope:** Standardized field test procedures for evaluating TLS performance (range accuracy, angular accuracy, 3D point accuracy). Defines simplified and full test procedures. Used for instrument verification and comparison.

## E57 File Format (ASTM E2807)
**Scope:** ASTM standard for 3D point cloud data exchange. Supports XYZ coordinates, intensity, color, normals, images, and metadata. XML-based header with binary data blocks. More flexible than LAS for TLS data (structured scans, panoramic images). Widely supported by CloudCompare, Cyclone, RealWorks.

## OGC CDB / 3D Tiles / LAS Optimized (COPC)
**Scope:** Emerging standards for cloud-native point cloud storage and streaming. COPC (Cloud-Optimized Point Cloud) is a LAZ-based format organized for HTTP range requests. Enables efficient access to massive datasets without downloading entire files. Increasingly adopted for web-based point cloud visualization.
