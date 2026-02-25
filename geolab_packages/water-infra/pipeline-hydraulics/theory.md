# Pipeline Hydraulics

## Fundamental Concepts

Pipeline hydraulics deals with pressurized (full-pipe) flow of water through closed conduits. Unlike open-channel flow, the driving force is the pressure difference between upstream and downstream, supplemented by elevation differences.

### Energy Grade Line (EGL) and Hydraulic Grade Line (HGL)

**EGL:** Total energy head at any point = z + P/(γ) + V²/(2g). The EGL always slopes downward in the direction of flow (unless a pump adds energy).

**HGL:** Piezometric head = z + P/(γ). The HGL is below the EGL by the velocity head V²/(2g). For constant-diameter pipe, V²/(2g) is constant, so HGL and EGL are parallel.

**Critical design check:** The HGL must remain above the pipe crown at all points along the pipeline profile. If the HGL drops below the pipe, negative pressures develop — risk of cavitation, air entrainment, and column separation.

## Steady-State Friction Losses

### Darcy-Weisbach Equation

The fundamental and theoretically sound equation for pipe friction:

hf = f × (L/D) × V²/(2g)

where f = Darcy-Weisbach friction factor (dimensionless), L = pipe length, D = internal diameter, V = mean velocity.

**Friction factor f** depends on Reynolds number (Re = VD/ν) and relative roughness (ε/D):
- Laminar flow (Re < 2000): f = 64/Re
- Turbulent flow: Colebrook-White equation (implicit) or Swamee-Jain (explicit approximation)

**Moody diagram** provides f graphically as a function of Re and ε/D. Key zones: laminar, transition, fully rough (f independent of Re).

### Hazen-Williams Equation

Empirical, widely used in water distribution practice:

V = k × C × R^0.63 × S^0.54 (SI: k = 0.849; US: k = 1.318)

or equivalently:

hf = (10.67 × Q^1.852) / (C^1.852 × D^4.87) × L (SI, hf in m, Q in m³/s, D in m)

where C = Hazen-Williams roughness coefficient. Only valid for water near 15°C in turbulent flow (Re > 4000). Not dimensionally homogeneous — use Darcy-Weisbach for precision work.

### Manning's Equation (for Full Pipe)
Sometimes used for gravity-flow pipelines:
V = (1/n) × R^(2/3) × S^(1/2) where R = D/4 for full circular pipe.

## Minor (Local) Losses

Head loss at fittings, valves, bends, transitions:

hm = K × V²/(2g)

where K = loss coefficient. Total system loss = Σ(friction) + Σ(minor losses).

**Equivalent length method:** Each fitting expressed as an equivalent length of straight pipe: Le = K × D / f. Useful for quick estimates.

For long transmission pipelines, minor losses are typically 5–15% of friction losses. For short, complex piping systems (pump stations), minor losses can dominate.

## System Curves

The system head curve plots the total head required (static lift + friction + minor losses) as a function of flow rate:

H_system = H_static + hf(Q) + hm(Q)

H_static is constant (elevation difference between source and destination). Friction and minor losses increase approximately with Q².

The operating point is where the system curve intersects the pump curve (for pumped systems) or where the available head equals the required head (for gravity systems).

## Water Hammer (Hydraulic Transients)

### Joukowsky Equation

Instantaneous valve closure (or pump trip) generates a pressure wave:

ΔP = ρ × a × ΔV   or   ΔH = (a × ΔV) / g

where a = wave speed (celerity) in the pipeline, ΔV = change in velocity.

### Wave Speed

a = √(K/ρ) / √(1 + (K×D)/(E×t) × c₁)

where K = bulk modulus of water (~2.2 GPa), E = modulus of elasticity of pipe wall, t = wall thickness, D = internal diameter, c₁ = pipe restraint factor (1.0 for thin-walled, anchored pipe).

**Typical wave speeds:** Steel pipe: 900–1200 m/s. DIP: 1000–1200 m/s. Concrete: 900–1100 m/s. PVC: 300–500 m/s. HDPE: 200–400 m/s.

### Critical Time

The time for the pressure wave to travel from the valve to the reservoir and back:

T_cr = 2L/a

If valve closure time tc < T_cr: "rapid" closure — full Joukowsky pressure develops.
If tc > T_cr: "slow" closure — pressure buildup is attenuated.

### Transient Control

- **Slow valve closure:** Program closure so that tc > 5–10 × T_cr
- **Surge tanks:** Open tanks or standpipes that absorb/supply water during transients
- **Air/vacuum valves:** Allow air in during negative pressure waves, release air during positive waves
- **Pressure relief valves:** Open at set pressure to discharge water
- **Flywheels on pumps:** Extend pump deceleration time after power failure
- **Check valves with dampeners:** Prevent reverse flow while managing slam

### Transient Analysis

Simple systems: rigid-column theory or algebraic (Joukowsky for screening).
Complex systems: Method of Characteristics (MOC) computer analysis. Industry-standard software: Bentley HAMMER, AFT Impulse, KYPipe.

## Air Management in Pipelines

Air in pipelines causes:
- Reduced capacity (air pockets at high points)
- Transient amplification
- Corrosion (dissolved oxygen)

**Air valves** are installed at:
- High points along the profile (combination air/vacuum valves)
- Pipeline summits (large-orifice air/vacuum valves for filling/draining)
- Downstream of control valves (small-orifice air release valves)
- Long descending sections (at regular intervals)

**Blowoffs (drain valves)** at low points for pipeline draining and sediment flushing.

## Pipeline Design Velocities

Velocity affects friction loss, pipe size, cost, and transient severity.

**Economic velocity:** Balances capital cost (larger pipe = more cost, less head loss) against operating cost (pumping energy). Typically 0.9–2.4 m/s (3–8 ft/s) for transmission mains.

**Minimum velocity:** ≥ 0.6 m/s (2 ft/s) to prevent sedimentation.

**Maximum velocity:** ≤ 3.0 m/s (10 ft/s) typical limit. Higher velocities increase friction, transient risk, erosion, and noise.
