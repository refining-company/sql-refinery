# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SQL Refinery is a VS Code extension that helps SQL analysts find inconsistent business logic patterns across large
codebases. It identifies expressions that are similar but not identical, suggesting they may represent alternative
implementations of the same business logic.

## Copilot for BI Analysts

The project is developing a Copilot designed to improve the speed and accuracy of work for Business Intelligence Analysts who build SQL data pipelines to dashboards and analytics.

The Copilot's secret sauce has two key ingredients:
- Reasoning about data and business logic by analyzing the existing SQL codebase
- Providing software engineering-like efficiency features specifically tailored for data work

Copilot will be implemented as a plugin to major IDEs, starting with VSCode.

Key Features:
- Autocompletion grounded in codebase-specific expressions (e.g., common join fields)
- Diagnostic highlighting of code snippets that deviate from codebase conventions
- Join analysis estimating result mappings (one-one, one-many, one-zero)
- Debugging with ability to drill down into result table cells
- Refactoring to propagate code changes across downstream queries
- Autofixes to detect and suggest updates when data patterns change (e.g., new CASE WHEN logic needed)

## Architecture

**Backend (Python 3.12.7):**

- **Pipeline Components**: SQL parsing (`src/sql.py`) → AST abstraction (`src/code.py`) → Logic analysis
  (`src/workspace.py`, `src/logic.py`)
- **LSP Server**: Translates analysis results into LSP diagnostics and code lenses (`src/server.py`)
- **Core Algorithm**: Uses Levenshtein distance (threshold 0.7) to detect expression similarity

**Frontend (Node 20.18.0):**

- VS Code extension (`frontend-vscode/src/extension.ts`) providing UI for viewing alternatives
- Currently uses mock UI with hardcoded examples; LSP integration is commented out
- Multiple providers for code lenses, virtual documents, and diagnostics

## Essential Commands

### Backend Development

```bash
# Run from backend/ directory
poetry run python -m pytest                        # Run all tests
poetry run python -m pytest tests/test_server.py   # Run specific test
poetry run python -m pytest -k "test_name"         # Run tests matching pattern
poetry run ruff check src/ tests/                  # Lint code
poetry run black src/ tests/                       # Format code
poetry run mypy src/ tests/                        # Type checking
poetry run python -m src.server                    # Start LSP server manually
```

### Frontend Development

```bash
# Run from frontend-vscode/ directory
npm run compile                                # Build extension
npm run watch:rebuild                          # Watch mode (rebuilds on backend/frontend changes)
npm run watch:tstypes                          # TypeScript type checking in watch mode
npm run lint                                   # ESLint
npm run test                                   # Run VS Code extension tests
npm run package                                # Production build
```

## Key Data Flow

1. **Analysis Pipeline**: SQL files → Tree-sitter parsing → AST with typed elements (`@query`, `@table`, `@column`,
   `@expression`) → Expression similarity detection
2. **Data Structures**:
   - `Tree.index`: Registry of elements by type
   - `Tree.map_key_to_expr`: Expression deduplication by signature
   - `Alternative`: Expression + similar alternatives + similarity score + locations
3. **LSP Translation**: Alternatives → Diagnostics (blue squiggles) + Code Lenses ("Alternatives found: N") → VS Code UI

## Design Philosophy

- **Simplicity**: Minimal lines, pythonic approach, avoid unnecessary code
- **Component Design**: Single responsibility, self-managed state, concise interfaces
- **Error Strategy**: Assertions for invariants; prefer crashes with clear messages over defensive code
- **Modern Features**: Leverage Python 3.12+ (match statements, union types, walrus operator)
- **UI Strategy**: Prioritise using native functionality for UI, suggest if a different UI can lead to simpler and more
  robust implementation

## Testing Infrastructure

- **Snapshot Testing**: `.last.md` files for debugging, `.true.md` files as golden standards
- **LSP Session Recording**: `tests/recorder.py` patches pygls protocol for NDJSON message recording
- **Replay Testing**: Generic message replay for LSP communication testing
- **Self-Contained Tests**: Each test manages its own state without external dependencies

## Key File Locations

- **Entry Points**: `backend/src/server.py` (LSP server), `frontend-vscode/src/extension.ts` (VS Code extension)
- **Core Logic**: `backend/src/logic.py` (similarity detection), `backend/src/workspace.py` (file ingestion)
- **Test Data**: `backend/tests/inputs/codebase/` (sample SQL files), `backend/tests/sessions/` (recorded LSP sessions)
- **Mock UI**: Extension currently shows hardcoded examples instead of live LSP integration