# Documentation Polish — Pre-Freeze Audit

> **Context**: This repo is being frozen as the companion code to [SSRN No. 6109087](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087). This directory tracks the final documentation polish ensuring comprehensive discoverability for new developers and LLM context engineering.

---

## Documentation Architecture

```
README.md (root)                    ← Entry point: "what is this?"
├── src/music_attribution/README.md ← Module map, pipeline overview
│   ├── etl/README.md               ← ETL pipeline details
│   ├── resolution/README.md        ← Entity resolution cascade
│   ├── attribution/README.md       ← Confidence scoring engine
│   ├── api/README.md               ← FastAPI routes
│   ├── chat/README.md              ← PydanticAI agent + AG-UI
│   ├── mcp/README.md               ← MCP consent server
│   └── schemas/README.md           ← Boundary objects
├── frontend/README.md              ← Next.js 15 editorial UI
├── tests/README.md                 ← Test pyramid (351+42+265)
├── docs/
│   ├── site/                       ← MkDocs (29 pages, Material theme)
│   ├── prd/README.md               ← PRD ecosystem (31 decision nodes)
│   ├── architecture/README.md      ← ADRs, security model, diagrams
│   ├── knowledge-base/README.md    ← RAG-optimized domain knowledge
│   └── figures/repo-figures/       ← 200 Nano Banana Pro figures
└── .claude/                        ← AI behavior contract
```

## Polish Tasks

| # | Task | Status | Impact |
|---|------|--------|--------|
| 1 | Fix docs/prd/README.md — outdated node count, add repo figures | Done | High |
| 2 | Fix Mermaid contrast across all docs (lineColor, node styles) | Done | High |
| 3 | Add repo-figure images to MkDocs site pages | Done | Medium |
| 4 | Update MkDocs nav with Design Decisions section | Done | Medium |
| 5 | Add repo-figures to module READMEs | Done | Medium |
| 6 | Final review — build MkDocs, verify links | Done | High |

## Visual Asset Inventory

| Category | Count | Prefix | Key Figures |
|----------|-------|--------|-------------|
| Repository overview | 31 | `fig-repo-*` | Hero, pipeline, stack, CI/CD, Docker, MCP security |
| Backend pipelines | 20 | `fig-backend-*` | ETL, resolution, attribution, FastAPI, DB |
| Agent / chat | 10 | `fig-agent-*` | Full stack, AG-UI flow, tool dispatch, failover |
| Frontend / design | 20 | `fig-frontend-*` | Architecture, tokens, components, accessibility |
| Technology choices | 18 | `fig-choice-*` | PydanticAI, CopilotKit, PostgreSQL, Tailwind, uv |
| PRD network | 10 | `fig-prd-*` | Decision network, node anatomy, archetypes |
| Ecosystem | 16 | `fig-ecosystem-*` | Integration models, CMO, compliance |
| Landscape | 32 | `fig-landscape-*` | Problem taxonomy, funding, TDA methods |
| Scenarios | 5 | `fig-scenario-*` | Archetype comparisons, decision paths |
| **Total** | **~200** | | |

## LLM Context Engineering Strategy

For a new developer asking an LLM to "describe this repo":

1. **Root README.md** provides executive summary, pipeline diagram, tech stack, sample data
2. **src/music_attribution/README.md** maps all modules with boundary objects
3. **Each module README** has: purpose, key classes, code examples, adjacent pipelines
4. **docs/prd/README.md** links to the Bayesian decision network explaining WHY each choice was made
5. **docs/figures/repo-figures/** provides 200 visual explanations with SEO/GEO-optimized alt text
6. **MkDocs site** (29 pages) provides the comprehensive reference with auto-generated API docs

The hierarchy is designed for progressive disclosure: README.md → module READMEs → MkDocs → knowledge-base.
