# Concrete Gravity Dam Design

## Principle

A gravity dam resists applied loads primarily by its own weight. The dam's mass generates sufficient friction on the foundation to resist sliding, and sufficient stabilizing moment to resist overturning. The cross-section is typically triangular, with a vertical or near-vertical upstream face and a sloped downstream face (0.7H:1V to 0.8H:1V typical).

## Loading Conditions

### Normal (Usual) Loading
- Headwater at normal maximum pool
- Tailwater at corresponding normal level
- Uplift with drainage system operational
- Dead load (dam weight)
- Silt/sediment pressure
- Ice pressure (if applicable)
- Temperature loads

### Unusual Loading
- Headwater at flood control pool or routed IDF level
- One drain gallery inoperative (for redundancy check)
- Post-earthquake condition with cracked base

### Extreme Loading
- Maximum credible earthquake (MCE) — pseudostatic or dynamic
- PMF passage with maximum pool
- Full uplift (drains inoperative)

## Stability Analysis — Gravity Method

The gravity method analyzes each horizontal section of the dam (typically the base and any construction joints) as a rigid body. Applicable to straight gravity dams where the section is representative of the full monolith width.

### Sliding Stability

The dam must resist sliding along the base or any horizontal plane.

**Shear-friction factor of safety:**
FS_sliding = (cA + (ΣN - U) × tan(φ)) / ΣT

where c = cohesion at the contact (concrete-rock or concrete-concrete), A = area of contact, ΣN = sum of normal forces (weight, vertical water pressure components), U = uplift force, φ = friction angle of contact, ΣT = sum of tangential (horizontal) driving forces.

**Required FS:**
- Usual loading: FS ≥ 3.0 (USBR), ≥ 2.0 (USACE)
- Unusual: FS ≥ 2.0 (USBR), ≥ 1.7 (USACE)
- Extreme: FS ≥ 1.0 (both) — "greater than 1.0" required

Note: USBR and USACE use slightly different definitions. USACE separates "sliding factor of safety" (limit equilibrium) from "shear-friction factor of safety."

### Overturning Stability

Sum moments about the downstream toe:

FS_overturning = Σ(Stabilizing moments) / Σ(Overturning moments)

Stabilizing: dam weight × arm, tailwater pressure × arm, vertical water pressure on sloped faces.
Overturning: headwater pressure × arm, uplift × arm, silt pressure × arm, seismic forces.

**Required FS:**
- Usual: FS ≥ 1.5 (typical)
- Unusual: FS ≥ 1.25
- Extreme: FS ≥ 1.0

Modern practice also checks the location of the resultant force — it should fall within the middle third of the base (no tension in usual loading) or at minimum within the base width (extreme loading).

### Base Stress Analysis

Assuming linear distribution of normal stress at the base:

σ = (ΣV/A) × [1 ± (6e/B)]

where ΣV = total vertical force, A = base area per unit width, e = eccentricity of resultant from center of base, B = base width.

**Criteria:**
- No tension on upstream face under usual loading (resultant in middle third)
- Maximum compressive stress < allowable for foundation rock and concrete
- For extreme loading, tension may be acceptable if it doesn't propagate a crack that destabilizes the section

### Uplift Pressure

Water pressure acts upward on the base of the dam through foundation joints and pores. Reduces effective normal force, decreasing sliding resistance.

**Without drains:** Linear distribution from full headwater pressure at the heel (upstream) to tailwater pressure at the toe (downstream).

**With drains:** Reduced uplift at the drain line. USBR assumes drain effectiveness of 2/3 (pressure at drain = tailwater + 1/3(headwater - tailwater)). USACE uses similar but with different drain effectiveness factors depending on drain spacing and proximity to grout curtain.

**Cracked base:** If tension is computed at the upstream face, assume the crack is full of reservoir pressure. Uplift recalculated with full headwater pressure extending to the crack tip, then drained reduction beyond the crack. Iterate until crack length is stable.

## Foundation Treatment

### Excavation
Remove weathered and fractured rock to expose competent foundation. Rock quality assessed by RQD, core recovery, geologic mapping. Dental concrete fills irregularities and overexcavated areas.

### Grout Curtain
A single or multiple rows of grout holes drilled from the dam gallery into the foundation along the upstream face. Cement grout injected under pressure to seal joints and reduce seepage. Depth: typically 30–60% of reservoir head, or to a defined low-permeability zone.

### Foundation Drains
Drilled downstream of the grout curtain, typically from the dam gallery. Reduce uplift pressure to the design assumptions. Drain spacing: 3–6 m (10–20 ft) typical. Must be maintained (flushed/redrilled periodically) to remain effective.

## Roller-Compacted Concrete (RCC) Gravity Dams

RCC is a dry, zero-slump concrete placed and compacted by vibratory rollers in horizontal lifts (typically 300 mm / 12 in thick). Construction is rapid — essentially earth-moving equipment places concrete.

**Advantages:** 30–50% cost savings over conventional concrete. Very rapid construction. No formwork for the dam body. Excellent for stepped spillway integration.

**Disadvantages:** Lift joints are potential seepage and sliding planes. Requires careful curing and joint treatment. Mix design requires optimization of paste volume for workability.

**Design:** Same gravity stability analysis. Pay special attention to lift joint shear strength (cohesion is lower than intact concrete — c = 0.5–1.5 MPa, φ = 45°–55° for well-prepared joints). Upstream face may be conventional concrete for impermeability, or use geomembrane.

## Thermal Analysis

Mass concrete generates significant heat from cement hydration. Thermal cracking occurs when tensile stresses from differential cooling exceed tensile strength.

**Peak temperature:** Occurs 3–7 days after placement. Temperature rise ≈ 10–15°C per 100 kg/m³ cement content.

**Thermal contraction:** As concrete cools to ambient, it contracts. If restrained (by foundation or adjacent placements), tensile stresses develop.

**Control measures:** Low-heat cement (Type II/IV), high SCM content (fly ash, slag), pre-cooling of aggregates and mix water, post-cooling with embedded cooling pipes, transverse contraction joints (typically every 15–20 m), placement in lifts with intervals between adjacent blocks.
