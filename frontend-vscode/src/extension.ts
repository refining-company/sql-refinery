// Entry point for the extension
import * as vscode from 'vscode';
import * as path from 'path';

import { LanguageClient, LanguageClientOptions, ServerOptions } from 'vscode-languageclient/node';
import { createLogger } from './logger';
import { initVariationsState, registerVariationsHandler } from './variations/variations';

let client: LanguageClient;
let log = createLogger(module.filename);

export async function activate(context: vscode.ExtensionContext) {
  log.info('Extension activate() called');
  const clientPromise = startServer(context);
  const stateManager = initVariationsState(context);
  const lspClient = await clientPromise;
  registerVariationsHandler(lspClient, stateManager);

  log.info('Extension activate() completed');
}

// Start the Python LSP server
async function startServer(context: vscode.ExtensionContext): Promise<any> {
  log.info('startServer() called');
  const backendPath = context.asAbsolutePath(path.join('..', 'backend'));
  log.info(`Backend path: ${backendPath}`);

  const serverOptions: ServerOptions = {
    // To enable debug mode: 'uv run python -m src.server --debug'
    // To enable recording: 'uv run python -m src.server --record'
    command: 'uv run python -m src.server',
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
  log.info('LanguageClient created');

  log.info('SQL Refinery client starting');
  await client.start();
  log.info('SQL Refinery client started successfully');

  return client;
}

// This method is called when your extension is deactivated
export async function deactivate() {
  if (client) {
    await client.stop();
  }
}
