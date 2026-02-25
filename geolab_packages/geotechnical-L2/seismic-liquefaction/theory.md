# Seismic Hazards & Liquefaction

## Overview

Liquefaction occurs when saturated loose granular soil loses strength due to cyclic loading (earthquake shaking). Excess pore pressure builds up, effective stress drops to zero, and the soil behaves as a heavy fluid. Consequences: settlement, lateral spreading, bearing capacity failure, flow slides.

## Susceptibility Screening

**Soil type:** Most susceptible: clean sands and silty sands (FC < 35%). Low-plasticity silts can liquefy. Clays with PI > 7 and w/LL < 0.85 are generally not susceptible (Boulanger & Idriss 2006 "clay-like" criterion).

**Saturation:** Must be saturated (or very nearly). Soils above the water table do not liquefy.

**Density:** Loose to medium-dense soils susceptible. Dense sands dilate and resist liquefaction.

**Age and cementation:** Recent Holocene deposits most susceptible. Pleistocene and older deposits less susceptible due to aging effects.

**Depth:** Liquefaction typically assessed to 20–25 m depth. Deeper soils have higher confining stress → less susceptible.

## Simplified Procedure (Seed & Idriss)

The standard-of-practice approach compares the Cyclic Stress Ratio (CSR — earthquake demand) to the Cyclic Resistance Ratio (CRR — soil capacity).

### Cyclic Stress Ratio (CSR)

CSR₇.₅ = 0.65 × (a_max/g) × (σ_v0/σ'_v0) × r_d / MSF

where:
- a_max = peak ground acceleration at site
- σ_v0 = total overburden stress at depth z
- σ'_v0 = effective overburden stress at depth z
- r_d = stress reduction factor (accounts for flexibility of soil column)
- MSF = magnitude scaling factor (adjusts to M = 7.5 reference)

### Stress Reduction Factor (r_d)

Boulanger & Idriss (2014):
- r_d = exp(α(z) + β(z)M)
- Complex function of depth z and magnitude M
- Simplified: r_d ≈ 1.0 - 0.00765z for z ≤ 9.15 m; r_d ≈ 1.174 - 0.0267z for 9.15 < z ≤ 23 m

### Magnitude Scaling Factor (MSF)

MSF = 10^2.24 / (M_w^2.56) (Idriss 1999)

For M = 7.5: MSF = 1.0 (reference). M = 6: MSF ≈ 1.8. M = 8: MSF ≈ 0.84.

## CRR from SPT

### Boulanger & Idriss (2014) SPT-based:

CRR₇.₅ = exp{(N₁)₆₀cs/14.1 + [(N₁)₆₀cs/126]² - [(N₁)₆₀cs/23.6]³ + [(N₁)₆₀cs/25.4]⁴ - 2.8}

where (N₁)₆₀cs = fines-corrected, overburden-corrected N-value.

**Fines correction:**
ΔN = exp(1.63 + 9.7/(FC + 0.01) - [15.7/(FC + 0.01)]²) for FC ≥ 5%
(N₁)₆₀cs = (N₁)₆₀ + ΔN

## CRR from CPT

### Boulanger & Idriss (2014) CPT-based:

CRR₇.₅ = exp{q_c1Ncs/113 + (q_c1Ncs/1000)² - (q_c1Ncs/140)³ + (q_c1Ncs/137)⁴ - 2.8}

where q_c1Ncs = fines-corrected, overburden-normalized cone resistance.

CPT is generally preferred over SPT for liquefaction assessment because:
- Continuous profile (no gaps)
- More repeatable (less operator dependence)
- Soil type identification from Q_tn, F_r

## Factor of Safety and Consequences

FS_liq = CRR₇.₅ / CSR₇.₅

- FS < 1.0: Liquefaction expected
- 1.0 ≤ FS < 1.2: Marginal (may liquefy, engineering judgment)
- FS ≥ 1.2: Liquefaction unlikely

### Post-Liquefaction Settlement

Tokimatsu & Seed (1987), Ishihara & Yoshimine (1992): Volumetric strain (εᵥ) as a function of FS and relative density. Integrate εᵥ over depth of liquefiable layers.

Typical: 1–5% volumetric strain in liquefied layers → 0.1–1+ m total settlement for thick liquefiable deposits.

### Lateral Spreading

Youd, Hansen & Bartlett (2002) empirical model:
log(D_H) = f(M, R, T₁₅, F₁₅, D50₁₅, slope or free-face ratio)

where D_H = horizontal ground displacement, T₁₅ = cumulative thickness of liquefiable layers with (N₁)₆₀ < 15.

## Newmark Displacement Analysis

For slopes or embankments: estimate permanent displacement from earthquake using yield acceleration concept.

1. Determine yield acceleration k_y (acceleration at which FS = 1.0 in pseudostatic analysis)
2. Use Newmark sliding block analogy with acceleration time history
3. Empirical correlations: Bray & Travasarou (2007), Makdisi & Seed (1978)

## Mitigation Measures

- **Densification:** Vibro-compaction, dynamic compaction, compaction grouting
- **Drainage:** Stone columns, wick drains (accelerate pore pressure dissipation)
- **Reinforcement:** Stone columns, soil mixing, jet grouting
- **Structural:** Deep foundations through liquefiable layers, ground improvement beneath foundations
- **Avoidance:** Relocate structure to non-liquefiable ground
