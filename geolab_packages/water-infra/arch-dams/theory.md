# Arch Dam Design & Analysis

## Fundamental Concept

Arch dams transfer the majority of the hydrostatic load horizontally to the canyon walls (abutments) through arch action, rather than relying on their own weight as gravity dams do. This structural efficiency allows much thinner cross-sections — typically 1/5 to 1/3 the volume of an equivalent gravity dam — but requires strong, competent rock abutments and a narrow to moderately wide valley.

## Site Requirements

### Valley Geometry
- **Ideal:** Narrow, V-shaped or U-shaped canyons with crest length-to-height ratio (L/H) of 2:1 to 5:1
- **L/H < 3:** Classical thin arch — highly efficient
- **L/H 3–6:** Thick arch or arch-gravity — transitional
- **L/H > 6:** Generally not economical for arch — consider gravity or embankment

### Foundation Requirements
- Competent rock capable of resisting arch thrust
- Both abutments must be geologically sound — asymmetric abutments complicate but don't preclude arch dams
- Minimum foundation rock: uniaxial compressive strength > 10–20 MPa, rock mass modulus > 5–10 GPa
- Geological features (faults, shear zones, joints, foliation) must be mapped and their effect on abutment stability analyzed
- Deformability contrast between abutments and foundation affects load distribution

## Arch Dam Types

### Constant-Radius Arch
- Single center of curvature at each elevation — simplest geometry
- Upstream face is vertical or slightly curved vertically
- Thicker at base, thinner at crest
- Suitable for symmetrical valleys

### Variable-Radius (Constant-Angle) Arch
- Radius decreases from crest to base, maintaining a constant central angle (≈ 100–140°)
- More uniform stress distribution than constant-radius
- Better fit to V-shaped valleys

### Double-Curvature (Cupola) Arch
- Curved in both horizontal (arch) and vertical (cantilever) directions
- Shell-like behavior — most structurally efficient
- Used for the highest and thinnest arch dams
- Complex geometry requires 3D analysis
- Examples: Hoover Dam (thick arch-gravity), Morrow Point Dam (thin double-curvature)

## Analysis Methods

### Thin Cylinder Formula (Preliminary)
For a thin arch ring under uniform radial pressure:

σ = P × R / t

where σ = arch compressive stress, P = hydrostatic pressure, R = arch radius, t = arch thickness.

This gives a quick estimate for initial proportioning. Optimal central angle for minimum concrete volume ≈ 133° (theoretical). Practical range: 100–150°.

### Independent Arch Method
Each horizontal arch ring analyzed independently as a circular (or parabolic) arch under hydrostatic load. Ignores cantilever action — conservative for thin arches, unconservative for thick arches.

### Trial Load Method (USBR)
The classical USBR method that divides the dam into horizontal arch elements and vertical cantilever elements. Applied loads are distributed between arches and cantilevers such that deflections at each node are compatible. Iterative procedure until deflection compatibility is achieved at all nodes.

- Arch elements carry load by flexure and thrust
- Cantilever elements carry load by flexure and shear
- Foundation flexibility modeled through abutment deformation
- Can include tangential shear and twist

### Finite Element Method (FEM)
Modern standard for arch dam analysis. 3D solid or shell elements model the dam body, foundation rock, and reservoir:
- Linear static analysis for normal loading
- Nonlinear analysis for contraction joint opening, cracking, foundation sliding
- Dynamic analysis for seismic loading (response spectrum or time-history)
- Thermal stress analysis (seasonal temperature, construction cooling)
- Dam-reservoir interaction (added mass or coupled fluid elements)

Industry software: FLAC3D, DIANA, Abaqus, ANSYS, USBR ADSAP.

## Load Combinations

Same general framework as gravity dams (usual, unusual, extreme) with additional considerations:
- **Temperature:** Critical for arch dams. Temperature drop (winter) increases arch stress. Temperature rise (summer) may open contraction joints.
- **Foundation deformation:** Differential deformation between abutments affects stress distribution
- **Seismic:** Arch dams are more sensitive to cross-valley (arch-axis) ground motion

### Typical Load Cases
1. **Usual:** Normal full reservoir + dead weight + temperature (mean annual)
2. **Unusual:** Full reservoir + temperature extremes; or earthquake (OBE)
3. **Extreme:** PMF + drains inoperative; or MCE seismic

## Stability Assessment

### Dam Body Stresses
- Maximum compressive stress: ≤ 0.30 × f'c for usual, 0.40 × f'c for unusual (FERC)
- Tensile stress: limited or zero for usual (arch action should maintain compression); minor tension acceptable in unusual/extreme with adequate factors of safety
- Principal stresses checked at upstream and downstream faces

### Abutment (Foundation) Stability
The critical failure mode for arch dams — the arch thrusts must be safely transferred into the rock mass.
- Identify potential sliding planes (faults, shear zones, bedding, joints)
- 3D wedge stability analysis: arch thrust + gravity + uplift vs. shear resistance on sliding surfaces
- FS against sliding: ≥ 2.0 usual, ≥ 1.5 unusual, > 1.0 extreme (FERC guidelines)
- Rock mass shear strength: Mohr-Coulomb (c, φ) or Barton-Bandis for joints

### Foundation Treatment
- **Grout curtain:** Deep grouting to reduce seepage and uplift. Often 0.3–0.5H deep.
- **Drainage curtain:** Drain holes downstream of grout curtain to relieve uplift.
- **Consolidation grouting:** Shallow grouting to improve rock mass modulus at dam-foundation contact.
- **Dental concrete:** Fill surface defects, shear zones, and overhangs with concrete.
- **Rock anchors/tendons:** Post-tensioned anchors to improve abutment stability where needed.

## Contraction Joints and Grouting

Arch dams are constructed in monolith blocks separated by contraction joints:
- Joints allow concrete to cool and shrink without cracking
- After cooling, joints are grouted with cement grout to make the dam monolithic
- Grouting is staged — typically from lowest joint upward
- Embedded grout pipes, shear keys (interlocking surfaces), and waterstops at each joint
- Joint opening monitored during cooling and grouting
