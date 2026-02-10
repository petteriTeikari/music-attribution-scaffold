.PHONY: help install install-dev lint format typecheck test test-unit test-integration test-cov clean
.PHONY: ci-local ci-docker test-docker test-docker-py311 lint-docker docker-build docker-clean

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
	uv sync

install-dev:  ## Install all dependencies (dev + test groups)
	uv sync --group dev --group test
	uv run pre-commit install

# =============================================================================
# LOCAL DEVELOPMENT (may differ from CI - use ci-docker for exact match)
# =============================================================================

lint:  ## Run linting checks locally
	uv run ruff check src/ tests/
	uv run ruff format --check src/ tests/
	uv run mypy src/

format:  ## Format code with ruff
	uv run ruff check --fix src/ tests/
	uv run ruff format src/ tests/

typecheck:  ## Run type checking with mypy
	uv run mypy src/

test:  ## Run all tests locally
	@uv run pytest tests/ -v || ([ $$? -eq 5 ] && echo "No tests collected yet - add tests to tests/" && exit 0)

test-unit:  ## Run unit tests only
	@uv run pytest tests/unit/ -v -m unit || ([ $$? -eq 5 ] && echo "No unit tests collected yet" && exit 0)

test-integration:  ## Run integration tests only
	@uv run pytest tests/integration/ -v -m integration || ([ $$? -eq 5 ] && echo "No integration tests collected yet" && exit 0)

test-cov:  ## Run tests with coverage report
	uv run pytest tests/ -v --cov=src/music_attribution --cov-report=html --cov-report=term-missing

# =============================================================================
# CI SIMULATION (RECOMMENDED - mirrors GitHub Actions exactly)
# =============================================================================

ci-local:  ## Run full CI locally (lint + typecheck + test) - quick but may differ from CI
	@echo "Running local CI simulation..."
	@echo "NOTE: For exact CI match, use 'make ci-docker'"
	@echo ""
	$(MAKE) lint
	$(MAKE) test-cov

ci-docker:  ## Run full CI in Docker (RECOMMENDED - mirrors GitHub Actions exactly)
	@echo "Running CI simulation in Docker (mirrors GitHub Actions)..."
	@./scripts/test-docker.sh ci --build

test-docker:  ## Run tests in Docker (Python 3.13, mirrors CI)
	@./scripts/test-docker.sh --build

test-docker-py311:  ## Run tests in Docker (Python 3.11, mirrors CI matrix)
	@./scripts/test-docker.sh py311 --build

lint-docker:  ## Run linting in Docker (mirrors CI)
	@./scripts/test-docker.sh lint --build

# =============================================================================
# DOCKER MANAGEMENT
# =============================================================================

docker-build:  ## Build test Docker image
	docker compose -f docker/docker-compose.test.yml build test

docker-clean:  ## Remove test Docker images and volumes
	docker compose -f docker/docker-compose.test.yml down --rmi local --volumes 2>/dev/null || true
	docker image prune -f

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
