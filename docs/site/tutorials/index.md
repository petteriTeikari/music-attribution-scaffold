# Tutorials

Step-by-step guides for common tasks.

| Tutorial | What You'll Build |
|----------|-------------------|
| [Reproducing the Paper](reproducing-the-paper.md) | Map SSRN paper claims to running code |
| [Adding Data Sources](adding-data-sources.md) | Add a new ETL extractor |
| [API Examples](api-examples.md) | Query the REST API with curl and Python |

---

## Using the Agent Sidebar

![How-to guide: AI agent sidebar for natural-language music attribution queries, showing a split-panel layout with a works dashboard displaying confidence scores on the left and a three-step conversational flow on the right -- user asks about music credits, agent invokes attribution tools, and returns a transparent confidence-scored answer with source provenance.](../figures/fig-howto-04-use-agent-sidebar.jpg)

*Agent sidebar interaction flow for the Music Attribution Scaffold. Non-technical users query music credits in natural language while the agent transparently invokes the same tools as the REST API, returning confidence-scored attribution data without requiring API knowledge (Teikari, 2026).*

The CopilotKit sidebar lets you query attribution data using natural language. Type a question like "Who produced Hide and Seek?" and the agent calls the right tools behind the scenes -- `lookup_work()`, `get_attribution()` -- to return a confidence-scored answer with source provenance. Requires `ANTHROPIC_API_KEY` in your environment. See [API Examples](api-examples.md) for the agent SSE endpoint details.

---

## Checking Permissions via MCP

![Workflow diagram: four-step MCP permission check for music attribution consent infrastructure, showing how an AI agent queries training rights for a music work, the MCP server evaluates rights holder preferences, and returns a structured ALLOW or DENY response with assurance level -- replacing ambiguous license text with machine-readable, transparent confidence-backed consent.](../figures/fig-howto-05-check-permissions-mcp.jpg)

*MCP consent infrastructure workflow for the Music Attribution Scaffold. An AI agent submits a structured permission query, the MCP server evaluates it against declared rights holder preferences, and returns an explicit decision with provenance -- embodying the paper's principle that consent must be machine-readable, not buried in license text (Teikari, 2026).*

The MCP (Model Context Protocol) server turns ambiguous licensing into machine-readable permission checks. An AI agent asks a structured question like "Can I use this track for AI training?", the MCP server evaluates the rights holder's declared permissions, and returns an explicit ALLOW or DENY with provenance. See [API Examples -- Check Permissions](api-examples.md#check-permissions) for curl and Python examples.

---

## Running Tests

![Tutorial diagram: decision tree for selecting the correct test suite in the open-source music attribution scaffold, branching from code change type -- Python backend, frontend components, or configuration -- to specific make commands for unit tests, integration tests, Vitest, Playwright E2E, and pre-commit hooks, ensuring transparent confidence in every code contribution.](../figures/fig-howto-06-run-tests.jpg)

*Test selection decision tree for the Music Attribution Scaffold. Contributors follow branching paths based on what they changed -- Python logic, database models, frontend components, or configuration -- to run the minimal necessary test suite, with pre-commit hooks as a universal quality gate before every commit (Teikari, 2026).*

Choose the right test suite based on what you changed: Python backend changes need `make test-local` (unit) or `make test` (integration), frontend changes need `make test-frontend`, and all changes must pass `pre-commit run --all-files` before any commit. See [Troubleshooting](../troubleshooting.md) if tests fail unexpectedly.

---

## Deploying to Production

![Step-by-step guide: five-step production deployment pipeline for the open-source music attribution scaffold, from Docker build through environment configuration and registry push to a branching deploy step with four paths -- Render PaaS, Kamal 2 Docker deployment, Hetzner with Ubicloud managed Kubernetes, and Big Three hyperscalers -- concluding with health check and Prometheus metrics verification, reflecting the scaffold philosophy that deployment paths vary by team archetype.](../figures/fig-howto-07-deploy-to-production.jpg)

*Production deployment pipeline for the Music Attribution Scaffold. Four deployment paths reflect PRD v2.1.0: Render for PaaS simplicity, Kamal 2 for Docker-without-K8s, Hetzner+Ubicloud for managed infrastructure at budget prices, and Big Three for enterprise compliance -- all converging on the same health and metrics verification endpoints (Teikari, 2026).*

The scaffold ships as a production-ready Docker image with Prometheus metrics and health checks. Deployment follows five steps: build, configure, push, deploy (choose your path), and verify. Four paths are supported -- from Render PaaS to Hetzner bare-metal -- reflecting the scaffold philosophy that no single deployment path is "correct."

---

## Creating Figures with Nano Banana Pro

![Workflow diagram: six-step figure creation pipeline for the music attribution scaffold documentation, from reading the figure plan and style guide through prompt composition and Nano Banana Pro image generation to quality verification and repository commit -- demonstrating content-style decoupling where plans define what to show and the style guide defines how, ensuring consistent open-source visual identity.](../figures/fig-howto-08-create-figures-nano-banana.jpg)

*Figure creation workflow for the Music Attribution Scaffold. The content-style decoupling principle separates semantic figure plans (what to communicate) from the visual style guide (how it should look), enabling reproducible, quality-gated figure generation via Nano Banana Pro with a minimum score threshold of 21/25 (Teikari, 2026).*

Figure creation follows a six-step pipeline: read the figure plan, load the style guide, compose the generation prompt, generate in Nano Banana Pro, verify against the quality checklist (score >= 21/25), and commit to the repo. Plans define WHAT (content), the style guide defines HOW (visual). See `docs/figures/repo-figures/figure-plans/` for all plan files and `STYLE-GUIDE-REPO.md` for the visual specification.

---

## How to Contribute

![How-to guide: six-step open-source contribution workflow for the music attribution scaffold, from fork and clone through branch creation, coding under CLAUDE.md behavioral rules, pre-commit hook verification, test execution, and pull request submission -- quality gates including ruff, mypy, and pytest are non-negotiable for both human and AI contributors to maintain transparent confidence in music metadata code.](../figures/fig-howto-09-how-to-contribute.jpg)

*Contribution workflow for the Music Attribution Scaffold. The CLAUDE.md behavioral contract governs both human and AI contributors equally, with four mandatory quality gates (ruff check, ruff format, mypy, pytest) ensuring that every pull request meets the project's standards for code quality and attribution correctness (Teikari, 2026).*

Every contribution follows a six-step path: fork, branch, code (following CLAUDE.md rules), pass pre-commit hooks, pass tests, and submit a PR. The quality gates are non-negotiable -- `ruff check`, `ruff format --check`, `mypy`, and `pytest` must all pass before any PR is reviewed. Run `make install-dev` after cloning to set up the development environment.
