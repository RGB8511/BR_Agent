# GeoLab Knowledge Packages — v2.0

**Generated:** 2026-02-24
**Packages:** 32 | **Equations:** 319 | **Tables:** 153 | **Files:** 160

## Disciplines & Packages

### Foundations (L0) — 4 packages
| Package | Equations | Tables |
|---------|-----------|--------|
| soil-classification | 6 | 8 |
| phase-relationships | 18 | 4 |
| rock-classification | 5 | 6 |
| mineralogy-clay | 4 | 5 |

### Soil Mechanics (L1) — 10 packages
| Package | Equations | Tables |
|---------|-----------|--------|
| effective-stress | 10 | 3 |
| permeability-seepage | 14 | 3 |
| compaction | 6 | 4 |
| consolidation | 18 | 4 |
| shear-strength | 14 | 5 |
| lateral-earth-pressure | 12 | 3 |
| bearing-capacity | 12 | 4 |
| slope-stability | 10 | 4 |
| deep-foundations | 14 | 5 |

### Site Investigation (L1) — 1 package
| Package | Equations | Tables |
|---------|-----------|--------|
| in-situ-testing | 16 | 6 |

### Rock Mechanics (L1) — 4 packages
| Package | Equations | Tables |
|---------|-----------|--------|
| hoek-brown | 12 | 5 |
| rock-mass-classification | 8 | 7 |
| discontinuity-shear-strength | 8 | 4 |
| rock-slope-stability | 8 | 3 |

### Geotechnical — Advanced (L2) — 3 packages
| Package | Equations | Tables |
|---------|-----------|--------|
| embankment-dams | 10 | 6 |
| seismic-liquefaction | 12 | 4 |
| ground-improvement | 10 | 5 |

### Concrete (L0–L1) — 4 packages
| Package | Equations | Tables |
|---------|-----------|--------|
| cement-hydration (L0) | 8 | 5 |
| mix-design (L1) | 8 | 6 |
| durability (L1) | 10 | 5 |
| testing (L1) | 10 | 5 |

### Coatings & Corrosion (L0–L1) — 4 packages
| Package | Equations | Tables |
|---------|-----------|--------|
| corrosion-fundamentals (L0) | 8 | 5 |
| coating-systems (L1) | 6 | 6 |
| surface-preparation (L1) | 4 | 5 |
| cathodic-protection (L1) | 8 | 5 |

### Hydrology (L0–L1) — 3 packages
| Package | Equations | Tables |
|---------|-----------|--------|
| fundamentals (L0) | 12 | 5 |
| open-channel (L1) | 10 | 4 |
| flood-frequency (L1) | 8 | 4 |

## Package Structure
Each package contains 5 files:
- `_manifest.json` — metadata, dependencies, tags
- `theory.md` — concepts and explanations
- `equations.json` — structured equations with variables and sources
- `tables.json` — structured reference/design tables
- `standards.md` — relevant standards and specifications

## Ingestion Order
1. **L0 first** (no dependencies): foundations/*, concrete/cement-hydration, coatings/corrosion-fundamentals, hydrology/fundamentals
2. **L1 parallel**: soil-mechanics/*, rock-mechanics/*, site-investigation/*, concrete/mix-design+durability+testing, coatings/coating-systems+surface-preparation+cathodic-protection, hydrology/open-channel+flood-frequency
3. **L2 last**: geotechnical-L2/*

## Changelog
- v1.0: 15 packages (foundations + core soil/rock mechanics)
- v1.1: 18 packages (+ slope-stability, deep-foundations, embankment-dams, seismic-liquefaction)
- v2.0: 32 packages (+ ground-improvement, concrete ×4, coatings ×4, hydrology ×3, all gaps filled)
