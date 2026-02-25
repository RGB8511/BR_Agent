# Standards Reference — Change Detection & Volumetric Analysis

## Wheaton et al. (2010) — Accounting for Uncertainty in DEMs from Repeat Topographic Surveys: Improved Sediment Budgets
**Scope:** Foundational methodology for DEM of Difference (DoD) analysis with spatially variable uncertainty propagation. Introduces minimum level of detection (minLOD), probabilistic thresholding, and volumetric uncertainty estimation. Implemented in the GCD (Geomorphic Change Detection) software. Essential reference for any DoD-based change analysis.

## Lague et al. (2013) — Accurate 3D Comparison of Complex Topography with Terrestrial Laser Scanner: Application to the Rangitikei Canyon (NZ)
**Scope:** Introduces the M3C2 algorithm for point cloud change detection. Defines normal-direction signed distance, statistical confidence intervals per point, and spatially variable level of detection. Implemented in CloudCompare. The standard reference for 3D point cloud differencing.

## ASPRS Positional Accuracy Standards for Digital Geospatial Data (2023)
**Scope:** American Society for Photogrammetry and Remote Sensing standards for positional accuracy of geospatial products including DEMs, orthoimages, and point clouds. Defines accuracy classes (horizontal and vertical), checkpoint requirements, and reporting methodology. Essential for specifying survey accuracy requirements for change detection projects.

## USACE EM 1110-1-1005 — Control and Topographic Surveying
**Scope:** US Army Corps of Engineers engineering manual for survey control and topographic mapping. Accuracy standards, control networks, GPS survey procedures, and quality assurance for engineering surveys. Relevant for establishing the control framework supporting repeat surveys.

## ISRM (International Society for Rock Mechanics) — Suggested Methods for Rock Mass Characterization Using Remote Sensing
**Scope:** ISRM commission guidance on using LiDAR and photogrammetry for rock mass characterization including change detection on rock slopes. Covers discontinuity mapping, rockfall detection, and progressive failure monitoring from point cloud comparisons.

## James & Robson (2014) — Mitigating Systematic Error in Topographic Models Derived from UAV and Ground-Based Image Networks
**Scope:** Identifies and addresses systematic "doming" errors in SfM-derived DEMs that contaminate change detection. Self-calibrating bundle adjustment, oblique image inclusion, and GCP distribution requirements. Critical reference for UAS-based change detection accuracy.
