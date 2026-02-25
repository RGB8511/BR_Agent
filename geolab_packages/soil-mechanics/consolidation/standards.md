# Standards Reference — Consolidation

## ASTM D2435 — Standard Test Methods for One-Dimensional Consolidation Properties of Soils Using Incremental Loading

**Scope:** Incremental load (IL) oedometer test to determine consolidation properties: C_c, C_r, σ'_p, c_v, C_α.

**Procedure:**
1. Trim undisturbed specimen into rigid ring (typically 63.5 mm dia × 25.4 mm height)
2. Apply seating load, then double stress each increment (LIR = 1): 12.5, 25, 50, 100, 200, 400, 800, 1600 kPa (typical)
3. Each increment maintained 24 hours (standard) or until EOP (end of primary)
4. Record dial gauge vs. time for each increment
5. Unload in stages, then may reload
6. Remove specimen, determine final water content and dry mass

**Data Reduction:**
- Plot e vs. log σ' → determine C_c, C_r, σ'_p (Casagrande construction)
- Plot dial vs. log t or √t for each increment → determine c_v (Casagrande or Taylor method)
- Post-EOP slope on log t plot → C_α

**Key Notes:**
- Sample quality critically affects σ'_p determination. Disturbed samples underestimate σ'_p.
- Load Increment Ratio (LIR) = Δσ/σ. Standard LIR = 1 (doubling). Smaller increments near σ'_p improve resolution.
- Specimen height/diameter ratio ≤ 0.4 to minimize side friction effects.
- Fixed-ring (drainage from top only) or floating-ring (drainage from both ends) configurations.
- Temperature effects: test at constant temperature; c_v increases ~2% per °C.

**Quality Indicators:**
- Initial void ratio should be consistent with moisture content and G_s
- Virgin compression line should be well-defined and approximately linear on e-log σ' plot
- Rebound index C_r should be much smaller than C_c

## ASTM D4186 — Standard Test Method for One-Dimensional Consolidation Properties of Saturated Cohesive Soils Using Controlled-Strain Loading (CRS)

**Scope:** Constant Rate of Strain (CRS) oedometer test. Continuous loading at constant strain rate with back-pressure saturation and pore pressure measurement at the base.

**Advantages over IL (D2435):**
- Continuous stress-strain curve (not discrete points)
- Better definition of σ'_p (no interpolation between load increments)
- Continuous c_v vs. σ' relationship
- Faster (typically 1–2 days vs. 1–2 weeks for IL)
- k vs. e relationship directly computed

**Key Requirements:**
- Strain rate: typically 0.5–1.0 %/hr for clays; slower for sensitive clays
- Pore pressure ratio (u_b/σ_v) should be maintained between 3–15% for valid results
- If ratio exceeds 15%, strain rate is too fast → reduce rate
- Back-pressure saturation required (B ≥ 0.95)

**Data Output:**
- σ'_v vs. ε_v (continuous) → C_c, C_r, σ'_p
- c_v vs. σ'_v (continuous) → c_v variation with stress level
- k vs. e (continuous) → permeability as function of void ratio
- No direct C_α measurement (no sustained load step) — supplement with IL or creep test if needed
