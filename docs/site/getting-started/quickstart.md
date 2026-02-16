# Quick Start

This walkthrough assumes you've completed the [Installation](installation.md) steps.

## Running the Full Stack

### Terminal 1: Backend API

```bash
make agent
```

This starts the FastAPI server on [http://localhost:8000](http://localhost:8000) with:

- REST API at `/api/v1/`
- OpenAPI docs at `/docs`
- AG-UI SSE endpoint at `/api/v1/copilotkit`
- Health check at `/health`

### Terminal 2: Frontend

```bash
make dev-frontend
```

This starts the Next.js 15 development server on [http://localhost:3000](http://localhost:3000).

## Exploring the Application

### Works List (`/works`)

The works page shows all 9 Imogen Heap attribution records:

- **Confidence gauges** — green (≥0.85), amber (0.50-0.84), red (<0.50)
- **Assurance badges** — A0 through A3, indicating provenance tier
- **Review flags** — works needing human review are highlighted

### Work Detail (`/works/{id}`)

Click any work to see:

- Per-field confidence scores (title, artist, songwriter, etc.)
- Source provenance panel (which sources contributed to each field)
- Citation references linking to the SSRN paper

### Permissions (`/permissions`)

Test the MCP permission checker:

- Select a work and a use case (streaming, sync licensing, AI training, voice cloning)
- See the permission result: ALLOW, DENY, or CONDITIONS

### Review Queue (`/review`)

The review queue shows works flagged for human review:

- AI-suggested attribution changes as diffs
- Batch approval workflow
- Progress counter

### Agent Sidebar

If you have an `ANTHROPIC_API_KEY` set, the CopilotKit sidebar lets you:

- Ask questions about any work's attribution
- Get confidence explanations
- Search across the catalog
- Check permissions via natural language

## API Quick Test

```bash
# List all works
curl http://localhost:8000/api/v1/attributions/ | python -m json.tool

# Get a specific work
curl http://localhost:8000/api/v1/attributions/work/hide-and-seek | python -m json.tool

# Check a permission
curl -X POST http://localhost:8000/api/v1/permissions/check \
  -H "Content-Type: application/json" \
  -d '{"work_id": "hide-and-seek", "use_case": "streaming"}' | python -m json.tool
```

## Running Tests

```bash
# Backend unit tests (fast, ~10 seconds)
make test-local

# Backend with Docker (CI parity)
make test

# Frontend tests
make test-frontend

# All lint checks
make lint-local
```

## Next Steps

- [Architecture Overview](../user-guide/architecture.md) — Understand the 5-pipeline design
- [Key Concepts](../concepts/index.md) — Learn the theory
- [Reproducing the Paper](../tutorials/reproducing-the-paper.md) — Map paper claims to code
