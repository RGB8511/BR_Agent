# Standards Reference — Deep Foundations

## ASTM D1143 — Standard Test Methods for Deep Foundations Under Static Axial Compressive Load

**Scope:** Full-scale static load test on individual piles or drilled shafts.

**Methods:**
- **Quick test:** Load increments held 5 minutes each. Faster, provides capacity but limited settlement data.
- **Maintained load test (standard):** Load in increments of 25% of design load, held until settlement rate < 0.01 in/hr (0.25 mm/hr) per increment. Continue to failure or 200% of design load.
- **Constant rate of penetration:** Push pile at constant rate (~0.25–1.25 mm/min), record load. Quick, gives clear failure load.

**Key Notes:**
- Reaction system: anchor piles, weighted platform, or ground anchors. Must be far enough to avoid interaction (≥ 5D from test pile to anchor piles).
- Instrumentation: dial gauges or LVDTs on reference beam, load cell at pile head.
- Strain gauges along shaft for load transfer distribution (telltale rods or sister bars).
- Test pile should be equivalent to production piles (same type, size, installation method).

**Interpretation:**
- Davisson offset method (standard for driven piles): failure load at intersection with offset line
- 5% diameter criterion (common for drilled shafts): failure load at settlement = 5% of base diameter
- Chin-Kondner extrapolation: hyperbolic fit for ultimate capacity estimation from incomplete tests

## ASTM D3966 — Standard Test Methods for Deep Foundations Under Lateral Load

**Scope:** Full-scale lateral load test.

**Key Notes:**
- Load applied horizontally near ground surface
- Measure lateral deflection, rotation, and moment (if instrumented)
- Used to calibrate p-y models and verify lateral design
- Free-head or fixed-head conditions

## FHWA GEC-10 — Drilled Shafts: Construction Procedures and Design Methods (2010)

**Scope:** Comprehensive design manual for drilled shafts.

**Key Design Methods:**
- α-method and β-method for shaft resistance
- Base resistance in soil and rock
- Lateral analysis using p-y method
- Rock socket design (Horvath & Kenney, O'Neill & Reese)
- Structural design of shaft concrete and reinforcement
- Construction procedures: dry, casing, wet (slurry) methods
- Integrity testing: CSL (crosshole sonic logging), TIP (thermal integrity profiling)

## FHWA GEC-12 — Design and Construction of Driven Pile Foundations (2016)

**Scope:** Comprehensive design manual for driven piles.

**Key Design Methods:**
- Static analysis methods (α, β, SPT, CPT)
- Wave equation analysis (WEAP) for driveability and capacity
- Dynamic monitoring (PDA) and CAPWAP signal matching
- Dynamic formulas (Gates, EN, modified EN) — less reliable, use with higher FS
- Group effects, negative skin friction, lateral loading
- LRFD calibration and resistance factors
