# Hydrology Fundamentals

## The Hydrologic Cycle

Water continuously circulates between the atmosphere, land surface, subsurface, and oceans through precipitation, evapotranspiration, infiltration, runoff, and groundwater flow. Engineering hydrology quantifies these processes to design infrastructure for water supply, flood control, drainage, and environmental protection.

## Water Balance Equation

The fundamental equation of hydrology:

P = Q + ET + ΔS

where P = precipitation, Q = runoff (surface + subsurface outflow), ET = evapotranspiration, and ΔS = change in storage (soil moisture, groundwater, surface water, snow). Over long periods for a watershed, ΔS ≈ 0.

## Precipitation

### Measurement
Point rainfall measured by rain gauges (tipping bucket, weighing gauge). Areal rainfall estimated by Thiessen polygons, isohyetal method, or radar (NEXRAD).

### Intensity-Duration-Frequency (IDF) Curves
Fundamental design tool relating rainfall intensity (mm/hr or in/hr) to duration and return period. Developed from long-term gauge records using frequency analysis.

**General form:** i = a / (t_c + b)^c (various empirical forms)

IDF curves are available from NOAA Atlas 14 for the US, providing point precipitation frequency estimates for durations from 5 minutes to 60 days and return periods from 1 to 1000 years.

### Return Period (Recurrence Interval)
The average time between events equaling or exceeding a given magnitude. A 100-year storm has a 1% probability of being equaled or exceeded in any given year.

P(exceedance) = 1/T

where T = return period in years. The probability of at least one occurrence in n years: P = 1 - (1 - 1/T)^n.

### Design Storm
A synthetic rainfall event used for design. Common types: SCS Type I, IA, II, III temporal distributions. Selection based on geographic region.

## Watershed (Drainage Basin) Characteristics

### Area (A)
Total contributing drainage area upstream of the point of interest. Delineated from topographic maps or DEMs.

### Slope
Average slope of the main channel or overland flow path. Affects time of concentration and peak flow.

### Time of Concentration (t_c)
Time for water to travel from the hydraulically most distant point in the watershed to the outlet. Critical parameter for peak flow estimation.

**Kirpich formula (rural):** t_c = 0.0078 × L^0.77 × S^(-0.385)
where t_c in minutes, L = channel length in feet, S = average slope (ft/ft).

**NRCS Lag Method:** t_c = L_lag / 0.6 where L_lag = (L^0.8 × (S_retention + 1)^0.7) / (1900 × Y^0.5)

Multiple methods exist (Kirpich, NRCS, Bransby-Williams, Izzard) — selection depends on watershed characteristics.

## Infiltration

Water entering the soil surface. Rate depends on soil type, moisture content, vegetation, and rainfall intensity.

### Horton's Equation
f(t) = f_c + (f_0 - f_c) × e^(-kt)

where f(t) = infiltration rate at time t, f_0 = initial rate, f_c = final (equilibrium) rate, k = decay constant.

### Green-Ampt Model
Physics-based infiltration model using Darcy's law:
f = K_s × [1 + (ψ × Δθ) / F]

where K_s = saturated hydraulic conductivity, ψ = wetting front suction head, Δθ = moisture deficit, F = cumulative infiltration.

## Runoff

### SCS Curve Number Method (NRCS)
Most widely used method for estimating direct runoff from rainfall.

Q = (P - I_a)² / (P - I_a + S)    for P > I_a; Q = 0 otherwise

where Q = runoff depth, P = rainfall depth, S = potential maximum retention = (1000/CN) - 10 (inches), and I_a = initial abstraction = 0.2S (standard) or 0.05S (updated).

CN (Curve Number) ranges from 30 (very permeable, forested) to 98 (impervious). Selected from tables based on soil group (A, B, C, D) and land use/cover.

### Rational Method
For small watersheds (< 80–200 hectares):

Q_p = C × i × A

where Q_p = peak discharge (cfs if i in in/hr, A in acres), C = runoff coefficient (0.05–0.95), i = rainfall intensity for duration = t_c, A = drainage area.

## Unit Hydrograph Theory

A unit hydrograph (UH) is the direct runoff hydrograph resulting from 1 unit (1 inch or 1 cm) of effective rainfall (excess rainfall) applied uniformly over the watershed for a specified duration.

**Assumptions:** Linearity (proportionality and superposition) and time invariance.

**SCS Dimensionless Unit Hydrograph:** Triangular approximation:
- Time to peak: T_p = Δt/2 + t_lag
- Peak flow: q_p = (484 × A) / T_p (in US customary units: q_p in cfs, A in mi², T_p in hours)
- Base time: T_b ≈ 2.67 × T_p

### Convolution
To compute the runoff hydrograph from a multi-period storm, convolve the excess rainfall hyetograph with the unit hydrograph using superposition.

## Evapotranspiration (ET)

Combined water loss from evaporation (soil, water surfaces) and transpiration (plants).

**Potential ET (PET):** Maximum ET rate given unlimited water supply. Estimated by Penman-Monteith (FAO-56), Hargreaves, or pan evaporation methods.

**Penman-Monteith (FAO-56):** Standard method for reference ET:
ET₀ = [0.408Δ(Rn-G) + γ(900/(T+273))u₂(es-ea)] / [Δ + γ(1+0.34u₂)]

where Δ = slope of saturation vapor pressure curve, Rn = net radiation, G = soil heat flux, γ = psychrometric constant, T = temperature, u₂ = wind speed at 2m, es-ea = vapor pressure deficit.
