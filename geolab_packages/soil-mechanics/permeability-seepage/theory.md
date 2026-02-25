# Permeability & Seepage

## Darcy's Law

The fundamental law governing fluid flow through porous media:

q = k × i × A

or in terms of discharge velocity: v = k × i

where q = flow rate, k = hydraulic conductivity (coefficient of permeability), i = hydraulic gradient (Δh/L), A = cross-sectional area of flow.

**Derivation basis:** Henri Darcy (1856) conducted experiments on water flow through sand filters in Dijon, France. He found that the flow rate is proportional to the head loss and inversely proportional to the length of flow path.

**Validity:** Darcy's law is valid for laminar flow (Re < 1–10 for porous media). It applies to virtually all natural groundwater flow conditions except in very coarse gravel, fractured rock with wide apertures, or near wells with very high velocities.

**Seepage velocity vs. discharge velocity:**
v_s = v / n = q / (A × n)

The actual velocity through voids (seepage velocity) is higher than the discharge velocity (superficial velocity) because water flows only through the void space.

## Hydraulic Conductivity

### Factors Affecting k
- **Void ratio:** k increases with e. For clays: log k is approximately linear with e.
- **Grain size:** k ∝ D₁₀² approximately (Hazen). Coarser soils = higher k.
- **Soil fabric/structure:** Flocculated > dispersed for same void ratio. Undisturbed > remolded.
- **Degree of saturation:** Unsaturated soils have much lower k than saturated.
- **Temperature:** Viscosity decreases with increasing temperature → k increases (~3% per °C). Correct to standard 20°C: k₂₀ = k_T × (μ_T/μ₂₀).
- **Anisotropy:** k_h typically 2–10× k_v for natural deposits (sometimes 100×+ for varved clays).

### Hazen's Equation (Empirical)
k = C × D₁₀²

where C ≈ 1.0 cm/s when D₁₀ is in cm (C ranges 0.4–1.5 depending on soil). Valid for clean, uniformly graded sands with 0.1 < D₁₀ < 3 mm and Cu < 5.

### Kozeny-Carman Equation (Semi-Theoretical)
k = (γ_w/μ) × [1/(C_k × S_s²)] × [e³/(1+e)]

Captures the dependence on void ratio through the e³/(1+e) term. More theoretically sound than Hazen but requires knowledge of specific surface area S_s and shape factor C_k.

## Equivalent Permeability of Layered Soils

**Horizontal flow (parallel to layers):**
k_h(eq) = Σ(k_i × H_i) / Σ(H_i)

Weighted average — dominated by the most permeable layer.

**Vertical flow (perpendicular to layers):**
k_v(eq) = Σ(H_i) / Σ(H_i/k_i)

Harmonic average — dominated by the least permeable layer.

This asymmetry (k_h >> k_v) is fundamental to understanding seepage in natural soil deposits and dam foundations.

## Flow Nets

A flow net is a graphical solution to the Laplace equation for 2D steady-state seepage through a homogeneous, isotropic medium.

**Construction rules:**
- Flow lines and equipotential lines intersect at right angles
- The shapes formed between adjacent flow lines and equipotential lines are approximate "squares" (same aspect ratio throughout)
- Boundary conditions: upstream/downstream heads are equipotential lines; impervious boundaries are flow lines; phreatic surface is a flow line where pressure head = 0

**Seepage quantity:**
q = k × H × (N_f / N_d)

where H = total head loss, N_f = number of flow channels, N_d = number of equipotential drops.

**Pore pressure at any point:**
u = γ_w × h_p

where h_p = pressure head at the point (total head minus elevation head, read from the flow net).

## Seepage Force and Critical Gradient

Water flowing through soil exerts a seepage force on the soil skeleton:

j = γ_w × i (seepage force per unit volume)

**Critical hydraulic gradient (quicksand condition):**
i_cr = (G_s - 1) / (1 + e) = γ'/γ_w

When the upward seepage force equals the submerged weight of the soil, effective stress becomes zero. For typical sands: i_cr ≈ 0.9–1.1. This is the "quicksand" condition — the soil behaves as a heavy fluid with no shear strength.

**Factor of safety against piping:**
FS = i_cr / i_exit

Design criteria: FS ≥ 3–5 for dam foundations (conservative because of the catastrophic consequences of piping failure).
