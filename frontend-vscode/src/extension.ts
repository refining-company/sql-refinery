// The module 'vscode' contains the VS Code extensibility API
import * as vscode from 'vscode';
import * as path from 'path';
import { LanguageClient, LanguageClientOptions, ServerOptions, TransportKind } from 'vscode-languageclient/node';

let client: LanguageClient;

export async function activate(context: vscode.ExtensionContext) {
  // Configuring output channel for debugging
  const outputChannel = vscode.window.createOutputChannel('SQL Refinery', {
    log: true,
  });
  outputChannel.clear();

  // Spawning sub-process with debugger and server
  const backendPath = context.asAbsolutePath(path.join('..', 'backend'));
  const serverOptions: ServerOptions = {
    command:
      // 'source .venv/bin/activate && python -Xfrozen_modules=off -m debugpy --listen 5678 -m src.server',
      'source .venv/bin/activate && python -Xfrozen_modules=off -m src.server',
    args: ['--codebase-path', 'tests/inputs/codebase/', '--start-server', '--start-debug'],
    options: {
      cwd: backendPath,
      shell: true,
    },
  };

  const clientOptions: LanguageClientOptions = {
    documentSelector: [
      { scheme: 'file', language: 'sql' },
      { scheme: 'untitled', language: 'sql' },
      { scheme: 'vscode-notebook', language: 'sql' },
      { scheme: 'vscode-notebook-cell', language: 'sql' },
    ],
    outputChannel: outputChannel,
    traceOutputChannel: outputChannel,
  };

  client = new LanguageClient('sqlRefinery', 'SQL Refinery', serverOptions, clientOptions);

  setImmediate(async () => {
    outputChannel.info('Starting client');
    await client.start();
    outputChannel.info('Server started');
  });
  wrapPeekLocation(context);
}

function wrapPeekLocation(context: vscode.ExtensionContext) {
  // Define your types and helper functions for the custom command
  type RawPosition = { line: number; character: number };
  type RawLocation = { uri: string; position: RawPosition };

  const mkPosition = (raw: RawPosition) => new vscode.Position(raw.line, raw.character);
  const mkLocation = (raw: RawLocation) => new vscode.Location(vscode.Uri.parse(raw.uri), mkPosition(raw.position));

  const disposable = vscode.commands.registerCommand(
    'sqlRefinery.peekLocations',
    async (rawUri, rawPosition, rawLocations, action) => {
      const uri = vscode.Uri.parse(rawUri);
      const position = mkPosition(rawPosition);
      const locations = rawLocations.map(mkLocation);
      await vscode.commands.executeCommand('editor.action.peekLocations', uri, position, locations, action);
    }
  );
  context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
export async function deactivate() {
  if (client) {
    await client.stop();
  }
}
