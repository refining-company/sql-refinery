import * as vscode from 'vscode';
import * as path from 'path';

// Global access to current alternatives (temporary during refactoring)
let getCurrentAlternatives: () => import('./mockData').UIAlternative[] = () => [];

export class InconsistencyCodeLensProvider implements vscode.CodeLensProvider {
  private diagnosticsCollection: vscode.DiagnosticCollection;
  private _onDidChangeCodeLenses = new vscode.EventEmitter<void>();
  readonly onDidChangeCodeLenses = this._onDidChangeCodeLenses.event;

  constructor(diagnosticsCollection: vscode.DiagnosticCollection) {
    this.diagnosticsCollection = diagnosticsCollection;
  }

  // Method to set current alternatives access
  setAlternativesProvider(provider: () => import('./mockData').UIAlternative[]) {
    getCurrentAlternatives = provider;
  }

  async provideCodeLenses(document: vscode.TextDocument): Promise<vscode.CodeLens[]> {
    // Only provide code lenses for SQL files
    if (document.languageId !== 'sql') {
      return [];
    }

    const codeLenses: vscode.CodeLens[] = [];
    const diagnostics = this.diagnosticsCollection.get(document.uri);

    if (!diagnostics) {
      return [];
    }

    // For each diagnostic with variants, create code lenses
    for (const diagnostic of diagnostics) {
      if (diagnostic.source === 'sql-refinery' && diagnostic.code) {
        // The diagnostic code is now the groupId
        const groupId = diagnostic.code.toString();
        
        // Try to find the alternative using the new structure
        const alternatives = getCurrentAlternatives();
        const alternative = alternatives.find(alt => alt.groupId === groupId);
        
        // Fall back to empty array if alternative not found
        const variants = alternative ? alternative.others : [];
        
        // Calculate total count including current expression
        const totalCount = alternative ? alternative.others.length + 1 : variants.length;
        
        // Position code lenses just above the diagnostic range
        const lensPosition = new vscode.Position(diagnostic.range.start.line, 0);
        const lensRange = new vscode.Range(lensPosition, lensPosition);

        // Add main action lens
        const showVariantsLens = new vscode.CodeLens(lensRange, {
          title: `→ Show ${totalCount} alternatives`,
          command: 'sql-refinery.showVariantsEditor',
          arguments: [{
            groupId,
            currentRange: diagnostic.range
          }],
          tooltip: 'Show all variants in side panel'
        });
        codeLenses.push(showVariantsLens);
        
        // Add ignore lens
        const ignoreLens = new vscode.CodeLens(lensRange, {
          title: '× Ignore',
          command: 'sql-refinery.ignoreVariant',
          arguments: [{
            groupId,
            diagnosticRange: diagnostic.range
          }],
          tooltip: 'Ignore this variant inconsistency'
        });
        codeLenses.push(ignoreLens);
      }
    }

    return codeLenses;
  }

}

// Mockup functions for development/demonstration purposes (no longer used)
// function mockupGroupIdFromRange(range: vscode.Range): string {
//   // Mock implementation: determine groupId based on line number
//   return range.start.line < 10 ? '1' : '2';
// }