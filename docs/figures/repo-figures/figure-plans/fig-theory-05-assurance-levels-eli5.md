# fig-theory-05: Assurance Levels A0-A3 -- ELI5 (ID Card Analogy)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-05 |
| **Title** | Assurance Levels A0-A3 -- ELI5 (ID Card Analogy) |
| **Audience** | L1 (Music Industry Professional) |
| **Complexity** | L1 (concept introduction -- no code, real-world analogy) |
| **Location** | docs/theory/assurance-levels.md, README.md theory section |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure introduces the four assurance levels (A0-A3) using an everyday analogy: different forms of identification. It answers: "How do we measure how much we trust a piece of attribution data?"

The key message is: "Trust comes in levels -- from 'no ID' to 'biometric scan' -- and each attribution claim carries a trust level that tells you how verified it really is."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  ASSURANCE LEVELS                                              |
|  ■ How Much Can You Trust This Credit?                         |
+---------------------------------------------------------------+
|                                                                |
|                                        ┌──────────────────┐   |
|                                        │  A3: BIOMETRIC   │   |
|                                        │  SCAN            │   |
|                               ┌────────│                  │   |
|                               │        │  "The artist     │   |
|                      ┌────────┤        │   verified it    │   |
|                      │        │        │   themselves"    │   |
|             ┌────────┤        │        └──────────────────┘   |
|             │        │        │                               |
|  ┌──────────┤        │  ┌─────┴──────────┐                   |
|  │          │        │  │  A2: PASSPORT   │                   |
|  │  ┌───────┴──────┐│  │                 │                   |
|  │  │ A1: BUSINESS ││  │  "Multiple      │                   |
|  │  │ CARD         ││  │   sources       │                   |
|  │  │              ││  │   agree"        │                   |
|  │  │ "Someone     ││  └────────────────┘                    |
|  │  │  claims it"  ││                                        |
|  │  └──────────────┘│                                        |
|  │                   │                                        |
|  │ ┌──────────────┐  │                                        |
|  │ │ A0: STICKY   │  │                                        |
|  │ │ NOTE         │  │                                        |
|  │ │              │  │                                        |
|  │ │ "No ID at    │  │                                        |
|  │ │  all"        │  │                                        |
|  │ └──────────────┘  │                                        |
|  │                   │                                        |
|  └───────────────────┘                                        |
|   LESS TRUST ◄─────────────────────────────► MORE TRUST       |
|                                                                |
+---------------------------------------------------------------+
|  ■ Every credit in every song carries one of these levels.     |
|    Higher = more evidence. A3 = the artist said "yes, that's   |
|    me."                                                        |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ASSURANCE LEVELS" with coral accent square |
| Subtitle | `label_editorial` | "How Much Can You Trust This Credit?" |
| A0 step | `assurance_a0` | Sticky note -- "No ID at all" -- lowest trust, gray-coded |
| A1 step | `assurance_a1` | Business card -- "Someone claims it" -- single source, amber-coded |
| A2 step | `assurance_a2` | Passport -- "Multiple sources agree" -- corroborated, blue-coded |
| A3 step | `assurance_a3` | Biometric scan -- "The artist verified it themselves" -- highest trust, green-coded |
| Staircase structure | `processing_stage` | Four ascending steps showing increasing trust |
| Trust spectrum bar | `data_flow` | Horizontal bar from "LESS TRUST" to "MORE TRUST" |
| Footer callout | `callout_box` | Plain-English explanation that every credit carries a level |

## Anti-Hallucination Rules

1. Assurance levels are A0, A1, A2, A3 -- exactly four levels, always starting at A0.
2. A0 = no data, A1 = single source claim, A2 = multiple sources agree, A3 = artist-verified. Do NOT alter these definitions.
3. The ID card analogy maps: sticky note (A0), business card (A1), passport (A2), biometric scan (A3). Do NOT change the analogies.
4. Do NOT use technical terms like "corroborated" or "provenance" -- this is L1, use plain language.
5. Do NOT include ISRC, ISWC, ISNI codes -- those belong in fig-theory-06.
6. Do NOT reference the analog hole or Oracle Problem -- this figure is purely about the trust levels.
7. The staircase must show ASCENDING trust from A0 to A3 -- never descending.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Concept diagram: four-step staircase showing music attribution assurance levels A0 through A3 using ID card analogies -- A0 as sticky note with no identification, A1 as business card with a single claim, A2 as passport with multiple sources agreeing, A3 as biometric scan with direct artist verification -- illustrating how transparent confidence scoring grades trust in music credits.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Concept diagram: four-step staircase showing music attribution assurance levels A0 through A3 using ID card analogies -- A0 as sticky note with no identification, A1 as business card with a single claim, A2 as passport with multiple sources agreeing, A3 as biometric scan with direct artist verification -- illustrating how transparent confidence scoring grades trust in music credits.](docs/figures/repo-figures/assets/fig-theory-05-assurance-levels-eli5.jpg)

*Figure 5. Assurance levels A0-A3 explained through everyday ID card analogies: every attribution claim carries a trust level from no data (A0) to artist-verified (A3), enabling music industry professionals to assess how much evidence supports each music credit.*

### From this figure plan (relative)

![Concept diagram: four-step staircase showing music attribution assurance levels A0 through A3 using ID card analogies -- A0 as sticky note with no identification, A1 as business card with a single claim, A2 as passport with multiple sources agreeing, A3 as biometric scan with direct artist verification -- illustrating how transparent confidence scoring grades trust in music credits.](../assets/fig-theory-05-assurance-levels-eli5.jpg)
