# Referenced Standards and Test Methods — Sage Creek Canal Reach 7 Rehabilitation

This document lists all standards, test methods, and specifications referenced in the Sage Creek Main Canal Reach 7 Rehabilitation Investigation and Design. Standards are organized by technical category.

---

## Geotechnical Testing

### ASTM D4546 — Standard Test Methods for One-Dimensional Swell or Collapse of Soils

**Organization:** ASTM International
**Current Edition:** ASTM D4546-14(2021)
**Applicability:** Used to quantify swell pressure and free swell of the Reach 7 lacustrine clay (Unit 2, CH), and collapse potential of the loess (Unit 1, ML/CL).

Three test methods are defined:

- **Method A (Constant Volume):** Sample is loaded to the in-situ overburden stress and confined against vertical deformation. Water is introduced and the additional stress required to prevent swelling is measured — this is the swell pressure. Used for Reach 7 clay samples; swell pressures measured at 3,600–6,500 psf. This method is most appropriate when the design constraint is a rigid structure (lining panel) that prevents volume change.

- **Method B (Constant Stress):** Sample is loaded to the design stress and allowed to swell freely to equilibrium. Percent swell is measured. Used for comparison and for computing free-swell versus confining pressure relationships.

- **Method C (Free Swell):** Sample is inundated under a token 144 psf (1 psi) surcharge and allowed to swell freely. Percent swell reported. Used for Reach 7 as a screening and classification tool; free swells ranged from 4.5–8.1%.

**Key result from project:** Mean swell pressure 4,800 psf (Method A); exceeds panel self-weight (50 psf) by 96×. Fundamental justification for lime treatment and/or geomembrane seepage control.

---

### ASTM D5333 — Standard Test Method for Measurement of Collapse Potential of Soils

**Organization:** ASTM International
**Current Edition:** ASTM D5333-03(2012)
**Applicability:** Used to classify the collapse potential of the Reach 7 loess (Unit 1).

The test loads a sample at natural moisture content to the applied stress (typically 4 tsf for canal subgrades) using an oedometer, then floods the sample and measures the immediate decrease in void ratio (collapse). Collapse potential CP = Δe / (1 + e₀) × 100%.

**Classification per ASTM D5333:**
| CP (%) | Severity |
|--------|----------|
| 0–1    | No problem |
| 1–5    | Moderate |
| 5–10   | Moderately severe |
| 10–20  | Severe |
| >20    | Very severe |

**Key results from project:** Five loess samples tested at 4 tsf; CP = 5.5–10.2% (Moderately Severe to Severe). Construction management plan must address risk of collapse during phased wetting of new subgrade.

---

### ASTM D3080 — Standard Test Method for Direct Shear Test of Soils Under Consolidated Drained Conditions

**Organization:** ASTM International
**Current Edition:** ASTM D3080-11(2012)
**Applicability:** Used to determine peak and residual shear strength parameters (c', φ', c'r, φ'r) for the Reach 7 loess and lacustrine clay. Critical for slope stability analysis of the right bank failure zone.

The test consolidates a soil specimen under a normal stress, then shears it by moving the lower box relative to the upper box at a constant, slow rate to ensure drainage (CD condition). Multiple specimens at different normal stresses define the Mohr-Coulomb failure envelope. Residual strength is obtained by reversing the shear direction multiple times until a stable minimum shear stress (plateau) is reached.

**Key results from project:** Lacustrine clay residual parameters (c'r = 40–80 psf, φ'r = 12–14°) govern slope stability analysis for the existing failure plane. Residual strength is the primary design input for demonstrating that FS = 0.92 exists under current conditions and FS = 1.35 with remediation.

---

### ASTM D5084 — Standard Test Methods for Measurement of Hydraulic Conductivity of Saturated Porous Materials Using a Flexible Wall Permeameter

**Organization:** ASTM International
**Current Edition:** ASTM D5084-16a
**Applicability:** Laboratory measurement of hydraulic conductivity for lacustrine clay and loess samples. Provides input data for SEEP/W seepage model.

