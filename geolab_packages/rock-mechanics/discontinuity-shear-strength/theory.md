# Discontinuity Shear Strength

## Overview

The strength of a rock mass is usually controlled by the strength of its discontinuities (joints, bedding planes, faults, shear zones) rather than the intact rock. Discontinuity shear strength depends on: normal stress, roughness, wall strength, infilling, and water pressure.

## Patton's Bilinear Model (1966)

The simplest model for rough joints. Two failure modes:

**At low normal stress — sliding over asperities:**
τ = σ'_n × tan(φ_b + i)

where φ_b = basic friction angle and i = effective roughness (dilation) angle.

**At high normal stress — shearing through asperities:**
τ = c_j + σ'_n × tanφ_r

where c_j = apparent cohesion from asperity shearing, φ_r = residual friction angle.

The transition between modes creates a bilinear envelope. In practice, this is an oversimplification — the transition is gradual and the Barton-Bandis criterion better captures the continuous curvature.

## Barton-Bandis Criterion (1977, 1982)

The most widely used nonlinear criterion for unfilled rock joints:

τ = σ'_n × tan[JRC × log₁₀(JCS/σ'_n) + φ_r]

where:
- JRC = Joint Roughness Coefficient (0–20)
- JCS = Joint Wall Compressive Strength (MPa)
- φ_r = residual friction angle of the joint surface
- σ'_n = effective normal stress on the joint

### Joint Roughness Coefficient (JRC)

JRC quantifies the roughness of the joint surface on a scale of 0 (planar, slickensided) to 20 (very rough, undulating). Determined by:

1. **Visual comparison** with Barton's 10 standard roughness profiles (most common method)
2. **Tilt test:** JRC = (α - φ_r) / log₁₀(JCS/σ'_n0) where α = tilt angle at sliding, σ'_n0 = stress at sliding from block weight
3. **Back-calculation** from direct shear test data

**Scale effect:** JRC decreases with joint length. Field-scale JRC is lower than lab-scale:
JRC_n = JRC_0 × (L_n/L_0)^(-0.02×JRC_0)

where L_0 = lab sample length (~100 mm), L_n = field joint length.

### Joint Wall Compressive Strength (JCS)

JCS is the compressive strength of the rock at the joint surface. For fresh, unweathered joints: JCS ≈ σ_ci. For weathered joints: JCS << σ_ci.

Measured using Schmidt hammer (rebound number R) on the joint surface:
log₁₀(JCS) = 0.00088 × γ_rock × R + 1.01 (using L-type hammer, γ in kN/m³)

**Scale effect on JCS:**
JCS_n = JCS_0 × (L_n/L_0)^(-0.03×JRC_0)

### Residual Friction Angle (φ_r)

φ_r for unweathered surfaces approximated from basic friction angle:
φ_r ≈ (φ_b - 20°) + 20 × (r/R)

where r = Schmidt hammer rebound on weathered joint surface, R = rebound on fresh rock surface, φ_b = basic friction angle of saw-cut or fresh surface.

If r/R = 1 (unweathered): φ_r = φ_b.

## Infilled Discontinuities

When joints contain clay, gouge, or other infilling, strength depends on infilling thickness relative to roughness amplitude:

**Thin infilling (t < asperity amplitude):** Rock-to-rock contact still occurs at peaks. Strength intermediate between infilling and rock joint.

**Thick infilling (t >> asperity amplitude):** Strength governed entirely by infilling material. Use Mohr-Coulomb parameters for the infilling (clay, gouge).

**Rule of thumb:** When infilling thickness exceeds ~2× the asperity amplitude, the rock wall roughness has negligible effect on shear strength.

Barton (1974) proposed a staged model:
- Stage 1: Rock wall contact → φ = φ_b + i (asperity controlled)
- Stage 2: Partial wall contact → intermediate strength
- Stage 3: No wall contact → φ = φ_filling
- Stage 4: Thick filling → c and φ of filling material

## Normal Stress Limitations

The Barton-Bandis criterion has a valid stress range:

σ'_n < JCS (approximately)

The term JRC × log₁₀(JCS/σ'_n) should not exceed ~70° (total friction + dilation angle). If it does, the calculated strength may be unconservative. At very high normal stress (σ'_n approaching JCS), the joint is fully interlocked and behavior transitions toward intact rock shear.
