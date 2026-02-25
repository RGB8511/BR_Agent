# Canal Design

## Overview

Canals are open channels constructed to convey water for irrigation, municipal supply, hydropower, navigation, or drainage. Design must balance hydraulic efficiency, structural stability, seepage control, cost, and constructibility.

## Canal Classification

### By Lining
- **Unlined (earthen):** Lowest construction cost, highest seepage loss and maintenance. Suitable where seepage loss is acceptable, soils are erosion-resistant, and water cost is low.
- **Lined:** Concrete, shotcrete, geomembrane, compacted clay, or combinations. Reduces seepage 60–95%, allows higher velocity, steeper slopes, and smaller cross-section.

### By Function
- **Main canal:** Conveys water from source (dam, diversion) to distribution system. Largest capacity.
- **Branch canal:** Distributes water from main canal to laterals.
- **Lateral:** Delivers water to individual farms or delivery points.
- **Sublateral / farm ditch:** On-farm distribution.

### By Flow Regime
- Subcritical (Froude number < 1) is standard — all canals are designed for subcritical, uniform flow under normal operation. Supercritical flow may occur in chutes and drops.

## Hydraulic Design

### Design Discharge
Canal capacity is set by the maximum delivery requirement plus conveyance losses:

Q_design = Q_delivery / (1 - L_loss)

where L_loss = fractional seepage + evaporation loss over the canal reach.

### Manning's Equation (Primary Design Tool)
Q = (1/n) × A × R^(2/3) × S^(1/2)

Design process: given Q and S (from topography/energy gradient), select n (from lining material), then solve for cross-section geometry (width b, depth y, side slope z) that produces the required area and hydraulic radius.

### Best Hydraulic Section
The cross-section with maximum hydraulic radius (minimum wetted perimeter) for a given area:
- **Trapezoidal:** Half-hexagon shape where R = y/2. Side slope z = 1/√3 (≈ 0.577 or about 30° from vertical). Ratio b/y = 2/√3 ≈ 1.155.
- **Rectangular:** b = 2y, R = y/2.

In practice, the best hydraulic section is rarely used exactly — side slopes are governed by soil stability, and width-to-depth ratio may be adjusted for constructibility or freeboard.

### Practical Cross-Section Design
For trapezoidal canals:
- **Side slopes:** Governed by soil stability (see table). Typical: 1.5:1 to 2:1 (H:V) for earth, 1:1 for lined, 0.5:1 or vertical for concrete-lined.
- **Bottom width-to-depth ratio (b/y):** 1.0–4.0 typical. Wider channels are more stable but use more land. USBR uses b/y ≈ 1.5–3.0 for most canals.
- **Bed slope (S):** Set by topography and energy requirements. Typical: 0.00005 to 0.001 (1:20,000 to 1:1,000). Steeper slopes → faster velocity → more erosion risk.

## Velocity Constraints

### Maximum Velocity (Erosion Limit)
Velocity must not exceed the erosion threshold of the channel boundary:
- **Unlined earth:** 0.5–1.5 m/s depending on soil (see permissible velocity tables)
- **Grass-lined:** 1.2–1.8 m/s
- **Concrete-lined:** 4.0–6.0 m/s
- **Riprap-lined:** 2.5–4.0 m/s

### Minimum Velocity (Sedimentation Limit)
Velocity must be sufficient to prevent sedimentation:
- Minimum: 0.3–0.6 m/s for clear water
- For sediment-laden water: use tractive force or regime theory

### Tractive Force Method
The boundary shear stress must not exceed the critical tractive stress of the bed/bank material:

τ₀ = γ × R × S ≤ τ_cr

where τ₀ = average boundary shear stress, R = hydraulic radius, S = bed slope, τ_cr = critical tractive stress of the boundary material. Bank shear is about 0.75 × τ₀ on a trapezoidal section.

## Regime Theory (Alluvial Canals)

For canals carrying sediment-laden water in alluvial soils, regime theory provides self-adjusting (equilibrium) channel dimensions.

### Lacey's Regime Equations
Developed from canal data in the Indian subcontinent:
- P = 4.75 × √Q (wetted perimeter, m; Q in m³/s)
- R = 0.47 × (Q/f)^(1/3) (hydraulic radius)
- S = 0.0003 × f^(5/3) / Q^(1/6) (regime slope)
- V = 0.630 × (f × R)^(0.5) (regime velocity)

where f = Lacey's silt factor (1.0 for medium sand, 0.5 for fine silt, 1.5 for coarse sand).

### Kennedy's Equation
V₀ = 0.55 × y^0.64 (critical velocity to prevent silting/scouring in Indian canals)

Used with Manning's equation to design non-silting, non-scouring channels.

## Freeboard

Freeboard = height of canal bank above design water surface.

Accounts for: wave action, operational surges, wind setup, measurement/estimation uncertainty, and settlement.

**USBR guidelines:**
- Small canals (Q < 0.5 m³/s): 0.15–0.30 m
- Medium canals (0.5–15 m³/s): 0.30–0.60 m
- Large canals (> 15 m³/s): 0.60–1.0+ m

Additional freeboard for: wind exposure, curves (superelevation), check gate operation, and ice.

## Seepage Loss

Seepage from unlined canals is a major water loss — 15–45% of flow in pervious soils.

### Estimation Methods
- **Moritz formula:** q_s = 0.0375 × C_s × √(Q/V) (q_s in m³/s per km; empirical, C_s = soil factor)
- **Darcy's law-based:** q_s = k × i × A_wetted (where k = soil permeability, i = hydraulic gradient ≈ 1.0 for shallow groundwater)
- **Canal ponding test:** Fill a section, measure drop over time

### Lining Types (see canal-lining package for details)
Concrete (most durable, 85–95% seepage reduction), geomembrane (90–99%), compacted clay (50–80%), shotcrete (80–90%).

## Canal Transitions

Transitions connect canal sections of different geometry (changes in width, depth, or slope):
- **Inlet/outlet transitions:** Connect canal to structures (flumes, siphons, turnouts)
- **Gradual transitions:** Converging or diverging walls, typically 12.5:1 to 4:1 (length:width change)
- **Energy loss in transitions:** Contraction: hL = 0.10 × ΔV²/(2g). Expansion: hL = 0.30 × ΔV²/(2g) (USBR values).
