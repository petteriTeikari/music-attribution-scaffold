# Documentation

This directory contains all documentation for the Music Attribution Scaffold, including the MkDocs site source, architecture plans, the probabilistic PRD, and the RAG-optimized knowledge base.

## Where to Find What

| Directory | Contents |
|---|---|
| `site/` | MkDocs source files (deployed to GitHub Pages) |
| `prd/` | Probabilistic decision network (79 nodes, 5 levels) |
| `prd/decisions/` | Individual decision node YAML files |
| `prd/archetypes/` | Team archetype profiles (engineer-heavy, musician-heavy, etc.) |
| `prd/domains/` | Domain overlay system (music attribution + DPP traceability) |
| `planning/` | Architecture plans, design rationale, task lists |
| `knowledge-base/` | RAG-optimized markdown for LLM consumption |
| `architecture/` | Architecture diagrams and design documents |
| `api/` | API documentation and OpenAPI extensions |
| `figures/` | Generated figures and visual references |
| `sources/` | Source materials (gitignored raw PDFs/HTML go in `raw-sources/`) |

## MkDocs Documentation Site

The project uses [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) for the documentation site, deployed to GitHub Pages.

### Local Preview

```bash
uv run mkdocs serve
```

This starts a local server at `http://localhost:8000` with live reload.

### Build

```bash
uv run mkdocs build --strict
```

The `--strict` flag ensures broken links and missing references cause build failures.

### Site Structure

The navigation is defined in `mkdocs.yml` at the project root. Key sections:

- **Getting Started**: Installation and quickstart guides
- **Concepts**: Oracle Problem, Assurance Levels, Conformal Prediction, etc.
- **User Guide**: Architecture, backend, frontend, agentic UI
- **API Reference**: Auto-generated from Python docstrings via mkdocstrings
- **Tutorials**: Reproducing the paper, adding data sources, API examples

### Adding a New Page

1. Create a `.md` file in the appropriate `docs/site/` subdirectory.
2. Add a nav entry in `mkdocs.yml` under the appropriate section.
3. Preview with `uv run mkdocs serve` to verify rendering.

## Figure Creation

Figures are generated using Nano Banana Pro and stored in `figures/`. Visual references for the editorial design system live in `figures/visual-references/`.

## Knowledge Base

The `knowledge-base/` directory contains markdown files optimized for RAG/LLM consumption. See `knowledge-base/README.md` for the conversion workflow from raw sources to clean markdown.

Important: Raw sources (PDFs, HTML) go in `raw-sources/` which is gitignored. Only clean markdown is committed.

## Visual Documentation

The `figures/repo-figures/assets/` directory contains 200 generated figures covering every aspect of the scaffold. Key figures for repository orientation:

<details>
<summary>Repository Overview Figures (31 figures)</summary>

![Directory structure map of the music attribution scaffold showing hierarchical organization of source, docs, frontend, and test directories.](figures/repo-figures/assets/fig-repo-03-directory-map.jpg)

*Repository directory structure and organization.*

![Technology stack showing Python 3.13, FastAPI, PostgreSQL with pgvector, PydanticAI, Next.js 15, Tailwind v4, and CopilotKit.](figures/repo-figures/assets/fig-repo-04-technology-stack.jpg)

*Complete technology stack with rationale for each choice.*

![Quickstart flow from git clone through make setup to running the scaffold on localhost.](figures/repo-figures/assets/fig-repo-05-quickstart-flow.jpg)

*Quickstart flow: clone, setup, run.*

![Make commands reference showing all available Makefile targets for development, testing, linting, and deployment.](figures/repo-figures/assets/fig-repo-06-make-commands-map.jpg)

*All Make commands available for development workflow.*

![Pre-commit quality gates: ruff check, ruff format, mypy, detect-secrets, YAML lint running before every commit.](figures/repo-figures/assets/fig-repo-07-precommit-quality-gates.jpg)

*Pre-commit hooks ensuring code quality on every commit.*

![CI/CD pipeline showing GitHub Actions workflow: lint, typecheck, test, build, deploy-docs.](figures/repo-figures/assets/fig-repo-08-ci-cd-pipeline.jpg)

*GitHub Actions CI/CD pipeline with path-based filtering.*

![Docker architecture showing docker-compose.dev.yml with PostgreSQL, pgvector, PgBouncer, and Valkey services.](figures/repo-figures/assets/fig-repo-09-docker-architecture.jpg)

*Docker Compose development environment topology.*

