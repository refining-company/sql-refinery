import * as vscode from 'vscode';

import { Expression, Variation, getMockVariations } from './mockData';
import { Logger } from '../logger';

let log: Logger = new Logger(module.filename);

export function initVariations(context: vscode.ExtensionContext) {
  log.info('initVariations: starting extension initialization');
  const stateManager = new VariationsState();
  context.subscriptions.push(stateManager);
  log.info('initVariations: state manager created');

  // Set up document event listeners - filter to SQL files only
  context.subscriptions.push(
    vscode.workspace.onDidOpenTextDocument((document) => {
      if (document.languageId === 'sql' && document.uri.scheme === 'file') {
        stateManager.updateVariations(document.uri, getMockVariations(document));
      }
    }),
    vscode.workspace.onDidChangeTextDocument(({ document }) => {
      if (document.languageId === 'sql' && document.uri.scheme === 'file') {
        stateManager.updateVariations(document.uri, getMockVariations(document));
      }
    })
  );

  log.info('initVariations: creating VariationsFeature');
  new VariationsFeature(context, stateManager);

  // Process already-open documents (after VariationsFeature subscribes)
  log.info(`initVariations: processing ${vscode.workspace.textDocuments.length} open documents`);
  vscode.workspace.textDocuments.forEach((document) => {
    if (document.languageId === 'sql' && document.uri.scheme === 'file') {
      stateManager.updateVariations(document.uri, getMockVariations(document));
    }
  });

  log.info('initVariations: extension initialization complete');
}

class VariationsState {
  private variationsMap: Map<string, Variation[]> = new Map<string, Variation[]>();
  private _onDidUpdateVariations = new vscode.EventEmitter<{ uri: vscode.Uri; variations: Variation[] }>();
  readonly onDidUpdateVariations = this._onDidUpdateVariations.event;

  updateVariations(uri: vscode.Uri, variations: Variation[]): void {
    log.info(`StateManager: updating ${uri.fsPath} with ${variations.length} variations`);
    this.variationsMap.set(uri.fsPath, variations);
    this._onDidUpdateVariations.fire({ uri, variations });
  }

  getVariations(uri: vscode.Uri): Variation[] | undefined {
    return this.variationsMap.get(uri.fsPath);
  }

  dispose(): void {
    this._onDidUpdateVariations.dispose();
  }
}

class VariationsFeature {
  private diagnosticsProvider: DiagnosticsProvider;
  private codeLensProvider: CodeLensProvider;
  private variationsExplorerFeature: VariationsExplorerFeature;

  constructor(context: vscode.ExtensionContext, private stateManager: VariationsState) {
    // Set up UI elements
    this.variationsExplorerFeature = new VariationsExplorerFeature(context, stateManager);
    this.diagnosticsProvider = new DiagnosticsProvider(context, 'sql-refinery-variations');
    this.codeLensProvider = new CodeLensProvider(context);

    // Subscribe to state changes
    context.subscriptions.push(
      stateManager.onDidUpdateVariations(({ uri, variations }) => {
        log.info(`VariationsFeature: received ${variations.length} variations for ${uri.fsPath}`);
        this.updateDiagnostic(uri, variations);
        this.updateCodeLens(uri, variations);
      })
    );

    context.subscriptions.push(
      vscode.commands.registerCommand(
        'sql-refinery.variations.show',
        this.variationsExplorerFeature.commandShow.bind(this.variationsExplorerFeature)
      ),
      vscode.commands.registerCommand('sql-refinery.variations.ignore', () => {
        // TODO: potentially cash on client side that these warning should be ignored
      })
    );
  }

