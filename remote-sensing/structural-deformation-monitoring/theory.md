# Structural Deformation Monitoring from Point Clouds

## Concept

Repeat TLS or UAS surveys of a structure at different time epochs enable detection and quantification of surface displacement (settlement, tilt, bulging, convergence). By comparing point clouds from epoch T₀ (baseline) to epoch Tₙ (monitoring), deformation maps are generated showing magnitude and direction of movement at every measurable surface point.

This approach provides **full-field** deformation data — thousands to millions of measurement points — versus traditional instrumentation which provides data at discrete points only.

## Monitoring Workflow

1. **Baseline survey (T₀):** Highest quality. Establish permanent reference targets (survey nails, prisms, stable benchmarks on stable ground). Comprehensive TLS/UAS coverage.
2. **Monitoring surveys (T₁, T₂, ...):** Same scanner positions, same targets, same acquisition parameters as baseline. Consistency is critical.
3. **Registration:** Align all epochs to common coordinate system using stable reference points/targets. Critical: reference points must be demonstrably stable (outside deformation zone).
4. **Distance computation:** M3C2, C2C, or mesh-to-mesh comparison between epochs.
5. **Significance testing:** Apply Level of Detection (LoD) threshold. Only report deformations exceeding LoD.
6. **Time-series analysis:** Track displacement at key points through all epochs. Plot displacement vs. time for trend analysis.

## Distance Computation Methods

### Cloud-to-Cloud (C2C)
Simplest: nearest-point distance between two clouds. Fast but unsigned (always positive), biased by point density differences and surface roughness. Suitable for quick visualization; not recommended for quantitative monitoring.

### Cloud-to-Mesh (C2M)
Compare point cloud to a meshed reference surface. Signed distance (positive = outward, negative = inward). Mesh quality affects result. Better than C2C but mesh smoothing may mask local detail.

### M3C2 (Multiscale Model-to-Model Cloud Comparison)
Gold standard for deformation monitoring. Computes signed distance along local surface normal between two point clouds. Provides per-point confidence interval based on local point cloud roughness and registration uncertainty.

**Key parameters:**
- **Normal scale (D):** Diameter over which surface normal is estimated. Larger D = smoother normals (less noise, less local detail). Typically 5–20× point spacing.
- **Projection scale (d):** Diameter of cylinder projected along normal to average points. Larger d = less noise but more spatial averaging. Typically 2–10× point spacing.

**Level of Detection (LoD₉₅%):**
LoD = ±1.96 × √(σ₁²/n₁ + σ₂²/n₂ + reg²)

where σ₁, σ₂ = local roughness in each epoch, n₁, n₂ = number of points in projection cylinders, reg = registration uncertainty.

## Deformation Types Detectable

### Settlement
Vertical downward displacement. Detected as negative vertical component of M3C2 distance on horizontal surfaces (dam crest, building slabs, embankment tops). Resolution: 2–10 mm typical for TLS monitoring.

### Tilt / Rotation
Detected as differential displacement across a surface — one side moves more than the other. Compute by fitting planes to deformation data. Tilt = arctan(Δd / L) where Δd = differential displacement, L = distance.

### Bulging / Deflection
Outward displacement of a surface (retaining wall under load, dam face under reservoir). M3C2 distance map shows positive (outward) displacement pattern centered on maximum deflection.

### Convergence (Tunnels)
Tunnel cross-section changes over time due to ground movement. Extract cross-sections at regular intervals from each epoch; compare diameters. Or use C2C/M3C2 on full tunnel surface.

### Crack Opening
Detected as displacement discontinuity across a crack — opposite sides move apart. Requires high point density (> 5000 pts/m²) and precise registration. Crack opening displacement measured perpendicular to crack trace.

## Reference Frame Considerations

**Stable reference:** Critical that reference targets/areas are truly stable. If reference moves, all deformations are biased. Use multiple independent references; check for consistency.

**Absolute vs. relative:** Absolute deformation (in real-world coordinates) requires georeferenced stable references. Relative deformation (change between epochs) requires only consistent registration — can use cloud-to-cloud alignment on stable portions.

**Thermal effects:** Steel and concrete expand/contract with temperature (α ≈ 12 × 10⁻⁶/°C). A 30 m concrete dam face changes ~1.4 mm per 4°C temperature change. Survey at consistent temperature, or apply thermal correction.

## Monitoring Frequency

Depends on expected deformation rate and required response time. Construction monitoring: daily to weekly. Long-term dam monitoring: monthly to annually. Post-event assessment: immediately + follow-up series.
