# Pipeline Design — Materials, Wall Thickness & Layout

## Material Selection

Pipe material selection depends on: working pressure, external loads, corrosion environment, design life, available sizes, joining method, constructibility, and cost.

### Steel Pipe
- **Sizes:** 100 mm to 3600+ mm (4 in to 144+ in)
- **Pressure:** Essentially unlimited — wall thickness designed to pressure
- **Joining:** Welded (butt, lap, bell-and-spigot with O-ring), flanged, mechanical couplings
- **Lining:** Cement-mortar lining (CML) standard for water service
- **Coating:** Polyurethane, fusion-bonded epoxy, coal-tar enamel, tape wrap, cement-mortar
- **Advantages:** Highest strength-to-weight ratio, weldable for monolithic pipeline, handles high pressure and transients
- **Limitations:** Requires corrosion protection (coating + cathodic protection), higher cost at small diameters
- **Design life:** 75–100+ years with proper protection

### Ductile Iron Pipe (DIP)
- **Sizes:** 75–1600 mm (3–64 in)
- **Pressure classes:** 150, 200, 250, 300, 350 psi (per AWWA C150/C151)
- **Joining:** Push-on (Tyton), mechanical joint, restrained joint (Megalug, TR-Flex), flanged
- **Lining:** CML standard. Polyethylene encasement in corrosive soils.
- **Advantages:** Widely available, relatively easy installation, good beam strength
- **Limitations:** Heavy, corrosion in aggressive soils, limited to standard pressure classes

### Prestressed Concrete Cylinder Pipe (PCCP)
- **Sizes:** 400–3600 mm (16–144 in)
- **Types:** Lined cylinder (LCP, small diameter), embedded cylinder (ECP, large diameter)
- **Pressure:** Up to 2.75 MPa (400 psi)
- **Joining:** Rubber gasket bell-and-spigot, steel joint rings
- **Advantages:** Large diameters, corrosion resistant, high pressure capability, long segments
- **Limitations:** Brittle failure mode (prestressing wire breaks), very heavy, difficult to repair, decreasing use due to wire failure concerns

### HDPE (PE4710 / PE100)
- **Sizes:** 16–1600 mm (½–63 in)
- **Pressure ratings:** DR 7–32.5 (corresponding to various pressure classes)
- **Joining:** Heat fusion (butt, electrofusion) — monolithic, leak-free
- **Advantages:** Flexible, excellent chemical resistance, fused joints (no leaks), lightweight, excellent surge resistance (low wave speed)
- **Limitations:** Low stiffness (requires good bedding), creep, thermal expansion, limited temperature range, lower pressure ratings than steel

### PVC (C900/C905)
- **Sizes:** 100–900 mm (4–36 in)
- **Pressure classes:** 100, 150, 200, 235, 305 psi (AWWA C900)
- **Joining:** Rubber gasket bell-and-spigot, restrained joints available
- **Advantages:** Smooth interior (C=150), corrosion-free, lightweight, low cost at smaller diameters
- **Limitations:** Brittle at low temperatures, UV-sensitive, limited maximum diameter, not suitable for above-ground

## Wall Thickness Design

### Internal Pressure (Barlow Formula)

t = (P × D) / (2 × σ_allow)

where P = design pressure (working pressure + surge allowance), D = outside diameter, σ_allow = allowable stress = yield strength / factor of safety.

**Design pressure components:**
- Working pressure: maximum steady-state pressure (HGL + static head at lowest point)
- Transient (surge) pressure: from water hammer analysis
- Total design pressure = max(working + surge allowance, test pressure)

**Steel pipe (AWWA M11):** σ_allow = 0.50 × σ_y for working pressure; can use 0.75 × σ_y for working + transient. Typical steel: ASTM A36 (σ_y = 250 MPa), A572 Gr 50 (σ_y = 345 MPa).

### External Pressure / Vacuum
Pipe must resist external collapse from:
- Internal vacuum during transients
- External groundwater pressure (below water table)
- Atmospheric pressure during draining

Critical buckling pressure: P_cr = 2E(t/D)³/(1-ν²) for unsupported steel ring. Safety factor ≥ 2.0 against collapse.

### Minimum Thickness
Regardless of pressure, pipe must have sufficient thickness for:
- Handling and installation (AWWA M11: t_min = D/288 + 1.27 mm for steel)
- External load resistance (Marston-Spangler or AASHTO loading)
- Corrosion allowance (0.8–1.5 mm for unprotected steel interior)

## Thrust Restraint

At bends, tees, reducers, dead ends, and valves, unbalanced hydraulic forces act on the pipeline. These thrust forces must be resisted by:

**Thrust blocks:** Concrete blocks bearing against undisturbed soil. Bearing area = Thrust / (allowable soil bearing pressure).

**Restrained joints:** Joints that resist axial pullout force (mechanical restraint, welded joints, fused HDPE). Required length of restrained pipe on each side of the fitting calculated from force balance with soil friction.

**Anchor blocks:** Massive concrete structures that rigidly anchor the pipe. Required at major bends, transitions to above-ground, and at valve structures.

**Thrust force at bend:**
T = 2 × P × A × sin(θ/2)

where P = internal pressure, A = pipe cross-sectional area, θ = deflection angle.

## Pipeline Appurtenances

### Air Valves
- **Air/vacuum valves:** At all high points — admit air during drainage, release air during filling
- **Air release valves:** At high points and long ascending runs — release accumulated air during operation
- **Combination valves:** Both functions in one body

### Blowoffs / Drain Valves
At low points for draining, flushing sediment. Sized for practical draining time.

### Isolation Valves
Butterfly or gate valves at regular intervals (every 1.5–3 km on transmission mains) to isolate sections for maintenance without draining the entire pipeline.

### Pressure Relief Valves
Downstream of pump stations or at locations where surge could exceed pipe design pressure.

## Pipeline Alignment and Profile

- Follow roads/rights-of-way where possible
- Minimum burial depth: below frost line + 300 mm, or 900 mm (3 ft) minimum cover for traffic loads (deeper for heavy traffic)
- Avoid high points in profile (air accumulation) — vent or eliminate
- Cross existing utilities with minimum clearances per local codes
- Maintain minimum separation from sewer lines (typically 3 m horizontal, 0.45 m vertical with sewer below)