  private updateDiagnostic(uri: vscode.Uri, variations: Variation[]): void {
    log.info(`updateDiagnostic: creating diagnostics for ${uri.fsPath}`);
    const diagnostics: vscode.Diagnostic[] = [];

    variations.forEach((variation, index) => {
      const diagnostic = new vscode.Diagnostic(
        variation.this.location.range,
        `Variations found: ${variation.others.length + 1} with ${Math.round(variation.similarity * 100)}% similarity`,
        vscode.DiagnosticSeverity.Information
      );
      diagnostic.code = index;
      diagnostic.source = 'sql-refinery';
      diagnostic.relatedInformation = variation.others.map(
        (expr, idx) =>
          new vscode.DiagnosticRelatedInformation(
            new vscode.Location(vscode.Uri.file(expr.location.file), expr.location.range),
            `Location ${idx + 1}`
          )
      );
      diagnostics.push(diagnostic);
    });
    log.info(`updateDiagnostic: setting ${diagnostics.length} diagnostics for ${uri.fsPath}`);
    this.diagnosticsProvider.updateDiagnostics(uri, diagnostics);
  }

  private updateCodeLens(uri: vscode.Uri, variations: Variation[]): void {
    log.info(`updateCodeLens: creating code lenses for ${uri.fsPath}`);
    const codeLenses: vscode.CodeLens[] = [];

    variations.forEach((variation, index) => {
      const showLens = new vscode.CodeLens(variation.this.location.range, {
        title: `→ Show ${variation.others.length + 1} variations`,
        command: 'sql-refinery.variations.show',
        arguments: [uri, index],
        tooltip: 'Show all variations of this code in side panel',
      });
      codeLenses.push(showLens);

      const ignoreLens = new vscode.CodeLens(variation.this.location.range, {
        title: '× Ignore',
        command: 'sql-refinery.variations.ignore',
        tooltip: 'Ignore this variation',
      });
      codeLenses.push(ignoreLens);
    });
    log.info(`updateCodeLens: setting ${codeLenses.length} code lenses for ${uri.fsPath}`);
    this.codeLensProvider.updateCodeLenses(uri, codeLenses);
  }
}

class VariationsExplorerFeature {
  private codeLensProvider: CodeLensProvider;

  constructor(context: vscode.ExtensionContext, private stateManager: VariationsState) {
    // Code lenses
    this.codeLensProvider = new CodeLensProvider(context, 'sql-refinery-explorer', 'sql');

    // Virtual documents
    new TextDocumentContentProvider(context, 'sql-refinery-explorer', this.renderExplorerContent.bind(this));
    new TextDocumentContentProvider(context, 'sql-refinery-explorer-diff', this.renderDiffContent.bind(this));

    // Commands
    context.subscriptions.push(
      vscode.commands.registerCommand('sql-refinery.variations.explorer.peek', this.commandPeek.bind(this)),
      vscode.commands.registerCommand('sql-refinery.variations.explorer.diff', this.commandDiff.bind(this)),
      vscode.commands.registerCommand('sql-refinery.variations.explorer.apply', () => {
        // TODO: implement apply logic
      })
    );
  }

  async commandShow(uri: vscode.Uri, id: number) {
    const explorerUri = vscode.Uri.parse(`sql-refinery-explorer:${uri.fsPath}/variation-${id}`);
    const doc = await vscode.workspace.openTextDocument(explorerUri);
    await vscode.window.showTextDocument(doc, { viewColumn: vscode.ViewColumn.Beside, preview: false });
    await vscode.languages.setTextDocumentLanguage(doc, 'sql');
  }

  async commandPeek(expr: Expression, uri: vscode.Uri, position: vscode.Position) {
    const locations = [new vscode.Location(vscode.Uri.file(expr.location.file), expr.location.range)];
    await vscode.commands.executeCommand('editor.action.peekLocations', uri, position, locations);
  }

  async commandDiff(file: string, indVariation: number, indExpr: number) {
    const originalUri = vscode.Uri.parse(`sql-refinery-explorer-diff:${file}/variation-${indVariation}/original`);
    const selectedUri = vscode.Uri.parse(`sql-refinery-explorer-diff:${file}/variation-${indVariation}/${indExpr}`);
    const originalDoc = await vscode.workspace.openTextDocument(originalUri);
    const selectedDoc = await vscode.workspace.openTextDocument(selectedUri);
    await vscode.languages.setTextDocumentLanguage(originalDoc, 'sql');
    await vscode.languages.setTextDocumentLanguage(selectedDoc, 'sql');
    await vscode.commands.executeCommand('vscode.diff', originalUri, selectedUri, 'Original ↔ Selected');
  }

