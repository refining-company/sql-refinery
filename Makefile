# Makefile for SQL Refinery monorepo
# Provides unified quality check interface for both backend (Python) and frontend (TypeScript)

.PHONY: help check test test-update clean install
.PHONY: backend-check backend-test backend-test-update backend-clean backend-install
.PHONY: frontend-check frontend-test frontend-test-update frontend-clean frontend-install

# Default target - show help
help:
	@echo "SQL Refinery - Monorepo Commands"
	@echo ""
	@echo "Full Repository:"
	@echo "  make check        Format, lint, and typecheck all code"
	@echo "  make test         Run all tests"
	@echo "  make test-update  Update all test snapshots"
	@echo "  make clean        Remove all cache and build files"
	@echo "  make install      Install all dependencies"
	@echo ""
	@echo "Backend Only:"
	@echo "  make backend-check        Format, lint, and typecheck backend (Black, Ruff, MyPy)"
	@echo "  make backend-test         Run backend tests"
	@echo "  make backend-test-update  Update backend test snapshots"
	@echo ""
	@echo "Frontend Only:"
	@echo "  make frontend-check        Format, lint, and typecheck frontend (Prettier, ESLint, TypeScript)"
	@echo "  make frontend-test         Run frontend tests"
	@echo "  make frontend-test-update  Update frontend test snapshots"

# ============================================================================
# Full Repository Commands
# ============================================================================

check: backend-check frontend-check
	@echo ""
	@echo "✓ All checks passed!"

test: backend-test frontend-test
	@echo ""
	@echo "✓ All tests passed!"

test-update: backend-test-update frontend-test-update
	@echo ""
	@echo "✓ All snapshots updated!"

clean: backend-clean frontend-clean
	@echo "✓ Cleaned all cache and build files"

install: backend-install frontend-install
	@echo "✓ All dependencies installed"

# ============================================================================
# Backend Commands (Python + Poetry)
# ============================================================================

backend-check:
	@echo "→ Backend: Formatting code (Black)..."
	@cd backend && poetry run black src/ tests/
	@echo ""
	@echo "→ Backend: Auto-fixing lint issues (Ruff)..."
	@cd backend && poetry run ruff check src/ tests/ --fix
	@echo ""
	@echo "→ Backend: Linting (Ruff)..."
	@cd backend && poetry run ruff check src/ tests/
	@echo ""
	@echo "→ Backend: Type checking (MyPy)..."
	@cd backend && poetry run mypy src/ tests/


backend-test:
	@cd backend && poetry run pytest

backend-test-update:
	@cd backend && poetry run pytest --snapshot-update

backend-clean:
	@cd backend && rm -rf .pytest_cache .mypy_cache .ruff_cache __pycache__
	@cd backend && find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@cd backend && find . -type f -name "*.pyc" -delete

backend-install:
	@cd backend && poetry install

# ============================================================================
# Frontend Commands (TypeScript + npm)
# ============================================================================

frontend-check:
	@echo "→ Frontend: Formatting code (Prettier)..."
	@cd frontend-vscode && npm run format
	@echo ""
	@echo "→ Frontend: Linting (ESLint)..."
	@cd frontend-vscode && npm run lint
	@echo ""
	@echo "→ Frontend: Type checking (TypeScript)..."
	@cd frontend-vscode && npm run check-types


frontend-test:
	@cd frontend-vscode && npm run test

frontend-test-update:
	@cd frontend-vscode && npm run test:update

frontend-clean:
	@cd frontend-vscode && npm run flush
	@cd frontend-vscode && rm -rf node_modules/.cache

frontend-install:
	@cd frontend-vscode && npm install
