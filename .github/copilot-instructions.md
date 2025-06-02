# Custom Instructions for GitHub Copilot

SQL Refining is a Copilot for SQL analysts working with large codebases.

- **Backend** (Python 3.12.7):

  - Pipeline:
    - SQL parsing (`backend/src/sql.py`)
    - Code AST abstraction (`backend/src/code.py`)
    - Workspace & logic analysis (`backend/src/workspace.py`, `backend/src/logic.py`)
  - Server:
    - LSP server translating pipeline results into LSP features (`backend/src/server.py`)

- **Frontend** (Node 20.18.0):
  - VS Code extension visualizing and interacting with LSP features (`frontend-vscode/src/extension.ts`)

## Guidelines

### Design Philosophy

- **Simplicity**: Use as few lines as possible, use most pythonic way, avoid unnecessary code I didn't ask for
- **Component Design**: Single responsibility, self-managed state, concise interfaces (`fn` for callables)
- **Error Strategy**: Use assertions for invariants; prefer crashes with clear messages over defensive code
- **Documentation**: Self-documenting code over comments; docstrings only for explaining “why”
- **Style**: Leverage modern language features, minimize globals, initialize state where used
- **Testing**: Self-contained tests manage their own state; non-intrusive harnesses; clear separation of logic

### Code Style Requirements

- **Remove Defensive Code**: Eliminate unnecessary if statements, guard clauses, and null checks
- **Eliminate Unnecessary Assignments**: Avoid intermediate variables when direct usage is clearer
- **Prefer Crashes Over Silent Failures**: Use assertions for invariants; let errors propagate with clear messages
- **Modern Python Features**: Leverage Python 3.12+ features (match statements, union types, walrus operator)

### Testing Infrastructure

- **Poetry Environment**: All test commands use `poetry run python` for consistent dependency management
- **Snapshot Testing**: `.last.md` files for debugging, `.true.md` files as golden standards
- **LSP Session Recording**: `tests/recorder.py` patches pygls protocol for message recording in NDJSON format
- **Replay Testing**: Raw protocol methods enable generic message replay for LSP communication testing
- **Self-Contained Tests**: Each test manages its own state and cleanup without relying on external setup

### Development Process

1. **Understand First**: Analyze codebase structure, state ownership, and component boundaries
2. **Design Simply**: Propose the most elegant solution; include alternatives for significant trade-offs
3. **Implement Cleanly**: Write concise code following design principles, then simplify further

## Architecture Deep Dive

### System Components

1. **Data Processing Pipeline**
   - **SQL Parser** (`sql.py`): Tree-sitter wrapper with meta-types (@query, @table, @column, @expression)
   - **AST Builder** (`code.py`): Domain objects (Column, Expression, Table, Query, Tree) with indexing
   - **Logic Analyzer** (`logic.py`): Expression similarity detection using Levenshtein distance (threshold: 0.7)

2. **Server Infrastructure**
   - **LSP Server** (`server.py`): pygls-based server translating analysis to LSP features
   - **Workspace Manager** (`workspace.py`): File ingestion and analysis coordination
   - **Protocol Features**: Diagnostics (blue squiggles), Code Lenses ("Alternatives found: N"), Peek Locations

3. **Client Integration**
   - **Extension Host** (`extension.ts`): VS Code extension spawning Python backend via Poetry
   - **Language Client**: SQL file handling, custom commands registration
   - **User Interface**: Inline diagnostics, clickable lenses, peek view for alternatives

### Data Flow Sequence

1. **Ingestion**: SQL file → LSP did_open → Workspace.ingest() → Tree.parse()
2. **Analysis**: Tree.expressions → logic.compare() → Alternative objects with similarity scores
3. **Presentation**: Alternatives → LSP diagnostics/lenses → VS Code UI rendering

### Key Data Structures

- **Tree.index**: Type-based element registry {type: [elements]}
- **Tree.map_key_to_expr**: Expression deduplication {signature: expression}
- **Alternative**: (expression, similarity_score, location) tuples
- **LSP Messages**: Diagnostic ranges, CodeLens commands, Location arrays
