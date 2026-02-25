# Concrete Durability & Degradation Mechanisms

## Overview

Durability is the ability of concrete to resist weathering, chemical attack, and other degradation processes while maintaining serviceability. Most durability problems trace to one principle: permeability controls durability. Lower permeability → slower ingress of harmful agents → longer service life.

## Chemical Degradation

### Alkali-Silica Reaction (ASR)
The most common deleterious chemical reaction in concrete worldwide.

**Mechanism:** Alkalis (Na₂O, K₂O) from cement react with certain siliceous minerals in aggregate to form alkali-silica gel. The gel absorbs water and swells, generating internal pressure that causes map cracking and expansion.

**Three requirements (all must be present):**
1. Sufficient alkalis (Na₂Oeq > 0.60% in cement, or high external alkali source)
2. Reactive silica in aggregate (opal, chert, strained quartz, volcanic glass, certain greywackes)
3. Sufficient moisture (RH > 80%)

**Prevention strategies:**
- Low-alkali cement (Na₂Oeq ≤ 0.60%)
- SCMs (fly ash 25%+, slag 50%+, silica fume 7%+)
- Non-reactive aggregate (petrographic examination per ASTM C295)
- Lithium compounds (LiNO₃) — interrupt gel formation

**Testing:**
- ASTM C1260 (accelerated mortar bar, 14 days): < 0.10% = innocuous, > 0.20% = potentially deleterious
- ASTM C1293 (concrete prism, 1 year): < 0.04% = innocuous
- ASTM C1567: mortar bar with SCMs to evaluate mitigation effectiveness

### Delayed Ettringite Formation (DEF)
Formation of ettringite in hardened concrete that was cured at elevated temperatures (> 65–70°C). Ettringite crystals exert expansive pressure within the paste. Common in steam-cured precast and mass concrete.

### Sulfate Attack
External sulfates (from soil, groundwater, or seawater) react with C₃A hydration products:
- **Ettringite formation:** Expansion and cracking
- **Gypsum formation:** Softening and loss of strength
- **Thaumasite form:** Rare, cold climates, attacks C-S-H directly

**Prevention:** Low C₃A cement (Type II or V), low w/cm (≤ 0.45), SCMs (slag, Class F fly ash), physical barriers.

### Carbonation
Atmospheric CO₂ diffuses into concrete and reacts with CH (portlandite):
Ca(OH)₂ + CO₂ → CaCO₃ + H₂O

This reduces pH from ~13 to ~9, destroying the passive oxide layer protecting reinforcing steel. Carbonation front advances approximately as:

d = K√t (square root of time law)

where K depends on w/cm, CO₂ concentration, humidity, and compaction quality. Carbonation rate fastest at 50–70% RH (needs both CO₂ diffusion and some moisture).

## Reinforcement Corrosion

### Chloride-Induced Corrosion
Most damaging and costly durability problem for reinforced concrete infrastructure.

**Mechanism:** Chloride ions (from deicing salts or marine environment) diffuse through concrete cover. When chloride concentration at the rebar exceeds a threshold (~0.2–0.4% by mass of cement), the passive oxide layer breaks down → active corrosion → rust (iron oxides) with 2–6× volume expansion → cracking, spalling, delamination.

**Fick's Second Law (chloride diffusion):**
C(x,t) = C_s × [1 - erf(x / (2√(D_a × t)))]

where C_s = surface chloride concentration, x = depth, D_a = apparent diffusion coefficient, t = time.

**Corrosion threshold:** 0.2% Cl⁻ by mass of cement (commonly used for design). Some codes use 0.4% for prestressed.

### Service Life Prediction
Two-phase model:
1. **Initiation period:** Time for chloride to reach rebar at threshold concentration (Fick's law)
2. **Propagation period:** Time from corrosion initiation to unacceptable damage

Design service life = initiation + propagation. Most design focuses on maximizing initiation period through adequate cover and low permeability.

## Physical Degradation

### Freeze-Thaw Damage
Water in saturated pore system expands ~9% on freezing. Hydraulic pressure from ice formation damages paste.

**Protection:** Air entrainment with adequate spacing factor (L̄ ≤ 0.20 mm). Without proper air void system, saturated concrete can deteriorate rapidly (< 50 cycles).

**Testing:** ASTM C666 Procedure A (freezing and thawing in water). Durability factor DF ≥ 60% after 300 cycles is satisfactory. DF = (P_n × N) / 300, where P_n = relative dynamic modulus at N cycles.

### Salt Scaling
Surface deterioration from repeated application of deicing salts. The osmotic/thermal shock mechanism causes surface flaking. Worse than plain freeze-thaw because of concentration gradients and glaze ice formation.

**Testing:** ASTM C672 (surface resistance to deicing chemicals). Visual rating 0–5 scale.

### Abrasion and Erosion
Wear from traffic, hydraulic action, or cavitation. Higher-strength, harder aggregate, good curing, and low w/cm improve abrasion resistance.

## Permeability and Transport

Concrete permeability governs the rate of ingress of all harmful agents. Key transport mechanisms:
- **Permeation:** Flow under pressure gradient (Darcy's law)
- **Diffusion:** Movement under concentration gradient (Fick's laws)
- **Absorption:** Capillary suction into dry concrete (sorptivity)

### Rapid Chloride Permeability Test (RCPT — ASTM C1202)
Measures charge passed (coulombs) through a 50mm thick, 100mm diameter disk in 6 hours under 60V DC.

| Charge (coulombs) | Chloride Permeability |
|---|---|
| > 4000 | High |
| 2000–4000 | Moderate |
| 1000–2000 | Low |
| 100–1000 | Very low |
| < 100 | Negligible |

Widely used but criticized — measures electrical conductivity, not true permeability. Influenced by pore solution chemistry.

### Bulk Diffusion Test (ASTM C1556)
Ponding test — expose concrete surface to NaCl solution for 35+ days, then profile grind and measure chloride at multiple depths. Fit Fick's second law to determine D_a. More representative of actual diffusion behavior than RCPT.
