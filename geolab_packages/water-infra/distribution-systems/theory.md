# Water Distribution System Design

## System Layout

### Network Configuration
**Looped systems:** Interconnected pipes forming closed loops. Preferred because: flow reaches customers from multiple directions (redundancy), lower head losses (flow splits between parallel paths), better fire flow, more uniform pressures. Required for urban and suburban areas.

**Branched systems:** Tree-like, with dead-end mains. Acceptable only for very low-density rural areas. Disadvantages: dead-ends cause water quality problems (stagnation, disinfectant loss), no redundancy, single-point failure isolates downstream customers.

**Grid pattern:** Combination of transmission mains (large diameter, long distance) and distribution mains (smaller, local service). Transmission mains deliver water to distribution zones; distribution mains serve customers directly.

### Pressure Zones
Large systems with significant topographic variation are divided into pressure zones — areas served at a common HGL (controlled by a tank, PRV, or pump station).

**Criteria:**
- Maximum static pressure at lowest service: ≤ 550 kPa (80 psi). Above 550 kPa, install individual PRVs at service connections.
- Minimum pressure during peak hour: ≥ 275 kPa (40 psi) at meter. During fire flow: ≥ 140 kPa (20 psi).
- Pressure zone range: typically 30–40 m (100–130 ft) of elevation difference per zone.

**Zone boundaries:** PRVs (pressure reducing valves) control pressure at zone interfaces. Altitude valves control tank fill. Pump stations boost pressure to higher zones.

## Demand Analysis

### Water Demand Components
- **Average day demand (ADD):** Total annual consumption / 365.
- **Maximum day demand (MDD):** Highest single-day demand in a year. Typically 1.5–2.5 × ADD.
- **Peak hour demand (PHD):** Highest hourly demand. Typically 1.5–2.0 × MDD or 2.5–4.0 × ADD.
- **Fire flow demand:** Superimposed on MDD (not PHD) for design purposes.

### Peaking Factors
Peaking factors vary by system size, climate, land use, and conservation measures. Larger systems have lower peaking factors due to demand averaging.

### Per-Capita Demand
Varies widely: 200–600 L/person/day (50–150 gpcd) depending on climate, conservation, industrial use, and system losses. US average ~300 L/person/day residential; total system demand including commercial/industrial higher.

### Fire Flow Requirements
Per ISO (Insurance Services Office) Commercial Risk Services rating, or local fire code. Based on building construction, occupancy, separation, and area. Typical: 500–3500 gpm (30–220 L/s) for 2–4 hours. Duration and flow depend on fire risk area.

## Hydraulic Design

### Pipe Sizing
Distribution mains: minimum 150 mm (6 in) diameter in residential areas with fire hydrants; 200 mm (8 in) preferred. Dead-end mains: minimum 150 mm (6 in). Transmission mains: sized for head loss and velocity criteria.

**Head loss criteria for distribution mains:**
- Maximum velocity: 1.5–2.4 m/s (5–8 ft/s) at fire flow
- Maximum head loss gradient: 10 m/km (10 ft/1000 ft) at fire flow; 3–5 m/km for normal peak flow
- Velocities during normal operation: typically < 1.0 m/s

### Network Analysis
Modern distribution systems are designed using computer hydraulic models (EPANET, WaterGEMS, WaterCAD, InfoWater).

**Steady-state analysis:** Solve simultaneously for all pipe flows and node pressures satisfying: continuity (ΣQ = 0 at each node) and energy (head loss around each loop = 0). Hardy-Cross iterative method historically; modern gradient algorithm.

**Extended-period simulation (EPS):** Time-varying demands, tank level changes, pump operations, and control valve actions over 24–72+ hours. Required for storage sizing, water quality analysis, and operational optimization.

### Water Quality Modeling
- **Water age:** Time since water entered the system from the source. Target: < 3–5 days. Excessive age correlates with disinfectant residual loss, DBP formation, taste/odor, and nitrification.
- **Chlorine residual decay:** First-order decay model: C(t) = C₀ × e^(-k×t). Bulk decay (in water) + wall decay (pipe surface reaction).
- **Trace analysis:** Track water from specific sources through the network to identify blending zones and source allocation.

## Fire Protection

### Hydrant Spacing
Residential: 150–200 m (500–660 ft) spacing typical. Commercial/industrial: 90–120 m (300–400 ft). Intersection placement preferred for multiple-direction access.

### Fire Flow Testing
Hydrant flow tests measure available fire flow at 140 kPa (20 psi) residual pressure. Test involves measuring static pressure, then flowing one or more hydrants and measuring residual pressure. Results used to calibrate hydraulic models.

## System Operations

### SCADA and Telemetry
Supervisory Control and Data Acquisition systems monitor and control: tank levels, pump operations, PRV settings, flow rates, pressures, chlorine residual, and turbidity. Real-time data for operators; historical data for planning.

### Unidirectional Flushing (UDF)
Systematic flushing program that opens hydrants in a planned sequence to move water through the system at high velocity (> 1.5 m/s), scouring sediment and biofilm. More effective than random flushing.

### Water Loss Control
Non-revenue water = authorized unbilled + apparent losses (meter error, unauthorized use) + real losses (leaks, breaks, overflow). Target real losses using IWA water balance methodology and Infrastructure Leakage Index (ILI). Economic level of leakage balances cost of active leak detection against value of water saved.
