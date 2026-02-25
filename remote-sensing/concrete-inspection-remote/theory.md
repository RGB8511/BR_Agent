# Remote Concrete Inspection — Crack Detection, Spalling & Condition Assessment

## Overview

Traditional concrete inspection requires close physical access — scaffolding, snooper trucks, rappelling, or dewatering. Remote sensing technologies (UAS imagery, thermal IR, LiDAR, and ground-penetrating radar) enable safer, faster, and more comprehensive inspection of concrete structures including dams, bridges, tunnels, spillways, retaining walls, and buildings.

**Key distinction from field geophysics packages:** This package covers above-surface, non-contact methods for assessing visible and near-surface concrete condition, not subsurface investigation.

## Visual Inspection by UAS

### High-Resolution Imagery

UAS equipped with high-resolution cameras (≥ 20 MP, preferably 45–61 MP full-frame) capture overlapping photographs of concrete surfaces from controlled distances.

**Critical parameter — Ground Sample Distance (GSD):**
- GSD < 0.5 mm/pixel: Required for reliable crack detection at 0.2 mm width
- GSD < 1.0 mm/pixel: Detects cracks ≥ 0.3 mm; suitable for structural assessment
- GSD < 3.0 mm/pixel: Detects large cracks (≥ 1 mm), spalling, staining; reconnaissance level

**Practical limitations:** GSD is controlled by sensor pixel size, focal length, and standoff distance. Achieving 0.5 mm GSD with a 24 MP sensor (6 μm pixel) requires a 50 mm lens at ~4 m standoff. Close approaches to structures require skilled pilots and obstacle avoidance.

### Orthomosaic and 3D Mesh Generation

Overlapping images (≥ 70% forward, ≥ 60% side overlap) processed through Structure-from-Motion (SfM) photogrammetry produce:
- **Orthomosaic:** Geometrically corrected image mosaic for crack mapping and measurement
- **Dense point cloud / 3D mesh:** For surface geometry, spalling depth measurement, deformation analysis
- **Digital Surface Model (DSM):** For volumetric analysis of spalling, erosion, or deterioration

## Crack Detection and Measurement

### Manual Crack Mapping on Orthomosaics

Cracks digitized manually in GIS or CAD from orthomosaics. Crack width measured from calibrated imagery. Advantages: human judgment on crack type, pattern, and significance. Disadvantages: time-consuming for large surfaces.

### Automated Crack Detection

**Traditional image processing:**
- Edge detection (Canny, Sobel) on grayscale images
- Thresholding (Otsu's method) after preprocessing (histogram equalization, filtering)
- Morphological operations (erosion/dilation) to clean detections
- Skeletonization for crack centerline extraction
- Limitations: sensitive to lighting, texture, staining; high false-positive rates

**Deep learning methods (current state of practice):**
- **Semantic segmentation** (U-Net, DeepLabV3+, SegNet): pixel-wise classification of crack vs. non-crack
- **Object detection** (YOLO, Faster R-CNN): bounding box detection of crack regions
- **Instance segmentation** (Mask R-CNN): individual crack identification and masking
- Training data: thousands of annotated crack images; transfer learning from pre-trained models
- Performance: precision/recall > 90% achievable on well-trained models for specific structure types
- Limitations: domain shift (model trained on bridges may not perform on dams); need retraining for new environments

### Crack Width Measurement from Images

Crack width measured by:
1. Calibrated orthomosaic: measure pixel width × GSD at crack location
2. Sub-pixel techniques: fit brightness profile across crack to estimate true width below GSD
3. Photogrammetric depth: crack depth estimated from parallax in overlapping images (limited to wide cracks)

**Accuracy:** Minimum measurable crack width ≈ 2–3 × GSD for reliable detection; ≈ 1 × GSD with sub-pixel techniques and good contrast. At 0.5 mm/pixel GSD, cracks ≥ 0.3 mm detectable, ≥ 0.5 mm measurable.

## Thermal Infrared (IR) Inspection

### Delamination Detection

Subsurface delaminations (separations between concrete layers, typically caused by rebar corrosion expansion) trap air, creating thermal anomalies. During solar heating, delaminated areas warm faster and appear warmer than sound concrete. During cooling, they cool faster and appear cooler.

**Best conditions for thermal IR delamination detection:**
- Clear sky, minimal wind (< 15 km/h)
- 4–6 hours after sunrise (heating phase) or 2–4 hours after sunset (cooling phase)
- Dry surface (moisture masks thermal contrasts)
- Minimum temperature differential: ≥ 0.5°C between delaminated and sound concrete

**Camera requirements:** LWIR (8–14 μm) thermal camera with ≥ 0.05°C NETD (thermal sensitivity). Resolution: ≥ 320×240 for reconnaissance; ≥ 640×512 for quantitative assessment.

### Moisture and Seepage Detection

Active moisture on concrete surfaces produces evaporative cooling visible in thermal imagery. Wet zones appear cooler than surrounding dry concrete. Applications: seepage through dam faces, leaking joints, active cracks with water flow.

## Ground-Penetrating Radar (GPR) for Concrete

### Rebar Detection and Cover Depth

GPR with high-frequency antennas (1.6–2.6 GHz) images rebar hyperbolas in concrete. Rebar depth = two-way travel time × velocity / 2. Concrete velocity varies (0.09–0.12 m/ns depending on moisture and mix).

### Delamination and Void Detection

Delaminations and voids produce reflections at impedance boundaries within the concrete section. Depth accuracy ±5–10 mm in good conditions.

### Concrete Thickness

GPR measures slab or wall thickness when there is a contrast at the back face (concrete/soil, concrete/air).

**Limitation of GPR vs. thermal IR:** GPR requires contact or near-contact and is slow for large surfaces. Thermal IR is non-contact and covers large areas rapidly but cannot determine delamination depth.

## Condition Rating Systems

### ACI 201.1R Visual Inspection Categories
- **Cracking:** pattern cracking (map/alligator), linear cracking (structural, shrinkage), D-cracking (freeze-thaw)
- **Scaling:** loss of surface morite; severity by depth of loss
- **Spalling:** fragmentation of concrete surface or edges; shallow (< 25 mm) or deep (> 25 mm)
- **Efflorescence:** white deposits from calcium carbonate leaching; indicates water movement through concrete
- **Staining:** rust (rebar corrosion), algae/biological, mineral deposits
- **Joint deterioration:** sealant failure, compression seal displacement, filler board exposure
- **Erosion/abrasion:** surface loss from flowing water, sediment, or traffic

### Dam Condition Assessment (FEMA / USACE)
Condition ratings typically on 1–5 or A–F scale for each structural element. Systematic photo documentation with GPS location. Remote sensing provides baseline and change-detection capability between inspections.
