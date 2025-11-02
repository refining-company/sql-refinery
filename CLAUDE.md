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

**4-Layer Pipeline:**
1. **SQL** (`sql.py`): Tree-sitter parsing → `tree_sitter.Tree`
2. **Code** (`code.py`): Syntactic AST → `code.Code` (1:1 with SQL, location-based, preserves duplicates)
3. **Model** (`model.py`): Semantic layer → `model.Model` (resolved references, identity-based, deduplicated)
4. **Features** (`variations.py`): Similarity analysis → `ExpressionVariations` (Levenshtein + column overlap)

**Orchestration:**
- `workspace.py`: Pipeline manager with index (`ws.new()`, `ws.get()`) and map system (`ws.map(fro, to, by=...)`)
- `server.py`: LSP server (thin I/O wrapper)

**Data Flow:**
```
SQL files → sql.build() → code.build() → model.build() → variations.build() → LSP → VSCode
```

**Stack:**
- Backend: Python 3.13.7
- Frontend: Node 20.18.0 (VSCode extension)

## 3. DEVELOPMENT GUIDELINES

### Design Philosophy

Optimize for developer velocity. Build fast, iterate quickly, add robustness only when needed.

**Core Principles:**
- Simplicity: minimal code, pythonic, refactor when needed
- Trust happy path: build for common cases first
- Minimal error checking: add validation when problems occur; use assertions for invariants
- Eliminate intermediate steps: go directly from A to C
- Feature-centric architecture: organize by features, not technical functions
- Modern Python 3.13+: match statements, union types, walrus operator, inline generics
- Direct API usage: use as intended, avoid defensive wrappers

### Coding Standards

- No emojis unless explicitly requested
- Minimal documentation: no proactive docs files, minimal inline comments
- Prefer editing existing files over creating new ones
- Use built-ins before custom solutions
- **Import style:**
  - `import src` + fully qualified names: `src.code.Code`, `src.utils.trunk_path()`
  - For other packages: `from pathlib import Path`
  - No aliasing except standard cases: `import tests.utils as utils`

### Naming

**Core Principle**: Name what something IS, not what it DOES

**Modules:** Nouns (substance), not verbs
- Good: `code`, `model`, `variations`, `workspace`
- Bad: ~~`parser`~~, ~~`analyzer`~~, ~~`builder`~~

**Classes:** Simple nouns, no suffixes
- Master classes match module: `code.Code`, `model.Model`
- Disambiguate via module: `code.Column` vs `model.Column`
- Bad: ~~`ColumnRef`~~, ~~`ParsedTree`~~, ~~`Tree`~~, ~~`Semantics`~~

**Functions:**
- Builders: `build()` (uniform across all modules)
- Analyzers: `find_*()`, `get_*()`, `is_*()`
- Private: `_prefix`

**Import Discipline:**
- Always `import src` + fully qualified names
- NEVER `from src import code` or `from src.code import Column`
- Rationale: `src.code.Column` vs `src.model.Column` are different abstractions

**Type Hints:**
- Required on all function signatures
- Module-qualified types: `src.code.Column`, `src.model.Model`
- Inline generics: `def new[T](self, obj: T) -> T:`

### Testing

**Snapshot Testing:**
- Each pipeline layer has snapshots (validate abstractions, not implementations)
- Refactoring should only break snapshots at changed layer
- `.true.md` files = golden standard, `.last.md` = debug output

**Test Data:**
- Recorded LSP sessions in `backend/tests/sessions/`
- Sample SQL codebases in `backend/tests/inputs/codebase/`

**Logs:**
- Backend: `logs/session.last.ndjson` (LSP client-server communication)
- Frontend: `logs/frontend-vscode.sh` (VSCode output panel)

### Commands

**IMPORTANT: Always use `make` commands. Never use `poetry` or `npm` directly.**

```bash
# Development workflow (run from repo root)
make check           # Format, lint, typecheck
make test            # Run tests
make test-update     # Update snapshots

# Backend-specific
make backend-check
make backend-test
make backend-test-update

# Frontend-specific
make frontend-check
make frontend-test
make frontend-test-update

# Utility
make clean
make install
```

### Workflow

- Test and commit all changes
- Commit prefixes: `setup:`, `feature:`, `fix:`, `refactor:`, `test:`
- **Check-in protocol**: When making multiple edits to existing code, pause and check in with the user to ensure you're not overengineering
