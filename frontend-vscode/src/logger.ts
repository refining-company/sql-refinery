// Custom logger
import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';
import { Console } from 'console';

export class Logger {
  public name: string;
  public outputChannel: vscode.LogOutputChannel;
  private outputFile: Console;
  private static logFilePath = path.join(__dirname, '..', '..', 'logs', 'frontend-vscode.log');

  constructor(filePath: string) {
    this.name = path.parse(filePath).name;

    // VSCode output pannel
    this.outputChannel = vscode.window.createOutputChannel('SQL Refinery', { log: true });
    this.outputChannel.clear();

    // File logging
    fs.mkdirSync(path.dirname(Logger.logFilePath), { recursive: true });
    const logStream = fs.createWriteStream(Logger.logFilePath);
    this.outputFile = new Console(logStream, logStream);
  }

  info(message: string): void {
    const formatted = this.format(message);
    this.outputChannel.info(formatted);
    this.outputFile.log(formatted);
  }

  error(message: string): void {
    const formatted = this.format(message);
    this.outputChannel.error(formatted);
    this.outputFile.error(formatted);
  }

  warn(message: string): void {
    const formatted = this.format(message);
    this.outputChannel.warn(formatted);
    this.outputFile.warn(formatted);
  }

  debug(message: string): void {
    const formatted = this.format(message);
    this.outputChannel.debug(formatted);
    this.outputFile.log(formatted);
  }

  private format(message: string): string {
    return `[${this.name}] ${message}`;
  }
}
