# Frontend-Backend Integration Plan

## Overview
The goal is to integrate the frontend VS Code extension with the backend LSP server to display SQL variations (similar expressions found across the codebase).

**Key Terminology Decision**: Use "variations" consistently instead of "inconsistencies"/"alternatives"/"variants".

## Phase 1: Clean Up Interfaces & MockData
- [x] Simplify `mockData.ts`:
  - [x] Keep only core interfaces: `Location`, `Column`, `Expression`, `Variation` (rename from `Alternative`)
  - [x] Remove `UIAlternative` interface (move UI concerns to translation layer)
  - [x] Remove legacy `MockVariant` and `MockDiagnostic` interfaces
  - [x] Keep helper functions minimal (only data transformation, no UI logic)

## Phase 2: Create Translation Layer
- [ ] Create `variations.ts` (rename from `inconsistencies.ts`):
  - [ ] Single responsibility: translate backend variations to VS Code UI elements
  - [ ] Handle variations → diagnostics conversion
  - [ ] Handle variations → code lenses conversion
  - [ ] Handle variations → virtual documents
  - [ ] Contain all UI-specific metadata enrichment

## Phase 3: Rename & Restructure Frontend and Backend
- [ ] Frontend file renames:
  - [ ] `inconsistencies.ts` → `variations.ts`
  - [ ] `variantsDocumentProvider.ts` → `variationsDocumentProvider.ts`
  - [ ] `variantsCodeLensProvider.ts` → `variationsCodeLensProvider.ts`
  - [ ] `inlineVariantsCodeLensProvider.ts` → `inlineVariationsCodeLensProvider.ts`
- [ ] Backend renaming:
  - [ ] Rename `Alternative` class to `Variation` in `logic.py`
  - [ ] Update all references to `Alternative` in backend code
  - [ ] Update function names (e.g., `find_inconsistencies` → `find_variations`)
  - [ ] Update variable names throughout backend
  - [ ] Update docstrings and comments to use "variations" terminology
- [ ] Update all frontend references:
  - [ ] Command names (e.g., `sql-refinery.showVariantsEditor` → `sql-refinery.showVariations`)
  - [ ] URI schemes (e.g., `sql-refinery-inconsistencies` → `sql-refinery-variations`)
  - [ ] Variable names throughout the codebase
  - [ ] User-facing messages to use "variations" terminology

## Phase 3.5: Test & Commit Renaming
- [ ] Run all tests (expect failures due to terminology changes):
  - [ ] Backend: `poetry run python -m pytest`
  - [ ] Frontend: `npm run test`
- [ ] Review test failures - should only be terminology changes:
  - [ ] Check that failures are due to "Alternative" → "Variation" renaming
  - [ ] Check that failures are due to "inconsistencies" → "variations" renaming
  - [ ] Visually verify the changes make sense
- [ ] Update snapshots:
  - [ ] Backend: Update snapshot files with new terminology
  - [ ] Frontend: `npm run test:update-snapshots`
- [ ] Re-run tests to ensure they pass
- [ ] Commit with message: "refactor: rename inconsistencies/alternatives to variations"

## Phase 4: Move UI Logic to Translation Layer
- [ ] In `variations.ts`:
  - [ ] Move logic from mockData.ts for creating diagnostics from Variation objects
  - [ ] Move logic for creating code lenses from Variation objects
  - [ ] Move logic for creating virtual document content
  - [ ] Create clean interfaces that take Variation[] and return VS Code UI elements
- [ ] Update all providers to use the new translation functions:
  - [ ] Update `variationsDocumentProvider.ts` to use new interfaces
  - [ ] Update `variationsCodeLensProvider.ts` to use new interfaces
  - [ ] Update `inlineVariationsCodeLensProvider.ts` to use new interfaces
- [ ] Ensure mockData.ts only contains data structures and mock data generation

## Phase 4.5: Test Translation Layer
- [ ] Run frontend tests to ensure UI logic migration worked
- [ ] Verify mock data still produces correct UI elements
- [ ] Test that all UI features still work with the new translation layer
- [ ] Commit with message: "refactor: move UI logic to variations.ts translation layer"

## Phase 5: Connect to Backend
- [ ] In `extension.ts`:
  - [ ] Create LSP client configuration
  - [ ] Connect to backend server on port (TBD)
  - [ ] Set up handlers for receiving variation data
- [ ] Create data flow:
  - [ ] Backend sends raw `Alternative` objects
  - [ ] Frontend receives and passes through translation layer
  - [ ] Remove hardcoded mock data calls
- [ ] Keep mock structure for testing purposes

## Phase 5: Test & Validate
- [ ] Run frontend tests: `npm run test`
- [ ] Compare snapshot diffs:
  - [ ] Structural changes expected (data flow)
  - [ ] UI behavior should remain the same
  - [ ] Terminology changes in messages
- [ ] Update snapshots where needed: `npm run test:update-snapshots`
- [ ] Manual testing:
  - [ ] Open SQL file
  - [ ] See blue squiggles for variations
  - [ ] Click "Show variations"
  - [ ] Test peek, diff, and apply actions

## Phase 6: Clean Up Backend
- [ ] Update `server.py`:
  - [ ] Remove diagnostic creation logic
  - [ ] Remove code lens creation logic  
  - [ ] Send raw `Alternative` objects as custom LSP messages
  - [ ] Keep the analysis pipeline unchanged
- [ ] Define custom LSP protocol:
  - [ ] Message type for variations data
  - [ ] Request/response for getting variations

## Design Principles
1. **Single source of truth**: Backend analyzes, frontend presents
2. **Clean interfaces**: Minimal data structures, no mixing of concerns
3. **Consistent terminology**: "Variations" everywhere
4. **Separation of concerns**: Backend = analysis, Frontend = presentation

## Current Issues to Address
- Frontend snapshot tests have glitches (noted by user)
- Mixed terminology throughout codebase
- Mock data is hardcoded instead of coming from backend
- Backend is creating UI elements (diagnostics, code lenses)

## Success Criteria
- [ ] Frontend receives variations from backend
- [ ] All UI features work as before
- [ ] Consistent "variations" terminology
- [ ] Clean separation of backend/frontend concerns
- [ ] Tests pass with updated snapshots