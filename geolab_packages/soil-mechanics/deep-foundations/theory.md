# Deep Foundations (Piles & Drilled Shafts)

## Overview

Deep foundations transfer loads through weak or compressible surface soils to stronger strata at depth. Two primary types:
- **Driven piles:** Steel H-piles, pipe piles, precast concrete, timber — installed by impact or vibratory driving
- **Drilled shafts (bored piles/caissons):** Cast-in-place concrete in drilled holes, typically 0.5–3+ m diameter

## Ultimate Capacity — Static Analysis

Total ultimate capacity:
Q_u = Q_s + Q_b = (Σ f_s × A_s) + q_b × A_b

where Q_s = shaft (skin) resistance, Q_b = base (tip) resistance, f_s = unit shaft friction, A_s = shaft surface area per layer, q_b = unit base resistance, A_b = base area.

## Shaft Resistance in Clay — α-Method (Total Stress)

f_s = α × s_u

where α = adhesion factor, s_u = undrained shear strength.

**α selection (API, Tomlinson):**
- s_u < 25 kPa: α = 1.0
- 25 < s_u < 70 kPa: α = 1.0 to 0.5 (decreasing)
- s_u > 70 kPa: α ≈ 0.5 (or lower for very stiff clays)

**O'Neill & Reese (1999) for drilled shafts:**
α = 0.55 for s_u/P_a ≤ 1.5
α = 0.55 - 0.1(s_u/P_a - 1.5) for 1.5 < s_u/P_a ≤ 2.5

## Shaft Resistance — β-Method (Effective Stress)

f_s = β × σ'_v = K × σ'_v × tanδ

where β = K × tanδ, K = lateral earth pressure coefficient, δ = pile-soil interface friction angle.

For NC clays: β ≈ (1 - sinφ') × tanφ' ≈ 0.25–0.35
For OC clays: β increases with OCR: β = (1 - sinφ') × OCR^sinφ' × tanφ'
For sands: β = K × tanδ where K ≈ 0.7–1.0 for driven piles, 0.5–0.7 for drilled shafts

β typically ranges 0.2–0.6 for clays, 0.3–1.2 for sands. β generally decreases with depth for long piles (limiting shaft friction concept — debated but commonly applied).

## Base Resistance

**Clay (undrained):** q_b = N_c × s_u = 9 × s_u (for D/B > 4; N_c = 9 is standard)

**Sand (Meyerhof):** q_b = N_q × σ'_v (limited to q_b,max)
- N_q from Meyerhof's charts or tables (function of φ')
- Limiting q_b to prevent unrealistic values at depth

**Drilled shafts in rock (O'Neill & Reese):**
q_b = N_cr × q_u(rock) where N_cr depends on RQD and joint spacing (typically 1.0–3.0 for competent rock)

## SPT-Based Methods

**Meyerhof (1976) for driven piles:**
q_b = 400 × N₆₀ × (D_b/D) ≤ 400 × N₆₀ (kPa)
f_s = 2 × N₆₀ (kPa) for displacement piles in sand

**FHWA method for drilled shafts in sand:**
f_s = β × σ'_v with β from SPT correlations
q_b from SPT with limiting values

## CPT-Based Methods

**De Ruiter & Beringen (1979):** Direct use of q_c for both q_b and f_s
**LCPC/LPC (Bustamante & Gianeselli 1982):** q_b = k_c × q_ca where k_c = bearing factor, q_ca = average q_c near tip
**UniCone (Eslami & Fellenius):** Uses effective cone resistance q_E = q_t - u₂

## Group Effects

**Efficiency:** η = Q_group / (n × Q_single)
- Driven piles in sand: η ≥ 1.0 (densification from driving)
- Driven piles in clay: η < 1.0 for close spacing
- Drilled shafts: η ≤ 1.0

**Block failure:** For closely spaced piles in clay, check block failure mode where the group acts as a single large foundation. Q_block = 2(B_g + L_g) × D × s_u + N_c × s_u × B_g × L_g

**Settlement:** Group settlement > single pile settlement. Use 2:1 distribution or Poulos charts. Equivalent raft method: treat group as a loaded area at 2/3 pile length, compute settlement of underlying layers.

## Negative Skin Friction (Downdrag)

When soil adjacent to the pile settles more than the pile (consolidating fill, rising WT), skin friction acts downward, adding load rather than providing resistance.

**Neutral plane:** Depth where pile settlement = soil settlement. Above: negative skin friction (load). Below: positive skin friction (resistance).

Design approach: Add dragload to applied loads; check structural capacity and settlement at neutral plane. Do NOT add dragload for geotechnical capacity check — it is a serviceability/structural issue.

## Lateral Loading

**p-y method:** Model pile as a beam on nonlinear springs (p-y curves). Each spring defined by soil type and depth. Standard p-y curves: Matlock (1970) for soft clay, Reese et al. (1975) for sand, API RP 2A.

Solved using finite difference or finite element beam analysis (LPILE, RSPile, or similar).

Key outputs: deflection, moment, and shear distribution along pile. Design typically governed by deflection limits rather than ultimate lateral capacity.
