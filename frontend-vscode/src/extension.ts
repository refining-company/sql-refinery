// Entry point for the extension
import * as vscode from 'vscode';
import * as path from 'path';
import { LanguageClient, LanguageClientOptions, ServerOptions, TransportKind } from 'vscode-languageclient/node';
import { Logger } from './logger';

let client: LanguageClient;
let log: Logger;

export async function activate(context: vscode.ExtensionContext) {
  Logger.init('SQL Refinery');
  log = new Logger(path.parse(__filename).name);

  // Spawning sub-process with LSP agent connecting to recording server
  const backendPath = context.asAbsolutePath(path.join('..', 'backend'));
  const serverOptions: ServerOptions = {
    command: 'poetry run python -m src.server --start-server --start-debug',
    options: { cwd: backendPath, shell: true },
  };

  const clientOptions: LanguageClientOptions = {
    documentSelector: [
      { scheme: 'file', language: 'sql' },
      { scheme: 'untitled', language: 'sql' },
      { scheme: 'vscode-notebook', language: 'sql' },
      { scheme: 'vscode-notebook-cell', language: 'sql' },
    ],
    outputChannel: Logger.outputChannel,
    traceOutputChannel: Logger.outputChannel,
  };

  client = new LanguageClient('sqlRefinery', 'SQL Refinery', serverOptions, clientOptions);

  setImmediate(async () => {
    log.info('LanguageClient starting');
    await client.start();
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