![Testing pyramid: 351 unit tests (fast), 42 integration tests (PostgreSQL), 265 frontend tests (Vitest), E2E (Playwright).](figures/repo-figures/assets/fig-repo-10-testing-pyramid.jpg)

*Test pyramid with counts across all layers.*

![Frontend architecture: Next.js 15 App Router with editorial design system, Jotai state, CopilotKit sidebar.](figures/repo-figures/assets/fig-repo-11-frontend-architecture.jpg)

*Frontend architecture showing Next.js App Router, design system, and CopilotKit integration.*

![Backend-to-frontend connection showing FastAPI API routes consumed by Next.js frontend with AG-UI streaming.](figures/repo-figures/assets/fig-repo-12-backend-frontend-connection.jpg)

*How the backend FastAPI API connects to the Next.js frontend.*

![Environment variables map showing all required and optional env vars for backend, frontend, and agent configuration.](figures/repo-figures/assets/fig-repo-13-environment-variables.jpg)

*Environment variable configuration reference.*

![Database schema: PostgreSQL tables for works, contributors, sources, permissions, feedback with pgvector columns.](figures/repo-figures/assets/fig-repo-14-database-schema.jpg)

*PostgreSQL database schema with relational and vector columns.*

![CLAUDE.md hierarchy showing root CLAUDE.md, .claude/CLAUDE.md, rules, domains, skills, and memory files.](figures/repo-figures/assets/fig-repo-15-claude-md-hierarchy.jpg)

*AI behavior contract hierarchy: CLAUDE.md, rules, domains, skills.*

![Music AI attribution landscape overview showing 50+ companies across 8 categories.](figures/repo-figures/assets/fig-repo-16-landscape-overview.jpg)

*Music AI attribution commercial landscape overview.*

![EU AI Act compliance timeline showing Article 50 transparency requirements and GPAI obligations.](figures/repo-figures/assets/fig-repo-18-eu-ai-act-timeline.jpg)

*EU AI Act compliance timeline relevant to music attribution.*

![MCP attack taxonomy showing 9 attack categories from MCPSecBench security research.](figures/repo-figures/assets/fig-repo-20-mcp-attack-taxonomy.jpg)

*MCP security attack taxonomy from MCPSecBench research.*

![Inverse scaling paradox showing how larger LLMs may be more susceptible to certain MCP attacks.](figures/repo-figures/assets/fig-repo-21-inverse-scaling-paradox.jpg)

*Inverse scaling paradox in MCP security.*

![MCP Guard three-stage protection: input validation, execution sandbox, output filtering.](figures/repo-figures/assets/fig-repo-22-mcp-guard-three-stage.jpg)

*Three-stage MCP Guard protection architecture.*

![MCP authentication crisis showing lack of standardized auth across MCP server implementations.](figures/repo-figures/assets/fig-repo-23-mcp-auth-crisis.jpg)

*MCP authentication standardization challenges.*

![Protocol landscape showing MCP, A2A, ACP, AP2, TAP and their interrelationships.](figures/repo-figures/assets/fig-repo-24-protocol-landscape.jpg)

*AI protocol landscape: MCP, A2A, ACP, AP2, TAP.*

![MCP evolution timeline from initial release through security research to production hardening.](figures/repo-figures/assets/fig-repo-25-mcp-evolution-timeline.jpg)

*MCP protocol evolution timeline.*

![Zero-trust MCP architecture with defense-in-depth security layers.](figures/repo-figures/assets/fig-repo-26-zero-trust-mcp.jpg)

*Zero-trust architecture for MCP deployments.*

![MCP CVE gallery showing known vulnerabilities and their mitigations.](figures/repo-figures/assets/fig-repo-27-mcp-cve-gallery.jpg)

*Known MCP vulnerabilities and mitigation strategies.*

![Sandbox isolation patterns for MCP server execution environments.](figures/repo-figures/assets/fig-repo-28-sandbox-isolation.jpg)

*Sandbox isolation for MCP server execution.*

![OWASP Agentic Top 10 security risks mapped to music attribution scaffold mitigations.](figures/repo-figures/assets/fig-repo-29-owasp-agentic-top10.jpg)

*OWASP Agentic Top 10 risks and scaffold mitigations.*

![MCP observability showing logging, tracing, and metrics collection for MCP server operations.](figures/repo-figures/assets/fig-repo-30-mcp-observability.jpg)

*MCP observability: logging, tracing, metrics.*

![AAIF governance framework for responsible AI agent deployment in music attribution.](figures/repo-figures/assets/fig-repo-31-aaif-governance.jpg)

*AAIF governance framework for responsible AI agents.*

</details>
