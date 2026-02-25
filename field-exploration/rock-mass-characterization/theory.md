# Rock Mass Characterization — Field Methods

## Purpose

Intact rock properties measured in the laboratory do not represent the behavior of the rock mass in situ. The rock mass is weakened and made anisotropic by discontinuities (joints, bedding, faults, foliation) and weathering. Field rock mass characterization quantifies these features to enable engineering classification (RMR, Q, GSI) and design parameter estimation.

## Discontinuity Surveys

### Scanline Mapping
A measuring tape is stretched along an exposed rock face. Every discontinuity intersecting the scanline is recorded with: distance along tape, orientation (dip/dip direction), type (joint, bedding, fault, foliation, cleavage), persistence, aperture, roughness, infilling, weathering of walls, and seepage.

**Advantages:** Systematic, quantitative, statistical analysis possible. Allows calculation of mean spacing, RQD from spacing, and fracture frequency.

**Bias:** Scanline undersamples joints parallel to the scanline. Correct using Terzaghi (1965) correction: λ_true = λ_apparent / cos(δ), where δ = angle between scanline and joint normal.

### Window Mapping
All discontinuities within a defined rectangular area (window) on the rock face are recorded. Less systematic than scanline but captures the full discontinuity network including shorter, less persistent features.

**Typical window size:** 2 m × 2 m to 10 m × 10 m depending on block size and exposure.

### Cell Mapping
Rock face divided into a grid of cells (typically 5 m × 5 m). Each cell is characterized as a unit with average properties (RQD, joint condition, weathering grade). Used for rapid assessment of large exposures (tunnels, open pits, dam foundations).

### Photography and Photogrammetry
Digital photogrammetry (Structure from Motion) and LIDAR scanning increasingly replace or supplement manual mapping. Software (e.g., ShapeMetrix, CloudCompare, DIPS) extracts discontinuity orientations from 3D point clouds. Advantages: permanent record, access to inaccessible faces, rapid data collection.

## Discontinuity Properties (ISRM Suggested Methods)

### Orientation
Measured with geological compass (Brunton, Silva, Clar). Recorded as dip angle and dip direction (e.g., 45/120 means 45° dip toward azimuth 120°). Plot on stereonet (equal-area, lower hemisphere — Schmidt net) to identify joint sets and their mean orientations.

### Spacing
Distance between adjacent parallel discontinuities of the same set, measured normal to the discontinuity planes.

Classification: extremely close (< 20 mm), very close (20–60 mm), close (60–200 mm), moderate (200–600 mm), wide (600–2000 mm), very wide (> 2000 mm).

### Persistence (Trace Length)
Observed length of the discontinuity trace on the exposure surface.

Classification: very low (< 1 m), low (1–3 m), medium (3–10 m), high (10–20 m), very high (> 20 m).

Persistence determines whether a discontinuity controls block size or can be bridged by intact rock.

### Roughness
Surface texture at two scales:
- **Large-scale waviness:** Stepped, undulating, planar
- **Small-scale roughness:** Rough, smooth, slickensided

**Joint Roughness Coefficient (JRC):** Barton & Choubey (1977). Profiles compared to standard roughness profiles (JRC 0–2 for smooth planar to JRC 18–20 for rough undulating). Measured with profile comb or photogrammetry.

### Aperture
Perpendicular distance between adjacent rock walls of the discontinuity (when no infilling present). Ranges from closed (< 0.1 mm) to very wide (> 100 mm). Controls permeability and shear stiffness.

### Infilling
Material between the discontinuity walls. Type (clay, silt, calcite, quartz, breccia, gouge) and thickness critically affect shear strength. Soft clay infilling may reduce friction angle to 10–15°. Hard mineral infilling may heal the joint.

### Wall Strength — Joint Compressive Strength (JCS)
Strength of the rock immediately adjacent to the discontinuity surface. Often lower than intact rock due to weathering. Measured with Schmidt (rebound) hammer on joint surfaces. Correlated to UCS via established charts.

### Seepage
Water flow observed from individual discontinuities. Rated from dry to continuous flow with measured rate. Affects both stability (pore pressure) and classification systems (water rating in RMR and Q).

