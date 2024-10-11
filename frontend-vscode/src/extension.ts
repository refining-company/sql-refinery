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
  let pythonExecutable: string;
  let venvPath: string;
  if (process.platform === 'win32') {
    pythonExecutable = context.asAbsolutePath(
      path.join('..', 'backend', '.venv', 'Scripts', 'python.exe')
    );
    venvPath = context.asAbsolutePath(
      path.join('..', 'backend', '.venv', 'Scripts')
    );
  } else {
    pythonExecutable = context.asAbsolutePath(
      path.join('..', 'backend', '.venv', 'bin', 'python')
    );
    venvPath = context.asAbsolutePath(
      path.join('..', 'backend', '.venv', 'bin')
    );
  }

  const serverScript = context.asAbsolutePath(
    path.join('..', 'backend', 'src', 'server.py')
  );

  const cwd = context.asAbsolutePath(path.join('..', 'backend'));
  const env = { ...process.env };
  env.VIRTUAL_ENV = context.asAbsolutePath(path.join('..', 'backend', '.venv'));
  env.PATH = `${venvPath}${path.delimiter}${env.PATH}`;

  if (env.PYTHONPATH) {
    env.PYTHONPATH = `${cwd}${path.delimiter}${env.PYTHONPATH}`;
  } else {
    env.PYTHONPATH = cwd;
  }

  const serverOptions: ServerOptions = {
    command: pythonExecutable,
    args: [
      '-u',
      // '-Xfrozen_modules=off',
      // '-m',
      // 'debugpy',
      // '--listen',
      // '5678',
      // '--wait-for-client',
      serverScript,
      '../tests/inputs/codebase/',
      '../tests/inputs/editor.sql',
    ],
    options: {
      env: env,
      cwd: cwd,
    },
    transport: TransportKind.stdio,
  };
  const outputChannel = vscode.window.createOutputChannel('SQL Refinery', {
    log: true,
  });
  const clientOptions: LanguageClientOptions = {
    documentSelector: [{ scheme: 'file', language: 'sql' }],
    synchronize: { configurationSection: 'sql' },
    outputChannel: outputChannel,
    traceOutputChannel: outputChannel,
  };
  const client = new LanguageClient(
    'sqlRefinery',
    'SQL Refinery',
    serverOptions,
    clientOptions
  );
  outputChannel.info('Client started');

  await client.start();
  outputChannel.info('Server started');
  context.subscriptions.push({ dispose: () => client.stop() });
}

// This method is called when your extension is deactivated
export function deactivate() {}
