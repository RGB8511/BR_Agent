# Concrete Testing Methods

## Compressive Strength (ASTM C39)

The most fundamental and widely used concrete test. Standard specimens are 150 × 300 mm (6 × 12 in) or 100 × 200 mm (4 × 8 in) cylinders loaded to failure in uniaxial compression.

**Procedure:** Cylinders cured per ASTM C31 (field) or C192 (lab). Ends capped with sulfur (C617) or neoprene pads (C1231). Load at 0.25 ± 0.05 MPa/s until failure.

**Compressive strength:** f'c = P / A where P = maximum load and A = cross-sectional area.

**Failure patterns:**
- Cone (ideal): shear planes form ~60° cones at both ends
- Columnar: vertical fractures through both ends — may indicate platen friction issues
- Shear: single diagonal fracture — may indicate eccentricity
- Side fracture: fracture through side — specimen defect

**Size effect:** 100 × 200 mm cylinders give ~3–5% higher strength than 150 × 300 mm. Apply correction factor if needed. L/D ratio affects results — standard is L/D = 2. For L/D < 1.75, apply correction factor (ASTM C42 Table 1).

## Split Tensile Strength (ASTM C496)

Indirect tension test. Cylinder loaded on its side along a diametral line. Creates near-uniform tensile stress across the vertical plane.

f_t = 2P / (π × L × D)

where L = length, D = diameter. Typical split tensile strength ≈ 8–14% of compressive strength (higher % at lower f'c).

## Flexural Strength — Modulus of Rupture (ASTM C78, C293)

Beam test. 150 × 150 × 500 mm (6 × 6 × 20 in) beams loaded in third-point (C78) or center-point (C293) bending.

Third-point loading (C78): f_r = P × L / (b × d²) (when fracture is in middle third)

Center-point loading (C293): f_r = 3P × L / (2 × b × d²)

Modulus of rupture f_r typically 10–15% of f'c. Commonly used for pavement design (FAA, DOTs).

## Modulus of Elasticity (ASTM C469)

Static modulus measured as secant modulus to 40% of f'c on cylinder specimens instrumented with compressometer.

E_c ≈ 4730√f'c (MPa) for normal weight concrete (ACI 318 empirical)
E_c = 0.043 × w^1.5 × √f'c (for unit weights 1440–2560 kg/m³)

Also measures Poisson's ratio (ν ≈ 0.15–0.25, typically 0.20 for normal concrete).

## Core Testing (ASTM C42)

When cylinder strength fails to meet specifications, cores drilled from the structure provide in-situ strength assessment.

**ACI 318 acceptance criteria:** Structure is adequate if average of 3 cores ≥ 0.85f'c AND no single core < 0.75f'c.

Cores are typically weaker than molded cylinders due to drilling damage, different curing conditions, and direction of casting vs. loading. Apply L/D correction factors for L/D < 1.75.

## Non-Destructive Testing (NDT)

### Rebound Hammer (ASTM C805)
Spring-loaded mass rebounds off concrete surface. Rebound number (R) correlates loosely with strength. Affected by surface condition, carbonation, moisture, aggregate type. Best for comparative assessment (uniformity surveys), not absolute strength.

### Ultrasonic Pulse Velocity (ASTM C597)
Measures time for ultrasonic pulse to travel through concrete. UPV correlates with quality and uniformity:

V = L / t

| UPV (m/s) | Quality |
|---|---|
| > 4500 | Excellent |
| 3500–4500 | Good |
| 3000–3500 | Questionable |
| 2000–3000 | Poor |
| < 2000 | Very poor |

Can detect internal voids, cracks, delamination. Combined with rebound hammer (SonReb method) gives better strength estimates than either alone.

### Ground Penetrating Radar (ASTM D6087)
Locates rebar, tendon ducts, voids, delamination. Non-contact, rapid scanning. Cannot determine strength.

### Impact Echo
Stress wave propagation for detecting delamination, voids, and thickness. Particularly useful for slabs and walls.

## Maturity Method (ASTM C1074)

Estimates in-place strength based on temperature-time history rather than test cylinders:

M = Σ(T - T₀) × Δt (Nurse-Saul maturity)

or equivalent age: t_e = Σ exp[Q(1/T_r - 1/T_a)] × Δt (Arrhenius)

Requires calibration with lab specimens from the same mix. Embedded temperature sensors transmit data. Useful for form stripping, prestressing, cold weather decisions.
