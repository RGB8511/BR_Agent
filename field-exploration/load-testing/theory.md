# Field Load Testing — Piles, Anchors, Plates & Proof Tests

## Static Pile Load Tests

### Axial Compression (ASTM D1143)
The definitive method for verifying pile capacity. A test pile is loaded incrementally to failure or a specified multiple of the design load while measuring settlement.

**Loading procedures:**
- **Slow Maintained Load (SM):** Apply load in increments (typically 25% of design load), maintain each increment until rate of settlement < 0.25 mm/hr, load to 200% of design load or failure. Unload in decrements. Duration: 24–72+ hours. Most common for contract verification.
- **Quick Maintained Load (QM):** Apply load in increments (5–10% of design load), maintain each for a fixed time (2.5–15 min regardless of settlement). Load to failure. Duration: 3–8 hours. Preferred for research and when failure load is needed.
- **Constant Rate of Penetration (CRP):** Advance pile at constant rate (0.25–1.25 mm/min for cohesive, 0.75–2.5 mm/min for granular). Load measured continuously. Quick test — determines ultimate capacity directly. Requires hydraulic servo control.

**Reaction system:** Dead weight (kentledge), reaction piles (anchored), or combination. Reaction piles spaced ≥ 5D (5 pile diameters) from test pile to minimize interaction. Reference beams for settlement measurement independent of reaction system (supported ≥ 8D from test pile).

### Axial Tension (ASTM D3689)
Test pile loaded in tension (uplift) to verify pullout resistance. Similar loading procedures to compression. Reaction frame bears on the ground surface — ensure bearing pads do not affect soil around test pile.

### Lateral Load (ASTM D3966)
Horizontal load applied to pile head. Measure lateral deflection vs. load. Results compared to p-y curve analysis (COM624G, LPILE). Loading: incremental to 200% design lateral load, or to specified deflection.

## Failure Criteria for Static Load Tests

### Davisson Offset Limit (1972)
The most widely used criterion in North America for driven piles:

s_failure = PL/(AE) + 3.8 + D/120 (mm, with D in mm)

where PL/(AE) = elastic compression of the pile, D = pile diameter/width. Draw this line offset from the origin on the load-settlement curve. Capacity = load at which the curve intersects the offset line.

### Other Criteria
- **Chin-Kondner (1970):** Plot Δ/Q vs. Δ (settlement/load vs. settlement). Linear portion → slope = 1/Q_ult. Hyperbolic extrapolation to ultimate capacity.
- **De Beer (1967):** Log-log plot of load vs. settlement. Break in slope indicates failure.
- **FHWA 5% D criterion:** Failure = load at settlement of 5% of pile diameter (for drilled shafts).
- **Butler-Hoy (1977):** Parallel tangent method.

## Osterberg Cell (O-Cell) Tests

Sacrificial hydraulic jack cast within the drilled shaft or driven pile. Expands bidirectionally — pushes downward against the soil below (mobilizing end bearing) and upward against the shaft above (mobilizing skin friction).

**Advantages:** No external reaction system needed. Tests very large loads (> 100 MN possible). Can separate skin friction from end bearing. Works at great depth where conventional tests are impractical.

**Limitations:** Sacrificial (jack cannot be reused, shaft is not usable as production pile unless grouted). Requires careful pre-selection of O-cell elevation to mobilize both components. Does not directly replicate top-down loading — requires construction of equivalent top-loaded curve.

## Dynamic Pile Testing

### Pile Driving Analyzer (PDA) — ASTM D4945
Strain transducers and accelerometers attached near the pile head during driving. Measure force and velocity waves from each hammer blow. Real-time estimates of capacity, hammer energy, pile stresses, and integrity.

**CASE Method:** Simplified closed-form capacity estimate from one hammer blow:

R_total = ½[(F₁ + Z×V₁) + (F₂ - Z×V₂)]

