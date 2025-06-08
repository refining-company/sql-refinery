import * as vscode from 'vscode';
import * as path from 'path';
import { getMockDiffLines, MockDiffLine } from './mockData';

export class VariantsProvider implements vscode.TextDocumentContentProvider {
  // Fired when you want VS Code to refresh the content
  private _onDidChange = new vscode.EventEmitter<vscode.Uri>();
  readonly onDidChange = this._onDidChange.event;

  // Store variant data by groupId
  private variantData = new Map<string, any[]>();
  
  // Store metadata for code lens positioning
  private variantMetadata = new Map<string, { startLine: number; endLine: number; variant: any }[]>();
  
  // Track which variants are showing diff
  private diffModeVariants = new Set<number>();
  
  // Store original SQL for diff comparison per group
  private originalSQL = new Map<string, string>();
  
  // Store diff line information for decorations (from backend)
  private diffLines = new Map<string, { deletions: number[]; additions: number[] }>();

  constructor() {}

  // VS Code calls this whenever it needs the document's text
  async provideTextDocumentContent(uri: vscode.Uri): Promise<string> {
    console.log('VariantsProvider called with URI:', uri.toString());
    console.log('URI scheme:', uri.scheme);
    console.log('URI authority:', uri.authority);
    console.log('URI path:', uri.path);
    console.log('Available data keys:', Array.from(this.variantData.keys()));
    
    // Extract groupId from document name: editor.sql:inconsistency-N
    const match = uri.path.match(/inconsistency-(\d+)/);
    const groupId = match ? match[1] : 'current';
    const variants = this.variantData.get(groupId) || [];
    console.log('Found variants for group', groupId, ':', variants.length);
    
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

    distinctVariants.forEach((data, sqlKey) => {
      // Add alternative header
      lines.push(`-- Alternative ${variantIndex}`);
      const startLine = currentLine + 1;
      
      // Add the SQL content with optional diff
      const sqlLines = data.sql.trim().split('\n');
      
      const deletionLines: number[] = [];
      const additionLines: number[] = [];
      
      if (this.diffModeVariants.has(variantIndex)) {
        // Show diff mode - use backend-provided diff data
        const originalSQLForGroup = this.originalSQL.get(groupId);
        if (originalSQLForGroup) {
          const backendDiffLines = getMockDiffLines(originalSQLForGroup, data.sql);
          
          // Add lines in diff order from backend
          backendDiffLines.forEach((diffLine) => {
            const lineNumber = lines.length;
            
            if (diffLine.type === 'common') {
              lines.push(`  ${diffLine.content}`);
            } else if (diffLine.type === 'deletion') {
              lines.push(`- ${diffLine.content}`);
              deletionLines.push(lineNumber);
            } else if (diffLine.type === 'addition') {
              lines.push(`+ ${diffLine.content}`);
              additionLines.push(lineNumber);
            }
          });
        } else {
          // No original SQL, just show alternative as additions
          sqlLines.forEach((line: string) => {
            const lineNumber = lines.length;
            lines.push(`+ ${line}`);
            additionLines.push(lineNumber);
          });
        }
        
        // Store diff line info for decorations
        this.diffLines.set(groupId, { deletions: deletionLines, additions: additionLines });
      } else {
        // Normal mode - just show the alternative SQL
        sqlLines.forEach((line: string) => lines.push(line));
      }
      
      const endLine = startLine + sqlLines.length - 1 + 
        (this.diffModeVariants.has(variantIndex) && this.originalSQL.get(groupId) ? 
         this.originalSQL.get(groupId)!.trim().split('\n').length : 0);
      
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
  
  
  // Toggle diff mode for an alternative
  public toggleDiffMode(variantIndex: number): void {
    if (this.diffModeVariants.has(variantIndex)) {
      this.diffModeVariants.delete(variantIndex);
      // Clear diff lines when turning off diff mode
      this.diffLines.clear();
    } else {
      this.diffModeVariants.add(variantIndex);
    }
  }
  
  // Set original SQL for diff comparison
  public setOriginalSQL(groupId: string, sql: string): void {
    this.originalSQL.set(groupId, sql);
  }
  
  // Get original SQL for diff comparison
  public getOriginalSQL(groupId: string): string {
    return this.originalSQL.get(groupId) || '';
  }
  
  // Check if alternative is in diff mode
  public isInDiffMode(variantIndex: number): boolean {
    return this.diffModeVariants.has(variantIndex);
  }
  
  // Get diff line information for decorations
  public getDiffLines(groupId: string): { deletions: number[]; additions: number[] } | undefined {
    return this.diffLines.get(groupId);
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