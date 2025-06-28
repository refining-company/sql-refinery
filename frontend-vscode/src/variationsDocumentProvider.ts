import * as vscode from 'vscode';
import * as path from 'path';
import { generateVirtualDocumentContent, VirtualDocumentSection, VirtualDocumentVariant } from './variations';

export class VariationsProvider implements vscode.TextDocumentContentProvider {
  // Fired when you want VS Code to refresh the content
  private _onDidChange = new vscode.EventEmitter<vscode.Uri>();
  readonly onDidChange = this._onDidChange.event;

  // Store variation data by groupId
  private variationData = new Map<string, VirtualDocumentVariant[]>();
  
  // Store plain SQL content for diff documents
  private diffContent = new Map<string, string>();
  
  // Store metadata for code lens positioning
  private variationMetadata = new Map<string, VirtualDocumentSection[]>();
  
  // Store original SQL for diff comparison per group
  private originalSQL = new Map<string, string>();

  constructor() {}

  // VS Code calls this whenever it needs the document's text
  async provideTextDocumentContent(uri: vscode.Uri): Promise<string> {
    
    // Handle diff documents - return plain SQL
    if (uri.path.includes('diff-')) {
      // Extract the full groupId including the .sql extension
      const groupId = uri.path.startsWith('/') ? uri.path.substring(1) : uri.path;
      return this.diffContent.get(groupId) || '';
    }
    
    // Extract groupId from document name: editor.sql:variation-N
    const match = uri.path.match(/variation-(\d+)/);
    const groupId = match ? match[1] : 'current';
    const variants = this.variationData.get(groupId) || [];
    
    // Use the translation layer to generate content
    const result = generateVirtualDocumentContent(variants);
    
    // Store metadata for code lens provider
    this.variationMetadata.set(groupId, result.metadata);

    return result.content;
  }

  // Store variation data for a group
  public setVariants(groupId: string, variants: VirtualDocumentVariant[]): void {
    this.variationData.set(groupId, variants);
  }
  
  // Store plain SQL content for diff documents
  public setDiffContent(groupId: string, sql: string): void {
    this.diffContent.set(groupId, sql);
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
  public getVariantMetadata(groupId: string): VirtualDocumentSection[] | undefined {
    return this.variationMetadata.get(groupId);
  }

  // Call this if you ever need to refresh the view
  public refresh(uri: vscode.Uri): void {
    this._onDidChange.fire(uri);
  }
}