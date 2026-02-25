# Shear Strength of Soils

## Mohr-Coulomb Failure Criterion

The fundamental strength model for soils:

τ_f = c' + σ'_n × tanφ'

where τ_f = shear strength on the failure plane, c' = effective cohesion (intercept), σ'_n = effective normal stress on failure plane, φ' = effective friction angle.

**Physical meaning:** Shear resistance comes from friction between particles (tanφ' term) and interparticle bonding/cementation (c' term). For most soils, c' is small or zero at large strains; φ' is the primary source of strength.

### Total Stress vs. Effective Stress Analysis

**Effective stress parameters (c', φ'):** Used for drained conditions or when pore pressures are known. Long-term stability, drained loading.

**Total stress parameters (c_u, φ_u or s_u):** Used for undrained conditions when pore pressures cannot be reliably predicted. Short-term stability of saturated clays. For saturated clay under undrained loading: φ_u = 0, and τ_f = s_u (undrained shear strength).

## Drained vs. Undrained Behavior

### Drained Conditions
- Excess pore pressure fully dissipated (Δu = 0)
- Volume change occurs freely
- Use effective stress parameters (c', φ')
- Applies to: long-term slope stability, granular soils under any loading rate, clays under very slow loading

### Undrained Conditions
- No volume change (ΔV = 0 for saturated soil)
- Excess pore pressure develops
- Use total stress analysis with s_u
- Applies to: rapid loading of saturated clays, end-of-construction for embankments on clay, rapid drawdown

### Partially Drained
- Intermediate condition during consolidation
- Common in practice; often bounded by fully drained and fully undrained analyses

## Triaxial Test Types

### UU — Unconsolidated Undrained (ASTM D2850)
- No consolidation, no drainage during shear
- Provides s_u (undrained shear strength)
- Total stress failure envelope: φ_u = 0 (horizontal line for saturated soils)
- Fastest test; does not require pore pressure measurement
- Used for: short-term bearing capacity, end-of-construction stability

### CU — Consolidated Undrained with Pore Pressure Measurement (ASTM D4767)
- Consolidate to desired effective stress, then shear undrained
- Pore pressure measured during shear
- Provides both total stress (c_u, φ_u) and effective stress (c', φ') parameters
- Most versatile test — most commonly specified
- Used for: effective stress analysis, stress path evaluation, excess pore pressure prediction

### CD — Consolidated Drained (ASTM D7181)
- Consolidate to desired effective stress, then shear slowly enough for full drainage
- Volume change measured during shear (no excess pore pressure)
- Directly provides c', φ'
- Very slow for clays (days to weeks to prevent pore pressure buildup)
- Used for: long-term stability when CU data not available

## Direct Shear Test (ASTM D3080)

Specimen sheared along a predetermined horizontal failure plane.

**Advantages:** Simple, fast, can test granular soils and interfaces.
**Limitations:** Failure plane forced (not free to develop on weakest plane), non-uniform stress/strain distribution, drainage conditions not well controlled, progressive failure on shear plane.

Test at 3+ normal stresses → plot τ_f vs. σ'_n → straight line gives c', φ'.

## Residual Strength

At large displacements, clay particles on the shear plane align parallel to the direction of movement, reducing strength to a minimum residual value:

τ_r = σ'_n × tanφ'_r

Residual friction angle φ'_r is always less than peak φ'. The difference is most significant for plastic clays:
- Low plasticity clays: φ'_r ≈ φ'_peak (small difference)
- High plasticity clays: φ'_r can be 5–15° less than φ'_peak
- Montmorillonite-rich: φ'_r as low as 5–10°

Residual strength governs: reactivated landslides, slopes with pre-existing shear surfaces, faults, and any surface with prior large displacement.

Measured using ring shear test (ASTM D6467) or repeated direct shear (ASTM D3080 with multiple reversals).

## Undrained Shear Strength

For saturated clays under undrained loading:

s_u = c_u = τ_f (with φ_u = 0)

### Correlations and Normalization

**s_u / σ'_v0 ratio:**
- NC clays: s_u/σ'_v0 ≈ 0.22 (Mesri, 1975) or 0.11 + 0.0037 × PI (Skempton, 1957)
- OC clays: s_u/σ'_v0 = (s_u/σ'_v0)_NC × OCR^m where m ≈ 0.8 (Ladd & Foott, 1974; SHANSEP)

**SHANSEP Method (Stress History and Normalized Soil Engineering Properties):**
s_u/σ'_v0 = S × OCR^m

where S = normalized strength ratio for NC soil, m = strength increase exponent. Determined from CK₀U tests on specimens consolidated to various OCRs.

### Field Measurement

**Vane shear test (ASTM D2573):** Four-bladed vane rotated in soft clay. Peak torque → s_u. Remolded torque → s_u(remolded) → sensitivity.

Correction factor (Bjerrum, 1972): s_u(design) = μ × s_u(vane) where μ = f(PI), typically 0.6–1.0. Correction accounts for rate effects, anisotropy, and progressive failure not captured in the vane test.

## Stress Path Concepts

The stress path plots the trajectory of stress states during loading in q-p' space:
- q = (σ'₁ - σ'₃)/2 (deviator stress)
- p' = (σ'₁ + σ'₃)/2 (mean effective stress)

The failure envelope in q-p' space: q_f = a + p'_f × tanα

where a = c' cosφ' and tanα = sinφ'.

Stress paths reveal:
- Whether loading is drained or undrained
- How close the current state is to failure
- The effect of pore pressure generation on stability
