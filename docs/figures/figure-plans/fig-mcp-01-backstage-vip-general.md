# fig-mcp-01: Backstage, VIP, General

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-mcp-01 |
| **Title** | Backstage, VIP, General Admission |
| **Gallery** | Contextual Galleries (docs/prd/mcp-server-prd.md) |
| **Audience** | Business stakeholders, potential API partners |
| **Template** | E2: Fashion Photography Collage |
| **Texture** | Magazine tear sheet, glossy/matte mix, bold typography |

---

## Narrative Position

**The Three-Tier Trust Model: Access Control as Venue Security**

This figure explains the MCP server's three-tier access control using the universal metaphor of concert venue access: Backstage (internal), VIP (verified partners), and General Admission (public API).

---

## Why Should I Care?

> "This determines who gets access to your data—and how much."

## Explain It to a Label Exec

> "Think of it like concert security: backstage access for our own team, VIP passes for verified partners like JenMusic, and general admission for everyone else—with strict limits at each level."

---

## Mogen/Andy Personalization

**Connecting to their real experience:**
- Mogen and Andy have toured for 20+ years—they UNDERSTAND venue access tiers intimately
- **Tier 1 (Backstage)**: system internal apps - "where the artist can see everything"
- **Tier 2 (VIP)**: Partners like JenMusic AI - verified, ethical, with negotiated access
- **Tier 3 (General)**: Unknown API consumers - rate-limited, read-only, anonymous

**Visual reference:**
- Use concert/festival aesthetic that Mogen would recognize from her performances
- Backstage passes, VIP laminates, wristbands as visual elements

---

## Visual Concept

**Style: Fashion photography collage meets concert production**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   ╔══════════════════════════════════════════════════════════════════════╗  │
│   ║    B A C K S T A G E   /   V I P   /   G E N E R A L                 ║  │
│   ║             The Three-Tier Trust Model                                ║  │
│   ╚══════════════════════════════════════════════════════════════════════╝  │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   ┌───────────────┐                                                 │   │
│   │   │               │   T I E R   1 :   B A C K S T A G E            │   │
│   │   │  [BACKSTAGE   │                                                 │   │
│   │   │   LAMINATE]   │   • Full access to all data                    │   │
│   │   │               │   • system internal apps                      │   │
│   │   │   ALL ACCESS  │   • No rate limits                             │   │
│   │   │               │   • Write permissions                          │   │
│   │   │   ATTRIBUTION    │                                                 │   │
│   │   │   INTERNAL    │   "Where the artist can see everything"        │   │
│   │   │               │                                                 │   │
│   │   └───────────────┘                                                 │   │
│   │                                                                      │   │
│   │   ─────────────────── SECURITY CHECK ───────────────────            │   │
│   │                                                                      │   │
│   │   ┌───────────────┐                                                 │   │
│   │   │               │   T I E R   2 :   V I P                         │   │
│   │   │  [VIP PASS]   │                                                 │   │
│   │   │               │   • Read access + scoped write                  │   │
│   │   │   VERIFIED    │   • 1000 requests/hour                         │   │
│   │   │   PARTNER     │   • Verified ethical AI companies              │   │
│   │   │               │                                                 │   │
│   │   │   JenMusic    │   Example: JenMusic AI (Verified Partner)      │   │
│   │   │   AI          │   "Trusted collaborators with negotiated       │   │
│   │   │               │    access"                                      │   │
│   │   └───────────────┘                                                 │   │
│   │                                                                      │   │
│   │   ─────────────────── SECURITY CHECK ───────────────────            │   │
│   │                                                                      │   │
│   │   ┌───────────────┐                                                 │   │
│   │   │               │   T I E R   3 :   G E N E R A L                 │   │
│   │   │  [WRISTBAND]  │                                                 │   │
│   │   │               │   • Read-only access                           │   │
│   │   │   GENERAL     │   • 100 requests/hour                          │   │
│   │   │   ADMISSION   │   • Anonymous or unverified clients            │   │
│   │   │               │                                                 │   │
│   │   │   PUBLIC      │   "Everyone else—limited view, no touching"    │   │
│   │   │   API         │                                                 │   │
│   │   └───────────────┘                                                 │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  "Your data, your rules. We just make sure the right people         │   │
│   │   get the right level of access."                                   │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Content Elements

| Element | Semantic Role | Visual Treatment |
|---------|---------------|------------------|
| Backstage laminate | Tier 1 visual | Cut-out photo of actual backstage pass |
| VIP pass | Tier 2 visual | Gold/special laminate style |
| General wristband | Tier 3 visual | Festival wristband |
| Security check lines | Tier boundaries | Bold horizontal dividers |
| Access details | Technical specs | Clean typography lists |
| Quote callout | Value proposition | Bottom strip |

