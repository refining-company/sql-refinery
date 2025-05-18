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

### Development Process

1. **Understand First**: Analyze codebase structure, state ownership, and component boundaries
2. **Design Simply**: Propose the most elegant solution; include alternatives for significant trade-offs
3. **Implement Cleanly**: Write concise code following design principles, then simplify further
