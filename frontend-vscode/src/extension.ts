// Entry point for the extension
import * as vscode from 'vscode';
import * as path from 'path';

import { LanguageClient, LanguageClientOptions, ServerOptions } from 'vscode-languageclient/node';
import { createLogger } from './logger';
import { initVariations } from './variations/variations';

let client: LanguageClient;
let log = createLogger(module.filename);

export async function activate(context: vscode.ExtensionContext) {
  log.info('Extension activate() called');
  startServer(context);
  initVariations(context);

  log.info('Extension activate() completed');
}

// Start the Python LSP server
async function startServer(context: vscode.ExtensionContext) {
  log.info('startServer() called');
  const backendPath = context.asAbsolutePath(path.join('..', 'backend'));
  log.info(`Backend path: ${backendPath}`);

  const serverOptions: ServerOptions = {
    // FIXME: debug blocks running in test mode
    // command: 'poetry run python -m src.server --start-server --start-debug --start-recording',
    command: 'poetry run python -m src.server --start-server',
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

  setImmediate(async () => {
    log.info('SQL Refinery client starting');
    await client.start();
    log.info('Extension calling initVariations()');

    log.info('SQL Refinery client started successfully');

    // Handle custom variations notification from backend - register after client starts
    client.onNotification('sql-refinery/variations', (params: { uri: string; variations: any[] }) => {
      log.info(`Received ${params.variations.length} variations for ${params.uri}`);
      log.info(`Variations data: ${JSON.stringify(params.variations, null, 2)}`);
    });
    log.info('Registered sql-refinery/variations notification handler');
  });
}

// This method is called when your extension is deactivated
export async function deactivate() {
  if (client) {
    await client.stop();
  }
}
