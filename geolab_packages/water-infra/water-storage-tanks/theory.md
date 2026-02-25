# Water Storage Tanks — Design & Sizing

## Functions of Storage in Water Systems

Water storage serves multiple critical functions:
- **Equalization:** Balances hourly demand fluctuations so supply infrastructure (treatment, pumping, transmission) can be sized for average rather than peak demand
- **Fire protection:** Provides stored volume for fire-fighting demand during fire flow events
- **Emergency reserve:** Water available during source or treatment outages, power failures, or main breaks
- **Pressure regulation:** Maintains system pressure within acceptable range as demands fluctuate

## Tank Types

### Ground-Level Reservoirs
Circular or rectangular tanks at ground level. Steel (welded per AWWA D100), prestressed concrete (AWWA D110), or reinforced concrete. Largest practical volumes. Require pumping to deliver water at pressure — commonly used as clearwells at treatment plants and large distribution storage.

### Elevated Tanks
Tank on a tower/pedestal that provides pressure by elevation (hydraulic grade). Steel (AWWA D100) or concrete (AWWA D115). Overflow elevation sets the maximum system HGL. Common types: spheroid, fluted column, composite (steel bowl on concrete pedestal).

### Standpipes
Tall, ground-level cylindrical tanks where only the upper portion provides usable pressure. Effective storage = volume above minimum HGL elevation. Simple construction but inefficient — much of the volume is below the useful pressure range.

### Buried/Partially Buried Reservoirs
Reinforced concrete or prestressed concrete. Protected from freezing and vandalism. Common for large clearwells and in areas where aesthetics are a concern.

## Storage Volume Components

### Equalization Storage
Volume needed to balance between supply rate and demand rate during peak demand periods. Typically determined from mass-balance analysis using diurnal demand curves.

**Rule of thumb:** Equalization storage ≈ 25% of maximum day demand. More precise: area between supply and demand curves on a cumulative mass diagram.

### Fire Storage
Volume required during fire flow events:

V_fire = Q_fire × T_fire

where Q_fire = required fire flow rate (from ISO, local fire code, or insurance requirements) and T_fire = fire flow duration (typically 2–4 hours for residential, 4–10 hours for commercial/industrial).

### Emergency Storage
Volume for service during supply disruption. Varies by system:
- Small systems: 1–3 days average demand
- Large systems: 12–24 hours average demand
- Some agencies use probabilistic approaches

### Dead Storage
Volume below the useful outlet or minimum operating level. Not available for pressure service. Should be minimized in design but cannot be zero (structural, mixing, and piping considerations).

## Sizing Methodology

Total required storage = Equalization + Fire + Emergency + Dead

For systems with multiple tanks, the total can be distributed. Not all components need to be in every tank — for example, fire storage might be in one tank while equalization is spread across several.

## Mixing and Water Quality

### Turnover
Tanks must turn over frequently enough to prevent water quality degradation (disinfectant residual decay, bacterial regrowth, taste and odor):
- Target: Complete turnover every 3–5 days for chlorinated systems
- Minimum: Exchange at least 25% of volume daily

### Mixing Design
Passive mixing (inlet/outlet configuration) or active mixing (mechanical mixers, recirculation pumps):
- Separate inlet and outlet (different elevations) to promote circulation
- Inlet diffuser or nozzle to create jet mixing
- Avoid dead zones and short-circuiting
- AWWA recommends CFD modeling for large tanks

### Thermal Stratification
In large tanks, warm water stratifies on top, cold on bottom. The stagnant upper layer loses disinfectant residual. Mixing systems prevent stratification.

## Structural Considerations

### Seismic Design
AWWA D100 (steel) and D110/D115 (concrete) include seismic provisions based on:
- Site seismic hazard (mapped spectral accelerations)
- Importance factor (essential facility = 1.5)
- Response modification factor (varies by tank type)
- Sloshing wave height and freeboard
- Anchoring vs. unanchored (flat-bottom steel tanks)

### Foundation
Tanks impose large, relatively uniform loads:
- Ring-wall foundation (concrete ring under shell) for steel tanks
- Mat foundation for concrete tanks
- Bearing capacity and settlement analysis required
- Differential settlement limits: AWWA D100 specifies maximum 1 in 200

### Overflow and Drain
- Overflow: Sized for maximum inflow rate with downstream energy dissipation
- Drain: Sized for practical drain time (typically 4–8 hours for maintenance access)
- Both discharge to safe location (not into sanitary sewer)
