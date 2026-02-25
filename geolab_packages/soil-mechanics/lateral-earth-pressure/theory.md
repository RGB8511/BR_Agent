# Lateral Earth Pressure

## Three States of Lateral Earth Pressure

### At-Rest (K₀)
No lateral deformation. Horizontal effective stress σ'_h = K₀ × σ'_v. Applies to rigid walls, basement walls restrained at top before backfilling, and the in-situ condition of undisturbed soil.

### Active (K_a)
Wall moves away from soil (sufficient to mobilize full shear strength). Minimum lateral pressure. Requires small displacement: ~0.001H–0.004H for sands, ~0.01H–0.04H for clays. Failure surface develops.

### Passive (K_p)
Wall pushed into soil. Maximum lateral pressure. Requires large displacement: ~0.02H–0.06H for sands, ~0.05H–0.10H for clays (much larger than active). Develops in front of embedded walls, anchor blocks, bearing capacity.

**Critical concept:** Active requires very small movement — most retaining walls achieve active conditions. Passive requires large movement and is often not fully mobilized, so design often uses reduced K_p or factored passive resistance.

## Rankine Theory

Assumes: smooth wall (no wall friction δ = 0), horizontal ground surface, vertical wall face, homogeneous soil.

**Active:** σ'_a = K_a × σ'_v - 2c'√K_a

K_a = tan²(45° - φ'/2) = (1 - sinφ') / (1 + sinφ')

**Passive:** σ'_p = K_p × σ'_v + 2c'√K_p

K_p = tan²(45° + φ'/2) = (1 + sinφ') / (1 - sinφ')

**For inclined backfill (slope angle β):**
K_a = cosβ × [cosβ - √(cos²β - cos²φ')] / [cosβ + √(cos²β - cos²φ')]
(resultant acts parallel to slope surface)

### Tension Crack Zone
For soils with c' > 0, the active pressure equation gives negative (tensile) stress near the surface. Since soil cannot sustain tension, a tension crack forms to depth:

z_c = (2c') / (γ × √K_a)

In practice, tension cracks fill with water, adding hydrostatic pressure. This is critical for slope stability and temporary excavation support.

## Coulomb Theory

Considers wall friction (δ) and inclined wall face. Assumes planar failure surface.

**Active:**
K_a = sin²(α + φ') / [sin²α × sin(α - δ) × (1 + √(sin(φ'+δ)×sin(φ'-β) / sin(α-δ)×sin(α+β)))²]

where α = wall face angle from horizontal (90° for vertical), β = backfill slope, δ = wall-soil friction angle.

**Passive (Coulomb — use with caution):**
The Coulomb passive pressure with wall friction significantly overestimates K_p because the actual failure surface is curved (log-spiral), not planar. For δ/φ' > 1/3, Coulomb passive is unconservative. Use log-spiral tables (Caquot & Kérisel) or Rankine (δ = 0) instead.

## Wall Friction

**Typical δ/φ' ratios:**
- Cast-in-place concrete against soil: δ/φ' = 0.7–1.0
- Precast concrete: δ/φ' = 0.5–0.7
- Steel sheet pile: δ/φ' = 0.5–0.7
- Wood: δ/φ' = 0.5–0.8
- Geomembrane: δ varies widely, must be tested

Wall friction reduces active pressure (favorable) and increases passive resistance (favorable) — but the Coulomb passive calculation is unreliable for δ > 0.

## Surcharge Loading

### Uniform Surcharge (q)
Adds constant horizontal pressure: Δσ_h = K × q (where K = K_a or K_0 as appropriate)

### Line Load, Strip Load, Point Load
Use elastic solutions (Boussinesq-type) modified for rigid wall boundary condition (image method — double the elastic solution for rigid wall):

Typical approach: 2× Boussinesq solution projected onto wall face, integrated over wall height. Charts in NAVFAC DM-7.02.

## Pressure Distribution on Walls

**Granular backfill (drained):** Triangular active pressure distribution + rectangular surcharge pressure. Resultant acts at H/3 from base (triangular) or H/2 (uniform surcharge).

**Clay backfill (short-term, undrained):**
σ_a = γz - 2s_u

Negative near surface (tension crack zone). Short-term pressures may be low, but long-term pressures as clay reaches drained equilibrium are higher. Generally avoid clay as retaining wall backfill.

**At-rest (unyielding walls):**
σ_h = K₀ × γ'z + u

Must include water pressure separately if wall is not drained.

## Water Pressure

Water behind retaining walls is the most common cause of retaining wall failure. Total lateral force includes both earth pressure (using effective stress and buoyant unit weight below WT) PLUS full hydrostatic water pressure. Proper drainage is essential.
