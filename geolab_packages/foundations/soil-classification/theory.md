# Soil Classification Systems

## Overview

Soil classification provides a systematic framework for grouping soils with similar engineering behavior. Two primary systems are used in practice: the Unified Soil Classification System (USCS) and the AASHTO system. Both rely on grain size distribution and Atterberg limits as index properties.

## Unified Soil Classification System (USCS)

### Basis and Structure

Developed by Arthur Casagrande in the 1940s for airfield construction, later standardized as ASTM D2487. The system uses a two-letter symbol based on:

- **Primary descriptor**: Grain size dominance (G=gravel, S=sand, M=silt, C=clay, O=organic, Pt=peat)
- **Secondary descriptor**: Gradation for coarse-grained (W=well-graded, P=poorly-graded) or plasticity for fine-grained (L=low plasticity LL<50, H=high plasticity LL≥50)

### Classification Decision Framework

**Step 1 — Coarse vs. Fine**: Determine if more than 50% by weight is retained on the No. 200 sieve (0.075 mm). If yes → coarse-grained soil. If no → fine-grained soil.

**Step 2a — Coarse-Grained Soils**: Determine if more than 50% of the coarse fraction is retained on the No. 4 sieve (4.75 mm). If yes → Gravel (G). If no → Sand (S).

- If less than 5% fines: classify by gradation using Cu and Cc
  - Well-graded (W): Cu ≥ 4 for gravels (≥6 for sands) AND 1 ≤ Cc ≤ 3
  - Poorly-graded (P): fails either criterion
- If 5–12% fines: dual symbol required (e.g., SW-SM, GP-GC) based on plasticity of fines
- If more than 12% fines: classify by plasticity of fines
  - M suffix: fines plot below A-line or PI < 4
  - C suffix: fines plot above A-line and PI ≥ 7
  - If 4 ≤ PI ≤ 7 and plots near A-line: dual symbol (e.g., SC-SM)

**Step 2b — Fine-Grained Soils**: Plot liquid limit (LL) and plasticity index (PI) on Casagrande's plasticity chart.

- **A-line equation**: PI = 0.73 × (LL - 20)
- **U-line equation**: PI = 0.9 × (LL - 8) — approximate upper bound for natural soils
- Soils above A-line: Clay (C)
- Soils below A-line: Silt (M)
- L suffix if LL < 50; H suffix if LL ≥ 50
- CL-ML zone: 4 ≤ PI ≤ 7 and plots above A-line

**Step 3 — Organic Soils**: If LL (oven-dried) / LL (not dried) < 0.75, classify as organic (OL or OH). Highly organic soils (peat) classified as Pt by visual-manual identification.

### Dual-Symbol Rules

Dual symbols are required in two situations:
1. Coarse-grained soils with 5–12% fines (borderline gradation/plasticity)
2. Fine-grained soils plotting in the CL-ML zone (4 ≤ PI ≤ 7, above A-line)

Dual symbols always list the dominant characteristic first.

## AASHTO Classification System

### Basis and Structure

Developed for highway subgrade evaluation per AASHTO M 145. Soils are classified into groups A-1 through A-7, with subgroups. Uses grain size distribution, liquid limit, and plasticity index.

### Group Index

The Group Index (GI) provides a quantitative measure of subgrade quality:

GI = (F₂₀₀ - 35)[0.2 + 0.005(LL - 40)] + 0.01(F₂₀₀ - 15)(PI - 10)

where F₂₀₀ = percent passing No. 200 sieve.

- GI = 0: excellent subgrade
- GI ≥ 20: very poor subgrade
- Negative intermediate values are set to zero
- For A-2-6 and A-2-7 subgroups, only the second term is used

### Classification Procedure

Evaluate from left to right in the AASHTO classification table. The first group whose criteria are satisfied is the correct classification. General quality ranking: A-1 (excellent) → A-7 (poor).

**Granular materials** (≤35% passing No. 200): A-1, A-2, A-3
**Silt-clay materials** (>35% passing No. 200): A-4, A-5, A-6, A-7

## USCS vs. AASHTO Correlation

No direct one-to-one mapping exists. General relationships:
- A-1-a ↔ GW, GP; A-1-b ↔ SW, SP, SM, GM
- A-2 ↔ GM, GC, SM, SC (coarse with significant fines)
- A-3 ↔ SP (clean sand)
- A-4, A-5 ↔ ML, MH, OL
- A-6 ↔ CL
- A-7-5 ↔ MH, OH; A-7-6 ↔ CH

## Visual-Manual Classification (ASTM D2488)

Field classification procedure without laboratory testing. Uses visual estimation of grain sizes, manual tests for plasticity (thread rolling, toughness), dilatancy (shaking test), and dry strength. Results are approximate and should be confirmed by laboratory classification per D2487 for design purposes.

### Manual Tests for Fine-Grained Soils

- **Dilatancy (reaction to shaking)**: Rapid → silt; none/slow → clay
- **Dry strength**: None/low → silt; high/very high → clay
- **Toughness**: Low → silt; high → clay
- These three tests together reliably distinguish silt from clay behavior in the field
