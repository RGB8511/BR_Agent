# Seepage & Thermal Anomaly Detection

## Overview

Seepage through earth dams, levees, concrete structures, and pipelines produces thermal signatures detectable by infrared sensors. Groundwater (and seepage water) maintains relatively constant temperature year-round, while surface temperatures vary seasonally and diurnally. This temperature contrast creates thermal anomalies at seepage exit points that are detectable with thermal infrared (IR) cameras from ground, UAS, or airborne platforms.

## Physical Basis

### Temperature Contrast Mechanism

Groundwater temperature approximates the mean annual air temperature (MAAT) at shallow depths and increases with geothermal gradient at greater depths. In winter, seepage water is warmer than the frozen/cold ground surface. In summer, seepage water is cooler than the sun-heated surface. Maximum thermal contrast occurs during temperature extremes.

**Optimal detection windows:**
- **Winter (cold climates):** Best overall — seepage water (8–15°C) is significantly warmer than frozen ground/snow (< 0°C). Contrasts of 5–15°C common.
- **Summer early morning:** Surface has cooled overnight; seepage zones remain at groundwater temperature. Moderate contrast (3–8°C).
- **Summer midday:** Poor — solar heating dominates; seepage cooling masked or overwhelmed.

### Seepage Indicators

**Direct indicators:**
- Thermal anomaly at a point or zone on the dam face or toe
- Wet zones (evaporative cooling in warm weather, warm zones in cold weather)
- Springs and boils at or downstream of the structure

**Indirect indicators:**
- Vegetation anomalies (lusher growth where seepage provides moisture)
- Soil moisture differences visible in thermal or multispectral imagery
- Ice-free zones in winter along levees or dam toes

## Platforms and Sensors

### Thermal IR Cameras

**LWIR (Long-Wave IR, 8–14 μm):** Standard for seepage detection. Measures emitted thermal radiation from surfaces. Uncooled microbolometer detectors (VOx or α-Si). Resolution: 320×240 to 1024×768 pixels. Thermal sensitivity (NETD): 0.03–0.08°C. Adequate for most applications.

**MWIR (Mid-Wave IR, 3–5 μm):** Cooled InSb detectors. Higher sensitivity but affected by solar reflection during daytime. Better for industrial/high-temperature applications.

### Ground-Based Surveys
Handheld or tripod-mounted thermal cameras. Best for targeted inspection of specific seepage concerns. Can scan entire downstream face of a dam. Requires clear line of sight. Slow for large levee systems.

### UAS-Mounted Thermal
Small UAS (DJI M300/M350 with H20T or XT2 thermal payload). Flight altitude 20–50 m for dam/levee inspection. Ground sampling distance: 50–150 mm/pixel thermal (compared to 5–15 mm/pixel RGB from same altitude). Efficient for linear features (levees, canals). Orthomosaic thermal maps.

**Limitation:** Thermal camera resolution is much lower than RGB. Small seepage points may be below thermal pixel resolution. Fuse thermal and RGB data for precise localization.

### Airborne (Manned Aircraft)
Fixed-wing or helicopter with calibrated thermal sensor. Covers long levee reaches (10–100+ km) efficiently. Ground resolution 0.3–1.0 m thermal. Used for system-wide seepage screening by USACE and state agencies. Best for wintertime surveys when contrast is maximum.

## Applications

### Earth Dams and Levees
- Detection of concentrated seepage paths through the embankment or foundation
- Identification of seepage exit points at the downstream toe
- Monitoring of seepage barrier (cutoff wall, grout curtain) performance
- Detection of internal erosion indicators (sand boils, piping)
- Change detection between surveys to identify new or worsening seepage

### Concrete Dams
- Seepage through lift joints, cracks, or construction joints
- Leakage around embedded waterstops
- Drain performance assessment (active drains should show thermal signatures)
- Foundation seepage emerging at the downstream face or gallery

### Canals and Pipelines
- Seepage losses from unlined or deteriorating canals
- Pipeline leaks (pressurized water creates saturated zones detectable thermally)
- Irrigation canal lining failure zones

### Tailings Dams
- Seepage through or under the embankment
- Phreatic surface monitoring (wet downstream face)
- Decant structure and drain performance

## Data Processing

### Thermal Orthomosaic
Multiple overlapping thermal images mosaicked into a georeferenced thermal map. Processing in standard photogrammetry software (Pix4D, Agisoft Metashape) using thermal images. Challenges: lower resolution, thermal drift during flight, changing conditions.

### Anomaly Detection
- Manual interpretation: trained inspectors identify anomalies against expected thermal patterns
- Statistical: pixel temperature deviation from local or global mean/median
- Temporal: comparison of current survey to baseline or seasonal expected values
- Machine learning: anomaly detection algorithms trained on labeled seepage/non-seepage data

### Quantitative Temperature Mapping
Requires radiometric calibration of the thermal camera. Factors: emissivity of surface (0.90–0.98 for soil, water, concrete; lower for metal), atmospheric transmission, reflected radiation, and camera calibration. Uncorrected thermal images show relative temperature only.
