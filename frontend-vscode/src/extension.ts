// Entry point for the extension
import * as vscode from 'vscode';
import * as path from 'path';

import { LanguageClient, LanguageClientOptions, ServerOptions } from 'vscode-languageclient/node';
import { Logger } from './logger';
import { initVariations } from './variations/variations';

let client: LanguageClient;
let log: Logger = new Logger(module.filename);

export async function activate(context: vscode.ExtensionContext) {
  initVariations(context);
  // startServer(context);
}

// Start the Python LSP server
function startServer(context: vscode.ExtensionContext) {
  const backendPath = context.asAbsolutePath(path.join('..', 'backend'));
  const serverOptions: ServerOptions = {
    command: 'poetry run python -m src.server --start-server --start-debug --start-recording',
    options: { cwd: backendPath, shell: true },
  };

  const clientOptions: LanguageClientOptions = {
    documentSelector: [
      { scheme: 'file', language: 'sql' },
      { scheme: 'untitled', language: 'sql' },
      { scheme: 'vscode-notebook', language: 'sql' },
      { scheme: 'vscode-notebook-cell', language: 'sql' },
    ],
    outputChannel: log.outputChannel,
    traceOutputChannel: log.outputChannel,
  };

  client = new LanguageClient('sql-refinery', 'SQL Refinery', serverOptions, clientOptions);

  setImmediate(async () => {
    log.info('SQL Refinery client starting');
    await client.start();
  });
}

// This method is called when your extension is deactivated
export async function deactivate() {
  if (client) {
    await client.stop();
  }
}
