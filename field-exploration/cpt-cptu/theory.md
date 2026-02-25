# Cone Penetration Test (CPT/CPTu)

## Overview

The CPT advances an instrumented cone at a constant rate (20 mm/s) through the soil, continuously measuring tip resistance (qc), sleeve friction (fs), and, in the piezocone (CPTu), pore water pressure (u2). It provides a continuous, repeatable, high-resolution profile of soil properties — far superior to discrete SPT sampling.

## Equipment

**Standard cone:** 35.7 mm diameter (10 cm² cross-sectional area), 60° apex angle. Friction sleeve: 150 cm² surface area, located immediately behind the cone tip. Pore pressure filter: typically at the u2 position (just behind the cone tip, at the shoulder).

**Push system:** Hydraulic rams (truck-mounted or anchored) capable of 100–200 kN push force. Penetration rate: 20 ± 5 mm/s per ASTM D5778.

**Seismic CPT (SCPT):** Geophone or accelerometer module above the cone measures shear wave arrivals from a surface source. Provides Vs profile alongside CPT data — combines two tests in one push.

## Measured Parameters

**qc — Cone tip resistance:** Force on cone tip / cone area. Ranges from < 0.5 MPa in very soft clay to > 50 MPa in dense sand/gravel.

**fs — Sleeve friction:** Friction force on sleeve / sleeve area. Typically 1–200 kPa.

**u2 — Pore pressure at shoulder:** Dynamic pore pressure during penetration. In clay: u2 >> hydrostatic (excess pore pressure from undrained shearing). In sand: u2 ≈ hydrostatic (drained). In OC clay: u2 may be zero or negative.

## Corrected Parameters

### Corrected Tip Resistance (qt)
Unequal area effects at the cone-sleeve junction require correction:

qt = qc + u2 × (1 - a)

where a = net area ratio (typically 0.70–0.85; specific to each cone). This correction is significant in soft clays where u2 is large relative to qc.

### Friction Ratio (Rf)
Rf = (fs / qt) × 100%

Ranges from < 1% in clean sand to > 5% in plastic clay. Key parameter for soil classification.

### Normalized Parameters (Robertson 2009)
Qt = (qt - σv) / σ'v (normalized cone resistance)
Fr = fs / (qt - σv) × 100% (normalized friction ratio)
Bq = (u2 - u0) / (qt - σv) (pore pressure ratio, where u0 = equilibrium pore pressure)

## Soil Classification

### Robertson SBTn Chart (2009)
Uses Qt and Fr on a log-log plot to classify soil behavior type. Nine zones from sensitive fine-grained (Zone 1) through sand/gravel (Zone 7) to very stiff OC soil (Zone 8-9).

### Soil Behavior Type Index (Ic)
Ic = √[(3.47 - log Qt)² + (log Fr + 1.22)²]

Ic < 1.31: gravelly sand; 1.31–2.05: sand; 2.05–2.60: sand mixtures; 2.60–2.95: silt mixtures; 2.95–3.60: clays; > 3.60: organic/sensitive.

Ic is used extensively for liquefaction screening (Ic < 2.6 generally considered potentially liquefiable).

## Dissipation Tests

Stop penetration and monitor u2 decay over time. The rate of excess pore pressure dissipation is related to the coefficient of consolidation (ch) and soil permeability.

**t50:** Time for 50% dissipation. Used to estimate ch using Teh & Houlsby (1991) solution:

ch = (T50* × r²) / t50

where T50* = theoretical time factor (function of rigidity index Ir), r = cone radius.

## Key Correlations

**Undrained shear strength:**
Su = (qt - σv) / Nkt where Nkt = 10–20 (site-specific calibration needed; typically 12–15)

**Effective friction angle (sand):**
φ' from qt using Kulhawy & Mayne (1990): φ' = 17.6 + 11.0 × log(Qt)

**Constrained modulus:**
M = α_M × (qt - σv) where α_M varies with Ic (5–15 for sands, 2–8 for clays)

**Small-strain shear modulus (from SCPT):**
G₀ = ρ × Vs² (directly measured from seismic module)

**Permeability (from dissipation):**
k = ch × γw / M

## Advantages over SPT

Continuous profile (no gaps), highly repeatable, operator-independent, faster, provides three independent measurements simultaneously, direct measurement of Vs (SCPT), pore pressure data for groundwater characterization, and better-defined theoretical framework for interpretation.

## Limitations

Cannot penetrate hard rock, cemented layers, or very dense gravel (cone refusal). No physical sample recovered — must pair with borings for classification confirmation. Equipment expensive. Requires specialized operators and equipment. Access more limited than conventional drill rigs (although track-mounted CPT rigs available).
