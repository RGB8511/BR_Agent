# Tracer Tests & Grouting — Investigation and Treatment

## PART 1: TRACER TESTS

### Purpose
Tracer tests investigate groundwater flow paths, velocities, connections between features (springs, wells, fractures), and aquifer transport properties (dispersivity, effective porosity). Essential for dam seepage investigation, karst characterization, contaminant transport assessment, and wellhead protection.

### Tracer Types

**Fluorescent dyes:**
- **Fluorescein (Uranine):** Most common. Green fluorescence. Detection limit ~0.01 ppb. Moderate sorption. Inexpensive.
- **Rhodamine WT:** Orange-red fluorescence. Lower detection limit. Higher sorption on soil/organics. Good for surface water.
- **Sulforhodamine B:** Red. Low sorption. Good for karst.
- **Optical brighteners (Tinopal):** UV fluorescence. Visual detection on cotton receptors. Cheap qualitative test.

**Other tracers:**
- **Salt (NaCl, KCl, LiBr):** Detected by conductivity (NaCl, KCl) or chemical analysis (LiBr). Non-toxic, cheap. Higher mass required.
- **Dissolved gases (SF₆, He):** Very low detection limits. Used in saturated zone studies.
- **Microspheres/particles:** Track particulate transport (different mechanism than dissolved tracers).
- **Temperature:** Natural tracer — particularly useful for identifying seepage through dams (thermal anomaly detection).

### Test Methods

**Qualitative (connection test):** Inject dye at point A, monitor at suspected discharge points (springs, wells, seeps). Positive detection = hydraulic connection exists. Uses activated charcoal (bug) or cotton receptors for passive collection.

**Quantitative (breakthrough curve):** Inject known mass of tracer; monitor concentration vs. time at discharge points with automatic samplers or continuous fluorometers. Breakthrough curve provides: first arrival time, peak arrival time, mean residence time, tracer recovery, and dispersivity.

### Interpretation

**Mean velocity:** v = L / t_mean where L = straight-line distance, t_mean = time of centroid of breakthrough curve.

**Effective porosity (for known conduit/fracture):** n_e = Q × t_mean / V_aquifer (volume between injection and detection).

**Longitudinal dispersivity:** α_L = σ²_t × v / (2 × t_mean) where σ²_t = variance of breakthrough curve. Scale-dependent — dispersivity increases with transport distance.

**Recovery:** R = (∫C(t)×Q(t) dt) / M_injected. Recovery < 100% indicates loss to sorption, diffusion into matrix, or undiscovered discharge points.

## PART 2: GROUTING

### Purpose
Grouting injects fluid materials into voids, fractures, or pore space in soil or rock to:
- Reduce permeability (seepage cutoff — dam foundations, excavation dewatering)
- Improve strength (foundation treatment, tunnel pre-support)
- Fill voids (karst treatment, mine workings, abandoned structures)
- Compact soil (compaction grouting for settlement remediation)

### Grout Types

**Cementitious grouts:**
- **Neat cement grout:** Portland cement + water. Standard for rock grouting. W:C ratio from 5:1 (thin, starting) to 0.5:1 (thick, final). Penetrates fractures > 0.1–0.2 mm.
- **Microfine cement:** Ground to < 15 μm (D95). Penetrates finer fractures (0.05–0.1 mm) and coarse sand. More expensive.
- **Cement-bentonite:** Cement + 2–5% bentonite. Reduces bleed, improves stability. Common for dam curtain grouting.
- **Cement-fly ash/slag:** Supplementary cementitious materials reduce heat, improve sulfate resistance.

**Chemical grouts:**
- **Sodium silicate:** Low viscosity, controllable set time. Permeation of sands. Environmental concerns with some catalysts.
- **Polyurethane:** Fast-setting; expands on contact with water. Used for active water inflow cutoff.
- **Acrylamide/acrylate:** Very low viscosity; penetrates fine sand/silt. Environmental and health concerns with some formulations.
- **Colloidal silica:** Nano-sized silica particles. Very low viscosity, non-toxic. Permeates fine sand.
- **Epoxy/resin:** Structural grouting — anchors, cracks, equipment bases.

### Dam Foundation Grouting

**Curtain grouting:** Single or multiple rows of grout holes drilled into the rock foundation along the dam axis. Purpose: reduce seepage under and around the dam. Depth: 30–70% of reservoir head, or to competent low-permeability rock.

**Blanket grouting:** Shallow, closely-spaced grout holes over a wide area under the dam footprint. Purpose: consolidate shallow fractured/weathered rock and reduce near-surface permeability. Depth: 6–15 m typically.

**Split-spacing method:** Start with primary holes at wide spacing (e.g., 12 m). Drill and grout secondary holes at midpoints. Continue splitting (tertiary, quaternary) until target permeability (Lugeon value) is achieved. Closure criterion: acceptable average Lugeon in final-stage verification holes.

**GIN Method (Grouting Intensity Number):**
Developed by Lombardi & Deere (1993). Single stable grout mix (W:C = 0.67–1.0 with superplasticizer). Grouting governed by limiting: maximum pressure (P_max), maximum volume per stage (V_max), and GIN = P × V (constant energy envelope). Computer-monitored in real time. Avoids multiple mix changes of traditional methods.

### Compaction Grouting
Injection of very stiff (low-slump) mortar grout to displace and densify surrounding soil. Used for:
- Sinkhole remediation
- Settlement compensation
- Liquefaction mitigation
- Void filling beneath structures

Grout does not permeate soil — it forms a bulb that compresses surrounding material. Injection pressure 0.5–5 MPa typical.

### Jet Grouting
High-pressure (20–50 MPa) cement grout injected through rotating nozzle at the bottom of a drill string. Erodes and mixes in-situ soil with grout to form soilcrete columns (0.6–2.5 m diameter). Three systems: single-fluid (grout only), double-fluid (grout + air), triple-fluid (water + air cutting jet, separate grout).
