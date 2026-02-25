# Borehole Geophysics & Logging

## Overview

Borehole geophysics acquires continuous or near-continuous measurements of physical properties along the borehole wall and surrounding formation. Unlike surface geophysics, borehole methods provide high-resolution data at the actual depth of interest, but only at the borehole location.

**Key advantages over surface methods:** Higher resolution, direct measurement at depth, continuous profiling, less ambiguity in interpretation. **Limitations:** Only samples material near the borehole (point measurement in plan view), borehole condition affects results, requires an open (uncased) or PVC-cased borehole.

## Seismic Methods (Borehole)

### Downhole Seismic (ASTM D7400)
**Principle:** Seismic source at surface; geophone(s) clamped at various depths in borehole. Measures P-wave and S-wave travel time from surface to each depth. Produces Vp and Vs profiles.

**Advantages:** Direct Vs measurement at specific depths. Standard for Vs30 verification. Single borehole required.

**Field procedure:** Geophone (3-component) lowered and clamped at 1–2 m intervals. Surface source: horizontal plank struck with sledgehammer for S-waves (reversed polarity for picking). P-wave from vertical impact.

**Interpretation:** First arrivals picked on each trace. Interval velocity between adjacent measurement points: Vs = Δz / Δt. Correct for inclined ray path if offset source.

### Crosshole Seismic (ASTM D4428)
**Principle:** Source in one borehole, receiver(s) in adjacent borehole(s), at the same depth. Measures direct travel time horizontally between boreholes.

**Advantages:** Measures horizontal Vp and Vs (anisotropy assessment). Higher confidence in velocity at specific depth than downhole.

**Requirements:** Minimum 2 boreholes (3 preferred), precisely surveyed for inclination (deviation survey mandatory), typically 3–5 m apart. PVC-cased, grouted boreholes.

### Suspension (PS) Logging
**Principle:** Single-borehole method using a probe with source and two receivers separated by 1 m. Measures Vp and Vs of the formation adjacent to the borehole at each depth.

**Advantages:** Very high resolution (1 m intervals), deep capability (hundreds of meters), single borehole. Widely used for deep Vs profiling (nuclear facilities, tall buildings, critical infrastructure).

**Requirements:** Open or PVC-cased fluid-filled borehole. Minimum diameter ~75 mm. Borehole must be fluid-filled (water or drilling fluid).

## Imaging Tools

### Optical Televiewer (OTV)
**Principle:** CCD camera photographs the borehole wall continuously, producing an oriented, unwrapped 360° image of the borehole surface.

**Applications:** Fracture/discontinuity identification and orientation (dip/dip direction), lithology contacts, bedding, foliation, cavity detection, core loss correlation.

**Requirements:** Clear water or air-filled borehole. Does NOT work in muddy/turbid water. Borehole must be open (no casing at logged interval). Oriented by magnetometer/accelerometer (avoid near steel casing).

### Acoustic Televiewer (ATV)
**Principle:** Rotating ultrasonic transducer measures travel time and amplitude of reflected pulse from borehole wall. Travel time → caliper (borehole shape). Amplitude → surface hardness/roughness.

**Applications:** Same as OTV (fracture orientation, lithology), but works in turbid/opaque fluid. Amplitude image distinguishes hard (high amplitude) from soft (low amplitude) materials. Can identify open vs. sealed fractures.

**Requirements:** Fluid-filled borehole (water or mud — NOT air). Works through turbid fluid (advantage over OTV).

### Combined OTV + ATV
Best practice for comprehensive borehole characterization: OTV for true-color lithology and visual features; ATV for fracture aperture, sealed vs. open distinction, and use in turbid zones. Data merged for fracture analysis with oriented dip/azimuth exported to stereonets.

## Conventional Logs

### Natural Gamma
**Principle:** Measures naturally occurring gamma radiation from K-40, U-238, Th-232 decay series in the formation. Clay minerals (illite, montmorillonite) and potassium feldspar produce high gamma counts.

**Applications:** Lithology discrimination — clay/shale (high gamma) vs. sand/gravel/limestone (low gamma). Best single log for basic stratigraphy. Works through PVC and steel casing.

**Units:** API (American Petroleum Institute) gamma units or counts per second (cps).

### Spontaneous Potential (SP)
**Principle:** Measures natural electrical potential difference between the borehole fluid and formation. SP response driven by salinity contrast between drilling fluid and formation water.

**Applications:** Identifying permeable zones (sand/gravel show SP deflection), estimating formation water salinity. Less used in geotechnical than petroleum, but valuable for hydrogeology.

### Resistivity Logs (Normal, Lateral, Focused)
**Principle:** Injects current and measures formation resistivity at various investigation depths. Short-normal (16 in) for near-borehole; long-normal (64 in) for deeper. Focused (laterolog) for thin-bed resolution.

**Applications:** Porosity estimation (Archie's law), water quality (salinity), lithology correlation, fracture detection (low resistivity in fractured zones with water).

### Caliper
**Principle:** Mechanical arms or acoustic measurement of borehole diameter along depth.

**Applications:** Borehole condition (washouts, breakouts, squeezing), volume calculations for grouting, identification of fractured/weak zones (enlarged borehole), casing placement planning.

### Full-Waveform Sonic
**Principle:** Transmitter generates acoustic pulse in borehole fluid; array of receivers records full waveform (P, S, Stoneley, tube waves). Processing extracts P-wave and S-wave velocity, dynamic elastic moduli.

**Applications:** Vp and Vs profiling (complementary to downhole/crosshole), rock quality assessment (high velocity = competent), fracture detection (Stoneley wave attenuation at fractures), cement bond evaluation in cased holes.

## Advanced Logs

### Neutron-Porosity
Measures hydrogen content (proxy for water-filled porosity). Used in hydrogeology for porosity profiling.

### Density (Gamma-Gamma)
Measures bulk density by gamma backscatter. Combined with sonic log to calculate impedance for synthetic seismograms.

### Nuclear Magnetic Resonance (NMR)
Measures free water content and pore size distribution. Distinguishes bound water (clay) from mobile water (producible). Advanced hydrogeological applications.

### Flowmeter
Spinner or heat-pulse flowmeter measures vertical flow velocity in the borehole under ambient or pumped conditions. Identifies permeable zones contributing flow.

## Fracture Analysis from Televiewer Data

Fracture traces appear as sinusoids on the unwrapped borehole image:
- **Dip angle:** tan(α) = amplitude of sinusoid / borehole diameter
- **Dip direction:** azimuth of the sinusoid's lowest point (for true dip)
- **Open vs. closed:** ATV amplitude — open fractures show low amplitude (soft); sealed fractures may show high amplitude
- **Aperture:** Estimated from ATV travel time anomaly or OTV visual

Data exported to stereonets (equal-area or equal-angle projection) for structural analysis. Identify fracture sets, compare with surface mapping, input to rock mass classification and kinematic stability analysis.
