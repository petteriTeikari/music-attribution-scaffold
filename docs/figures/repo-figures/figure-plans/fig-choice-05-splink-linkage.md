# fig-choice-05: Why Splink for Entity Linkage?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-05 |
| **Title** | Why Splink for Entity Linkage? |
| **Audience** | L4 (AI/ML Architect) |
| **Complexity** | L4 (algorithmic detail) |
| **Location** | docs/planning/, src/music_attribution/resolution/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains why the scaffold uses Splink (based on the Fellegi-Sunter model) for probabilistic record linkage in the entity resolution pipeline. Compares against dedupe.io (Python, active learning) and custom matching (exact + fuzzy rules). Splink provides Bayesian match weights with EM training, scales to millions of records via DuckDB/Spark backends, and produces interpretable match scores.

The key message is: "Splink implements Fellegi-Sunter probabilistic linkage with EM-trained match weights -- scalable, interpretable, and statistically principled entity resolution."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY SPLINK FOR ENTITY LINKAGE?                                |
|  ■ Fellegi-Sunter Model with EM-Trained Weights                |
+---------------------------------------------------------------+
|                                                                |
|  THE PROBLEM                                                   |
|  Same artist appears differently across sources:               |
|  MusicBrainz: "Bjork Gudmundsdottir"                          |
|  Discogs: "Bjork" | ID3: "bjork" | Label: "Bjork!"            |
|  Need: probabilistic matching, not exact string match          |
|                                                                |
|  FELLEGI-SUNTER MODEL                                          |
|  ┌─────────────────────────────────────────────────────────┐   |
|  │  For each field pair, compute:                          │   |
|  │  match_weight = log2(m/u) where                         │   |
|  │    m = P(agree | true match)                            │   |
|  │    u = P(agree | non-match)                             │   |
|  │  Total score = sum of field match weights               │   |
|  │  Classify: match (>upper) / non-match (<lower) / review │   |
|  └─────────────────────────────────────────────────────────┘   |
|                                                                |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ SPLINK       │ │ dedupe.io    │ │ CUSTOM RULES │          |
|  │ ■ SELECTED   │ │              │ │              │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Fellegi-     │ │ Active       │ │ Exact + fuzzy│          |
|  │ Sunter model │ │ learning     │ │ thresholds   │          |
|  │              │ │              │ │              │          |
|  │ EM-trained   │ │ Human-in-   │ │ Manual tuning│          |
|  │ weights      │ │ the-loop     │ │              │          |
|  │              │ │              │ │              │          |
|  │ DuckDB/Spark │ │ Python-only  │ │ Any backend  │          |
|  │ backends     │ │ in-memory    │ │              │          |
|  │              │ │              │ │              │          |
|  │ Interpretable│ │ Less         │ │ Not          │          |
|  │ match weights│ │ interpretable│ │ probabilistic│          |
|  │              │ │              │ │              │          |
|  │ Scales to    │ │ ~100K        │ │ Depends on   │          |
|  │ millions     │ │ records      │ │ implementation│          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
+---------------------------------------------------------------+
|  Splink v4 API: from splink import block_on (top-level)       |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY SPLINK FOR ENTITY LINKAGE?" with coral accent square |
| Problem statement | `problem_statement` | Same artist, different representations across sources |
| Fellegi-Sunter model box | `processing_stage` | Mathematical foundation: m/u parameters, match weights |
| Splink card | `selected_option` | EM-trained, scalable, interpretable |
| dedupe.io card | `deferred_option` | Active learning, human-in-the-loop, Python-only |
| Custom rules card | `deferred_option` | Manual thresholds, not probabilistic |
| API reference footer | `callout_bar` | Splink v4 import pattern |

## Anti-Hallucination Rules

1. Splink v4 import: `from splink import block_on` (top-level) -- NOT `splink.blocking_rules_library` (v3 pattern).
2. Fellegi-Sunter model uses m-probability (P agree given match) and u-probability (P agree given non-match).
3. Match weight formula: log2(m/u) for each comparison field.
4. Splink supports DuckDB, Spark, and other backends for scalability.
5. The artist name examples (Bjork variations) are illustrative -- they represent the real-world problem.
6. dedupe.io uses active learning for training -- it asks humans to label pairs.
7. Do NOT claim Splink is the only option -- the scaffold's entity resolution module could use other approaches.
8. The resolution pipeline is Stage II in the 5-pipeline architecture.
9. Background must be warm cream (#f6f3e6).

## Alt Text

Three-option comparison for entity linkage: Splink selected for Fellegi-Sunter probabilistic model with EM training and scalable backends, versus dedupe.io and custom rules.
