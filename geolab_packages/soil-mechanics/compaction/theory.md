# Compaction Theory & Practice

## Fundamentals

Compaction is the densification of soil by expelling air from the voids through mechanical energy. Unlike consolidation, compaction is rapid, involves air expulsion (not water), and applies to unsaturated soils.

### The Compaction Curve

Plotting dry unit weight (γ_d) versus molding water content (w) produces a bell-shaped curve with a distinct peak. The peak defines the maximum dry unit weight (γ_d,max) and optimum moisture content (w_opt).

**Dry side of optimum:** Soil is stiff, clods resist breakdown, air voids remain trapped. Water acts as lubricant — adding water allows particles to rearrange more efficiently, increasing density.

**Wet side of optimum:** Pore water pressure develops during compaction, resisting further densification. Additional water occupies void space without corresponding air expulsion. Density decreases.

**Zero Air Voids (ZAV) line:** The theoretical upper bound where S = 100%. No compaction point can plot above the ZAV line. The compaction curve approaches but never reaches the ZAV line at high moisture contents.

### Effect of Compactive Effort

Increasing compactive effort (more blows, heavier hammer, or more passes):
- Increases γ_d,max
- Decreases w_opt
- Shifts the entire curve upward and to the left
- The line of optimums approximately parallels the ZAV line

### Effect of Soil Type

- **Well-graded gravelly soils:** High γ_d,max (19–22 kN/m³), low w_opt (6–10%)
- **Uniform sands:** Moderate γ_d,max, may show erratic curve (capillary tension at low w)
- **Silts:** Moderate γ_d,max (15–18 kN/m³), moderate w_opt (12–20%)
- **Clays (CL):** Moderate γ_d,max (15–18 kN/m³), moderate w_opt (12–20%)
- **Fat clays (CH):** Low γ_d,max (12–16 kN/m³), high w_opt (18–30%)
- **Organic soils:** Very low γ_d,max, generally unsuitable for structural fill

## Standard vs. Modified Proctor

The two standard laboratory compaction tests bracket typical field equipment energy:

**Standard Proctor (ASTM D698):** 5.5 lb (2.49 kg) hammer, 12 in (305 mm) drop, 3 layers, 25 blows/layer in 4-in mold. Compactive effort = 12,400 ft·lb/ft³ (600 kN·m/m³).

**Modified Proctor (ASTM D1557):** 10 lb (4.54 kg) hammer, 18 in (457 mm) drop, 5 layers, 25 blows/layer in 4-in mold. Compactive effort = 56,000 ft·lb/ft³ (2,700 kN·m/m³).

Modified Proctor produces γ_d,max approximately 5–10% higher and w_opt approximately 3–5% lower than Standard Proctor for the same soil.

## Compaction Specifications

### Relative Compaction (RC)
RC = γ_d(field) / γ_d,max(lab) × 100%

Typical specifications:
- Structural fills, dam cores: ≥ 95% of Modified Proctor
- General earthwork, highways: ≥ 95% of Standard Proctor
- Backfill around structures: ≥ 90–95% of Standard Proctor
- Landscape/non-structural: ≥ 85–90% of Standard Proctor

### Moisture Content Window
Typically specified as w_opt ± 2% to ± 4% depending on application. Dry side gives higher strength and stiffness but is more brittle and susceptible to collapse on wetting. Wet side gives lower permeability but lower strength and higher compressibility.

**Dam cores:** Often specified wet of optimum (w_opt to w_opt + 3%) to minimize permeability and prevent hydraulic fracturing. USBR and USACE practice.

**Highway subgrades:** Often specified near optimum for balanced strength and compressibility.

## Structure and Engineering Properties

Compaction on the dry vs. wet side of optimum produces fundamentally different soil fabric, even at the same dry density:

**Dry of optimum (flocculated structure):**
- Higher shear strength
- Higher stiffness (modulus)
- Higher permeability
- More brittle stress-strain behavior
- Susceptible to collapse on wetting
- Susceptible to swelling from adsorbed water

**Wet of optimum (dispersed structure):**
- Lower shear strength
- Lower stiffness
- Lower permeability (10–100× lower than dry side)
- More ductile stress-strain behavior
- Less susceptible to collapse on wetting
- Higher pore pressures during loading

## Field Compaction Equipment

- **Smooth drum roller:** General fill, granular soils. Static or vibratory.
- **Sheepsfoot/padfoot roller:** Cohesive soils. Kneads and bonds lifts. "Walks out" when compaction is adequate.
- **Pneumatic (rubber-tired) roller:** Versatile. Good for granular and cohesive. Kneading action.
- **Vibratory roller:** Essential for granular soils. Vibration causes particle rearrangement. Frequency and amplitude tuned to soil type.
- **Impact (rammer):** Confined areas, trench backfill.

**Lift thickness:** Typically 6–12 in (150–300 mm) loose, depending on equipment and soil type. Heavier equipment allows thicker lifts.

## Field Density Testing

### Sand Cone Method (ASTM D1556)
Excavate hole in compacted fill, weigh removed soil, determine volume by filling hole with calibrated sand. Calculate γ and w. The reference method — slow but reliable.

### Nuclear Density Gauge (ASTM D6938)
Rapid measurement of γ and w using gamma radiation (density) and neutron emission (moisture). Requires calibration against sand cone. Direct transmission mode (probe in hole) more accurate than backscatter (surface).

### Drive Cylinder (ASTM D2937)
Thin-walled tube driven into cohesive fill. Intact sample weighed and measured. Simple but limited to cohesive soils without gravel.

### Relative Compaction vs. Relative Density
For cohesionless soils, relative density (D_r from D4253/D4254) is sometimes used instead of Proctor-based RC. Approximate relationship:

RC ≈ 80 + 0.2 × D_r (Lee & Singh, 1971)

This means 100% relative density ≈ 100% relative compaction, and 0% relative density ≈ 80% relative compaction. The correlation is approximate.
