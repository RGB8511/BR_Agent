# Field Vane Shear Test

## Purpose and Applicability

The field vane shear test (FVT) measures the in-situ undrained shear strength (Su) of soft to medium-stiff, saturated, fine-grained soils. It is the most direct in-situ measurement of Su and is the reference test against which other in-situ test correlations (CPT Nkt, SPT) are often calibrated.

**Best suited for:** Soft to firm clays and silts (Su < 200 kPa). Saturated, fine-grained soils where undrained conditions prevail during rapid shearing.

**Not suitable for:** Stiff fissured clays (fissures cause progressive failure), sands and gravels (drainage during test), partially saturated soils, organic soils with fibrous inclusions (fibers wrap around vane), soils with gravel/shells (vane cannot penetrate or results are erratic).

## Test Procedure

### Equipment
A four-bladed rectangular vane attached to rods is pushed into the soil to the test depth. Standard vane: 65 mm diameter × 130 mm height (H/D = 2). Smaller vanes for stiffer soils; larger for very soft soils.

The vane is advanced below the bottom of the borehole (or pushed directly through soft soil without a borehole) to a test depth at least 5 vane diameters below any disturbed zone.

### Testing Sequence
1. **Advance vane** to test depth. Wait 1–5 minutes for pore pressure equalization (longer for stiff soils).
2. **Rotate vane** at a constant rate of 6°/min (0.1°/s) per ASTM D2573. Measure torque vs. rotation.
3. **Record peak torque** — this corresponds to peak undrained shear strength.
4. **Continue rotation** (typically 10 full revolutions) to fully remold the soil at the shear surface.
5. **Measure remolded torque** — corresponds to remolded undrained shear strength.
6. **Calculate sensitivity:** St = Su(peak) / Su(remolded).

### Key Procedural Considerations
- **Rotation rate matters:** Faster rates overestimate Su due to viscous effects. ASTM specifies 6°/min but some standards allow up to 12°/min.
- **Rod friction:** Must be accounted for or eliminated. Slip coupling isolates vane from rod friction. If no slip coupling, perform a friction test (rotate rods without vane) and subtract.
- **Time delay before testing:** Excessive wait time allows consolidation around the vane, overestimating Su. Minimize insertion-to-test time.
- **Depth of insertion below borehole:** Minimum 4–5 vane diameters (260–325 mm for standard vane) below the bottom of the borehole to test undisturbed soil.

## Bjerrum Correction Factor

Field experience from embankment failures showed that direct FVT Su values overestimate the operational strength for stability analysis, particularly in plastic clays. Bjerrum (1972) developed a correction factor μ:

Su(design) = μ × Su(FVT)

The correction accounts for: rate effects (FVT is faster than field loading), anisotropy (vane measures an average of horizontal and vertical Su, but failure surfaces may be dominated by one), progressive failure, and stress path differences.

**μ values:** Range from ~1.0 for low-plasticity clays (PI ~20) to ~0.5 for highly plastic clays (PI > 100). Typical: μ = 0.6–0.8 for moderate-plasticity clays.

## Sensitivity

Sensitivity (St) from the vane test is an important indicator of clay behavior:
- St < 2: Low sensitivity (insensitive)
- St = 2–4: Medium sensitivity
- St = 4–8: Sensitive
- St = 8–16: Extra-sensitive
- St > 16: Quick clay

Quick clays (St > 30 in some Scandinavian/Canadian marine clays) can lose nearly all strength when remolded, leading to rapid retrogressive landslides.

## Mini-Vane (Laboratory Vane)

The laboratory mini-vane (ASTM D4648) is a smaller version used on tube samples, block samples, or test pits. Blade sizes: 12.7–25.4 mm diameter. Quick assessment of Su and sensitivity on samples. Useful for sample quality evaluation and correlation with field vane results.
