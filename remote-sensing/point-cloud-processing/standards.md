# Standards Reference — Point Cloud Processing

## ASPRS LAS Specification (v1.4 R15)
**Scope:** Standard binary format for LiDAR data. Point record formats, classification codes, coordinate systems, variable-length records. The universal interchange format.

## ASTM E2807 — Standard Specification for 3D Imaging Data Exchange (E57)
**Scope:** File format for 3D imaging systems (TLS, structured light). XML metadata with binary point data. Supports structured scans, images, and sensor metadata.

## PDAL — Point Data Abstraction Library
**Scope:** Open-source library for point cloud processing pipelines. Readers/writers for all major formats, filters (noise, outlier, ground classification, decimation), and processing stages. JSON-based pipeline definition enables automated, reproducible workflows.

## PCL — Point Cloud Library
**Scope:** Open-source C++ library for point cloud processing. Algorithms for filtering, feature estimation, segmentation, registration, surface reconstruction, and visualization. Academic/research standard; basis for many commercial implementations.

## CloudCompare Documentation
**Scope:** Open-source 3D point cloud processing software. Key algorithms: ICP registration, C2C/C2M distance, M3C2 plugin, RANSAC shape detection, CSF ground filter, qFacets (discontinuity detection), volume calculation, cross-sections. The primary free tool for geotechnical point cloud analysis.

## Lague et al. (2013) — M3C2 Algorithm
**Scope:** Multiscale Model-to-Model Cloud Comparison. Published in Journal of Geophysical Research. Defines the M3C2 distance computation with per-point confidence intervals. The standard algorithm for detecting statistically significant surface change from repeat point cloud surveys.
