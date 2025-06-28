import * as vscode from 'vscode';
import { VariationsProvider } from './variationsDocumentProvider';
import { generateVirtualDocumentCodeLenses } from './variations';

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

    // Use the translation layer to generate code lenses
    const originalSQL = this.variationsProvider.getOriginalSQL(groupId);
    return generateVirtualDocumentCodeLenses(metadata, groupId, originalSQL);
  }
}