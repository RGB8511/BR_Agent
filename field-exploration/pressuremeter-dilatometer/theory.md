# Pressuremeter & Flat Dilatometer Tests

## PRESSUREMETER TEST (PMT)

### Principle
A cylindrical probe is expanded radially against the borehole wall by applying internal pressure (gas or water). The relationship between applied pressure and radial expansion provides: in-situ horizontal stress, shear modulus, undrained shear strength (clays), and limit pressure.

### Types of Pressuremeter

**Prebored Pressuremeter (PBP / Menard PMT):**
- Probe inserted into a pre-drilled borehole
- Most common type worldwide
- Borehole must be carefully prepared (close to probe diameter, clean, stable)
- Results affected by borehole disturbance — initial portion of curve represents reconsolidation against disturbed soil, not in-situ conditions
- Menard interpretation uses empirical rules developed specifically for PBP

**Self-Boring Pressuremeter (SBPMT):**
- Probe drills its own way into the soil, minimizing disturbance
- Provides the most reliable measurement of in-situ horizontal stress (K₀)
- Better curve quality — initial linear portion reflects true elastic response
- More complex equipment, slower, more expensive
- Cambridge-type (UK) and PAF-type (France)

**Full-Displacement Pressuremeter (FDPMT):**
- Probe pushed or driven into soil (like a large CPT cone with an expanding section)
- Results reflect soil response after large displacement — useful for pile design
- Cone pressuremeter: CPT cone with pressuremeter module behind it

### Menard Pressuremeter Interpretation

The Menard pressure-volume curve yields:
- **p₀:** Initial pressure at which membrane contacts the borehole wall (lift-off pressure). In a perfect test, p₀ ≈ total horizontal stress σh0. In PBP, p₀ is uncertain due to borehole disturbance.
- **pf (creep pressure):** Pressure at which creep volume significantly increases — marks transition from pseudo-elastic to plastic behavior. Approximately pf ≈ (p₀ + pL)/2.
- **pL (limit pressure):** Pressure at which cavity expansion is theoretically infinite (soil fails completely). Extrapolated from the test curve.
- **EM (Menard modulus):** Slope of the linear portion × geometric factor. EM = 2(1+ν)(V₀+Vm) × ΔP/ΔV. Note: EM is NOT a Young's modulus — it is a hybrid parameter used in Menard's empirical design methods.

### SBPMT Interpretation

The SBPMT curve is analyzed using cavity expansion theory:
- **σh0:** Lift-off pressure (reliable K₀ measurement)
- **Gur (unload-reload modulus):** From unload-reload loops — best estimate of in-situ shear stiffness
- **Su:** From undrained cavity expansion theory: Su = (pL - σh0)/[1 + ln(G/Su)]
- **φ':** From drained cavity expansion in sands (Hughes, Wroth & Windle 1977)

## FLAT DILATOMETER TEST (DMT)

### Principle
A flat, stainless-steel blade (14 mm thick, 95 mm wide) with a 60 mm diameter flexible steel membrane on one face is pushed vertically into the soil using CPT/drill rod push system. At each test depth (typically every 200 mm), two pressure readings are taken:
- **A-pressure (p₀):** Pressure at which the membrane lifts off (starts to move 0.05 mm)
- **B-pressure (p₁):** Pressure at which the membrane expands 1.10 mm into the soil

### DMT Intermediate Parameters

From p₀ and p₁ (corrected for membrane stiffness):
- **Material Index:** ID = (p₁ - p₀) / (p₀ - u₀)
- **Horizontal Stress Index:** KD = (p₀ - u₀) / σ'v0
- **Dilatometer Modulus:** ED = 34.7 × (p₁ - p₀)

### DMT Interpretation

**Soil type from ID:** ID < 0.6: clay. 0.6–1.8: silt. ID > 1.8: sand.

**OCR from KD:** OCR = (0.5 × KD)^1.56 (Marchetti 1980, for clays). KD is analogous to K₀ but amplified by the blade insertion process. KD = 2 corresponds approximately to NC soil (OCR ≈ 1).

**K₀ from KD:** K₀ = (KD/1.5)^0.47 - 0.6 (Marchetti 1980). Approximate; best for NC to lightly OC clays.

**Su from KD:** Su = 0.22 × σ'v0 × (0.5 × KD)^1.25 (Marchetti 1980).

**Constrained modulus M from ED:** M = RM × ED, where RM is a factor depending on ID and KD (Marchetti 1980, modified by Marchetti et al. 2001). For ID < 0.6 (clay): RM ≈ 0.14 + 2.36×log(KD). For sands: RM is more complex.

### DMT Advantages
- Fast: 200 mm depth increments, 1–2 min per test depth → 15–25 m/day
- Repeatable: two simple pressure readings, minimal operator dependence
- Robust: blade is durable; simple equipment
- Provides: soil type, K₀ estimate, OCR, Su, M, and indirectly φ'
- Good complement to CPT — provides different parameters from independent measurements
