# Music Attribution Scaffold

Open-source research scaffold for music attribution with transparent confidence scoring.

**Companion code to**: Teikari, P. (2026). *Music Attribution with Transparent Confidence*. SSRN No. 6109087.

## Quick Reference

| Aspect | Details |
|--------|---------|
| **Project Type** | library |
| **Language** | Python 3.13 |
| **Package Manager** | uv (ONLY) |
| **Linter/Formatter** | ruff |
| **Type Checker** | mypy |
| **Test Framework** | pytest |

## Critical Rules

1. **uv ONLY** - Never use pip, conda, or requirements.txt
2. **AST ONLY (ZERO EXCEPTIONS)** - For ANY Python source analysis, use `ast.parse()` + `ast.walk()`. No grep/sed/awk/regex/string-`in`. Applies to production code, test code, scripts — everything
3. **Pre-commit Required** - All changes must pass pre-commit hooks
4. **Encoding** - Always specify `encoding='utf-8'` for file operations
5. **Paths** - Always use `pathlib.Path()` not string concatenation
6. **Timezone** - Always use `datetime.now(timezone.utc)` not `datetime.now()`

## Quick Commands

```bash
# Install dependencies
make install-dev

# Run tests
make test

# Lint and format
make lint
make format

# Type check
make typecheck

# Coverage report
make test-cov
```

## What AI Must NEVER Do

- Modify files marked with `# AIDEV-IMMUTABLE`
- Use pip, conda, or create requirements.txt
- Parse Python code with grep/sed/awk/regex
- Skip pre-commit hooks
- Hardcode file paths
- Use `datetime.now()` without timezone
- Commit secrets or credentials

## Knowledge Base

The `docs/knowledge-base/` directory contains RAG-optimized markdown for LLM consumption.

**Important workflow**:
- Raw sources (PDFs, HTML) go in `raw-sources/` (gitignored)
- Convert to clean markdown before committing
- Use SYNTHESIS.md pattern for aggregation

See [docs/knowledge-base/README.md](docs/knowledge-base/README.md) for details.

## Theoretical Background — Manuscript Lineage

This repo is the companion code to a chain of academic manuscripts. Always consult these for the theoretical foundations:

| Manuscript | Path | Focus |
|-----------|------|-------|
| **Music Attribution (primary)** | `~/Dropbox/github-personal/sci-llm-writer/manuscripts/music_traceability_v2026/submission/preprint-ssrn/music-generative-transition-ssrn.tex` | "Governing Generative Music" — A0-A3 assurance levels, Oracle Problem, two-friction taxonomy, deterrence economics, MCP permission patchbay, agent archetypes (BYO vs bowling-shoe) |
| **AI Passport v2 (fashion DPP)** | `~/Dropbox/github-personal/sci-llm-writer/manuscripts/mcp-review/submissions/preprint/v2-Jan13-2026/ai-passport-v2-8-3-SSRN.tex` | "Digital Product Passports as Agentic Supply Chain Infrastructure" — Assurance Stack A0-A3, specification costs, SConU confidence calibration, governance tiers (Autonomous/Recommend/Escalate) |
| **AI Passport v1 (agentic commerce)** | `~/Dropbox/github-personal/sci-llm-writer/manuscripts/mcp-review/submissions/preprint/v1-Dec24-2025/ai-passport-v1-12-bbl-SSRN.tex` | "From Compliance to Capability" — more agentic commerce heavy: protocol soup (MCP/A2A/ACP/AP2/TAP), SEO-to-GEO transition, Block/Feed/Partner framework, confidence-driven commerce |
| **Long MCP draft (seed ideas)** | `~/Dropbox/github-personal/sci-llm-writer/manuscripts/mcp-review/archived/mcp-draft-ssrn-long.tex` | "Intelligent Interoperability" — Bayesian knowledge graphs, Coasean singularity, phased deployment (post-sales first), verification economics pyramid, regenerative systems, protocol obsolescence |

### Key Concepts Across All Papers

- **A0-A3 Assurance Levels**: Tiered provenance (None → Identity-verified), maps to ISRC/ISWC/ISNI
- **Oracle Problem**: Digital systems cannot fully verify physical/training reality — design for deterrence, not detection
- **Two-Friction Taxonomy**: Administrative friction (automate) vs. discovery friction (preserve)
- **MCP as consent infrastructure**: Machine-readable permission queries for AI training rights
- **Attribution-by-Design**: Embed provenance at creation, not post-hoc
- **Probabilistic confidence**: Conformal prediction, SConU, Bayesian updating across knowledge graphs

### Design Philosophy

This repo is **not** a single-architecture implementation. It is a **scaffold** — a general framework that could be instantiated by teams with very different constraints (engineer-heavy vs. musician-heavy, custom-code vs. low-code, Hetzner vs. Render vs. big-three clouds). The probabilistic PRD captures these branching paths.

## See Also

- [.claude/CLAUDE.md](.claude/CLAUDE.md) - Detailed behavior contract
- [.claude/golden-paths.md](.claude/golden-paths.md) - Approved patterns
- [.claude/rules/](.claude/rules/) - Domain-specific rules
- [docs/planning/](docs/planning/) - Architecture plans and PRDs
- [docs/prd/decisions/](docs/prd/decisions/) - Probabilistic decision network (23 nodes, 5 levels)
- [docs/prd/decisions/REPORT.md](docs/prd/decisions/REPORT.md) - Decision network report with mermaid visualizations
- [docs/prd/archetypes/](docs/prd/archetypes/) - Team archetype profiles
- [docs/prd/domains/](docs/prd/domains/) - Domain overlay system (music attribution + DPP traceability)
- [docs/planning/probabilistic-prd-design.md](docs/planning/probabilistic-prd-design.md) - Probabilistic PRD design rationale
- [.claude/skills/self-learning-iterative-coder/SKILL.md](.claude/skills/self-learning-iterative-coder/SKILL.md) - Self-correcting TDD loop skill
- [SSRN Preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087) - Research paper
