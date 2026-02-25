# LiDAR Fundamentals — Terrestrial, Airborne & Mobile

## Principles of Laser Scanning

LiDAR (Light Detection And Ranging) measures distances by emitting laser pulses and recording the return signal. Combined with precise positioning (GNSS) and orientation (IMU), each return is converted to a 3D point in a georeferenced coordinate system. Millions to billions of points form a "point cloud" — a dense, accurate 3D representation of surfaces and objects.

### Ranging Mechanisms

**Time-of-Flight (ToF):** Measures round-trip travel time of a laser pulse. Range = c × t / 2 where c = speed of light, t = two-way travel time. Used in long-range systems (ALS, long-range TLS). Typical accuracy: ±2–10 mm at ranges of 100–2000 m.

**Phase-Shift:** Measures phase difference between emitted and returned continuous-wave modulated laser. Higher precision at shorter ranges. Used in many TLS systems. Typical accuracy: ±1–2 mm at ranges of 1–100 m. Ambiguity at ranges exceeding modulation wavelength — resolved with multiple frequencies.

**Waveform Digitization:** Records the entire return waveform rather than just discrete peaks. Enables extraction of multiple returns within a single pulse footprint and characterization of target geometry. Full-waveform ALS standard for vegetation and forestry; increasingly used for structural analysis.

### Key Parameters

**Pulse Repetition Rate (PRR):** Number of laser pulses per second. Modern systems: TLS: 100,000–2,000,000 pts/s. ALS: 100,000–1,000,000+ pts/s. Higher PRR = denser point cloud for a given scan speed.

**Beam divergence:** Angular spread of the laser beam. Determines footprint size at range. Footprint diameter = Range × beam divergence (radians). Typical: 0.1–0.5 mrad for TLS (1 cm footprint at 100 m); 0.2–0.5 mrad for ALS.

**Scan pattern:** TLS: panoramic (360° × ~300° vertical) or limited field-of-view. ALS: oscillating mirror, rotating polygon, Palmer scan, or fiber scanner producing parallel or sinusoidal ground tracks.

## Terrestrial Laser Scanning (TLS)

### Static TLS
Scanner on tripod at fixed position. Full panoramic scan captures everything visible from that position. Multiple scan positions required for complete coverage (occlusion elimination).

**Registration:** Aligning point clouds from multiple scan positions into a common coordinate system. Methods: target-based (spheres, checkerboards), cloud-to-cloud (ICP algorithm), feature-based, or GNSS-based (if each scan is directly georeferenced).

**Typical applications in geotechnical:**
- Rock slope discontinuity mapping (orientation, spacing, persistence, roughness)
- Structural monitoring (dam faces, retaining walls, tunnel convergence)
- As-built vs. design comparison (earthwork, concrete structures)
- Crack mapping on concrete surfaces
- Volumetric calculations (stockpiles, excavations, borrow pits)

**Accuracy:** 1–5 mm at ranges up to 100 m (phase-shift systems); 5–20 mm at 100–300 m (ToF systems). Point density: 1,000–50,000 pts/m² at typical working distances.

### Long-Range TLS
Systems designed for ranges of 1–6+ km (Riegl VZ-6000, Leica RTC360 extended). Used for large rock faces, quarries, open-pit mines. Lower point density at range but still sufficient for structural geology and volumetric work.

## Airborne Laser Scanning (ALS)

Aircraft or helicopter-mounted LiDAR system combining laser scanner, GNSS receiver, and IMU.

**Point density:** Depends on flying height, speed, PRR, and scan rate. Typical: 2–25 pts/m² for mapping; 25–100+ pts/m² for corridor surveys and engineering. USGS QL1: ≥ 8 pts/m². QL0: ≥ 8 pts/m² with higher accuracy.

**Accuracy:** Vertical: ±5–15 cm (RMSE) typical for well-controlled surveys. Horizontal: ±10–30 cm. Better with low altitude, high IMU grade, and ground control.

**Multiple returns:** ALS records multiple discrete returns per pulse as the beam passes through canopy, understory, and reaches the ground. Essential for bare-earth DEM extraction in vegetated terrain. First return ≈ canopy; last return ≈ ground (usually).

**Applications:** DEM/DTM generation, flood mapping, corridor mapping (pipeline, transmission line), large-area topographic surveys, landslide mapping, fault scarp identification.

## Mobile Laser Scanning (MLS)

Scanner mounted on vehicle (truck, boat, rail car, backpack). Continuous scanning while moving. GNSS+IMU for trajectory solution.

**Point density:** Variable — highest near the scanner, decreasing with range. Corridor focus: 500–5000+ pts/m² on nearby surfaces.

**Applications:** Road/rail corridor surveys, bridge inspection, tunnel profiling, riverbank mapping, utility mapping, pavement condition.

## UAS-Mounted LiDAR

Drone-based LiDAR systems (DJI Zenmuse L1/L2, Riegl miniVUX, YellowScan). Combines advantages of ALS (aerial perspective) with lower cost and higher point density at low altitude.

**Typical specs:** Flying height 30–120 m AGL. Point density: 50–500 pts/m². Accuracy: ±2–5 cm vertical with GCPs. Flight duration: 15–40 min per battery.

**Advantages over UAS photogrammetry:** Penetrates vegetation canopy (multi-return), works in shadow/uniform texture, less affected by lighting conditions, direct georeferencing (no GCPs required for moderate accuracy).

**Limitations:** Higher cost than photogrammetry, heavier payload, shorter flight times, no inherent color (must pair with camera for colorized point cloud).

## Point Cloud Attributes

Each point in a LiDAR dataset carries attributes beyond XYZ:
- **Intensity:** Strength of the return signal. Related to surface reflectivity, range, and angle of incidence.
- **Return number / number of returns:** Which return this point represents (1st, 2nd, etc.) out of total returns for that pulse. Critical for vegetation filtering.
- **Classification:** Assigned category (ground, vegetation, building, water, noise, etc.) per ASPRS LAS classification codes.
- **GPS time:** Precise acquisition timestamp. Enables trajectory reconstruction and time-based filtering.
- **Scan angle:** Angle from nadir at which the point was acquired. Edge-of-swath points have lower accuracy.
- **RGB color:** If co-acquired with camera or colorized from orthophoto.
