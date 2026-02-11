.PHONY: help install install-dev setup
.PHONY: test test-py311 test-all lint
.PHONY: test-local test-unit test-integration test-cov lint-local format typecheck ci-local
.PHONY: ci-docker docker-build docker-clean clean
.PHONY: dev-frontend test-frontend lint-frontend build-frontend
.PHONY: agent dev-agent

.DEFAULT_GOAL := help

# Project variables
PROJECT_NAME := music-attribution
PYTHON_VERSION := 3.13

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# =============================================================================
# DEPENDENCY MANAGEMENT
# =============================================================================

install:  ## Install production dependencies only
	uv sync --frozen

install-dev:  ## Install all dependencies (dev + test groups)
	uv sync --frozen --group dev --group test
	uv run pre-commit install

setup:  ## One-command setup: Docker + deps + migrations + seed + frontend
	@./scripts/setup.sh

# =============================================================================
# DOCKER TESTING (DEFAULT - mirrors GitHub Actions exactly)
# =============================================================================

test: ## Default: run tests in Docker (CI-parity)
	@./scripts/test-docker.sh --build

test-py311:  ## Tests in Docker (Python 3.11, CI matrix)
	@./scripts/test-docker.sh py311 --build

test-all:  ## Full CI simulation in Docker (lint + typecheck + tests)
	@./scripts/test-docker.sh ci --build

lint:  ## Lint in Docker (CI-parity)
	@./scripts/test-docker.sh lint --build

ci-docker: test-all  ## Alias for test-all

# =============================================================================
# LOCAL DEVELOPMENT (quick iteration, may differ from CI)
# =============================================================================

test-local:  ## Run tests locally (fast, no Docker)
	@uv run pytest tests/ -v || ([ $$? -eq 5 ] && echo "No tests collected yet" && exit 0)

test-unit:  ## Run unit tests only (local)
	@uv run pytest tests/unit/ -v -m unit || ([ $$? -eq 5 ] && echo "No unit tests collected yet" && exit 0)

test-integration:  ## Run integration tests only (requires Docker daemon)
	.venv/bin/python -m pytest tests/integration/ -v -m integration --timeout=120

test-all-local:  ## Run ALL tests: unit + integration (requires Docker daemon)
	.venv/bin/python -m pytest tests/ -v -m "unit or integration" --timeout=120

test-cov:  ## Run tests with coverage (local)
	uv run pytest tests/ -v --cov=src/music_attribution --cov-report=html --cov-report=term-missing

lint-local:  ## Run linting locally (fast, no Docker)
	uv run ruff check src/ tests/
	uv run ruff format --check src/ tests/
	uv run mypy src/

format:  ## Format code with ruff (local)
	uv run ruff check --fix src/ tests/
	uv run ruff format src/ tests/

typecheck:  ## Run type checking with mypy (local)
	uv run mypy src/

ci-local:  ## Run full CI locally (quick but may differ from CI)
	@echo "Running local CI simulation..."
	@echo "NOTE: For exact CI match, use 'make test-all'"
	@echo ""
	$(MAKE) lint-local
	$(MAKE) test-cov

# =============================================================================
# DOCKER MANAGEMENT
# =============================================================================

docker-build:  ## Build test Docker image
	docker compose -f docker/docker-compose.test.yml build test

docker-clean:  ## Remove test Docker images and volumes
	docker compose -f docker/docker-compose.test.yml down --rmi local --volumes 2>/dev/null || true
	docker image prune -f

# =============================================================================
# FRONTEND (Next.js)
# =============================================================================

dev-frontend:  ## Start frontend dev server (localhost:3000)
	cd frontend && npm run dev

test-frontend:  ## Run frontend tests (Vitest)
	cd frontend && npm test

lint-frontend:  ## Lint frontend (ESLint + TypeScript)
	cd frontend && npm run lint && npx tsc --noEmit

build-frontend:  ## Build frontend for production
	cd frontend && npm run build

# =============================================================================
# AGENT (PydanticAI + AG-UI)
# =============================================================================

agent:  ## Start FastAPI with CopilotKit AG-UI endpoint (localhost:8000)
	uv run uvicorn music_attribution.api.app:create_app --factory --host 0.0.0.0 --port 8000 --reload

dev-agent:  ## Start agent backend + frontend dev server
	@echo "Starting agent backend on :8000 and frontend on :3000"
	@echo "Set NEXT_PUBLIC_API_URL=http://localhost:8000 in frontend/.env.local"
	$(MAKE) agent &
	NEXT_PUBLIC_API_URL=http://localhost:8000 $(MAKE) dev-frontend

# =============================================================================
# CLEANUP
# =============================================================================

clean:  ## Clean build artifacts and cache
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -rf dist/
	rm -rf .coverage
	rm -rf coverage.xml
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
