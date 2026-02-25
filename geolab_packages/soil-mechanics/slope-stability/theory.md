# Slope Stability Analysis

## Overview

Slope stability analysis determines the factor of safety (FS) against shear failure along a potential slip surface. FS = available shear strength / mobilized shear stress. FS > 1.0 implies stability.

## Infinite Slope Analysis

For shallow translational failures where the slip surface is parallel to the slope face and the slope is long relative to the depth of sliding.

**Dry slope (cohesionless):**
FS = tanφ' / tanβ

where β = slope angle. Stable when β < φ'. Independent of depth.

**Submerged slope (seepage parallel to slope):**
FS = (γ'/γ_sat) × (tanφ' / tanβ)

Seepage parallel to slope approximately halves the FS compared to dry conditions (γ'/γ_sat ≈ 0.5).

**Infinite slope with cohesion:**
FS = c' / (γ × z × sinβ × cosβ) + tanφ' / tanβ - (u × tanφ') / (γ × z × sinβ × cosβ)

where z = depth to slip surface, u = pore water pressure at base.

## Method of Slices — General Framework

The soil mass above a trial slip surface is divided into vertical slices. For each slice:
- W = weight = γ × b × h (average)
- N = normal force on slip surface base
- T = shear force on slip surface base
- E = interslice normal forces (left, right)
- X = interslice shear forces (left, right)
- U = pore pressure force on slice base

The methods differ in how they handle the statical indeterminacy of the interslice forces.

## Bishop's Simplified Method (1955)

Satisfies overall moment equilibrium for circular slip surfaces. Assumes interslice shear forces X = 0.

FS = Σ[c'b + (W - ub)tanφ'] / m_α / Σ(W sinα)

where m_α = cosα + (sinα × tanφ')/FS

This is iterative (FS appears on both sides) — solved by trial. Converges in 3–5 iterations typically.

**Accuracy:** Excellent for circular surfaces (within 1–2% of rigorous methods). Not recommended for non-circular surfaces.

**Usage:** Most common method for circular slip surface analysis. Required/accepted by most design codes.

## Spencer's Method (1967)

Satisfies both force and moment equilibrium. Assumes interslice forces are parallel (constant inclination θ). Solves for both FS and θ simultaneously.

**Accuracy:** Rigorous for both circular and non-circular surfaces. Results very close to Morgenstern-Price.

## Morgenstern-Price Method (1965)

Most rigorous method. Satisfies both force and moment equilibrium. Uses a variable interslice force function f(x) relating X = λ × f(x) × E.

**Accuracy:** Complete equilibrium solution. Reference standard for all other methods. Suitable for any slip surface geometry.

## Undrained Analysis (φ = 0)

For saturated clays under rapid loading:

FS = Σ(s_u × Δl) / Σ(W sinα)

For circular surface with constant s_u:
FS = s_u × R × θ_arc / Σ(W × d)

where R = radius, θ_arc = arc angle, d = moment arm from center of rotation.

## Pore Pressure Representation

### Pore Pressure Ratio (r_u)
r_u = u / (γ × z)

where u = pore pressure at point on slip surface, z = depth below ground surface.

FS is strongly sensitive to r_u. Typical values:
- r_u = 0: dry slope
- r_u = 0.25–0.50: typical for slopes with water table
- r_u = 0.50: water table at ground surface, seepage parallel to slope

### Piezometric Line
Defines pore pressure from actual water table geometry. More accurate than r_u for non-uniform pore pressure distributions.

### Steady-State Seepage
Flow net or numerical seepage analysis provides pore pressure field. Most accurate for dam slopes.

## Seismic Pseudostatic Analysis

Apply a horizontal force k_h × W and optionally vertical force k_v × W to each slice.

FS = FS_static adjusted for seismic forces

k_h = horizontal seismic coefficient (fraction of g). Typical: 0.05–0.25 depending on seismicity and design criteria.

**Hynes-Griffin & Franklin (1984):** Use k_h = 0.5 × PGA/g with yield acceleration concept and 80% of s_u for clays.

**ASCE 7 / FEMA:** k_h depends on mapped spectral acceleration and site class.

Acceptable FS under pseudostatic loading: typically FS ≥ 1.0–1.1 (since the earthquake loading is transient).

## Rapid Drawdown

Critical for dam upstream slopes. Three-stage analysis:
1. Steady-state seepage at normal pool (establish effective stress and pore pressure)
2. Instantaneous drawdown of reservoir (undrained response in low-permeability materials)
3. Analyze stability with changed water loading and undrained strengths

**Duncan, Wright & Wong (1990) method:** Three-stage effective stress approach using staged undrained strength and pore pressure redistribution. Now standard USACE practice.

## Back-Analysis

When a slope has failed, back-analysis determines the mobilized shear strength at FS = 1.0. Provides the best estimate of in-situ operative strength along the failure surface. Used to:
- Calibrate strength parameters for adjacent slopes
- Determine residual vs. peak strength mobilization
- Validate laboratory test results
