# Features

1. Frontend: Make replacement comply with formatting
2. Frontend: Make replacement comply with local column names
3. Testing: Configurable snapshots (e.g. `variations.config.json`) for assertions vs captured output

# Future Architecture

## Current (v0): Full Rebuild

Workspace orchestrates 4-layer pipeline: SQL → Code → Model → Variations
- Full rebuild on file change
- Index system: `ws.new(obj)` registers, `ws.get(type)` retrieves
- Map system: `ws.map(fro, to, by=...)` for cross-layer lookups with multi-hop traversal

## Incremental Updates (v1)

Dependency-driven invalidation:
- File change → affected code.Query → affected model.Expression → Variations
- Track objects by file for granular updates
- Lazy map invalidation

## Persistence (v2)

Save model layer only (no tree-sitter `_node` references):
- Model layer + file contents + pre-built maps
- Lazy re-parse SQL/Code layers on load
- Lazy-load file contents for large codebases

## Async (v3)

- Lock during rebuild (simple approach)
- Consider copy-on-write for non-blocking reads later
