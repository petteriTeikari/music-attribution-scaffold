# fig-theory-03: Attribution-by-Design vs Post-Hoc Detection

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-03 |
| **Title** | Attribution-by-Design vs Post-Hoc Detection |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (academic terms, structural comparison) |
| **Location** | docs/theory/oracle-problem.md, docs/theory/attribution-design.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure contrasts the two fundamental approaches to the attribution problem: trying to detect provenance after the fact (post-hoc) versus embedding provenance at the point of creation (by-design). It answers: "If we can't unmix the paint, what CAN we do instead?"

The key message is: "Post-hoc detection is inherently limited by the Oracle Problem -- attribution-by-design embeds provenance before the mixing happens, making the question answerable."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  ATTRIBUTION APPROACHES                                        |
|  ■ Post-Hoc Detection vs Attribution-by-Design                 |
+-------------------------------+-------------------------------+
|                               |                               |
|  I. POST-HOC DETECTION        |  II. ATTRIBUTION-BY-DESIGN    |
|  ─────────────────────        |  ──────────────────────────    |
|  (Trying to unmix paint)      |  (Label the tubes first)      |
|                               |                               |
|  ┌──────────┐                |  ┌──────────┐                 |
|  │Generated │                |  │ Creator  │                 |
|  │ Output   │                |  │  Data    │                 |
|  └────┬─────┘                |  └────┬─────┘                 |
|       │                       |       │                       |
|       ▼                       |       ▼                       |
|  ┌──────────┐                |  ┌──────────┐                 |
|  │ Content  │                |  │ Embed    │                 |
|  │ Analysis │                |  │Provenance│                 |
|  │ ???      │                |  │ A2 ✓     │                 |
|  └────┬─────┘                |  └────┬─────┘                 |
|       │                       |       │                       |
|   - - ▼ - - (broken)         |       ▼                       |
|  ┌──────────┐                |  ┌──────────┐                 |
|  │ Style    │                |  │ Training │                 |
|  │ Matching │                |  │ w/ Tags  │                 |
|  │ ???      │                |  │ ✓        │                 |
|  └────┬─────┘                |  └────┬─────┘                 |
|       │                       |       │                       |
|   - - ▼ - - (broken)         |       ▼                       |
|  ┌──────────┐                |  ┌──────────┐                 |
|  │ NO       │                |  │ Query    │                 |
|  │ ANSWER   │                |  │Provenance│                 |
|  │ ✗        │                |  │ = Known  │                 |
|  └──────────┘                |  └──────────┘                 |
|                               |                               |
|  Oracle Problem blocks        |  Provenance survives because  |
|  reverse engineering          |  it was embedded before       |
|                               |  training began               |
+-------------------------------+-------------------------------+
|  ■ This repo implements the RIGHT side: embed first, query    |
|    later. ISRC, ISWC, ISNI codes at A0-A3 assurance levels.  |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ATTRIBUTION APPROACHES" with coral accent square |
| Subtitle | `label_editorial` | "Post-Hoc Detection vs Attribution-by-Design" |
| Left panel header | `section_numeral` | "I. POST-HOC DETECTION" with subtitle "(Trying to unmix paint)" |
| Right panel header | `section_numeral` | "II. ATTRIBUTION-BY-DESIGN" with subtitle "(Label the tubes first)" |
| Left: Generated Output box | `problem_statement` | Starting point for post-hoc approach -- the output already exists |
| Left: Content Analysis box | `problem_statement` | Attempted analysis with "???" showing uncertainty |
| Left: Style Matching box | `problem_statement` | Attempted style comparison with "???" |
| Left: NO ANSWER box | `problem_statement` | Dead end -- failure state with cross mark |
| Left: Broken arrows | `data_flow` | Dashed/broken arrows showing failed information flow |
| Right: Creator Data box | `solution_component` | Starting point -- original creator data |
| Right: Embed Provenance box | `solution_component` | Provenance tagging step with A2 assurance indicator |
| Right: Training w/ Tags box | `solution_component` | Training that preserves embedded provenance |
| Right: Query Provenance box | `solution_component` | Successful provenance query with known result |
| Right: Solid arrows | `data_flow` | Solid arrows showing intact information flow |
| Vertical divider | `accent_line_v` | Coral red vertical line between panels |
| Footer callout | `callout_box` | "This repo implements the RIGHT side" with ISRC/ISWC/ISNI reference |

## Anti-Hallucination Rules

1. Post-hoc detection is shown as FAILING -- do NOT imply it works partially or for certain cases.
2. Attribution-by-design requires embedding provenance BEFORE training -- not during or after.
3. Industry identifiers are ISRC, ISWC, ISNI, IPI -- do NOT invent other identifier codes.
4. Assurance levels are A0-A3 -- always use this range, not A1-A4 or any other.
5. Do NOT claim this repo performs content analysis or style matching -- it implements the by-design approach.
6. Do NOT name specific AI models or music generation tools.
7. The "label the tubes" metaphor connects back to fig-theory-01 -- maintain consistency.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Comparison chart: post-hoc detection with broken arrows leading to no answer versus attribution-by-design with embedded provenance at ISRC and ISWC assurance levels A0-A3 leading to queryable music credits -- demonstrating why open-source music attribution scaffolds must embed provenance before AI training rather than attempting reverse engineering afterward.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Comparison chart: post-hoc detection with broken arrows leading to no answer versus attribution-by-design with embedded provenance at ISRC and ISWC assurance levels A0-A3 leading to queryable music credits -- demonstrating why open-source music attribution scaffolds must embed provenance before AI training rather than attempting reverse engineering afterward.](docs/figures/repo-figures/assets/fig-theory-03-attribution-by-design-vs-posthoc.jpg)

*Figure 3. Attribution-by-design versus post-hoc detection: the left panel shows how the oracle problem blocks reverse engineering of AI-generated output, while the right panel shows how embedding provenance with industry identifiers (ISRC, ISWC, ISNI) before training preserves queryable attribution.*

### From this figure plan (relative)

![Comparison chart: post-hoc detection with broken arrows leading to no answer versus attribution-by-design with embedded provenance at ISRC and ISWC assurance levels A0-A3 leading to queryable music credits -- demonstrating why open-source music attribution scaffolds must embed provenance before AI training rather than attempting reverse engineering afterward.](../assets/fig-theory-03-attribution-by-design-vs-posthoc.jpg)
