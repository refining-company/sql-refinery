import * as vscode from 'vscode';
import * as path from 'path';
import { getCurrentVariations, getVariationByGroupId, setCodeLensRefreshCallback } from './variations';
import { variationToVirtualDocumentVariants } from './variationsExplore';

// Show all variations in the current document
export class InlineVariationsCodeLensProvider implements vscode.CodeLensProvider {
  private diagnosticsCollection: vscode.DiagnosticCollection;
  private _onDidChangeCodeLenses = new vscode.EventEmitter<void>();
  readonly onDidChangeCodeLenses = this._onDidChangeCodeLenses.event;

  constructor(diagnosticsCollection: vscode.DiagnosticCollection) {
    this.diagnosticsCollection = diagnosticsCollection;
  }

  async provideCodeLenses(document: vscode.TextDocument): Promise<vscode.CodeLens[]> {
    if (document.languageId !== 'sql') {
      return [];
    }

    const codeLenses: vscode.CodeLens[] = [];
    const diagnostics = this.diagnosticsCollection.get(document.uri);

    if (!diagnostics) {
      return [];
    }

    for (const diagnostic of diagnostics) {
      if (diagnostic.source === 'sql-refinery' && diagnostic.code) {
        const groupId = diagnostic.code.toString();
        
        const variations = getCurrentVariations();
        const variationIndex = parseInt(groupId);
        const variation = variations[variationIndex];
        
        const totalCount = variation ? variation.others.length + 1 : 0;
        
        const lensPosition = new vscode.Position(diagnostic.range.start.line, 0);
        const lensRange = new vscode.Range(lensPosition, lensPosition);

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

  // Method to trigger refresh from external modules
  refreshCodeLenses(): void {
    this._onDidChangeCodeLenses.fire();
  }
}

export async function showVariationsCommand(
  args: { groupId: string; currentRange: vscode.Range },
  context: vscode.ExtensionContext,
  variationsProvider: any
): Promise<void> {
  const { groupId, currentRange } = args;
  
  const variation = getVariationByGroupId(groupId, getCurrentVariations());
  if (!variation) {
    vscode.window.showErrorMessage(`No variation found for group ${groupId}`);
    return;
  }
  
  const variants = variationToVirtualDocumentVariants(variation);
  variationsProvider.setVariants(groupId, variants);

  const activeEditor = vscode.window.activeTextEditor;
  if (!activeEditor) {
    return;
  }

  const originalSQL = variation.this.sql;
  variationsProvider.setOriginalSQL(groupId, originalSQL);

  context.workspaceState.update(`currentRange-${groupId}`, {
    start: { line: currentRange.start.line, character: currentRange.start.character },
    end: { line: currentRange.end.line, character: currentRange.end.character },
    documentUri: activeEditor.document.uri.toString(),
  });

  const currentFileName = path.basename(activeEditor.document.fileName);
  const virtualFileName = `${currentFileName}:variation-${groupId}`;

  const variationsUri = vscode.Uri.parse(`sql-refinery-variations:${virtualFileName}`);
  const doc = await vscode.workspace.openTextDocument(variationsUri);
  await vscode.window.showTextDocument(doc, {
    viewColumn: vscode.ViewColumn.Beside,
    preview: false,
  });

  await vscode.languages.setTextDocumentLanguage(doc, 'sql');
}

export function initShowJourney(context: vscode.ExtensionContext, diagnosticCollection: vscode.DiagnosticCollection): InlineVariationsCodeLensProvider {
  const inlineVariationsCodeLensProvider = new InlineVariationsCodeLensProvider(diagnosticCollection);
  
  setCodeLensRefreshCallback(() => inlineVariationsCodeLensProvider.refreshCodeLenses());
  
  context.subscriptions.push(
    vscode.languages.registerCodeLensProvider({ scheme: 'file', language: 'sql' }, inlineVariationsCodeLensProvider)
  );

  return inlineVariationsCodeLensProvider;
}