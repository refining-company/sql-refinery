import * as vscode from 'vscode';
import * as path from 'path';
import { VariationsProvider } from './variationsDocumentProvider';
import { VariationsCodeLensProvider } from './variationsCodeLensProvider';
import { InlineVariationsCodeLensProvider } from './inlineVariationsCodeLensProvider';
import { getMockVariations, Variation } from './mockData';
import { variationsToDiagnostics, getVariationByGroupId, variationToVirtualDocumentVariants } from './variations';

let variationsProvider: VariationsProvider;
let variationsCodeLensProvider: VariationsCodeLensProvider;
let inlineVariationsCodeLensProvider: InlineVariationsCodeLensProvider;
let diagnosticCollection: vscode.DiagnosticCollection;
let currentVariations: Variation[] = [];

export function initVariations(context: vscode.ExtensionContext) {
  initDiagnostics(context);
  initCodeLenses(context);
  initVariationsDocument(context);
}

function initDiagnostics(context: vscode.ExtensionContext) {
  // Create diagnostics collection for variation detection
  diagnosticCollection = vscode.languages.createDiagnosticCollection('sql-refinery-variations');
  context.subscriptions.push(diagnosticCollection);

  // Initialize mockup system for demonstration
  mockupDiagnosticsSystem(context, diagnosticCollection);
}

function initCodeLenses(context: vscode.ExtensionContext) {
  // Register inline code lens provider (shows "Show variations" and "Ignore" on original files)
  inlineVariationsCodeLensProvider = new InlineVariationsCodeLensProvider(diagnosticCollection);
  
  // Provide access to current variations
  inlineVariationsCodeLensProvider.setVariationsProvider(() => currentVariations);
  
  context.subscriptions.push(
    vscode.languages.registerCodeLensProvider({ scheme: 'file', language: 'sql' }, inlineVariationsCodeLensProvider)
  );
}

function initVariationsDocument(context: vscode.ExtensionContext) {
  // Register the virtual document provider for variations
  variationsProvider = new VariationsProvider();
  context.subscriptions.push(
    vscode.workspace.registerTextDocumentContentProvider('sql-refinery-variations', variationsProvider)
  );

  // Register code lens provider for variation actions (Peek, Diff, Apply)
  variationsCodeLensProvider = new VariationsCodeLensProvider(variationsProvider);
  context.subscriptions.push(
    vscode.languages.registerCodeLensProvider({ scheme: 'sql-refinery-variations' }, variationsCodeLensProvider)
  );

  // Register command to show variations in virtual document
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-refinery.showVariations', async (args) => {
      const { groupId, currentRange } = args;
      
      // Find the variation using the new data structure
      const variation = getVariationByGroupId(groupId, currentVariations);
      if (!variation) {
        vscode.window.showErrorMessage(`No variation found for group ${groupId}`);
        return;
      }
      
      // Convert to virtual document format
      const variants = variationToVirtualDocumentVariants(variation);
      variationsProvider.setVariants(groupId, variants);

      // Store original range and document for apply command
      const activeEditor = vscode.window.activeTextEditor;
      if (!activeEditor) {
        return;
      }

      // Get original SQL from the variation object
      const originalSQL = variation.this.sql;
      variationsProvider.setOriginalSQL(groupId, originalSQL);

      context.workspaceState.update(`currentRange-${groupId}`, {
        start: { line: currentRange.start.line, character: currentRange.start.character },
        end: { line: currentRange.end.line, character: currentRange.end.character },
        documentUri: activeEditor.document.uri.toString(),
      });

      // Create descriptive file name for virtual document
      const currentFileName = path.basename(activeEditor.document.fileName);
      const variationNumber = groupId;
      const virtualFileName = `${currentFileName}:variation-${variationNumber}`;

      // Open group-specific virtual document
      const variationsUri = vscode.Uri.parse(`sql-refinery-variations:${virtualFileName}`);
      const doc = await vscode.workspace.openTextDocument(variationsUri);
      await vscode.window.showTextDocument(doc, {
        viewColumn: vscode.ViewColumn.Beside,
        preview: false,
      });

      await vscode.languages.setTextDocumentLanguage(doc, 'sql');
    })
  );

  // Register command to apply a variation
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-refinery.applyVariation', async (args) => {
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
    })
  );

  // Register command for native diff viewer
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-refinery.showNativeDiff', async (args) => {
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
      mockupDebugDiffData(timestamp, originalSQL, variant.sql);
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

        const alternativeNumber = variantIndex || 1;
        const title = `${currentFileName} ↔ alternative-${alternativeNumber}`;

        // Open native diff editor
        await vscode.commands.executeCommand('vscode.diff', originalUri, variantUri, title);
      } catch (error) {
        console.error('Error opening native diff editor:', error);
        vscode.window.showErrorMessage(`Failed to open diff editor: ${error}`);
      }
    })
  );

  // Register command for peek locations
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-refinery.peekLocations', async (args) => {
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
    })
  );
}

function mockupDiagnosticsSystem(context: vscode.ExtensionContext, diagnosticCollection: vscode.DiagnosticCollection) {
  // Watch for SQL file opens/changes
  const updateDiagnostics = (document: vscode.TextDocument) => {
    if (document.languageId !== 'sql' || document.uri.scheme === 'sql-refinery-variations') {
      return;
    }

    // Get variations using new data structure
    currentVariations = getMockVariations(document);
    const diagnostics = variationsToDiagnostics(currentVariations);
    diagnosticCollection.set(document.uri, diagnostics);

    // Trigger code lens refresh
    if (inlineVariationsCodeLensProvider) {
      (inlineVariationsCodeLensProvider as any)._onDidChangeCodeLenses.fire();
    }
  };

  // Update diagnostics on file open/change
  context.subscriptions.push(
    vscode.workspace.onDidOpenTextDocument(updateDiagnostics),
    vscode.workspace.onDidChangeTextDocument((e) => updateDiagnostics(e.document))
  );

  // Update diagnostics for all open SQL files
  vscode.workspace.textDocuments.forEach(updateDiagnostics);
}

// Mockup functions for development/demonstration purposes
function mockupDebugDiffData(timestamp: number, originalSQL: string, variantSQL: string) {
  console.log('Storing diff data for timestamp:', timestamp);
  console.log('Original SQL:', originalSQL);
  console.log('Variant SQL:', variantSQL);
}