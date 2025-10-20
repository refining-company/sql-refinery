# Backend Streamlining Plan

## Overview
Standardize field naming, reduce coupling between pipeline stages, eliminate boilerplate code.

## Staged Implementation

### Stage 0: Add Missing Snapshot for model.build()  NEXT
**Goal**: Complete pipeline observability before making changes

**Changes**:
- Add `src.model.build` to `patch_pipeline()` in `test_sessions.py`
- Define terminal classes for model layer snapshots
- Run tests to generate baseline snapshots

**Expected Impact**:
- New snapshot files: `src.model.build.*.true.json`
- No changes to existing snapshots
- Validates current model layer output

**Files Modified**:
- `backend/tests/test_sessions.py` - add model.build capture

---

### Stage 1: Rename model Fields with `_` Prefix
**Goal**: Mark pipeline-linking fields as private/terminal

**Changes**:
- `model.Column.code` ’ `model.Column._code`
- `model.Expression.code` ’ `model.Expression._code`
- Update all references in `model.py` (build functions use these fields internally)

**Expected Impact**:
- **model.build snapshots**: `code`/`_code` field renamed but content identical
- **variations.build snapshots**: Should be UNCHANGED (variations doesn't access `.code` fields directly)
- **exchange snapshots**: BREAKING CHANGE - `.code` arrays will no longer be serialized to frontend (serialise strips `_` fields)

**Frontend Impact**:
- Current behavior: Frontend receives full `code` arrays in variations data
- After change: Frontend will NOT receive them (aligns with server.py TODO comment lines 42-44)
- This is intentional - reduces payload size

**Files Modified**:
- `backend/src/model.py` - field renames
- `backend/tests/test_sessions.py` - update snapshots

---

### Stage 2: Standardize Location.__hash__
**Goal**: Use tuple-based hashing instead of string-based

**Changes**:
- `Location.__hash__`: `hash(repr(self))` ’ `hash((self.file, self.range))`

**Expected Impact**:
- **All snapshots**: UNCHANGED (hash values not in snapshots, only used for deduplication)
- Pure internal refactor

**Files Modified**:
- `backend/src/code.py`

---

### Stage 3: Create Base Classes
**Goal**: Centralize common patterns, eliminate duplicated __repr__ and __hash__

**Changes**:
- Add `@dataclass(frozen=True) class _Syntactic` base to code.py
  - Implements: `__hash__` using `self.location`
  - Implements: `__repr__` with standardized format
- Add `@dataclass(frozen=True) class _Semantic` base to model.py
  - Implements: standardized `__repr__` pattern
- Update classes to inherit from bases, remove redundant methods

**Expected Impact**:
- **All snapshots**: UNCHANGED (repr output stays identical)
- Significant code reduction, no behavior change

**Files Modified**:
- `backend/src/code.py`
- `backend/src/model.py`

---

### Stage 4: Simplify Terminal Handling in Tests
**Goal**: Use `_` convention to auto-determine terminal fields in simplify()

**Changes**:
- Update `simplify()` to automatically treat fields starting with `_` as terminal
- Simplify terminal class lists in `patch_pipeline()`
- Consider `@terminal` decorator for classes

**Expected Impact**:
- **All snapshots**: UNCHANGED (terminal behavior stays same, just determined automatically)
- Test code becomes more maintainable
- Future dataclass changes won't require manual terminal list updates

**Files Modified**:
- `backend/tests/test_sessions.py`

---

## Key Findings Summary

### Current Issues Identified
1. **Inconsistent field naming**: `code.*._node` uses `_` prefix, but `model.*.code` doesn't (both are pipeline links)
2. **Unnecessary coupling**: `model.Column.code` and `model.Expression.code` hold full lists of syntactic objects
3. **Fragile terminal handling**: `simplify()` requires manual terminal class lists in tests
4. **Duplicated boilerplate**: Each class manually implements `__repr__`, `__hash__` with similar patterns
5. **Missing snapshot coverage**: model.build() not captured in tests

### Snapshot Analysis
From `src.variations.build.1.true.json`:
- `model.Expression.code` arrays are currently INCLUDED in serialized output to frontend
- Server.py comment (lines 42-44) acknowledges this needs filtering
- Stage 1 will implement this filtering automatically via `_` prefix convention

## Implementation Order
1.  NEXT: Stage 0 - Add model.build snapshot
2. Stage 1 - Rename to `_` prefix (breaking change for frontend payload, but intentional)
3. Stage 2 - Location hash cleanup (quick win)
4. Stage 3 - Base classes (major code reduction)
5. Stage 4 - Test improvements
