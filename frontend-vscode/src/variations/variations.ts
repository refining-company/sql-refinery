import * as vscode from 'vscode';
import { basename } from 'path';

import { createLogger } from '../logger';

let log = createLogger(module.filename);
const uriUI = '⌬ [SQL Refinery]';

// Core interfaces matching Python backend structure
interface Location {
  file: string;
  range: vscode.Range;
}

interface Column {
  dataset: string | null;
  table: string | null;
  column: string | null;
}

interface Expression {
  location: Location;
  columns: Column[];
  alias: string | null;
  sql: string;
}

interface ExpressionGroup {
  expressions: Expression[];
  repr: string;
  columns: string[];
  reliability: number;
}

interface ExpressionVariation {
  group: ExpressionGroup;
  similarity: number;
}

interface ExpressionVariations {
  this: Expression;
  others: ExpressionVariation[];
}

export function initVariationsState(context: vscode.ExtensionContext): VariationsState {
  log.info('initVariationsState');
  const stateManager = new VariationsState();
  context.subscriptions.push(stateManager);
  log.info('initVariationsState: state manager created');

  log.info('initVariationsState: creating VariationsFeature');
  new VariationsFeature(context, stateManager);

  log.info('initVariationsState: complete');
  return stateManager;
}

export function registerVariationsHandler(client: any, stateManager: VariationsState) {
  log.info('registerVariationsHandler: registering notification handler');

  // Register notification handler from LSP server
  client.onNotification('sql-refinery/variations', (params: { uri: string; variations: any[] }) => {
    try {
      log.info(`Received ${params.variations.length} variations for ${params.uri}`);
      const uri = vscode.Uri.parse(params.uri);
      const variations = deserializeVariations(params.variations);
      log.info(`Deserialized ${variations.length} variations`);
      stateManager.updateVariations(uri, variations);
      log.info(`Updated state manager with variations`);
    } catch (error) {
      log.error(`Error handling variations notification: ${error}`);
    }
  });
  log.info('registerVariationsHandler: notification handler registered');
}

function deserializeVariations(data: any[]): ExpressionVariations[] {
  return data.map((item) => ({
    this: {
      location: {
        file: item.this.location.file,
        range: new vscode.Range(
          item.this.location.range.start_line,
          item.this.location.range.start_character,
          item.this.location.range.end_line,
          item.this.location.range.end_character
        ),
      },
      columns: item.this.columns,
      alias: item.this.alias,
      sql: item.this.sql,
    },
    others: item.others.map((other: any) => ({
      group: {
        expressions: other.group.expressions.map((expr: any) => ({
          location: {
            file: expr.location.file,
            range: new vscode.Range(
              expr.location.range.start_line,
              expr.location.range.start_character,
              expr.location.range.end_line,
              expr.location.range.end_character
            ),
          },
          columns: expr.columns,
          alias: expr.alias,
          sql: expr.sql,
        })),
        repr: other.group.repr,
        columns: other.group.columns,
        reliability: other.group.reliability,
      },
      similarity: other.similarity,
    })),
  }));
}

class VariationsState {
  private variationsMap: Map<string, ExpressionVariations[]> = new Map<string, ExpressionVariations[]>();
  private _onDidUpdateVariations = new vscode.EventEmitter<{ uri: vscode.Uri; variations: ExpressionVariations[] }>();
  readonly onDidUpdateVariations = this._onDidUpdateVariations.event;

  updateVariations(uri: vscode.Uri, variations: ExpressionVariations[]): void {
    log.info(`StateManager: updating ${uri.fsPath} with ${variations.length} variations`);
    this.variationsMap.set(uri.fsPath, variations);
    this._onDidUpdateVariations.fire({ uri, variations });
  }

  getVariations(uri: vscode.Uri): ExpressionVariations[] | undefined {
    return this.variationsMap.get(uri.fsPath);
  }

