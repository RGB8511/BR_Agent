# In-Situ Testing (SPT, CPT, PMT, DMT)

## Standard Penetration Test (SPT)

### Description
A split-spoon sampler (51 mm OD, 35 mm ID) driven 450 mm (18 in) by a 63.5 kg (140 lb) hammer falling 760 mm (30 in). Blow count for last 300 mm (12 in) = N-value. The first 150 mm (6 in) is seating — not counted.

### Energy Correction
Measured N depends on hammer energy delivery. Standard reference: 60% theoretical energy (N₆₀).

N₆₀ = N × C_E × C_B × C_S × C_R

where C_E = energy ratio correction (auto-trip hammer ~1.0–1.2; safety hammer ~0.75; donut ~0.55–0.60), C_B = borehole diameter correction, C_S = sampler correction, C_R = rod length correction.

### Overburden Correction
For sand density/relative density correlations, normalize to 1 atm (100 kPa) effective overburden:

(N₁)₆₀ = N₆₀ × C_N

C_N = (P_a/σ'_v0)^0.5 ≤ 2.0 (Liao & Whitman 1986)

Alternative: C_N = 0.77 × log(2000/σ'_v0) for σ'_v0 in kPa (Peck, Hanson & Thornburn)

### SPT Correlations

**Relative density (Skempton 1986):**
D_r = [(N₁)₆₀ / (60 × OCR^0.18)]^0.5 (approximate for NC to lightly OC sands)

**Friction angle (Hatanaka & Uchida 1996):**
φ' = √(20 × (N₁)₆₀) + 20 (for sands)

**Undrained shear strength (rough correlation):**
s_u ≈ 4.5 × N₆₀ to 6.0 × N₆₀ (kPa) — very approximate, large scatter. Use CPT or vane for s_u.

**Settlement (Meyerhof 1965, Burland & Burbidge 1985):**
Various empirical methods for footings on sand using N₆₀.

## Cone Penetration Test (CPT / CPTu)

### Description
A standardized cone (60° apex, 35.7 mm diameter, 10 cm² base area) pushed into the ground at constant rate of 20 mm/s. Measures cone resistance (q_c), sleeve friction (f_s), and pore pressure (u₂ for CPTu) continuously with depth.

### Derived Parameters

**Corrected cone resistance:**
q_t = q_c + u₂(1 - a)

where a = net area ratio of cone (typically 0.70–0.85). Correction significant in clays.

**Normalized parameters (Robertson 2009):**
- Q_tn = [(q_t - σ_v0)/P_a] × (P_a/σ'_v0)^n (stress-normalized tip resistance)
- F_r = [f_s / (q_t - σ_v0)] × 100% (normalized friction ratio)
- B_q = (u₂ - u₀) / (q_t - σ_v0) (pore pressure ratio)

where n = stress exponent (~0.5 for sands, ~1.0 for clays; iterative with SBTn chart).

### Robertson SBTn Classification
Soil behavior type from Q_tn vs. F_r chart. Nine zones:
1. Sensitive fine-grained
2. Organic soils
3. Clays (clay to silty clay)
4. Silt mixtures (clayey silt to silty clay)
5. Sand mixtures (silty sand to sandy silt)
6. Sands (clean to silty)
7. Gravelly sand to dense sand
8. Very stiff sand to clayey sand (cemented/OC)
9. Very stiff fine-grained (cemented/OC)

### CPT Correlations

**Undrained shear strength:**
s_u = (q_t - σ_v0) / N_kt

N_kt = empirical cone factor, typically 10–18 (commonly ~14 for general use; should be calibrated locally).

**Effective friction angle (Robertson & Campanella 1983):**
φ' = arctan[0.1 + 0.38 × log(q_t/σ'_v0)] (for uncemented, unaged quartz sands)

**Relative density (Kulhawy & Mayne 1990):**
D_r = 100 × √[(q_t/P_a) / (305 × Q_c × OCR^0.18)]

where Q_c = compressibility factor (0.91 low, 1.0 moderate, 1.09 high compressibility sands).

**Constrained modulus (Robertson 2009):**
M = α_M × (q_t - σ_v0)

α_M varies with soil type (typically 2–8 for clays, 3–10 for sands).

## Pressuremeter Test (PMT)

### Description
A cylindrical probe expanded radially in a borehole. Measures pressure-volume relationship of the borehole wall. Pre-bored (Ménard) or self-boring (SBP) types.

### Key Parameters
- p_0: In-situ horizontal stress (lift-off pressure for SBP)
- p_L: Limit pressure (pressure at very large expansion)
- E_M: Ménard pressuremeter modulus (from reload curve slope)

**Bearing capacity (Ménard):**
q_u = q + k × (p_L - p_0) where k = bearing factor (depends on soil type, shape, depth).

**Settlement (Ménard):**
Uses E_M with empirical shape/rheological factors. E_M ≠ Young's modulus — it is specific to the PMT interpretation framework.

## Flat Dilatometer Test (DMT)

### Description
A flat blade (15 mm thick) pushed into ground. A thin membrane on one face is inflated; two pressures measured: A (lift-off/contact) and B (1.1 mm expansion).

### Key Parameters
- I_D = (p₁ - p₀) / (p₀ - u₀): Material index (clay < 0.6, silt 0.6–1.8, sand > 1.8)
- K_D = (p₀ - u₀) / σ'_v0: Horizontal stress index (K_D = 2 for NC)
- E_D = 34.7 × (p₁ - p₀): Dilatometer modulus

### Correlations
- K₀ = (K_D/1.5)^0.47 - 0.6 (Marchetti 1980)
- OCR = (0.5 × K_D)^1.56 (Marchetti 1980)
- M (constrained modulus) = R_M × E_D where R_M = f(I_D, K_D)
- φ' ≈ 28° + 14.6 × log K_D - 2.1 × (log K_D)² (for sands)
