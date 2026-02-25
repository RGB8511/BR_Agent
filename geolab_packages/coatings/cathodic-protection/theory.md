# Cathodic Protection

## Principle

Cathodic protection (CP) prevents corrosion by making the protected structure the cathode of an electrochemical cell. By shifting the metal's potential in the negative (cathodic) direction, the anodic dissolution reaction (metal → metal ions + electrons) is suppressed or eliminated.

Two methods:
1. **Galvanic (sacrificial anode):** Connect a more active (less noble) metal to the structure. The anode corrodes preferentially, providing protective current.
2. **Impressed current (ICCP):** Use an external DC power source (rectifier) to force current from an anode bed to the structure through the electrolyte.

## Galvanic (Sacrificial Anode) Systems

### Anode Materials

**Zinc anodes:** Potential approximately -1.10 V vs. Cu/CuSO₄ (CSE). Used in soil, fresh water, and marine environments. Reliable, predictable consumption. Driving voltage to steel: ~0.25 V.

**Magnesium anodes:** Standard alloy: -1.55 V vs. CSE. High-potential alloy: -1.75 V vs. CSE. Higher driving voltage (~0.70–0.90 V) — used in higher-resistivity soils. Consumes faster than zinc. Not efficient in seawater (self-corrosion).

**Aluminum anodes:** Potential -1.05 to -1.10 V vs. CSE (activated alloys). High current capacity (ampere-hours per kg). Primary anode material for offshore and marine structures. Lighter than zinc.

### Design Considerations
- Driving voltage = E_anode - E_protected_structure (must exceed minimum to deliver adequate current)
- Limited by electrolyte resistivity — galvanic anodes struggle in high-resistivity soils (> 5000–10000 Ω·cm)
- Simple, no external power required, low maintenance
- Limited current output — suitable for well-coated structures or small bare areas

## Impressed Current Cathodic Protection (ICCP)

### Components
- **Rectifier:** Converts AC to DC. Adjustable voltage/current output. Air-cooled or oil-immersed.
- **Anode bed:** High-silicon cast iron, graphite, mixed metal oxide (MMO) coated titanium, platinum-clad niobium/titanium. Designed for long life (20–30+ years).
- **Wiring:** Positive (anode), negative (structure/cathode), reference cell connections. Must be properly insulated.

### Advantages over Galvanic
- Higher driving voltage — works in any resistivity
- Adjustable output — can protect large, poorly coated structures
- Can protect long pipeline sections from a single installation

### Disadvantages
- Requires external power (electricity)
- Over-protection risk (hydrogen embrittlement, coating disbondment)
- More complex design and monitoring
- Interference effects on nearby structures

## Protection Criteria

### -850 mV Criterion (CSE)
Structure-to-soil potential of -850 mV or more negative measured with a Cu/CuSO₄ reference electrode (CSE) with CP applied. The most widely used criterion.

**With IR drop:** Measured potential includes voltage drop through soil. True polarized potential is more negative than measured ON potential. Instant-OFF reading (within 1 second of current interruption) removes most IR error.

### Polarized Potential Criterion
Instant-OFF potential of -850 mV or more negative vs. CSE. Eliminates IR drop error. More accurate than ON potential. Required by many specifications.

### 100 mV Polarization Shift
Structure must be polarized at least 100 mV more negative than its natural (free-corroding) potential. Measured as difference between native potential and polarized (instant-OFF) potential. Alternative criterion when native potential is already very negative.

### 300 mV Shift (Less Common)
Used in some older standards. 300 mV negative shift from native potential with CP applied.

## Potential Measurement

**Reference electrodes:**
- Cu/CuSO₄ (CSE): Standard for soil/onshore. +316 mV vs. SHE.
- Ag/AgCl (seawater): Standard for marine. +222 mV vs. SHE.
- Zinc: Used as permanent reference in some marine applications. -780 mV vs. SHE.

**Survey methods:**
- Structure-to-soil (pipe-to-soil) potential: Measured at test stations along pipeline
- Close-interval potential survey (CIPS/CIS): Readings every 1–1.5 m (3–5 ft) along pipeline with trailing wire
- Interruption (instant-OFF): Synchronized current interruption to measure polarized potential

## Over-Protection

Excessive negative potential (more negative than about -1100 to -1200 mV CSE) can cause:
- **Cathodic disbondment:** Coating lifts due to alkaline environment at cathode (OH⁻ production)
- **Hydrogen embrittlement:** Hydrogen evolution at very negative potentials — concern for high-strength steels
- **Increased anode consumption:** Wasted current and accelerated anode depletion

## Applications

**Buried pipelines:** Most extensive CP application. Combination of coating + CP. NACE SP0169 is the primary standard.

**Marine structures:** Offshore platforms, ship hulls, port facilities. Galvanic (zinc, aluminum) or ICCP.

**Storage tanks:** Tank bottoms in contact with soil. Internal CP for water storage tanks.

**Reinforcing steel in concrete:** Impressed current or galvanic (zinc) anodes embedded in concrete or applied as thermal spray zinc on surface. NACE SP0290.

**Water heaters and heat exchangers:** Small galvanic anodes (magnesium rods).

## CP and Coatings — Complementary System

Coatings reduce the bare metal area requiring protection, dramatically reducing CP current demand. CP protects coating defects (holidays, damage). Together they provide the most effective and economical long-term protection. Without coating, CP current requirements for large structures become impractically high.
