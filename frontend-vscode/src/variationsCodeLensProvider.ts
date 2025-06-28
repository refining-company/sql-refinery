import * as vscode from 'vscode';
import { VariationsProvider } from './variationsDocumentProvider';

export class VariationsCodeLensProvider implements vscode.CodeLensProvider {
  private _onDidChangeCodeLenses = new vscode.EventEmitter<void>();
  readonly onDidChangeCodeLenses = this._onDidChangeCodeLenses.event;
  
  constructor(private variationsProvider: VariationsProvider) {}

  async provideCodeLenses(document: vscode.TextDocument): Promise<vscode.CodeLens[]> {
    // Only provide code lenses for our virtual SQL documents
    if (document.uri.scheme !== 'sql-refinery-variations') {
      return [];
    }

    // Extract groupId from document name: editor.sql:variation-N
    const match = document.uri.path.match(/variation-(\d+)/);
    const groupId = match ? match[1] : 'current';
    const metadata = this.variationsProvider.getVariantMetadata(groupId);
    
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
        command: 'sql-refinery.peekLocations',
        arguments: [{
          locations: variant.locations,
          groupId: groupId,
          position: peekPosition
        }],
        tooltip: 'Peek at all locations where this variation appears'
      });
      codeLenses.push(locationsLens);

      // Show native diff lens
      const diffLens = new vscode.CodeLens(range, {
        title: '↔ Show diff',
        command: 'sql-refinery.showNativeDiff',
        arguments: [{ 
          variant, 
          originalSQL: this.variationsProvider.getOriginalSQL(groupId),
          groupId,
          variantIndex: variant.variantIndex
        }],
        tooltip: 'Show differences in native diff editor'
      });
      codeLenses.push(diffLens);
      
      // Apply variation lens
      const applyLens = new vscode.CodeLens(range, {
        title: '✓ Apply',
        command: 'sql-refinery.applyVariation',
        arguments: [{ variant, groupId: groupId }],
        tooltip: 'Replace current SQL with this variation'
      });
      codeLenses.push(applyLens);
    });

    return codeLenses;
  }
}