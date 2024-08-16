import src


if __name__ == "__main__":
    logic = src.logic.Logic(codebase_path=".submodules/playground/code/codebase")
    logic.analyse(editor_path=".submodules/playground/code/editor.sql")