The flexible wall permeameter (also called a triaxial permeameter) encloses the sample in a membrane, applies a confining stress, and measures flow under a controlled hydraulic gradient. The method controls the effective stress on the sample (preventing swelling or consolidation during testing), making it more accurate for expansive and compressible soils than rigid-wall methods.

**Key results from project:** k_clay = 1.5–4.2 × 10⁻⁷ cm/s (lacustrine CH); k_loess = 1.2–3.8 × 10⁻⁵ cm/s (ML/CL). Both used as material properties in SEEP/W model calibration.

---

### ASTM D698 — Standard Test Methods for Laboratory Compaction Characteristics of Soil Using Standard Effort

**Organization:** ASTM International
**Current Edition:** ASTM D698-12(2021)
**Applicability:** Standard Proctor compaction test for establishing maximum dry density (MDD) and optimum moisture content (OMC) of the lime-treated subgrade. Referenced for field compaction QC specification.

Note: Modified Proctor (ASTM D1557) was also used for compaction control of the lime-treated subgrade layer, as the modified effort more closely matches the compaction energy achievable with vibratory rollers. Design specifies 95% of modified MDD (ASTM D1557) at OMC + 0 to +2%.

---

### ASTM D6276 — Standard Test Method for Using pH to Estimate the Soil-Lime Proportion Requirement for Soil Stabilization

**Organization:** ASTM International
**Current Edition:** ASTM D6276-19
**Applicability:** Used to establish the minimum lime content (CaO dosage) required to satisfy the ion exchange capacity of the Reach 7 lacustrine clay and initiate the pozzolanic reaction. This is the Eades and Grim pH method.

The test prepares soil-lime mixtures at a range of lime contents (2%–8%) in distilled water and measures pH after one hour at 77°F. The minimum lime content yielding pH ≥ 12.4 is the design dosage.

**Key results from project:** 6% CaO achieves pH = 12.5; confirmed as design dosage. At this dosage, 28-day cured specimens show PI reduced from 30–42 to 8–12, swell pressure reduced to <400 psf, and UCS = 45–65 psi.

---

### ASTM D4044 — Standard Test Method for (Field Procedure) for Instantaneous Change in Head (Slug) Tests for Determining Hydraulic Properties of Aquifers

**Organization:** ASTM International
**Current Edition:** ASTM D4044-96(2013)
**Applicability:** Field slug tests conducted in monitoring wells installed in BH-SC-02, BH-SC-03, and BH-SC-04 to measure in-situ horizontal hydraulic conductivity of the alluvial sand lenses (Unit 3) and lacustrine clay (Unit 2).

**Key results from project:** k_sand = 3.5 × 10⁻³ cm/s (Unit 3 alluvial lens) — five orders of magnitude more permeable than the surrounding clay (k = 1.5 × 10⁻⁷ cm/s). The sand lens is the dominant seepage pathway and its elimination from the hydraulic circuit by the HDPE geomembrane is critical to achieving the design seepage reduction target.

---

## Concrete and Aggregate Testing

### ASTM C1260 — Standard Test Method for Potential Alkali Reactivity of Aggregates (Mortar-Bar Method)

**Organization:** ASTM International
**Current Edition:** ASTM C1260-14(2021)
**Applicability:** Used to screen proposed new concrete aggregates for alkali-silica reactivity (ASR) potential. Required for qualification of all aggregate sources for the new Reach 7 lining concrete.

The test accelerates ASR by immersing mortar bars in 1 N NaOH at 80°C for 14 days and measuring expansion. Acceptance criterion: expansion ≤ 0.10% at 14 days (low reactivity); 0.10–0.20% requires further testing (ASTM C1293); >0.20% = potentially deleterious reactivity.

**Project requirement:** All aggregate sources must demonstrate expansion < 0.10% at 14 days per ASTM C1260 before use in the new lining concrete. The failure of the 1962 concrete is partly attributable to use of locally sourced volcanic (rhyolite) aggregate that would likely have failed this screening test.

---

### ASTM C260 — Standard Specification for Air-Entraining Admixtures for Concrete

