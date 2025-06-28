import * as vscode from 'vscode';
import * as path from 'path';

// Global access to current variations (temporary during refactoring)
let getCurrentVariations: () => import('./mockData').Variation[] = () => [];

export class InlineVariationsCodeLensProvider implements vscode.CodeLensProvider {
  private diagnosticsCollection: vscode.DiagnosticCollection;
  private _onDidChangeCodeLenses = new vscode.EventEmitter<void>();
  readonly onDidChangeCodeLenses = this._onDidChangeCodeLenses.event;

  constructor(diagnosticsCollection: vscode.DiagnosticCollection) {
    this.diagnosticsCollection = diagnosticsCollection;
  }

  // Method to set current variations access
  setVariationsProvider(provider: () => import('./mockData').Variation[]) {
    getCurrentVariations = provider;
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
        
        // Try to find the variation using the new structure
        const variations = getCurrentVariations();
        const variationIndex = parseInt(groupId) - 1;
        const variation = variations[variationIndex];
        
        // Fall back to empty array if variation not found
        const variants = variation ? variation.others : [];
        
        // Calculate total count including current expression
        const totalCount = variation ? variation.others.length + 1 : variants.length;
        
        // Position code lenses just above the diagnostic range
        const lensPosition = new vscode.Position(diagnostic.range.start.line, 0);
        const lensRange = new vscode.Range(lensPosition, lensPosition);

        // Add main action lens
        const showVariationsLens = new vscode.CodeLens(lensRange, {
          title: `→ Show ${totalCount} variations`,
          command: 'sql-refinery.showVariations',
          arguments: [{
            groupId,
            currentRange: diagnostic.range
          }],
          tooltip: 'Show all variations in side panel'
        });
        codeLenses.push(showVariationsLens);
        
        // Add ignore lens
        const ignoreLens = new vscode.CodeLens(lensRange, {
          title: '× Ignore',
          command: 'sql-refinery.ignoreVariation',
          arguments: [{
            groupId,
            diagnosticRange: diagnostic.range
          }],
          tooltip: 'Ignore this variation'
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