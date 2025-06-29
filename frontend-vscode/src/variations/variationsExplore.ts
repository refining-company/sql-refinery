import * as vscode from 'vscode';
import * as path from 'path';
import { Variation } from './variations';

export interface VirtualDocumentVariant {
  file: string;
  line: number;
  alias: string;
  occurrences: number;
  range: vscode.Range;
  sql: string;
}

export interface VirtualDocumentSection {
  startLine: number;
  endLine: number;
  variant: {
    sql: string;
    locations: VirtualDocumentVariant[];
    variantIndex: number;
  };
}

export interface VirtualDocumentResult {
  content: string;
  metadata: VirtualDocumentSection[];
}

// For selected variation show all other variations

export function variationToVirtualDocumentVariants(variation: Variation): VirtualDocumentVariant[] {
  const variants: VirtualDocumentVariant[] = [];
  
  variants.push({
    file: 'Current file',
    line: variation.this.location.range.start.line + 1,
    alias: variation.this.alias || '',
    occurrences: 1,
    range: variation.this.location.range,
    sql: variation.this.sql
  });
  
  for (const other of variation.others) {
    variants.push({
      file: other.location.file,
      line: other.location.range.start.line + 1,
      alias: other.alias || '',
      occurrences: 1,
      range: other.location.range,
      sql: other.sql
    });
  }
  
  return variants;
}

export function generateVirtualDocumentContent(variants: VirtualDocumentVariant[]): VirtualDocumentResult {
  if (variants.length === 0) {
    return {
      content: '-- No variations found\n-- No SQL variations were found for this group.',
      metadata: []
    };
  }

  const distinctVariations = new Map<string, { sql: string; locations: VirtualDocumentVariant[] }>();
  
  variants.forEach(v => {
    const key = v.sql.trim();
    if (!distinctVariations.has(key)) {
      distinctVariations.set(key, { sql: v.sql, locations: [] });
    }
    distinctVariations.get(key)!.locations.push(v);
  });

  const lines: string[] = [];
  const metadata: VirtualDocumentSection[] = [];
  
  lines.push('-- SQL-Refinery');
  lines.push('-- SQL variations found in the codebase');
  lines.push('');
  
  let currentLine = 3;
  let variationIndex = 1;

  distinctVariations.forEach((data) => {
    lines.push(`-- Variation ${variationIndex}`);
    const startLine = currentLine + 1;
    
    const sqlLines = data.sql.trim().split('\n');
    sqlLines.forEach((line: string) => lines.push(line));
    
    const endLine = startLine + sqlLines.length - 1;
    
    const variationWithLocations = {
      sql: data.sql,
      locations: data.locations,
      variantIndex: variationIndex
    };
    
    metadata.push({ startLine, endLine, variant: variationWithLocations });
    
    lines.push('');
    lines.push('');
    
    currentLine = endLine + 3;
    variationIndex++;
  });

  return {
    content: lines.join('\n'),
    metadata
  };
}

