# fig-choice-13: Why tinytag over mutagen?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-13 |
| **Title** | Why tinytag over mutagen? |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/L3-implementation/audio-metadata-library.decision.yaml |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the audio metadata library decision. The scaffold chose tinytag (BSD-3 license) over mutagen (GPL-2.0 license). This is primarily a LICENSE decision -- GPL-2.0 would force the entire scaffold to be GPL-licensed, conflicting with the open-source research scaffold goal. tinytag reads standard metadata fields (title, artist, album, duration, ISRC) without write capabilities -- sufficient for the ETL pipeline's needs.

The key message is: "tinytag's BSD-3 license preserves the scaffold's permissive licensing -- mutagen's GPL-2.0 would force copyleft on the entire project."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY TINYTAG OVER MUTAGEN?                                     |
|  ■ Audio Metadata Library: License-Driven Decision             |
+-------------------------------+-------------------------------+
|                               |                               |
|  TINYTAG (selected)           |  MUTAGEN                      |
|  ═══════════════════          |  ═══════                      |
|                               |                               |
|  License: BSD-3-Clause        |  License: GPL-2.0             |
|  ■ Permissive                 |  ■ Copyleft                   |
|  ■ No viral licensing         |  ■ Forces entire project      |
|  ■ Compatible with scaffold   |  ■ to be GPL-licensed         |
|                               |                               |
|  Features:                    |  Features:                    |
|  ■ Read-only metadata         |  ■ Read + Write metadata      |
|  ■ ID3, Vorbis, FLAC, MP4   |  ■ Full format support        |
|  ■ Title, artist, album      |  ■ TIPL credits, custom tags  |
|  ■ Duration, ISRC            |  ■ Complete editing            |
|                               |                               |
|  Limitations:                 |  Limitations:                 |
|  ■ No write support           |  ■ GPL viral clause           |
|  ■ No TIPL (credits list)    |  ■ Heavy dependency tree      |
|  ■ Basic field extraction     |                               |
|                               |                               |
|  Size: ~50KB                  |  Size: ~2MB                   |
|  Dependencies: zero           |  Dependencies: multiple       |
|                               |                               |
+-------------------------------+-------------------------------+
|  PRD Node: audio_metadata_library = tinytag_bsd (selected)     |
|  Issue: #29 closed (mutagen → tinytag license swap)            |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY TINYTAG OVER MUTAGEN?" with coral accent square |
| tinytag panel (left) | `selected_option` | BSD-3 license, read-only, zero dependencies |
| mutagen panel (right) | `deferred_option` | GPL-2.0, read+write, full feature set |
| License comparison | `feature_list` | Permissive vs copyleft with implications |
| Feature comparison | `feature_list` | Read-only vs full editing capabilities |
| Size comparison | `data_mono` | ~50KB vs ~2MB |
| PRD reference footer | `callout_bar` | Decision node and issue number |

## Anti-Hallucination Rules

1. tinytag license is BSD-3-Clause -- permissive.
2. mutagen license is GPL-2.0 -- copyleft, forces derivative works to be GPL.
3. The license swap was tracked in Issue #29, which is closed.
4. tinytag is READ-ONLY -- it cannot write/modify audio file metadata.
5. tinytag supports ID3 (MP3), Vorbis (OGG), FLAC, MP4/M4A formats.
6. tinytag does NOT support TIPL (credits list) -- this is an acknowledged limitation.
7. The PRD decision node is `audio_metadata_library` added in v1.7.0.
8. The data model complexity decision influences this: complex models may need TIPL credits (mutagen), but standard fields suffice for MVP.
9. Background must be warm cream (#f6f3e6).

## Alt Text

Split-panel comparison of tinytag and mutagen audio metadata libraries, highlighting BSD-3 versus GPL-2.0 licensing as the primary decision driver.
