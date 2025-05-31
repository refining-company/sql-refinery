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
