# Gates, Valves & Flow Control

## Classification

### Surface Gates (Spillway / Crest Gates)
Control flow over or through spillway crests:

**Radial (Tainter) Gate:** Curved skin plate pivoting on trunnion pins. Hydrostatic force passes through the trunnion, so hoist force is only the gate weight component. Most common spillway gate worldwide for heads up to 20+ m. Advantages: low hoist force, reliable operation, proven design. Disadvantages: trunnion corrosion/fatigue critical, requires piers.

**Vertical Lift Gate:** Flat or curved leaf raised vertically by hoists. Simple but requires tall piers and heavy hoists (full hydrostatic load on seals). Used for moderate heads. Can be fixed-wheel or sliding.

**Drum Gate:** Hollow gate hinged at the downstream edge, operated by controlling water pressure in a chamber beneath the gate. Self-operating (no mechanical hoist). Used on long crests (e.g., Hoover Dam).

**Flap Gate (Bascule Gate):** Hinged at bottom, tips downstream under hydraulic pressure or mechanical actuation. Common for low-head applications and automatic water level control.

**Stop Logs / Bulkheads:** Individual beams or panels stacked in slots. Not for flow regulation — used for maintenance closure (dewatering). Must not be operated under unbalanced head unless specifically designed for it.

**Flashboards:** Wooden or steel panels on top of a fixed crest. Designed to fail (break away) at a predetermined water level. Provide incremental storage above the fixed crest.

**Fusegates / Fuse Plugs:** Tilting concrete or steel blocks on the spillway crest. Designed to tip and release flow at specific water levels. Self-actuating, no mechanical parts. Used for emergency spillway augmentation.

### Outlet Gates (Conduit Gates)
Control flow through conduits and outlet works:

**Slide Gate:** Flat plate moving vertically in guides. Simple and robust. High-head slide gates require significant hoist force due to friction on seals and guides. Used for guard/emergency closure and flow regulation at moderate heads.

**Fixed-Wheel Gate (Wheeled Gate):** Similar to slide gate but with wheels that roll on tracks, reducing friction. Suitable for higher-head applications. Can be used for flow regulation.

**Jet-Flow Gate:** Designed to discharge into air — the downstream conduit is expanded so the jet doesn't contact the walls. Excellent cavitation and vibration characteristics. USBR standard for high-head outlets.

### Outlet Valves
**Hollow-Jet Valve:** Cylindrical valve with a moving needle that creates an annular jet discharging into a downstream hood. Excellent energy dissipation within the valve body. Used for reservoir release and flow regulation at heads up to 300+ m.

**Howell-Bunger (Fixed-Cone) Valve:** Discharges a hollow cone of water into the atmosphere. No downstream enclosure needed — self-dissipating spray. Used for reservoir releases, especially where tailwater energy dissipation is needed.

**Needle Valve:** Internal needle moves axially to create an annular orifice. Very precise flow control. Used for high-head, small-diameter applications.

**Butterfly Valve:** Disc rotates 90° within the pipe. Compact, low cost, fast operation. Standard for pipeline isolation. Limited for flow regulation due to high losses at partial opening and potential for cavitation.

**Cone (Plug) Valve:** Conical or cylindrical plug rotates within a seat. Quarter-turn operation. Good for throttling and flow control. Higher cost than butterfly but better flow characteristics.

### Canal Gates
**Check Gates:** Maintain upstream water level in canal for turnout deliveries. Overshot (water flows over), undershot (water flows under), or combined.

**Radial Gates (small):** Used on canal checks, diversion dams, and turnouts.

**Constant-Head Orifice (CHO):** Maintains constant head differential across a turnout for metered delivery.

## Hydraulic Design Principles

### Discharge Under Gates

**Free (unsubmerged) orifice flow:**
Q = Cd × A × √(2g × H)

where Cd = discharge coefficient (0.55–0.72 depending on gate type and geometry), A = gate opening area, H = upstream head above center of opening.

**Submerged orifice flow:**
Q = Cd × A × √(2g × (H₁ - H₂))

where H₁ = upstream head, H₂ = downstream (tailwater) head.

### Gate Discharge Coefficients
Cd depends on gate type, geometry, and degree of opening:
- Radial gate: 0.60–0.72 (varies with opening and head ratio)
- Slide gate: 0.55–0.65
- Vertical lift gate (underflow): 0.55–0.70
- Orifice in wall: 0.61 (sharp-edged, standard)

### Hydrostatic Loads
For a vertical flat gate:
F = γ × h_c × A

where h_c = depth to centroid of the gate from the water surface, A = wetted area of gate. The resultant acts at the center of pressure, below the centroid.

### Hoist and Operating Forces
- **Slide gate:** Hoist force = W_gate + friction (μ × F_hydrostatic on seals + side guides). μ = 0.25–0.50 for metal on metal, 0.10–0.25 for rubber seals.
- **Radial gate:** Hoist force = W_gate × sin(θ) + seal friction. Much lower than slide gate because hydrostatic load passes through trunnion.
- **Safety factor:** Hoist capacity ≥ 1.5 × calculated maximum operating force (USACE).

### Cavitation and Vibration
Gates operating at partial openings in high-head conditions are susceptible to:
- **Cavitation:** Pressure downstream of gate drops below vapor pressure. Critical at gate openings < 50% and heads > 15–20 m. Design countermeasures: aeration, gate geometry (jet-flow design), limited operating range.
- **Flow-induced vibration:** Vortex shedding from gate lip, seal flutter, unstable shear layers. Can cause fatigue failure. Countermeasures: proper seal design, gate lip geometry, operational restrictions.

**Cavitation index:** σ = (P_d - P_v) / (ρV²/2). Incipient cavitation at σ ≈ 0.2–1.5 depending on gate type. σ < σ_incipient → cavitation damage.

## Gate Operating Strategies

- **Symmetrical operation:** On multi-gate spillways, open gates symmetrically about the channel centerline to maintain balanced flow.
- **Equal opening vs. equal flow:** Equal gate openings do not produce equal flows if heads differ. Computer-controlled systems can optimize for equal flow distribution.
- **Gate scheduling:** Pre-determined gate openings vs. reservoir level for flood operations. Published in the Water Control Manual.
- **Emergency closure:** Gates must be capable of closure under maximum flow conditions (emergency closure with full hydrostatic + hydrodynamic loads).
