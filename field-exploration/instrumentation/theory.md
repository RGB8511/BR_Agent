# Geotechnical Instrumentation & Monitoring

## Instrumentation Philosophy

Dunnicliff's principle: "Every instrument installed should be selected and placed to assist in answering a specific question." Instrumentation programs fail when instruments are installed without clear objectives or when data is collected but never analyzed.

**Key questions instrumentation answers:**
- Is the design performing as predicted? (verification)
- Are conditions changing that could affect safety? (safety monitoring)
- What are the actual field conditions? (characterization)
- Can construction proceed safely? (construction control)

## Pore Water Pressure Measurement

### Standpipe Piezometer (Open)
Simplest type — a small-diameter pipe with a porous tip or screened section installed in a borehole. Water rises in the standpipe to the equilibrium piezometric level.

**Advantages:** Simple, reliable, self-de-airing, no electronics to fail, can measure permeability (slug test), inexpensive.
**Limitations:** Slow response in low-permeability soils (days to weeks in clay), reads only positive pore pressure, vulnerable to damage, cannot be read remotely without adding transducer.

**Response time:** t₉₅ ≈ (F × V_standpipe) / (k × A_tip) where F = intake shape factor, V = volume of water change needed, k = permeability, A = intake area. In clay (k = 10⁻⁹ m/s), response can take weeks.

### Vibrating Wire Piezometer (VWP)
Most widely used electronic piezometer. A tensioned steel wire vibrates at a frequency that changes with applied pressure on the diaphragm.

**Advantages:** Excellent long-term stability, small volume change (fast response even in clay), remote readout, suitable for automated data acquisition, lightning-resistant signal.
**Limitations:** Cannot be recalibrated after installation, wire can corrode if saturated (sealed units preferred), not self-de-airing.

**Measurement:** Pore pressure = calibration factor × (f₁² - f₀²) + temperature correction, where f = resonant frequency in Hz.

### Pneumatic Piezometer
Gas-operated — applies gas pressure to balance pore water pressure on a diaphragm. When gas pressure equals pore pressure, flow occurs through the return line.

**Advantages:** No electronics in the ground, can be read from remote panel, fast response.
**Limitations:** Requires gas supply (nitrogen), tubing can be damaged or blocked, limited in deep installations, less common now due to VWP availability.

## Deformation Measurement

### Inclinometers
Measure lateral deformation profile along a borehole. A probe with accelerometers traverses a grooved casing, measuring tilt at regular intervals (typically 0.5 m).

**Types:**
- **Traversing (manual) inclinometer:** Probe lowered in casing, readings taken at each depth. Accuracy ±2 mm per 25 m typical. Standard for deep lateral movement monitoring.
- **In-place inclinometers (IPI):** Fixed sensors at specific depths, connected to datalogger. Continuous real-time data but only at sensor locations.
- **Shape Accel Array (SAA):** Rigid segments with MEMS accelerometers, installed in casing. Continuous profile at 0.3–1.0 m intervals with real-time data. Becoming standard for critical applications.

**Casing:** 70 mm (2.75 in) OD with 4 orthogonal grooves for probe orientation. Grouted into borehole with grout stiffness matched to surrounding soil. Bottom of casing must be in stable ground (anchor zone).

**Data processing:** Displacement = Σ(L_i × sin θ_i) summed from bottom. Systematic errors (bias shift) can accumulate — always check "A+B" checksums.

### Settlement Measurement

- **Settlement plates:** Steel plate on fill surface with riser pipe extending upward as fill is placed. Survey the top of the riser. Simple, reliable, measures total settlement of the plate elevation.
- **Settlement gauges (hydraulic/pneumatic):** Measure settlement below fill. Liquid-filled tube connects embedded plate to readout panel. Operates on manometer principle.
- **Magnetic extensometers (Sondex):** Spider magnets installed in borehole at various depths. Probe measures magnet positions. Provides settlement profile with depth.
- **Horizontal inclinometer:** Inclinometer casing installed horizontally in fill — measures settlement profile along length. Good for embankments.
- **Multi-point borehole extensometer (MPBX):** Anchors at various depths in a borehole, connected by rods or wires to a head at the surface. Measures relative displacement between anchor points. Standard for tunnel and excavation monitoring.
- **Survey monuments:** Precise leveling or GPS survey of surface points. Accuracy ±1 mm (precise leveling) to ±3 mm (GPS). Essential for long-term monitoring.

### Automated Total Stations (AMTS)
Robotic total stations that automatically measure angles and distances to prism targets on structures, slopes, or retaining walls. Real-time 3D displacement monitoring. Accuracy ±1–3 mm depending on distance. Increasingly common for construction monitoring.

## Stress and Load Measurement

### Earth Pressure Cells
Flat, fluid-filled cells that measure total stress in soil. Two types:
- **Embedded cells:** Placed within fill during construction. Measure vertical or horizontal total stress.
- **Contact (push-in) cells:** Pushed into soft soil. Measure in-situ lateral stress.

**Caution:** Soil arching around rigid cells can cause readings to differ from true stress. Cell must be much stiffer than surrounding soil. Calibration and interpretation require experience.

### Load Cells
Measure force in structural elements:
- **Vibrating wire load cells:** For anchor loads, strut loads, pile loads. Ring cells or flat-jack cells.
- **Strain gauge load cells:** Higher accuracy, faster response. Common for load testing.
- **Hydraulic load cells (flat jacks):** Fluid-filled, robust. Common for tunnel support and mining.

### Strain Gauges
Measure strain in structural members (steel, concrete, shotcrete). Sister bar (rebar-mounted VW gauges), spot-weldable gauges for steel, embedment gauges for concrete. Strain × E × A = force.

## Temperature Measurement

Thermistors and thermocouples embedded in concrete (mass concrete temperature monitoring), dam cores, and foundation grouting zones. VW piezometers typically include integral thermistors.

## Data Acquisition and Management

### Manual Reading
Portable readout units for VW instruments, inclinometer probes, survey crews. Labor-intensive but provides quality-checked data.

### Automated Data Acquisition Systems (ADAS)
Dataloggers connected to instruments via cables. Read at programmable intervals (minutes to hours). Data transmitted via cellular, radio, satellite, or fiber optic to central database. Essential for real-time monitoring of critical structures.

### Trigger Levels and Response Plans
Instrumentation data is compared against pre-established trigger levels (green/yellow/red or similar). Each level has defined response actions: increase monitoring frequency, notify engineer, implement contingency plan, evacuate.
