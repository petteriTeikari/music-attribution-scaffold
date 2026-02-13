# Installation

## System Requirements

### Backend

```bash
# Python 3.13 (required — we use modern typing features)
python --version  # Should show 3.13.x

# uv package manager (ONLY — pip/conda are not supported)
uv --version

# Docker (for PostgreSQL + pgvector)
docker --version
docker compose version
```

### Frontend

```bash
# Node.js 22+ (for Next.js 15)
node --version

# npm (comes with Node.js)
npm --version
```

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/petteriTeikari/music-attribution-scaffold.git
cd music-attribution-scaffold
```

### 2. Install Backend Dependencies

```bash
# Install all dependency groups (dev + test + docs)
uv sync

# Verify the virtual environment
uv run python -c "import music_attribution; print(music_attribution.__version__)"
```

### 3. Start PostgreSQL with pgvector

```bash
# Start the database container
docker compose -f docker-compose.dev.yml up -d postgres

# Verify it's running
docker compose -f docker-compose.dev.yml ps
```

### 4. Run Database Migrations

```bash
# Apply all Alembic migrations
uv run alembic upgrade head

# Seed with Imogen Heap sample data
uv run python -m music_attribution.cli.db seed
```

### 5. Install Frontend Dependencies

```bash
cd frontend
npm install
cd ..
```

### 6. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit as needed (most defaults work for local development)
```

#### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DATABASE_URL` | Yes | `postgresql+asyncpg://...` | PostgreSQL connection string |
| `NEXT_PUBLIC_API_URL` | Yes | `http://localhost:8000` | Backend URL for frontend |
| `ANTHROPIC_API_KEY` | No | — | Required for AI agent sidebar |
| `POSTHOG_KEY` | No | — | Optional analytics |
| `ATTRIBUTION_AGENT_MODEL` | No | `anthropic:claude-haiku-4-5` | Agent model selection |

## Verify Installation

```bash
# Run backend tests (fast, no Docker needed)
make test-local

# Run frontend tests
make test-frontend

# Run lint checks
make lint-local
```

## All-in-One Setup

For convenience, `make setup` runs steps 2-5 automatically:

```bash
make setup  # uv sync + docker up + migrations + seed + npm install
```

## Troubleshooting

See the [Troubleshooting](../troubleshooting.md) page for common issues.
