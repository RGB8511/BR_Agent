# Dam Hydrology — Inflow Design Floods & Reservoir Routing

## Hydrologic Hazard Classification

Every dam requires an Inflow Design Flood (IDF) commensurate with the consequences of failure. Dam hazard classification drives the IDF selection:

**High hazard (Class I/A):** Failure would cause probable loss of life. IDF typically = PMF or a large fraction thereof.

**Significant hazard (Class II/B):** Failure could cause significant economic damage but no expected loss of life. IDF typically between 0.5×PMF and PMF, or a flood with an annual exceedance probability (AEP) of 10⁻⁴ to 10⁻⁶.

**Low hazard (Class III/C):** Failure causes minimal damage. IDF typically 100-year to 0.5×PMF.

Classifications vary by jurisdiction. USACE, USBR, FERC, and state dam safety programs each maintain their own criteria, but the framework is consistent.

## Probable Maximum Flood (PMF)

The PMF is the flood resulting from the most severe combination of critical meteorological and hydrologic conditions that are reasonably possible in a region. It is NOT a statistically derived event — it has no assigned return period, though it is often loosely considered to exceed 10,000-year to 1,000,000-year return periods.

### PMF Development Process
1. Determine the Probable Maximum Precipitation (PMP) for the watershed
2. Apply temporal and spatial distribution to the PMP
3. Route the PMP through a calibrated rainfall-runoff model (HEC-HMS)
4. Include snowmelt contribution if applicable (rain-on-snow events)
5. Add base flow to the direct runoff hydrograph

### Probable Maximum Precipitation (PMP)

PMP is estimated using:

**Generalized estimates:** HMR 51 (eastern US), HMR 52 (application of HMR 51), HMR 57 (Columbia River), HMR 59 (Pacific slope). These provide PMP depth-area-duration (DAD) curves by region.

**Site-specific PMP studies:** Moisture maximization and storm transposition of historical extreme storms. Process: identify controlling storms, maximize moisture (multiply observed rainfall by ratio of maximum precipitable water to storm precipitable water), transpose storms to the watershed, construct depth-area-duration envelope.

**Stochastic approaches:** Emerging methods using stochastic storm transposition (SST) to develop probabilistic PMP estimates. Not yet standard practice but gaining acceptance.

### Antecedent Conditions
- **Antecedent storm:** A smaller storm (typically 40–60% of PMP, 3–5 days prior) that saturates the watershed. Required by many agencies for PMF computation.
- **Snowpack:** For basins with seasonal snow, include 100-year snowpack with design temperature sequence.
- **Reservoir level:** Assume pool at normal maximum (spillway crest or top of active storage) at the start of the flood event.

## Inflow Design Flood (IDF) Selection

### Incremental Damage Assessment (IDA)
For dams where PMF is not automatically required, an IDA determines whether dam failure during a specific flood would cause incremental damage (damage beyond what the flood alone would cause without failure). If incremental loss of life = 0, a smaller IDF may be justified.

### Risk-Informed Approach
Modern practice (USACE, USBR, FERC) increasingly uses risk-informed methods:
- Estimate annualized probability of failure for each loading condition
- Compare to tolerable risk guidelines (e.g., USBR: individual risk < 10⁻⁴/year, societal risk per f-N chart)
- IDF selected so that hydrologic risk contribution does not dominate total dam risk

### Interim IDF Guidelines (Common Practice)
Until a full risk assessment is completed:
- High hazard → PMF (or demonstrated that a fraction of PMF meets risk criteria)
- Significant hazard → 0.5×PMF to PMF, or 10⁻⁴ AEP flood
- Low hazard → 100-year to 500-year flood, or 0.1×PMF to 0.5×PMF

## Reservoir Flood Routing

Routing transforms the inflow hydrograph to an outflow hydrograph by accounting for reservoir storage. It determines: peak outflow (< peak inflow), maximum pool level, freeboard adequacy, and spillway capacity requirements.

### Level-Pool (Modified Puls) Routing

Assumes horizontal water surface in the reservoir (valid for most reservoirs where length-to-depth ratio is large).

**Storage indication equation:**
(2S₂/Δt + O₂) = (I₁ + I₂) + (2S₁/Δt - O₁)

where S = storage, O = outflow, I = inflow, subscripts 1 and 2 = beginning and end of time step Δt.

**Required relationships:**
1. Elevation-storage curve (from reservoir topography)
2. Elevation-discharge curve (spillway rating curve + outlet works + any other releases)

**Procedure:** For each time step, compute the right-hand side (known), then look up (2S₂/Δt + O₂) to find O₂ and the corresponding pool elevation.

### Dynamic Routing
For long, narrow reservoirs or dam-break flood routing through downstream channels, use unsteady flow (Saint-Venant equations) via HEC-RAS. Level-pool assumption breaks down when the flood wave travel time through the reservoir is a significant fraction of the flood duration.

## Dam Breach Analysis

### Purpose
Estimate the peak outflow, timing, and downstream flood wave from a hypothetical dam failure. Required for:
- Emergency Action Plans (EAPs)
- Hazard classification (does failure cause loss of life?)
- Incremental damage assessment
- Dam break flood inundation mapping

### Breach Parameters
A breach is characterized by:
- **Breach width (B_avg):** Average width at final breach geometry
- **Breach depth (H_b):** Full height of dam or depth to breach bottom
- **Side slopes (z):** Breach side slopes (H:V)
- **Formation time (t_f):** Time from initiation to full breach development

### Empirical Breach Parameter Estimation

**Froehlich (2008) — Breach width:**
B_avg = 0.27 × k₀ × Vw^0.32 × Hb^0.04

**Froehlich (2008) — Formation time:**
tf = 63.2 × √(Vw / (g × Hb²))

where Vw = reservoir volume at breach (m³), Hb = breach height (m), k₀ = 1.3 for overtopping, 1.0 for piping.

**Xu & Zhang (2009):** Regression equations relating breach parameters to dam height, reservoir volume, and dam type/erodibility. Provides wider range of parameters.

### Peak Breach Outflow Estimates

**USBR (1982) simplified:**
Qp = 19.1 × (Hw)^1.85

where Qp = peak breach outflow (m³/s), Hw = depth of water above breach bottom at time of failure (m).

**Froehlich (1995):**
Qp = 0.607 × Vw^0.295 × Hw^1.24

### Routing the Breach Flood
Route the breach outflow hydrograph downstream using HEC-RAS (unsteady flow, 2D preferred for complex floodplains). Map inundation extent, depth, velocity, and arrival time at population centers. DV (depth × velocity) product used for life safety assessment.

## Spillway Design Flood (SDF)

The SDF is the flood used to size the spillway. For high-hazard dams, SDF = IDF = PMF typically. However, some jurisdictions allow a distinction where the IDF is the flood the dam must safely pass (potentially with some controlled overtopping if designed), while the SDF sizes the spillway for normal operation.

The key design output from dam hydrology is the **maximum reservoir elevation** during routing of the IDF/SDF, which directly determines:
- Spillway capacity requirements
- Dam crest elevation (max pool + freeboard)
- Downstream flood hazard
