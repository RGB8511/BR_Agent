# Rock Slope Stability

## Failure Modes

Rock slope failures are controlled by discontinuity geometry relative to the slope face. Four primary modes:

### Planar Failure
A block slides along a single discontinuity plane that daylights in the slope face. Requirements:
1. Strike of failure plane approximately parallel to slope face (within ±20°)
2. Dip of failure plane less than dip of slope face (daylight condition)
3. Dip of failure plane greater than friction angle of the surface (kinematic condition)
4. Release surfaces (lateral boundaries) present or negligible lateral resistance

### Wedge Failure
A block defined by two intersecting discontinuity planes slides along the line of intersection. Most common failure mode in rock slopes.
Requirements:
1. Line of intersection plunges toward the slope face
2. Plunge of intersection less than slope face dip (daylights)
3. Plunge of intersection greater than friction angle along sliding surfaces

### Toppling Failure
Columns or blocks rotate forward about a fixed base point. Occurs when steeply dipping discontinuities strike approximately parallel to the slope face.
Requirements:
1. Strike of discontinuities within ~30° of slope face strike
2. Discontinuities dip steeply into the slope face (180° - dip < slope face dip + friction angle → base sliding; for toppling: block height/width > critical ratio)

### Circular Failure
Failure through highly fractured, weak, or soil-like rock masses where no single discontinuity controls. Analyzed using soil mechanics methods (Bishop, Morgenstern-Price) with Hoek-Brown or equivalent Mohr-Coulomb parameters.

## Kinematic Analysis

Stereonet-based assessment of whether the orientation of discontinuities permits a specific failure mode, given the slope geometry.

### Stereonet Conventions
- Great circles represent planes (slope face, discontinuities)
- Poles represent the normals to planes
- Friction cone: small circle at angle φ from center of stereonet

### Markland Test (Modified)

**Planar failure:** A pole falls in the critical zone (crescent between slope face great circle and friction circle, in the dip direction of the slope).

**Wedge failure:** The intersection line of two planes falls in the zone between the slope face great circle and the friction circle.

**Toppling:** The pole to the discontinuity falls in the toppling zone (near the perimeter of the stereonet, opposite the dip direction of the slope face).

## Planar Failure Analysis

For a single plane with tension crack, water pressure, and seismic loading:

FS = [cA + (W cosψ_p - U - V sinψ_p + T cosθ) × tanφ] / [W sinψ_p + V cosψ_p - T sinθ]

where:
- W = weight of sliding block
- ψ_p = dip of failure plane
- U = uplift water force on failure plane
- V = water force in tension crack
- T = reinforcement force at angle θ below horizontal
- A = area of failure plane
- c, φ = Mohr-Coulomb parameters of the failure plane

For dry slope with no reinforcement:
FS = [c × A + W cosψ_p × tanφ] / [W sinψ_p]

If c = 0: FS = tanφ / tanψ_p (simplest form — friction-only)

## Wedge Failure Analysis

Full 3D wedge analysis requires resolving forces along two sliding planes. The simplified Hoek & Bray method:

FS = (R_A × tanφ_A + R_B × tanφ_B) / W sinψ_i

where R_A, R_B = normal reactions on planes A and B, ψ_i = plunge of intersection line, φ_A, φ_B = friction angles on each plane.

For equal friction on both planes: FS = (F_w / F_s) × (tanφ / tanψ_i)

where F_w/F_s are geometric factors from wedge geometry (tabulated or computed from stereonet).

## Rockfall

Detached blocks fall, bounce, and roll down slope. Analysis includes:
- Source identification (overhanging blocks, weathered zones)
- Trajectory analysis (2D: Ritchie, RocFall; 3D: CRSP)
- Mitigation: catchment ditches (Ritchie criteria), barriers, mesh, bolting, scaling

**Ritchie ditch criteria:** Empirical ditch width and depth based on slope height and face angle. Widely used in highway rock cut design.

## Design Criteria

Typical FS requirements:
- Permanent slopes, high consequence: FS ≥ 1.5
- Temporary slopes: FS ≥ 1.25
- Mining (temporary pit walls): FS ≥ 1.2
- Natural slopes (hazard assessment): FS = 1.0 is equilibrium

**Probability of failure (PoF):** Increasingly used alongside FS. Typical acceptance criteria: PoF < 10% (general), PoF < 5% (infrastructure), PoF < 1% (life safety critical).