---

## Text Content (Max 30 chars each)

### Labels
- "TIER 1: BACKSTAGE"
- "TIER 2: VIP"
- "TIER 3: GENERAL"
- "ALL ACCESS"
- "VERIFIED PARTNER"
- "GENERAL ADMISSION"
- "ATTRIBUTION INTERNAL"
- "JenMusic AI"
- "PUBLIC API"

### Access Details
- Tier 1: "Full access, no limits, write"
- Tier 2: "Read + scoped write, 1000/hr"
- Tier 3: "Read-only, 100/hr, anonymous"

### Quotes
- Tier 1: "Where the artist sees everything"
- Tier 2: "Trusted collaborators"
- Tier 3: "Limited view, no touching"
- Bottom: "Your data, your rules"

### Caption
The three-tier trust model for MCP API access, visualized as concert venue security: Backstage (Tier 1) for the system internal apps with full access, VIP (Tier 2) for verified partners like JenMusic with negotiated permissions, and General Admission (Tier 3) for public API consumers with read-only, rate-limited access.

---

## Style-Specific Prompt

```
Create a fashion photography collage showing three access tiers as concert venue passes.

STYLE: Magazine editorial collage meets concert production
- Cut-out photos of real access passes/laminates
- Bold typography overlay (concert poster aesthetic)
- High contrast black & white with gold/color accents
- Magazine tear sheet aesthetic
- Glossy laminate texture on passes

COMPOSITION - Vertical stack of three tiers:

TIER 1 (Top - Backstage):
- Large backstage laminate pass (black with gold "ALL ACCESS")
- Navy blue (#1E3A5F) accent color
- Text: "ATTRIBUTION INTERNAL"
- Bullet list: Full access, no limits, write permissions
- Quote: "Where the artist sees everything"

TIER 2 (Middle - VIP):
- VIP pass laminate (gold themed)
- Text: "VERIFIED PARTNER"
- Example: "JenMusic AI"
- Bullet list: Read + scoped write, 1000 req/hr
- Quote: "Trusted collaborators with negotiated access"

TIER 3 (Bottom - General):
- Festival wristband (gray/muted)
- Text: "GENERAL ADMISSION / PUBLIC API"
- Bullet list: Read-only, 100 req/hr, anonymous
- Quote: "Limited view, no touching"

BETWEEN TIERS:
- Bold horizontal lines with "SECURITY CHECK" text

BOTTOM:
- Quote callout: "Your data, your rules"

PALETTE: Navy blue, gold, black, white, gray
BACKGROUND: Warm off-white (#F8F4E8)

MOOD: Exclusive, controlled, professional. Access is a privilege, not a right.

TEXT: Mix of bold condensed type and clean sans-serif. All text crisp and legible.
```

### Negative Prompt
```
cartoon, simplified icons, generic flowchart,
corporate infographic, tech startup aesthetic,
sci-fi, glowing effects, cyberpunk,
pure white background, sterile clinical look,
database diagram style, API documentation aesthetic,
uniform/boring pass designs (each tier should look distinct),
childish/playful wristband designs
```

---

## Alt Text

Fashion photography collage showing three MCP API access tiers as concert venue passes. Top: "Backstage" tier showing black laminate with gold "ALL ACCESS ATTRIBUTION INTERNAL" for Tier 1 with full data access. Middle: "VIP" tier showing gold laminate "VERIFIED PARTNER JenMusic AI" for Tier 2 with 1000 requests/hour. Bottom: "General Admission" tier showing gray wristband "PUBLIC API" for Tier 3 with read-only, 100 requests/hour. Security check dividers between tiers. Bottom quote: "Your data, your rules."

---

## Musical/Industry References

- **Visual reference**: Concert backstage passes, festival laminates, VIP wristbands
- **Venue metaphor**: Security checkpoints, tiered access at major concerts
- **Typography**: Concert poster bold condensed type
- **Color reference**: AAA laminate color coding (typically black for crew, gold for VIP)

---

## Visual Diversity Matrix Check

| Dimension | This Figure | Differs From |
|-----------|-------------|--------------|
| Primary Color | Navy + gold + black | Different from all README figures |
| Era Reference | Contemporary concert | Different from technical figures |
| Texture | Glossy laminate + magazine | Unique among all figures |
| Human Figures | None (passes/objects) | Different from fashion sketches |

---

## Status

- [x] Specification complete
- [ ] Generated via Nano Banana Pro
- [ ] Reviewed for clarity
- [ ] Embedded in MCP Server PRD