**Organization:** ASTM International
**Current Edition:** ASTM C260/C260M-10a(2016)
**Applicability:** Specification governing the air-entraining admixture (AEA) to be incorporated in the new Reach 7 lining concrete at a dosage achieving 6 ± 1% air content. Air entrainment is the primary protection against freeze-thaw damage.

The specification covers: water-soluble residue, effect on setting time, effect on compressive strength, effect on flexural strength, uniformity, and compatibility with supplementary cementitious materials (SCM). The Idaho climate (80–120 freeze-thaw cycles per year) requires robust air void structure with spacing factor ≤ 0.008 inch per the new design.

**Basis for inclusion:** All four concrete cores from the existing 1962 lining lacked an air void system (spacing factor > 0.010 inch in the best case), directly causing the pervasive freeze-thaw damage (surface scaling, delamination) observed throughout Reach 7. This deficiency will not be repeated in the new design.

---

### ASTM C666 — Standard Test Method for Resistance of Concrete to Rapid Freezing and Thawing

**Organization:** ASTM International
**Current Edition:** ASTM C666/C666M-15(2021)
**Applicability:** Used during concrete mix design qualification to verify that the proposed mix (4,000 psi, 6% air, SCM, non-reactive aggregate) achieves adequate freeze-thaw durability. Mix design must achieve a durability factor DF ≥ 80 after 300 cycles.

The test subjects concrete prisms to repeated freezing and thawing cycles (Procedure A: freezing and thawing in water; Procedure B: freezing in air, thawing in water). Relative dynamic modulus of elasticity is measured periodically; durability factor DF = (relative modulus at 300 cycles) × 100%.

**Project requirement:** New concrete mix design must achieve DF ≥ 80 per ASTM C666 Procedure A before final approval. This requirement supplements the minimum 6% air content requirement.

---

## Geosynthetics

### GRI GM-13 — Standard Specification for Test Properties, Testing Frequency, and Recommended Warranty for High Density Polyethylene (HDPE) Smooth and Textured Geomembranes

**Organization:** Geosynthetic Research Institute (GRI)
**Current Edition:** GRI GM13 (2018)
**Applicability:** Governs the minimum property requirements for the 40-mil HDPE geomembrane specified for Reach 7. All supplied rolls of geomembrane must be manufactured conforming to GRI GM-13 and accompanied by certified quality control (CQC) test results from the manufacturer.

**Key minimum properties for 40-mil smooth HDPE per GRI GM-13:**

| Property | Test Method | Minimum Value |
|----------|-------------|---------------|
| Nominal thickness | ASTM D5994 | 40 mil (1.0 mm) |
| Density | ASTM D1505 | 0.940 g/cm³ |
| Tensile Strength at Break | ASTM D6693 Type IV | 128 lb/in |
| Tensile Elongation at Break | ASTM D6693 Type IV | 700% |
| Tear Resistance | ASTM D1004 | 35 lb |
| Puncture Resistance | ASTM D4833 | 65 lb |
| Carbon Black Content | ASTM D4218 | 2.0–3.0% |
| Carbon Black Dispersion | ASTM D5596 | Category 1 or 2 |
| Stress Crack Resistance (NCTL) | ASTM D5397 | 500 hours |
| Oxidative Induction Time (OIT) | ASTM D5885 | 100 minutes |

**Project-specific requirements beyond GRI GM-13:** 100% seam testing (dual-track fusion welds: air pressure test at 30 psi for 5 minutes; extrusion welds: air lance at 25 psi); minimum overlap at transverse seams 12 inches; minimum overlap at longitudinal seams 6 inches; seam tensile strength ≥ 100% of parent material (ASTM D6392).

---

## Lime Stabilization

### ASTM D6276 — See Geotechnical Testing section above.

### TRB Transportation Research Record 1819 / National Lime Association

**Organization:** National Lime Association; Transportation Research Board
**Reference:** Little, D.N. (2000). "Evaluation of Structural Properties of Lime Stabilized Soils and Aggregates, Volume 1: Summary of Findings." National Lime Association.
**Applicability:** Design guidance for determining lime treatment effectiveness, curing requirements, treatment depth, and compaction specifications. Provides empirical correlations between lime content, clay activity, PI reduction, swell reduction, and strength gain. Used to confirm that 6% CaO at 8-inch depth is adequate to eliminate swell potential in the Reach 7 CH clay.

