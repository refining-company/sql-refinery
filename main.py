import src
import textwrap


if __name__ == "__main__":
    logic = src.logic.Logic(codebase_path=".submodules/playground/code/codebase")
    suggestions = logic.compare_codebases(editor_path=".submodules/playground/code/editor.sql")

    # debug output
    for suggestion in suggestions:
        print(
            "{file}:{start_row}:{start_col}-{end_row}:{end_col}\n"
            "{op}\n\n"
            "Alternatives freq={freq} sim={score}\n"
            "{alts}\n\n=======================\n".format(
                file=suggestion.op.file,
                start_row=suggestion.op.node.start_point.row + 1,
                start_col=suggestion.op.node.start_point.column + 1,
                end_row=suggestion.op.node.end_point.row + 1,
                end_col=suggestion.op.node.end_point.column + 1,
                op=suggestion.op.node.text.decode("utf-8"),
                freq=suggestion.freq,
                score=suggestion.score,
                alts=textwrap.indent("\n\n".join(n.node.text.decode("utf-8") for n in suggestion.alt), prefix="\t"),
            )
        )
