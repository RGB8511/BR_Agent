# Construction Support Testing — Subgrade & Foundation Verification

## Overview

Construction support testing verifies that subgrade, base course, and foundation materials meet design requirements beyond density alone. These tests assess stiffness, bearing capacity, uniformity, and structural adequacy of the prepared surface before placement of the next layer or structure.

## Plate Load Test — ASTM D1196

### Principle
A rigid circular plate (typically 300, 450, or 762 mm diameter) is loaded incrementally against the ground surface using a hydraulic jack reacting against a loaded truck or anchor frame. Settlement is measured by dial gauges referenced to an independent beam. Load-settlement curve yields modulus of subgrade reaction (k) and bearing capacity.

### Modulus of Subgrade Reaction
k = q / δ (kPa/m or pci)

where q = applied pressure at a defined settlement (typically 1.27 mm = 0.05 in for k-value), δ = settlement.

**Corrections:**
- Plate size correction: k₃₀ = k_plate × (plate diameter / 30 in) for converting to standard 30-inch plate
- Saturation correction: test at expected worst-case moisture condition
- Repeated load: k from second load cycle may differ from first (virgin vs. reload modulus)

### Applications
Pavement design (rigid pavement k-value), foundation bearing verification, compaction quality assessment on large fills (dams, embankments), modulus determination for mat foundations.

### Limitations
Time-consuming (2–4 hours per test). Requires heavy reaction load (loaded truck, anchor piles). Influences only ~1.5–2× plate diameter depth. Point test — high spatial variability.

## Dynamic Cone Penetrometer (DCP) — ASTM D6951

### Principle
An 8 kg (17.6 lb) hammer drops 575 mm (22.6 in) onto an anvil attached to a rod with a 60° cone tip. Penetration per blow (mm/blow) recorded as the cone advances through the subgrade.

**DCP Index (DCPI):** mm/blow. Low DCPI = stiff/strong material. High DCPI = weak/soft.

### Correlations
CBR ≈ 292 / DCPI^1.12 (most common correlation — USACE, ASTM D6951 Appendix)

Many agency-specific correlations exist for CBR, modulus, and classification.

### Applications
Subgrade evaluation, compaction uniformity checking, identifying weak layers at depth (continuous profiling), pavement investigation (through existing pavement cutout), rapid screening of large areas.

### Advantages
Simple, portable, inexpensive, fast (15–30 minutes per sounding to 1 m depth). Provides continuous strength profile with depth (unlike surface-only tests).

## Clegg Impact Value (CIV) — ASTM D5874

### Principle
A 4.5 kg hammer (standard) dropped from 450 mm onto the soil surface. Accelerometer on the hammer measures peak deceleration on the 4th drop. Output: CIV (Clegg Impact Value, 0–100 scale).

### Correlations
CBR ≈ 0.07 × CIV² (approximate, varies by soil type)

### Applications
Rapid quality check for compacted surfaces. Quick go/no-go screening. Used in sports field and pavement construction for uniformity.

## Light Weight Deflectometer (LWD) — ASTM E2583

### Principle
Falling weight impacts a circular plate (200 or 300 mm) on the soil surface. Load cell measures impact force; geophone measures surface deflection. Calculates dynamic deformation modulus (E_vd).

E_vd = (1 - ν²) × σ₀ × r / d₀

where σ₀ = peak stress, r = plate radius, d₀ = peak deflection, ν = Poisson's ratio.

### Applications
Compaction quality assessment, subgrade modulus, base course stiffness. Faster and more portable than static plate load. Increasingly specified by European and some US agencies.

### Correlation
E_LWD ≈ (1–3) × E_static_plate depending on soil type and test conditions. Agency-specific target E_vd values used for acceptance.

## Falling Weight Deflectometer (FWD)

### Principle
Trailer-mounted device drops calibrated weight onto a loading plate on the pavement surface. Multiple geophones at increasing distances from the plate measure the deflection basin. Back-calculation of layer moduli from the deflection basin shape.

### Applications
In-service pavement structural evaluation, overlay design, joint load transfer (rigid pavements), void detection. Not typically used for bare subgrade — LWD or plate load for that.

## Proof Rolling

### Principle
A loaded pneumatic-tired roller (typically 25–50 ton gross vehicle weight) is driven slowly over the prepared subgrade. An observer watches for deflection, rutting, pumping (water/fines), or instability under the roller.

### Acceptance Criteria
Typical: no visible deflection, rutting < 25 mm (1 in), no pumping. Any area showing distress is marked for correction (removal and replacement, additional compaction, stabilization).

### Applications
Rapid whole-area assessment of subgrade adequacy. Identifies localized soft spots that point tests (NDG, DCP) might miss between test locations. Standard practice before pavement placement on highway and airfield projects.

## Field CBR — ASTM D4429

In-place CBR test using a piston pushed into the ground surface at standard rate (1.27 mm/min) with loads measured at 2.5 mm and 5.0 mm penetration. Compared against standard CBR value. Rarely performed in practice — laboratory CBR (ASTM D1883) on field-compacted samples is more common. DCP correlation to CBR has largely replaced field CBR.
