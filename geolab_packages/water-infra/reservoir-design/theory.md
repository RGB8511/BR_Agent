# Reservoir Planning & Design

## Reservoir Zones

A reservoir's vertical extent is divided into functional zones, each serving a specific purpose:

**Dead storage (inactive pool):** Volume below the lowest outlet invert. Cannot be released. Serves as sediment storage and may provide minimum pool for recreation, fish habitat, or head on outlet works. Sized to accommodate the design sedimentation life (typically 50–100 years).

**Active storage (conservation pool):** Volume between dead storage and normal maximum pool (top of conservation). Used for water supply, irrigation, power generation, environmental flows, and recreation. Sized by yield analysis.

**Flood control pool (flood storage):** Volume between top of conservation and maximum flood control pool. Reserved empty during flood season to capture inflows and reduce downstream flood peaks. Operated per the Water Control Manual.

**Surcharge storage:** Volume between top of flood control and maximum pool (dam crest minus freeboard). Temporarily stored during passage of extreme floods. Spillway capacity determines how quickly surcharge is evacuated.

**Freeboard:** Vertical distance from maximum pool (during IDF passage) to dam crest. Provides margin for wave action, wind setup, settlement, and uncertainty.

## Elevation-Area-Storage Curves

The fundamental physical relationship for any reservoir. Developed from topographic survey or DEM analysis.

**Area-elevation:** A = f(h) from contour area measurements at each elevation.

**Storage-elevation:** S(h) = ∫₀ʰ A(h') dh', computed by trapezoidal or prismoidal method between contour intervals.

These curves drive all reservoir analysis: routing, yield, sedimentation, evaporation losses.

## Reservoir Yield Analysis

### Firm (Safe) Yield
The maximum rate of continuous release that can be maintained through the worst drought of record (or design drought) without exhausting active storage. This is the fundamental sizing criterion for water supply reservoirs.

### Rippl (Mass Curve) Method
Plot cumulative inflow versus time for the historical period. The maximum deficit (departure of cumulative inflow below cumulative demand) equals the required active storage.

S_required = max[Σ(D_i - I_i)] for all periods where D > I

where D_i = demand in period i, I_i = inflow in period i. Apply to the critical (driest) period in the record. Adjust for evaporation and seepage losses.

### Sequent Peak Algorithm
More practical for computer analysis than graphical mass curve:
1. Compute S_t = S_{t-1} + D_t - I_t for each period
2. If S_t < 0, set S_t = 0 (reservoir spills)
3. Required storage = maximum S_t over the entire record

### Stochastic Methods
For records shorter than desired design life, generate synthetic streamflow sequences (Thomas-Fiering, disaggregation models, or modern copula-based methods) to assess yield reliability probabilistically. Reliability = fraction of years in which full demand is met. Typical target: 95–99% reliability for municipal supply.

## Reservoir Losses

### Evaporation
Net evaporation = gross evaporation - precipitation on reservoir surface (which would have become runoff without the reservoir). Compute monthly evaporation using pan evaporation data (apply pan coefficient, typically 0.70–0.80) or Penman method.

Annual net evaporation loss can be significant — 0.5–2.5 m depth in arid climates. Loss volume = net evaporation rate × reservoir surface area (which varies with pool level).

### Seepage
Reservoir losses through the reservoir floor and rim. Geology-dependent. Ranges from negligible (impervious clay/shale basins) to severe (karst, fractured rock, permeable alluvium). May require treatment: grouting, blankets, or geomembrane liners. Monitor with reservoir balance calculations: ΔS = Inflow - Outflow - Evaporation - Seepage.

## Sedimentation

### Sediment Inflow
Annual sediment yield from the watershed estimated by sediment-rating curves, USLE/RUSLE, PSIAC method, or regional regression. Expressed as total sediment volume (accounting for bulk density of deposited sediment).

### Trap Efficiency
Fraction of incoming sediment retained in the reservoir. Depends on ratio of reservoir capacity to annual inflow:

Brune's curve: empirical relationship between trap efficiency (%) and capacity-to-inflow ratio (C/I). At C/I = 1.0: trap efficiency ≈ 95–99%. At C/I = 0.01: trap efficiency ≈ 50–70%.

### Sedimentation Life
Dead storage is typically sized to accommodate sediment accumulation for the design life:

V_dead ≥ S_annual × T_design / (TE × γ_d)

where S_annual = annual sediment mass inflow, T_design = design sedimentation life (50–100 years), TE = trap efficiency, γ_d = dry bulk density of deposited sediment (1.0–1.5 t/m³).

### Sediment Distribution in Reservoir
Coarse sediment (sand/gravel) deposits as deltas near the upstream end. Fine sediment (silt/clay) deposits throughout, with density currents carrying some to the dam face. Empirical methods (Borland-Miller area-reduction method) distribute sediment vertically in the reservoir.

## Reservoir Operations

### Water Control Plan (Operations Manual)
Every major reservoir has a water control plan specifying:
- Rule curves: target pool elevations by season (conservation, flood control zones)
- Release schedules: minimum flows, water supply deliveries, power generation targets
- Flood operations: spillway gate operating procedures, downstream channel capacity constraints
- Drought operations: curtailment priorities, minimum pool criteria

### Multipurpose Reservoir Trade-offs
Competing objectives require balancing: water supply wants maximum conservation storage, flood control wants empty flood pool, recreation wants stable pool, power wants head, environment wants variable flows. Optimization methods (linear programming, simulation) help resolve conflicts.
