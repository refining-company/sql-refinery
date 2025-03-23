// Custom logger
import * as vscode from 'vscode';

export class Logger {
  public static outputChannel: vscode.LogOutputChannel;
  public name: string;

  static init(channelName: string): void {
    if (!Logger.outputChannel) {
      Logger.outputChannel = vscode.window.createOutputChannel(channelName, { log: true });
      Logger.outputChannel.clear();
    } else {
      console.warn('Logger is not initialized. Call Logger.init() first.');
    }
  }

  public constructor(loggerName: string) {
    this.name = loggerName;
    if (!Logger.outputChannel) {
      throw new Error('Logger is not initialized. Call Logger.init() first.');
    }
  }

  info(message: string): void {
    Logger.outputChannel.info(this.format(message));
  }

  error(message: string): void {
    Logger.outputChannel.error(this.format(message));
  }

  warn(message: string): void {
    Logger.outputChannel.warn(this.format(message));
  }

  debug(message: string): void {
    Logger.outputChannel.debug(this.format(message));
  }

  private format(message: string): string {
    return `[frontend:${this.name}] ${message}\n`;
  }
}
