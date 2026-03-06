import React, { useState, useRef, useCallback, useEffect, useMemo } from 'react';
import katex from 'katex';
import 'katex/dist/katex.min.css';

// ════════════════════════════════════════════════════════════════
// THEME COLORS
// ════════════════════════════════════════════════════════════════
const COLORS = {
  bg: '#0a0f1a',
  panelBg: '#0d1321',
  cardBg: '#111827',
  cardBorder: '#1e293b',
  // Level 0: Router
  router: '#00d4aa',
  // Level 1: Projects
  project: '#4a9eff',
  // Level 2: Domains
  domain: '#9775fa',
  accent: '#4a9eff',
  textPrimary: '#e2e8f0',
  textSecondary: '#94a3b8',
  textDim: '#475569',
  chunkSource: '#d4879c',
  scoreGreen: '#40c057',
  scoreYellow: '#f0c040',
  scoreOrange: '#e8a838',
};

function scoreColor(score) {
  if (score >= 0.9) return COLORS.scoreGreen;
  if (score >= 0.8) return COLORS.scoreYellow;
  return COLORS.scoreOrange;
}

// ════════════════════════════════════════════════════════════════
// LIVE MODE CONFIG
// ════════════════════════════════════════════════════════════════
const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8100';

const DISCIPLINE_MAP = {
  'geotechnical':  { icon: '\uD83E\uDEA8', color: '#9775fa' },
  'water-infra':   { icon: '\uD83C\uDF0A', color: '#4a9eff' },
  'concrete':      { icon: '\uD83E\uDDF1', color: '#e8a838' },
  'structural':    { icon: '\uD83C\uDFD7\uFE0F', color: '#40c057' },
  'environmental': { icon: '\uD83C\uDF3F', color: '#51cf66' },
  'dam-safety':    { icon: '\uD83D\uDD12', color: '#f06595' },
  'geology':       { icon: '\u26F0\uFE0F', color: '#cc5de8' },
};

function transformTopology(tree) {
  const children = (tree.children || []).map((child) => {
    // Discipline node (has disc:xxx id)
    if (child.id && child.id.startsWith('disc:')) {
      const disc = child.discipline || child.id.replace('disc:', '');
      const mapped = DISCIPLINE_MAP[disc] || { icon: '\uD83D\uDCC2', color: COLORS.domain };
      return {
        id: child.id,
        icon: mapped.icon,
        label: child.label,
        color: mapped.color,
        docCount: child.chunk_count,
        children: (child.children || []).map((pkg) => ({
          id: pkg.id || pkg.package_id,
          icon: '\uD83D\uDCC4',
          label: pkg.label,
          color: mapped.color,
          docCount: pkg.chunk_count,
        })),
      };
    }
    // Project node (has project: prefix in id)
    if (child.id && child.id.startsWith('project:')) {
      return {
        id: child.id,
        icon: '\uD83D\uDCC1',
        label: child.label,
        color: COLORS.project,
        docCount: child.chunk_count,
      };
    }
    // Fallback
    return {
      id: child.id,
      icon: '\uD83D\uDCC2',
      label: child.label,
      color: COLORS.domain,
      docCount: child.chunk_count,
      children: (child.children || []).map((pkg) => ({
        id: pkg.id || pkg.package_id,
        icon: '\uD83D\uDCC4',
        label: pkg.label,
        color: COLORS.domain,
        docCount: pkg.chunk_count,
      })),
    };
  });

  return {
    id: 'router',
    icon: '\u25C9',
    label: tree.label || 'Routing Agent',
    color: COLORS.router,
    children,
  };
}

// ════════════════════════════════════════════════════════════════
// HARDCODED AGENT TREE (demo fallback)
// ════════════════════════════════════════════════════════════════
const AGENT_TREE = {
  id: 'router',
  icon: '\u25C9',
  label: 'Routing Agent',
  color: COLORS.router,
  children: [
    {
      id: 'jc',
      icon: '\uD83D\uDCC1',
      label: 'Juniper Canyon Dam',
      color: COLORS.project,
      children: [
        { id: 'jc-lab', icon: '\uD83E\uDDEA', label: 'Lab Testing', docCount: 5, color: COLORS.domain },
        { id: 'jc-field', icon: '\uD83D\uDD0D', label: 'Field Exploration', docCount: 5, color: COLORS.domain },
        { id: 'jc-design', icon: '\uD83D\uDCD0', label: 'Design & Analysis', docCount: 5, color: COLORS.domain },
        { id: 'jc-admin', icon: '\uD83D\uDCCB', label: 'Project Administration', docCount: 5, color: COLORS.domain },
      ],
    },
    {
      id: 'rd',
      icon: '\uD83D\uDCC1',
      label: 'Rimrock Diversion Structure',
      color: COLORS.project,
      children: [
        { id: 'rd-lab', icon: '\uD83E\uDDEA', label: 'Lab Testing', docCount: 4, color: COLORS.domain },
        { id: 'rd-field', icon: '\uD83D\uDD0D', label: 'Field Exploration', docCount: 4, color: COLORS.domain },
        { id: 'rd-design', icon: '\uD83D\uDCD0', label: 'Design & Analysis', docCount: 4, color: COLORS.domain },
        { id: 'rd-admin', icon: '\uD83D\uDCCB', label: 'Project Administration', docCount: 4, color: COLORS.domain },
      ],
    },
  ],
};

