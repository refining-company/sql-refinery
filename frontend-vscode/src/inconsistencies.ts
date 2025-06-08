import * as vscode from 'vscode';
import * as path from 'path';
import { VariantsProvider } from './variantsDocumentProvider';
import { VariantsCodeLensProvider } from './variantsCodeLensProvider';
import { InlineVariantsCodeLensProvider } from './inlineVariantsCodeLensProvider';
import { createMockDiagnostics, getVariantsForGroup } from './mockData';

let variantsProvider: VariantsProvider;
let codeLensProvider: VariantsCodeLensProvider;
let inlineCodeLensProvider: InlineVariantsCodeLensProvider;

// Decoration types for diff visualization
let deletionDecorationType: vscode.TextEditorDecorationType;
let additionDecorationType: vscode.TextEditorDecorationType;

export function initInconsistencies(context: vscode.ExtensionContext) {
  setupDecorations(context);
  const diagnosticCollection = setupDiagnostics(context);
  setupProviders(context, diagnosticCollection);
  setupCommands(context);
}

function setupDecorations(context: vscode.ExtensionContext) {
  // Create decoration types for diff visualization
  deletionDecorationType = vscode.window.createTextEditorDecorationType({
    backgroundColor: new vscode.ThemeColor('diffEditor.removedTextBackground'),
    overviewRulerColor: new vscode.ThemeColor('diffEditor.removedTextBackground'),
    overviewRulerLane: vscode.OverviewRulerLane.Left,
    isWholeLine: true
  });
  
  additionDecorationType = vscode.window.createTextEditorDecorationType({
    backgroundColor: new vscode.ThemeColor('diffEditor.insertedTextBackground'),
    overviewRulerColor: new vscode.ThemeColor('diffEditor.insertedTextBackground'),
    overviewRulerLane: vscode.OverviewRulerLane.Right,
    isWholeLine: true
  });
  
  context.subscriptions.push(deletionDecorationType, additionDecorationType);
}

function setupDiagnostics(context: vscode.ExtensionContext): vscode.DiagnosticCollection {
  // Create diagnostics collection
  const diagnosticCollection = vscode.languages.createDiagnosticCollection('sql-insights');
  context.subscriptions.push(diagnosticCollection);

  // Watch for SQL file opens/changes
  const updateDiagnostics = (document: vscode.TextDocument) => {
    if (document.languageId !== 'sql' || document.uri.scheme === 'sql-refinery') {
      return;
    }
    
    const diagnostics = createMockDiagnostics(document);
    diagnosticCollection.set(document.uri, diagnostics);
    
    // Trigger code lens refresh
    if (inlineCodeLensProvider) {
      (inlineCodeLensProvider as any)._onDidChangeCodeLenses.fire();
    }
  };

  // Update diagnostics on file open/change
  context.subscriptions.push(
    vscode.workspace.onDidOpenTextDocument(updateDiagnostics),
    vscode.workspace.onDidChangeTextDocument(e => updateDiagnostics(e.document))
  );

  // Update diagnostics for all open SQL files
  vscode.workspace.textDocuments.forEach(updateDiagnostics);
  
  // Listen for active editor changes to apply decorations
  context.subscriptions.push(
    vscode.window.onDidChangeActiveTextEditor((editor) => {
      if (editor && editor.document.uri.scheme === 'sql-refinery') {
        setTimeout(() => applyDiffDecorations(), 50);
      }
    })
  );

  return diagnosticCollection;
}

function setupProviders(context: vscode.ExtensionContext, diagnosticCollection: vscode.DiagnosticCollection) {
  // Register the virtual document provider
  variantsProvider = new VariantsProvider();
  context.subscriptions.push(
    vscode.workspace.registerTextDocumentContentProvider('sql-refinery', variantsProvider)
  );
  
  // Register code lens providers
  codeLensProvider = new VariantsCodeLensProvider(variantsProvider);
  context.subscriptions.push(
    vscode.languages.registerCodeLensProvider(
      { scheme: 'sql-refinery' },
      codeLensProvider
    )
  );
  
  inlineCodeLensProvider = new InlineVariantsCodeLensProvider(diagnosticCollection);
  context.subscriptions.push(
    vscode.languages.registerCodeLensProvider(
      { scheme: 'file', language: 'sql' },
      inlineCodeLensProvider
    )
  );
}

