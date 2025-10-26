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

1. **Layer 1 (Sources)**: `code.py` - Parse SQL files into syntactic tree
2. **Layer 2 (Semantics)**: `model.py` - Build unified semantic model (future: merge code + database + catalog)
3. **Layer 3 (Orchestration)**: `workspace.py` - Manage pipeline, caching, incremental computation
4. **Layer 4 (Features)**: `variations.py`, `autocomplete.py`, `lineage.py` (future) - Analysis features

**Key Modules:**
- `code.py`: Parse SQL → `code.Tree` (syntactic AST, location-based hashing, 1:1 with SQL)
- `model.py`: Build semantic model → `model.Semantics` (resolved references, identity-based hashing, deduplication)
- `workspace.py`: Orchestrate pipeline, cache results, manage incremental updates
- `variations.py`: Find similar expression patterns across codebase (Levenshtein distance, threshold 0.7)
- `server.py`: LSP server (thin I/O wrapper)

**Layer Separation:**
- Syntactic (code.py): Preserves all SQL occurrences, aliases, duplicates; hash by location
- Semantic (model.py): Groups identical expressions by canonical representation; hash by identity
- `model.Semantics.code_to_expression`: Maps each syntactic expression to its semantic group

**Data Flow:**
```
SQL files → code.build() → code.Tree (syntactic, with duplicates)
                              ↓
         model.build() → model.Semantics (semantic, deduplicated, with code_to_expression map)
                              ↓
      variations.build() → dict[Path, list[ExpressionVariations]] (organized by file)
                              ↓
         workspace → LSP server → VS Code
```

**Backend**: Python 3.13.7 | **Frontend**: Node 20.18.0 (VS Code extension)

### File Structure

**Backend (Python):**
- `src/code.py` - SQL parsing, syntactic AST
- `src/model.py` - Semantic model, schema registry (future: multi-source integration)
- `src/workspace.py` - Pipeline orchestration, caching, incremental updates
- `src/variations.py` - Expression pattern detection
- `src/server.py` - LSP server (thin I/O layer)
- `src/logger.py`, `src/utils.py` - Infrastructure

**Test Data:**
- `backend/tests/inputs/codebase/` - Sample SQL files
- `backend/tests/sessions/` - Recorded LSP sessions
- `backend/tests/snapshots/` - Expected outputs (.true.md = golden, .last.md = debug)

**Frontend (TypeScript):**
- `frontend-vscode/src/extension.ts` - VS Code extension entry point

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
- **Modern Features**: Leverage Python 3.13+ (match statements, union types, walrus operator)
- **Native UI**: Prioritise using native functionality for UI, suggest if a different UI can lead to simpler and more
  robust implementation
- **Direct API usage** - Use APIs as intended rather than wrapping everything in defensive abstractions

### Coding Standards

- **No Emojis**: Never use emojis in code, comments, documentation, or commit messages unless explicitly requested
- **Minimal Documentation**: Do not proactively create documentation files, or excessive self-explanatory inline
  comments
- **Prefer Editing**: Always prefer editing existing files over creating new ones
- **Use Built-ins**: Always check for built-in functions/methods before implementing custom solutions
- **Import Style**:
  - For src modules: Use absolute imports `import src` and reference with full path like `src.code.Tree`, `src.utils.trunk_path()`
  - For other packages: Use `from package import module` pattern. Example: `from pathlib import Path`
  - Avoid aliasing imports except for standard cases like `import tests.utils as utils`

### Naming Framework

**Core Principle**: Name what something IS (substance), not what it DOES (function)

**Module Names:**
- Nouns representing substance: `code`, `model`, `variations`, `workspace`
- NOT verbs: ~~`parser`~~, ~~`analyzer`~~, ~~`builder`~~

**Class Names:**
- Simple nouns, NO suffixes: `Column`, `Table`, `Expression`, `Query`, `Tree`
- Disambiguation via module: `code.Column` (syntactic) vs `model.Column` (semantic)
- NOT: ~~`ColumnRef`~~, ~~`ParsedTree`~~, ~~`ColumnDef`~~

**Function Names:**
- Builders: `build()` (uniform across modules)
  - `code.build(files) -> code.Tree`
  - `model.build(tree) -> model.SemanticModel`
  - `variations.build(model) -> dict`
- Analyzers: `analyze()`, `find()`, `detect()`
- Private: `_prefix` (e.g., `_parse()`, `_TreeBuilder`)

**Import Discipline (STRICT):**
- Always: `import src` (absolute import for src package)
- Use fully qualified names: `src.code.Column`, `src.model.Column`, `src.utils.trunk_path()`
- NEVER: `from src import code, model` (use absolute import instead)
- NEVER: `from src.code import *`
- NEVER: `from src.code import Column` (ambiguous across modules)

**Type Hints (REQUIRED):**
- All function signatures must specify module-qualified types
- Example: `def resolve(ref: src.code.Column, registry: src.model.SchemaRegistry) -> src.model.Column | None`

**Rationale**: Same names across layers (Column, Expression, Query) represent different abstractions:
- `src.code.Column` = syntactic reference in SQL text (may not exist)
- `src.model.Column` = semantic definition in schema (exists, has type)
- Fully qualified names + type hints prevent confusion

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
make check         # Format, lint, and typecheck all code
make test          # Run all tests
make test-update   # Update all test snapshots

# Backend only
make backend-check         # Format, lint, and typecheck backend (Black, Ruff, MyPy)
make backend-test          # Run backend tests
make backend-test-update   # Update backend snapshots

# Frontend only
make frontend-check        # Format, lint, and typecheck frontend (Prettier, ESLint, TypeScript)
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
  - `feature:` - New features or functionality
  - `fix:` - Bug fixes
  - `refactor:` - Code changes that neither fix bugs nor add features
  - `test:` - Adding or updating tests
  - `docs:` - Documentation changes
