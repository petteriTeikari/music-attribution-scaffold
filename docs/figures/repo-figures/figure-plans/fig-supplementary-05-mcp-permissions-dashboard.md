# fig-supplementary-05: MCP Permissions Dashboard

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-supplementary-05 |
| **Title** | MCP Permissions Dashboard |
| **Audience** | L1 (Music Industry Professional) |
| **Location** | Supplementary materials, docs/figures/repo-figures/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:10 |
| **Layout Template** | A (Hero) |
| **Medium** | Frontend screenshot |

## Purpose

Shows the MCP permissions management interface where rights holders set per-work, per-use permissions. Answers: "How do rights holders control AI use of their music through the scaffold's consent infrastructure?"

## Key Message

The permissions dashboard lets rights holders control AI use of their music with granular per-work, per-use-type permissions -- streaming (allow), AI training (deny), remix (conditional).

## Visual Concept

Full browser screenshot of the permissions page showing per-work permission profiles with toggle-style controls for different use types, color-coded by permission state (ALLOW green, DENY red, CONDITIONS amber).

```
+--+----------------------------------------------------------+
|  |  PERMISSIONS                                              |
|S |  ■ Machine-Readable Consent                               |
|I |                                                           |
|D |  ─────────────────────────────────────────────────        |
|E |  Hide and Seek                                            |
|B |    Streaming       ● ALLOW                                |
|A |    Sync License    ● ALLOW                                |
|R |    Download        ● CONDITIONS                           |
|  |    AI Training     ○ DENY                                 |
|  |    Voice Cloning   ○ DENY                                 |
|  |  ─────────────────────────────────────────────────        |
|  |  Goodnight and Go                                         |
|  |    Streaming       ● ALLOW                                |
|  |    Sync License    ● CONDITIONS                           |
|  |    Download        ● ALLOW                                |
|  |    AI Training     ○ DENY                                 |
|  |    Voice Cloning   ○ DENY                                 |
|  |  ─────────────────────────────────────────────────        |
|  |  Headlock                                                 |
|  |    Streaming       ● ALLOW                                |
|  |    Sync License    ● ALLOW                                |
|  |    Download        ● ALLOW                                |
|  |    AI Training     ● CONDITIONS                           |
|  |    Voice Cloning   ○ DENY                                 |
|  |  ─────────────────────────────────────────────────        |
+--+----------------------------------------------------------+
```

## Screenshot Specification

| Parameter | Value |
|-----------|-------|
| **Browser** | Chrome / headless Chromium |
| **Viewport** | 1440 x 900 px |
| **Theme** | Light |
| **URL** | `localhost:3000/permissions` |
| **State** | Permissions page with at least 3 works showing different permission profiles |
| **Annotations** | Optional -- callout on permission toggles |
| **Device pixel ratio** | 1x (standard) |
| **Font loading** | Wait for all three font families to load |
| **Network** | Mock data loaded, no loading skeletons visible |
| **Scroll position** | Top of page, showing at least 3 work permission blocks |

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Page heading | `heading_display` | "PERMISSIONS" in Instrument Serif |
| Subtitle | `label_editorial` | "Machine-Readable Consent" |
| Work permission blocks | `content_row` | Per-work grouped permission controls |
| Work title | `label_primary` | Work name heading each permission block |
| Use type labels | `label_secondary` | Streaming, Sync License, Download, AI Training, Voice Cloning |
| Permission state indicators | `permission_state` | Color-coded: ALLOW (green), DENY (red), CONDITIONS (amber) |
| Permission toggles | `action_toggle` | Interactive controls for setting permission state |
| Divider lines | `accent_line` | Horizontal dividers between work blocks |
| Sidebar | `navigation` | 60px fixed left sidebar |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Permission toggles | MCP server | arrow | "machine-readable via check_permissions" |
| Rights holder action | Permission state | arrow | "sets per-work, per-use permission" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "MCP CONSENT" | Optional annotation showing permissions are machine-readable preferences | top-right |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "MCP Permissions Dashboard"
- Label 2: "Per-Work Consent Controls"
- Label 3: "ALLOW / DENY / CONDITIONS"
- Label 4: "Machine-Readable Preferences"

### Caption (for embedding in documentation)

The MCP permissions dashboard enables rights holders to set granular per-work, per-use-type consent (streaming, sync license, download, AI training, voice cloning) with three permission states -- ALLOW, DENY, and CONDITIONS -- served as machine-readable preferences via the MCP check_permissions tool.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `permission_state`, `action_toggle`, `content_row` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. **This is a SCREENSHOT, not AI-generated.** Do NOT use Nano Banana Pro for this figure.
10. **Do NOT mock the screenshot** -- capture actual running frontend at localhost:3000/permissions.
11. Permission use types: streaming, sync license, download, AI training, voice cloning (from fig-theory-22 permission matrix).
12. Permission states: ALLOW (green), DENY (red), CONDITIONS (amber).
13. The MCP server provides machine-readable consent via the `check_permissions` tool.
14. **Do NOT claim permissions are legally binding** -- they are machine-readable preferences, not legal contracts.
15. Show at least 3 works with different permission profiles to demonstrate the variety of consent configurations.

## Alt Text

Permissions dashboard screenshot: per-work AI use controls with allow/deny/conditional states

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "supplementary-05",
    "title": "MCP Permissions Dashboard",
    "audience": "L1",
    "layout_template": "A",
    "medium": "frontend_screenshot"
  },
  "content_architecture": {
    "primary_message": "Rights holders control AI use with granular per-work, per-use-type permissions via the MCP consent infrastructure.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Work Permission Blocks",
        "role": "content_row",
        "is_highlighted": true,
        "labels": ["Per-work groups", "5 use types each"]
      },
      {
        "name": "Permission State Indicators",
        "role": "permission_state",
        "is_highlighted": true,
        "labels": ["ALLOW", "DENY", "CONDITIONS"]
      },
      {
        "name": "Use Type Labels",
        "role": "label_secondary",
        "is_highlighted": false,
        "labels": ["Streaming", "Sync License", "Download", "AI Training", "Voice Cloning"]
      }
    ],
    "relationships": [
      {
        "from": "Permission Toggle",
        "to": "MCP Server",
        "type": "arrow",
        "label": "machine-readable via check_permissions"
      }
    ],
    "callout_boxes": []
  },
  "screenshot_spec": {
    "browser": "Chrome/headless",
    "viewport": "1440x900",
    "theme": "light",
    "url": "localhost:3000/permissions",
    "state": "3+ works with different permission profiles",
    "annotations": "optional callout on permission toggles"
  }
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Screenshot specification defined (replaces spatial anchors)
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed (8 default + 7 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L1)
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Frontend running and screenshot captured
- [ ] Quality reviewed
- [ ] Embedded in supplementary materials
