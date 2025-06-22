import * as vscode from 'vscode';
import * as path from 'path';

export class InconsistencyProvider implements vscode.TextDocumentContentProvider {
  // Fired when you want VS Code to refresh the content
  private _onDidChange = new vscode.EventEmitter<vscode.Uri>();
  readonly onDidChange = this._onDidChange.event;

  // Store variant data by groupId
  private variantData = new Map<string, any[]>();
  
  // Store metadata for code lens positioning
  private variantMetadata = new Map<string, { startLine: number; endLine: number; variant: any }[]>();
  
  // Store original SQL for diff comparison per group
  private originalSQL = new Map<string, string>();

  constructor() {}

  // VS Code calls this whenever it needs the document's text
  async provideTextDocumentContent(uri: vscode.Uri): Promise<string> {
    mockupDebugDocumentRequest(uri, this.variantData);
    
    // Handle diff documents - return plain SQL
    if (uri.path.includes('diff-')) {
      // Extract the full groupId including the .sql extension
      const groupId = uri.path.startsWith('/') ? uri.path.substring(1) : uri.path;
      const variants = this.variantData.get(groupId) || [];
      return variants.length > 0 ? variants[0].sql : '';
    }
    
    // Extract groupId from document name: editor.sql:inconsistency-N
    const match = uri.path.match(/inconsistency-(\d+)/);
    const groupId = match ? match[1] : 'current';
    const variants = this.variantData.get(groupId) || [];
    
    if (variants.length === 0) {
      return '-- No alternatives found\n-- No SQL alternatives were found for this group.';
    }

    // Group alternatives by their SQL content to find distinct alternatives
    const distinctVariants = new Map<string, { sql: string; locations: any[] }>();
    
    variants.forEach(v => {
      const key = v.sql.trim();
      if (!distinctVariants.has(key)) {
        distinctVariants.set(key, { sql: v.sql, locations: [] });
      }
      distinctVariants.get(key)!.locations.push({
        file: v.file,
        line: v.line,
        alias: v.alias,
        sql: v.sql,
        occurrences: v.occurrences,
        range: v.range
      });
    });

    // Build a SQL document with distinct alternatives
    const lines: string[] = [];
    const metadata: { startLine: number; endLine: number; variant: any }[] = [];
    
    // Add header comment
    lines.push('-- SQL-Refinery');
    lines.push('-- Inconsistent query: alternative variants found in the codebase');
    lines.push('');
    
    let currentLine = 3;
    let variantIndex = 1;

    distinctVariants.forEach((data) => {
      // Add alternative header
      lines.push(`-- Alternative ${variantIndex}`);
      const startLine = currentLine + 1;
      
      // Add the SQL content
      const sqlLines = data.sql.trim().split('\n');
      sqlLines.forEach((line: string) => lines.push(line));
      
      const endLine = startLine + sqlLines.length - 1;
      
      // Create an alternative object with all locations
      const variantWithLocations = {
        sql: data.sql,
        locations: data.locations,
        variantIndex: variantIndex
      };
      
      // Store metadata for code lens
      metadata.push({ startLine, endLine, variant: variantWithLocations });
      
      // Add blank lines between alternatives
      lines.push('');
      lines.push('');
      
      currentLine = endLine + 3;
      variantIndex++;
    });

    // Store metadata for code lens provider
    this.variantMetadata.set(groupId, metadata);

    return lines.join('\n');
  }

  // Store variant data for a group
  public setVariants(groupId: string, variants: any[]): void {
    this.variantData.set(groupId, variants);
  }
  
  
  
  // Set original SQL for diff comparison
  public setOriginalSQL(groupId: string, sql: string): void {
    this.originalSQL.set(groupId, sql);
  }
  
  // Get original SQL for diff comparison
  public getOriginalSQL(groupId: string): string {
    return this.originalSQL.get(groupId) || '';
  }
  

  // Get metadata for code lens provider
  public getVariantMetadata(groupId: string): { startLine: number; endLine: number; variant: any }[] | undefined {
    return this.variantMetadata.get(groupId);
  }

  // Call this if you ever need to refresh the view
  public refresh(uri: vscode.Uri): void {
    this._onDidChange.fire(uri);
  }
}

// Mockup functions for development/demonstration purposes
function mockupDebugDocumentRequest(uri: vscode.Uri, variantData: Map<string, any[]>) {
  console.log('VariantsProvider called with URI:', uri.toString());
  console.log('URI path:', uri.path);
  console.log('Available data keys:', Array.from(variantData.keys()));
}