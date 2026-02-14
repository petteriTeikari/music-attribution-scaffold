# fig-prd-10: Scaffold vs Product

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-prd-10 |
| **Title** | Scaffold vs Product -- This Repo Is a Scaffold |
| **Audience** | L1 (Music Industry Professional) |
| **Complexity** | L1 (concept introduction) |
| **Location** | README.md, docs/index.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Clarifies the fundamental nature of this repository. Many visitors will expect a finished product or SaaS application. This figure explains that it is a scaffold -- a configurable research framework that teams instantiate differently based on their constraints. Split-panel contrasts scaffold (left) with production system (right).

The key message is: "This repo is a scaffold (configurable, research, teaching) -- not a production system (fixed, deployed, serving users)."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  SCAFFOLD vs PRODUCT                                           |
|  ■ This Repo Is a Scaffold                                     |
+-------------------------------+-------------------------------+
|                               |                               |
|  I. SCAFFOLD (this repo)      |  II. PRODUCTION SYSTEM        |
|  ─────────────────────        |  ──────────────────           |
|                               |                               |
|  ■ Configurable               |  ■ Fixed architecture          |
|    Multiple valid paths       |    One chosen path            |
|    through decisions          |    deployed and running       |
|                               |                               |
|  ■ Research-oriented          |  ■ User-facing                |
|    Explores trade-offs        |    Serves real traffic        |
|    and alternatives           |    with SLAs                  |
|                               |                               |
|  ■ Teaching tool              |  ■ Revenue-generating         |
|    Shows WHY decisions        |    Optimized for              |
|    are made, not just WHAT    |    performance and cost       |
|                               |                               |
|  ■ Probabilistic PRD          |  ■ Fixed requirements doc     |
|    30+ decisions with         |    "We use PostgreSQL,        |
|    weighted options           |    period."                   |
|                               |                               |
|  ■ 4 team archetypes          |  ■ 1 team, 1 config          |
|    Engineer, Musician,        |    Deployed and running       |
|    Solo, Well-Funded          |                               |
|                               |                               |
|  ■ 2 domain overlays          |  ■ 1 domain                   |
|    Music + DPP                |    The one you ship           |
|                               |                               |
+-------------------------------+-------------------------------+
|  "Companion code to Teikari (2026), SSRN No. 6109087"        |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "SCAFFOLD vs PRODUCT" with coral accent square |
| Subtitle | `label_editorial` | "This Repo Is a Scaffold" |
| Scaffold panel (left) | `solution_zone` | Six attributes of a scaffold: configurable, research, teaching, probabilistic PRD, 4 archetypes, 2 domains |
| Product panel (right) | `problem_zone` | Six contrasting attributes of a production system |
| Feature bullets | `feature_list` | Coral accent squares as bullet markers |
| Vertical divider | `accent_line_v` | Coral red vertical line separating panels |
| Roman numerals I/II | `section_numeral` | Panel headers |
| Footer citation | `citation_bar` | SSRN reference |

## Anti-Hallucination Rules

1. The repo is a SCAFFOLD -- this is stated in CLAUDE.md, the README, and the design philosophy section.
2. There are 4 team archetypes: Engineer-Heavy, Musician-First, Solo Hacker, Well-Funded -- not more, not fewer.
3. There are 2 active domain overlays: Music Attribution and DPP Traceability (+ 1 planned: Generic Graph RAG).
4. The SSRN number is 6109087 -- do not invent a different number.
5. The scaffold has 30+ decision nodes (40+ in v2.0.0) -- not a single fixed architecture.
6. Do NOT imply this repo is a product, a SaaS app, or a deployed service.
7. The companion paper author is Teikari (2026).
8. Background must be warm cream (#f6f3e6).
9. This is L1 audience -- NO code, NO technical jargon, NO database names.

## Alt Text

Comparison chart: open-source music attribution scaffold versus production system -- the scaffold offers configurable decision paths, research-oriented trade-off exploration, and a probabilistic PRD with four team archetypes, while a production system deploys one fixed architecture, highlighting that this repository is a teaching and research framework for music credits and transparent confidence scoring.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Comparison chart: open-source music attribution scaffold versus production system -- the scaffold offers configurable decision paths, research-oriented trade-off exploration, and a probabilistic PRD with four team archetypes, while a production system deploys one fixed architecture, highlighting that this repository is a teaching and research framework for music credits and transparent confidence scoring.](docs/figures/repo-figures/assets/fig-prd-10-scaffold-vs-product.jpg)

*Figure 10. This repository is a scaffold -- a configurable research framework with weighted decision options, four team archetypes, and two domain overlays -- not a deployed production system. Companion code to Teikari (2026), SSRN No. 6109087.*

### From this figure plan (relative)

![Comparison chart: open-source music attribution scaffold versus production system -- the scaffold offers configurable decision paths, research-oriented trade-off exploration, and a probabilistic PRD with four team archetypes, while a production system deploys one fixed architecture, highlighting that this repository is a teaching and research framework for music credits and transparent confidence scoring.](../assets/fig-prd-10-scaffold-vs-product.jpg)
