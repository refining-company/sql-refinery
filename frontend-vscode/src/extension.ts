// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import * as path from 'path';
import {
  LanguageClient,
  LanguageClientOptions,
  ServerOptions,
  TransportKind,
} from 'vscode-languageclient/node';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export async function activate(context: vscode.ExtensionContext) {
  // Configuring output channel for debugging
  const outputChannel = vscode.window.createOutputChannel('SQL Refinery', {
    log: true,
  });
  outputChannel.clear();

  // Spawning sub-process with debugger and server
  outputChannel.info('Starting client');
  const backendPath = context.asAbsolutePath(path.join('..', 'backend'));
  const serverOptions: ServerOptions = {
    command:
      'source .venv/bin/activate && python -Xfrozen_modules=off -m debugpy --connect 5678 -m src.server',
    args: ['../tests/inputs/codebase/', '../tests/inputs/editor.sql'],
    options: {
      cwd: backendPath,
      shell: true,
    },
    transport: TransportKind.stdio,
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
  const client = new LanguageClient(
    'sqlRefinery',
    'SQL Refinery',
    serverOptions,
    clientOptions
  );

  await client.start();
  context.subscriptions.push({ dispose: () => client.stop() });
}

// This method is called when your extension is deactivated
export function deactivate() {}