// ════════════════════════════════════════════════════════════════
// DEMO QUERIES
// ════════════════════════════════════════════════════════════════
const QUERIES = [
  // ── Query 1: Single Agent, Single Project ──
  {
    label: 'What is the preconsolidation pressure at BH-2?',
    query: 'What is the preconsolidation pressure at BH-2?',
    routingText:
      'Analyzing query intent...\n  Project: Juniper Canyon Dam (confidence: 0.96)\n  Domains: Lab Testing (confidence: 0.93)\n  Routing to: JC \u2192 Lab Testing Agent',
    activatedAgents: ['jc-lab'],
    chunks: {
      'jc-lab': [
        {
          source: 'JC-LAB-004',
          score: 0.96,
          text: '1-D consolidation test on BH-2 at 22ft depth yielded compression index Cc = 0.38, recompression index Cr = 0.06, and preconsolidation pressure \u03C3\u2019p = 3.2 tsf. The in-situ effective vertical stress \u03C3\u2019v0 = 1.52 tsf gives an overconsolidation ratio OCR = 2.1, indicating a lightly overconsolidated deposit.',
        },
        {
          source: 'JC-LAB-004',
          score: 0.88,
          text: 'The e-log p curve for BH-2 at 22ft shows a well-defined break at the preconsolidation pressure. Casagrande construction was used to determine \u03C3\u2019p. Initial void ratio e0 = 0.82. End-of-primary consolidation was confirmed via Cv analysis using the Casagrande log-time method.',
        },
        {
          source: 'JC-LAB-002',
          score: 0.71,
          text: 'BH-2 samples at 20-24ft classified as CL (Lean Clay) with LL = 44, PL = 22, PI = 22. Natural moisture content w = 31%, near the liquid limit, consistent with soft to medium stiff consistency.',
        },
      ],
    },
    response: `Based on the 1-D consolidation testing performed on BH-2 at 22 ft depth (ASTM D2435), the preconsolidation pressure (\u03C3\u2019p) is **3.2 tsf**.

Key consolidation parameters from this test:
- Compression index (Cc): 0.38
- Recompression index (Cr): 0.06
- Initial void ratio (e\u2080): 0.82
- In-situ effective stress (\u03C3\u2019v0): 1.52 tsf
- Overconsolidation ratio (OCR): 2.1

The OCR of 2.1 indicates the foundation clay at this location is lightly overconsolidated. The \u03C3\u2019p was determined using Casagrande\u2019s graphical construction on a well-defined e-log p curve. The soil at this depth classifies as CL (Lean Clay) with PI = 22 and natural moisture content near the liquid limit.`,
  },

  // ── Query 2: Multi-Agent, Single Project ──
  {
    label: 'Summarize the subsurface conditions at Juniper Canyon',
    query: 'Summarize the subsurface conditions at Juniper Canyon',
    routingText:
      'Analyzing query intent...\n  Project: Juniper Canyon Dam (confidence: 0.98)\n  Domains: Field Exploration (confidence: 0.95), Lab Testing (confidence: 0.82)\n  Routing to: JC \u2192 Field Exploration Agent, JC \u2192 Lab Testing Agent',
    activatedAgents: ['jc-field', 'jc-lab'],
    chunks: {
      'jc-field': [
        {
          source: 'JC-FLD-001',
          score: 0.95,
          text: 'Subsurface conditions across the dam axis consist of 3-5 ft of alluvial overburden (loose silty sand with gravel) overlying 15-25 ft of soft to medium stiff lacustrine clay (CL to CH), underlain by dense glacial till and weathered bedrock encountered at 30-42 ft depth.',
        },
        {
          source: 'JC-FLD-002',
          score: 0.89,
          text: 'CPTu soundings C1-C4 show consistent pore pressure response in the clay zone between 5-25 ft, with qt values ranging from 8-15 tsf and Bq values of 0.4-0.6, confirming the fine-grained, normally to lightly overconsolidated nature of the deposit.',
        },
        {
          source: 'JC-FLD-004',
          score: 0.74,
          text: 'Seismic refraction profiles indicate competent bedrock (Vp > 4,500 m/s) at depths of 32-45 ft across the alignment, with a low-velocity weathered zone of 3-8 ft thickness above the rock surface.',
        },
      ],
      'jc-lab': [
        {
          source: 'JC-LAB-001',
          score: 0.91,
          text: 'Grain size analysis across BH-1 through BH-6 shows the lacustrine clay unit has 65-80% fines content (passing No. 200 sieve), with 30-45% clay-size particles (< 0.002 mm). The alluvial overburden contains 25-40% gravel, 35-50% sand, and 15-25% fines.',
        },
        {
          source: 'JC-LAB-002',
          score: 0.87,
          text: 'Atterberg limits testing shows the clay deposit ranges from CL to CH classification. BH-3 at 15ft yielded the highest plasticity (LL=62, PI=34, CH classification) while BH-1 at 10ft was the least plastic (LL=38, PI=16, CL classification).',
        },
      ],
    },
    response: `The subsurface conditions at the Juniper Canyon Dam site consist of a three-layer profile based on six borings (BH-1 through BH-6) and four CPTu soundings:

**Layer 1 \u2014 Alluvial Overburden (0 to 3-5 ft):** Loose silty sand with gravel. Contains 25-40% gravel and 35-50% sand with 15-25% fines. This is a relatively thin surficial deposit.

**Layer 2 \u2014 Lacustrine Clay (3-5 ft to 25-30 ft):** The dominant foundation unit. Classifies as CL to CH (Lean to Fat Clay) with liquid limits ranging from 38-62 and plasticity indices from 16-34. Fines content is 65-80% with 30-45% clay-size particles. CPTu data confirms soft to medium stiff consistency with Bq values of 0.4-0.6 indicating significant excess pore pressure generation.

**Layer 3 \u2014 Glacial Till / Bedrock (30-42+ ft):** Dense glacial till overlying weathered bedrock. Seismic refraction indicates competent rock (Vp > 4,500 m/s) at 32-45 ft with a 3-8 ft weathered transition zone.

The lacustrine clay layer is the critical design unit \u2014 its compressibility (Cc = 0.38), moderate overconsolidation (OCR \u2248 2), and thickness will control foundation settlement and stability for the dam.`,
  },

  // ── Query 3: Cross-Project Comparison ──
  {
    label: 'Compare foundation conditions between Juniper Canyon and Rimrock',
    query: 'Compare foundation soil conditions between Juniper Canyon and Rimrock',
    routingText:
      'Analyzing query intent...\n  Project: Juniper Canyon Dam (confidence: 0.92), Rimrock Diversion (confidence: 0.90)\n  Domains: Lab Testing (confidence: 0.88), Field Exploration (confidence: 0.85)\n  Routing to: JC \u2192 Lab, JC \u2192 Field, RD \u2192 Lab, RD \u2192 Field\n  [4 sub-agents activated]',
    activatedAgents: ['jc-lab', 'jc-field', 'rd-lab', 'rd-field'],
    chunks: {
      'jc-lab': [
        {
          source: 'JC-LAB-002',
          score: 0.90,
          text: 'Atterberg limits testing shows the clay deposit ranges from CL to CH classification. BH-3 at 15ft yielded the highest plasticity (LL=62, PI=34, CH classification) while BH-1 at 10ft was the least plastic (LL=38, PI=16, CL classification).',
        },
        {
          source: 'JC-LAB-004',
          score: 0.84,
          text: '1-D consolidation test on BH-2 at 22ft depth yielded compression index Cc = 0.38, recompression index Cr = 0.06, and preconsolidation pressure \u03C3\u2019p = 3.2 tsf.',
        },
      ],
      'jc-field': [
        {
          source: 'JC-FLD-001',
          score: 0.92,
          text: 'Subsurface conditions across the dam axis consist of 3-5 ft of alluvial overburden overlying 15-25 ft of soft to medium stiff lacustrine clay (CL to CH), underlain by dense glacial till and weathered bedrock at 30-42 ft depth.',
        },
      ],
      'rd-lab': [
        {
          source: 'RD-LAB-002',
          score: 0.91,
          text: 'Foundation soils at the Rimrock Diversion site classify predominantly as GW-GM (Well-Graded Gravel with Silt) to GP-GM (Poorly-Graded Gravel with Silt). Atterberg limits on the fines fraction yield LL = 28, PL = 21, PI = 7 (non-plastic to low plasticity).',
        },
        {
          source: 'RD-LAB-003',
          score: 0.85,
          text: "Direct shear testing on BH-R2 at 8ft yielded peak friction angle \u03C6\u2019 = 36\u00B0 with c\u2019 = 0.1 tsf. BH-R3 at 12ft yielded \u03C6\u2019 = 34\u00B0 with c\u2019 = 0.15 tsf. Residual friction angles were 31\u00B0 and 29\u00B0 respectively.",
        },
      ],
      'rd-field': [
        {
          source: 'RD-FLD-001',
          score: 0.93,
          text: 'Subsurface conditions at the Rimrock Diversion site consist of 2-4 ft of topsoil and organic silt overlying 8-15 ft of alluvial gravel (dense to very dense, GW-GM), underlain by moderately weathered basalt bedrock at 10-18 ft depth.',
        },
        {
          source: 'RD-FLD-002',
          score: 0.79,
          text: 'Test pits TP-R1 through TP-R6 confirmed the alluvial gravel deposit is laterally continuous across the diversion alignment. Cobbles and boulders (6-18 inch) comprise approximately 15-20% of the deposit. Groundwater was not encountered in any test pit to maximum depth of 12 ft.',
        },
      ],
    },
    response: `The two project sites have fundamentally different foundation conditions:

**Juniper Canyon Dam** is founded on a thick (15-25 ft) lacustrine clay deposit classified CL to CH, with high plasticity (PI up to 34), significant compressibility (Cc = 0.38), and soft to medium stiff consistency. This clay unit is the controlling design layer \u2014 it governs settlement, stability, and seepage behavior. Bedrock lies 30-42 ft below ground surface.

**Rimrock Diversion Structure** is founded on dense to very dense alluvial gravels (GW-GM to GP-GM) that are essentially non-plastic (PI = 7 on fines fraction). The deposit is 8-15 ft thick with high shear strength (\u03C6\u2019 = 34-36\u00B0) and shallow bedrock at 10-18 ft. No groundwater issues were encountered.

The key engineering implications of this contrast:
- **Settlement**: Juniper Canyon requires detailed consolidation analysis; Rimrock settlement will be negligible
- **Stability**: Juniper Canyon\u2019s clay controls slope stability with undrained strength governing; Rimrock\u2019s granular foundation provides high frictional resistance
- **Seepage**: The clay at Juniper Canyon creates a low-permeability foundation (benefit for dam, but high pore pressure response); Rimrock\u2019s gravels are highly permeable, requiring engineered seepage control for the diversion
- **Construction**: Juniper Canyon clay is moisture-sensitive and difficult to excavate/compact; Rimrock gravels are excellent structural fill but cobbles/boulders complicate excavation`,
  },

  // ── Query 4: Single Domain, Both Projects ──
  {
    label: 'What are the design seismic parameters for both sites?',
    query: 'What are the design seismic parameters for both sites?',
    routingText:
      'Analyzing query intent...\n  Project: Juniper Canyon Dam (confidence: 0.88), Rimrock Diversion (confidence: 0.86)\n  Domains: Design & Analysis (confidence: 0.96)\n  Routing to: JC \u2192 Design Agent, RD \u2192 Design Agent',
    activatedAgents: ['jc-design', 'rd-design'],
    chunks: {
      'jc-design': [
        {
          source: 'JC-DES-003',
          score: 0.97,
          text: 'Probabilistic seismic hazard analysis (PSHA) for the Juniper Canyon Dam site yields PGA = 0.28g for the 2,475-year return period (MCE). Site-specific spectral acceleration values: Ss = 0.72g, S1 = 0.31g. Site Class D (stiff soil) per ASCE 7-22 based on Vs30 = 220 m/s from geophysical survey.',
        },
        {
          source: 'JC-DES-003',
          score: 0.91,
          text: 'Liquefaction triggering analysis using the Boulanger & Idriss (2014) procedure indicates the loose alluvial overburden (0-5 ft) has factors of safety against liquefaction of 0.7-0.9 under MCE loading. The underlying lacustrine clay is not susceptible to liquefaction but may experience cyclic softening.',
        },
      ],
      'rd-design': [
        {
          source: 'RD-DES-004',
          score: 0.95,
          text: 'Seismic design parameters for the Rimrock Diversion site: PGA = 0.22g (2,475-yr return period). Ss = 0.58g, S1 = 0.24g. Site Class C (very dense soil/soft rock) per ASCE 7-22 based on Vs30 = 410 m/s estimated from SPT correlations in the dense gravel.',
        },
        {
          source: 'RD-DES-004',
          score: 0.88,
          text: 'Liquefaction assessment concludes the dense alluvial gravel foundation (N1,60 > 30 across all borings) is not susceptible to liquefaction. The thin organic silt cap (2-4 ft) has insufficient thickness to pose a liquefaction hazard. Overall site liquefaction potential is negligible.',
        },
      ],
    },
    response: `Seismic design parameters for both sites (2,475-year return period / MCE level):

| Parameter | Juniper Canyon | Rimrock Diversion |
|-----------|---------------|-------------------|
| PGA | 0.28g | 0.22g |
| Ss | 0.72g | 0.58g |
| S1 | 0.31g | 0.24g |
| Site Class | D (Stiff Soil) | C (Dense Soil/Soft Rock) |
| Vs30 | 220 m/s | 410 m/s |

Juniper Canyon faces higher seismic demand due to both higher ground motions and softer site conditions (Class D vs C). The loose alluvial overburden at Juniper Canyon has liquefaction factors of safety below 1.0 under MCE loading, and the clay foundation may experience cyclic softening \u2014 both requiring mitigation in the dam design.

Rimrock has no liquefaction susceptibility \u2014 the dense gravel foundation (N1,60 > 30) and thin surficial soils pose negligible risk. The lower seismic demand and better foundation conditions simplify the seismic design for the diversion structure.`,
  },

  // ── Query 5: Non-Technical Routing (Admin) ──
  {
    label: 'What is the QA/QC plan for laboratory testing at Juniper Canyon?',
    query: 'What is the QA/QC plan for laboratory testing at Juniper Canyon?',
    routingText:
      'Analyzing query intent...\n  Project: Juniper Canyon Dam (confidence: 0.94)\n  Domains: Project Administration (confidence: 0.89), Lab Testing (confidence: 0.52)\n  Routing to: JC \u2192 Project Admin Agent\n  [Lab Testing below threshold \u2014 not activated]',
    activatedAgents: ['jc-admin'],
    chunks: {
      'jc-admin': [
        {
          source: 'JC-ADM-004',
          score: 0.95,
          text: 'The QA/QC plan for laboratory testing follows ISO/IEC 17025 accreditation requirements. All soil classification and index property tests require duplicate testing at a frequency of 1 per 10 samples. Strength and consolidation tests require calibration verification before each test series.',
        },
        {
          source: 'JC-ADM-004',
          score: 0.90,
          text: 'Proficiency testing participation is required annually for AASHTO re:source programs covering: grain size analysis (ASTM D6913), Atterberg limits (ASTM D4318), and standard Proctor (ASTM D698). Any test result exceeding 2-sigma from the program mean requires root cause investigation.',
        },
        {
          source: 'JC-ADM-004',
          score: 0.78,
          text: 'Data validation follows a three-tier review process: (1) technician self-check against standard acceptance criteria, (2) senior technician review for completeness and outliers, (3) Professional Engineer review and approval with digital signature before results enter the LIMS database.',
        },
      ],
    },
    response: `The Juniper Canyon QA/QC plan for laboratory testing (documented in JC-ADM-004) follows ISO/IEC 17025 accreditation requirements with three key components:

**Testing Frequency**: Duplicate testing at 1:10 ratio for index property tests. Strength and consolidation equipment requires calibration verification before each test series.

**Proficiency Testing**: Annual participation in AASHTO re:source programs for grain size (D6913), Atterberg limits (D4318), and standard Proctor (D698). Results exceeding 2-sigma from the program mean trigger root cause investigation.

**Data Validation**: Three-tier review \u2014 technician self-check, senior technician review for completeness/outliers, and PE review with digital signature before LIMS entry.

This is consistent with standard practice for dam safety investigations where data quality has regulatory implications.`,
  },

  // \u2500\u2500 Query 6: Rimrock-only, Design + Admin \u2500\u2500
  {
    label: 'What is the slope stability design basis for Rimrock Diversion?',
    query: 'What is the slope stability design basis for Rimrock Diversion?',
    routingText:
      'Analyzing query intent...\n  Project: Rimrock Diversion (confidence: 0.97)\n  Domains: Design & Analysis (confidence: 0.94), Project Administration (confidence: 0.61)\n  Routing to: RD \u2192 Design Agent, RD \u2192 Admin Agent',
    activatedAgents: ['rd-design', 'rd-admin'],
    chunks: {
      'rd-design': [
        {
          source: 'RD-DES-002',
          score: 0.95,
          text: 'Slope stability analyses for the Rimrock Diversion embankment were performed using Spencer\u2019s method with circular and non-circular failure surfaces. The minimum factor of safety under static conditions is 1.52 for the downstream slope and 1.48 for the upstream slope, both exceeding the FEMA P-94 requirement of 1.5.',
        },
        {
          source: 'RD-DES-002',
          score: 0.88,
          text: 'Pseudo-static seismic analysis using a horizontal coefficient kh = 0.11 (= 0.5 \u00D7 PGA) yields minimum factors of safety of 1.12 (downstream) and 1.08 (upstream), exceeding the FEMA minimum of 1.0 for the pseudo-static case.',
        },
        {
          source: 'RD-DES-003',
          score: 0.76,
          text: 'Shear strength parameters used for the alluvial gravel foundation: drained friction angle \u03C6\u2019 = 34\u00B0, cohesion c\u2019 = 0 tsf (conservative lower-bound from direct shear testing). The embankment fill was modeled with \u03C6\u2019 = 32\u00B0 and c\u2019 = 0.05 tsf based on compacted fill specifications.',
        },
      ],
      'rd-admin': [
        {
          source: 'RD-ADM-001',
          score: 0.72,
          text: 'The design basis document specifies that all stability analyses shall comply with FEMA P-94 Federal Guidelines for Dam Safety, with independent peer review by a Board of Consultants before final design approval.',
        },
        {
          source: 'RD-ADM-003',
          score: 0.65,
          text: 'Risk classification for Rimrock Diversion Structure is Significant Hazard (Class II) per state dam safety regulations, requiring stability factors of safety per FEMA guidelines and annual inspection by a licensed Professional Engineer.',
        },
      ],
    },
    response: `The slope stability design basis for the Rimrock Diversion Structure follows FEMA P-94 Federal Guidelines for Dam Safety, consistent with its Significant Hazard (Class II) risk classification:

**Static Stability** (Spencer\u2019s method, circular + non-circular surfaces):
- Downstream slope FS = 1.52 (required \u2265 1.5)
- Upstream slope FS = 1.48 (marginal \u2014 meets minimum)

**Pseudo-Static Seismic** (kh = 0.11, equal to 0.5 \u00D7 PGA):
- Downstream slope FS = 1.12 (required \u2265 1.0)
- Upstream slope FS = 1.08 (required \u2265 1.0)

**Material Parameters**:
- Foundation (alluvial gravel): \u03C6\u2019 = 34\u00B0, c\u2019 = 0 tsf (lower-bound from direct shear)
- Compacted fill: \u03C6\u2019 = 32\u00B0, c\u2019 = 0.05 tsf (specification-based)

The upstream static factor of safety of 1.48 is at the regulatory threshold. The design requires independent peer review by a Board of Consultants before final approval, and annual PE inspection is mandated under the state dam safety program.`,
  },

  // \u2500\u2500 Query 7: Single Project, Field + Design \u2500\u2500
  {
    label: 'What are the groundwater conditions affecting the Juniper Canyon Dam design?',
    query: 'What are the groundwater conditions affecting the Juniper Canyon Dam design?',
    routingText:
      'Analyzing query intent...\n  Project: Juniper Canyon Dam (confidence: 0.95)\n  Domains: Field Exploration (confidence: 0.92), Design & Analysis (confidence: 0.78)\n  Routing to: JC \u2192 Field Exploration Agent, JC \u2192 Design Agent',
    activatedAgents: ['jc-field', 'jc-design'],
    chunks: {
      'jc-field': [
        {
          source: 'JC-FLD-003',
          score: 0.94,
          text: 'Piezometer installations in BH-3 and BH-5 indicate a groundwater table at approximately 8-12 ft below ground surface across the dam footprint, within the upper portion of the lacustrine clay unit. Seasonal fluctuations of 3-4 ft were observed between wet and dry seasons.',
        },
        {
          source: 'JC-FLD-002',
          score: 0.86,
          text: 'CPTu pore pressure dissipation tests at 15 ft and 20 ft depths in C-2 yielded equilibrium pore pressures consistent with a hydrostatic groundwater table at 10 ft depth. The measured Bq values of 0.4-0.6 indicate significant excess pore pressure generation during cone penetration in the clay.',
        },
        {
          source: 'JC-FLD-005',
          score: 0.71,
          text: 'Falling-head permeability tests on Shelby tube samples from BH-2 and BH-4 yield hydraulic conductivity values of 2\u00D710\u207B\u2078 to 8\u00D710\u207B\u2078 cm/s for the lacustrine clay, classifying it as practically impervious per Terzaghi\u2019s criteria.',
        },
      ],
      'jc-design': [
        {
          source: 'JC-DES-001',
          score: 0.89,
          text: 'Seepage analysis using SEEP/W indicates steady-state phreatic surface will intersect the downstream slope at approximately elevation 4,285 ft without internal drainage provisions. A chimney drain and horizontal blanket drain are specified to maintain the phreatic surface below the downstream slope face.',
        },
        {
          source: 'JC-DES-001',
          score: 0.79,
          text: 'Pore pressure ratio r\u1D64 = 0.35 was adopted for the effective stress stability analyses based on the measured groundwater levels and anticipated reservoir loading. This corresponds to a phreatic surface approximately at mid-height of the embankment under steady-state seepage.',
        },
      ],
    },
    response: `Groundwater conditions at the Juniper Canyon Dam site play a critical role in the design:

**Field Observations**:
- Groundwater table at **8-12 ft depth** across the dam footprint, within the lacustrine clay
- Seasonal fluctuation of 3-4 ft between wet and dry seasons
- CPTu dissipation tests confirm hydrostatic conditions at \u223C10 ft depth
- Clay hydraulic conductivity: 2\u00D710\u207B\u2078 to 8\u00D710\u207B\u2078 cm/s (practically impervious)

**Design Implications**:
- Without drainage, the steady-state phreatic surface would **daylight on the downstream slope** at elevation 4,285 ft \u2014 an unacceptable condition
- A **chimney drain and horizontal blanket drain** are specified to control the phreatic surface
- Effective stress stability analyses use pore pressure ratio r\u1D64 = 0.35, corresponding to a mid-height phreatic surface under steady-state seepage

The combination of high groundwater, low-permeability clay foundation, and reservoir loading makes internal drainage provisions essential. The clay\u2019s low hydraulic conductivity means pore pressures will dissipate slowly during construction and initial reservoir filling \u2014 a staged construction and monitoring program should be considered.`,
  },
];

