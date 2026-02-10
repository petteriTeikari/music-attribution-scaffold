#!/bin/bash
# test-docker.sh - Run tests in Docker environment matching GitHub Actions CI
#
# This script ensures local testing matches CI exactly, eliminating
# "works on my machine" failures.
#
# Usage:
#   ./scripts/test-docker.sh          # Run all tests (Python 3.13)
#   ./scripts/test-docker.sh py311    # Run tests with Python 3.11
#   ./scripts/test-docker.sh lint     # Run linting only
#   ./scripts/test-docker.sh ci       # Run full CI simulation
#   ./scripts/test-docker.sh --build  # Force rebuild before testing

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
COMPOSE_FILE="$PROJECT_ROOT/docker/docker-compose.test.yml"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Docker is running
if ! docker info > /dev/null 2>&1; then
    echo -e "${RED}Error: Docker is not running${NC}"
    echo "Please start Docker and try again."
    exit 1
fi

# Parse arguments
BUILD_FLAG=""
SERVICE="test"

for arg in "$@"; do
    case $arg in
        --build)
            BUILD_FLAG="--build"
            ;;
        py311)
            SERVICE="test-py311"
            ;;
        lint)
            SERVICE="lint"
            ;;
        ci)
            SERVICE="ci"
            ;;
        *)
            echo -e "${YELLOW}Unknown argument: $arg${NC}"
            echo "Usage: $0 [py311|lint|ci] [--build]"
            exit 1
            ;;
    esac
done

echo -e "${GREEN}Running $SERVICE in Docker (mirrors GitHub Actions CI)...${NC}"
echo ""

# Build and run
cd "$PROJECT_ROOT"

if [ -n "$BUILD_FLAG" ]; then
    echo -e "${YELLOW}Building Docker image...${NC}"
    docker compose -f "$COMPOSE_FILE" build "$SERVICE"
fi

# Run the service (disable errexit to capture exit code)
set +e
docker compose -f "$COMPOSE_FILE" run --rm $BUILD_FLAG "$SERVICE"
EXIT_CODE=$?
set -e

# Show coverage report location if tests ran
if [ "$SERVICE" = "test" ] || [ "$SERVICE" = "ci" ]; then
    if [ -d "$PROJECT_ROOT/htmlcov" ]; then
        echo ""
        echo -e "${GREEN}Coverage report available at: htmlcov/index.html${NC}"
    fi
fi

# Handle exit codes
# Exit code 5 from pytest means "no tests collected" - treat as success for now
if [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo -e "${GREEN}All checks passed!${NC}"
elif [ $EXIT_CODE -eq 5 ]; then
    echo ""
    echo -e "${YELLOW}No tests collected yet - add tests to tests/${NC}"
    echo -e "${GREEN}All other checks passed!${NC}"
    EXIT_CODE=0
else
    echo ""
    echo -e "${RED}Checks failed with exit code $EXIT_CODE${NC}"
fi

exit $EXIT_CODE
