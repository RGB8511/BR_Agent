# Surface Geophysics for Geotechnical Investigation

## Overview

Surface geophysics provides non-invasive subsurface characterization by measuring physical property contrasts (seismic velocity, electrical resistivity, dielectric permittivity, density, magnetic susceptibility) from the ground surface. Methods complement direct exploration (borings, CPT) by filling spatial gaps between point measurements and identifying anomalous zones for targeted investigation.

**Key principle:** Every geophysical method measures a physical property contrast. No contrast = no detection. Geophysics provides models of physical properties, not directly geology — interpretation requires ground truth from borings.

## Seismic Methods

### Seismic Refraction
**Principle:** Measures travel time of compressional (P) waves refracted along subsurface layer boundaries where velocity increases with depth. First arrivals at each geophone plotted as time-distance graph; slope inversions indicate layer boundaries.

**Applications:** Depth to bedrock, rippability assessment, water table depth (saturated soil velocity jump), weathering profile characterization.

**Limitations:** Requires velocity increase with depth (velocity inversions = hidden layers). Cannot resolve thin layers. Blind to low-velocity zones beneath high-velocity layers. Resolution decreases with depth.

**Field setup:** Linear geophone array (24–48 geophones at 1–5 m spacing). Source: sledgehammer (shallow) or explosive/weight drop (deep). Multiple shot points at array ends and offsets.

**Depth of investigation:** ~1/3 to 1/5 of total spread length. 120 m spread → ~25–40 m depth.

### Multichannel Analysis of Surface Waves (MASW)
**Principle:** Records Rayleigh surface waves, which are dispersive — different frequencies (wavelengths) sample different depths. Dispersion curve (phase velocity vs. frequency) is inverted to produce a 1D shear wave velocity (Vs) profile.

**Applications:** Vs30 for seismic site classification (IBC/ASCE 7), liquefaction assessment (Vs-based), ground stiffness profiling, detection of soft/weak zones.

**Advantages over refraction:** Does not require velocity increase with depth; can detect velocity inversions (soft layers beneath stiff). Directly measures Vs (key geotechnical parameter).

**Field setup:** Linear array of 24–48 low-frequency (4.5 Hz) geophones at 1–2 m spacing. Active source (sledgehammer, weight drop) at multiple offsets. Passive MASW uses ambient noise (traffic, ocean waves) for deeper investigation.

**Depth:** Active MASW: 15–30 m typical. Passive: 50–100+ m with favorable ambient noise.

### Seismic Reflection
**Principle:** Records reflected seismic waves from impedance contrasts (velocity × density boundaries). Common midpoint (CMP) stacking improves signal/noise. Produces depth sections similar to cross-sections.

**Applications:** Deep stratigraphy (> 30 m), fault detection, buried channel mapping, cavity detection (in some conditions).

**Limitations:** Expensive, requires significant processing expertise. Near-surface reflections often obscured by direct/refracted arrivals. Less commonly used in geotechnical than in petroleum/mining.

## Electrical and Electromagnetic Methods

### Electrical Resistivity Imaging (ERI) / Electrical Resistivity Tomography (ERT)
**Principle:** Injects current between electrode pairs and measures potential difference at other electrode pairs. Multiple electrode combinations (Wenner, Schlumberger, dipole-dipole arrays) build a 2D pseudosection that is inverted to produce a true resistivity cross-section.

**Applications:** Bedrock depth and topography, groundwater table, clay/sand differentiation, contamination plumes, karst/void detection, seepage paths in dams/levees, landslide investigation.

**Resolution:** Electrode spacing controls resolution. 1–2 m spacing for near-surface detail; 5–10 m for deeper regional surveys. Depth ≈ 1/5 to 1/3 of total array length (Wenner) or shallower for dipole-dipole (better lateral resolution).

**Typical resistivities:** Clay: 1–100 Ω·m. Sand (saturated): 10–800 Ω·m. Sand (dry): 200–5000+ Ω·m. Bedrock (intact): 100–10,000+ Ω·m. Contaminated groundwater: low resistivity.

### Ground Penetrating Radar (GPR)
**Principle:** Transmits electromagnetic pulses (10 MHz – 2.5 GHz) into the ground. Reflections from dielectric contrasts are recorded. Produces a radar-gram (depth section).

**Applications:** Utility detection, rebar/void location in concrete, shallow bedrock mapping, pavement thickness, archaeological features, shallow stratigraphy in sand/gravel.

**Critical limitation:** Highly attenuated in clay and saturated fine-grained soils. Penetration in clay: < 1 m. In dry sand/gravel: 10–30 m. In rock: 5–20 m. Frequency tradeoff: higher frequency → better resolution but less depth.

### Electromagnetic Induction (EM / FEM)
**Principle:** Transmitter coil generates primary EM field; secondary field induced in conductive ground is measured by receiver coil. No ground contact required (fast for reconnaissance).

**Instruments:** Geonics EM31 (shallow: 0–6 m), EM34 (deeper: 10–60 m), EM38 (agricultural: 0–1.5 m), GEM-2 (multi-frequency).

**Applications:** Mapping conductive zones (clay, contamination, salinity), landfill boundaries, buried metal objects, quick lateral variability screening.

## Potential Field Methods

### Gravity / Microgravity
**Principle:** Measures subtle variations in gravitational acceleration caused by density contrasts. Requires extremely sensitive instruments (resolution ~1–10 μGal).

**Applications:** Karst/void detection (negative anomaly from air-filled cavity), buried valley mapping, bedrock topography in some settings.

**Limitations:** Non-unique inversion (many models fit the data). Requires precise elevation survey and extensive data corrections (terrain, tidal, drift).

### Magnetics
**Principle:** Measures total magnetic field or vertical gradient. Anomalies from magnetic susceptibility contrasts (ferrous objects, some minerals, volcanic rocks).

**Applications:** Buried metal detection (USTs, drums, pipes, unexploded ordnance), igneous rock mapping, some mineral exploration. Gradiometer (two sensors) improves resolution and reduces diurnal correction needs.

## Method Selection

No single method solves all problems. Effective geophysical investigation typically combines 2–3 methods. Seismic for velocity/stiffness, ERI for resistivity/stratigraphy, and GPR or EM for shallow detail. All require calibration against borehole data.
