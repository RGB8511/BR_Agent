# In-Situ Permeability & Hydraulic Conductivity Testing

## Overview

In-situ permeability testing measures the hydraulic conductivity (k) of soil and rock in place, avoiding the disturbance and scale effects inherent in laboratory testing. Field tests capture the effects of natural fabric, fissures, bedding, and discontinuities that control real flow behavior.

## Packer (Lugeon) Tests in Rock

### Purpose
The water pressure test (WPT), commonly called the Lugeon test, measures the permeability of rock masses by injecting water under pressure into a sealed interval of a borehole. It is the standard permeability test for dam foundations, tunnel alignment investigations, and grouting programs.

### Procedure
1. Drill borehole to test interval depth (typically NX or HQ diameter)
2. Set single or double packer to isolate a test interval (typically 3–5 m, maximum 6 m)
3. Inject water at controlled pressure in 5 steps (ascending and descending): typically 0.25, 0.50, 0.75, 1.0, and 0.75, 0.50, 0.25 × maximum test pressure
4. Record flow rate at each pressure step after steady state (typically 10 min per step)
5. Maximum test pressure: usually limited to avoid hydrofracture (rule: ≤ 1 psi per foot of overburden, or ≤ 0.023 MPa per meter)

### Lugeon Value
1 Lugeon (Lu) = 1 liter/minute per meter of test interval at a reference pressure of 1 MPa (10 bar / ~145 psi).

Lugeons relate approximately to hydraulic conductivity: 1 Lu ≈ 1.3 × 10⁻⁷ m/s (order-of-magnitude approximation only — depends on borehole geometry and assumptions).

### Pattern Analysis (Houlsby 1976)
The shape of the pressure-flow curve (ascending vs. descending steps) reveals the flow regime:
- **Laminar flow:** Linear Q-P relationship; ascending and descending curves coincide. Simple Lugeon calculation valid.
- **Turbulent flow:** Q increases less than proportionally with P; no hysteresis. Compute Lugeon at low pressures.
- **Dilation (jacking):** Flow increases dramatically at higher pressures; descending flow > ascending flow. Fractures open under pressure.
- **Washout:** Progressive increase in flow with time at each step; descending > ascending. Joint infill eroded by flow.
- **Void filling:** Flow decreases with time; ascending > descending. Voids being filled. Not a true permeability measurement.

## Slug Tests in Soil and Rock

### Principle
A known volume of water is instantaneously added to (falling-head) or removed from (rising-head) a monitoring well or piezometer, and the rate of water level recovery to static conditions is measured.

### Hvorslev Method (1951)
Assumes uniform, homogeneous conditions around the well screen:

K = (r² × ln(Le/R)) / (2 × Le × T₀)

where T₀ = basic time lag (time for 63% recovery), r = standpipe radius, R = well screen radius, Le = screen length.

Plot ln(H/H₀) vs. time → T₀ = time at H/H₀ = 0.37.

### Bouwer-Rice Method (1976)
For unconfined aquifers with partially or fully penetrating wells:

K = (rc² × ln(Re/rw)) / (2 × Le × t) × ln(H₀/Ht)

where Re = effective radius over which head dissipates (from empirical curves depending on geometry), rc = casing radius, rw = well radius (including gravel pack).

Plot ln(H) vs. time → slope gives K.

## Pump Tests (Aquifer Tests)

### Purpose
Full-scale pump tests measure aquifer properties (transmissivity T, storativity S, hydraulic conductivity K) by pumping a well at constant rate and measuring drawdown in observation wells over time.

### Theis Method (Confined Aquifer)
s = (Q / 4πT) × W(u)

where u = r²S/(4Tt), W(u) = well function. Type-curve matching of drawdown vs. time on log-log paper.

### Cooper-Jacob Method (Simplified Theis)
For large times (u < 0.05):
s = (2.303 × Q) / (4π × T) × log(2.25Tt / r²S)

Plot s vs. log(t) → T from slope, S from intercept. Most practical method for routine analysis.

### Unconfined Aquifers
Neuman (1975) method accounts for delayed yield (drainage from above the water table). Double straight-line behavior on semilog plot.

## Falling/Rising Head Tests in Boreholes

### Open Borehole (Variable Head)
For uncased borehole in uniform soil:

K = (A / F × t) × ln(H₁/H₂)

where A = cross-sectional area of standpipe, F = shape factor (depends on borehole geometry and test configuration), H₁ and H₂ = head at times t₁ and t₂.

Shape factors from Hvorslev (1951) for various borehole configurations (flush bottom, extended below casing, with/without filter).

## Field vs. Laboratory Permeability

Field tests generally yield higher permeability than laboratory tests because:
- Field tests capture macro-fabric (fissures, sand lenses, root holes, bedding planes)
- Laboratory tests measure matrix permeability only
- Scale effect: larger test volume captures more heterogeneity
- Rock mass permeability is dominated by discontinuities, not intact rock matrix

Typical ratio: K_field / K_lab = 2–100+ (rock can be 1000×). For dam seepage analysis and dewatering design, use field-measured values.
