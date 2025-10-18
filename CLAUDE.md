# CLAUDE.md

## 1. OVERVIEW

The project is developing a Copilot designed to improve the speed and accuracy of work for Business Intelligence
Analysts who build SQL data pipelines to dashboards and analytics.

**Secret ingredient:**

- Reasoning about data and business logic by analyzing the existing SQL codebase of the company and colleagues. This is
  the source of information that allows reasoning about data.
- Providing software engineering-like efficiency features specifically tailoring it for data work (like debugging,
  tracing, refactoring)

**Key Features:**

- Autocompletion grounded in codebase-specific expressions (e.g., common join fields)
- Diagnostic highlighting of code snippets that deviate from codebase conventions
- Join analysis estimating result mappings (one-one, one-many, one-zero)
- Debugging with ability to drill down into result table cells
- Refactoring to propagate code changes across downstream queries
- Autofixes to detect and suggest updates when data patterns change (e.g., new CASE WHEN logic needed)

## 2. TECHNICAL IMPLEMENTATION

### Architecture

**Backend (Python 3.12.7):**

- **Pipeline Components**: SQL parsing (`src/sql.py`) → AST abstraction (`src/code.py`) → Logic analysis
  (`src/workspace.py`, `src/logic.py`)
- **LSP Server**: Translates analysis results into LSP diagnostics and code lenses (`src/server.py`)
- **Core Algorithm**: Uses Levenshtein distance (threshold 0.7) to detect expression similarity

**Frontend (Node 20.18.0):**

- VS Code extension (`frontend-vscode/src/extension.ts`) providing UI for viewing alternatives
- Multiple providers for code lenses, virtual documents, and diagnostics

### Key Data Flow

1. **Analysis Pipeline**: SQL files → Tree-sitter parsing → AST with typed elements (`@query`, `@table`, `@column`,
   `@expression`) → Expression similarity detection
2. **Data Structures**:
   - `Tree.index`: Registry of elements by type
   - `Tree.map_file_to_expr`: Mapping from files to their expressions
   - `ExpressionVariations`: Expression + similar variations + similarity scores + locations
3. **LSP Translation**: Alternatives → Diagnostics (blue squiggles) + Code Lenses ("Alternatives found: N") → VS Code UI

### File Structure

- **Entry Points**: `backend/src/server.py` (LSP server), `frontend-vscode/src/extension.ts` (VS Code extension)
- **Core Logic**: `backend/src/logic.py` (similarity detection), `backend/src/workspace.py` (file ingestion)
- **Test Data**: `backend/tests/inputs/codebase/` (sample SQL files), `backend/tests/sessions/` (recorded LSP sessions)
- **Mock UI**: Extension currently shows hardcoded examples instead of live LSP integration

## 3. DEVELOPMENT GUIDELINES

### Design Philosophy

Optimize for developer velocity rather than defensive programming. Build fast, iterate quickly, and add robustness only
where experience shows it's actually needed.

**Core Principles:**

- **Simplicity**: Avoid unnecessary code, write minimal lines, follow pythonic approach. Start simple and refactor when
  needed rather than architecting for problems you don't have
- **Trust the happy path** - Don't over-engineer for edge cases initially; build for the common scenarios first
- **Minimal error checking** - Add validation only when problems actually occur in practice, not preemptively. Use
  assertions for invariants; prefer crashes with clear messages over defensive code
- **Eliminate intermediate steps** - If you can go from A to C directly, skip the intermediate B step
- **Feature-Centric Architecture**: Design around features and user journeys rather than technical functions - this
  creates better encapsulation and more intuitive code organization
- **Modern Features**: Leverage Python 3.12+ (match statements, union types, walrus operator)
- **Native UI**: Prioritise using native functionality for UI, suggest if a different UI can lead to simpler and more
  robust implementation
- **Direct API usage** - Use APIs as intended rather than wrapping everything in defensive abstractions

### Coding Standards

- **No Emojis**: Never use emojis in code, comments, or documentation unless explicitly requested
- **Minimal Documentation**: Do not proactively create documentation files, or excessive self-explanatory inline
  comments
- **Prefer Editing**: Always prefer editing existing files over creating new ones
- **Use Built-ins**: Always check for built-in functions/methods before implementing custom solutions
- **Import Style**: Use `from package import module` pattern, not `import package` - clearer module origin without
  excessive verbosity. Example: `from src import code, logger` then use `code.Tree`, `logger.get()`. Avoid aliasing
  imports except for standard cases like `import tests.utils as utils`

### Testing Approach

SQL analysis pipeline (Parse → AST → Analysis → LSP) creates natural abstraction layers. When refactoring, only
snapshots at the changed layer should break - if downstream snapshots fail, we've broken an abstraction.

**Key Principles:**

- **Feature-driven snapshots**: Test vulnerable SQL codebases + recorded user sessions capture capabilities, not
  implementations
- **Progressive complexity**: Simple → complex SQL examples document growing feature support
- **Refactoring validation**: Parser changes should only break parser snapshots; LSP snapshots stay stable

**Architecture:**

- **Backend**: Snapshot each pipeline stage
- **Frontend**: Snapshot final visualizations

This inverts traditional snapshot testing - instead of locking in implementation details, we validate that our
abstractions work correctly while documenting system capabilities.

- **File names convention**: `.last.md` files for debugging, `.true.md` files as golden standards

**Logs** Located in `./logs`:

- **Frontend**: `frontend-vscode.sh` with output pannel from VSCode
- **Backend**: `session.last.ndjson` for client-server LSP comms

### Essential Commands

**Quality Checks & Testing (run from repository root):**

```bash
# Full monorepo
make check         # Run all quality checks (format, lint, typecheck, test)
make format        # Format all code
make test          # Run all tests
make test-update   # Update all test snapshots

# Backend only
make backend-check         # Check backend (Black, Ruff, MyPy, pytest)
make backend-format        # Format backend code
make backend-test          # Run backend tests
make backend-test-update   # Update backend snapshots

# Frontend only
make frontend-check        # Check frontend (TypeScript, ESLint, Prettier)
make frontend-format       # Format frontend code
make frontend-test         # Run frontend tests
make frontend-test-update  # Update frontend snapshots

# Utility
make clean         # Remove cache files
make install       # Install all dependencies
```

### Workflow

- **Test and Commit All Changes**: Every change must be tested and committed to ensure stability and track progress
- **Commit Prefixes**: Use standard prefixes for commit messages:
  - `setup:` - Build system, dependencies, configuration
  - `feat:` - New features or functionality
  - `fix:` - Bug fixes
  - `refactor:` - Code changes that neither fix bugs nor add features
  - `test:` - Adding or updating tests
  - `docs:` - Documentation changes
