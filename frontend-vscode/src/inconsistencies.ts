import * as vscode from 'vscode';
import * as path from 'path';
import { InconsistencyProvider } from './variantsDocumentProvider';
import { AlternativeCodeLensProvider } from './variantsCodeLensProvider';
import { InconsistencyCodeLensProvider } from './inlineVariantsCodeLensProvider';
import { getMockAlternatives, alternativesToDiagnostics, getAlternativeByGroupId, alternativeToMockVariants, UIAlternative } from './mockData';

let inconsistencyProvider: InconsistencyProvider;
let alternativeCodeLensProvider: AlternativeCodeLensProvider;
let inconsistencyCodeLensProvider: InconsistencyCodeLensProvider;
let diagnosticCollection: vscode.DiagnosticCollection;
let currentAlternatives: UIAlternative[] = [];

export function initInconsistencies(context: vscode.ExtensionContext) {
  initDiagnostics(context);
  initCodeLenses(context);
  initAlternativesDocument(context);
}

function initDiagnostics(context: vscode.ExtensionContext) {
  // Create diagnostics collection for inconsistency detection
  diagnosticCollection = vscode.languages.createDiagnosticCollection('sql-refinery-inconsistencies');
  context.subscriptions.push(diagnosticCollection);

  // Initialize mockup system for demonstration
  mockupDiagnosticsSystem(context, diagnosticCollection);
}

function initCodeLenses(context: vscode.ExtensionContext) {
  // Register inline code lens provider (shows "Show alternatives" and "Ignore" on original files)
  inconsistencyCodeLensProvider = new InconsistencyCodeLensProvider(diagnosticCollection);
  
  // Provide access to current alternatives
  inconsistencyCodeLensProvider.setAlternativesProvider(() => currentAlternatives);
  
  context.subscriptions.push(
    vscode.languages.registerCodeLensProvider({ scheme: 'file', language: 'sql' }, inconsistencyCodeLensProvider)
  );
}

function initAlternativesDocument(context: vscode.ExtensionContext) {
  // Register the virtual document provider for alternatives
  inconsistencyProvider = new InconsistencyProvider();
  context.subscriptions.push(
    vscode.workspace.registerTextDocumentContentProvider('sql-refinery-inconsistencies', inconsistencyProvider)
  );

  // Register code lens provider for alternative actions (Peek, Diff, Apply)
  alternativeCodeLensProvider = new AlternativeCodeLensProvider(inconsistencyProvider);
  context.subscriptions.push(
    vscode.languages.registerCodeLensProvider({ scheme: 'sql-refinery-inconsistencies' }, alternativeCodeLensProvider)
  );

  // Register command to show alternatives in virtual document
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-refinery.showVariantsEditor', async (args) => {
      const { groupId, currentRange } = args;
      
      // Find the alternative using the new data structure
      const alternative = getAlternativeByGroupId(groupId, currentAlternatives);
      if (!alternative) {
        vscode.window.showErrorMessage(`No alternative found for group ${groupId}`);
        return;
      }
      
      // Convert to legacy format for the virtual document (temporarily)
      const variants = alternativeToMockVariants(alternative);
      inconsistencyProvider.setVariants(groupId, variants);

      // Store original range and document for apply command
      const activeEditor = vscode.window.activeTextEditor;
      if (!activeEditor) {
        return;
      }

      const originalRange = new vscode.Range(
        currentRange.start.line,
        currentRange.start.character,
        currentRange.end.line,
        currentRange.end.character
      );
      // Get original SQL from the alternative object
      const originalSQL = alternative.this.sql;
      inconsistencyProvider.setOriginalSQL(groupId, originalSQL);

      context.workspaceState.update(`currentRange-${groupId}`, {
        start: { line: currentRange.start.line, character: currentRange.start.character },
        end: { line: currentRange.end.line, character: currentRange.end.character },
        documentUri: activeEditor.document.uri.toString(),
      });

      // Create descriptive file name for virtual document
      const currentFileName = path.basename(activeEditor.document.fileName);
      const inconsistencyNumber = groupId;
      const virtualFileName = `${currentFileName}:inconsistency-${inconsistencyNumber}`;

      // Open group-specific virtual document
      const variantsUri = vscode.Uri.parse(`sql-refinery-inconsistencies:${virtualFileName}`);
      const doc = await vscode.workspace.openTextDocument(variantsUri);
      await vscode.window.showTextDocument(doc, {
        viewColumn: vscode.ViewColumn.Beside,
        preview: false,
      });

      await vscode.languages.setTextDocumentLanguage(doc, 'sql');
    })
  );

  // Register command to apply an alternative
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-refinery.applyVariant', async (args) => {
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
        // Close the variants document
        const variantsEditor = vscode.window.visibleTextEditors.find(
          (editor) => editor.document.uri.scheme === 'sql-refinery-inconsistencies'
        );
        if (variantsEditor) {
          await vscode.window.showTextDocument(variantsEditor.document, variantsEditor.viewColumn);
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

      // Create temporary URIs for diff - using the sql-refinery-inconsistencies scheme
      const timestamp = Date.now();
      const originalUri = vscode.Uri.parse(`sql-refinery-inconsistencies:diff-original-${timestamp}.sql`);
      const variantUri = vscode.Uri.parse(`sql-refinery-inconsistencies:diff-variant-${timestamp}.sql`);

      // Store the content temporarily in the inconsistency provider
      mockupDebugDiffData(timestamp, originalSQL, variant.sql);
      inconsistencyProvider.setVariants(`diff-original-${timestamp}.sql`, [{ sql: originalSQL }]);
      inconsistencyProvider.setVariants(`diff-variant-${timestamp}.sql`, [{ sql: variant.sql }]);

      try {
        // Create descriptive title
        const activeEditor = vscode.window.activeTextEditor;
        let currentFileName = activeEditor ? path.basename(activeEditor.document.fileName) : 'current';

        // If we're already in a virtual document, don't add inconsistency number again
        if (currentFileName.includes(':inconsistency-')) {
          // Already contains inconsistency info, use as-is
        } else {
          // Add inconsistency number to the original file name
          currentFileName = `${currentFileName}:inconsistency-${groupId}`;
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
    if (document.languageId !== 'sql' || document.uri.scheme === 'sql-refinery-inconsistencies') {
      return;
    }

    // Get alternatives using new data structure
    currentAlternatives = getMockAlternatives(document);
    const diagnostics = alternativesToDiagnostics(currentAlternatives);
    diagnosticCollection.set(document.uri, diagnostics);

    // Trigger code lens refresh
    if (inconsistencyCodeLensProvider) {
      (inconsistencyCodeLensProvider as any)._onDidChangeCodeLenses.fire();
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
