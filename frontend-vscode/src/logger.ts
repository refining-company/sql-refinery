import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';

const outputChannel = vscode.window.createOutputChannel('SQL Refinery', { log: true });
outputChannel.clear();

const logFilePath = path.join(__dirname, '..', '..', 'logs', 'frontend-vscode.log');
fs.mkdirSync(path.dirname(logFilePath), { recursive: true });
const logStream = fs.createWriteStream(logFilePath, { flags: 'w' });

export function createLogger(filePath: string) {
  const name = path.parse(filePath).name;

  function format(level: string, message: string): string {
    const timestamp = new Date().toLocaleTimeString('en-US', { hour12: false, timeZone: 'UTC' });
    return `[${timestamp}] [${name}] [${level}] ${message}`;
  }

  return {
    outputChannel,
    info: (message: string) => {
      const formatted = format('INFO', message);
      outputChannel.info(formatted);
      logStream.write(formatted + '\n');
    },
    error: (message: string) => {
      const formatted = format('ERROR', message);
      outputChannel.error(formatted);
      logStream.write(formatted + '\n');
    },
    warn: (message: string) => {
      const formatted = format('WARN', message);
      outputChannel.warn(formatted);
      logStream.write(formatted + '\n');
    },
    debug: (message: string) => {
      const formatted = format('DEBUG', message);
      outputChannel.debug(formatted);
      logStream.write(formatted + '\n');
    },
  };
}
