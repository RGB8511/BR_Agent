# Phase Relationships & Index Properties

## The Phase Diagram

Soil is a three-phase system: solid particles, water, and air. The phase diagram represents these as separate blocks with known volume and mass relationships.

```
  |---------|
  |   Air   |  V_a     M_a ≈ 0
  |---------|
  |  Water  |  V_w     M_w
  |---------|
  | Solids  |  V_s     M_s
  |---------|
```

Total volume: V = V_s + V_w + V_a = V_s + V_v (where V_v = V_w + V_a is void volume)
Total mass: M = M_s + M_w (air mass negligible)

## Fundamental Volume Relationships

### Void Ratio (e)
e = V_v / V_s

The ratio of void volume to solid volume. Range: 0.4–0.9 for sands, 0.5–4+ for clays. Unlike porosity, e can exceed 1.0 for very loose or highly compressible soils. Void ratio is preferred in geotechnical engineering because V_s remains constant during consolidation.

### Porosity (n)
n = V_v / V

The ratio of void volume to total volume. Always less than 1.0.

**Relationship:** n = e / (1 + e) and e = n / (1 - n)

### Degree of Saturation (S)
S = V_w / V_v

Ranges from 0 (completely dry) to 1.0 (fully saturated). Below the water table, S = 1.0 for practical purposes. In the capillary zone above the water table, S can be high but < 1.0.

## Fundamental Mass Relationships

### Moisture Content (w)
w = M_w / M_s

The ratio of water mass to dry solid mass. Expressed as a percentage. Can exceed 100% for highly organic or very soft clays. The single most commonly measured property in geotechnical engineering.

### Specific Gravity of Soil Solids (G_s)
G_s = ρ_s / ρ_w

The ratio of soil solid density to water density. Most mineral soils: G_s = 2.60–2.80. Quartz ≈ 2.65, feldspars ≈ 2.55–2.70, clay minerals ≈ 2.60–2.90, iron-rich minerals ≈ 3.0–5.0. Organic soils can have G_s < 2.0.

## Unit Weight Relationships

All derivable from the phase diagram using e, G_s, S, and w:

### Total (Bulk) Unit Weight
γ = (G_s + Se)γ_w / (1 + e)

Or equivalently: γ = γ_d(1 + w)

### Dry Unit Weight
γ_d = G_s × γ_w / (1 + e)

The weight of solids per unit total volume. Used for compaction control.

### Saturated Unit Weight (S = 1.0)
γ_sat = (G_s + e)γ_w / (1 + e)

### Submerged (Buoyant) Unit Weight
γ' = γ_sat - γ_w = (G_s - 1)γ_w / (1 + e)

Used for effective stress calculations below the water table.

### Unit Weight of Water
γ_w = 9.81 kN/m³ = 62.4 lb/ft³

## Key Interrelationships

### The Phase Relationship Identity
Se = wG_s

This single equation connects all phase quantities. Given any two of (S, e, w, G_s), the third can be computed.

**Derivation:** From definitions:
- V_w = S × V_v = S × e × V_s
- M_w = ρ_w × V_w = ρ_w × Se × V_s
- w = M_w/M_s = (ρ_w × Se × V_s) / (G_s × ρ_w × V_s) = Se/G_s
- Therefore: Se = wG_s ∎

### At Full Saturation (S = 1)
e = wG_s → w_sat = e/G_s

## Zero Air Voids Line

The zero air voids (ZAV) dry unit weight represents the theoretical maximum dry density at a given moisture content when S = 1.0:

γ_zav = G_s × γ_w / (1 + wG_s)

This defines the upper boundary on a compaction curve. No soil can exist above the ZAV line — it would require negative air volume.

## Relative Density

For granular soils, relative density D_r relates the in-situ void ratio to the maximum and minimum void ratios:

D_r = (e_max - e) / (e_max - e_min)

Or in terms of dry unit weight:

D_r = [(γ_d - γ_d,min) / (γ_d,max - γ_d,min)] × [γ_d,max / γ_d]

- D_r = 0%: loosest state (e = e_max)
- D_r = 100%: densest state (e = e_min)
- D_r < 35%: loose; 35–65%: medium; 65–85%: dense; > 85%: very dense

Relative density is meaningful only for cohesionless soils with less than ~15% fines.
