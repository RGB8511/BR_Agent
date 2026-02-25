# Open Channel Hydraulics

## Fundamental Concepts

Open channel flow has a free surface exposed to atmospheric pressure, distinguishing it from pipe flow. The driving force is gravity (slope), resisted by boundary friction.

### Flow Classification
- **Steady vs. unsteady:** Conditions at a point change (or not) with time
- **Uniform vs. non-uniform:** Conditions change (or not) along the channel
- **Subcritical (Fr < 1):** Slow, deep, tranquil flow — controlled from downstream
- **Supercritical (Fr > 1):** Fast, shallow, rapid flow — controlled from upstream
- **Critical (Fr = 1):** Transition condition — minimum specific energy for a given discharge

### Geometric Parameters
- **Wetted perimeter (P):** Length of channel boundary in contact with water
- **Hydraulic radius (R):** R = A/P where A = cross-sectional flow area
- **Top width (T):** Width of the free surface
- **Hydraulic depth (D):** D = A/T

## Uniform Flow

Uniform flow occurs when depth, velocity, and cross-section are constant along the channel. Gravity force balances friction force exactly. The water surface is parallel to the channel bed (slope S₀ = energy slope Sf).

### Manning's Equation
The most widely used open-channel flow formula:

V = (k/n) × R^(2/3) × S^(1/2)

where k = 1.0 (SI, m) or 1.486 (US customary, ft), n = Manning's roughness coefficient, R = hydraulic radius, S = slope.

Discharge form: Q = (k/n) × A × R^(2/3) × S^(1/2)

Manning's n is the critical parameter — selected from tables based on channel material, vegetation, irregularity, and obstructions.

### Chézy Equation
V = C × √(R × S)

where C = Chézy coefficient. Related to Manning's: C = (k/n) × R^(1/6).

### Normal Depth
The depth at which uniform flow occurs for a given Q, n, S₀, and channel geometry. Found by solving Manning's equation iteratively (no closed-form for most channel shapes).

## Energy Concepts

### Specific Energy
E = y + V²/(2g) = y + Q²/(2gA²)

where y = flow depth, V = mean velocity. At critical flow, specific energy is minimum for a given Q.

### Froude Number
Fr = V / √(gD) = V / √(g × A/T)

Fr < 1: subcritical. Fr = 1: critical. Fr > 1: supercritical.

### Critical Depth
For rectangular channels: yc = (q²/g)^(1/3) where q = Q/b (discharge per unit width).

General: Q²T/(gA³) = 1 at critical conditions.

### Energy Equation (Bernoulli for Open Channels)
z₁ + y₁ + V₁²/(2g) = z₂ + y₂ + V₂²/(2g) + hf + hL

where z = bed elevation, hf = friction loss, hL = local (minor) losses.

## Gradually Varied Flow (GVF)

Water surface profile changes gradually along the channel. Governed by:

dy/dx = (S₀ - Sf) / (1 - Fr²)

where S₀ = bed slope, Sf = friction slope (from Manning's at local depth). This ODE is solved numerically (standard step method in HEC-RAS).

### Profile Classifications
Named by channel slope type and zone:
- **M profiles (mild slope, S₀ < Sc):** M1 (backwater), M2 (drawdown), M3 (below normal and critical)
- **S profiles (steep slope, S₀ > Sc):** S1, S2, S3
- **C profiles (critical slope):** C1, C3
- **H profiles (horizontal):** H2, H3
- **A profiles (adverse slope):** A2, A3

## Rapidly Varied Flow

### Hydraulic Jump
Transition from supercritical to subcritical flow with significant energy loss. Conjugate (sequent) depths for rectangular channel:

y₂/y₁ = 0.5 × [-1 + √(1 + 8Fr₁²)]

Energy loss: ΔE = (y₂ - y₁)³ / (4y₁y₂)

### Weirs and Sharp-Crested Overflow
Rectangular weir: Q = Cd × (2/3) × √(2g) × L × H^(3/2)

V-notch (triangular) weir: Q = Cd × (8/15) × √(2g) × tan(θ/2) × H^(5/2)

where Cd = discharge coefficient, L = crest length, H = head above crest, θ = notch angle.

## Culvert Hydraulics

Culverts can operate under inlet control (capacity limited by inlet geometry) or outlet control (capacity limited by barrel friction and tailwater).

**Inlet control:** Flow passes through critical depth near entrance. Headwater determined by inlet geometry, not barrel characteristics.

**Outlet control:** Barrel flows full or partially full. Headwater determined by friction losses, outlet conditions, and tailwater depth.

FHWA HDS-5 provides nomographs and equations for both conditions. Design headwater is the larger of inlet-control and outlet-control headwater.
