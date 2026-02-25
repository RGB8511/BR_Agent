# Rock Classification & Identification

## Rock Types by Geological Origin

### Igneous Rocks
Formed from cooling and solidification of magma or lava.

**Intrusive (plutonic):** Cooled slowly at depth — large crystals (phaneritic texture). Examples: granite, diorite, gabbro, peridotite. Generally strong, durable foundation materials.

**Extrusive (volcanic):** Cooled rapidly at surface — fine crystals or glassy (aphanitic texture). Examples: basalt, andesite, rhyolite, obsidian, tuff. Tuff and pyroclastic deposits can be weak and compressible. Basalt typically strong but may have vesicles, columnar joints.

**Engineering Significance:** Igneous rocks are generally strong (UCS 100–300+ MPa for granites, 100–350 MPa for basalt). Weathering patterns depend on mineral composition — feldspar-rich rocks weather faster than quartz-rich. Columnar jointing in basalt creates distinctive block patterns.

### Sedimentary Rocks
Formed from deposition, compaction, and cementation of sediments.

**Clastic:** sandstone, siltstone, mudstone/shale, conglomerate, breccia. Properties heavily dependent on cement type (siliceous strongest, calcareous moderate, ferruginous variable, clay weakest).

**Chemical/Biochemical:** limestone, dolostone, chert, gypsum, halite, coal. Limestone susceptible to dissolution (karst). Gypsum and halite are soluble — not suitable foundation materials.

**Engineering Significance:** Wide strength range (UCS 5–200 MPa). Bedding planes are persistent discontinuities. Shale/mudstone often problematic: low strength, swelling, slaking. Sandstone properties depend on cementation and grain packing.

### Metamorphic Rocks
Formed by transformation under heat and pressure.

**Foliated:** slate, phyllite, schist, gneiss. Foliation creates anisotropy — strength varies significantly with loading direction relative to foliation planes.

**Non-foliated:** quartzite, marble, hornfels. Generally isotropic and strong (quartzite UCS 150–300+ MPa). Marble susceptible to dissolution like limestone.

**Engineering Significance:** Foliation planes are pre-existing discontinuities that control shear strength and excavation behavior. Schist and phyllite can be very weak parallel to foliation (UCS may be 3–10× lower than perpendicular). Gneiss often has strength and behavior similar to granite.

## Weathering Classification

The ISRM six-grade weathering classification (W1–W6):

- **W1 — Fresh:** No visible sign of weathering. Rock fresh, crystals bright.
- **W2 — Slightly weathered:** Discoloration on major discontinuity surfaces. Rock may be slightly discolored but not noticeably weaker.
- **W3 — Moderately weathered:** Less than half of rock material is decomposed. Discolored rock is present, noticeably weaker than fresh rock.
- **W4 — Highly weathered:** More than half of rock material is decomposed. Rock is discolored and material altered, large pieces cannot be broken by hand.
- **W5 — Completely weathered:** All rock material decomposed to soil. Original fabric preserved (saprolite). Can be crumbled by hand.
- **W6 — Residual soil:** Completely weathered. No original fabric visible. Soil behavior dominates.

Weathering profiles vary by rock type: granite → spheroidal weathering (corestones in saprolite); basalt → laterite development in tropical climates; shale → rapid degradation when exposed.

## Rock Quality Designation (RQD)

Introduced by Deere (1963) as a quantitative measure of rock core quality:

RQD = (Σ length of intact core pieces ≥ 10 cm) / (total core run length) × 100%

**Rules:**
- Only intact pieces of hard, sound rock ≥ 10 cm (4 in) counted
- Fresh mechanical breaks caused by drilling are counted as intact
- Measure along centerline of core
- RQD is a directional measure — depends on borehole orientation relative to discontinuities

**Correlation to Rock Quality:**
- 0–25%: Very poor
- 25–50%: Poor
- 50–75%: Fair
- 75–90%: Good
- 90–100%: Excellent

**Limitations:** RQD does not capture joint condition (roughness, filling, aperture), joint orientation, or strength. Should always be supplemented with more comprehensive classification systems (Q, RMR, GSI).

### Volumetric RQD (RQD from Joint Spacing)

For rock exposures where core is not available, RQD can be estimated from joint spacing (Jv = number of joints per m³):

RQD = 115 - 3.3 × Jv (for Jv > 4.5; RQD = 100% for Jv ≤ 4.5)

Or from mean joint spacing λ (joints per meter along a line):

RQD = 100 × e^(-0.1λ) × (0.1λ + 1)

## Point Load Index

A rapid field or laboratory test correlating to UCS:

I_s(50) = P / D_e² (corrected to equivalent 50 mm diameter)

Size correction: I_s(50) = I_s × (D_e / 50)^0.45

UCS correlation: UCS ≈ K × I_s(50) where K typically 20–25 (ranges from 15–50 depending on rock type; must be calibrated for specific rock types).
