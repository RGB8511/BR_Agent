# Bearing Capacity

## General Bearing Capacity Theory

Bearing capacity is the maximum pressure a foundation soil can support without shear failure. The general bearing capacity equation for a shallow foundation (D_f ≤ B) is:

q_u = c' × N_c × s_c × d_c × i_c + q × N_q × s_q × d_q × i_q + 0.5 × γ × B × N_γ × s_γ × d_γ × i_γ

where:
- First term: cohesion contribution
- Second term: surcharge (overburden) contribution
- Third term: soil weight (width) contribution
- s, d, i = shape, depth, and inclination correction factors
- q = γ × D_f (overburden pressure at foundation level)
- B = foundation width (use B' = effective width for eccentric loading)

### Failure Modes

**General shear failure:** Well-defined failure surface reaching ground surface. Dense sands, stiff clays. Clear peak in load-settlement curve. Terzaghi/Meyerhof equations apply directly.

**Local shear failure:** Failure surface does not reach surface. Loose to medium sands, soft to medium clays. Gradual, no clear peak. Terzaghi suggested using reduced parameters: c'* = 2/3 × c', φ'* = arctan(2/3 × tanφ').

**Punching shear failure:** Foundation punches straight down. Very loose sands, very soft clays. No visible failure surface. Settlement analysis governs rather than bearing capacity.

## Terzaghi's Original Equation (1943)

For strip footing on horizontal ground:

q_u = c' × N_c + q × N_q + 0.5 × γ × B × N_γ

**Shape corrections (Terzaghi):**
- Square: q_u = 1.3c'N_c + qN_q + 0.4γBN_γ
- Circular: q_u = 1.3c'N_c + qN_q + 0.3γBN_γ (B = diameter)

Terzaghi N-factors:
- N_c, N_q from Prandtl (1921) and Reissner (1924):
  N_q = e^(πtanφ') × tan²(45° + φ'/2)
  N_c = (N_q - 1) × cotφ'
- N_γ: various solutions exist (Meyerhof, Hansen, Vesic — different values)

## General Bearing Capacity (Meyerhof / Hansen / Vesic)

### N-Factors (Exact for N_c, N_q; Approximate for N_γ)

N_q = e^(πtanφ') × tan²(45° + φ'/2) (Prandtl-Reissner, exact)
N_c = (N_q - 1) × cotφ'  (Prandtl, exact; for φ' = 0: N_c = 5.14)
N_γ varies by author:
- Meyerhof: N_γ = (N_q - 1) × tan(1.4φ')
- Hansen: N_γ = 1.5 × (N_q - 1) × tanφ'
- Vesic: N_γ = 2 × (N_q + 1) × tanφ'

### Shape Factors (Hansen/Vesic)
- s_c = 1 + (B/L)(N_q/N_c)
- s_q = 1 + (B/L)tanφ'
- s_γ = 1 - 0.4(B/L)

### Depth Factors (Hansen)
For D_f/B ≤ 1:
- d_c = 1 + 0.4(D_f/B)
- d_q = 1 + 2tanφ'(1-sinφ')²(D_f/B)
- d_γ = 1.0

For D_f/B > 1: replace (D_f/B) with arctan(D_f/B) in radians.

### Inclination Factors (Hansen)
For inclined load at angle β from vertical:
- i_c = i_q - (1-i_q)/(N_c × tanφ')
- i_q = (1 - 0.5H/(V + Bc'cotφ'))²
- i_γ = (1 - 0.7H/(V + Bc'cotφ'))²

## Eccentric Loading

For loads applied at eccentricity e_B and e_L from the center:

Effective dimensions: B' = B - 2e_B, L' = L - 2e_L

Use B' and L' in all bearing capacity calculations.

**Kern rule:** For no tensile stress under the footing, eccentricity must be within B/6 (strip) or the kern zone (rectangular).

## Undrained Bearing Capacity (φ_u = 0)

For saturated clay under rapid loading:

q_u = 5.14 × s_u × s_c × d_c × i_c + q

For a strip footing with no corrections: q_u = 5.14 s_u + γD_f

Net ultimate bearing capacity: q_net = q_u - q = 5.14 × s_u (for strip, no depth correction)

## Factor of Safety

q_all = q_u / FS

Typical FS values:
- Dead + normal live load: FS = 3.0
- Maximum load including wind/seismic: FS = 2.0–2.5
- Temporary structures: FS = 2.0

**Note:** In modern practice, settlement almost always controls foundation design in sands, and often in clays as well. Bearing capacity failure is relatively rare for properly sized foundations.
