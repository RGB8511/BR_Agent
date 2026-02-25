# Hoek-Brown Failure Criterion

## Overview

The Hoek-Brown criterion is the most widely used nonlinear failure criterion for intact rock and rock masses. Unlike Mohr-Coulomb, it captures the curved nature of the rock failure envelope — especially important at low confining stresses where Mohr-Coulomb overpredicts tensile strength.

## Generalized Hoek-Brown Criterion (2002 Edition)

σ'₁ = σ'₃ + σ_ci × (m_b × σ'₃/σ_ci + s)^a

where:
- σ'₁ = major principal effective stress at failure
- σ'₃ = minor principal effective stress at failure
- σ_ci = uniaxial compressive strength of intact rock
- m_b, s, a = rock mass parameters (derived from GSI and intact rock constant m_i)

## Intact Rock Criterion

For intact rock (GSI = 100, D = 0): m_b = m_i, s = 1, a = 0.5

σ'₁ = σ'₃ + σ_ci × (m_i × σ'₃/σ_ci + 1)^0.5

The intact rock constant m_i reflects the frictional character of the rock: high m_i for coarse-grained, interlocking minerals (granite ~32); low m_i for fine-grained or foliated rocks (mudstone ~4–7).

## Rock Mass Parameters

The reduction from intact rock to rock mass strength is controlled by the Geological Strength Index (GSI) and Disturbance Factor (D):

m_b = m_i × exp[(GSI - 100) / (28 - 14D)]

s = exp[(GSI - 100) / (9 - 3D)]

a = 0.5 + (1/6) × [exp(-GSI/15) - exp(-20/3)]

For good quality rock masses (GSI > 65): s approaches 1, a ≈ 0.5
For very poor rock masses (GSI < 25): s approaches 0, a approaches 0.65

## Geological Strength Index (GSI)

GSI combines rock mass structure and discontinuity surface condition into a single number (0–100) that drives the Hoek-Brown parameter reduction.

**Structure axis (horizontal):** Intact/massive → Blocky → Very blocky → Blocky/disturbed → Disintegrated → Laminated/sheared

**Surface condition axis (vertical):** Very good → Good → Fair → Poor → Very poor

GSI is estimated from visual observation of rock exposures or core. It is NOT measured — it is a geological observation that requires experience and judgment.

**Key points:**
- GSI should not be used for rock masses where there is a dominant structural orientation (e.g., slate, phyllite with well-defined foliation) — anisotropic analysis required
- GSI < 25 indicates very poor rock approaching soil-like behavior; the criterion becomes less reliable
- Do not try to be precise with GSI — it is inherently imprecise (±5 is realistic)

## Disturbance Factor (D)

D accounts for blast damage and stress relaxation:
- D = 0: Undisturbed in-situ rock mass (TBM excavation, careful blasting)
- D = 0.5: Moderate blast damage
- D = 0.7: Good blasting, typical open pit
- D = 1.0: Very poor blasting, heavy production blasting

D should only be applied to the damaged zone (typically 1–3 m behind the excavation face), not to the entire rock mass. Applying D = 1.0 to a whole slope or pillar significantly underestimates strength.

## Equivalent Mohr-Coulomb Parameters

Many design methods require Mohr-Coulomb (c', φ'). Equivalent parameters are fitted over a specified stress range σ'₃,max:

sinφ' = [6a × m_b × (s + m_b × σ'₃n)^(a-1)] / [2(1 + a)(2 + a) + 6a × m_b × (s + m_b × σ'₃n)^(a-1)]

c' = σ_ci × [(1 + 2a)s + (1 - a) × m_b × σ'₃n] × (s + m_b × σ'₃n)^(a-1) / [(1 + a)(2 + a) × √(1 + [6a × m_b × (s + m_b × σ'₃n)^(a-1)] / [(1 + a)(2 + a)])]

where σ'₃n = σ'₃,max / σ_ci.

**Selecting σ'₃,max:**
- For tunnels: σ'₃,max / σ_cm = 0.47 × (σ_cm / γH)^(-0.94)
- For slopes: σ'₃,max = 0.72 × σ_cm × (σ_cm / γH)^(-0.91)
where σ_cm = rock mass UCS and H = depth or slope height.

## Rock Mass Strength

**Uniaxial compressive strength of rock mass:**
σ_cm = σ_ci × [m_b + 4s - a(m_b - 8s)] × [m_b/4 + s]^(a-1) / [2(1+a)(2+a)]

Simplified (for a = 0.5): σ_cm = σ_ci × s^a

**Tensile strength of rock mass:**
σ_t = -s × σ_ci / m_b

## Rock Mass Modulus

**Hoek-Diederichs (2006):**
E_rm = E_i × (0.02 + [1 - D/2] / [1 + exp((60 + 15D - GSI)/11)])

where E_i = intact rock modulus (typically 200–500 × σ_ci for most rocks, or measured from UCS test).

Alternative (simplified, for D = 0):
E_rm (GPa) = (1 - D/2) × √(σ_ci/100) × 10^((GSI-10)/40) (for σ_ci > 100 MPa)
