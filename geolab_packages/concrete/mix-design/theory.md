# Concrete Mix Design

## Objectives

Mix design selects proportions of cement, water, aggregates, admixtures, and SCMs to achieve target properties: strength, workability, durability, and economy. The fundamental principle: concrete properties are controlled primarily by the water-to-cementitious materials ratio (w/cm).

## Abrams' Law

f'c = A / B^(w/c)

where A and B are empirical constants depending on age, cement type, and curing. The relationship is approximately: as w/c decreases, strength increases. Valid for fully compacted concrete.

**Practical range:** w/c from 0.25 (very high strength, needs superplasticizer) to 0.65 (low strength, high permeability). Most structural concrete: 0.40–0.55.

## ACI 211.1 Mix Design Procedure

### Step 1 — Select Slump
Based on type of construction and placement method. If not specified:
- Footings, caissons: 25–75 mm (1–3 in)
- Walls, columns: 25–100 mm (1–4 in)
- Slabs, beams: 25–75 mm (1–3 in)
- Mass concrete: 25–50 mm (1–2 in)

### Step 2 — Select Maximum Aggregate Size
Largest practical size that fits structural constraints: ≤ 1/5 narrowest form dimension, ≤ 3/4 clear spacing between bars, ≤ 1/3 slab depth. Larger aggregate → less water → less cement → economy + less shrinkage.

### Step 3 — Estimate Water Content and Air Content
Water content depends on slump, max aggregate size, and whether air-entrained. From ACI 211.1 Table 6.3.3.

Air content: non-air-entrained for interior concrete; air-entrained for freeze-thaw exposure (4–7% total air depending on max aggregate size and exposure severity).

### Step 4 — Select w/cm Ratio
Based on required strength and durability. Lower of:
- Strength requirement (from Table 6.3.4a): e.g., f'c = 28 MPa → w/c ≤ 0.53 (non-AE) or 0.46 (AE)
- Durability requirement: exposure class dictates maximum w/cm (e.g., 0.45 for freeze-thaw, 0.40 for sulfate exposure per ACI 318 Table 19.3.2)

### Step 5 — Calculate Cement Content
Cement (kg/m³) = Water content / (w/cm)

Check against minimum cement content for durability if specified.

### Step 6 — Estimate Coarse Aggregate Volume
From ACI 211.1 Table 6.3.6 based on fineness modulus (FM) of fine aggregate and max aggregate size. Expressed as fraction of dry-rodded unit weight.

### Step 7 — Estimate Fine Aggregate
By absolute volume method: Fine aggregate volume = 1.0 m³ - (volumes of water, cement, coarse aggregate, air, SCMs).

### Step 8 — Adjust for Moisture
Aggregates carry moisture — adjust water and aggregate weights for absorption and surface moisture.

## Absolute Volume Method

Total volume = 1.0 m³ = V_cement + V_water + V_CA + V_FA + V_air + V_SCM + V_admixture

V_material = Mass / (SG × ρ_water)

This is the fundamental calculation. All materials occupy real volume.

## Air Entrainment

Air-entrained concrete contains microscopic, well-distributed air bubbles (10–1000 μm) that provide:
- Freeze-thaw resistance (critical — most important durability feature in cold climates)
- Improved workability (ball-bearing effect)
- Reduced bleeding and segregation

**Spacing factor (L̄):** Maximum distance from any point in paste to nearest air bubble. L̄ ≤ 0.20 mm (0.008 in) required for freeze-thaw durability. Measured by ASTM C457 (linear traverse or modified point count on hardened concrete).

**Strength penalty:** Each 1% air ≈ 2–6% strength reduction. Air-entrained concrete at a given w/cm is weaker than non-air-entrained.

## Admixtures

**Water reducers (ASTM C494 Type A):** Reduce water 5–10% at same slump. Lignosulfonates.

**Mid-range water reducers (Type A modified):** Reduce water 8–15%.

**High-range water reducers / superplasticizers (Type F, G):** Reduce water 12–30+%. Polycarboxylate ethers (PCE) are the modern standard. Essential for high-strength and self-consolidating concrete.

**Retarders (Type B, D):** Delay setting. Hot weather, long hauls, mass pours.

**Accelerators (Type C, E):** Speed setting and early strength. Calcium chloride (not for reinforced — promotes corrosion) or non-chloride accelerators.

**Air-entraining agents (ASTM C260):** Surfactants that stabilize micro-bubbles. Dosage adjusted to achieve target air content.

## Trial Batches

Mix design is always verified by trial batches. Adjust proportions based on actual slump, air content, unit weight, and strength. Minimum 3 cylinders per batch, tested at target age.

## Required Average Strength (f'cr)

Design requires f'cr > f'c to account for variability:
- f'cr = f'c + 1.34s (when s is known, ≤ 35 MPa)
- f'cr = f'c + 2.33s - 3.45 (alternative, ≤ 35 MPa)
Use larger value. s = standard deviation of prior test results.

When no data: f'cr = f'c + 8.3 MPa (for f'c ≤ 21 MPa) or f'cr = 1.1f'c + 5.0 (for f'c > 35 MPa).
