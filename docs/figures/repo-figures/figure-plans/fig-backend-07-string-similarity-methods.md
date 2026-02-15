# fig-backend-07: String Similarity Methods

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-07 |
| **Title** | String Similarity: Jaro-Winkler vs Token Sort Ratio |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/resolution/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure compares the two string similarity algorithms used in entity resolution -- Jaro-Winkler (via jellyfish) and token sort ratio (via thefuzz). It shows when each method excels, the normalization pipeline applied before comparison, and the score combination strategy.

The key message is: "Two complementary methods handle different failure modes -- Jaro-Winkler catches typos in short strings, token sort ratio handles word reordering. The matcher takes the maximum of both scores, with a configurable threshold of 0.85."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  STRING SIMILARITY MATCHING                                    |
|  ■ Fuzzy Matching for Music Entity Names                       |
+---------------------------------------------------------------+
|                                                                 |
|  INPUT NORMALIZATION PIPELINE                                  |
|  ────────────────────────────                                  |
|  Raw name ──> NFD Unicode ──> Strip accents ──> lowercase      |
|          ──> "The" prefix fix ──> Expand abbreviations         |
|          ──> Normalize whitespace                              |
|                                                                 |
|  ABBREVIATION MAP                                              |
|  "feat." -> "featuring"    "prod." -> "produced by"            |
|  "ft."   -> "featuring"    "arr."  -> "arranged by"            |
|  "vs."   -> "versus"       "orch." -> "orchestra"              |
|  "w/"    -> "with"                                             |
|                                                                 |
|  ─────────────────────────────────────────────────────         |
|                                                                 |
|  JARO-WINKLER                 TOKEN SORT RATIO                 |
|  (jellyfish)                  (thefuzz / fuzz)                 |
|  ────────────                 ─────────────────                |
|  Best for:                    Best for:                        |
|  ■ Short strings              ■ Word reordering               |
|  ■ Single-char typos          ■ Different word order           |
|  ■ Prefix similarity          ■ Extra/missing words            |
|                                                                 |
|  Example:                     Example:                         |
|  "Bjork" vs "Bjork"  = 1.0   "John Paul Jones"                |
|  "Bjork" vs "Bjrok"  = 0.93  vs "Jones, John Paul"  = 1.0     |
|  "Imogen" vs "Imojen" = 0.91 "feat. Jay-Z"                    |
|                               vs "Jay-Z featuring" = high      |
|                                                                 |
|  ─────────────────────────────────────────────────────         |
|                                                                 |
|  COMBINATION: score = max(jaro_winkler, token_sort / 100)      |
|  THRESHOLD: >= 0.85 is a match                                 |
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "STRING SIMILARITY MATCHING" |
| Normalization pipeline | `processing_stage` | Sequential text normalization steps |
| Abbreviation map | `data_mono` | Music-domain abbreviation expansions |
| Jaro-Winkler column | `entity_resolve` | Algorithm characteristics and examples |
| Token Sort Ratio column | `entity_resolve` | Algorithm characteristics and examples |
| Library names | `data_mono` | "jellyfish" and "thefuzz" in monospace |
| Example scores | `data_mono` | Similarity scores for example pairs |
| Combination formula | `final_score` | max(jaro_winkler, token_sort / 100) |
| Threshold | `confidence_high` | 0.85 threshold indicator |
| Accent dividers | `accent_line` | Coral lines separating sections |

## Anti-Hallucination Rules

1. The two algorithms are Jaro-Winkler (jellyfish.jaro_winkler_similarity) and token sort ratio (fuzz.token_sort_ratio). No other algorithms are used.
2. The combination strategy is max(), not average or weighted sum.
3. Token sort ratio returns 0-100 and is divided by 100.0 in the code.
4. Default match threshold is 0.85, not 0.8 or 0.9.
5. The normalization includes exactly these steps: NFD unicode, strip accents, lowercase, "The" prefix handling, abbreviation expansion, whitespace normalization.
6. The abbreviation map has exactly 10 entries as defined in _ABBREVIATIONS.
7. The class is StringSimilarityMatcher in `music_attribution.resolution.string_similarity`.
8. "Beatles, The" is normalized to "the beatles" (specific comma-suffix handling).

## Alt Text

Comparison diagram of two string similarity algorithms for music attribution entity resolution — Jaro-Winkler (via jellyfish) for typo detection in short names and token sort ratio (via thefuzz) for word reordering — with a music-domain normalization pipeline expanding abbreviations like "feat." and "prod.", using the maximum of both scores at a 0.85 match threshold for transparent confidence scoring of music credits.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Comparison diagram of two string similarity algorithms for music attribution entity resolution — Jaro-Winkler (via jellyfish) for typo detection in short names and token sort ratio (via thefuzz) for word reordering — with a music-domain normalization pipeline expanding abbreviations like "feat." and "prod.", using the maximum of both scores at a 0.85 match threshold for transparent confidence scoring of music credits.](docs/figures/repo-figures/assets/fig-backend-07-string-similarity-methods.jpg)

*Figure 7. Two complementary string similarity methods handle different failure modes in music metadata: Jaro-Winkler catches single-character typos while token sort ratio handles name reordering, both preceded by domain-specific normalization of music abbreviations.*

### From this figure plan (relative)

![Comparison diagram of two string similarity algorithms for music attribution entity resolution — Jaro-Winkler (via jellyfish) for typo detection in short names and token sort ratio (via thefuzz) for word reordering — with a music-domain normalization pipeline expanding abbreviations like "feat." and "prod.", using the maximum of both scores at a 0.85 match threshold for transparent confidence scoring of music credits.](../assets/fig-backend-07-string-similarity-methods.jpg)
