# fig-topic-09: Provenance & Attribution-by-Design

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-09 |
| **Title** | Provenance — Why Attribution Must Be Designed In, Not Detected After |
| **Audience** | General + Technical |
| **Complexity** | L3 (detailed) |
| **Location** | Landing page, Topic Card IX (Governance & Security group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Post-hoc attribution fails because of the Oracle Problem: digital systems cannot fully verify physical/training reality. This figure contrasts attribution-by-design (solid provenance chain from creation to AI consent query) with post-hoc detection (broken chain hitting three epistemic barriers). Uses "Hide and Seek" by Imogen Heap as a concrete running example, maps provenance events to W3C PROV (Entity/Activity/Agent) and OpenLineage (Job/Run/Dataset), and shows Morreale et al.'s key distinction between training-time and inference-time attribution. Communicates: "you cannot detect attribution after the fact — you must design it in at creation, and even then, deterrence works better than detection."

Key concepts:
- **Oracle Problem**: Three epistemic barriers (training verification, influence attribution, absence verification)
- **Deterrence equation**: p × d × F ≥ g (audit probability × detection probability × fine ≥ expected gain)
- **Morreale et al. (2025)**: Training-time attribution is intractable; inference-time attribution is viable
- **W3C PROV**: Entity/Activity/Agent with wasGeneratedBy, wasDerivedFrom, wasAttributedTo
- **OpenLineage**: Job/Run/Dataset model with extensible facets

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  ATTRIBUTION-BY-DESIGN         ║  POST-HOC ATTRIBUTION      │
│  (solid provenance chain)      ║  (broken chain)            │
│  ─────────────────────         ║  ────────────────          │
│                                ║                             │
│  "Hide and Seek" life story:   ║  THREE EPISTEMIC BARRIERS  │
│                                ║  (the Oracle Problem)       │
│  ● CREATE                      ║                             │
│  │ Heap records with DigiTech  ║  ① TRAINING VERIFICATION   │
│  │ Vocalist harmonizer, 2005   ║  "Did the model train on   │
│  │ PROV: Recording             ║   this track?"             │
│  │   wasGeneratedBy Session    ║  → Cannot prove what data  │
│  │   wasAttributedTo Heap      ║    entered a black box     │
│  │                             ║                             │
│  ● REGISTER                    ║  ② INFLUENCE ATTRIBUTION   │
│  │ ISRC: GBUM70500123 (A1)    ║  "Did the output derive    │
│  │ ISWC: T-xxx.xxx.xxx (A2)   ║   from this track?"        │
│  │ ISNI: 0000 0000 7840 (A3)  ║  → Similarity ≠ causation  │
│  │                             ║    (correlation trap)       │
│  ● DISTRIBUTE                  ║                             │
│  │ DDEX messages → DSPs        ║  ③ ABSENCE VERIFICATION    │
│  │ Megaphonic Records          ║  "Did the model NOT use    │
│  │                             ║   this track?"             │
│  ● DERIVE                      ║  → Cannot prove a negative │
│  │ "Whatcha Say" (Jason Derulo) ║                            │
│  │ wasDerivedFrom "Hide & Seek"║  Each barrier is           │
│  │ Mechanical license cleared   ║  epistemic, not technical  │
│  │                             ║  — no technology solves it  │
│  ● AI CONSENT QUERY            ║                             │
│  │ Agent → MCP server:         ║  Post-hoc similarity       │
│  │ "Can I train on GBUM705?"   ║  detection:                │
│  │ Response: DENIED (training) ║  ○ · · · ? · · · ○         │
│  │ Alternative: inference OK   ║  broken    unknown          │
│  │ at $0.003/generation        ║  chain     provenance       │
│  │                             ║                             │
│  Solid chain: every event      ║                             │
│  recorded at creation time     ║                             │
│                                ║                             │
│  ═══════════════════════════════════════════════════════════ │
│                                                              │
│  DETERRENCE > DETECTION                                     │
│  ──────────────────────                                     │
│  p × d × F ≥ g                                              │
│  0.1 × 0.3 × $5M = $150K > $100K (gain)                   │
│  Deterrence holds even with imperfect detection             │
│                                                              │
│  MORREALE ET AL. (2025): KEY DISTINCTION                    │
│  ──────────────────────────────────────                     │
│  Training-time attribution: INTRACTABLE                     │
│  (cannot prove what trained the model)                      │
│  Inference-time attribution: VIABLE                         │
│  (can verify what conditioned a specific output)            │
│                                                              │
│  ■ RECORDED  ■ INFERRED  ? UNKNOWN  ║ ORACLE BOUNDARY      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| By-design chain (left) | `data_primary` | Teal solid vertical chain: CREATE → REGISTER → DISTRIBUTE → DERIVE → AI CONSENT |
| "Hide and Seek" events | `label_editorial` | Concrete provenance events with real identifiers (ISRC, ISWC, ISNI) |
| W3C PROV labels | `typography_mono` | wasGeneratedBy, wasDerivedFrom, wasAttributedTo annotations |
| Assurance level badges | `data_primary` | A1, A2, A3 badges at ISRC, ISWC, ISNI registration steps |
| Oracle boundary | `line_accent` | Coral vertical divider between approaches |
| Three epistemic barriers | `data_warning` | Orange numbered list: ① training verification, ② influence attribution, ③ absence verification |
| Post-hoc broken chain | `data_warning` | Orange dotted line with gaps and question mark |
| Deterrence equation | `typography_mono` | p × d × F ≥ g with worked numeric example |
| Morreale distinction | `region_secondary` | Two-row comparison: training-time (intractable) vs inference-time (viable) |
| MCP consent query | `data_accent` | Coral-highlighted agent query with DENIED response and alternative pricing |
| Legend | `label_editorial` | RECORDED / INFERRED / UNKNOWN markers + Oracle Boundary |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "ATTRIBUTION-BY-DESIGN", "POST-HOC ATTRIBUTION", "Hide and Seek" provenance events, PROV relationship names, ISRC/ISWC/ISNI identifiers, "THREE EPISTEMIC BARRIERS", "ORACLE PROBLEM", barrier descriptions, "DETERRENCE > DETECTION", deterrence equation with numbers, "MORREALE ET AL.", "INTRACTABLE", "VIABLE", "RECORDED", "INFERRED", "UNKNOWN", "ORACLE BOUNDARY", MCP query example.

## Alt Text

Provenance infographic split by a coral Oracle Boundary. Left side: attribution-by-design showing "Hide and Seek" by Imogen Heap as a solid teal provenance chain with five events — CREATE (2005 recording with DigiTech Vocalist), REGISTER (ISRC at A1, ISWC at A2, ISNI at A3), DISTRIBUTE (DDEX messages to DSPs), DERIVE (Jason Derulo's "Whatcha Say" with mechanical license), and AI CONSENT QUERY (MCP server denies training, offers inference at $0.003/generation). W3C PROV labels annotate each event. Right side: post-hoc attribution hitting three epistemic barriers — training verification (cannot prove what data entered a black box), influence attribution (similarity does not prove causation), and absence verification (cannot prove a negative). A broken orange dotted chain with question marks illustrates the post-hoc failure. Below, the deterrence equation (p × d × F ≥ g) shows deterrence holds even at 10% audit probability. Morreale et al.'s key distinction: training-time attribution is intractable, inference-time attribution is viable.