// ════════════════════════════════════════════════════════════════
// UTILITIES
// ════════════════════════════════════════════════════════════════
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function getProjectId(agentId) {
  if (agentId.startsWith('jc')) return 'jc';
  if (agentId.startsWith('rd')) return 'rd';
  return null;
}

// ════════════════════════════════════════════════════════════════
// MARKDOWN RENDERER
// ════════════════════════════════════════════════════════════════
function renderMath(latex, displayMode) {
  try {
    const html = katex.renderToString(latex, {
      displayMode,
      throwOnError: false,
      trust: false,
    });
    return (
      <span
        dangerouslySetInnerHTML={{ __html: html }}
        style={displayMode ? { display: 'block', margin: '8px 0', overflowX: 'auto' } : undefined}
      />
    );
  } catch {
    return <code>{latex}</code>;
  }
}

function renderInline(text) {
  if (!text) return null;
  // Split on: display math $$...$$, inline math $...$, bold **...**, inline code `...`, citation [N]
  const TOKEN_RE = /(\$\$[\s\S]+?\$\$|\$(?!\s)(?:[^$\\]|\\.)+?\$|\*\*.*?\*\*|`[^`]+`|\[\d+[a-z]?\])/g;
  const parts = text.split(TOKEN_RE);
  return parts.map((part, i) => {
    if (!part) return null;
    // Display math
    if (part.startsWith('$$') && part.endsWith('$$')) {
      return <React.Fragment key={i}>{renderMath(part.slice(2, -2).trim(), true)}</React.Fragment>;
    }
    // Inline math
    if (part.startsWith('$') && part.endsWith('$') && part.length > 2) {
      return <React.Fragment key={i}>{renderMath(part.slice(1, -1), false)}</React.Fragment>;
    }
    // Bold
    if (part.startsWith('**') && part.endsWith('**')) {
      return (
        <strong key={i} style={{ color: COLORS.textPrimary, fontWeight: 600 }}>
          {part.slice(2, -2)}
        </strong>
      );
    }
    // Inline code
    if (part.startsWith('`') && part.endsWith('`')) {
      return (
        <code
          key={i}
          style={{
            background: '#1e293b',
            color: '#e8a838',
            padding: '1px 5px',
            borderRadius: '3px',
            fontSize: '0.82em',
            fontFamily: 'monospace',
          }}
        >
          {part.slice(1, -1)}
        </code>
      );
    }
    // Citation reference [N]
    if (/^\[\d+[a-z]?\]$/.test(part)) {
      return (
        <span
          key={i}
          style={{
            color: COLORS.accent,
            fontSize: '0.75em',
            fontWeight: 600,
            verticalAlign: 'super',
            cursor: 'default',
          }}
        >
          {part}
        </span>
      );
    }
    return <span key={i}>{part}</span>;
  });
}

function TableBlock({ text }) {
  const rows = text
    .split('\n')
    .filter((r) => r.trim().startsWith('|'));
  const parsed = rows.map((row) =>
    row
      .split('|')
      .slice(1, -1)
      .map((cell) => cell.trim())
  );
  const isSeparator = (row) => row.every((cell) => /^[-:]+$/.test(cell));
  const header = parsed[0];
  const dataRows = parsed.slice(1).filter((row) => !isSeparator(row));

  return (
    <div className="overflow-x-auto" style={{ margin: '8px 0' }}>
      <table
        style={{
          width: '100%',
          borderCollapse: 'collapse',
          fontSize: '0.8rem',
        }}
      >
        <thead>
          <tr>
            {header.map((h, i) => (
              <th
                key={i}
                style={{
                  textAlign: 'left',
                  padding: '6px 10px',
                  borderBottom: `2px solid ${COLORS.cardBorder}`,
                  color: COLORS.textPrimary,
                  fontWeight: 600,
                  whiteSpace: 'nowrap',
                }}
              >
                {renderInline(h)}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {dataRows.map((row, ri) => (
            <tr key={ri}>
              {row.map((cell, ci) => (
                <td
                  key={ci}
                  style={{
                    padding: '5px 10px',
                    borderBottom: `1px solid ${COLORS.cardBorder}`,
                    color: COLORS.textSecondary,
                    whiteSpace: 'nowrap',
                  }}
                >
                  {renderInline(cell)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function MarkdownRenderer({ text }) {
  if (!text) return null;
  const blocks = text.split('\n\n');

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
      {blocks.map((block, bi) => {
        const trimmed = block.trim();
        if (!trimmed) return null;

        // Horizontal rule
        if (/^-{3,}$/.test(trimmed)) {
          return (
            <hr
              key={bi}
              style={{
                border: 'none',
                borderTop: `1px solid ${COLORS.cardBorder}`,
                margin: '4px 0',
                width: '100%',
              }}
            />
          );
        }

        // Display math block ($$...$$)
        if (trimmed.startsWith('$$') && trimmed.endsWith('$$')) {
          return (
            <div key={bi} style={{ margin: '6px 0', overflowX: 'auto' }}>
              {renderMath(trimmed.slice(2, -2).trim(), true)}
            </div>
          );
        }

        // Heading
        const headingMatch = trimmed.match(/^(#{1,4})\s+(.*)/);
        if (headingMatch) {
          const level = headingMatch[1].length;
          const sizes = { 1: '1.3rem', 2: '1.1rem', 3: '0.95rem', 4: '0.88rem' };
          return (
            <div
              key={bi}
              style={{
                fontSize: sizes[level] || '0.88rem',
                fontWeight: 700,
                color: COLORS.textPrimary,
                marginTop: level <= 2 ? '8px' : '4px',
                paddingBottom: level <= 2 ? '4px' : 0,
                borderBottom: level <= 2 ? `1px solid ${COLORS.cardBorder}` : 'none',
                lineHeight: 1.4,
              }}
            >
              {renderInline(headingMatch[2])}
            </div>
          );
        }

        // Table block
        if (trimmed.includes('|') && trimmed.split('\n').filter((l) => l.trim().startsWith('|')).length >= 2) {
          const tableLines = trimmed
            .split('\n')
            .filter((l) => l.trim().startsWith('|'))
            .join('\n');
          const nonTableLines = trimmed
            .split('\n')
            .filter((l) => !l.trim().startsWith('|'));
          return (
            <div key={bi}>
              {nonTableLines.length > 0 && nonTableLines.some((l) => l.trim()) && (
                <p style={{ color: COLORS.textSecondary, lineHeight: 1.6 }}>
                  {nonTableLines.map((l, li) => (
                    <React.Fragment key={li}>
                      {renderInline(l)}
                      {li < nonTableLines.length - 1 && <br />}
                    </React.Fragment>
                  ))}
                </p>
              )}
              <TableBlock text={tableLines} />
            </div>
          );
        }

        // Bullet list (lines starting with - or with checkbox ✅/⚠️ prefix)
        const lines = trimmed.split('\n');
        if (lines.every((l) => /^\s*- /.test(l))) {
          return (
            <ul
              key={bi}
              style={{
                margin: 0,
                paddingLeft: '20px',
                display: 'flex',
                flexDirection: 'column',
                gap: '4px',
              }}
            >
              {lines.map((l, li) => (
                <li
                  key={li}
                  style={{ color: COLORS.textSecondary, lineHeight: 1.5, fontSize: '0.85rem' }}
                >
                  {renderInline(l.replace(/^\s*- /, ''))}
                </li>
              ))}
            </ul>
          );
        }

        // Numbered list
        if (lines.every((l) => /^\s*\d+\.\s+/.test(l))) {
          return (
            <ol
              key={bi}
              style={{
                margin: 0,
                paddingLeft: '20px',
                display: 'flex',
                flexDirection: 'column',
                gap: '4px',
              }}
            >
              {lines.map((l, li) => (
                <li
                  key={li}
                  style={{ color: COLORS.textSecondary, lineHeight: 1.5, fontSize: '0.85rem' }}
                >
                  {renderInline(l.replace(/^\s*\d+\.\s+/, ''))}
                </li>
              ))}
            </ol>
          );
        }

        // Mixed content: heading-like lines + regular lines, or numbered + bullet mixed
        // Handle blocks with a mix of list items and non-list content
        const hasListItems = lines.some((l) => /^\s*[-\d]/.test(l) && /^\s*(-\s|\d+\.\s)/.test(l));
        const hasNonListItems = lines.some((l) => !/^\s*(-\s|\d+\.\s)/.test(l) && l.trim());
        if (hasListItems && hasNonListItems) {
          return (
            <div key={bi} style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
              {lines.map((l, li) => {
                if (/^\s*-\s/.test(l)) {
                  return (
                    <div key={li} style={{ color: COLORS.textSecondary, lineHeight: 1.5, fontSize: '0.85rem', paddingLeft: '16px' }}>
                      {'• '}{renderInline(l.replace(/^\s*- /, ''))}
                    </div>
                  );
                }
                if (/^\s*\d+\.\s/.test(l)) {
                  const num = l.match(/^\s*(\d+)\./)[1];
                  return (
                    <div key={li} style={{ color: COLORS.textSecondary, lineHeight: 1.5, fontSize: '0.85rem', paddingLeft: '16px' }}>
                      {num}. {renderInline(l.replace(/^\s*\d+\.\s+/, ''))}
                    </div>
                  );
                }
                return (
                  <div key={li} style={{ color: COLORS.textSecondary, lineHeight: 1.6, fontSize: '0.85rem' }}>
                    {renderInline(l)}
                  </div>
                );
              })}
            </div>
          );
        }

        // Regular paragraph
        return (
          <p key={bi} style={{ margin: 0, color: COLORS.textSecondary, lineHeight: 1.6, fontSize: '0.85rem' }}>
            {lines.map((l, li) => (
              <React.Fragment key={li}>
                {renderInline(l)}
                {li < lines.length - 1 && <br />}
              </React.Fragment>
            ))}
          </p>
        );
      })}
    </div>
  );
}

// ════════════════════════════════════════════════════════════════
// CSS KEYFRAMES (injected via style tag)
// ════════════════════════════════════════════════════════════════
const KEYFRAMES = `
@keyframes glow-pulse {
  0%, 100% { box-shadow: 0 0 6px var(--glow-color, #00d4aa); opacity: 1; }
  50% { box-shadow: 0 0 20px var(--glow-color, #00d4aa); opacity: 0.85; }
}
@keyframes fade-slide-in {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes cursor-blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}
@keyframes dot-pulse {
  0%, 80%, 100% { opacity: 0.3; }
  40% { opacity: 1; }
}
`;

// ════════════════════════════════════════════════════════════════
// CHUNK CARD COMPONENT
// ════════════════════════════════════════════════════════════════
function ChunkCard({ chunk, domainColor, isBest }) {
  const [expanded, setExpanded] = useState(false);
  const preview = chunk.text.length > 80 ? chunk.text.slice(0, 80) + '...' : chunk.text;
  const srcColor = COLORS.chunkSource;

  return (
    <div
      onClick={() => setExpanded(!expanded)}
      style={{
        background: COLORS.cardBg,
        borderLeft: `3px solid ${domainColor}`,
        borderRadius: '4px',
        padding: '6px 8px',
        marginTop: '4px',
        cursor: 'pointer',
        animation: 'fade-slide-in 0.3s ease forwards',
        fontSize: '0.72rem',
        lineHeight: 1.4,
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
        {isBest && (
          <span style={{ color: COLORS.scoreGreen, fontSize: '0.7rem', flexShrink: 0 }}>
            {'\u2713'}
          </span>
        )}
        <span
          style={{
            background: srcColor + '25',
            color: srcColor,
            padding: '1px 5px',
            borderRadius: '3px',
            fontWeight: 600,
            fontSize: '0.65rem',
            whiteSpace: 'nowrap',
          }}
        >
          {chunk.source}
        </span>
        <span
          style={{
            background: scoreColor(chunk.score) + '20',
            color: scoreColor(chunk.score),
            padding: '1px 5px',
            borderRadius: '3px',
            fontWeight: 600,
            fontSize: '0.65rem',
          }}
        >
          {chunk.score.toFixed(2)}
        </span>
        <span style={{ color: COLORS.textDim, flex: 1, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
          {expanded ? '' : `\u2014 "${preview}"`}
        </span>
      </div>
      {expanded && (
        <p style={{ color: COLORS.textSecondary, margin: '6px 0 2px', fontSize: '0.72rem', lineHeight: 1.5 }}>
          &ldquo;{chunk.text}&rdquo;
        </p>
      )}
    </div>
  );
}

// ════════════════════════════════════════════════════════════════
// AGENT NODE COMPONENT (recursive)
// ════════════════════════════════════════════════════════════════
function AgentNode({ node, depth, nodeStates, activeChunks, routingText }) {
  const state = nodeStates[node.id] || 'idle';
  const isActive = state !== 'idle';
  const color = node.color || COLORS.router;

  const isPulsing = state === 'routing' || state === 'synthesizing';
  const isSearching = state === 'activated';
  const isRetrieving = state === 'retrieving';
  const isComplete = state === 'complete';
  const chunks = activeChunks[node.id] || [];

  const hasChildren = node.children && node.children.length > 0;

  // Auto-collapse: nodes with children collapse when actively routing
  // (activated, retrieving, or routing/synthesizing). Expand when idle or complete.
  const autoCollapsed = hasChildren && isActive && !isComplete;
  const [manualToggle, setManualToggle] = useState(null); // null = follow auto
  const collapsed = manualToggle !== null ? manualToggle : autoCollapsed;

  // Reset manual toggle when activity state changes significantly
  useEffect(() => {
    setManualToggle(null);
  }, [isActive, isComplete]);

  // Status indicator
  let statusEl = null;
  if (isPulsing) {
    statusEl = (
      <span style={{ display: 'flex', gap: '3px', marginLeft: '6px' }}>
        {[0, 1, 2].map((i) => (
          <span
            key={i}
            style={{
              width: 4,
              height: 4,
              borderRadius: '50%',
              background: color,
              animation: `dot-pulse 1.2s ${i * 0.15}s ease-in-out infinite`,
            }}
          />
        ))}
      </span>
    );
  } else if (isSearching) {
    statusEl = (
      <span style={{ color: color, fontSize: '0.65rem', marginLeft: '6px', opacity: 0.9 }}>
        Searching {node.docCount || '...'} docs...
      </span>
    );
  }

  return (
    <div
      style={{
        marginLeft: depth > 0 ? 16 : 0,
        borderLeft: depth > 0 ? `2px solid ${isActive ? color + '60' : COLORS.cardBorder + '40'}` : 'none',
        paddingLeft: depth > 0 ? 12 : 0,
        transition: 'border-color 0.4s ease',
      }}
    >
      {/* Node header */}
      <div
        onClick={hasChildren ? () => setManualToggle((prev) => prev !== null ? !prev : !autoCollapsed) : undefined}
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '6px',
          padding: '5px 8px',
          borderRadius: '6px',
          background: isActive ? color + '0c' : 'transparent',
          border: isActive ? `1px solid ${color}20` : '1px solid transparent',
          transition: 'all 0.3s ease',
          cursor: hasChildren ? 'pointer' : 'default',
          userSelect: 'none',
          ...(isPulsing
            ? {
                '--glow-color': color,
                animation: 'glow-pulse 1.5s ease-in-out infinite',
              }
            : {}),
        }}
      >
        {/* Collapse chevron for nodes with children */}
        {hasChildren ? (
          <span
            style={{
              fontSize: '0.6rem',
              color: isActive ? color : COLORS.textDim + '80',
              transition: 'transform 0.2s ease, color 0.3s ease',
              transform: collapsed ? 'rotate(0deg)' : 'rotate(90deg)',
              flexShrink: 0,
              width: 10,
              textAlign: 'center',
            }}
          >
            &#9654;
          </span>
        ) : (
          /* Agent indicator dot for leaf nodes */
          <span
            style={{
              width: depth === 0 ? 10 : 8,
              height: depth === 0 ? 10 : 8,
              borderRadius: '50%',
              border: `1.5px solid ${isActive ? color : COLORS.textDim + '80'}`,
              background: isActive ? color + '30' : 'transparent',
              flexShrink: 0,
              transition: 'all 0.3s ease',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            <span
              style={{
                width: depth === 0 ? 4 : 3,
                height: depth === 0 ? 4 : 3,
                borderRadius: '50%',
                background: isActive ? color : COLORS.textDim + '60',
                transition: 'background 0.3s ease',
              }}
            />
          </span>
        )}
        <span style={{ fontSize: depth === 0 ? '1rem' : '0.8rem', flexShrink: 0 }}>{node.icon}</span>
        <span
          style={{
            fontSize: depth === 0 ? '0.85rem' : '0.78rem',
            fontWeight: depth <= 1 ? 600 : 500,
            color: isActive ? color : COLORS.textDim,
            transition: 'color 0.3s ease',
            whiteSpace: 'nowrap',
            overflow: 'hidden',
            textOverflow: 'ellipsis',
          }}
        >
          {node.label}
        </span>
        {node.docCount != null && !isSearching && (
          <span style={{ color: COLORS.textDim, fontSize: '0.65rem', opacity: 0.7 }}>
            ({node.docCount})
          </span>
        )}
        {/* Show child count badge when collapsed */}
        {hasChildren && collapsed && (
          <span style={{
            color: isActive ? color : COLORS.textDim,
            fontSize: '0.6rem',
            opacity: 0.7,
            marginLeft: '2px',
          }}>
            [{node.children.length}]
          </span>
        )}
        {statusEl}
      </div>

      {/* Routing decision text (router node only) */}
      {node.id === 'router' && routingText && (
        <div
          style={{
            background: '#0f172a',
            border: `1px solid ${COLORS.cardBorder}`,
            borderRadius: '4px',
            padding: '8px 10px',
            margin: '4px 0 4px 8px',
            fontFamily: 'monospace',
            fontSize: '0.68rem',
            lineHeight: 1.6,
            color: COLORS.textSecondary,
            whiteSpace: 'pre-wrap',
            animation: 'fade-slide-in 0.3s ease forwards',
          }}
        >
          {routingText}
        </div>
      )}

      {/* Retrieved chunks */}
      {chunks.length > 0 && (() => {
        const bestScore = Math.max(...chunks.map((c) => c.score));
        return (
          <div style={{ margin: '2px 0 4px 8px' }}>
            {chunks.map((chunk, i) => (
              <ChunkCard key={i} chunk={chunk} domainColor={color} isBest={chunk.score === bestScore} />
            ))}
          </div>
        );
      })()}

      {/* Children — collapsible */}
      {hasChildren && !collapsed && (
        <div style={{ marginTop: '2px', animation: 'fade-slide-in 0.2s ease forwards' }}>
          {node.children.map((child) => (
            <AgentNode
              key={child.id}
              node={child}
              depth={depth + 1}
              nodeStates={nodeStates}
              activeChunks={activeChunks}
              routingText={routingText}
            />
          ))}
        </div>
      )}
    </div>
  );
}

// ════════════════════════════════════════════════════════════════
// CHAT MESSAGE COMPONENT
// ════════════════════════════════════════════════════════════════
function ChatMessage({ message }) {
  const isUser = message.role === 'user';

  return (
    <div
      style={{
        display: 'flex',
        gap: '10px',
        padding: '12px 16px',
        animation: 'fade-slide-in 0.3s ease forwards',
      }}
    >
      {/* Avatar */}
      <div
        style={{
          width: 28,
          height: 28,
          borderRadius: '50%',
          background: isUser ? '#1e3a5f' : COLORS.router + '20',
          border: `1.5px solid ${isUser ? '#4a9eff' : COLORS.router}`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '0.75rem',
          flexShrink: 0,
          marginTop: '2px',
        }}
      >
        {isUser ? '\uD83D\uDC64' : '\uD83E\uDD16'}
      </div>

      {/* Content */}
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ fontSize: '0.7rem', color: COLORS.textDim, marginBottom: '4px', fontWeight: 600 }}>
          {isUser ? 'You' : 'Agent'}
        </div>
        {isUser ? (
          <p style={{ margin: 0, color: COLORS.textPrimary, fontSize: '0.85rem', lineHeight: 1.5 }}>
            {message.content}
          </p>
        ) : (
          <div>
            <MarkdownRenderer text={message.content} />
            {message.isStreaming && (
              <span
                style={{
                  display: 'inline-block',
                  width: '2px',
                  height: '14px',
                  background: COLORS.router,
                  marginLeft: '2px',
                  verticalAlign: 'text-bottom',
                  animation: 'cursor-blink 0.8s step-end infinite',
                }}
              />
            )}
          </div>
        )}
      </div>
    </div>
  );
}

// ════════════════════════════════════════════════════════════════
// MAIN COMPONENT
// ════════════════════════════════════════════════════════════════
export default function AgenticRoutingDemo() {
  const [messages, setMessages] = useState([]);
  const [nodeStates, setNodeStates] = useState({});
  const [activeChunks, setActiveChunks] = useState({});
  const [routingText, setRoutingText] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  const [leftPanelOpen, setLeftPanelOpen] = useState(true);
  const [inputValue, setInputValue] = useState('');

  // Dual-mode state: null = checking, true = live, false = demo
  const [isLiveMode, setIsLiveMode] = useState(null);
  const [liveTree, setLiveTree] = useState(null);
  const [conversationId, setConversationId] = useState(null);

  const animationIdRef = useRef(0);
  const nodeStatesRef = useRef({});
  const activeChunksRef = useRef({});
  const messagesRef = useRef([]);
  const chatEndRef = useRef(null);
  // Track which nodes have been activated during a live query
  const activatedNodesRef = useRef(new Set());

  // ── Backend detection on mount ──
  useEffect(() => {
    fetch(`${API_BASE}/api/v1/kb/topology`)
      .then((r) => r.json())
      .then((data) => {
        setLiveTree(transformTopology(data.tree));
        setIsLiveMode(true);
      })
      .catch(() => setIsLiveMode(false));
  }, []);

  // The tree to render — live topology or hardcoded demo
  const currentTree = isLiveMode ? liveTree : AGENT_TREE;

  // Scroll chat to bottom on new messages
  const scrollChat = useCallback(() => {
    if (chatEndRef.current) {
      chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, []);

  // State helpers that update both ref and state
  const updateNode = useCallback((nodeId, state) => {
    nodeStatesRef.current = { ...nodeStatesRef.current, [nodeId]: state };
    setNodeStates({ ...nodeStatesRef.current });
  }, []);

  const addChunk = useCallback((nodeId, chunk) => {
    const prev = activeChunksRef.current[nodeId] || [];
    activeChunksRef.current = { ...activeChunksRef.current, [nodeId]: [...prev, chunk] };
    setActiveChunks({ ...activeChunksRef.current });
  }, []);

  const resetState = useCallback(() => {
    nodeStatesRef.current = {};
    activeChunksRef.current = {};
    activatedNodesRef.current = new Set();
    setNodeStates({});
    setActiveChunks({});
    setRoutingText('');
  }, []);

  const addMessage = useCallback((role, content, isStreaming = false) => {
    const msg = { role, content, isStreaming };
    messagesRef.current = [...messagesRef.current, msg];
    setMessages([...messagesRef.current]);
    setTimeout(scrollChat, 50);
  }, [scrollChat]);

  const updateLastMessage = useCallback((content, isStreaming = true) => {
    const msgs = [...messagesRef.current];
    msgs[msgs.length - 1] = { ...msgs[msgs.length - 1], content, isStreaming };
    messagesRef.current = msgs;
    setMessages(msgs);
    setTimeout(scrollChat, 50);
  }, [scrollChat]);

  // ── Helper: find tree node by predicate ──
  const findTreeNode = useCallback((predicate, tree) => {
    if (!tree) return null;
    if (predicate(tree)) return tree;
    if (tree.children) {
      for (const child of tree.children) {
        const found = findTreeNode(predicate, child);
        if (found) return found;
      }
    }
    return null;
  }, []);

  // ── Helper: find parent of a node ──
  const findParentNode = useCallback((nodeId, tree, parent) => {
    if (!tree) return null;
    if (tree.id === nodeId) return parent;
    if (tree.children) {
      for (const child of tree.children) {
        const found = findParentNode(nodeId, child, tree);
        if (found) return found;
      }
    }
    return null;
  }, []);

  // ── SSE Event Handler for live mode ──
  const handleSSEEvent = useCallback((event) => {
    const tree = liveTree;

    switch (event.type) {
      case 'conversation_id':
        setConversationId(event.conversation_id);
        break;

      case 'routing_started':
        updateNode('router', 'routing');
        setRoutingText('Analyzing query...');
        break;

      case 'tool_call': {
        const args = event.arguments || {};
        const toolName = event.tool_name;

        // Build routing text
        const routingParts = [`Tool: ${toolName}`];
        if (args.discipline) routingParts.push(`Discipline: ${args.discipline}`);
        if (args.project) routingParts.push(`Project: ${args.project}`);
        if (args.query) routingParts.push(`Query: "${args.query.slice(0, 80)}"`);
        setRoutingText((prev) => (prev ? prev + '\n' : '') + routingParts.join(' | '));

        // Activate target nodes based on tool arguments
        if (toolName === 'search_kb') {
          if (args.discipline) {
            const discNode = findTreeNode((n) => n.id === `disc:${args.discipline}`, tree);
            if (discNode) {
              updateNode(discNode.id, 'activated');
              activatedNodesRef.current.add(discNode.id);
            }
          }
          if (args.source === 'project' && args.project) {
            const projNode = findTreeNode(
              (n) => n.id === `project:${args.project}` || n.id === args.project,
              tree
            );
            if (projNode) {
              updateNode(projNode.id, 'activated');
              activatedNodesRef.current.add(projNode.id);
            }
          }
        } else if (args.discipline) {
          // lookup_equation, lookup_table, get_package_info
          const discNode = findTreeNode((n) => n.id === `disc:${args.discipline}`, tree);
          if (discNode) {
            updateNode(discNode.id, 'activated');
            activatedNodesRef.current.add(discNode.id);
          }
        }
        break;
      }

      case 'tool_result': {
        const chunks = event.chunks || [];
        for (const chunk of chunks) {
          const chunkData = {
            source: chunk.id || chunk.title || 'chunk',
            score: chunk.score || 0,
            text: chunk.snippet || chunk.title || '',
          };

          // Find the best matching node for this chunk
          let targetNodeId = null;

          // Try to match by package_id first
          if (chunk.package_id) {
            const pkgNode = findTreeNode((n) => n.id === chunk.package_id, tree);
            if (pkgNode) {
              targetNodeId = pkgNode.id;
              updateNode(pkgNode.id, 'retrieving');
              activatedNodesRef.current.add(pkgNode.id);
              // Also activate parent discipline
              const parent = findParentNode(pkgNode.id, tree, null);
              if (parent && parent.id !== 'router') {
                updateNode(parent.id, 'retrieving');
                activatedNodesRef.current.add(parent.id);
              }
            }
          }

          // Fallback to discipline
          if (!targetNodeId && chunk.discipline) {
            const discNode = findTreeNode((n) => n.id === `disc:${chunk.discipline}`, tree);
            if (discNode) {
              targetNodeId = discNode.id;
              updateNode(discNode.id, 'retrieving');
              activatedNodesRef.current.add(discNode.id);
            }
          }

          // Final fallback to router
          if (!targetNodeId) {
            targetNodeId = 'router';
          }

          addChunk(targetNodeId, chunkData);
        }

        // Mark the tool_call's target as retrieving
        if (event.tool_name) {
          for (const nodeId of activatedNodesRef.current) {
            if (nodeStatesRef.current[nodeId] === 'activated') {
              updateNode(nodeId, 'retrieving');
            }
          }
        }
        break;
      }

      case 'synthesis_started':
        updateNode('router', 'synthesizing');
        addMessage('assistant', '', true);
        break;

      case 'text':
        updateLastMessage(
          (messagesRef.current[messagesRef.current.length - 1]?.content || '') + event.text,
          true
        );
        break;

      case 'rewrite':
        if (event.rewrite) {
          updateLastMessage(event.rewrite, false);
        }
        break;

      case 'done':
        // Mark all activated nodes as complete
        for (const nodeId of activatedNodesRef.current) {
          updateNode(nodeId, 'complete');
        }
        updateNode('router', 'complete');
        // Finalize last message streaming
        if (messagesRef.current.length > 0) {
          const lastMsg = messagesRef.current[messagesRef.current.length - 1];
          if (lastMsg.isStreaming) {
            updateLastMessage(lastMsg.content, false);
          }
        }
        setIsProcessing(false);
        break;

      case 'error':
        addMessage('assistant', `Error: ${event.error}`);
        setIsProcessing(false);
        break;

      default:
        // Handle legacy events without type (e.g. conversation_id)
        if (event.conversation_id) {
          setConversationId(event.conversation_id);
        }
        break;
    }
  }, [liveTree, updateNode, addChunk, addMessage, updateLastMessage, findTreeNode, findParentNode]);

  // ── Live mode: SSE consumer ──
  const processRealQuery = useCallback(
    async (query) => {
      if (isProcessing) return;
      resetState();
      setIsProcessing(true);
      addMessage('user', query);

      try {
        const resp = await fetch(`${API_BASE}/api/v1/chat/stream`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            message: query,
            conversation_id: conversationId,
          }),
        });

        if (!resp.ok) {
          addMessage('assistant', `Error: Server returned ${resp.status}`);
          setIsProcessing(false);
          return;
        }

        const reader = resp.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          buffer += decoder.decode(value, { stream: true });

          // Parse SSE lines
          const lines = buffer.split('\n');
          buffer = lines.pop(); // Keep incomplete line
          for (const line of lines) {
            if (!line.startsWith('data: ')) continue;
            try {
              const event = JSON.parse(line.slice(6));
              handleSSEEvent(event);
            } catch {
              // Skip malformed SSE lines
            }
          }
        }

        // Process any remaining buffer
        if (buffer.startsWith('data: ')) {
          try {
            const event = JSON.parse(buffer.slice(6));
            handleSSEEvent(event);
          } catch {
            // Skip malformed final line
          }
        }
      } catch (err) {
        addMessage('assistant', `Connection error: ${err.message}`);
        setIsProcessing(false);
      }
    },
    [isProcessing, conversationId, resetState, addMessage, handleSSEEvent]
  );

  // ── Demo mode: scripted animation sequence ──
  const processQuery = useCallback(
    async (queryIndex) => {
      if (isProcessing) return;
      const myId = ++animationIdRef.current;
      const alive = () => animationIdRef.current === myId;

      const q = QUERIES[queryIndex];
      resetState();
      setIsProcessing(true);

      // User message
      addMessage('user', q.query);

      // Phase 1: Router activates
      await delay(500);
      if (!alive()) return;
      updateNode('router', 'routing');

      await delay(1500);
      if (!alive()) return;

      // Phase 2: Type routing decision
      const fullText = q.routingText;
      for (let i = 0; i < fullText.length; i += 3) {
        if (!alive()) return;
        setRoutingText(fullText.slice(0, Math.min(i + 3, fullText.length)));
        await delay(18);
      }
      setRoutingText(fullText);
      await delay(400);

      // Phase 3: Activate sub-agents (and their project parents)
      for (const agentId of q.activatedAgents) {
        if (!alive()) return;
        const projectId = getProjectId(agentId);
        if (projectId) updateNode(projectId, 'activated');
        updateNode(agentId, 'activated');
        await delay(300);
      }

      // Phase 4: Searching (wait 1s)
      await delay(1000);
      if (!alive()) return;

      // Phase 5: Transition to retrieving and show chunks
      for (const agentId of q.activatedAgents) {
        updateNode(agentId, 'retrieving');
      }
      // Show chunks sequentially across all agents
      for (const agentId of q.activatedAgents) {
        const chunks = q.chunks[agentId] || [];
        for (let i = 0; i < chunks.length; i++) {
          if (!alive()) return;
          addChunk(agentId, chunks[i]);
          await delay(500);
        }
      }

      // Phase 6: Pause
      await delay(500);
      if (!alive()) return;

      // Phase 7: Synthesize — router glows again
      updateNode('router', 'synthesizing');
      addMessage('assistant', '', true);

      // Stream response word-by-word
      const CHARS_PER_CHUNK = 38;
      let pos = 0;
      while (pos < q.response.length) {
        if (!alive()) return;
        pos = Math.min(pos + CHARS_PER_CHUNK, q.response.length);
        // Snap to next whitespace boundary
        while (pos < q.response.length && q.response[pos] !== ' ' && q.response[pos] !== '\n') {
          pos++;
        }
        updateLastMessage(q.response.slice(0, pos), true);
        await delay(80);
      }
      updateLastMessage(q.response, false);

      // Phase 8: Complete
      for (const agentId of q.activatedAgents) {
        updateNode(agentId, 'complete');
        const projectId = getProjectId(agentId);
        if (projectId) updateNode(projectId, 'complete');
      }
      updateNode('router', 'complete');
      setIsProcessing(false);
    },
    [isProcessing, resetState, addMessage, updateNode, addChunk, updateLastMessage]
  );

  // Handle freeform input — routes to live or demo handler
  const handleFreeform = useCallback(() => {
    if (!inputValue.trim() || isProcessing) return;
    const query = inputValue.trim();
    setInputValue('');

    if (isLiveMode) {
      processRealQuery(query);
    } else {
      addMessage('user', query);
      addMessage(
        'assistant',
        'This demo supports the pre-built queries above. In production, any question would be routed through the agent tree.'
      );
    }
  }, [inputValue, isProcessing, isLiveMode, addMessage, processRealQuery]);

  // Loading state while checking backend
  if (isLiveMode === null) {
    return (
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        height: '100vh', background: COLORS.bg, color: COLORS.textDim,
        fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
      }}>
        Connecting to backend...
      </div>
    );
  }

  return (
    <>
      <style>{KEYFRAMES}</style>
      <div
        style={{
          display: 'flex',
          height: '100vh',
          width: '100%',
          background: COLORS.bg,
          color: COLORS.textPrimary,
          fontFamily:
            "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif",
          overflow: 'hidden',
        }}
      >
        {/* ── Demo Mode Banner ── */}
        {!isLiveMode && (
          <div
            style={{
              position: 'fixed',
              top: 0,
              left: 0,
              right: 0,
              zIndex: 100,
              background: '#e8a838',
              color: '#0a0f1a',
              textAlign: 'center',
              padding: '4px 0',
              fontSize: '0.72rem',
              fontWeight: 700,
              letterSpacing: '0.05em',
            }}
          >
            DEMO MODE — Backend unavailable, showing scripted demo
          </div>
        )}

        {/* ── Mobile toggle button ── */}
        <button
          onClick={() => setLeftPanelOpen(!leftPanelOpen)}
          style={{
            position: 'fixed',
            top: !isLiveMode ? 36 : 12,
            left: 12,
            zIndex: 50,
            background: COLORS.cardBg,
            border: `1px solid ${COLORS.cardBorder}`,
            borderRadius: '6px',
            padding: '6px 10px',
            color: COLORS.textSecondary,
            cursor: 'pointer',
            fontSize: '0.8rem',
            display: 'none',
          }}
          className="mobile-toggle"
        >
          {leftPanelOpen ? '\u2715' : '\u2630'}
        </button>

        {/* ═══════════════════════════════ LEFT PANEL ═══════════════════════════════ */}
        {leftPanelOpen && (
          <div
            style={{
              width: '35%',
              minWidth: '320px',
              maxWidth: '480px',
              height: '100%',
              background: COLORS.panelBg,
              borderRight: `1px solid ${COLORS.cardBorder}`,
              display: 'flex',
              flexDirection: 'column',
              flexShrink: 0,
              marginTop: !isLiveMode ? 24 : 0,
            }}
          >
            {/* Header */}
            <div
              style={{
                padding: '14px 16px',
                borderBottom: `1px solid ${COLORS.cardBorder}`,
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
              }}
            >
              <span style={{ fontSize: '1rem' }}>{'\uD83D\uDD2C'}</span>
              <span style={{ fontWeight: 700, fontSize: '0.9rem', color: COLORS.textPrimary }}>
                Agent Hierarchy
              </span>
              <span
                style={{
                  marginLeft: 'auto',
                  fontSize: '0.6rem',
                  color: isLiveMode ? COLORS.scoreGreen : COLORS.textDim,
                  background: isLiveMode ? COLORS.scoreGreen + '15' : COLORS.cardBg,
                  padding: '2px 8px',
                  borderRadius: '10px',
                  border: `1px solid ${isLiveMode ? COLORS.scoreGreen + '40' : COLORS.cardBorder}`,
                }}
              >
                {isLiveMode ? 'LIVE' : 'DEMO'}
              </span>
            </div>

            {/* Tree */}
            <div style={{ flex: 1, overflowY: 'auto', padding: '10px 12px' }}>
              {currentTree && (
                <AgentNode
                  node={currentTree}
                  depth={0}
                  nodeStates={nodeStates}
                  activeChunks={activeChunks}
                  routingText={routingText}
                />
              )}
            </div>
          </div>
        )}

        {/* ═══════════════════════════════ RIGHT PANEL ═══════════════════════════════ */}
        <div
          style={{
            flex: 1,
            display: 'flex',
            flexDirection: 'column',
            minWidth: 0,
            marginTop: !isLiveMode ? 24 : 0,
          }}
        >
          {/* Header */}
          <div
            style={{
              padding: '14px 20px',
              borderBottom: `1px solid ${COLORS.cardBorder}`,
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
            }}
          >
            <span style={{ fontSize: '1rem' }}>{'\uD83D\uDCAC'}</span>
            <span style={{ fontWeight: 700, fontSize: '0.9rem' }}>Agent Chat</span>
            <span
              style={{
                marginLeft: 'auto',
                fontSize: '0.6rem',
                color: COLORS.router,
                background: COLORS.router + '15',
                padding: '2px 8px',
                borderRadius: '10px',
                border: `1px solid ${COLORS.router}30`,
              }}
            >
              {isLiveMode ? 'Live RAG' : 'RAG Demo'}
            </span>
          </div>

          {/* Quick-select query buttons (demo mode only) */}
          {!isLiveMode && (
            <div
              style={{
                padding: '10px 20px',
                borderBottom: `1px solid ${COLORS.cardBorder}`,
                display: 'flex',
                flexWrap: 'wrap',
                gap: '6px',
              }}
            >
              {QUERIES.map((q, i) => (
                <button
                  key={i}
                  onClick={() => processQuery(i)}
                  disabled={isProcessing}
                  style={{
                    background: isProcessing ? COLORS.cardBg : COLORS.cardBg,
                    border: `1px solid ${COLORS.cardBorder}`,
                    borderRadius: '16px',
                    padding: '5px 14px',
                    color: isProcessing ? COLORS.textDim : COLORS.textSecondary,
                    fontSize: '0.72rem',
                    cursor: isProcessing ? 'not-allowed' : 'pointer',
                    transition: 'all 0.2s ease',
                    whiteSpace: 'nowrap',
                    opacity: isProcessing ? 0.5 : 1,
                  }}
                  onMouseEnter={(e) => {
                    if (!isProcessing) {
                      e.target.style.borderColor = COLORS.router;
                      e.target.style.color = COLORS.router;
                    }
                  }}
                  onMouseLeave={(e) => {
                    e.target.style.borderColor = COLORS.cardBorder;
                    e.target.style.color = isProcessing ? COLORS.textDim : COLORS.textSecondary;
                  }}
                >
                  {q.label}
                </button>
              ))}
            </div>
          )}

          {/* Chat messages */}
          <div
            style={{
              flex: 1,
              overflowY: 'auto',
              padding: '8px 0',
            }}
          >
            {messages.length === 0 && (
              <div
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  height: '100%',
                  gap: '12px',
                  opacity: 0.5,
                }}
              >
                <span style={{ fontSize: '2rem' }}>{'\uD83D\uDD2C'}</span>
                <span style={{ color: COLORS.textDim, fontSize: '0.85rem' }}>
                  {isLiveMode
                    ? 'Ask any question about the knowledge base'
                    : 'Select a query above to start the demo'}
                </span>
                <span style={{ color: COLORS.textDim, fontSize: '0.7rem' }}>
                  {isLiveMode
                    ? 'The agent tree will animate in real-time as your query is processed'
                    : 'Watch the agent tree animate as queries are routed and processed'}
                </span>
              </div>
            )}
            {messages.map((msg, i) => (
              <ChatMessage key={i} message={msg} />
            ))}
            <div ref={chatEndRef} />
          </div>

          {/* Input bar */}
          <div
            style={{
              padding: '12px 20px',
              borderTop: `1px solid ${COLORS.cardBorder}`,
              display: 'flex',
              gap: '8px',
            }}
          >
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter') handleFreeform();
              }}
              placeholder={
                isLiveMode
                  ? 'Ask any question...'
                  : 'Type a question or select a demo query above...'
              }
              disabled={isProcessing}
              style={{
                flex: 1,
                background: COLORS.cardBg,
                border: `1px solid ${COLORS.cardBorder}`,
                borderRadius: '8px',
                padding: '8px 14px',
                color: COLORS.textPrimary,
                fontSize: '0.82rem',
                outline: 'none',
              }}
            />
            <button
              onClick={handleFreeform}
              disabled={isProcessing || !inputValue.trim()}
              style={{
                background: COLORS.router + '20',
                border: `1px solid ${COLORS.router}40`,
                borderRadius: '8px',
                padding: '8px 16px',
                color: COLORS.router,
                fontSize: '0.8rem',
                fontWeight: 600,
                cursor: isProcessing || !inputValue.trim() ? 'not-allowed' : 'pointer',
                opacity: isProcessing || !inputValue.trim() ? 0.4 : 1,
              }}
            >
              Send
            </button>
          </div>
        </div>
      </div>
    </>
  );
}
