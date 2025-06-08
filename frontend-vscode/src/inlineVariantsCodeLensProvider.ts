import * as vscode from 'vscode';
import * as path from 'path';
import { getVariantsForGroup } from './mockData';

export class InlineVariantsCodeLensProvider implements vscode.CodeLensProvider {
  private diagnosticsCollection: vscode.DiagnosticCollection;
  private _onDidChangeCodeLenses = new vscode.EventEmitter<void>();
  readonly onDidChangeCodeLenses = this._onDidChangeCodeLenses.event;

  constructor(diagnosticsCollection: vscode.DiagnosticCollection) {
    this.diagnosticsCollection = diagnosticsCollection;
  }

  async provideCodeLenses(document: vscode.TextDocument, token: vscode.CancellationToken): Promise<vscode.CodeLens[]> {
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
      if (diagnostic.source === 'sql-refinery' && diagnostic.code === 'inconsistency') {
        // Determine groupId based on diagnostic range (mock implementation)
        const groupId = diagnostic.range.start.line < 10 ? 'region-clustering' : 'industry-classification';
        const variants = getVariantsForGroup(groupId);
        
        // Position code lenses just above the diagnostic range
        const lensPosition = new vscode.Position(diagnostic.range.start.line, 0);
        const lensRange = new vscode.Range(lensPosition, lensPosition);

        // Add main action lens
        const showVariantsLens = new vscode.CodeLens(lensRange, {
          title: `→ Show ${variants.length} alternatives`,
          command: 'sql-insights.showVariantsEditor',
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
          command: 'sql-insights.ignoreVariant',
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