# Dam & Levee Surveillance Using Remote Sensing

## Overview

Remote sensing technologies provide spatially continuous, non-contact monitoring of dams and levees that complements traditional point-based instrumentation (piezometers, inclinometers, survey monuments). Key capabilities include: surface deformation mapping, seepage/leakage detection via thermal imaging, vegetation anomaly identification, bathymetric monitoring of reservoirs, and automated change detection. These methods are increasingly integrated into dam safety surveillance programs per ICOLD, USBR, and USACE guidance.

## Surface Deformation Monitoring

### Satellite InSAR for Dams
PS-InSAR and SBAS techniques monitor mm-scale displacement of dam crests, faces, abutments, and surrounding slopes. Corner reflectors installed on concrete surfaces enhance persistent scatterer density and measurement precision.

**Applications:** Concrete dam crest deflection (thermal + hydrostatic), embankment settlement, abutment creep, reservoir rim slope movement, regional foundation compression.

**Limitations:** Temporal resolution limited by satellite revisit (6–14 days). LOS measurement only — decomposition requires ascending + descending data. Vegetation on embankment faces reduces coherence (particularly C-band).

### Ground-Based InSAR (GB-InSAR)
Terrestrial radar interferometer mounted on stable ground facing the dam. Provides displacement maps of the entire visible surface at sub-mm precision with 1–60 minute temporal resolution.

**Advantages over satellite InSAR:** Much higher temporal resolution (minutes vs. days). Targeted coverage of specific structure. Better geometry for measuring cross-valley displacement. Independent of cloud cover.

**Typical deployment:** Ku-band (17 mm wavelength) or C-band. Range: 50 m to 4 km. Pixel resolution: 0.5–5 m. Displacement precision: 0.1–1.0 mm. Continuous operation for months to years for critical dams.

### Terrestrial LiDAR (TLS) for Dams
Repeat TLS surveys detect surface change on dam faces, spillway surfaces, and abutments. M3C2 comparison identifies bulging, settlement, erosion, and structural distress.

**Typical precision:** 2–5 mm at 100 m range (survey-grade scanners). Point density: 1000+ pts/m² enables detailed surface characterization. Repeat interval: semi-annual to annual for routine surveillance; more frequent during concern.

### UAS Photogrammetry/LiDAR for Dams
UAS provides rapid, flexible survey of dam crests, downstream faces, spillway surfaces, and abutment slopes. Orthoimagery enables visual inspection at cm-scale resolution. SfM-derived point clouds support change detection and volumetric analysis.

**Typical accuracy:** 15–50 mm with RTK-GNSS or well-distributed GCPs. Coverage: entire dam and appurtenant structures in hours. Repeat surveys for change detection and construction monitoring.

## Thermal Imaging for Seepage Detection

### Principles
Water seeping through or beneath a dam has a temperature signature different from the surrounding surface. In cool weather, seepage water (at reservoir temperature) is typically warmer than the dry dam surface. In warm weather, the seepage zone may be cooler. The thermal contrast is detectable with infrared cameras from UAS, aircraft, or ground positions.

### Applications
- **Embankment dam seepage:** Wet zones on downstream face, toe drains, foundation seepage paths
- **Concrete dam leakage:** Water emerging through joints, cracks, or drainage galleries
- **Levee seepage:** Through-seepage, under-seepage, sand boil detection during flood events
- **Canal seepage:** Locating sections of high seepage loss for targeted lining repair

### Optimal Conditions
- **Best contrast:** Early morning (pre-dawn) in cool weather — maximum thermal contrast between seepage (warm) and dry surface (cold)
- **Minimum temperature difference detectable:** 0.1–0.5°C with cooled LWIR sensors; 0.5–2°C with uncooled microbolometers
- **Wavelength:** Long-wave infrared (LWIR, 8–14 μm) is standard for surface temperature measurement. Mid-wave infrared (MWIR, 3–5 μm) useful for some applications.

### Platforms
- **Ground-based:** Tripod-mounted thermal cameras for targeted monitoring of known seepage areas
- **UAS-mounted:** Radiometric thermal cameras (e.g., FLIR Vue Pro R, DJI Zenmuse H20T) for full coverage. Typical resolution: 3–10 cm GSD at 30–60 m flight altitude.
- **Manned aircraft:** Airborne thermal surveys for long levee systems (100+ km in a single flight). Lower resolution (0.3–1 m GSD) but very efficient for reconnaissance.

## Vegetation Anomaly Detection

### Principle
Anomalous vegetation on dam and levee embankments can indicate seepage, moisture concentration, or distress. Healthy vegetation in an unexpected location (e.g., lush green strip on otherwise dry downstream face) often correlates with subsurface moisture from seepage. Conversely, stressed or dead vegetation may indicate chemical changes, heat, or soil instability.

### Remote Sensing Methods
- **NDVI (Normalized Difference Vegetation Index):** From multispectral imagery (visible + near-infrared). NDVI = (NIR - Red) / (NIR + Red). High NDVI in unexpected zones = possible seepage indicator.
- **Time-series NDVI:** Seasonal patterns of vegetation vigor compared to historical baseline. Anomalous green-up timing or persistence indicates subsurface moisture.
- **Thermal + NDVI fusion:** Combines surface temperature and vegetation index for more robust seepage identification than either method alone.

## Reservoir Monitoring

### Bathymetric Change Detection
Repeat multibeam or single-beam surveys detect sedimentation, scour around outlet works, and potential sinkhole development.

### Shoreline/Rim Monitoring
UAS or satellite imagery tracks reservoir rim erosion, wave-cut bank retreat, and slope instability above the reservoir. Change detection on rim slopes identifies zones of active movement that could threaten dam safety.

### Floating Debris and Intake Obstruction
Routine UAS overflights identify log jams, floating debris accumulation near intakes or spillways, and vegetation encroachment that could obstruct flow passages.

## Integration with Dam Safety Programs

### Data Fusion
Remote sensing data most valuable when integrated with:
- **Piezometric data:** Correlate seepage thermal anomalies with pore pressure trends
- **Survey monuments:** Calibrate/validate InSAR and TLS displacement measurements
- **Visual inspection records:** Correlate imagery with observed distress conditions
- **Structural analysis:** Measured displacements compared to analytical predictions

### Frequency and Triggers
- **Routine surveillance:** Annual UAS/TLS surveys; continuous satellite InSAR processing
- **Enhanced monitoring:** Monthly surveys during periods of concern (high reservoir, rapid drawdown, seismicity)
- **Emergency response:** Immediate UAS deployment for rapid damage assessment after earthquake, flood, or observed distress
