# Corrosion Fundamentals

## Definition and Significance

Corrosion is the deterioration of a material (usually a metal) through chemical or electrochemical reaction with its environment. It is fundamentally a return of refined metals to their thermodynamically stable, lower-energy oxide/sulfide/carbonate forms — the reverse of extraction metallurgy.

Global cost of corrosion: estimated at 3–4% of GDP in industrialized nations. Most corrosion is preventable with proper design, material selection, and protection.

## Electrochemical Basis

All aqueous metallic corrosion is electrochemical, requiring four components:
1. **Anode:** Where metal dissolves (oxidation): M → M^n+ + ne⁻
2. **Cathode:** Where reduction occurs (electrons consumed)
3. **Electrolyte:** Ionic conductor (water with dissolved salts)
4. **Metallic path:** Electronic conductor connecting anode to cathode

Remove any one → corrosion stops. This is the basis for all protection strategies.

### Anodic Reaction (Oxidation)
Fe → Fe²⁺ + 2e⁻ (iron dissolution)

### Cathodic Reactions (Reduction)
- **Oxygen reduction (neutral/alkaline):** O₂ + 2H₂O + 4e⁻ → 4OH⁻ (most common in nature)
- **Hydrogen evolution (acidic):** 2H⁺ + 2e⁻ → H₂↑
- **Oxygen reduction (acidic):** O₂ + 4H⁺ + 4e⁻ → 2H₂O

### Nernst Equation
E = E° - (RT/nF) × ln(a_products / a_reactants)

At 25°C: E = E° - (0.0592/n) × log(a_products/a_reactants)

This governs the equilibrium potential of any half-cell reaction and determines which metal is anodic in a galvanic couple.

## Galvanic Series

When two dissimilar metals are electrically connected in an electrolyte, the more active (more negative potential) metal becomes the anode and corrodes preferentially — protecting the more noble metal.

**Practical galvanic series in seawater** (anodic → cathodic):
Magnesium → Zinc → Aluminum alloys → Carbon steel → Cast iron → Stainless steel (active) → Lead → Copper → Brass → Bronze → Nickel → Stainless steel (passive) → Titanium → Gold → Platinum

**Design rules:**
- Avoid large cathode / small anode area ratios
- Insulate dissimilar metal connections
- Use sacrificial anodes (Zn, Mg, Al) for cathodic protection

## Forms of Corrosion

### Uniform (General) Corrosion
Even metal loss over entire surface. Predictable, measurable by weight loss. Easiest to manage — design for corrosion allowance.

### Galvanic Corrosion
Occurs at dissimilar metal junctions. Rate depends on potential difference, area ratio, and electrolyte conductivity.

### Pitting Corrosion
Localized attack forming small holes. Most dangerous — penetrates wall thickness rapidly while overall metal loss is minimal. Stainless steels and aluminum susceptible. Initiated by chloride ions breaking passive film.

**Pitting resistance equivalent number (PREN):**
PREN = %Cr + 3.3(%Mo) + 16(%N)

Higher PREN = better pitting resistance. PREN > 40 generally resistant to seawater pitting.

### Crevice Corrosion
Accelerated corrosion within confined spaces (flanges, gaskets, fastener interfaces) due to oxygen depletion, local acidification, and chloride concentration. Similar mechanism to pitting but geometry-driven.

### Intergranular Corrosion
Preferential attack along grain boundaries. In stainless steels: sensitization — chromium carbide precipitation at grain boundaries during welding (450–850°C), depleting adjacent zones of Cr below the 12% passivity threshold.

**Prevention:** Low-carbon grades (304L, 316L — C < 0.03%), stabilized grades (321-Ti, 347-Nb), or solution anneal after welding.

### Stress Corrosion Cracking (SCC)
Brittle fracture under combined tensile stress + specific corrosive environment. Requires three simultaneous factors: susceptible material, specific corrosive species, and sufficient tensile stress.

Classic systems: stainless steel + chlorides, carbon steel + caustic (NaOH), brass + ammonia, aluminum + chloride.

### Erosion-Corrosion
Combined mechanical wear + chemical attack. Flowing fluids, slurries, and turbulent conditions remove protective films and expose fresh metal. Common in piping elbows, pump impellers, and turbine blades.

### Microbiologically Influenced Corrosion (MIC)
Corrosion catalyzed by microbial activity. Sulfate-reducing bacteria (SRB) produce H₂S, creating aggressive conditions under biofilms. Common in buried pipelines, cooling water systems, and stagnant conditions.

## Corrosion Rate Measurement

### Faraday's Law
m = (M × I × t) / (n × F)

Relates electrical current to mass of metal dissolved.

**Corrosion rate in mils per year (mpy):**
CR = (K × W) / (A × T × ρ)

where K = constant (3.45 × 10⁶ for mpy), W = weight loss (g), A = area (cm²), T = time (hours), ρ = density (g/cm³).

**Corrosion rate from current density:**
CR (mpy) = 0.129 × (i_corr × M) / (n × ρ)

where i_corr = corrosion current density (μA/cm²), M = atomic weight, n = electrons transferred.

## Pourbaix Diagrams

Potential-pH diagrams showing thermodynamic stability regions for metal-water systems. Three regions:
- **Immunity:** Metal is stable (cathodic protection operates here)
- **Corrosion:** Metal dissolves as ions
- **Passivity:** Protective oxide film is stable

These are thermodynamic (not kinetic) — they show what CAN corrode, not how fast. Kinetics require polarization curves.

## Polarization

Deviation of electrode potential from equilibrium due to current flow.

- **Activation polarization:** Charge transfer controlled (Tafel behavior): η = β × log(i/i₀)
- **Concentration polarization:** Mass transport limited — diffusion of reactants
- **Resistance polarization:** IR drop through solution or film

**Tafel equation:** η_a = β_a × log(i/i_corr)

where β_a = anodic Tafel slope (typically 60–120 mV/decade), i₀ = exchange current density.

Mixed potential theory (Wagner-Traud): corrosion potential E_corr occurs where total anodic current = total cathodic current. Corrosion rate = i_corr at this intersection.
