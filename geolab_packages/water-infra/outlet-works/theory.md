# Outlet Works Design

## Purpose and Functions

Outlet works provide controlled release of water from a reservoir for:
- **Water supply delivery:** Irrigation, municipal, industrial
- **Flood control releases:** Controlled drawdown of flood storage
- **Environmental flows:** Minimum releases for downstream ecology
- **Reservoir drawdown:** Emergency or maintenance lowering of pool
- **Power generation bypass:** When turbines are offline

Every dam requires outlet works capable of drawing down the reservoir in a reasonable time. USBR typically requires capability to lower the reservoir by at least the depth of the flood surcharge pool within a specified period, and many agencies require the ability to drain the reservoir completely for inspection.

## System Components

### Intake Structure
The upstream entrance to the conduit system. Types include:

**Intake tower (wet tower):** Freestanding or dam-attached concrete tower in the reservoir. Multiple intake ports at different elevations allow selective withdrawal (temperature/water quality control). Access bridge connects to dam crest. Most common for large dams.

**Submerged intake:** Intake at the upstream end of a conduit through or under the dam. Simpler than a tower. Limited to single-level withdrawal.

**Inclined intake:** Intake structure built on the upstream slope of an embankment dam. Multiple ports at different elevations. Less common — structural stability on slope is challenging.

### Trashrack
Screens at the intake entrance to prevent debris, ice, and aquatic life from entering the conduit. Design considerations:
- Bar spacing: 75–150 mm (3–6 in) typical for large outlets
- Structural design for differential head (partial clogging: assume 50% blocked)
- Velocity through gross rack area: ≤ 0.6 m/s (2 ft/s) to minimize head loss and fish impingement
- Vibration: ensure natural frequency of bars avoids vortex shedding frequency

### Conduit
The pipe or tunnel conveying water through or under the dam.

**Through-dam conduit (embankment):** Steel pipe encased in concrete, placed in a trench in the foundation. Critical concern: differential settlement between the rigid conduit and the compressible embankment — seepage paths along the conduit are a primary failure mode. FEMA 484 provides detailed guidance.

**Through-dam conduit (concrete dam):** Formed opening within the dam body. Lined with steel plate at high-velocity sections.

**Tunnel:** Excavated through abutment rock. Lined with concrete or steel. Used where a conduit through the dam is impractical.

**Anti-seep collars/filter collars:** Historically, anti-seep collars (concrete fins around the conduit) were used to lengthen the seepage path. Modern practice (FEMA 484) favors filter/drain zones around the conduit as more reliable — collars are difficult to compact around and can create the problem they intend to solve. Filter diaphragms at the downstream end of the impervious zone are the current standard of practice.

### Gates and Valves

**Guard gate (upstream):** Normally open, used for emergency closure or maintenance isolation. Allows dewatering of the conduit for downstream valve maintenance. Must be operable under full reservoir head with flow through the conduit.

**Regulating gate/valve (downstream):** Controls flow rate. Located at or near the downstream end of the conduit to minimize conduit pressure during operation.

**Common types for outlet works:**
- Slide gates (rectangular openings, moderate heads)
- Fixed-wheel gates (high-head, large openings)
- Jet-flow gates (high-head, free discharge, USBR design)
- Hollow-jet valves (fixed-cone, high-head, excellent energy dissipation in free discharge)
- Needle valves (tubular, interior needle regulates annular orifice)
- Butterfly valves (guard service, not throttling)
- Ball/plug valves (full-bore, guard service)
- Howell-Bunger (fixed-cone dispersion) valves

## Hydraulic Design

### Conduit Sizing
Full-flow conduit capacity determined by energy equation:

H = Σ(hL) = h_entrance + h_friction + h_bends + h_gate + h_exit

where H = net head (reservoir to tailwater or discharge point).

For pressurized conduit:
Q = Cd × A × √(2gH_net)

where Cd accounts for all losses. Typically Cd = 0.6–0.8 depending on geometry and fittings.

### Pressure Conduit Flow
Apply energy equation from reservoir surface to discharge point:

H_reservoir = H_tailwater + V²/(2g) + Σ(K × V²/(2g)) + f(L/D)(V²/(2g))

where K = loss coefficients for entrance, bends, gates, transitions, exit.

### Free-Flow vs. Pressure-Flow Transitions
Conduit may flow partially full (free-surface) at low reservoir levels or with gate partially open. Transitions between free-surface and pressurized flow can cause instabilities (slug flow, air entrainment). Design to avoid operating in the transition zone — conduit should be clearly either free-surface or pressurized.

### Air Demand
When a guard gate is upstream and the regulating gate is downstream, the conduit between them can develop sub-atmospheric pressure. An air vent is required downstream of the guard gate to:
- Prevent conduit collapse from vacuum
- Prevent unstable flow (slam, surge)
- Provide air for free-discharge energy dissipation

Air demand: Q_air / Q_water ≈ 0.03 to 0.25 (depends on gate geometry and Froude number downstream of gate). Size air vent for maximum air velocity ≤ 45 m/s (150 ft/s) to limit noise and head loss.

### Cavitation in Conduits and Gates
High-velocity flow past gates, offsets, and changes in section can produce cavitation. Cavitation index σ = (P - Pv)/(½ρV²). At partially open gates, local velocities can be 2–4× the average conduit velocity. Design gate slots and transitions to maintain σ > 0.2. Aerate downstream of gates where needed.

## Energy Dissipation for Outlet Works

### Stilling Basin (Submerged Discharge)
Similar to spillway stilling basins. Outlet flow enters a basin, forms a hydraulic jump. USBR impact-type basins (Type VI) for small outlets. Plunge pool or basin for larger outlets.

### Free Discharge (Valve/Gate Dissipation)
Hollow-jet valves and Howell-Bunger valves discharge into the atmosphere, breaking the jet into spray that dissipates energy by aeration and impact. Requires adequate area downstream to contain spray.

### Flip Bucket / Trajectory
Similar to spillway flip buckets. Used where a stilling basin is impractical and competent rock exists downstream.

## Conduit Through Embankment Dams — Critical Design Issues

Per FEMA 484:
- Conduit must be founded on competent, non-erodible material (rock preferred, or structural fill designed as filter)
- Filter diaphragm at downstream end of impervious zone — critical for preventing internal erosion along the conduit
- No joints in the conduit through the impervious zone (continuous steel pipe, welded)
- Cradle/encasement of unreinforced or lightly reinforced concrete
- Compaction of fill around conduit: critical — use hand-operated equipment in restricted zones
- Instrumentation: piezometers at filter diaphragm, seepage measurement at conduit outlet
