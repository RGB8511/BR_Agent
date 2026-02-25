# Effective Stress & Pore Pressure

## Terzaghi's Effective Stress Principle

The single most important concept in soil mechanics. All measurable effects of a change of stress, such as compression, distortion, and change of shearing resistance, are exclusively due to changes in effective stress.

σ' = σ - u

where σ = total stress, u = pore water pressure, σ' = effective stress.

**Physical meaning:** Total stress is carried partly by the soil skeleton (effective stress) and partly by the pore water (pore pressure). Only effective stress controls soil behavior because water cannot resist shear.

**Validity:** The principle is exact for saturated soils and an excellent approximation for most engineering purposes. Minor deviations exist for very high contact stresses or unusual grain mineralogy, but these are negligible in practice.

## Total Stress Distribution

Total vertical stress at any depth z below the ground surface:

σ_v = Σ(γ_i × h_i)

where γ_i = unit weight of layer i, h_i = thickness of layer i.

For a uniform soil profile: σ_v = γz

Total stress increases linearly with depth and is independent of the water table position (except through its effect on unit weight — use γ_sat below WT, γ_moist above).

## Pore Water Pressure

**Hydrostatic conditions (no flow):**
u = γ_w × h_w

where h_w = depth below the water table (or height of water in a piezometer above the point of interest).

**Artesian conditions:** Pore pressure exceeds hydrostatic — piezometric surface above ground.

**Underdrained conditions:** Pore pressure less than hydrostatic — downward seepage.

**Negative pore pressure (suction):** Above the water table, capillary tension creates negative pore pressures. In fine-grained soils, this can extend meters above the WT.

## In-Situ Stress State

### Vertical Effective Stress
σ'_v = σ_v - u

### Horizontal Effective Stress
σ'_h = K₀ × σ'_v

where K₀ = coefficient of lateral earth pressure at rest (ratio of horizontal to vertical effective stress under conditions of zero lateral strain).

### K₀ Relationships

**Normally consolidated soils (Jaky 1944):**
K₀ = 1 - sinφ'

This is the most widely used and reliable relationship. For φ' = 30°: K₀ = 0.5.

**Overconsolidated soils (Mayne & Kulhawy 1982):**
K₀(OC) = K₀(NC) × OCR^sinφ' = (1 - sinφ') × OCR^sinφ'

K₀ increases with overconsolidation. For heavily overconsolidated soils, K₀ can exceed 1.0 (σ'_h > σ'_v), which is important for excavation design and tunneling.

## Pore Pressure Parameters (Skempton)

For undrained loading, the change in pore pressure is related to changes in total stress:

Δu = B[Δσ₃ + A(Δσ₁ - Δσ₃)]

**Parameter B:** Relates pore pressure change to isotropic stress change.
- B = 1.0 for fully saturated soil
- B < 1.0 for partially saturated soil (B = 0 for dry soil)
- B is measured as the first stage of a triaxial test (B-check)

**Parameter A:** Relates pore pressure change to deviator stress change.
- A at failure (A_f) varies with soil type and OCR:
  - Soft NC clays: A_f = 0.5–1.5+
  - Lightly OC clays: A_f = 0–0.5
  - Heavily OC clays: A_f = -0.5–0 (dilative behavior)
  - NC loose sands: A_f = 2–3
  - Dense sands: A_f = -0.3–0

## Capillary Effects

Above the water table, surface tension in the menisci between soil grains creates capillary suction (negative pore pressure):

u_c = -2T_s cosα / (r)

where T_s = surface tension of water (~0.073 N/m at 20°C), α = contact angle, r = effective pore radius.

**Capillary rise height:**
h_c ≈ C / (e × D₁₀)

where C = empirical constant (~0.01–0.05 m²), e = void ratio, D₁₀ = effective grain size.

Practical significance: Capillary provides apparent cohesion in sands (allowing sandcastles), but disappears upon saturation or drying. In clays, capillary suction contributes to desiccation cracking at the surface.

## Stress Profile Construction

Standard procedure for computing the vertical stress profile:

1. Identify soil layers and their unit weights (γ_moist above WT, γ_sat below WT)
2. Compute total stress σ_v at each layer boundary: σ_v = Σ(γ_i × h_i)
3. Compute pore pressure u at each point (hydrostatic from WT, or from piezometer data)
4. Compute effective stress: σ'_v = σ_v - u
5. Plot σ_v, u, and σ'_v vs. depth

Key checks: σ'_v must always be positive (if negative, something is wrong). Effective stress increases with depth but at a lesser rate below the water table because buoyancy partially offsets the weight.
