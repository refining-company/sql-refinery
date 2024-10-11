# Setup

TODO: On refresh (either VS Code with extension, or debugging) the VSCode debugpy does not restart.
Server debugpy failes to connect to VSCode debugpy and crashes. This in turn crashes the
extension

TODO: I changed the code to

```
@server.feature(lsp.TEXT_DOCUMENT_CODE_LENS)
def code_lens_provider(params: lsp.CodeLensParams):
    document_uri = params.text_document.uri
    code_lenses = []

    # Retrieve diagnostics for the document
    suggestions = all_suggestions.get(document_uri, [])
    for suggestion in suggestions:
        title = f"Similar code snippets: {len(suggestion.others)} found"
        diagnostic_range = lsp.Range(
            start=lsp.Position(
                line=suggestion.this.node.start_point.row,
                character=suggestion.this.node.start_point.column,
            ),
            end=lsp.Position(
                line=suggestion.this.node.end_point.row,
                character=suggestion.this.node.end_point.column,
            ),
        )
        locations = []
        for other in suggestion.others:
            location_uri = (session.path_codebase / other.file).resolve().as_uri()
            location_range = lsp.Range(
                start=lsp.Position(line=other.node.start_point.row, character=other.node.start_point.column),
                end=lsp.Position(line=other.node.end_point.row, character=other.node.end_point.column),
            )
            locations.append(lsp.Location(uri=location_uri, range=location_range))

        # Create the CodeLens entry
        code_lens = lsp.CodeLens(
            range=diagnostic_range,
            command=lsp.Command(
                title=title,
                command="editor.action.peekLocations",
                arguments=[document_uri, diagnostic_range, locations, "peek"],
            ),
        )
        code_lenses.append(code_lens)

        # Optionally, store the alternatives for use in a command
        code_lens_data[(document_uri, diagnostic_range.start.line, diagnostic_range.start.character)] = (
            suggestion.others
        )

    return code_lenses
```

Now I'm getting a popup in VS Code where I debug it that says

`argument does not match one of these constraints: arg instanceof constraint, arg.constructor === constraint, nor constraint(arg) === true`
