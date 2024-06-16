# Setup

1. Initialise submodules (linked repos)

   ```bash
   git submodule init
   git submodule update
   ```

2. Create environment and install dependencies

   ```bash
   conda create --prefix ./.conda python=3.12 pytest -y
   conda activate ./.conda
   pip install tree-sitter
   pip install -e ./.submodules/tree-sitter-sql-bigquery
   ```

3. Configure VS Code `.vscode/settings.json`

   ```json
   {
     "python.testing.unittestEnabled": false,
     "python.testing.pytestEnabled": true,
     "python.testing.pytestArgs": ["tests"],
     "black-formatter.args": ["--config", "./pyproject.toml"],
     "files.exclude": {
       "**/.conda": true,
       "**/__pycache__": true,
       "**/.pytest_cache": true
     }
   }
   ```

4. Configure tasks `.vscode/tasks.json`

   This will allow `> Tasks: Run Task` in VSCode to launch tree-sitter playground in browser

   ```json
   {
     "version": "2.0.0",
     "tasks": [
       {
         "label": "Playground: tree-sitter-sql-bigquery",
         "type": "shell",
         "command": "${workspaceFolder}/.submodules/tree-sitter-sql-bigquery/playground/start.sh",
         "problemMatcher": []
       }
     ]
   }
   ```

# Overview

**`src/`** contains the entire logic.

- `sql.py` is in the lowest level. It abstracts some of the tree-sitter complexity
  by adding new node types (with "@" prefix) and helper functions.

  In the future, it should be able to provide an interface for all SQL dialects.

- `db.py` (doesn't exist yet) is in the lowest level too. It should abstract DB
  connectivity.

- `codebase.py` should link together the abstracted code AST (via `sql.py`) and the data
  model (via `db.py`) to create a computational tree.

- `checker.py` is the error checker that will use `codebase.py` to analyze computations
  and find similar but not exact matches, highlighting them as errors.

**`tests/`** will be for the unit tests. The approach will be similar to the one used by
[tree-sitter](https://github.com/ilyakochik/tree-sitter-sql-bigquery/blob/main/test/corpus/analytic_function.txt):

- For each package in `src/`, there will be a corresponding package in `tests/` (e.g., `tests/sql/`).

- In each test package, there will be some input data (e.g., `tests/sql/input.sql` file with multiple SQL
  statements).

- The test file (e.g., `tests/sql/test_sql.py`) should be able to test a few key functions. For that:

  - It should be able to generate a reference answer (e.g., `sql.Tree` pickle of `sql.parse()`) and save
    it as `output.pickle`.

  - To run the test, it will run `sql.parse()` on `tests/sql/input.sql` and compare outputs
    with `output.pickle`. Each element in `output.pickle` should be treated as an independent test (e.g., by
    using [fixtures](https://docs.pytest.org/en/7.1.x/how-to/parametrize.html)).
