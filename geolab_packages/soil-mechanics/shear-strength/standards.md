# Standards Reference — Shear Strength

## ASTM D2850 — Standard Test Method for Unconsolidated-Undrained Triaxial Compression Test on Cohesive Soils (UU)

**Scope:** Quick undrained shear strength (s_u) of cohesive soils without consolidation or drainage.

**Procedure:** Apply confining pressure (no consolidation). Shear at ~1%/min strain rate with no drainage. Minimum 3 specimens at different confining pressures.

**Key Notes:**
- For saturated clays, Mohr circles should have same diameter (φ_u = 0). If circles vary significantly → partial saturation or soil variability.
- Cell pressure should approximate field stress conditions but does not affect s_u for truly saturated soil.
- No pore pressure measurement required (but B-check recommended to verify saturation).
- Sample quality critical — trimming must be done carefully.

## ASTM D4767 — Standard Test Method for Consolidated Undrained Triaxial Compression Test for Cohesive Soils (CU)

**Scope:** CU triaxial with pore pressure measurement. Provides effective stress parameters (c', φ') and total stress parameters.

**Procedure:**
1. Backpressure saturate (B ≥ 0.95)
2. Consolidate isotropically (or anisotropically for CK₀U) to desired effective stress
3. Shear undrained while measuring pore pressure
4. Minimum 3 specimens at different consolidation pressures

**Key Notes:**
- Most commonly specified triaxial test for design
- Effective stress failure envelope from Mohr circles plotted in terms of effective stress
- Strain rate: typically 0.5–1.0 %/hr for clays (must be slow enough for uniform pore pressure equalization)
- Specimen typically 71 mm dia × 142 mm height (2.8 × 5.6 in) — H/D = 2:1
- Rubber membrane corrections may be needed at large strains

## ASTM D7181 — Standard Test Method for Consolidated Drained Triaxial Compression Test for Soils (CD)

**Scope:** Drained triaxial with volume change measurement. Directly provides c', φ'.

**Key Notes:**
- Shearing rate must be slow enough to prevent excess pore pressure: typically calculate from c_v and specimen size
- For clays: may require days to weeks per specimen
- Volume change measured by burette or volume change device
- Provides stress-dilatancy relationship for granular soils
- Less common than CU for clays due to time requirements

## ASTM D3080 — Standard Test Method for Direct Shear Test of Soils Under Consolidated Drained Conditions

**Scope:** Shear strength along a horizontal plane under controlled normal stress.

**Procedure:** Apply normal stress, allow consolidation, shear at specified rate. Repeat at 3+ normal stresses.

**Key Notes:**
- Displacement rate: typically 0.005–0.1 mm/min (depends on soil type and drainage)
- Specimen size: typically 60 × 60 mm or 100 × 100 mm square boxes
- Maximum particle size ≤ 1/10 of specimen width
- For residual strength: multiple reversals (forward-reverse-forward) until constant τ
- Interface testing: lower box filled with structural material (concrete, steel, geosynthetic)

## ASTM D6528 — Standard Test Method for Consolidated Undrained Direct Simple Shear Testing of Fine-Grained Soils

**Scope:** DSS test simulates K₀-consolidated, undrained loading with rotation of principal stresses. More representative of field conditions for many stability problems than triaxial.

**Key Notes:**
- Wire-reinforced membrane or stacked rings maintain K₀ condition during consolidation
- Provides s_u at K₀ condition (intermediate between triaxial compression and extension)
- Used for SHANSEP determination when anisotropy matters
- Specimen is short disk (~20 mm height × 70 mm diameter) for uniform shear

## ASTM D2573 — Standard Test Method for Field Vane Shear Test in Saturated Fine-Grained Soils

**Scope:** In-situ measurement of s_u in soft to medium clays.

**Key Notes:**
- Standard vane: 65 mm dia × 130 mm height (H/D = 2)
- Insert vane at least 5 diameters below bottom of borehole to avoid disturbance
- Rotation rate: 0.1°/s (6°/min)
- After peak, rotate 10+ full turns for remolded strength → sensitivity
- Apply Bjerrum correction factor for design
- Not valid for stiff clays, silts with sand, or soils with shells/gravel
