# fig-theory-07: Assurance Level Decision Tree

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-07 |
| **Title** | Assurance Level Decision Tree |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation logic, decision flow) |
| **Location** | docs/theory/assurance-levels.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the classification logic for determining which assurance level a given attribution record reaches. It answers: "Given a set of evidence, how does the system decide between A0, A1, A2, and A3?"

The key message is: "Assurance classification is a deterministic decision tree -- check for artist verification first, then source agreement, then any identifier, falling to A0 if nothing is found."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  ASSURANCE LEVEL DECISION TREE                                 |
|  ■ Classification Logic                                        |
+---------------------------------------------------------------+
|                                                                |
|              ┌───────────────────────┐                         |
|              │  START: Attribution    │                         |
|              │  record received       │                         |
|              └───────────┬───────────┘                         |
|                          │                                     |
|                          ▼                                     |
|              ┌───────────────────────┐                         |
|              │  Has artist directly   │                         |
|              │  verified this claim?  │                         |
|              └─────┬───────────┬─────┘                         |
|                YES │           │ NO                             |
|                    ▼           ▼                                |
|         ┌──────────────┐  ┌───────────────────────┐           |
|         │  A3           │  │  Do 2+ independent    │           |
|         │  VERIFIED     │  │  sources agree?        │           |
|         │  ────────     │  └─────┬───────────┬─────┘           |
|         │  ISNI + IPI   │    YES │           │ NO              |
|         │  confirmed    │        ▼           ▼                 |
|         └──────────────┘  ┌──────────┐  ┌───────────────┐     |
|                           │  A2       │  │  Is there ANY  │     |
|                           │ CORROBOR. │  │  identifier    │     |
|                           │ ────────  │  │  (ISRC/ISWC)?  │     |
|                           │ ISWC+ISRC │  └──┬──────────┬──┘     |
|                           │ cross-ref │  YES│          │NO      |
|                           └──────────┘     ▼          ▼        |
|                                      ┌──────────┐ ┌──────────┐|
|                                      │  A1       │ │  A0       │|
|                                      │  CLAIMED  │ │  UNKNOWN  │|
|                                      │  ──────── │ │  ──────── │|
|                                      │  Single   │ │  No data  │|
|                                      │  source   │ │  No ID    │|
|                                      └──────────┘ └──────────┘|
|                                                                |
+---------------------------------------------------------------+
|  ■ NOTES                                                       |
|  1. Tree evaluates TOP-DOWN: A3 first, A0 last (fail-safe)    |
|  2. "Independent sources" = different databases, not fields     |
|  3. Artist verification requires signed attestation or          |
|     authenticated API submission                                |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ASSURANCE LEVEL DECISION TREE" with coral accent square |
| Subtitle | `label_editorial` | "Classification Logic" |
| Start node | `processing_stage` | "Attribution record received" -- entry point |
| Decision: Artist verified? | `decision_point` | Diamond/rectangle asking about direct artist verification |
| Decision: 2+ sources agree? | `decision_point` | Diamond/rectangle asking about independent source agreement |
| Decision: Any identifier? | `decision_point` | Diamond/rectangle asking about existence of any standard ID |
| A3 terminal | `assurance_a3` | "VERIFIED" -- green-coded terminal with ISNI+IPI |
| A2 terminal | `assurance_a2` | "CORROBORATED" -- blue-coded terminal with ISWC+ISRC |
| A1 terminal | `assurance_a1` | "CLAIMED" -- amber-coded terminal with single source |
| A0 terminal | `assurance_a0` | "UNKNOWN" -- gray-coded terminal with no data |
| YES/NO branch labels | `label_editorial` | Branch labels on each decision edge |
| Flow arrows | `data_flow` | Downward arrows connecting decision nodes to outcomes |
| Notes callout | `callout_box` | Three implementation notes about evaluation order and definitions |

## Anti-Hallucination Rules

1. The tree evaluates TOP-DOWN: A3 first, then A2, then A1, falling to A0. Do NOT reorder.
2. Each decision has exactly two outcomes: YES and NO. Do NOT add "MAYBE" or partial branches.
3. "2+ independent sources" means different databases (e.g., MusicBrainz AND Discogs), not two fields from the same source.
4. Artist verification requires signed attestation or authenticated API submission -- do NOT weaken this to "self-reported."
5. A0 is the FAIL-SAFE default -- if nothing else matches, the record is A0.
6. Do NOT add additional decision nodes beyond the three shown.
7. Do NOT include confidence scores in this figure -- this is about assurance levels, not confidence.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Decision tree: deterministic classification flowchart for music attribution assurance levels -- starting with an attribution record, checking artist verification for A3, then independent source agreement for A2, then any ISRC or ISWC identifier for A1, defaulting to A0 unknown as fail-safe -- showing how the open-source attribution scaffold assigns transparent confidence levels to music credits.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Decision tree: deterministic classification flowchart for music attribution assurance levels -- starting with an attribution record, checking artist verification for A3, then independent source agreement for A2, then any ISRC or ISWC identifier for A1, defaulting to A0 unknown as fail-safe -- showing how the open-source attribution scaffold assigns transparent confidence levels to music credits.](docs/figures/repo-figures/assets/fig-theory-07-assurance-decision-tree.jpg)

*Figure 7. The assurance level decision tree evaluates top-down from A3 to A0: artist verification yields A3, cross-database agreement yields A2, any standard identifier yields A1, and absence of all evidence defaults to A0 as a fail-safe classification.*

### From this figure plan (relative)

![Decision tree: deterministic classification flowchart for music attribution assurance levels -- starting with an attribution record, checking artist verification for A3, then independent source agreement for A2, then any ISRC or ISWC identifier for A1, defaulting to A0 unknown as fail-safe -- showing how the open-source attribution scaffold assigns transparent confidence levels to music credits.](../assets/fig-theory-07-assurance-decision-tree.jpg)