where F, V = force and velocity at times t₁ (impact) and t₂ = t₁ + 2L/c (reflection), Z = pile impedance = EA/c.

### CAPWAP (Case Pile Wave Analysis Program)
Signal-matching analysis of PDA data. Iterative: adjust soil resistance distribution (shaft friction + end bearing, quake, damping) until computed wave matches measured wave. More accurate than CASE method. Provides capacity, resistance distribution, and load-settlement simulation.

### Statnamic Testing
Controlled explosion (fuel combustion) accelerates a mass upward, pushing the pile down. Load duration ~100–200 ms — between static and dynamic. Measures force, acceleration, and displacement. Unloading point method extracts static capacity from the dynamic response.

**Advantages:** Faster than static test, no reaction system, loads up to 30 MN+. Tests pile in actual soil conditions.

## Pile Integrity Testing

### Cross-hole Sonic Logging (CSL)
Water-filled access tubes cast in drilled shaft. Ultrasonic source in one tube, receiver in another. Measures wave speed and energy through the concrete between tubes. Detects defects (voids, inclusions, necking, cracks).

**Tube requirements:** One tube per 300 mm of shaft diameter (minimum 3). Steel or PVC tubes, water-filled, bottom-capped.

### Pile Integrity Test (PIT) / Low-Strain Impact
Small hammer strikes pile head; accelerometer measures reflected waves. Changes in impedance (cross-section or material change) produce reflections. Quick screening for major defects (necking, breaks). Cannot detect minor defects or assess capacity.

### Thermal Integrity Profiling (TIP)
Thermal wires or probes in access tubes measure temperature distribution during concrete curing. Hydration heat is proportional to concrete cross-section. Anomalies indicate defects. Advantage: 100% coverage of shaft perimeter; quantitative diameter profile.

## Anchor and Tieback Tests

### Test Types (per PTI DC35.1 and FHWA-SA-99-015)

**Performance test:** Load anchor in increments to maximum test load (typically 133% of design load). At each increment, measure creep (movement vs. time at constant load, typically 10 min). Full load-deformation and creep behavior documented. Required on a percentage of production anchors (typically 5%).

**Proof test:** Simplified performance test. Load to maximum test load (133% DL), hold and measure creep, then lock off at design load. Required on every production anchor.

**Extended creep test:** Load held at maximum test load for extended period (24–72 hr for soil, 8 hr for rock typical). Required when anchoring in creep-susceptible soils (soft clay, organic, weathered shale).

### Acceptance Criteria
- **Elastic movement:** Total movement minus residual (creep) must exceed 80% of theoretical elastic elongation of the unbonded length. This verifies the anchor is loaded, the bond zone is intact, and the unbonded length is free.
- **Creep rate:** Movement during hold period at maximum test load must be less than specified limit (typically 1–2 mm per log cycle of time for soil anchors, less for rock).
- **Residual movement:** Residual movement after unloading must not exceed specified amount.

## Plate Load Tests

### Surface Plate Load Test (ASTM D1196 / D1195)
Rigid circular or square plate (typically 300–750 mm diameter) loaded incrementally against the ground surface. Measures load-settlement response. Used for:
- Modulus of subgrade reaction (k = q/s at specific settlement)
- Bearing capacity estimation
- Pavement subgrade evaluation

**Size effect:** Plate test results apply to loaded area only. Scale to footing size using: k_footing = k_plate × (B_plate/B_footing) for cohesionless soils; k_footing ≈ k_plate for cohesive soils (width-independent).

### Plate Load in Borehole/Test Pit (ASTM D4394/D4395)
Plate loaded at depth (in test pit or at bottom of borehole). Tests soil at foundation bearing elevation. More representative than surface tests.

### Flat Jack Test (Rock)
Thin hydraulic jack inserted into a saw-cut slot in a rock surface. Used to measure in-situ stress (cancel deformation caused by sawing) and rock mass deformability.
