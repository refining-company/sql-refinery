# Cleanup

1. ~~Update `__str__` and `__repr__` in model to be aligned with src.code~~
2. Review variations to use model abstractions
3. `__str__` and `__repr__` in variations

# Features

1. Make replacement in frontend comply with formatting
2. Make replacement in frontend comply with local column names
3. Make test snapshots configurable so there is a config file (e.g. `variations.config.json`) that tracks which
   snapshots are used in assert, and which are just captured (maybe using wildcards on filenames)

# Architecture

## Workspace as Index ("Christmas Tree" Pattern)

**Concept:** Workspace is mutable container that flows through pipeline. Each layer decorates it with data.

### Evolution Stages

**v0: Full rebuild (current target)**
- Full pipeline rebuild on file change
- No persistence
- Layers mutate workspace, return nothing

**v1: Incremental updates (future)**
- Dependency-driven invalidation: File change → affected Queries → affected Expressions → Variations
- Track objects by file for granular updates
- Lazy map invalidation

**v2: Persistence (future)**
- Save only model layer (no tree-sitter `_node` references)
- Lazy re-parse code/sql layers on load
- Lazy-load file contents for large codebases

**v3: Async (future)**
- Lock during rebuild (simple approach)
- Consider copy-on-write for non-blocking reads later

### Workspace Structure (Three-Tier Access)

```python
workspace.layer.code          # Layer outputs (Tree, Semantics objects)
workspace.objects.model_expressions  # Flat typed collections
workspace.maps.code_expr_to_model    # Relationship mappings (lazy)
```

**Tier 1: Layer Outputs**
- `layer.sql` - SQL parse trees (not persisted, has _node)
- `layer.code` - Code AST (not persisted, has _node)
- `layer.model` - Semantics (persisted)

**Tier 2: Object Collections**
- `objects.model_expressions` - All model.Expression instances
- `objects.model_columns` - All model.Column instances
- Track by file in v1: `objects._expr_by_file`

**Tier 3: Relationship Maps (Lazy)**
- Common maps: Explicit properties (fast, type-safe)
- Generic maps: `map(from_type, to_type)` auto-introspection (flexible)
- Cached, invalidated on updates

### Design Decisions

**Mutability:** Mutable workspace (dataclasses are frozen, workspace is container)

**Layer returns:** Layers mutate workspace, optionally return object for backwards compat
- Eventually migrate to: `src.code.build(workspace)` returns nothing
- Access via: `workspace.layer.code`

**Reverse mappings:** Lazy properties with caching
- Build on first access
- Finalize before persistence (pre-build all)

**Generic maps:** Hybrid approach
- Explicit for common: `workspace.maps.code_expr_to_model`
- Generic for rare: `workspace.maps.map(code.Location, model.Expression)`
- Introspection-based, cached

**Circular imports:** Use `from __future__ import annotations` + `TYPE_CHECKING`

### Persistence Strategy

**Save:**
- Model layer only (no _node references)
- File contents (text)
- Pre-built maps

**Don't save:**
- SQL parse trees (_node)
- Code AST (_node)

**Load:**
- Restore model + maps
- Lazy re-parse sql/code if accessed

### Incremental Update Strategy (v1)

**Dependency cascade:**
1. File changes → identify affected `code.Query` objects
2. Rebuild queries → invalidate dependent `model.Expression` objects
3. Rebuild expressions → invalidate dependent `Variations`
4. Rebuild variations

**Tracking:**
- File → objects mapping
- Object → dependent objects (via introspection or explicit tracking)

### Open Questions

1. Dependency granularity: File-level or Expression-level?
2. Store code objects in workspace.objects? (Not persisted but available)
3. Incremental Tree updates: Mutable Tree or full rebuild?
4. Generic map direction: Always reverse `{from: [to]}` or smart cardinality?

### Implementation Notes

- Start simple (v0), add complexity incrementally
- Profile before optimizing (introspection vs explicit)
- Test `_node` pickling (likely fails, confirms strategy)
