# Custom Instructions for GitHub Copilot

## About This Repository

This project is a Copilot for business intelligence analysts who work on large SQL codebases. It aims to enhance their
productivity and streamline SQL development workflows.

1.  **Backend**: A Python-based application that containes all the logic for SQL analysis.
2.  **Frontend**: A TypeScript VS Code extension. Provides the user interface using Language Server Protocol (LSP).

## Backend (Python)

- Located in `backend/src/`, entry point is `backend/src/server.py`.
- Uses Python 3.12.7.
- Pay attention to dependencies listed in `backend/requirements.txt`.
- Tests are located in `backend/tests/`, and uses `pytest` framework.

## Frontend (TypeScript)

- Located `frontend-vscode/src/`, entry point is `frontend-vscode/src/extension.ts`.
- Uses Node v20.18.0.
- Pay attention to dependencies listed in`package.json`
- Tests are located in `frontend-vscode/src/test/`.

## Coding Conventions

- Use `black` for Python code formatting and `prettier` for TypeScript.
- Write clear and concise commit messages. Use prefixes `feature:`, `refactor:`, `fix:`, `docs:`, `setup:`.
- Do not write inline comments, unless it is a critical business logic.
- Do not remove existing comments, unless they are outdated or incorrect.
- Use latest Python, Node and TypeScript features.
- Use a shorter variable naming whenever possible. For callable parameters use `fn`.

## Development Process

Follow these steps, ask for my confirmation at each step, and iterate until the task is complete:

1. Take in my request, understand the codebase, come up with one or several solutions.
2. Suggest naming conventions, code structure, and any other relevant details.
3. Implement the solution, then check if code could be simplified or made more elegant.
4. Find the correspoinding launch configuration in `launch.json` and run the code using python module launch.
5. Analyse the output, if there are errors or unexpected results, debug the code and propose improvements
