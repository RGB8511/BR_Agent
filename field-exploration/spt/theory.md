# Standard Penetration Test (SPT)

## Test Procedure

The SPT is the most widely performed in-situ test worldwide. A split-spoon sampler (51 mm OD, 35 mm ID, 610 mm long) is driven into the soil at the bottom of a borehole by a 63.5 kg (140 lb) hammer falling 760 mm (30 in).

**Procedure (ASTM D1586):**
1. Clean borehole to test depth. Minimize disturbance to bottom of hole.
2. Lower sampler to bottom of borehole on drill rods.
3. Drive sampler 450 mm (18 in) in three 150 mm (6 in) increments.
4. Record blows for each 150 mm increment.
5. First 150 mm = seating drive (discarded — disturbed zone at bottom).
6. N-value = sum of blows for second and third 150 mm increments (last 300 mm = 12 in).
7. If 50 blows reached in any 150 mm increment, or 100 blows total, record refusal.
8. Recover sampler, extract split-spoon sample for classification and logging.

## Raw N-Value Limitations

The raw field N-value is affected by many factors beyond soil properties: hammer type and energy, borehole diameter, rod length, sampler condition (with or without liner), and overburden pressure. To compare N-values between different borings, sites, or reference correlations, corrections are essential.

## Energy Corrections

### Hammer Energy Ratio
The theoretical free-fall energy is 63.5 kg × 9.81 m/s² × 0.76 m = 474 J. Actual delivered energy varies by hammer type:

- **Automatic trip hammer:** 80–100% efficiency (ER ≈ 80–95%). Modern standard — most consistent.
- **Safety hammer (rope & cathead):** 55–70% efficiency (ER ≈ 60%). Historically most common in US. Highly operator-dependent.
- **Donut hammer (rope & cathead):** 30–60% efficiency (ER ≈ 45%). Common historically outside US (Japan, S. America). Very inconsistent.

### N₆₀ — Energy-Corrected N-Value
All modern correlations are referenced to 60% energy ratio:

N₆₀ = N_field × (ER/60)

where ER = actual energy ratio of the hammer system as a percentage.

### Full Correction to (N₁)₆₀
For correlations involving effective overburden stress (liquefaction, relative density):

(N₁)₆₀ = N_field × C_E × C_B × C_S × C_R × C_N

where C_E = energy correction, C_B = borehole diameter, C_S = sampler liner, C_R = rod length, C_N = overburden pressure.

## Overburden Correction (C_N)

SPT blow count increases with confining pressure. To normalize to a reference stress (typically 1 atm = 100 kPa):

C_N = (Pa / σ'v)^n

where n = 0.5 (Liao & Whitman 1986) or various other forms. Maximum C_N typically capped at 1.7–2.0.

## Correlations

### Sand — Relative Density
Dr (%) ≈ function of (N₁)₆₀ and σ'v. Numerous correlations (Meyerhof, Skempton, Cubrinovski & Ishihara). Approximate: Dr(%) ≈ √((N₁)₆₀ / Cd) × 100 where Cd ≈ 40–60.

### Sand — Friction Angle
φ' related to (N₁)₆₀ through various correlations (Hatanaka & Uchida 1996, Schmertmann 1975). Approximate range: N₆₀ = 10 → φ' ≈ 30°; N₆₀ = 30 → φ' ≈ 36°; N₆₀ = 50 → φ' ≈ 40°.

### Clay — Undrained Shear Strength
Su/Pa ≈ 0.06 × N₆₀ (Stroud 1975, for stiff clays with PI ≈ 15–30)
Su ≈ 4.4 × N₆₀ kPa (Terzaghi & Peck, approximate, low reliability)

SPT is NOT recommended for undrained strength of soft to medium clays — use vane shear, CPT, or laboratory tests instead.

### Liquefaction Triggering
(N₁)₆₀ is a primary input to simplified liquefaction triggering analysis (Seed & Idriss 1971, updated by Youd et al. 2001, Boulanger & Idriss 2014). CSR vs. (N₁)₆₀ curves define boundary between liquefaction and no liquefaction for a given earthquake magnitude and fines content.
