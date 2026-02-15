# fig-theory-16: Resolution Cascade

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-16 |
| **Title** | Resolution Cascade -- Five-Step Waterfall |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (code terms, module references, implementation flow) |
| **Location** | docs/theory/entity-resolution.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the five-step entity resolution cascade, from cheapest/fastest (identifier match) to most expensive (probabilistic Splink). It answers: "In what order does the system try to resolve whether two records refer to the same entity?"

The key message is: "Resolution is a waterfall of increasingly expensive methods -- exact identifier match first, then string similarity, then embeddings, then LLM, then probabilistic linking -- each step only fires if the previous one was inconclusive."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  RESOLUTION CASCADE                                            |
|  ■ Five Steps: Cheap First, Expensive Last                     |
+---------------------------------------------------------------+
|                                                                |
|  INPUT: Two records that might be the same entity              |
|  ───────────────────────────────────────────────               |
|       │                                                        |
|       ▼                                                        |
|  ┌──────────────────────────────────────────────┐              |
|  │  STEP 1: IDENTIFIER MATCH                    │              |
|  │  ─────────────────────────                   │              |
|  │  ISRC, ISWC, ISNI, IPI exact equality        │              |
|  │  Cost: ~0ms  │  Confidence: 0.99 if match    │              |
|  │  When: Both records have standard IDs        │              |
|  └────────────────────┬─────────────────────────┘              |
|        MATCH ─► DONE  │ INCONCLUSIVE                           |
|                       ▼                                        |
|  ┌──────────────────────────────────────────────┐              |
|  │  STEP 2: STRING SIMILARITY                   │              |
|  │  ─────────────────────────                   │              |
|  │  Normalized Levenshtein, Jaro-Winkler        │              |
|  │  Cost: ~1ms  │  Confidence: 0.70-0.95        │              |
|  │  When: Names available, no IDs               │              |
|  └────────────────────┬─────────────────────────┘              |
|        MATCH ─► DONE  │ INCONCLUSIVE                           |
|                       ▼                                        |
|  ┌──────────────────────────────────────────────┐              |
|  │  STEP 3: EMBEDDING MATCH                     │              |
|  │  ─────────────────────────                   │              |
|  │  Cosine similarity on name/context vectors   │              |
|  │  Cost: ~10ms │  Confidence: 0.60-0.90        │              |
|  │  When: String similarity ambiguous           │              |
|  └────────────────────┬─────────────────────────┘              |
|        MATCH ─► DONE  │ INCONCLUSIVE                           |
|                       ▼                                        |
|  ┌──────────────────────────────────────────────┐              |
|  │  STEP 4: LLM JUDGMENT                        │              |
|  │  ─────────────────                           │              |
|  │  Contextual reasoning with structured output │              |
|  │  Cost: ~500ms│  Confidence: 0.65-0.85        │              |
|  │  When: Embeddings disagree or low confidence │              |
|  └────────────────────┬─────────────────────────┘              |
|        MATCH ─► DONE  │ INCONCLUSIVE                           |
|                       ▼                                        |
|  ┌──────────────────────────────────────────────┐              |
|  │  STEP 5: SPLINK PROBABILISTIC                │              |
|  │  ─────────────────────────                   │              |
|  │  Fellegi-Sunter model, blocking + comparison │              |
|  │  Cost: ~50ms │  Confidence: 0.55-0.95        │              |
|  │  When: All above inconclusive, batch mode    │              |
|  └──────────────────────────────────────────────┘              |
|                                                                |
+---------------------------------------------------------------+
|  ■ Each step returns: MATCH (done) or INCONCLUSIVE (try next). |
|    Early exit saves cost. Total confidence = weighted blend.   |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "RESOLUTION CASCADE" with coral accent square |
| Subtitle | `label_editorial` | "Five Steps: Cheap First, Expensive Last" |
| Input description | `processing_stage` | "Two records that might be the same entity" |
| Step 1: Identifier Match | `entity_resolve` | ISRC/ISWC/ISNI/IPI exact equality, ~0ms, 0.99 confidence |
| Step 2: String Similarity | `entity_resolve` | Levenshtein/Jaro-Winkler, ~1ms, 0.70-0.95 confidence |
| Step 3: Embedding Match | `entity_resolve` | Cosine similarity on vectors, ~10ms, 0.60-0.90 confidence |
| Step 4: LLM Judgment | `entity_resolve` | Contextual reasoning, ~500ms, 0.65-0.85 confidence |
| Step 5: Splink Probabilistic | `entity_resolve` | Fellegi-Sunter model, ~50ms, 0.55-0.95 confidence |
| MATCH exit arrows | `data_flow` | Right-pointing arrows from each step labeled "MATCH -> DONE" |
| INCONCLUSIVE fall-through arrows | `data_flow` | Downward arrows between steps labeled "INCONCLUSIVE" |
| Cost labels | `data_mono` | Latency estimates in monospace: ~0ms, ~1ms, ~10ms, ~500ms, ~50ms |
| Confidence ranges | `data_mono` | Ranges in monospace: 0.99, 0.70-0.95, etc. |
| Footer callout | `callout_box` | Early exit saves cost; total confidence is weighted blend |

## Anti-Hallucination Rules

1. The five steps IN ORDER are: Identifier Match, String Similarity, Embedding Match, LLM Judgment, Splink Probabilistic. Do NOT reorder.
2. The cascade is a WATERFALL -- each step only fires if the previous was inconclusive. Do NOT show parallel execution.
3. Cost estimates (~0ms, ~1ms, ~10ms, ~500ms, ~50ms) are APPROXIMATE ORDER-OF-MAGNITUDE -- do NOT claim precision.
4. Confidence ranges are ILLUSTRATIVE -- do NOT present as exact calibrated values.
5. Splink uses the Fellegi-Sunter model -- do NOT reference other probabilistic frameworks.
6. String similarity methods are Levenshtein and Jaro-Winkler -- do NOT add or substitute others.
7. LLM judgment produces STRUCTURED OUTPUT -- do NOT imply free-text responses.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Waterfall diagram: five-step entity resolution cascade for music attribution -- identifier match at near zero cost, string similarity via Jaro-Winkler, embedding match via cosine similarity, LLM judgment with structured output, and Splink probabilistic linking via Fellegi-Sunter model -- each step fires only when the previous is inconclusive, optimizing transparent confidence scoring by trying the cheapest method first.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Waterfall diagram: five-step entity resolution cascade for music attribution -- identifier match at near zero cost, string similarity via Jaro-Winkler, embedding match via cosine similarity, LLM judgment with structured output, and Splink probabilistic linking via Fellegi-Sunter model -- each step fires only when the previous is inconclusive, optimizing transparent confidence scoring by trying the cheapest method first.](docs/figures/repo-figures/assets/fig-theory-16-resolution-cascade.jpg)

*Figure 16. The resolution cascade: entity resolution proceeds from cheapest to most expensive -- exact identifier match (ISRC/ISWC), string similarity, embedding cosine distance, LLM contextual reasoning, and Splink probabilistic linking -- with early exit on match to minimize cost while maintaining confidence.*

### From this figure plan (relative)

![Waterfall diagram: five-step entity resolution cascade for music attribution -- identifier match at near zero cost, string similarity via Jaro-Winkler, embedding match via cosine similarity, LLM judgment with structured output, and Splink probabilistic linking via Fellegi-Sunter model -- each step fires only when the previous is inconclusive, optimizing transparent confidence scoring by trying the cheapest method first.](../assets/fig-theory-16-resolution-cascade.jpg)