  async renderDiffContent(uri: vscode.Uri): Promise<string> {
    const match = uri.path.match(/(.+)\/variation-(\d+)\/(original|\d+)$/);
    if (!match) return '';

    const filePath = match[1];
    const variationInd = parseInt(match[2]);
    const otherInd = match[3];
    const variation = this.stateManager.getVariations(vscode.Uri.file(filePath))?.[variationInd];
    if (!variation) return '';

    if (otherInd === 'original') {
      return variation.this.sql;
    } else {
      return variation.others[parseInt(otherInd)]?.sql || '';
    }
  }

  async renderExplorerContent(uri: vscode.Uri): Promise<string> {
    const match = uri.path.match(/(.+)\/variation-(\d+)$/);
    if (!match) return '';

    const variationFile = match[1];
    const variationInd = parseInt(match[2]);
    const variation = this.stateManager.getVariations(vscode.Uri.file(variationFile))?.[variationInd];
    const others = variation?.others;
    if (!others) return '';

    const lines: string[] = [];
    const codeLenses: vscode.CodeLens[] = [];

    lines.push('-- SQL-Refinery');
    lines.push('-- Expression variations found in the codebase');
    lines.push('');

    others.forEach((expr: Expression, exprInd) => {
      // Text
      lines.push(`-- Variation ${exprInd + 1}`);
      const rangeLenses = new vscode.Range(lines.length, 0, lines.length, 0);
      expr.sql.split('\n').forEach((line) => lines.push(line));
      const positionPeek = new vscode.Position(lines.length - 1, 0);
      lines.push('');

      // CodeLens
      codeLenses.push(
        new vscode.CodeLens(rangeLenses, {
          title: `→ Peek locations`,
          command: 'sql-refinery.variations.explorer.peek',
          arguments: [expr, uri, positionPeek],
        }),
        new vscode.CodeLens(rangeLenses, {
          title: `↔ Show diff`,
          command: 'sql-refinery.variations.explorer.diff',
          arguments: [variationFile, variationInd, exprInd],
        }),
        new vscode.CodeLens(rangeLenses, {
          title: `✓ Apply`,
          command: 'sql-refinery.variations.explorer.apply',
        })
      );
    });

    this.codeLensProvider.updateCodeLenses(uri, codeLenses);

    return lines.join('\n');
  }
}

// Thin interfaces with VSCode Extension API

class DiagnosticsProvider {
  private diagnosticsCollection: vscode.DiagnosticCollection;

  constructor(context: vscode.ExtensionContext, name: string) {
    this.diagnosticsCollection = vscode.languages.createDiagnosticCollection(name);
    context.subscriptions.push(this.diagnosticsCollection);
  }

  updateDiagnostics(uri: vscode.Uri, diagnostics: vscode.Diagnostic[]) {
    this.diagnosticsCollection.set(uri, diagnostics);
  }
}

class CodeLensProvider implements vscode.CodeLensProvider {
  private codeLensMap: Map<string, vscode.CodeLens[]> = new Map<string, vscode.CodeLens[]>();

  constructor(context: vscode.ExtensionContext, scheme: string = 'file', language: string = 'sql') {
    context.subscriptions.push(vscode.languages.registerCodeLensProvider({ scheme, language }, this));
  }

  updateCodeLenses(uri: vscode.Uri, codeLenses: vscode.CodeLens[]): void {
    this.codeLensMap.set(uri.fsPath, codeLenses);
  }

  provideCodeLenses(document: vscode.TextDocument): vscode.CodeLens[] {
    return this.codeLensMap.get(document.uri.fsPath) || [];
  }
}

class TextDocumentContentProvider implements vscode.TextDocumentContentProvider {
  private _provideTextDocumentContent: CallableFunction;

  constructor(context: vscode.ExtensionContext, name: string, content: CallableFunction) {
    context.subscriptions.push(vscode.workspace.registerTextDocumentContentProvider(name, this));
    this._provideTextDocumentContent = content;
  }

  async provideTextDocumentContent(uri: vscode.Uri): Promise<string> {
    return this._provideTextDocumentContent(uri);
  }
}