function setupCommands(context: vscode.ExtensionContext) {
  // Show variants in side document
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-insights.showVariantsEditor', async (args) => {
      const { groupId, currentRange } = args;
      const variants = getVariantsForGroup(groupId);
      
      variantsProvider.setVariants('current', variants);
      
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
      const originalSQL = activeEditor.document.getText(originalRange);
      variantsProvider.setOriginalSQL(originalSQL);
      
      context.workspaceState.update(`currentRange-current`, {
        start: { line: currentRange.start.line, character: currentRange.start.character },
        end: { line: currentRange.end.line, character: currentRange.end.character },
        documentUri: activeEditor.document.uri.toString()
      });
      
      // Open virtual document
      const variantsUri = vscode.Uri.parse(`sql-refinery:sql-refinery:alternatives`);
      const doc = await vscode.workspace.openTextDocument(variantsUri);
      await vscode.window.showTextDocument(doc, {
        viewColumn: vscode.ViewColumn.Beside,
        preview: false
      });
      
      await vscode.languages.setTextDocumentLanguage(doc, 'sql');
      setTimeout(() => applyDiffDecorations(), 100);
    })
  );
  
  // Apply a variant
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-insights.applyVariant', async (args) => {
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
        vscode.window.showInformationMessage(
          `Applied SQL variant from ${path.basename(variant.file)}`
        );
        
        // Close the variants document
        const variantsEditor = vscode.window.visibleTextEditors.find(
          editor => editor.document.uri.scheme === 'sql-refinery'
        );
        if (variantsEditor) {
          await vscode.window.showTextDocument(variantsEditor.document, variantsEditor.viewColumn);
          await vscode.commands.executeCommand('workbench.action.closeActiveEditor');
        }
      }
    })
  );
  
  // Toggle inline diff
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-insights.toggleDiff', async (args) => {
      const { variantIndex } = args;
      
      variantsProvider.toggleDiffMode(variantIndex);
      
      const variantsUri = vscode.Uri.parse(`sql-refinery:sql-refinery:alternatives`);
      variantsProvider.refresh(variantsUri);
      
      setTimeout(() => applyDiffDecorations(), 100);
      
      if (codeLensProvider) {
        (codeLensProvider as any)._onDidChangeCodeLenses.fire();
      }
    })
  );
  
  // Peek at locations
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-insights.peekLocations', async (args) => {
      const { locations, position } = args;
      const activeEditor = vscode.window.activeTextEditor;
      if (!activeEditor) {
        return;
      }
      
      const vscodeLocations = locations.map((loc: any) => {
        return new vscode.Location(
          vscode.Uri.file(loc.file),
          new vscode.Range(loc.line - 1, 0, loc.line - 1, 0)
        );
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
  
  // Ignore variant
  context.subscriptions.push(
    vscode.commands.registerCommand('sql-insights.ignoreVariant', async () => {
      vscode.window.showInformationMessage('Variant ignored (not implemented yet)');
    })
  );
}

// Apply diff decorations to virtual document
function applyDiffDecorations() {
  const activeEditor = vscode.window.activeTextEditor;
  if (!activeEditor || activeEditor.document.uri.scheme !== 'sql-refinery') {
    return;
  }
  
  const diffLines = variantsProvider.getDiffLines('current');
  if (!diffLines || (diffLines.deletions.length === 0 && diffLines.additions.length === 0)) {
    activeEditor.setDecorations(deletionDecorationType, []);
    activeEditor.setDecorations(additionDecorationType, []);
    return;
  }
  
  try {
    const deletionRanges = diffLines.deletions
      .filter(lineNumber => lineNumber < activeEditor.document.lineCount)
      .map(lineNumber => 
        new vscode.Range(lineNumber, 0, lineNumber, activeEditor.document.lineAt(lineNumber).text.length)
      );
    
    const additionRanges = diffLines.additions
      .filter(lineNumber => lineNumber < activeEditor.document.lineCount)
      .map(lineNumber => 
        new vscode.Range(lineNumber, 0, lineNumber, activeEditor.document.lineAt(lineNumber).text.length)
      );
    
    activeEditor.setDecorations(deletionDecorationType, deletionRanges);
    activeEditor.setDecorations(additionDecorationType, additionRanges);
  } catch (error) {
    console.error('Error applying decorations:', error);
    activeEditor.setDecorations(deletionDecorationType, []);
    activeEditor.setDecorations(additionDecorationType, []);
  }
}