export function generateVirtualDocumentCodeLenses(
  metadata: VirtualDocumentSection[], 
  groupId: string, 
  originalSQL: string
): vscode.CodeLens[] {
  const codeLenses: vscode.CodeLens[] = [];

  metadata.forEach(({ startLine, endLine, variant }) => {
    const range = new vscode.Range(startLine - 1, 0, startLine - 1, 0);
    const locationCount = variant.locations.length;
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

    const diffLens = new vscode.CodeLens(range, {
      title: '↔ Show diff',
      command: 'sql-refinery.showNativeDiff',
      arguments: [{ 
        variant, 
        originalSQL,
        groupId,
        variantIndex: variant.variantIndex
      }],
      tooltip: 'Show differences in native diff editor'
    });
    codeLenses.push(diffLens);
    
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

export class VariationsProvider implements vscode.TextDocumentContentProvider {
  private _onDidChange = new vscode.EventEmitter<vscode.Uri>();
  readonly onDidChange = this._onDidChange.event;

  private variationData = new Map<string, VirtualDocumentVariant[]>();
  private diffContent = new Map<string, string>();
  private variationMetadata = new Map<string, VirtualDocumentSection[]>();
  private originalSQL = new Map<string, string>();

  constructor() {}

  async provideTextDocumentContent(uri: vscode.Uri): Promise<string> {
    if (uri.path.includes('diff-')) {
      const groupId = uri.path.startsWith('/') ? uri.path.substring(1) : uri.path;
      return this.diffContent.get(groupId) || '';
    }
    
    const match = uri.path.match(/variation-(\d+)/);
    const groupId = match ? match[1] : 'current';
    const variants = this.variationData.get(groupId) || [];
    
    const result = generateVirtualDocumentContent(variants);
    this.variationMetadata.set(groupId, result.metadata);

    return result.content;
  }

  public setVariants(groupId: string, variants: VirtualDocumentVariant[]): void {
    this.variationData.set(groupId, variants);
  }
  
  public setDiffContent(groupId: string, sql: string): void {
    this.diffContent.set(groupId, sql);
  }
  
  public setOriginalSQL(groupId: string, sql: string): void {
    this.originalSQL.set(groupId, sql);
  }
  
  public getOriginalSQL(groupId: string): string {
    return this.originalSQL.get(groupId) || '';
  }

  public getVariantMetadata(groupId: string): VirtualDocumentSection[] | undefined {
    return this.variationMetadata.get(groupId);
  }

  public refresh(uri: vscode.Uri): void {
    this._onDidChange.fire(uri);
  }
}

// Code lens provider for virtual documents
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

// ========================================
// EXPLORATION COMMANDS
// ========================================

// Apply variation command - replaces current SQL with selected variation
export async function applyVariationCommand(
  args: { variant: any; groupId: string },
  context: vscode.ExtensionContext
): Promise<void> {
  const data = Array.isArray(args) ? args[0] : args;
  const { variant, groupId } = data;
  const rangeData = context.workspaceState.get<any>(`currentRange-${groupId}`);

  if (!rangeData || !rangeData.documentUri) {
    vscode.window.showErrorMessage('No original document information found');
    return;
  }

  const originalUri = vscode.Uri.parse(rangeData.documentUri);
  const originalDocument = await vscode.workspace.openTextDocument(originalUri);

  await vscode.window.showTextDocument(originalDocument, vscode.ViewColumn.One);

  const currentRange = new vscode.Range(
    rangeData.start.line,
    rangeData.start.character,
    rangeData.end.line,
    rangeData.end.character
  );

  const edit = new vscode.WorkspaceEdit();
  edit.replace(originalUri, currentRange, variant.sql);

  const success = await vscode.workspace.applyEdit(edit);

  if (success) {
    // Close the variations document
    const variationsEditor = vscode.window.visibleTextEditors.find(
      (editor) => editor.document.uri.scheme === 'sql-refinery-variations'
    );
    if (variationsEditor) {
      await vscode.window.showTextDocument(variationsEditor.document, variationsEditor.viewColumn);
      await vscode.commands.executeCommand('workbench.action.closeActiveEditor');
    }
  }
}

// Show native diff command
export async function showNativeDiffCommand(
  args: { variant: any; originalSQL: string; groupId: string; variantIndex: number },
  variationsProvider: VariationsProvider
): Promise<void> {
  const { variant, originalSQL, groupId, variantIndex } = args;

  if (!originalSQL || !variant || !variant.sql) {
    vscode.window.showErrorMessage('Missing SQL content for diff comparison');
    return;
  }

  // Create temporary URIs for diff - using the sql-refinery-variations scheme
  const timestamp = Date.now();
  const originalUri = vscode.Uri.parse(`sql-refinery-variations:diff-original-${timestamp}.sql`);
  const variantUri = vscode.Uri.parse(`sql-refinery-variations:diff-variant-${timestamp}.sql`);

  // Store the content temporarily in the variations provider
  variationsProvider.setDiffContent(`diff-original-${timestamp}.sql`, originalSQL);
  variationsProvider.setDiffContent(`diff-variant-${timestamp}.sql`, variant.sql);

  try {
    // Create descriptive title
    const activeEditor = vscode.window.activeTextEditor;
    let currentFileName = activeEditor ? path.basename(activeEditor.document.fileName) : 'current';

    // If we're already in a virtual document, don't add variation number again
    if (currentFileName.includes(':variation-')) {
      // Already contains variation info, use as-is
    } else {
      // Add variation number to the original file name
      currentFileName = `${currentFileName}:variation-${groupId}`;
    }

    const variationNumber = variantIndex || 1;
    const title = `${currentFileName} ↔ variation-${variationNumber}`;

    // Open native diff editor
    await vscode.commands.executeCommand('vscode.diff', originalUri, variantUri, title);
  } catch (error) {
    console.error('Error opening native diff editor:', error);
    vscode.window.showErrorMessage(`Failed to open diff editor: ${error}`);
  }
}

// Peek locations command
export async function peekLocationsCommand(args: { locations: any[]; position?: vscode.Position }): Promise<void> {
  const { locations, position } = args;
  const activeEditor = vscode.window.activeTextEditor;
  if (!activeEditor) {
    return;
  }

  const vscodeLocations = locations.map((loc: any) => {
    return new vscode.Location(vscode.Uri.file(loc.file), new vscode.Range(loc.line - 1, 0, loc.line - 1, 0));
  });

  const peekPosition = position || activeEditor.selection.active;

  await vscode.commands.executeCommand(
    'editor.action.peekLocations',
    activeEditor.document.uri,
    peekPosition,
    vscodeLocations,
    'peek'
  );
}

// Initialize the exploration journey
export function initExploreJourney(context: vscode.ExtensionContext): VariationsProvider {
  // Register the virtual document provider for variations
  const variationsProvider = new VariationsProvider();
  context.subscriptions.push(
    vscode.workspace.registerTextDocumentContentProvider('sql-refinery-variations', variationsProvider)
  );

  // Register code lens provider for variation actions (Peek, Diff, Apply)
  const variationsCodeLensProvider = new VariationsCodeLensProvider(variationsProvider);
  context.subscriptions.push(
    vscode.languages.registerCodeLensProvider({ scheme: 'sql-refinery-variations' }, variationsCodeLensProvider)
  );

  // Register exploration commands
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-refinery.applyVariation', (args) => 
      applyVariationCommand(args, context)
    ),
    vscode.commands.registerCommand('sql-refinery.showNativeDiff', (args) => 
      showNativeDiffCommand(args, variationsProvider)
    ),
    vscode.commands.registerCommand('sql-refinery.peekLocations', peekLocationsCommand)
  );

  return variationsProvider;
}