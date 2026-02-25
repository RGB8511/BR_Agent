# Ground Improvement Methods

## Overview

Ground improvement encompasses techniques that modify in-situ soil properties to meet engineering requirements — increasing strength, reducing compressibility, accelerating consolidation, controlling seepage, or mitigating liquefaction. Selection depends on soil type, required improvement, depth, area, schedule, and cost.

## Preloading and Surcharge

### Principle
Apply temporary load (fill surcharge) to consolidate soft soils before construction. Remove surcharge after target settlement or strength gain is achieved.

### Without Drains
Consolidation occurs via vertical drainage. Time depends on t = Tv × H²dr / cv. For thick clay layers, consolidation can take years to decades.

### With Prefabricated Vertical Drains (PVDs / Wick Drains)
Wick drains (band-shaped, typically 100 mm × 4 mm) installed in a grid pattern reduce the drainage path from the full layer thickness to half the drain spacing. Consolidation governed by radial drainage:

Ū_r = 1 - exp(-8T_h / F(n))

where T_h = c_h × t / d_e², d_e = equivalent diameter of influence zone (1.05s for triangular, 1.13s for square spacing, s = drain spacing), and F(n) accounts for drain well resistance and smear effects.

**Typical spacing:** 1.0–2.5 m. Installed by mandrel to full depth of compressible layer.

### Vacuum Preloading
Apply atmospheric pressure (~80 kPa) as consolidation pressure via sealed membrane and vacuum pumps. Equivalent to surcharge fill but without stability concerns. Can be combined with PVDs.

## Densification Methods (Granular Soils)

### Vibro-Compaction
Vibratory probe (vibroflot) lowered into ground, densifies loose granular soil by vibration and optional backfill. Effective in clean sands (FC < 10–15%). Typical improvement depth: up to 20 m. Quality control by post-improvement CPT or SPT.

### Dynamic Compaction
Heavy weight (10–40 tonnes) dropped from height (10–30 m) repeatedly on a grid pattern. Effective depth ≈ n√(W×H) where n = 0.3–0.7 (empirical), W = weight (tonnes), H = drop height (m). Suitable for loose fills, granular soils, and some waste deposits. Not effective for saturated fine-grained soils (unless combined with drainage).

### Rapid Impact Compaction (RIC)
Hydraulic hammer (5–12 tonnes) dropped repeatedly from 1–2 m. Shallower improvement than dynamic compaction (3–6 m). Less ground vibration.

## Reinforcement Methods

### Stone Columns (Vibro-Replacement)
Columns of compacted gravel (600–1000 mm diameter) installed by displacement or replacement vibroflot. Functions: drainage (reduces consolidation time), reinforcement (carries load through stiffer column), and stress concentration (load transfers from soft soil to column). Applicable to soft clays and silts.

**Area replacement ratio:** a_s = A_column / A_tributary

**Composite modulus:** E_comp = a_s × E_column + (1 - a_s) × E_soil

Stress concentration ratio (n) typically 2–5 for stone columns.

### Aggregate Piers (Rammed Aggregate Piers)
Short, densely compacted aggregate columns installed by ramming aggregate in a pre-drilled or displacement cavity. Higher stiffness than conventional stone columns. Typical improvement: bearing capacity increase 2–4×, settlement reduction 50–70%.

## Grouting Methods

### Compaction Grouting
Injection of stiff, low-slump mortar (typically 25–75 mm slump) at high pressure to displace and densify surrounding soil. Does not penetrate soil pores. Used for: settlement remediation under existing structures, sinkhole repair, liquefaction mitigation.

### Permeation Grouting
Injection of fluid grout (chemical or microfine cement) that permeates soil pores. Applicable to sands and gravels. Reduces permeability, increases strength. Limited to soils with sufficient permeability (k > 10⁻³ cm/s for microfine cement, > 10⁻² for standard cement).

### Jet Grouting
High-pressure (30–60 MPa) fluid jets erode and mix in-situ soil with cement grout to create soilcrete columns (0.6–3.0 m diameter depending on system). Three systems: single fluid (grout only), double fluid (grout + air), triple fluid (water + air to erode, grout to fill). Applicable to all soil types. Used for underpinning, excavation support, groundwater cutoff.

### Deep Soil Mixing (DSM)
Mechanical mixing of in-situ soil with cement, lime, or slag binder using rotating auger(s). Wet method (slurry) or dry method (powder). Creates columns or panels of improved soil. UCS of mixed soil: 0.5–5+ MPa depending on soil type, binder, and dosage.

## Soil Stabilization

### Cement Stabilization
Portland cement mixed with soil (typically 3–15% by dry weight). Increases strength and stiffness, reduces plasticity and swell potential. Effective for granular soils and low-plasticity clays. Requires pulverization, mixing, compaction, and curing.

### Lime Stabilization
Quicklime (CaO) or hydrated lime (Ca(OH)₂) mixed with clayey soil (typically 3–8%). Reduces plasticity immediately (cation exchange), followed by long-term pozzolanic reactions (strength gain over weeks–months). Most effective for high-plasticity clays (PI > 10).

### Fly Ash Stabilization
Fly ash (with or without lime/cement activator) mixed with soil. Pozzolanic reactions develop strength over time. Economical where fly ash is locally available.

## Geosynthetic Reinforcement

### Basal Reinforcement
High-strength geotextile or geogrid placed at the base of embankments over soft ground. Increases stability during construction by providing tensile reinforcement at the failure surface. Does not reduce settlement.

### Mechanically Stabilized Earth (MSE) / Reinforced Earth
Alternating layers of compacted fill and horizontal reinforcement (metallic strips, geogrids, geotextiles) with a facing system. Creates steep or vertical reinforced soil structures. Design per AASHTO LRFD or FHWA-NHI-10-024.
