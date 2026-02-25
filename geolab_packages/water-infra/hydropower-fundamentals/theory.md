# Hydropower Fundamentals

## Hydropower Concept

Hydropower converts the potential energy of water (elevation head) to mechanical energy (turbine rotation) and then to electrical energy (generator). The power available is proportional to the product of flow rate and head.

### Classification by Head
- **High head (> 100 m):** Pelton turbine. Long penstocks or steep drops. Storage or diversion schemes.
- **Medium head (30–100 m):** Francis turbine. Dam or diversion schemes.
- **Low head (< 30 m):** Kaplan or propeller turbine. Run-of-river, canal drops, navigation dams.

### Classification by Operation
- **Storage (reservoir):** Dam impounds water; releases controlled for peaking power. High capacity factor flexibility.
- **Run-of-river:** Little or no storage. Power generation follows natural flow (baseload). Low environmental impact. Diversion weir + penstock typical.
- **Pumped storage:** Two reservoirs at different elevations. Pump water uphill during low demand; generate during peak. Energy storage, not energy source.
- **In-conduit / water supply:** Turbine replaces pressure-reducing valve in pipelines. Recovers energy that would otherwise be dissipated.

### Classification by Size
- **Large hydro:** > 30 MW
- **Small hydro:** 1–30 MW
- **Mini hydro:** 100 kW–1 MW
- **Micro hydro:** 5–100 kW
- **Pico hydro:** < 5 kW

## Power and Energy

### Hydraulic Power Available
P_hydraulic = ρ × g × Q × H_gross

### Net Power at Generator
P_gen = ρ × g × Q × H_net × η_turbine × η_generator

where H_net = H_gross - head losses (penstock friction, trash rack, intake, valves).

### Annual Energy
E = P_rated × CF × 8760 hours/year (kWh)

where CF = capacity factor (ratio of actual output to rated capacity, annualized).

Alternatively: E = Σ(P_i × Δt_i) over the year, using flow duration data.

## Turbine Types

### Pelton Turbine (Impulse)
- **Head range:** 50–1800+ m
- **How it works:** One or more high-velocity jets strike bucket-shaped vanes on a runner. All energy conversion occurs in the jet (at atmospheric pressure). Runner operates in air.
- **Specific speed:** Ns = 4–60 (US), very low.
- **Efficiency:** Peak 90–93%, good part-load by shutting off jets.
- **Variants:** Single jet, multi-jet (2, 4, or 6 jets for higher flow/power).
- **Application:** Mountain hydro, high head with limited flow.

### Francis Turbine (Reaction)
- **Head range:** 10–700 m
- **How it works:** Water enters spiral casing, passes through adjustable wicket gates, flows radially inward through the runner (energy extracted by both pressure and velocity change), and exits axially through a draft tube. Runner is fully submerged.
- **Specific speed:** Ns = 60–400 (US).
- **Efficiency:** Peak 92–95%, moderate part-load efficiency.
- **Application:** Most widely used turbine type worldwide. Covers broadest range of head and flow.

### Kaplan Turbine (Reaction, Axial)
- **Head range:** 2–70 m
- **How it works:** Water passes through wicket gates and flows axially through adjustable-blade propeller runner. Double regulation (wicket gates + blade angle) gives excellent part-load efficiency.
- **Specific speed:** Ns = 300–900 (US), highest.
- **Efficiency:** Peak 90–93%, excellent part-load due to double regulation.
- **Variants:** Fixed-blade propeller (lower cost, poor part-load), semi-Kaplan (adjustable blades, fixed gates), bulb turbine (horizontal, in-stream).
- **Application:** Low-head, high-flow sites. Navigation dams, run-of-river.

### Crossflow (Banki-Michell) Turbine
- **Head range:** 2–200 m (versatile)
- **Simple construction:** Water passes through runner blades twice. Lower peak efficiency (80–85%) but relatively flat efficiency curve and easy to manufacture. Popular for small/mini hydro in developing regions.

## Turbine Selection

Turbine type is selected primarily by specific speed, which depends on head and flow:

Ns = N × √P / H^(5/4) (US: N in rpm, P in hp, H in ft)

At each specific speed, there is an optimal turbine type that gives maximum efficiency. Turbine manufacturers provide selection charts mapping H and Q to recommended turbine types.

## Penstock Design

The penstock conveys water from the intake or forebay to the turbine.

**Sizing:** Economic diameter balances capital cost (larger pipe = more steel cost) vs. energy loss (smaller pipe = more friction loss = less revenue). Rule of thumb: head loss in penstock ≤ 4–8% of gross head.

**Material:** Steel (most common for high head), HDPE (small/micro hydro), GRP, concrete.

**Surge analysis:** Mandatory — load rejection causes water hammer. Surge tank or relief valve typically required. Wave speed and Joukowsky equation apply (see pipeline-hydraulics package).

## Draft Tube

For reaction turbines (Francis, Kaplan), the draft tube recovers kinetic energy at the runner exit by converting velocity head back to pressure head through diffusion.

**Height limitation:** The draft tube sets the turbine elevation relative to tailwater. The turbine must be set low enough to maintain adequate pressure at the runner exit — otherwise cavitation occurs.

**Thoma cavitation coefficient:** σ_T = (P_atm - P_v)/(ρgH) - H_s/H, where H_s = turbine setting above tailwater. The turbine must be set so σ ≥ σ_critical (from model test). At high elevation, lower atmospheric pressure requires the turbine to be set lower (sometimes below tailwater).

## Powerhouse Layout

- **Surface powerhouse:** At dam toe or at end of penstock. Most common.
- **Underground powerhouse:** In rock cavern. Used for high-head schemes where surface space is limited or for security/aesthetics.
- **Semi-outdoor / indoor:** Climate-dependent.

Key spaces: turbine floor, generator floor, erection bay (for maintenance), control room, transformer bay, switchyard.

## Environmental Considerations

- Fish passage (upstream and downstream)
- Minimum instream flow requirements
- Dissolved oxygen in releases
- Sediment transport continuity
- Thermal effects (hypolimnetic releases from deep reservoirs)
- Recreation and aesthetics
