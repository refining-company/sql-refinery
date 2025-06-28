import * as assert from 'assert';
import * as vscode from 'vscode';
import * as path from 'path';
import { VSCodeRecorder, sleep, waitForDiagnostics } from './utils/recorder';

suite('Alternatives Workflow Test', () => {
  let recorder: VSCodeRecorder;

  setup(() => {
    const snapshotsPath = path.join(__dirname, '../../src/test/snapshots');
    recorder = new VSCodeRecorder('alternatives', snapshotsPath);
  });

  test('User workflow with alternatives', async function () {
    this.timeout(60000); // Increase timeout for full workflow

    try {
      // Step 1: Open file and wait for diagnostics
      const editorPath = path.join(vscode.workspace.workspaceFolders![0].uri.fsPath, 'editor.sql');
      const doc = await vscode.workspace.openTextDocument(editorPath);
      await vscode.window.showTextDocument(doc);

      // Wait for extension to process and show diagnostics
      await waitForDiagnostics(doc.uri, 10000);
      await sleep(1000); // Extra wait for code lenses

      await recorder.capture('1. File opened with diagnostics and code lenses');

      // Step 2: Show alternatives for first inconsistency (CASE)
      const codeLenses = (await vscode.commands.executeCommand(
        'vscode.executeCodeLensProvider',
        doc.uri
      )) as vscode.CodeLens[];

      console.log(`Found ${codeLenses?.length || 0} code lenses`);

      const showAltLens =
        codeLenses &&
        codeLenses.find((lens) => lens.command?.title.includes('Show') && lens.command?.title.includes('variations'));

      if (showAltLens?.command) {
        console.log(`Executing command: ${showAltLens.command.command}`);
        await vscode.commands.executeCommand(showAltLens.command.command, ...(showAltLens.command.arguments || []));
        await sleep(1000); // Wait for virtual document to open
      }

      await recorder.capture('2. Showed alternatives for first inconsistency (CASE statement)');

      // Step 3: Execute peek command and capture the result
      const activeEditor = vscode.window.activeTextEditor;
      if (activeEditor?.document.uri.scheme === 'sql-refinery-variations') {
        const virtualCodeLenses = (await vscode.commands.executeCommand(
          'vscode.executeCodeLensProvider',
          activeEditor.document.uri
        )) as vscode.CodeLens[];

        // Execute peek
        const peekLens =
          virtualCodeLenses &&
          virtualCodeLenses.find(
            (lens) => lens.command?.title.includes('Peek') || lens.command?.command.includes('peek')
          );
        if (peekLens?.command) {
          console.log(`Executing peek command: ${peekLens.command.command}`);
          await vscode.commands.executeCommand(peekLens.command.command, ...(peekLens.command.arguments || []));
          await sleep(1000); // Give more time for peek view to open
        }
      }

      await recorder.capture('3. Peek locations opened for first alternative');

      // Step 4: Apply the first alternative
      const virtualEditor = vscode.window.visibleTextEditors.find(
        (e) => e.document.uri.scheme === 'sql-refinery-variations' && !e.document.uri.path.includes('diff-')
      );

      if (virtualEditor) {
        await vscode.window.showTextDocument(virtualEditor.document);
        await sleep(500);

        const virtualCodeLenses = (await vscode.commands.executeCommand(
          'vscode.executeCodeLensProvider',
          virtualEditor.document.uri
        )) as vscode.CodeLens[];

        const applyLens =
          virtualCodeLenses &&
          virtualCodeLenses.find(
            (lens) => lens.command?.title.includes('Apply') || lens.command?.command.includes('apply')
          );

        if (applyLens?.command) {
          console.log(`Executing apply command: ${applyLens.command.command}`);
          await vscode.commands.executeCommand(applyLens.command.command, ...(applyLens.command.arguments || []));
          await sleep(1000);
        }
      }

      await recorder.capture('4. Applied first alternative (CASE statement replaced)');

      // Step 5: Show alternatives for second inconsistency (IIF)
      const originalEditor = vscode.window.visibleTextEditors.find(
        (e) => e.document.uri.scheme === 'file' && e.document.fileName.includes('editor.sql')
      );

      if (originalEditor) {
        await vscode.window.showTextDocument(originalEditor.document);
        await sleep(500);

        const newCodeLenses = (await vscode.commands.executeCommand(
          'vscode.executeCodeLensProvider',
          originalEditor.document.uri
        )) as vscode.CodeLens[];

        // Find remaining "Show variations" lens (should be for IIF now)
        const showAltLenses =
          newCodeLenses &&
          newCodeLenses.filter(
            (lens) => lens.command?.title.includes('Show') && lens.command?.title.includes('variations')
          );

        if (showAltLenses && showAltLenses.length > 0) {
          // After applying first alternative, the second one might be at a different index
          const iifLens =
            showAltLenses.find(
              (lens) => lens.range.start.line > 10 // IIF is after line 10
            ) || showAltLenses[0];

          console.log(`Executing show command for IIF: ${iifLens.command!.command}`);
          await vscode.commands.executeCommand(iifLens.command!.command, ...(iifLens.command!.arguments || []));
          await sleep(1000);
        }
      }

      await recorder.capture('5. Showed alternatives for second inconsistency (IIF statement)');

      // Execute some commands on the second inconsistency to demonstrate functionality
      const newVirtualEditor = vscode.window.activeTextEditor;
      if (newVirtualEditor?.document.uri.scheme === 'sql-refinery-variations') {
        const virtualCodeLenses = (await vscode.commands.executeCommand(
          'vscode.executeCodeLensProvider',
          newVirtualEditor.document.uri
        )) as vscode.CodeLens[];

        // Click peek to demonstrate
        const peekLens =
          virtualCodeLenses &&
          virtualCodeLenses.find(
            (lens) => lens.command?.title.includes('Peek') || lens.command?.command.includes('peek')
          );

        if (peekLens?.command) {
          await vscode.commands.executeCommand(peekLens.command.command, ...(peekLens.command.arguments || []));
          await sleep(500);
        }
      }

      // Wait and capture final state
      await sleep(1000);
      await recorder.capture('6. Final state - workflow completed');

      // Assert that the snapshot matches the golden snapshot
      await recorder.assertMatches();

      // Basic assertion to ensure test passed
      assert.ok(true, 'Workflow completed successfully');
    } catch (error) {
      console.error('Test failed:', error);

      // Save snapshot even on failure for debugging
      const errorMessage = error instanceof Error ? error.message : String(error);
      await recorder.capture(`ERROR: ${errorMessage}`);

      throw error;
    }
  });
});
