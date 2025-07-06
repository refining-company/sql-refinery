import * as vscode from 'vscode';
import { Variation, getMockVariations } from './mockData';

export { Variation };

export function variationsToDiagnostics(variations: Variation[]): vscode.Diagnostic[] {
  const diagnostics: vscode.Diagnostic[] = [];
  
  variations.forEach((variation, index) => {
    const totalVariations = variation.others.length + 1;
    const diagnostic = new vscode.Diagnostic(
      variation.this.location.range,
      `${totalVariations} variation${totalVariations > 1 ? 's' : ''} found (${Math.round(variation.similarity * 100)}% similar)`,
      vscode.DiagnosticSeverity.Information
    );
    
    diagnostic.code = index.toString();
    diagnostic.source = 'sql-refinery';
    
    const allExpressions = [variation.this, ...variation.others];
    diagnostic.relatedInformation = allExpressions.map((expr, idx) => 
      new vscode.DiagnosticRelatedInformation(
        new vscode.Location(
          vscode.Uri.file(expr.location.file),
          expr.location.range
        ),
        `Variation ${idx + 1}: ${expr.alias || 'unnamed'}`
      )
    );
    
    diagnostics.push(diagnostic);
  });
  
  return diagnostics;
}

export function getVariationByGroupId(groupId: string, variations: Variation[]): Variation | undefined {
  const index = parseInt(groupId);
  return variations[index];
}



// Setup and detection

export let currentVariations: Variation[] = [];

export function setCurrentVariations(variations: Variation[]): void {
  currentVariations = variations;
}

export function getCurrentVariations(): Variation[] {
  return currentVariations;
}

export function initDiagnostics(context: vscode.ExtensionContext): vscode.DiagnosticCollection {
  const diagnosticCollection = vscode.languages.createDiagnosticCollection('sql-refinery-variations');
  context.subscriptions.push(diagnosticCollection);

  setupVariationDetection(context, diagnosticCollection);
  return diagnosticCollection;
}

function setupVariationDetection(context: vscode.ExtensionContext, diagnosticCollection: vscode.DiagnosticCollection) {
  const updateDiagnostics = (document: vscode.TextDocument) => {
    if (document.languageId !== 'sql' || document.uri.scheme === 'sql-refinery-variations') {
      return;
    }

    const variations = getMockVariations(document);
    setCurrentVariations(variations);
    
    const diagnostics = variationsToDiagnostics(variations);
    diagnosticCollection.set(document.uri, diagnostics);

    triggerCodeLensRefresh();
  };

  context.subscriptions.push(
    vscode.workspace.onDidOpenTextDocument(updateDiagnostics),
    vscode.workspace.onDidChangeTextDocument((e) => updateDiagnostics(e.document))
  );

  vscode.workspace.textDocuments.forEach(updateDiagnostics);
}

let codeLensRefreshCallback: (() => void) | null = null;

export function setCodeLensRefreshCallback(callback: () => void): void {
  codeLensRefreshCallback = callback;
}

function triggerCodeLensRefresh(): void {
  if (codeLensRefreshCallback) {
    codeLensRefreshCallback();
  }
}

// Main initialization

export function initVariations(context: vscode.ExtensionContext): void {
  const diagnosticCollection = initDiagnostics(context);
  
  const { initShowJourney, showVariationsCommand } = require('./variationsShow');
  initShowJourney(context, diagnosticCollection);
  
  const { initExploreJourney } = require('./variationsExplore');
  const variationsProvider = initExploreJourney(context);
  
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-refinery.showVariations', (args) => 
      showVariationsCommand(args, context, variationsProvider)
    ),
    vscode.commands.registerCommand('sql-refinery.ignoreVariation', (args) => {
      vscode.window.showInformationMessage(`Ignored variation group ${args.groupId}`);
    })
  );
}