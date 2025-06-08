import * as vscode from 'vscode';
import * as path from 'path';
import { VariantsProvider } from './variantsDocumentProvider';

export class VariantsCodeLensProvider implements vscode.CodeLensProvider {
  private _onDidChangeCodeLenses = new vscode.EventEmitter<void>();
  readonly onDidChangeCodeLenses = this._onDidChangeCodeLenses.event;
  
  constructor(private variantsProvider: VariantsProvider) {}

  async provideCodeLenses(document: vscode.TextDocument, token: vscode.CancellationToken): Promise<vscode.CodeLens[]> {
    // Only provide code lenses for our virtual SQL documents
    if (document.uri.scheme !== 'sql-refinery') {
      return [];
    }

    // For sql-refinery:alternatives, use 'current' as groupId
    const groupId = 'current';
    const metadata = this.variantsProvider.getVariantMetadata(groupId);
    
    if (!metadata) {
      return [];
    }

    const codeLenses: vscode.CodeLens[] = [];

    metadata.forEach(({ startLine, endLine, variant }) => {
      const range = new vscode.Range(startLine - 1, 0, startLine - 1, 0);
      
      // Locations lens
      const locationCount = variant.locations.length;
      
      // Position peek at the bottom of the variant code
      const peekPosition = new vscode.Position(endLine, 0);
      
      const locationsLens = new vscode.CodeLens(range, {
        title: `→ Peek ${locationCount} locations`,
        command: 'sql-insights.peekLocations',
        arguments: [{
          locations: variant.locations,
          groupId: 'current',
          position: peekPosition
        }],
        tooltip: 'Peek at all locations where this variant appears'
      });
      codeLenses.push(locationsLens);

      // Toggle diff lens
      const variantIndex = variant.variantIndex || 1;
      const isInDiffMode = this.variantsProvider.isInDiffMode(variantIndex);
      const diffLens = new vscode.CodeLens(range, {
        title: isInDiffMode ? '↔ Hide diff' : '↔ Show diff',
        command: 'sql-insights.toggleDiff',
        arguments: [{ variant, groupId: 'current', variantIndex }],
        tooltip: isInDiffMode ? 'Hide inline diff' : 'Show inline diff'
      });
      codeLenses.push(diffLens);
      
      // Apply variant lens
      const applyLens = new vscode.CodeLens(range, {
        title: '✓ Apply',
        command: 'sql-insights.applyVariant',
        arguments: [{ variant, groupId: 'current' }],
        tooltip: 'Replace current SQL with this variant'
      });
      codeLenses.push(applyLens);
    });

    return codeLenses;
  }
}