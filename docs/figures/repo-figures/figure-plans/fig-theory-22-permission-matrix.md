# fig-theory-22: Permission Matrix

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-22 |
| **Title** | Permission Matrix -- Works x Use Cases |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (academic terms, policy implications) |
| **Location** | docs/theory/mcp-consent.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows a permission matrix where rows are musical works and columns are use cases, with each cell indicating ALLOW, DENY, or CONDITIONS. It answers: "What does a real permission landscape look like across multiple works and use types?"

The key message is: "Permissions are not binary -- each work has a unique permission profile across different use types, and artists can set granular per-work, per-use policies."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  PERMISSION MATRIX                                             |
|  ■ Works x Use Cases                                           |
+---------------------------------------------------------------+
|                                                                |
|              │Streaming│Sync    │Download│AI      │Voice  │   |
|              │         │License │        │Training│Clone  │   |
|  ────────────┼─────────┼────────┼────────┼────────┼───────┤   |
|              │         │        │        │        │       │   |
|  "Hide &     │  ALLOW  │ COND.  │ ALLOW  │  DENY  │ DENY  │   |
|   Seek"      │         │ (fee)  │        │        │       │   |
|  ────────────┼─────────┼────────┼────────┼────────┼───────┤   |
|              │         │        │        │        │       │   |
|  "Headlock"  │  ALLOW  │ ALLOW  │ ALLOW  │ COND.  │ DENY  │   |
|              │         │        │        │(attrib)│       │   |
|  ────────────┼─────────┼────────┼────────┼────────┼───────┤   |
|              │         │        │        │        │       │   |
|  "Blanket"   │  ALLOW  │ COND.  │ DENY   │  DENY  │ DENY  │   |
|              │         │(apprvl)│        │        │       │   |
|  ────────────┼─────────┼────────┼────────┼────────┼───────┤   |
|              │         │        │        │        │       │   |
|  "First      │  ALLOW  │ ALLOW  │ ALLOW  │ ALLOW  │ COND. │   |
|   Train      │         │        │        │        │(fee + │   |
|   Home"      │         │        │        │        │attrib)│   |
|  ────────────┼─────────┼────────┼────────┼────────┼───────┤   |
|              │         │        │        │        │       │   |
|  "Goodnight  │  ALLOW  │ DENY   │ ALLOW  │  DENY  │ DENY  │   |
|   and Go"    │         │        │        │        │       │   |
|              │         │        │        │        │       │   |
+---------------------------------------------------------------+
|                                                                |
|  LEGEND                                                        |
|  ──────                                                        |
|                                                                |
|  ■ ALLOW  = Permitted, no additional steps                     |
|  ■ DENY   = Not permitted under any conditions                 |
|  ■ COND.  = Permitted with conditions (fee, attribution,       |
|             approval required)                                 |
|                                                                |
|  KEY INSIGHT: Voice cloning is almost always DENY --           |
|  streaming is almost always ALLOW. The interesting cases       |
|  are in between.                                               |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "PERMISSION MATRIX" with coral accent square |
| Subtitle | `label_editorial` | "Works x Use Cases" |
| Column headers (use cases) | `label_editorial` | Streaming, Sync License, Download, AI Training, Voice Clone |
| Row headers (works) | `stakeholder_artist` | Five Imogen Heap songs as row labels |
| ALLOW cells | `confidence_high` | Green-coded cells indicating unconditional permission |
| DENY cells | `confidence_low` | Red-coded cells indicating absolute denial |
| COND. cells | `confidence_medium` | Amber-coded cells indicating conditional permission |
| Condition annotations | `data_mono` | "(fee)," "(attrib)," "(apprvl)," "(fee+attrib)" in monospace |
| Matrix grid lines | `accent_line` | Coral divider lines forming the grid |
| Legend section | `callout_box` | Three-item legend: ALLOW, DENY, COND. with definitions |
| Key insight note | `callout_box` | Voice cloning mostly DENY, streaming mostly ALLOW |

## Anti-Hallucination Rules

1. The five works are Imogen Heap songs: "Hide & Seek," "Headlock," "Blanket," "First Train Home," "Goodnight and Go." Do NOT use non-Imogen-Heap songs.
2. Five use cases: Streaming, Sync License, Download, AI Training, Voice Clone. Do NOT add or remove columns.
3. Streaming is ALLOW for all works -- this is the baseline expected permission.
4. Voice cloning is DENY for almost all works -- this reflects real artist sentiment.
5. Conditions include: fee, attribution, approval. Do NOT invent other condition types.
6. The matrix values are ILLUSTRATIVE -- do NOT claim these are Imogen Heap's actual permissions.
7. COND. is short for CONDITIONS -- always define it in the legend.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Matrix diagram: permission matrix for music attribution with five Imogen Heap songs as rows and five use types as columns (streaming, sync license, download, AI training, voice cloning) -- cells colored green for allow, red for deny, amber for conditional with fee or attribution requirements -- showing how machine-readable consent enables granular per-work permission profiles with transparent confidence in the open-source music credits scaffold.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Matrix diagram: permission matrix for music attribution with five Imogen Heap songs as rows and five use types as columns (streaming, sync license, download, AI training, voice cloning) -- cells colored green for allow, red for deny, amber for conditional with fee or attribution requirements -- showing how machine-readable consent enables granular per-work permission profiles with transparent confidence in the open-source music credits scaffold.](docs/figures/repo-figures/assets/fig-theory-22-permission-matrix.jpg)

*Figure 22. Permission matrix across works and use cases: permissions are not binary -- each musical work has a unique profile where streaming is typically allowed, voice cloning is typically denied, and the interesting policy decisions (AI training, sync licensing) vary per work with conditional terms.*

### From this figure plan (relative)

![Matrix diagram: permission matrix for music attribution with five Imogen Heap songs as rows and five use types as columns (streaming, sync license, download, AI training, voice cloning) -- cells colored green for allow, red for deny, amber for conditional with fee or attribution requirements -- showing how machine-readable consent enables granular per-work permission profiles with transparent confidence in the open-source music credits scaffold.](../assets/fig-theory-22-permission-matrix.jpg)
