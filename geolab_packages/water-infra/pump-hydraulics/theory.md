# Pump Hydraulics & Selection

## Pump Classification

### By Operating Principle
- **Centrifugal (rotodynamic):** Impeller imparts kinetic energy to fluid, which is converted to pressure in the volute/diffuser. Dominant type for water infrastructure.
- **Positive displacement:** Piston, diaphragm, screw, or progressive cavity. Used for metering, high-viscosity, or high-pressure/low-flow applications.

### By Specific Speed (Centrifugal)
Specific speed classifies impeller geometry based on the operating point:
- **Radial flow (Ns < 4000 US):** Low Q, high H. Flat curve. Standard centrifugal pump.
- **Mixed flow (Ns 4000–10,000):** Moderate Q and H. Steeper curve.
- **Axial flow (Ns > 10,000):** High Q, low H. Propeller pump. Very steep curve. Used for flood control, irrigation lift, fish passage.

### By Configuration
- **Horizontal end-suction:** Most common for smaller applications. Easy maintenance.
- **Horizontal split-case:** Large capacity, double-suction impeller. High efficiency. Standard for water utility pump stations.
- **Vertical turbine (lineshaft):** Pump bowls submerged in wet well. Long shaft to surface-mounted motor. Used for deep wells and pump stations with high suction requirements.
- **Submersible:** Motor and pump submerged together. Used in wells, wet wells, and where space is limited. No long shaft.

## Pump Performance Curves

Manufacturer-provided curves show performance at a given speed:
- **Head-capacity (H-Q):** Head produced vs. flow rate. Decreasing curve for centrifugal pumps.
- **Efficiency (η-Q):** Pump efficiency vs. flow. Bell-shaped with peak at BEP (Best Efficiency Point).
- **Power (P-Q):** Power consumed vs. flow. Brake horsepower = ρgQH/(η).
- **NPSH_R (NPSHR-Q):** Net Positive Suction Head Required vs. flow. Increases with flow.

**Best Efficiency Point (BEP):** The operating point at maximum efficiency. Design should target operation within 80–110% of BEP flow for acceptable efficiency, vibration, and bearing life.

## System-Pump Interaction

### Operating Point
The intersection of the pump H-Q curve and the system head curve defines the operating point — the actual Q and H at which the system operates.

H_pump(Q) = H_system(Q)

### Multiple Pumps — Parallel
For identical pumps in parallel: combined curve doubles the flow at each head value. Total flow increases, but not by 2× because the system curve steepens at higher flow. Each pump operates at a slightly different point on its individual curve.

### Multiple Pumps — Series
Combined curve doubles the head at each flow value. Used when a single pump cannot generate sufficient head. Rare in water utility practice (multistage pumps serve the same function).

## Affinity Laws

For a given pump (same impeller diameter), changing speed from N₁ to N₂:

Q₂/Q₁ = N₂/N₁
H₂/H₁ = (N₂/N₁)²
P₂/P₁ = (N₂/N₁)³

For changing impeller diameter (same speed) from D₁ to D₂:
Q₂/Q₁ = D₂/D₁
H₂/H₁ = (D₂/D₁)²
P₂/P₁ = (D₂/D₁)³

**Variable Frequency Drives (VFDs):** Use speed affinity laws to adjust pump output to match varying demand. Energy savings are dramatic — reducing speed by 20% reduces power by ~50%. VFDs are now standard for most water utility pump stations.

## Net Positive Suction Head (NPSH)

### NPSH Available (NPSHA)
The energy available at the pump suction above the vapor pressure:

NPSHA = P_atm/(ρg) + H_s - hf_suction - Pv/(ρg)

where P_atm = atmospheric pressure, H_s = static suction head (positive if suction source is above pump, negative if below), hf_suction = friction loss in suction piping, Pv = vapor pressure of water.

### NPSH Required (NPSHR)
The minimum suction energy the pump needs to avoid cavitation. Provided by the manufacturer on the pump curve. Increases with flow rate.

### NPSH Margin
NPSHA must exceed NPSHR with adequate margin:

NPSHA ≥ NPSHR × safety factor

Hydraulic Institute recommends NPSHA ≥ 1.2 × NPSHR minimum. For critical service or variable speed operation, NPSHA ≥ 1.5–2.0 × NPSHR.

### Cavitation
When NPSHA < NPSHR, vapor bubbles form at the impeller eye and collapse violently in higher-pressure zones. Effects: noise, vibration, pitting/erosion of impeller, loss of head and capacity. Suction specific speed (Nss = N√Q / NPSHR^0.75) should be ≤ 8500–11000 (US units) for reliable operation.

## Pump Efficiency and Power

### Hydraulic Power (Water Power)
P_water = ρ × g × Q × H (watts)

### Brake Horsepower (Shaft Power)
P_brake = P_water / η_pump = ρgQH / η_pump

### Wire-to-Water Efficiency
η_total = η_pump × η_motor × η_VFD (if applicable)

Typical overall efficiency: 60–80% for well-designed pump stations. Major losses: hydraulic (pump), mechanical (bearings, seals), electrical (motor, VFD).

## Pump Station Design Considerations

- **Duty/standby arrangement:** N+1 redundancy (one standby pump for N duty pumps) is standard.
- **Turndown ratio:** Range of flow from minimum to maximum. Multiple pumps and VFDs provide turndown.
- **Suction conditions:** Adequate submergence, approach velocity, anti-vortex devices. Avoid air entrainment.
- **Vibration and noise:** Mount pumps on isolation pads. Design piping to minimize vibration transmission.
- **Surge protection:** Check valve on each pump discharge. Surge anticipator valves or other transient control if needed.
