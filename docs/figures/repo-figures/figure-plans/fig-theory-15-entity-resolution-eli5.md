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

The key message is: "The same person appears with different names in different databases -- entity resolution figures out that 'I. Heap,' 'Imogen Heap,' and 'HEAP, IMOGEN' are all the same artist."

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
|  │  I. Heap   │  │  Imogen    │  │  HEAP,     │              |
|  │            │  │  Heap      │  │  IMOGEN    │              |
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
|  │  │  Imogen Heap                        │    │              |
|  │  │  ISNI: 0000 0001 1234 5678          │    │              |
|  │  │  Also known as: I. Heap, HEAP       │    │              |
|  │  │  IMOGEN, Imogen J. Heap             │    │              |
|  │  └─────────────────────────────────────┘    │              |
|  └─────────────────────────────────────────────┘              |
|                                                                |
|  WHERE THE NAMES COME FROM:                                    |
|  ──────────────────────────                                    |
|                                                                |
|  ┌───────────┐  ┌───────────┐  ┌───────────┐                 |
|  │ MusicBrainz│  │  Discogs   │  │ File Tag  │                 |
|  │ "Imogen   │  │ "HEAP,    │  │ "I. Heap" │                 |
|  │  Heap"    │  │  IMOGEN"  │  │           │                 |
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
| Name tag 1 | `source_musicbrainz` | "HELLO my name is I. Heap" -- abbreviated form |
| Name tag 2 | `source_artist` | "HELLO my name is Imogen Heap" -- full name |
| Name tag 3 | `source_discogs` | "HELLO my name is HEAP, IMOGEN" -- inverted form |
| Convergence arrows | `data_flow` | Three arrows pointing from name tags to unified record |
| Unified person record | `primary_outcome` | Single card: "Imogen Heap" with ISNI and aliases listed |
| ISNI identifier | `data_mono` | "ISNI: 0000 0001 1234 5678" in monospace (illustrative) |
| Source attribution row | `processing_stage` | Three source boxes showing where each name variant originates |
| MusicBrainz source | `source_musicbrainz` | "Imogen Heap" -- canonical name |
| Discogs source | `source_discogs` | "HEAP, IMOGEN" -- inverted catalog format |
| File tag source | `source_file` | "I. Heap" -- abbreviated ID3 tag |
| Footer callout | `callout_box` | Entity resolution ensures the right person gets credited and paid |

## Anti-Hallucination Rules

1. The example artist is Imogen Heap -- this is the project persona. Do NOT use a different artist.
2. Name variants shown: "I. Heap," "Imogen Heap," "HEAP, IMOGEN." These are representative formats.
3. The ISNI number "0000 0001 1234 5678" is ILLUSTRATIVE -- do NOT claim it is Imogen Heap's real ISNI.
4. Do NOT use technical terms like "fuzzy matching," "Levenshtein distance," or "embeddings" -- this is L1.
5. The "conference name tag" analogy is specific -- do NOT switch to a different analogy.
6. The payoff is "credited and paid" -- always connect entity resolution to real-world consequences.
7. Sources are MusicBrainz, Discogs, and file tags -- do NOT add other sources in this figure.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Three conference name tags showing I. Heap, Imogen Heap, and HEAP IMOGEN converging to a single unified person record with ISNI identifier and source attributions.
