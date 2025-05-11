# Custom Instructions for GitHub Copilot

## About This Repository

SQL Refining is a Copilot for SQL analysts working with large codebases:

1. **Backend**: Python analysis engine in `backend/src/` (Python 3.12.7, entry: `server.py`)
2. **Frontend**: VS Code extension in `frontend-vscode/src/` using LSP (Node 20.18.0, entry: `extension.ts`)

## Design Philosophy

- **Component Design**: Single responsibility, self-managed state, concise interfaces (`fn` for callables)
- **Error Strategy**: Use assertions for invariants, prefer crashes with clear messages over defensive code
- **Documentation**: Self-documenting code over comments, docstrings only for explaining "why"
- **Style**: Latest language features, minimal globals, initialization where state is used
- **Testing**: Self-contained tests manage their own state, non-intrusive harnesses, separated business logic

## Development Process

1. **Understand First**: Analyze codebase structure, state ownership, and component boundaries
2. **Design Simply**: Propose the most elegant solution, with alternatives for significant trade-offs
3. **Implement Cleanly**: Write concise code following design principles, then simplify further
4. **Verify Thoroughly**: Run tests that respect the separation between logic and test harnesses
5. **Iterate Based on Feedback**: Reconsider approaches and look for additional simplifications
