# Rock Mass Classification Systems (RMR & Q)

## Rock Mass Rating (RMR) — Bieniawski 1989

### Overview
RMR is an additive rating system summing five parameters to give a total score (0–100). Originally developed for tunneling, widely adapted for slopes, foundations, and mining.

### Rating Parameters

**A1 — Strength of Intact Rock (0–15 points)**
Based on UCS or point load index. UCS > 250 MPa = 15 pts; UCS 1–5 MPa = 1 pt.

**A2 — RQD (3–20 points)**
RQD 90–100% = 20 pts; RQD < 25% = 3 pts.

**A3 — Spacing of Discontinuities (5–20 points)**
Spacing > 2 m = 20 pts; spacing < 60 mm = 5 pts.

**A4 — Condition of Discontinuities (0–30 points)**
Most influential parameter. Considers:
- Persistence (length): < 1m = 6 pts; > 20m = 0 pts
- Aperture: none = 6 pts; > 5mm = 0 pts
- Roughness: very rough = 6 pts; slickensided = 0 pts
- Infilling: none = 6 pts; soft > 5mm = 0 pts
- Weathering: unweathered = 6 pts; decomposed = 0 pts

**A5 — Groundwater (0–15 points)**
Completely dry = 15 pts; flowing = 0 pts.

**B — Orientation Adjustment (-60 to 0)**
Adjustment for unfavorable discontinuity orientation relative to excavation. Very unfavorable for tunneling = -12; for slopes = -60.

### RMR Classification
- RMR 81–100: Class I — Very good rock
- RMR 61–80: Class II — Good rock
- RMR 41–60: Class III — Fair rock
- RMR 21–40: Class IV — Poor rock
- RMR < 21: Class V — Very poor rock

### Design Applications
- Stand-up time and span correlations for unsupported excavations
- Support requirements (bolt spacing, shotcrete thickness)
- GSI ≈ RMR - 5 (for RMR > 23; based on 1989 RMR with dry conditions and no orientation adjustment)

## Q-System — Barton, Lien & Lunde (1974, updated 2002)

### Overview
Multiplicative rating system with six parameters, designed specifically for tunnel support design. More detailed than RMR for discontinuity characterization.

### The Q Formula

Q = (RQD/J_n) × (J_r/J_a) × (J_w/SRF)

Each ratio represents:
- RQD/J_n = relative block size (rock quality / number of joint sets)
- J_r/J_a = relative frictional strength (joint roughness / joint alteration)
- J_w/SRF = environmental and stress effects (water / stress reduction factor)

Q ranges from 0.001 (exceptionally poor) to 1000 (exceptionally good).

### Parameter Details

**RQD (0–100):** Standard RQD. Use 10 as minimum if measured RQD = 0.

**J_n — Joint Set Number:**
- Massive (0–1 joint sets): 0.5–2
- One set: 2; one set + random: 3
- Two sets: 4; two sets + random: 6
- Three sets: 9; three sets + random: 12
- Four+ sets (heavily jointed): 15
- Crushed rock: 20

**J_r — Joint Roughness Number:**
- Discontinuous joints: 4
- Rough, undulating: 3
- Smooth, undulating: 2
- Slickensided, undulating: 1.5
- Rough, planar: 1.5
- Smooth, planar: 1.0
- Slickensided, planar: 0.5

**J_a — Joint Alteration Number:**
- Tightly healed: 0.75
- Unaltered, surface staining: 1.0
- Slightly altered: 2.0
- Silty/sandy coating: 3.0
- Soft clay coating < 5mm: 4.0
- Soft clay filling > 5mm: 6–12
- Swelling clay filling: 8–18

**J_w — Joint Water Reduction Factor:**
- Dry or minor inflow: 1.0
- Medium inflow: 0.66
- Large inflow, unfilled joints: 0.5
- Large inflow, filling washed out: 0.33
- Exceptionally high inflow: 0.1–0.2

**SRF — Stress Reduction Factor:**
Accounts for in-situ stress conditions, weakness zones, squeezing, and swelling. Ranges from 1 (low stress) to 20+ (heavy squeezing). Complex parameter with multiple cases — weakness zones, competent rock stress ratios, squeezing rock, swelling rock.

### Support Design

The Equivalent Dimension (D_e) is used with Q to determine support:

D_e = Span (or height) / ESR

**ESR — Excavation Support Ratio:**
- Temporary mine openings: 3–5
- Permanent mine openings: 1.6
- Water tunnels, pilot tunnels: 1.6
- Minor road/rail tunnels: 1.3
- Major road/rail tunnels, powerhouses: 1.0
- Underground nuclear power, defense: 0.8
- Portal intersections: 0.5

Plot D_e vs. Q on the support chart to determine category (no support, spot bolting, systematic bolting, shotcrete combinations, CCA).

## RMR–Q Correlation

GSI ≈ RMR₈₉ - 5 (for RMR > 23)
RMR₈₉ ≈ 9 × lnQ + 44
Q ≈ exp[(RMR - 44) / 9]

These are approximate — there is significant scatter because the systems weight parameters differently.
