# fig-theory-15: Entity Resolution -- ELI5 (Name Tag Analogy)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-15 |
| **Title** | Entity Resolution -- ELI5 (Name Tag Analogy) |
| **Audience** | L1 (Music Industry Professional) |
| **Complexity** | L1 (concept introduction -- no code, real-world analogy) |
| **Location** | docs/theory/entity-resolution.md, README.md theory section |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure introduces entity resolution -- the process of recognizing that different name variations refer to the same person -- using the analogy of name tags at a conference. It answers: "Why do databases disagree about who made a song, and how do we fix it?"

The key message is: "The same person appears with different names in different databases -- entity resolution figures out that 'E. Voss,' 'Elena Voss,' and 'VOSS, ELENA' are all the same artist."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  ENTITY RESOLUTION                                             |
|  ■ Same Person, Different Name Tags                            |
+---------------------------------------------------------------+
|                                                                |
|  THE PROBLEM: CONFERENCE NAME TAGS                             |
|  ────────────────────────────────                              |
|                                                                |
|  ┌────────────┐  ┌────────────┐  ┌────────────┐              |
|  │            │  │            │  │            │              |
|  │  HELLO     │  │  HELLO     │  │  HELLO     │              |
|  │  my name is│  │  my name is│  │  my name is│              |
|  │            │  │            │  │            │              |
|  │  E. Voss   │  │  Elena     │  │  VOSS,     │              |
|  │            │  │  Voss      │  │  ELENA     │              |
|  │            │  │            │  │            │              |
|  └──────┬─────┘  └──────┬─────┘  └──────┬─────┘              |
|         │               │               │                     |
|         │       ┌───────┘               │                     |
|         │       │                       │                     |
|         ▼       ▼                       ▼                     |
|  ┌─────────────────────────────────────────────┐              |
|  │              SAME PERSON                     │              |
|  │              ───────────                     │              |
|  │  ┌─────────────────────────────────────┐    │              |
|  │  │  Elena Voss                        │    │              |
|  │  │  ISNI: 0000 0001 1234 5678          │    │              |
|  │  │  Also known as: E. Voss, VOSS       │    │              |
|  │  │  ELENA, Elena K. Voss              │    │              |
|  │  └─────────────────────────────────────┘    │              |
|  └─────────────────────────────────────────────┘              |
|                                                                |
|  WHERE THE NAMES COME FROM:                                    |
|  ──────────────────────────                                    |
|                                                                |
|  ┌───────────┐  ┌───────────┐  ┌───────────┐                 |
|  │ MusicBrainz│  │  Discogs   │  │ File Tag  │                 |
|  │ "Elena    │  │ "VOSS,    │  │ "E. Voss" │                 |
|  │  Voss"    │  │  ELENA"   │  │           │                 |
|  └───────────┘  └───────────┘  └───────────┘                 |
|                                                                |
+---------------------------------------------------------------+
|  ■ Entity resolution connects these name tags so the right     |
|    person gets credited -- and paid.                           |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ENTITY RESOLUTION" with coral accent square |
| Subtitle | `label_editorial` | "Same Person, Different Name Tags" |
| Name tag 1 | `source_musicbrainz` | "HELLO my name is E. Voss" -- abbreviated form |
| Name tag 2 | `source_artist` | "HELLO my name is Elena Voss" -- full name |
| Name tag 3 | `source_discogs` | "HELLO my name is VOSS, ELENA" -- inverted form |
| Convergence arrows | `data_flow` | Three arrows pointing from name tags to unified record |
| Unified person record | `primary_outcome` | Single card: "Elena Voss" with ISNI and aliases listed |
| ISNI identifier | `data_mono` | "ISNI: 0000 0001 1234 5678" in monospace (illustrative) |
| Source attribution row | `processing_stage` | Three source boxes showing where each name variant originates |
| MusicBrainz source | `source_musicbrainz` | "Elena Voss" -- canonical name |
| Discogs source | `source_discogs` | "VOSS, ELENA" -- inverted catalog format |
| File tag source | `source_file` | "E. Voss" -- abbreviated ID3 tag |
| Footer callout | `callout_box` | Entity resolution ensures the right person gets credited and paid |

## Anti-Hallucination Rules

1. The example artist is Elena Voss -- a FICTIONAL artist name chosen to avoid image generation content filters. Do NOT use a different artist.
2. Name variants shown: "E. Voss," "Elena Voss," "VOSS, ELENA." These are representative formats.
3. The ISNI number "0000 0001 1234 5678" is ILLUSTRATIVE -- do NOT claim it is a real ISNI.
4. Do NOT use technical terms like "fuzzy matching," "Levenshtein distance," or "embeddings" -- this is L1.
5. The "conference name tag" analogy is specific -- do NOT switch to a different analogy.
6. The payoff is "credited and paid" -- always connect entity resolution to real-world consequences.
7. Sources are MusicBrainz, Discogs, and file tags -- do NOT add other sources in this figure.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Concept diagram: three conference name tags showing name variants E. Voss, Elena Voss, and VOSS ELENA from different music metadata sources converging to a single unified person record with ISNI identifier -- illustrating entity resolution for music attribution where the same artist appears differently across MusicBrainz, Discogs, and file tags, ensuring correct music credits and payment.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Concept diagram: three conference name tags showing name variants E. Voss, Elena Voss, and VOSS ELENA from different music metadata sources converging to a single unified person record with ISNI identifier -- illustrating entity resolution for music attribution where the same artist appears differently across MusicBrainz, Discogs, and file tags, ensuring correct music credits and payment.](docs/figures/repo-figures/assets/fig-theory-15-entity-resolution-eli5.jpg)

*Figure 15. Entity resolution explained through a conference name tag analogy: the same artist appears as "E. Voss," "Elena Voss," and "VOSS, ELENA" across different databases, and entity resolution connects these variants so the right person gets credited and paid.*

### From this figure plan (relative)

![Concept diagram: three conference name tags showing name variants E. Voss, Elena Voss, and VOSS ELENA from different music metadata sources converging to a single unified person record with ISNI identifier -- illustrating entity resolution for music attribution where the same artist appears differently across MusicBrainz, Discogs, and file tags, ensuring correct music credits and payment.](../assets/fig-theory-15-entity-resolution-eli5.jpg)
