# fig-theory-06: Assurance Levels -- Standards Mapping

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-06 |
| **Title** | Assurance Levels -- Standards Mapping |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (code terms, industry standard identifiers) |
| **Location** | docs/theory/assurance-levels.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure maps the A0-A3 assurance levels to real music industry standard identifiers (ISRC, ISWC, ISNI, IPI) and shows what evidence is required at each level. It answers: "What concrete identifiers and evidence correspond to each assurance level?"

The key message is: "Each assurance level maps to specific industry identifiers and evidence requirements -- from no identifier (A0) to artist-verified identity with ISNI/IPI (A3)."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  ASSURANCE LEVELS — STANDARDS MAPPING                          |
|  ■ From Identifiers to Trust                                   |
+---------------------------------------------------------------+
|                                                                |
|                         ┌─────────────────────┐                |
|                         │  A3: VERIFIED        │                |
|                         │  ─────────           │                |
|                         │  ISNI + IPI          │                |
|                    ┌────│  Artist signature    │                |
|                    │    │  Direct verification │                |
|                    │    └─────────────────────┘                |
|               ┌────┤                                           |
|               │    │    ┌─────────────────────┐                |
|               │    └────│  A2: CORROBORATED    │                |
|               │         │  ─────────────       │                |
|          ┌────┤         │  ISWC + ISRC         │                |
|          │    │         │  2+ sources match    │                |
|          │    │         │  Cross-DB agreement  │                |
|          │    │         └─────────────────────┘                |
|     ┌────┤    │                                                |
|     │    │    │         ┌─────────────────────┐                |
|     │    │    └─────────│  A1: CLAIMED         │                |
|     │    │              │  ──────────          │                |
|     │    │              │  ISRC only           │                |
|     │    │              │  Single source       │                |
|     │    │              │  File metadata       │                |
|     │    │              └─────────────────────┘                |
|     │    │                                                     |
|     │    │              ┌─────────────────────┐                |
|     │    └──────────────│  A0: UNKNOWN         │                |
|     │                   │  ──────────          │                |
|     │                   │  No identifier       │                |
|     │                   │  No provenance       │                |
|     │                   │  Metadata absent     │                |
|     │                   └─────────────────────┘                |
|     │                                                          |
|     │   ┌──────────────────────────────────────┐               |
|     └──►│  ANALOG HOLE WARNING                  │               |
|         │  ────────────────────                 │               |
|         │  Re-encoding breaks identifier chain. │               |
|         │  A3 ≠ tamper-proof. Deterrence, not   │               |
|         │  detection (see fig-theory-04).        │               |
|         └──────────────────────────────────────┘               |
|                                                                |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ASSURANCE LEVELS -- STANDARDS MAPPING" with coral accent square |
| Subtitle | `label_editorial` | "From Identifiers to Trust" |
| A0 block | `assurance_a0` | "UNKNOWN" -- No identifier, no provenance, metadata absent |
| A1 block | `assurance_a1` | "CLAIMED" -- ISRC only, single source, file metadata |
| A2 block | `assurance_a2` | "CORROBORATED" -- ISWC + ISRC, 2+ sources match, cross-DB agreement |
| A3 block | `assurance_a3` | "VERIFIED" -- ISNI + IPI, artist signature, direct verification |
| Pyramid structure | `processing_stage` | Ascending blocks showing narrowing evidence requirements |
| Identifier labels (ISRC, ISWC, ISNI, IPI) | `data_mono` | Industry codes in monospace font |
| Evidence requirements | `label_editorial` | Plain-text descriptions of what each level requires |
| Analog hole warning | `problem_statement` | Callout box warning that re-encoding breaks identifier chains |
| Cross-reference to fig-theory-04 | `citation_bar` | Reference to deterrence economics figure |

## Anti-Hallucination Rules

1. Standard identifiers: ISRC (International Standard Recording Code), ISWC (International Standard Musical Work Code), ISNI (International Standard Name Identifier), IPI (Interested Parties Information). Do NOT invent others.
2. A0 has NO identifiers. A1 has ISRC only. A2 has ISWC + ISRC. A3 has ISNI + IPI on top.
3. The analog hole WARNING must be present -- A3 is NOT tamper-proof or immutable.
4. Do NOT claim that any level guarantees correctness -- they represent EVIDENCE levels, not truth.
5. "2+ sources" at A2 means at least two independent databases agree -- not two fields in the same database.
6. Do NOT include Spotify, Apple Music, or any platform-specific identifiers.
7. The pyramid narrows upward because fewer records achieve higher assurance -- do NOT invert this.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Mapping diagram: pyramid mapping music attribution assurance levels A0 through A3 to industry standard identifiers -- A0 with no identifier, A1 with ISRC only, A2 adding ISWC for cross-database agreement, A3 adding ISNI and IPI for artist-verified identity -- with analog hole warning showing that even A3 is not tamper-proof, supporting transparent confidence in music metadata.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Mapping diagram: pyramid mapping music attribution assurance levels A0 through A3 to industry standard identifiers -- A0 with no identifier, A1 with ISRC only, A2 adding ISWC for cross-database agreement, A3 adding ISNI and IPI for artist-verified identity -- with analog hole warning showing that even A3 is not tamper-proof, supporting transparent confidence in music metadata.](docs/figures/repo-figures/assets/fig-theory-06-assurance-standards-mapping.jpg)

*Figure 6. Assurance levels mapped to music industry standard identifiers (ISRC, ISWC, ISNI, IPI): each level requires progressively stronger evidence, from no provenance at A0 to artist-verified identity at A3, while the analog hole warning acknowledges that no level guarantees tamper-proof attribution.*

### From this figure plan (relative)

![Mapping diagram: pyramid mapping music attribution assurance levels A0 through A3 to industry standard identifiers -- A0 with no identifier, A1 with ISRC only, A2 adding ISWC for cross-database agreement, A3 adding ISNI and IPI for artist-verified identity -- with analog hole warning showing that even A3 is not tamper-proof, supporting transparent confidence in music metadata.](../assets/fig-theory-06-assurance-standards-mapping.jpg)
