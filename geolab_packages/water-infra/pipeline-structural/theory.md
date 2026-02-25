# Pipeline Structural Design — External Loads & Bedding

## Classification: Rigid vs. Flexible Pipe

**Rigid pipe:** Resists external loads primarily through the structural strength of the pipe wall. Concrete, reinforced concrete, vitrified clay, asbestos-cement. Failure mode: cracking/fracture. Design based on D-load (three-edge bearing strength) modified by bedding factor.

**Flexible pipe:** Deforms under external load, mobilizing side support from surrounding soil to resist loading. Steel, DIP, HDPE, PVC, GRP. Failure mode: excessive deflection or buckling. Design based on deflection limits (Iowa formula).

The classification depends on relative stiffness: pipe is "flexible" when it deforms significantly enough to mobilize passive soil resistance.

## Earth Loads on Buried Pipe

### Marston Theory — Trench Condition
For pipe installed in a trench dug into undisturbed soil:

W_d = C_d × γ × B_d²

where C_d = load coefficient depending on H/B_d and soil friction, γ = unit weight of backfill, B_d = trench width at pipe crown.

**Key insight:** Friction between backfill and trench walls reduces the load below the full prism weight. Narrower trench = less load (up to a point — transition width where prism load governs).

### Marston Theory — Embankment Condition
For pipe under embankment fill (positive projecting):

W_c = C_c × γ × D²

where C_c depends on H/D and settlement ratio (ratio of settlement of backfill adjacent to pipe vs. the embankment above). Positive projection: pipe projects above natural ground. Load can exceed prism weight due to negative arching if pipe is stiffer than surrounding fill.

### Prism Load (Simplified)
For very deep burial or wide trench, the load approaches the simple prism weight:

W_prism = γ × H × D_o

This is conservative for trench installations but may underestimate embankment loads on rigid pipe.

## Live Loads (Traffic)

### AASHTO HL-93 (Highway)
Design truck (HS-20 equivalent): 72 kN (16 kip) wheel load. Impact factor applied for shallow cover. Load spread through soil at approximately 1.75H:1V. At depths > 2.4 m (8 ft), live load becomes negligible compared to earth load.

### Cooper E-80 (Railroad)
Much heavier than highway: 142 kN (32 kip) wheel load per rail. Requires deeper burial or stronger pipe class. Impact factor significant at shallow depth. At depths > 9 m (30 ft), railroad live load becomes negligible.

### Aircraft Loading (FAA)
Depends on aircraft type and gear configuration. Critical near runways and taxiways. FAA AC 150/5320-5D provides guidance.

## Flexible Pipe Design

### Modified Iowa Formula (Spangler-Watkins)
Predicts horizontal deflection of flexible pipe under external loads:

Δx = (D_L × K × W_c) / (EI/r³ + 0.061 × E'_s)

where D_L = deflection lag factor (1.0–1.5), K = bedding constant (0.1 for standard), W_c = load per unit length, EI/r³ = pipe stiffness, E'_s = modulus of soil reaction.

**Deflection limits:**
- Steel pipe: 2–5% of diameter (AWWA M11)
- DIP: 3% (AWWA C150)
- PVC: 5% (AWWA M23)
- HDPE: 5–7.5% (short-term), 5% long-term (AWWA M55)

### Soil Modulus (E's)
The most critical and uncertain parameter. Depends on:
- Native soil stiffness
- Backfill material and compaction level
- Pipe zone geometry (haunch, bedding, cover)

**Typical values:** Dumped sand: 2–7 MPa. Compacted granular: 7–21 MPa. Well-compacted crushed stone: 21–35 MPa.

### Buckling Resistance
For flexible pipe under external pressure (groundwater + vacuum):

q_cr = 32 × R_w × B' × E's × (EI/D³)

where R_w = water buoyancy factor, B' = empirical coefficient. Safety factor ≥ 2.0 against buckling.

## Rigid Pipe Design

### Three-Edge Bearing Strength (D-Load)
Rigid pipe is tested in the three-edge bearing configuration (worst-case point loading). Strength expressed as D-load: force per unit length per unit diameter to produce specified crack width.

### Bedding Factor (B_f)
The installed pipe performs better than the three-edge bearing test because the bedding distributes the load:

D_load_required = W_total / (B_f × D)

where W_total = earth load + live load, B_f = bedding factor (1.1 for flat bottom to 4.8 for Class A concrete cradle).

**ASCE Standard Installation Direct Design (SIDD):** Modern approach replacing Marston-Spangler for rigid pipe. Uses finite element analysis to develop installation-specific load distributions. Four standard installation types with defined bedding and compaction requirements.

## Pipe Zone Terminology and Bedding Classes

**Foundation:** Undisturbed material below the pipe.
**Bedding:** Shaped support directly under the pipe barrel. Provides uniform support.
**Haunch:** Material placed and compacted in the lower quarter of the pipe (critical zone for flexible pipe support).
**Initial backfill:** Material from pipe invert to 150–300 mm above crown.
**Final backfill:** Material above initial backfill to ground surface.

**Bedding classes (traditional ASCE):**
- Class A: Concrete cradle or arch (B_f = 2.8–4.8). Used under extreme loads.
- Class B: Shaped granular bedding with compacted fill to springline (B_f = 1.9–2.5).
- Class C: Shaped subgrade with granular bedding, moderate compaction (B_f = 1.5–2.0).
- Class D: Flat bottom, minimal preparation (B_f = 1.1). Not recommended for most applications.

## Thrust Blocks and Anchorage

At bends, tees, and dead ends, unbalanced pressure forces require external restraint. This is covered in the pipeline-design package. From a structural perspective, the thrust block must be sized for the soil bearing capacity and placed against undisturbed soil.
