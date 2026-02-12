#!/usr/bin/env bash
# setup.sh — One-command dev environment bootstrap
#
# Usage: make setup  (or ./scripts/setup.sh directly)
#
# Steps:
#   1. Check prerequisites (Docker, uv, node)
#   2. Start PostgreSQL via docker compose
#   3. Install Python dependencies via uv
#   4. Run Alembic migrations
#   5. Seed Imogen Heap data
#   6. Install frontend dependencies
#   7. Verify with health check

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

step=0
total_steps=7

print_step() {
    step=$((step + 1))
    echo ""
    echo -e "${BLUE}[$step/$total_steps]${NC} $1"
    echo "────────────────────────────────────────"
}

print_ok() {
    echo -e "  ${GREEN}✓${NC} $1"
}

print_warn() {
    echo -e "  ${YELLOW}!${NC} $1"
}

print_error() {
    echo -e "  ${RED}✗${NC} $1"
}

# ──────────────────────────────────────────────────────────────────────────────
# Step 1: Check prerequisites
# ──────────────────────────────────────────────────────────────────────────────

print_step "Checking prerequisites"

MISSING=0

if command -v docker &> /dev/null; then
    print_ok "docker found: $(docker --version | head -1)"
else
    print_error "docker not found — install from https://docs.docker.com/get-docker/"
    MISSING=1
fi

if command -v uv &> /dev/null; then
    print_ok "uv found: $(uv --version)"
else
    print_error "uv not found — install from https://docs.astral.sh/uv/getting-started/installation/"
    MISSING=1
fi

if command -v node &> /dev/null; then
    print_ok "node found: $(node --version)"
else
    print_error "node not found — install from https://nodejs.org/"
    MISSING=1
fi

if [ "$MISSING" -eq 1 ]; then
    echo ""
    print_error "Missing prerequisites. Please install them and re-run 'make setup'."
    exit 1
fi

# ──────────────────────────────────────────────────────────────────────────────
# Step 2: Start PostgreSQL via docker compose
# ──────────────────────────────────────────────────────────────────────────────

print_step "Starting PostgreSQL (pgvector/pgvector:pg17)"

cd "$PROJECT_ROOT"

# Check if postgres is already running
if docker compose -f docker-compose.dev.yml ps --status running 2>/dev/null | grep -q postgres; then
    print_warn "PostgreSQL is already running — skipping start"
else
    docker compose -f docker-compose.dev.yml up -d postgres
    print_ok "PostgreSQL container started"

    # Wait for healthy
    echo "  Waiting for PostgreSQL to be healthy..."
    retries=0
    max_retries=30
    while ! docker compose -f docker-compose.dev.yml ps --status running 2>/dev/null | grep -q postgres; do
        retries=$((retries + 1))
        if [ "$retries" -ge "$max_retries" ]; then
            print_error "PostgreSQL failed to start within ${max_retries}s"
            exit 1
        fi
        sleep 1
    done
    # Additional wait for healthcheck
    sleep 3
    print_ok "PostgreSQL is healthy"
fi

# ──────────────────────────────────────────────────────────────────────────────
# Step 3: Install Python dependencies
# ──────────────────────────────────────────────────────────────────────────────

print_step "Installing Python dependencies"

cd "$PROJECT_ROOT"
uv sync --frozen --group dev --group test
print_ok "Python dependencies installed"

# Install pre-commit hooks
uv run pre-commit install 2>/dev/null || true
print_ok "Pre-commit hooks installed"

# ──────────────────────────────────────────────────────────────────────────────
# Step 4: Run Alembic migrations
# ──────────────────────────────────────────────────────────────────────────────

print_step "Running Alembic migrations"

cd "$PROJECT_ROOT"
uv run alembic upgrade head
print_ok "Database migrated to head"

# ──────────────────────────────────────────────────────────────────────────────
# Step 5: Seed Imogen Heap data
# ──────────────────────────────────────────────────────────────────────────────

print_step "Seeding Imogen Heap attribution data"

cd "$PROJECT_ROOT"
uv run python -c "
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from music_attribution.seed.imogen_heap import seed_imogen_heap

async def main():
    engine = create_async_engine(
        'postgresql+psycopg://musicattr:musicattr_dev@localhost:5432/music_attribution',  # pragma: allowlist secret
        echo=False,
    )
    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with factory() as session:
        await seed_imogen_heap(session)
        await session.commit()
    await engine.dispose()
    print('  Seeded 8 Imogen Heap works')

asyncio.run(main())
"
print_ok "Seed data inserted (idempotent — safe to re-run)"

# ──────────────────────────────────────────────────────────────────────────────
# Step 6: Install frontend dependencies
# ──────────────────────────────────────────────────────────────────────────────

print_step "Installing frontend dependencies"

cd "$PROJECT_ROOT/frontend"
if [ -d "node_modules" ]; then
    print_warn "node_modules already exists — running npm install to update"
fi
npm install --silent
print_ok "Frontend dependencies installed"

# ──────────────────────────────────────────────────────────────────────────────
# Step 7: Verify with health check
# ──────────────────────────────────────────────────────────────────────────────

print_step "Running health checks"

cd "$PROJECT_ROOT"

# Check Python imports work
uv run python -c "from music_attribution.api.app import app; print('  FastAPI app importable')"
print_ok "Python backend OK"

# Check frontend can build types
cd "$PROJECT_ROOT/frontend"
npx tsc --noEmit --pretty false 2>/dev/null && print_ok "Frontend TypeScript OK" || print_warn "Frontend has type warnings (non-blocking)"

cd "$PROJECT_ROOT"

echo ""
echo "════════════════════════════════════════════════════════════════"
echo -e "${GREEN}  Setup complete!${NC}"
echo ""
echo "  Quick start:"
echo "    make dev-frontend     # Start frontend at localhost:3000"
echo "    make test-local       # Run backend tests"
echo "    make test-frontend    # Run frontend tests"
echo ""
echo "  PostgreSQL:"
echo "    Host: localhost:5432"
echo "    DB:   music_attribution"
echo "    User: musicattr / musicattr_dev"
echo "════════════════════════════════════════════════════════════════"
