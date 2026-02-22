.PHONY: help install install-dev setup
.PHONY: dev dev-down dev-logs
.PHONY: test test-all lint
.PHONY: test-local test-integration test-cov lint-local format typecheck ci-local
.PHONY: ci-docker docker-build docker-clean clean
.PHONY: dev-frontend test-frontend lint-frontend build-frontend test-e2e test-e2e-ui
.PHONY: agent dev-agent
.PHONY: install-voice test-voice dev-voice voice-local
.PHONY: docs docs-serve test-docs
.PHONY: zenodo-archive

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
# DOCKER DEVELOPMENT (PRIMARY — PhD student starts here)
# =============================================================================

dev:  ## Start full stack via Docker (postgres + backend + frontend)
	docker compose -f docker-compose.dev.yml up --build

dev-down:  ## Tear down Docker dev environment
	docker compose -f docker-compose.dev.yml down

dev-logs:  ## Follow logs from Docker dev environment
	docker compose -f docker-compose.dev.yml logs -f

# =============================================================================
# DOCKER TESTING (mirrors GitHub Actions exactly)
# =============================================================================

test: ## Default: run unit tests in Docker (CI-parity)
	@./scripts/test-docker.sh --build

test-all:  ## Full CI simulation in Docker (lint + typecheck + tests)
	@./scripts/test-docker.sh ci --build

lint:  ## Lint in Docker (CI-parity)
	@./scripts/test-docker.sh lint --build

ci-docker: test-all  ## Alias for test-all

# =============================================================================
# LOCAL DEVELOPMENT (quick iteration, may differ from CI)
# =============================================================================

test-local:  ## Run ALL tests locally: unit + integration (requires Docker daemon for testcontainers)
	.venv/bin/python -m pytest tests/ -v --timeout=120

test-integration:  ## Run integration tests only (testcontainers PostgreSQL, requires Docker daemon)
	.venv/bin/python -m pytest tests/integration/ -v --timeout=120

test-cov:  ## Run ALL tests with coverage (requires Docker daemon for testcontainers)
	.venv/bin/python -m pytest tests/ -v --timeout=120 --cov=src/music_attribution --cov-report=html --cov-report=term-missing

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

docker-clean:  ## Remove Docker images and volumes
	docker compose -f docker/docker-compose.test.yml down --rmi local --volumes 2>/dev/null || true
	docker compose -f docker-compose.dev.yml down --rmi local --volumes 2>/dev/null || true
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

test-e2e:  ## Run Playwright E2E tests (chromium, auto-starts dev server)
	cd frontend && npx playwright test

test-e2e-ui:  ## Run Playwright E2E in interactive UI mode
	cd frontend && npx playwright test --ui

# =============================================================================
# AGENT (PydanticAI + AG-UI)
# =============================================================================

agent:  ## Start FastAPI with CopilotKit AG-UI endpoint (localhost:8000)
	DATABASE_URL=postgresql+psycopg://musicattr:musicattr_dev@localhost:5432/music_attribution uv run uvicorn music_attribution.api.app:create_app --factory --host 0.0.0.0 --port 8000 --reload  # pragma: allowlist secret

dev-agent:  ## Start agent backend + frontend dev server
	@echo "Starting agent backend on :8000 and frontend on :3000"
	@echo "Set NEXT_PUBLIC_API_URL=http://localhost:8000 in frontend/.env.local"
	$(MAKE) agent &
	NEXT_PUBLIC_API_URL=http://localhost:8000 $(MAKE) dev-frontend

# =============================================================================
# VOICE AGENT (Pipecat + open-source STT/TTS)
# =============================================================================

install-voice:  ## Install voice dependencies (open-source stack)
	uv sync --frozen --group voice

test-voice:  ## Run voice agent tests
	.venv/bin/python -m pytest tests/unit/voice/ -v --timeout=60

dev-voice:  ## Start voice agent dev server (localhost:8001)
	VOICE_TRANSPORT=websocket uv run uvicorn music_attribution.voice.server:create_voice_app --factory --host 0.0.0.0 --port 8001 --reload

voice-local:  ## Run fully local voice agent (Whisper + Piper, $0/min)
	@echo "Starting fully local voice agent"
	@echo "Requires: VOICE_LLM_API_KEY set in .env (see .env.example)"
	VOICE_STT_PROVIDER=whisper VOICE_TTS_PROVIDER=piper uv run python scripts/voice_demo.py

# =============================================================================
# DOCUMENTATION
# =============================================================================

test-docs:  ## Run docs safety tests (math overflow, dollar signs)
	.venv/bin/python -m pytest tests/unit/test_docs_math_safety.py -v

GITHUB_BLOB := https://github.com/petteriTeikari/music-attribution-scaffold/blob/main
TUTORIAL_FIXUP = \
	sed -i 's|../figures/repo-figures/assets/|../figures/|g' docs/site/tutorials/voice-agent-implementation.md && \
	sed -i 's|../../src/|$(GITHUB_BLOB)/src/|g' docs/site/tutorials/voice-agent-implementation.md && \
	sed -i 's|../../scripts/|$(GITHUB_BLOB)/scripts/|g' docs/site/tutorials/voice-agent-implementation.md && \
	sed -i 's|../../pyproject.toml|$(GITHUB_BLOB)/pyproject.toml|g' docs/site/tutorials/voice-agent-implementation.md && \
	sed -i 's|../planning/|$(GITHUB_BLOB)/docs/planning/|g' docs/site/tutorials/voice-agent-implementation.md && \
	sed -i 's|../prd/|$(GITHUB_BLOB)/docs/prd/|g' docs/site/tutorials/voice-agent-implementation.md && \
	sed -i 's|../../.claude/|$(GITHUB_BLOB)/.claude/|g' docs/site/tutorials/voice-agent-implementation.md

docs:  ## Build MkDocs site (copies figures first)
	@mkdir -p docs/site/figures
	@cp docs/figures/repo-figures/assets/*.jpg docs/site/figures/
	@mkdir -p docs/site/tutorials
	@cp docs/tutorials/voice-agent-implementation.md docs/site/tutorials/
	@$(TUTORIAL_FIXUP)
	uv run mkdocs build --strict

docs-serve:  ## Serve MkDocs locally with live reload
	@mkdir -p docs/site/figures
	@cp docs/figures/repo-figures/assets/*.jpg docs/site/figures/
	@mkdir -p docs/site/tutorials
	@cp docs/tutorials/voice-agent-implementation.md docs/site/tutorials/
	@$(TUTORIAL_FIXUP)
	uv run mkdocs serve

# =============================================================================
# RELEASE / ZENODO
# =============================================================================

zenodo-archive:  ## Build clean archive for Zenodo upload
	$(eval VERSION := $(shell grep '^version' pyproject.toml | head -1 | sed 's/.*"\(.*\)"/\1/'))
	git archive --format=zip --prefix=music-attribution-scaffold-$(VERSION)/ \
		-o music-attribution-scaffold-$(VERSION).zip HEAD
	@ls -lh music-attribution-scaffold-$(VERSION).zip
	@echo "Upload to https://zenodo.org/deposit/new"

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
