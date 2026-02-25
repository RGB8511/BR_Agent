# Field Density Testing — Compaction Verification

## Purpose

Field density testing verifies that compacted fill meets the specified density (compaction) requirements. The measured field dry density is compared against a laboratory maximum dry density from a standard or modified Proctor test to determine the percent relative compaction.

## Nuclear Density Gauge (NDG) — ASTM D6938

### Principle
A radioactive source (Cs-137 for density, Am-241:Be for moisture) emits gamma rays and neutrons into the soil. Detectors measure backscattered radiation. Gamma attenuation correlates with bulk density; neutron thermalization correlates with hydrogen (moisture) content.

### Modes
- **Direct transmission (density):** Source rod inserted into a predrilled hole (150–300 mm depth). Most accurate mode — gamma passes through the material between source and surface detector.
- **Backscatter (density):** Source and detector both on the surface. Less accurate — primarily measures upper 75–100 mm. Used when rod hole cannot be drilled (very stiff, rocky material).
- **Moisture:** Am-241:Be neutron source always in backscatter mode. Measures upper 150–200 mm. Less accurate than oven-drying — calibrate against oven-dried samples.

### Advantages
Fast (1–4 minute test), non-destructive, simultaneous density and moisture, repeatable. Standard for routine construction QA/QC.

### Limitations
Requires NRC license and radiation safety training. Chemical composition affects readings (high mineral density or unusual hydrogen sources). Not accurate in chemite-treated or highly organic soils without correction. Must be calibrated against reference blocks. Regulatory and transportation requirements for radioactive source.

### Field Procedure
1. Prepare level test surface (plate seats flat)
2. Drill rod hole (for direct transmission) using provided drill rod
3. Seat gauge, insert source rod to test depth
4. Take 1-minute standard count; record wet density and moisture
5. Calculate dry density: γ_d = γ_wet / (1 + w)

## Sand Cone Method — ASTM D1556

### Principle
Excavate a test hole in the compacted material. Determine the volume of the hole by filling it with calibrated sand (Ottawa sand, C778) from a cone apparatus. Weigh the excavated soil and determine moisture content by oven-drying.

### Procedure
1. Level surface; seat base plate
2. Excavate hole through plate opening (typically 100–150 mm diameter, 150 mm deep)
3. Collect ALL excavated material; weigh
4. Place sand cone apparatus on plate; open valve and fill hole + cone with sand
5. Determine sand volume from weight of sand used (subtract cone volume)
6. V_hole = W_sand_in_hole / γ_sand_calibrated
7. γ_wet = W_soil / V_hole
8. Determine w from oven-dried sample
9. γ_d = γ_wet / (1 + w)

### Advantages
No radioactive source required. Directly measures volume and mass. Can verify NDG calibration. Required where NDG not available or for verification testing.

### Limitations
Destructive (must excavate). Slower than NDG (30–45 minutes). Sensitive to vibration during sand placement. Hole walls must be stable (difficult in very loose or cohesionless soil without moisture).

## Rubber Balloon Method — ASTM D2167

Similar to sand cone but uses a water-filled rubber balloon to measure hole volume. Balloon is inflated into the test hole under calibrated pressure; volume change of water measured on graduated cylinder.

**Advantages:** Faster than sand cone, reusable water. **Limitations:** Irregular hole walls may not be fully contacted; less common than sand cone.

## Drive Cylinder Method — ASTM D2937

Thin-walled steel cylinder driven into the material. Volume = cylinder volume. Weight of soil in cylinder / volume = density. Simple, fast, but only suitable for cohesive soils that hold shape when cylinder is extracted.

## Percent Relative Compaction

RC (%) = (γ_d_field / γ_d_max) × 100

where γ_d_max is from the reference Proctor test (standard D698 or modified D1557).

**Typical specifications:**
- Structural fill: ≥ 95% of modified Proctor (D1557)
- General fill: ≥ 90–95% of standard Proctor (D698)
- Trench backfill: ≥ 90% of standard Proctor
- Roadway subgrade: ≥ 95% of modified Proctor

Moisture must also be within the specified range — typically within ±2–3% of optimum moisture content (wet side preferred for low-permeability applications; dry side for strength).

## One-Point Proctor Method

When many different soil types are encountered and running full Proctor curves for each is impractical, the one-point method uses a single compaction test point and a family of Proctor curves to estimate the maximum dry density and optimum moisture content. Per ASTM D5080 (Hilf method): plot the one-point result on a family of curves for the soil type to estimate γ_d_max and w_opt.

## Non-Nuclear Alternatives

### Electrical Density Gauge (EDG)
Uses electrical impedance measurements (capacitance and resistance) to determine density and moisture. No radioactive source. Examples: Humboldt GeoGauge-EDG, TransTech SDG-200.

### Time Domain Reflectometry (TDR)
Electromagnetic pulse propagation in soil. Dielectric constant correlates with moisture content. Can estimate density when combined with separate measurement.

### Stiffness/Modulus Gauges
GeoGauge (Humboldt H-4140): measures surface stiffness/modulus of the upper ~225 mm. Does not directly measure density but correlates with compaction quality. ASTM D6758. Useful for relative comparison but does not replace density testing for specification compliance.
