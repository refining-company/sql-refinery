import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs-extra';
import * as diff from 'diff';
import { AssertionError } from 'assert';

export class VSCodeRecorder {
  private captures: string[] = [];
  private name: string;
  private path: string;

  constructor(name: string, workdir: string) {
    this.name = name;
    this.path = workdir;
  }

  getRecording(): string {
    return `# Test: ${this.name}\n\n` + this.captures.join('\n');
  }

  async assertMatches(): Promise<void> {
    const lastSnapshot = this.getRecording();
    const lastPath = path.join(this.path, `${this.name}.last.md`);
    const truePath = path.join(this.path, `${this.name}.true.md`);

    await fs.outputFile(lastPath, lastSnapshot);

    if (process.env.UPDATE_SNAPSHOTS === '1') {
      await fs.outputFile(truePath, lastSnapshot);
      console.log('Golden snapshot updated');
    }

    const trueSnapshot = await fs.readFile(truePath, 'utf8').catch(() => '');
    if (lastSnapshot !== trueSnapshot) {
      const patch = diff.createPatch(`${this.name}.true.md`, trueSnapshot, lastSnapshot);
      throw new AssertionError({
        message: `Snapshot mismatch:\n${patch}`,
        actual: lastSnapshot,
        expected: trueSnapshot,
      });
    }

    console.log('Snapshot matches');
  }

  async capture(name: string): Promise<void> {
    let output = '';
    output += `## Step: ${name}\n`;
    output += this.captureOpenEditors();
    output += await this.captureActiveEditor();
    output += '\n';
    this.captures.push(output);
  }

  private captureOpenEditors(): string {
    const activeEditor = vscode.window.activeTextEditor;
    const openEditors = vscode.window.visibleTextEditors;

    let output = `### Open Editors (${openEditors.length}):\n`;
    openEditors?.forEach((editor, i) => {
      const fileName = this.formatFilename(editor.document.uri);
      const isActive = editor === activeEditor ? ' (active)' : '';
      output += `${i}. ${fileName} (column ${editor.viewColumn})${isActive}\n`;
    });
    return output + '\n';
  }

  private async captureActiveEditor(): Promise<string> {
    const activeEditor = vscode.window.activeTextEditor;
    if (!activeEditor) {
      return '### Active Editor: (none)\n\n';
    }

    const fileName = this.formatFilename(activeEditor.document.uri);
    let output = `### Active Editor: ${fileName}\n`;

    output += this.formatCode(activeEditor.document.getText());
    output += '\n';

    if (!activeEditor.selection.isEmpty) {
      output += `#### Selection: ${this.formatRange(activeEditor.selection)}\n`;
      output += this.formatCode(activeEditor.document.getText(activeEditor.selection));
      output += '\n';
    }

    output += this.captureDiagnostics(activeEditor);
    output += await this.captureCodeLenses(activeEditor);
    return output + '\n';
  }

  private captureDiagnostics(editor: vscode.TextEditor): string {
    const diagnostics = vscode.languages.getDiagnostics(editor.document.uri) || [];

    let output = `#### Diagnostics (${diagnostics?.length}):\n`;
    diagnostics.forEach((d, index) => {
      output += `\n##### ${index}. ${d.message}\n`;
      output += `- **Source**: ${d.source ?? '(none)'}\n`;
      output += `- **Severity**: ${vscode.DiagnosticSeverity[d.severity]}\n`;
      output += `- **Code**: ${d.code ?? '(none)'}\n`;
      output += `- **Range**: ${this.formatRange(d.range)}\n`;
      output += `- **Snippet**: ${this.formatCodePeek(editor.document.getText(d.range))}\n`;

      if (d.relatedInformation?.length) {
        output += `- **Related Information** (${d.relatedInformation.length}):\n`;
        d.relatedInformation.forEach((ri) => {
          const fileName = this.formatFilename(ri.location.uri);
          const preview = editor.document.getText(ri.location.range);
          output += `  - ${fileName}:${this.formatRange(ri.location.range)} - ${ri.message}\n`;
          output += `    ${this.formatCodePeek(preview)}\n`;
        });
      }
      output += '\n';
    });
    return output + '\n';
  }

  private async captureCodeLenses(editor: vscode.TextEditor): Promise<string> {
    const codeLenses =
      ((await vscode.commands.executeCommand(
        'vscode.executeCodeLensProvider',
        editor.document.uri
      )) as vscode.CodeLens[]) || [];

    let output = `#### Code Lenses (${codeLenses?.length}):\n`;
    codeLenses.forEach((cl, index) => {
      if (cl.command) {
        output += `\n${index}. **${cl.command.title}**\n`;
        output += `   - **Range**: ${this.formatRange(cl.range)}\n`;
        output += `   - **Snippet**: ${this.formatCodePeek(editor.document.getText(cl.range))}\n`;
        output += `   - **Command**: \`${cl.command.command}\`\n`;
        output += `   - **Arguments**: ${JSON.stringify(cl.command.arguments)}\n`;
      }
    });
    return output + '\n';
  }

  private formatFilename(uri: vscode.Uri): string {
    return uri.scheme === 'file' ? path.basename(uri.fsPath) : uri.toString();
  }

  private formatRange(range: vscode.Range | vscode.Selection): string {
    return `${range.start.line}:${range.start.character}-${range.end.line}:${range.end.character}`;
  }

  private formatCode(text: string, indent: string = ''): string {
    const lines = text.split('\n');
    const indentedLines = lines.map((line) => indent + line).join('\n');
    return `${indent}\`\`\`sql\n${indentedLines}\n${indent}\`\`\`\n`;
  }

  private formatCodePeek(text: string): string {
    return `\`${text.replace(/\n/g, '\\n')}\``;
  }
}

// Helper function for tests
export function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export async function waitForDiagnostics(uri: vscode.Uri, timeout = 5000): Promise<void> {
  const start = Date.now();
  while (Date.now() - start < timeout) {
    const diagnostics = vscode.languages.getDiagnostics(uri);
    if (diagnostics.length > 0) {
      return;
    }
    await sleep(100);
  }
  throw new Error(`Timeout waiting for diagnostics on ${uri.toString()}`);
}