The key design principle established in this reference: lime dosage must be sufficient to (1) satisfy the immediate exchange capacity of the clay (Eades and Grim pH test), (2) provide excess calcium for the long-term pozzolanic reaction, and (3) achieve the pH environment (≥ 12.4) needed to dissolve silica and alumina from the clay mineral structure for CSH and CAH binder formation. The 7-day minimum curing period before loading specified for Reach 7 is consistent with recommendations in this reference.

---

## Canal Design

### USBR Design Standards No. 3 — Canals and Related Structures

**Organization:** U.S. Bureau of Reclamation
**Current Edition:** Chapter 2 (2014 revision); supplemented by earlier chapters
**Applicability:** Primary USBR design reference for canal hydraulics, freeboard calculation, lining thickness, and concrete mix design for irrigation canal rehabilitation. Specifies USBR freeboard formula: F = 0.5 + 0.025 × V × √d.

**Key design standards applied to Reach 7:**
- Minimum freeboard for canals carrying 100–1,000 cfs: 1.5 ft (Table 2-1)
- Manning's n for new concrete lining: 0.013 (smooth formed), 0.014 (unformed surface)
- Minimum concrete lining thickness for design discharge > 100 cfs: 3.5 inches (plain) or 3.0 inches (reinforced)
- Expansion joint spacing: 12 ft (maximum) for concrete-lined canals in expansive clay subgrades
- Waterstop requirement: PVC waterstop at all expansion joints in areas of known expansive soils

---

### USBR Water Measurement Manual

**Organization:** U.S. Bureau of Reclamation
**Current Edition:** 3rd Edition, revised 2001 (reprinted 2014)
**Applicability:** Guidance for inflow-outflow seepage measurement methodology, including calibration of staff gauges, selection of velocity measurement equipment, and calculation of measurement uncertainty. Inflow-outflow measurements conducted in 2023 followed the procedures in Chapter 13 of this manual.

---

## Slope Stability

### ASTM D7928 — Standard Test Method for Particle-Size Distribution (Gradation) of Fine-Grained Soils Using the Sedimentation (Hydrometer) Analysis

**Organization:** ASTM International
**Current Edition:** ASTM D7928-17
**Applicability:** Hydrometer analysis for determination of clay fraction (% < 0.002 mm) in lacustrine clay samples. Clay fraction is required for calculation of activity (A = PI / CF), which confirms montmorillonite as the dominant mineral (A > 0.75 threshold). Used in conjunction with ASTM D6913 (sieve analysis) for the complete gradation curve.

---

### GeoStudio SLOPE/W and SEEP/W — Geostudio 2021

