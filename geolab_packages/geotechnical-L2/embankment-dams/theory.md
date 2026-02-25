# Embankment Dam Design

## Dam Zoning

Modern embankment dams use zoned cross-sections to optimize material placement:

**Zone 1 — Impervious core:** Low-permeability clay or silt (CL, CH, SC). Controls seepage. Placed wet of optimum for low permeability and resistance to hydraulic fracturing. k < 10⁻⁶ cm/s target.

**Zone 2 — Filter/drain:** Processed sand/gravel meeting filter criteria. Prevents internal erosion of core material. Placed on both upstream and downstream sides of core. Also includes blanket drains, chimney drains, toe drains.

**Zone 3 — Shell (transition):** Well-graded sand/gravel. Provides structural support to core, transitions between core and rockfill.

**Zone 4 — Rockfill shell:** Provides slope stability and drainage. High shear strength, free-draining. Upstream shell provides wave protection; downstream shell provides weight and drainage.

**Zone 5 — Riprap:** Upstream slope protection against wave erosion. Sized for wind-generated wave height.

### Core Geometry
- **Central core:** Most common. Core extends from foundation to crest. Typical 0.5H–1.0H width at base.
- **Inclined core:** Core inclined upstream. Reduces pore pressure in downstream shell. Less common.
- **Thin core (diaphragm):** Concrete, asphalt, or geomembrane. Used when adequate core material unavailable.

## Filter Design Criteria

Filters are the most critical safety feature. They prevent erosion of fine particles while remaining free-draining.

### Terzaghi Filter Criteria (Original)
- Retention: D₁₅(filter) / D₈₅(base) ≤ 4–5
- Permeability: D₁₅(filter) / D₁₅(base) ≥ 4–5

### Modern No-Erosion Filter (NEF) Criteria (USACE/Foster & Fell)
More conservative, accounts for broadly graded and gap-graded base soils:
- For base soil with > 85% fines: D₁₅(filter) ≤ 0.7 mm (Category 1)
- For base soil 35–85% fines: D₁₅(filter) ≤ 0.7 mm (Category 2)
- For base soil 15–35% fines: D₁₅(filter) ≤ 4 × D₈₅(base), ≤ 0.7 mm min (Category 3)
- For base soil < 15% fines: D₁₅(filter) ≤ 4 × D₈₅(base) (Category 4)

### Additional Filter Requirements
- Uniformity: Cu ≤ 20 (well-graded but not gap-graded)
- D₅(filter) ≥ 0.075 mm (no fines in filter)
- D₉₀(filter) ≤ 20 mm (practical limit for placement)
- Self-filtering: internally stable (Kenney & Lau 1985 criteria)

## Internal Erosion and Piping

The leading cause of embankment dam failures. Four mechanisms:

### Backward Erosion Piping (BEP)
Progressive erosion from downstream exit point, working backward toward reservoir. Occurs in non-cohesive foundation soils beneath or through the embankment. Requires:
1. Seepage exit point
2. Exit gradient exceeding critical value
3. Continuous seepage path in erodible material
4. Roof to support pipe (cohesive layer above)

### Concentrated Leak Erosion
Water flows through a crack, defect, or preferential path in the core (hydraulic fracture, poorly compacted zone, conduit interface). Erosion along the leak walls. Most dangerous because it requires no minimum gradient — just a through-going crack.

### Suffusion (Internal Instability)
Selective removal of fine particles from the matrix of an internally unstable soil. The coarse matrix remains but fines wash out, increasing permeability. Kenney & Lau (1985) criteria identify susceptible soils.

### Contact Erosion
Erosion at the interface between a coarse layer and fine layer when seepage flows parallel to the contact (e.g., gravel foundation beneath clay core).

## Seepage Analysis

### Steady-State Seepage
Flow net or numerical analysis (SEEP/W, PLAXIS) to determine:
- Phreatic surface location
- Pore pressure distribution for stability analysis
- Seepage quantities (for drain sizing)
- Exit gradients (for piping assessment)

### Transient Seepage (Rapid Drawdown)
Time-dependent analysis as reservoir drops. Pore pressures in upstream shell and core lag behind the falling reservoir — critical for upstream slope stability.

### Key Design Checks
- Exit gradient at downstream toe: FS ≥ 3–5 against critical gradient
- Seepage quantity through core: must be within drain capacity
- Phreatic surface must not emerge on downstream slope (chimney drain captures it)

## Instrumentation

### Piezometers
- Vibrating wire (most common): reliable, automated, long-term stability
- Standpipe (Casagrande): simple, robust, slow response in clay
- Pneumatic: faster response than standpipe, no freeze issues
- Location: within core, at base of core, in foundation, upstream/downstream shells

### Settlement Monitoring
- Surface monuments (survey)
- Internal settlement gauges (cross-arm, magnetic extensometer, shape array)
- Hydrostatic settlement cells

### Seepage Monitoring
- V-notch weirs at drain outlets (measure total seepage)
- Turbidity monitoring (detect internal erosion — increasing turbidity = alarm)
- Seepage collected and measured separately from different zones if possible

### Inclinometers
- Lateral deformation in foundation or embankment
- Critical for monitoring creep on downstream slopes

### Dam Safety Monitoring Program
- Establish baseline readings during construction and first filling
- Threshold and action levels for each instrument
- Automated data acquisition systems (ADAS) for critical dams
- Regular visual inspection is the most important monitoring tool