## Field Index Tests

### Schmidt Hammer (Rebound Hammer)
**ASTM D5873 / ISRM Suggested Method.** Spring-loaded hammer impacts rock surface; rebound value (R) correlates with UCS. L-type hammer for weak to moderate rock; N-type for moderate to strong rock.

**Procedure:** 20 impacts per location on smooth, non-fractured surface. Discard lowest 50% of readings. Average remaining 10. Apply correction for orientation if not horizontal.

**Correlation (Miller 1965):** log₁₀(UCS) = 0.00088 × γ × R + 1.01 (for L-type, horizontal), where γ = unit weight (kN/m³).

### Point Load Test (Franklin)
**ASTM D5731 / ISRM Suggested Method.** Portable hydraulic press that fractures irregular rock pieces, core, or cut blocks between two conical platens. Quick field estimate of UCS.

**Index:** Is(50) = P / De² where P = failure load, De = equivalent core diameter. For axial test on core: De = D. For irregular lumps: De = √(4A/π) where A = minimum cross-sectional area.

**Correlation:** UCS ≈ K × Is(50) where K = 20–25 (commonly 24 for average rock). K varies by rock type (15 for weak sedimentary to 28 for strong igneous).

## Rock Mass Classification Systems — Field Application

### RQD (Rock Quality Designation)
**Deere (1963).** Percentage of intact core pieces ≥ 100 mm in a core run.

RQD = (Σ lengths of intact pieces ≥ 100 mm) / (total core run length) × 100%

Can also be estimated from discontinuity frequency (Jv, volumetric joint count):
RQD ≈ 115 - 3.3 × Jv (for Jv > 4.5; RQD = 100 for Jv ≤ 4.5)

Or from mean discontinuity spacing (λ = discontinuities per meter):
RQD ≈ 100 × e^(-0.1λ) × (0.1λ + 1)

### Geological Strength Index (GSI)
**Hoek (1994), Hoek & Marinos (2000).** Visual assessment of rock mass structure (intact/blocky/very blocky/blocky-disturbed/disintegrated/laminated-sheared) and surface condition of discontinuities (very good/good/fair/poor/very poor). Directly estimated from exposure; no calculations needed in the field.

GSI ranges from ~5 (very poor, sheared) to ~90 (intact, massive). Fed into generalized Hoek-Brown criterion to estimate rock mass strength and deformability.

### RMR (Rock Mass Rating)
**Bieniawski (1989).** Sum of five parameters rated in the field:
1. Intact rock strength (UCS or point load): 0–15 points
2. RQD: 3–20 points
3. Discontinuity spacing: 5–20 points
4. Condition of discontinuities: 0–30 points
5. Groundwater: 0–15 points

Total RMR (basic) = sum of all ratings (max 100). Adjustment for discontinuity orientation gives final RMR.

### Q-System
**Barton, Lien & Lunde (1974).** Six parameters:

Q = (RQD/Jn) × (Jr/Ja) × (Jw/SRF)

RQD = Rock Quality Designation (10–100)
Jn = Joint set number (0.5–20)
Jr = Joint roughness number (0.5–4)
Ja = Joint alteration number (0.75–20)
Jw = Joint water reduction (0.05–1.0)
SRF = Stress Reduction Factor (0.5–400)

Q ranges from 0.001 (exceptionally poor) to 1000 (exceptionally good). Log scale. Developed for tunnel support design but widely applied.

## Kinematic Analysis

Stereonet-based assessment of potential slope failure modes using discontinuity orientations:

- **Planar sliding:** Joint dips out of slope face, dip direction within ~20° of slope face direction, joint dip > friction angle, joint dip < slope angle
- **Wedge sliding:** Intersection line of two joints plunges out of slope, plunge > friction angle, plunge < slope angle
- **Toppling:** Steep joints dip into slope face; interlayer slip on joints dipping out of slope

Markland test provides quick screening. Detailed analysis requires limit-equilibrium calculations with block geometry, water pressures, and cohesion/friction on discontinuities.