**Organization:** Seequent (formerly GEO-SLOPE International)
**Version:** GeoStudio 2021 (version 10.0)
**Applicability:** Software used for all slope stability analyses (SLOPE/W, Spencer's method) and seepage modeling (SEEP/W, finite element method). Spencer's method implementation satisfies both force and moment equilibrium for arbitrary inter-slice force function, appropriate for non-circular failure surfaces. SEEP/W finite element mesh provides pore pressure distributions imported directly into SLOPE/W for each phreatic surface condition.

SLOPE/W verification: Results for Case 3 (existing geometry, residual strength, mid-season phreatic) cross-checked against hand calculation for the simplified Bishop method and against limit equilibrium analysis in CheckSTABL; agreement within ±0.03 FS units.

---

## Additional Referenced Standards

### ASTM D4318 — Standard Test Methods for Liquid Limit, Plastic Limit, and Plasticity Index of Soils

**Organization:** ASTM International
**Current Edition:** ASTM D4318-17e1
**Applicability:** Atterberg limits testing for all soil samples in the Reach 7 investigation. Results (LL, PL, PI) used for USCS classification, expansive clay assessment, lime treatment design, and compaction control. The PI of the lacustrine clay (PI = 30–42) is both a classification parameter and a direct predictor of swell potential and lime demand.

---

### ASTM D7263 — Standard Test Methods for Laboratory Determination of Density and Unit Weight of Soil Specimens

**Organization:** ASTM International
**Current Edition:** ASTM D7263-09(2018)
**Applicability:** Measurement of total and dry unit weight for all soil samples. Results used to calculate void ratio, relative compaction, overburden stresses for swell testing, and collapse potential calculations.

---

### ASTM D1505 — Standard Test Method for Density of Plastics by the Density-Gradient Technique

**Organization:** ASTM International
**Current Edition:** ASTM D1505-18
**Applicability:** Verification of HDPE geomembrane density per GRI GM-13 requirements (minimum 0.940 g/cm³). Geomembrane density is a quality indicator; below-specification density indicates insufficient resin crystallinity, which reduces stress crack resistance and chemical resistance.

---

### ASTM D6392 — Standard Test Method for Determining the Integrity of Nonreinforced Geomembrane Seams Produced Using Thermo-Fusion Methods

**Organization:** ASTM International
**Current Edition:** ASTM D6392-08(2020)
**Applicability:** Testing of HDPE geomembrane field seam integrity for fusion-welded (hot wedge and extrusion) seams. Project specification requires seam shear strength ≥ 100% of parent material (640 lb/in minimum for 40-mil HDPE) and seam peel strength ≥ 70% of parent material. Combined with 100% non-destructive testing (air channel for dual-track, air lance for extrusion), this ensures a watertight seam system.

---

### ASTM C309 — Standard Specification for Liquid Membrane-Forming Compounds for Curing Concrete

**Organization:** ASTM International
**Current Edition:** ASTM C309-19
**Applicability:** Specification for the curing compound to be applied to the new concrete lining immediately after finishing. Project specifies white-pigmented Type 1-D curing compound (dissipating, water-based) to reflect solar radiation and minimize thermal gradient in the fresh concrete during Idaho summer placement temperatures. Minimum curing efficiency: 55% retention of water (standard evaporation test ASTM C156).

---

### ASTM C457 — Standard Test Methods for Microscopical Determination of Parameters of the Air-Void System in Hardened Concrete

**Organization:** ASTM International
**Current Edition:** ASTM C457/C457M-16
**Applicability:** Verification of air void system parameters (air content, void spacing factor, specific surface) in cores from the existing 1962 lining and in hardened test cylinders from the proposed mix design. Existing lining cores showed spacing factors > 0.010 inch (inadequate for freeze-thaw resistance; threshold is 0.008 inch per ACI 201.2R). New mix design must achieve spacing factor ≤ 0.008 inch from ASTM C457 analysis of pre-construction test cylinders.

---

### ACI 201.2R — Guide to Durable Concrete

**Organization:** American Concrete Institute
**Current Edition:** ACI 201.2R-16
**Applicability:** Comprehensive design guidance for concrete durability, including resistance to freezing and thawing, alkali-silica reaction (ASR), sulfate attack, and abrasion. Provides the technical basis for the new Reach 7 lining mix design requirements: maximum w/c ≤ 0.45, minimum 6% air entrainment, SCM requirement for ASR mitigation (30% Class F fly ash or 40% slag), and non-reactive aggregate per ASTM C1260.

**ASR Mitigation per ACI 201.2R:** For aggregate that may be borderline reactive (ASTM C1260 expansion 0.10–0.20%), the combination of 30% Class F fly ash and limiting the total alkali loading to ≤ 3.0 lb/yd³ (Na₂O equivalent) is accepted as adequate mitigation. The new design uses non-reactive aggregate (ASTM C1260 < 0.10%), making this a belt-and-suspenders provision.

---

### ASTM C42 — Standard Test Method for Obtaining and Testing Drilled Cores and Sawed Beams of Concrete

**Organization:** ASTM International
**Current Edition:** ASTM C42/C42M-18a
**Applicability:** Extraction and compressive strength testing of 2-inch diameter concrete cores from the existing Reach 7 lining. Core compressive strengths were corrected for length-to-diameter ratio per ASTM C42 Table 1 to obtain equivalent 28-day cylinder strengths for comparison against the 3,000 psi design value. Results confirmed that most existing panels fall below design strength (range 980–3,850 psi across all condition categories).
