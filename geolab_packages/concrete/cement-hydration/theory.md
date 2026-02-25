# Cement Chemistry & Hydration

## Portland Cement Composition

Portland cement is manufactured by heating limestone (CaCO₃) and clay/shale to ~1450°C in a rotary kiln, producing clinker, which is then ground with gypsum.

### Major Compounds (Cement Chemist Notation)

- **C₃S — Tricalcium silicate (alite):** 50–70% of cement. Primary strength contributor, especially early strength (1–28 days). Reacts relatively rapidly.
- **C₂S — Dicalcium silicate (belite):** 15–30%. Contributes to later strength (28+ days). Reacts slowly.
- **C₃A — Tricalcium aluminate:** 5–12%. Reacts very rapidly. Controls early setting and heat generation. Susceptible to sulfate attack.
- **C₄AF — Tetracalcium aluminoferrite (ferrite):** 5–15%. Moderate reactivity. Gives cement its gray color. Contributes little to strength.

**Notation convention:** C = CaO, S = SiO₂, A = Al₂O₃, F = Fe₂O₃, H = H₂O, Š = SO₃

### Bogue Calculation

Estimates compound composition from oxide analysis:
- C₃S = 4.071CaO - 7.600SiO₂ - 6.718Al₂O₃ - 1.430Fe₂O₃ - 2.852SO₃
- C₂S = 2.867SiO₂ - 0.7544C₃S
- C₃A = 2.650Al₂O₃ - 1.692Fe₂O₃
- C₄AF = 3.043Fe₂O₃

Where oxide percentages are by mass. This is an approximation — actual compounds differ due to solid solutions and impurities.

## Hydration Reactions

### C₃S Hydration (Primary Strength)
2C₃S + 6H → C₃S₂H₃ (C-S-H gel) + 3CH (calcium hydroxide/portlandite)

C-S-H gel is the primary binding phase — provides ~50–60% of paste strength. Calcium hydroxide (CH) is a crystalline byproduct (~20–25% of hydration products by mass).

### C₂S Hydration
2C₂S + 4H → C₃S₂H₃ (C-S-H gel) + CH

Same products as C₃S but slower reaction and less CH produced.

### C₃A Hydration (With Gypsum)
C₃A + 3CŠH₂ + 26H → C₆AŠ₃H₃₂ (ettringite)

Gypsum controls the rapid reaction of C₃A, preventing flash set. Ettringite later converts to monosulfoaluminate as sulfate is consumed.

### C₄AF Hydration
Similar to C₃A but slower. Forms iron-substituted phases.

## Heat of Hydration

Hydration is exothermic. Total heat and rate of heat evolution depend on compound composition:

| Compound | Heat of hydration (J/g) |
|----------|------------------------|
| C₃S      | 500                    |
| C₂S      | 250                    |
| C₃A      | 870                    |
| C₄AF     | 420                    |

**Five stages of heat evolution:**
1. Initial hydrolysis (minutes): rapid heat burst as C₃A and C₃S surfaces react
2. Dormant period (1–3 hours): slow reaction, concrete is workable
3. Acceleration (3–12 hours): rapid C₃S hydration, setting and early hardening
4. Deceleration (12–24 hours): reaction rate slows as hydration products coat grains
5. Steady state (days–years): diffusion-controlled, slow continued hydration

## Cement Types (ASTM C150)

- **Type I:** General purpose. No special requirements.
- **Type II:** Moderate sulfate resistance (C₃A ≤ 8%). Moderate heat.
- **Type III:** High early strength. Finer grind, more C₃S.
- **Type IV:** Low heat of hydration (C₃S ≤ 35%, C₃A ≤ 7%). For mass concrete. Rarely available.
- **Type V:** High sulfate resistance (C₃A ≤ 5%).

## Supplementary Cementitious Materials (SCMs)

### Fly Ash (ASTM C618)
- **Class F:** Low calcium (CaO < 18%). Siliceous. Pozzolanic. From bituminous coal.
- **Class C:** High calcium (CaO > 18%). Both pozzolanic and cementitious. From sub-bituminous/lignite.
- Typical replacement: 15–35% by mass of cement. Reduces heat, improves long-term strength and durability.

### Ground Granulated Blast-Furnace Slag (GGBFS, ASTM C989)
- Glassy granulated byproduct of iron production.
- Both pozzolanic and latent hydraulic (reacts with water when activated by CH from cement hydration).
- Grades 80, 100, 120 (based on strength activity index).
- Typical replacement: 25–70%. Excellent for sulfate resistance and alkali-silica reaction (ASR) mitigation.

### Silica Fume (ASTM C1240)
- Ultrafine amorphous silica (particle size ~0.1 μm — 100× finer than cement).
- Highly reactive pozzolan. Reacts with CH to form additional C-S-H.
- Typical addition: 5–10%. Dramatically reduces permeability, increases strength, improves bond.
- Increases water demand — requires superplasticizer.

### Pozzolanic Reaction
Pozzolan + CH + H₂O → C-S-H (secondary)

This consumes the weak, soluble CH and produces additional C-S-H, improving strength, impermeability, and durability. The pozzolanic reaction is slower than cement hydration — benefits appear at 28+ days.

## Fineness

Fineness controls the rate of hydration. Finer cement → faster hydration → higher early strength → more heat → less late-age strength gain.

Measured by:
- Blaine air permeability (ASTM C204): specific surface area in cm²/g (typical 300–500 m²/kg)
- Particle size distribution (laser diffraction): more informative than Blaine
