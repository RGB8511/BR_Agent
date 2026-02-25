# Embankment Dam Design — Hydraulic & Seepage Aspects

## Overview

This package addresses the hydraulic and seepage design aspects of embankment dams, complementing the geotechnical package that covers slope stability, compaction, and material properties. The focus is on controlling water movement through and under the dam to prevent internal erosion — the leading cause of embankment dam failures.

## Seepage Control Philosophy

Every embankment dam will experience seepage — the goal is to control it safely:
1. **Minimize seepage:** Low-permeability core, foundation cutoff (grout curtain, slurry wall, cutoff trench)
2. **Filter and drain seepage:** Collect seepage in properly designed filters and drains before it exits uncontrolled
3. **Reduce uplift and exit gradients:** Relief wells, drainage blankets, weighted berms

**Critical principle:** Seepage must be intercepted by a filter before it reaches an unfiltered exit face. This prevents internal erosion.

## Seepage Analysis

### Flow Nets
Graphical solution for 2D steady-state seepage. Equipotential lines and flow lines form a network where:
- q = k × H × (Nf/Nd) per unit length of dam
- where Nf = number of flow channels, Nd = number of equipotential drops, H = total head, k = permeability

### Numerical Seepage Analysis
For complex geometries, anisotropic materials, transient conditions:
- Finite element seepage analysis (SEEP/W, PLAXIS, SLIDE)
- Models include: steady-state phreatic surface, transient drawdown, foundation seepage
- Output: pore pressure distribution (for stability analysis), flow quantities, gradients, exit conditions

## Filter Design

Filters are the single most important seepage control element. A properly designed filter:
- Prevents migration of base soil particles (retention)
- Is sufficiently permeable to discharge seepage water without building pressure (permeability)
- Does not segregate during placement (self-filtering)

### USBR/USACE No-Erosion Filter Design Criteria

**Retention (prevent piping):**
D15F / d85B ≤ 5 (for broadly graded base soils)
D15F / d85B ≤ 4 × d85B adjusted (USBR method considering base soil gradation)

**Permeability:**
D15F / d15B ≥ 5 (ensures filter is permeable enough)

**Gradation limits:**
- Maximum particle size: 75 mm (3 in)
- < 5% passing No. 200 sieve (non-plastic fines)
- Uniformity coefficient Cu = D60/D10 ≤ 6 (well-graded but not gap-graded)
- No gap-graded materials (could allow particle migration)

### Critical Filter (Sand-Size) Applications
- Chimney drain/filter: vertical or inclined zone downstream of core
- Blanket drain: horizontal zone at base of downstream shell
- Toe drain: at downstream toe collecting foundation and embankment seepage
- Filter diaphragms: around conduits passing through the dam

## Foundation Seepage Control

### Grout Curtain
- Single or multiple rows of cement grout holes drilled into rock foundation
- Reduces seepage through fractured rock by filling joints and fissures
- Depth: typically 0.3–0.7 × head (USBR), deeper at abutments
- Primary spacing 3–6 m, split-spacing to 1.5 m where needed
- Effectiveness measured by Lugeon testing: target < 3–5 Lu

### Cutoff Trench
- Excavation through pervious alluvium to impervious foundation
- Backfilled with compacted impervious material (core material)
- Most positive seepage barrier when practical

### Slurry Wall (Cutoff Wall)
- Cement-bentonite or soil-cement-bentonite slurry wall through alluvial foundation
- Constructed by slurry trench method or secant pile method
- Permeability target: < 10⁻⁷ cm/s
- Used when cutoff trench is impractical (deep alluvium, high water table)

### Relief Wells
- Downstream of the dam toe, drilled into pervious foundation layers
- Reduce artesian pressure (uplift) beneath the impervious blanket
- Spacing designed to reduce exit gradients below critical values

## Freeboard Design

Freeboard = dam crest elevation - maximum reservoir level

### Components (USBR DS-13 Ch6)
1. **Normal freeboard** = Flood surcharge + wave runup + wind setup + settlement + safety margin
2. Maximum reservoir level = IDF routing + initial pool level

### Wave Runup (SMB/Saville Method)
- Significant wave height Hs from wind speed, fetch, and duration
- Wave runup R on riprap slope depends on Hs, wave period, and slope angle
- R/Hs typically 1.5–3.0 for riprap slopes depending on permeability

### Wind Setup
S = V²F / (62,000 × d_avg) (English units, V in mph, F in miles, d in ft)

### Settlement Allowance
1–2% of embankment height for rockfill, 2–5% for earth-fill

### Minimum Freeboard
USBR: Normal freeboard ≥ 3 ft (0.9 m) above maximum water surface (PMF for high-hazard)

## Slope Protection

### Upstream Slope
- **Riprap:** Most common. Sized for wave action (Hudson formula or USACE method). Typical D50: 150–600 mm depending on wave height. Underlain by bedding/filter layer.
- **Soil-cement:** 6–8 inch lifts compacted on slope. Economical in some regions.
- **Concrete facing:** Slip-formed or pre-cast panels. Used on concrete-face rockfill dams (CFRD).

### Downstream Slope
- Grass/vegetation (most common for earth dams)
- Riprap (if subject to tailwater or wave action)
- Adequate drainage to prevent saturation
