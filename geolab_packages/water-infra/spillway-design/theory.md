# Spillway Design

## Purpose and Classification

A spillway is the critical hydraulic structure that safely conveys flood flows past or through a dam. Failure to adequately pass the design flood is a primary cause of dam failure, particularly for embankment dams where overtopping leads to rapid erosion.

### Classification by Function
- **Service (principal) spillway:** Designed to pass the full range of floods up to and including the IDF. Operates frequently.
- **Auxiliary (emergency) spillway:** Operates only during extreme floods exceeding the service spillway capacity. May be designed for limited use — some erosion may be acceptable.
- **Fuse plug spillway:** Designed to erode or breach at a predetermined pool elevation, providing emergency discharge. Single-use.

### Classification by Control
- **Controlled (gated):** Discharge regulated by gates (radial/tainter, vertical lift, drum). Allows reservoir level management and flood operations flexibility.
- **Uncontrolled (ungated):** Discharge determined solely by head on the crest. Simpler, no operational decisions during floods, no gate failure risk.

### Classification by Type
- **Overflow (ogee):** Water passes over a shaped crest, most common for concrete dams.
- **Chute:** Open channel conveying water from crest to downstream, common for embankment dams.
- **Side channel:** Flow enters the spillway laterally (parallel to dam axis), turns 90° into a chute.
- **Morning glory (shaft):** Circular crest drains into a vertical shaft and tunnel. Used where space is limited.
- **Labyrinth/Piano Key:** Folded crest increases effective length for a given channel width.
- **Stepped:** Steps on the chute face dissipate energy progressively. Common for RCC dams.
- **Tunnel:** Spillway discharge conveyed through a tunnel in the abutment.
- **Siphon:** Closed conduit operating by siphonic action. Limited capacity, used for small reservoirs.

## Ogee (Overflow) Spillway Design

The ogee crest profile follows the lower nappe of a sharp-crested weir at the design head (Hd). This provides the maximum discharge efficiency — atmospheric pressure on the crest surface at design head.

### WES Standard Crest Profile

**Upstream face:** Typically vertical or with a small radius curve.

**Downstream profile (USBR/WES):**
y/Hd = -K × (x/Hd)^n

where K and n depend on upstream face inclination and approach velocity. For vertical upstream face: K = 0.5, n = 1.85 (USBR standard).

### Ogee Discharge Equation
Q = C₀ × L_eff × He^1.5

where C₀ = discharge coefficient (depends on He/Hd, P/Hd, downstream submergence), L_eff = effective crest length (adjusted for piers and abutments), He = total energy head on crest including approach velocity head.

**Design head C₀:** At He = Hd, C₀ ≈ 2.18 m^0.5/s (3.95 ft^0.5/s) for the WES standard shape.

**At heads exceeding design (He > Hd):** Pressures become sub-atmospheric on the crest. C₀ increases (up to ~2.32 at He/Hd ≈ 1.5) but cavitation risk increases. Limit He/Hd ≤ 1.33 to maintain safe pressures without aeration.

**At heads below design (He < Hd):** Pressures are positive (above atmospheric). C₀ decreases. No cavitation concern.

### Effective Crest Length Correction
L_eff = L - 2(N × Kp + Ka) × He

where N = number of piers, Kp = pier contraction coefficient (0.01–0.02 for rounded piers), Ka = abutment contraction coefficient (0.10–0.20).

## Chute Spillway Design

An open channel (chute) conveys water from the spillway crest to the downstream channel. Components: control section (crest), transition, chute channel, terminal structure (energy dissipator).

### Chute Hydraulics
- Flow is typically supercritical in the chute (steep slope)
- Water surface profile computed by gradually varied flow (step-backwater) or energy equation
- Include air entrainment bulking — flow depth increases 20–40% due to self-aeration at high velocities
- Chute walls must be designed for bulked depth plus freeboard (typically 0.6–1.0 m above bulked depth)

### Air Entrainment and Cavitation
At velocities exceeding ~12 m/s (40 ft/s), cavitation becomes a concern at surface irregularities:
- **Cavitation index (σ):** σ = (P₀ - Pv) / (½ρV²). If σ < 0.2, cavitation damage likely.
- **Prevention:** Smooth surfaces (offsets < 6 mm), aerator slots/ramps to introduce air into the boundary layer, low flow velocities where possible.
- **Self-aeration:** Begins when turbulent boundary layer reaches the surface (~50–100 m downstream of crest at typical slopes). Provides natural cavitation protection.

## Labyrinth and Piano Key Weirs

Folded crest geometry increases the effective crest length within a limited channel width.

### Labyrinth Weir
Plan: trapezoidal or triangular folds. Effective length ratio L/W = 3–8 (L = total crest length, W = channel width). Discharge increases 2–4× over a straight weir for the same head and channel width at low heads. Efficiency decreases at high heads as the folds interfere.

**Discharge:** Q = Cd × (2/3) × √(2g) × L × Ht^1.5

where Cd is a function of Ht/P, L/W, sidewall angle, and crest shape (quarter-round, half-round, ogee). Tullis et al. (1995) and Crookston & Tullis (2013) provide Cd curves.

### Piano Key Weir
Overhang upstream and downstream apexes (cantilevers). More structurally efficient than labyrinth — can be placed on existing gravity dam crests with limited structural modifications. Similar hydraulic performance to labyrinth weirs.

## Stepped Spillway

Steps on the chute face dissipate energy progressively through: (1) nappe flow at low discharges (water falls as individual nappes between steps) and (2) skimming flow at high discharges (water flows as a coherent stream over the step edges with recirculating vortices in the step cavities).

**Energy dissipation:** 40–70% of total head can be dissipated on the steps, significantly reducing the size of the terminal structure.

**Design:** Step height = 0.6–1.2 m (RCC lift height). Transition from nappe to skimming flow occurs at unit discharge q ≈ 3–5 m²/s per meter of width (depends on step height). Maximum unit discharge typically limited to 15–30 m²/s for stepped spillways.

## Energy Dissipation — Stilling Basins

### Hydraulic Jump Stilling Basin
Supercritical flow from the chute enters the basin, forms a hydraulic jump, and exits as subcritical flow. Basin floor is depressed below downstream channel to force the jump to form within the basin.

**USBR Type I:** Simple flat-floor basin. No appurtenances. For Fr < 2.5 or where tailwater significantly exceeds sequent depth.

**USBR Type II:** Chute blocks + dentated end sill. For Fr > 4.5, V > 15 m/s. Reduces basin length ~33% compared to Type I.

**USBR Type III:** Chute blocks + baffle piers + solid end sill. For Fr > 4.5, V < 15 m/s, q < 18.5 m²/s. Most efficient but baffle piers cannot withstand high velocities.

**USBR Type IV:** For 2.5 < Fr < 4.5 (oscillating jump range). Large chute blocks, no baffles. Difficult to design well.

### Flip Bucket (Ski Jump)
Deflects flow into the air, forming a free jet that impacts downstream. Energy dissipated by jet breakup, aeration, and plunge pool action. Used where adequate tailwater for a stilling basin is not available and competent rock exists downstream. Jet trajectory computed by projectile equations.

### Plunge Pool
Natural or excavated pool below flip bucket or free overfall. Scour depth estimated by empirical equations (Mason & Arumugam, Bollaert). Requires competent rock or designed lined pool.