  removeVariation(uri: vscode.Uri, variationIndex: number): void {
    const variations = this.variationsMap.get(uri.fsPath);
    if (variations && variationIndex >= 0 && variationIndex < variations.length) {
      variations.splice(variationIndex, 1);
      log.info(`StateManager: removed variation ${variationIndex} from ${uri.fsPath}, ${variations.length} remaining`);
      this._onDidUpdateVariations.fire({ uri, variations });
    }
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

  private updateDiagnostic(uri: vscode.Uri, variations: ExpressionVariations[]): void {
    log.info(`updateDiagnostic: creating diagnostics for ${uri.fsPath}`);
    const diagnostics: vscode.Diagnostic[] = [];

    variations.forEach((variation, index) => {
      const diagnostic = new vscode.Diagnostic(
        variation.this.location.range,
        `${variation.others.length} variation${variation.others.length !== 1 ? 's' : ''} found`,
        vscode.DiagnosticSeverity.Information
      );
      diagnostic.code = index;
      diagnostic.source = 'sql-refinery';
      diagnostics.push(diagnostic);
    });
    log.info(`updateDiagnostic: setting ${diagnostics.length} diagnostics for ${uri.fsPath}`);
    this.diagnosticsProvider.updateDiagnostics(uri, diagnostics);
  }

  private updateCodeLens(uri: vscode.Uri, variations: ExpressionVariations[]): void {
    log.info(`updateCodeLens: creating code lenses for ${uri.fsPath}`);
    const codeLenses: vscode.CodeLens[] = [];

    variations.forEach((variation, index) => {
      const showLens = new vscode.CodeLens(variation.this.location.range, {
        title: `→ Show ${variation.others.length} variation${variation.others.length !== 1 ? 's' : ''}`,
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
      vscode.commands.registerCommand('sql-refinery.variations.explorer.apply', this.commandApply.bind(this))
    );
  }

  async commandShow(uri: vscode.Uri, id: number) {
    const explorerUri = vscode.Uri.parse(
      `sql-refinery-explorer:${uriUI} ${basename(uri.fsPath)}?file=${encodeURIComponent(uri.fsPath)}&var=${id}`
    );
    const doc = await vscode.workspace.openTextDocument(explorerUri);
    const editor = await vscode.window.showTextDocument(doc, { viewColumn: vscode.ViewColumn.Beside, preview: false });
    await vscode.languages.setTextDocumentLanguage(doc, 'sql');
    
    // Set cursor to beginning of document
    const startPosition = new vscode.Position(0, 0);
    editor.selection = new vscode.Selection(startPosition, startPosition);
    editor.revealRange(new vscode.Range(startPosition, startPosition));
  }

  async commandPeek(expressions: Expression[], uri: vscode.Uri, position: vscode.Position) {
    const locations = expressions.map(expr =>
      new vscode.Location(vscode.Uri.file(expr.location.file), expr.location.range)
    );
    await vscode.commands.executeCommand('editor.action.peekLocations', uri, position, locations);
  }

  async commandDiff(file: string, indVariation: number, indExpr: number) {
    const originalUri = vscode.Uri.parse(`sql-refinery-explorer-diff:${file}?var=${indVariation}`);
    const selectedUri = vscode.Uri.parse(`sql-refinery-explorer-diff:${file}?var=${indVariation}&expr=${indExpr}`);
    const originalDoc = await vscode.workspace.openTextDocument(originalUri);
    const selectedDoc = await vscode.workspace.openTextDocument(selectedUri);
    await vscode.languages.setTextDocumentLanguage(originalDoc, 'sql');
    await vscode.languages.setTextDocumentLanguage(selectedDoc, 'sql');
    await vscode.commands.executeCommand('vscode.diff', originalUri, selectedUri, `${uriUI} Original ↔ Selected`);
  }

  async commandApply(targetExpr: Expression, newExpr: Expression, thisUri: vscode.Uri) {
    const edit = new vscode.WorkspaceEdit();
    
    // Get the target document to determine indentation
    const targetDoc = await vscode.workspace.openTextDocument(vscode.Uri.file(targetExpr.location.file));
    const targetLine = targetDoc.lineAt(targetExpr.location.range.start.line);
    const indentation = targetLine.text.substring(0, targetExpr.location.range.start.character);
    
    // Apply indentation to lines 2+ of the replacement text
    const lines = newExpr.sql.split('\n');
    const indentedSql = lines.map((line, index) => 
      index === 0 ? line : indentation + line
    ).join('\n');
    
    edit.replace(vscode.Uri.file(targetExpr.location.file), targetExpr.location.range, indentedSql);
    await vscode.workspace.applyEdit(edit);

    // Remove all variations from the state
    const targetUri = vscode.Uri.file(targetExpr.location.file);
    this.stateManager.updateVariations(targetUri, []);

    // Close the virtual document
    await Promise.all(
      vscode.window.visibleTextEditors
        .filter((editor) => editor.document.uri.toString() === thisUri.toString())
        .map((editor) => vscode.commands.executeCommand('workbench.action.closeActiveEditor', editor.document.uri))
    );
  }

  async renderDiffContent(uri: vscode.Uri): Promise<string> {
    const params = new URLSearchParams(uri.query);
    const filePath = uri.fsPath;
    const variationInd = parseInt(params.get('var') || '-1');
    const exprInd = parseInt(params.get('expr') || '-1');
    if (!filePath) return '';

    const variation = this.stateManager.getVariations(vscode.Uri.file(filePath))?.[variationInd];
    if (!variation) return '';

    if (exprInd >= 0) {
      return variation.others[exprInd]?.group.expressions[0]?.sql || '';
    } else {
      return variation.this.sql;
    }
  }

  async renderExplorerContent(uri: vscode.Uri): Promise<string> {
    const params = new URLSearchParams(uri.query);
    const filePath = params.get('file');
    const variationId = parseInt(params.get('var') || '-1');
    if (!filePath) return '';

    const variation = this.stateManager.getVariations(vscode.Uri.file(filePath))?.[variationId];
    if (!variation || !variation.others) return '';

    const lines: string[] = [];
    const codeLenses: vscode.CodeLens[] = [];

    lines.push(`-- ${uriUI}`);
    lines.push('-- Expression variations found in the codebase');
    lines.push('');

    variation.others.forEach((exprVar: ExpressionVariation, varIndex) => {
      const firstExpr = exprVar.group.expressions[0];
      if (!firstExpr) return;

      // Text
      const locationCount = exprVar.group.expressions.length;
      const similarityPercent = Math.round(exprVar.similarity * 100);
      const reliability = exprVar.group.reliability;

      lines.push(
        `-- Variation ${varIndex + 1}:` +
          ` ${similarityPercent}% similarity,` +
          ` reliability ${reliability},` +
          ` ${locationCount} location${locationCount !== 1 ? 's' : ''}`
      );
      const rangeLenses = new vscode.Range(lines.length, 0, lines.length, 0);
      firstExpr.sql.split('\n').forEach((line) => lines.push(line));
      const positionPeek = new vscode.Position(lines.length - 1, 0);
      lines.push('');

      // CodeLens
      codeLenses.push(
        new vscode.CodeLens(rangeLenses, {
          title: `→ Peek ${locationCount} location${locationCount !== 1 ? 's' : ''}`,
          command: 'sql-refinery.variations.explorer.peek',
          arguments: [exprVar.group.expressions, uri, positionPeek],
        }),
        new vscode.CodeLens(rangeLenses, {
          title: `↔ Show diff`,
          command: 'sql-refinery.variations.explorer.diff',
          arguments: [filePath, variationId, varIndex],
        }),
        new vscode.CodeLens(rangeLenses, {
          title: `✓ Apply`,
          command: 'sql-refinery.variations.explorer.apply',
          arguments: [variation.this, firstExpr, uri],
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
