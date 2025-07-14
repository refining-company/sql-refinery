// Custom logger
// consider moving to winston-transport-vscode
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

  function format(message: string): string {
    const timestamp = new Date().toLocaleTimeString('en-US', { hour12: false, timeZone: 'UTC' });
    return `[${timestamp}] [${name}] ${message}`;
  }

  return {
    outputChannel,
    info: (message: string) => {
      const formatted = format(message);
      outputChannel.info(formatted);
      logStream.write('[info] ' + formatted + '\n');
    },
    error: (message: string) => {
      const formatted = format(message);
      outputChannel.error(formatted);
      logStream.write('[error] ' + formatted + '\n');
    },
    warn: (message: string) => {
      const formatted = format(message);
      outputChannel.warn(formatted);
      logStream.write('[warn] ' + formatted + '\n');
    },
    debug: (message: string) => {
      const formatted = format(message);
      outputChannel.debug(formatted);
      logStream.write('[debug] ' + formatted + '\n');
    },
  };
}
