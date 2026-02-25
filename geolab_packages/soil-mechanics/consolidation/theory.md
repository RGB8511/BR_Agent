# Consolidation Theory & Settlement

## Overview

Consolidation is the time-dependent compression of saturated fine-grained soil due to the expulsion of pore water under sustained loading. Unlike immediate (elastic) compression, consolidation involves gradual pore pressure dissipation and volume change.

## Types of Settlement

**Immediate (elastic) settlement (S_i):** Occurs instantaneously upon loading. Elastic distortion without volume change in saturated clays (undrained). Significant in sands and gravels.

**Primary consolidation settlement (S_c):** Time-dependent volume change as excess pore pressure dissipates and effective stress increases. Dominant in clays and silts.

**Secondary compression (creep) (S_s):** Continued compression after primary consolidation is complete (excess pore pressure fully dissipated). Volume change at constant effective stress due to viscous rearrangement of soil skeleton.

Total settlement: S_total = S_i + S_c + S_s

## One-Dimensional Consolidation Theory (Terzaghi)

### Assumptions
1. Soil is homogeneous, fully saturated
2. Soil particles and water are incompressible
3. Flow is one-dimensional (vertical only)
4. Darcy's law is valid
5. Coefficient of permeability (k) and coefficient of volume compressibility (m_v) remain constant during each load increment
6. Strain is small

### Governing Equation
∂u/∂t = c_v × ∂²u/∂z²

This is a diffusion equation. The coefficient of consolidation c_v controls the rate of pore pressure dissipation.

## Compressibility Parameters

### From e-log σ' Plot (Oedometer Test)

**Compression index (C_c):** Slope of the virgin compression line (NCL) on e vs. log σ' plot.
C_c = -Δe / Δ(log σ')   (on the NCL)

**Recompression (swelling) index (C_r):** Slope of the unload-reload line.
C_r = -Δe / Δ(log σ')   (on the URL)

Typically C_r ≈ C_c/5 to C_c/10.

**Preconsolidation pressure (σ'_p):** Maximum past effective stress the soil has experienced. Determined from the e-log σ' curve using Casagrande's graphical construction:
1. Locate point of maximum curvature on the curve
2. Draw horizontal line and tangent line at this point
3. Bisect the angle between them
4. Extend the virgin line (NCL) upward
5. σ'_p = intersection of bisector with virgin line

### Alternative Parameters

**Coefficient of volume compressibility:**
m_v = Δε_v / Δσ' = (1/1+e₀) × Δe/Δσ'

**Constrained modulus:**
D = 1/m_v = Δσ'/Δε_v

**Modified compression index:**
C_cε = C_c / (1 + e₀)

These are stress-dependent — valid only over the stress range from which they are determined.

## Settlement Calculations

### Normally Consolidated Clay (σ'_v0 = σ'_p)

S_c = [C_c × H / (1 + e₀)] × log[(σ'_v0 + Δσ') / σ'_v0]

### Overconsolidated Clay — Case 1: σ'_v0 + Δσ' ≤ σ'_p

S_c = [C_r × H / (1 + e₀)] × log[(σ'_v0 + Δσ') / σ'_v0]

### Overconsolidated Clay — Case 2: σ'_v0 + Δσ' > σ'_p

S_c = [C_r × H / (1 + e₀)] × log[σ'_p / σ'_v0] + [C_c × H / (1 + e₀)] × log[(σ'_v0 + Δσ') / σ'_p]

## Time Rate of Consolidation

### Degree of Consolidation

U(t) = 1 - (u_avg(t) / u₀) = S(t) / S_∞

where u₀ = initial excess pore pressure, u_avg(t) = average excess pore pressure at time t, S(t) = settlement at time t, S_∞ = total primary consolidation settlement.

### Time Factor

T_v = c_v × t / H_dr²

where H_dr = length of drainage path (H for single drainage, H/2 for double drainage).

### U-T Relationships (Uniform Initial Excess Pore Pressure)

For U < 60%: T_v ≈ π/4 × U² (or U ≈ √(4T_v/π))
For U > 60%: T_v ≈ -0.933 × log(1 - U) - 0.085

Key values:
- U = 50%: T_v = 0.197
- U = 90%: T_v = 0.848
- U = 95%: T_v = 1.129

### Determining c_v from Test Data

**Log-time method (Casagrande):**
1. Plot dial reading vs. log(time) for a load increment
2. Locate d₀ (initial reading) and d₁₀₀ (end of primary, before secondary linear portion)
3. d₅₀ = (d₀ + d₁₀₀) / 2
4. Find t₅₀ from the plot
5. c_v = 0.197 × H_dr² / t₅₀

**Root-time method (Taylor):**
1. Plot dial reading vs. √time
2. Draw straight line through initial linear portion
3. Draw line at 1.15 × the slope
4. Intersection with curve gives √t₉₀
5. c_v = 0.848 × H_dr² / t₉₀

## Secondary Compression

After primary consolidation is complete (U → 100%), compression continues at a rate proportional to log(time):

S_s = C_αε × H × log(t₂/t₁)

where C_αε = secondary compression index = Δε / Δ(log t) measured from the linear portion of the dial vs. log(time) curve after primary consolidation.

C_αε = C_α / (1 + e_p) where C_α is the secondary compression index in terms of void ratio.

**Mesri's correlation:** C_α/C_c ≈ 0.04 ± 0.01 for most inorganic clays and silts. This means secondary compression is proportionally larger for more compressible soils.

For peats and organic soils: C_α/C_c ≈ 0.05–0.07 (higher secondary compression).
