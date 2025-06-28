import * as vscode from 'vscode';
import { Variation } from './mockData';

// Generate unique group ID for a variation
function generateGroupId(_variation: Variation, index: number): string {
  return `${index + 1}`;
}

// Convert variations to VS Code diagnostics
export function variationsToDiagnostics(variations: Variation[]): vscode.Diagnostic[] {
  const diagnostics: vscode.Diagnostic[] = [];
  
  variations.forEach((variation, index) => {
    const totalVariations = variation.others.length + 1; // +1 for the current expression
    const diagnostic = new vscode.Diagnostic(
      variation.this.location.range,
      `${totalVariations} variation${totalVariations > 1 ? 's' : ''} found (${Math.round(variation.similarity * 100)}% similar)`,
      vscode.DiagnosticSeverity.Information
    );
    
    diagnostic.code = generateGroupId(variation, index);
    diagnostic.source = 'sql-refinery';
    
    // Add related information for all variation locations (including current)
    const allExpressions = [variation.this, ...variation.others];
    diagnostic.relatedInformation = allExpressions.map((expr, idx) => 
      new vscode.DiagnosticRelatedInformation(
        new vscode.Location(
          vscode.Uri.file(expr.location.file),
          expr.location.range
        ),
        `Variation ${idx + 1}: ${expr.alias || 'unnamed'}`
      )
    );
    
    diagnostics.push(diagnostic);
  });
  
  return diagnostics;
}

// Get variation by group ID
export function getVariationByGroupId(groupId: string, variations: Variation[]): Variation | undefined {
  const index = parseInt(groupId) - 1;
  return variations[index];
}

// Convert a variation to a format suitable for virtual document display
export interface VirtualDocumentVariant {
  file: string;
  line: number;
  alias: string;
  occurrences: number;
  range: vscode.Range;
  sql: string;
}

export function variationToVirtualDocumentVariants(variation: Variation): VirtualDocumentVariant[] {
  const variants: VirtualDocumentVariant[] = [];
  
  // Add the current expression
  variants.push({
    file: 'Current file',
    line: variation.this.location.range.start.line + 1,
    alias: variation.this.alias || '',
    occurrences: 1,
    range: variation.this.location.range,
    sql: variation.this.sql
  });
  
  // Add all other expressions
  for (const other of variation.others) {
    variants.push({
      file: other.location.file,
      line: other.location.range.start.line + 1,
      alias: other.alias || '',
      occurrences: 1,
      range: other.location.range,
      sql: other.sql
    });
  }
  
  return variants;
}




// Virtual document content generation for variations display
export interface VirtualDocumentSection {
  startLine: number;
  endLine: number;
  variant: {
    sql: string;
    locations: VirtualDocumentVariant[];
    variantIndex: number;
  };
}

export interface VirtualDocumentResult {
  content: string;
  metadata: VirtualDocumentSection[];
}

export function generateVirtualDocumentContent(variants: VirtualDocumentVariant[]): VirtualDocumentResult {
  if (variants.length === 0) {
    return {
      content: '-- No variations found\n-- No SQL variations were found for this group.',
      metadata: []
    };
  }

  // Group variations by their SQL content to find distinct variations
  const distinctVariations = new Map<string, { sql: string; locations: VirtualDocumentVariant[] }>();
  
  variants.forEach(v => {
    const key = v.sql.trim();
    if (!distinctVariations.has(key)) {
      distinctVariations.set(key, { sql: v.sql, locations: [] });
    }
    distinctVariations.get(key)!.locations.push(v);
  });

  // Build a SQL document with distinct variations
  const lines: string[] = [];
  const metadata: VirtualDocumentSection[] = [];
  
  // Add header comment
  lines.push('-- SQL-Refinery');
  lines.push('-- SQL variations found in the codebase');
  lines.push('');
  
  let currentLine = 3;
  let variationIndex = 1;

  distinctVariations.forEach((data) => {
    // Add variation header
    lines.push(`-- Variation ${variationIndex}`);
    const startLine = currentLine + 1;
    
    // Add the SQL content
    const sqlLines = data.sql.trim().split('\n');
    sqlLines.forEach((line: string) => lines.push(line));
    
    const endLine = startLine + sqlLines.length - 1;
    
    // Create a variation object with all locations
    const variationWithLocations = {
      sql: data.sql,
      locations: data.locations,
      variantIndex: variationIndex
    };
    
    // Store metadata for code lens
    metadata.push({ startLine, endLine, variant: variationWithLocations });
    
    // Add blank lines between variations
    lines.push('');
    lines.push('');
    
    currentLine = endLine + 3;
    variationIndex++;
  });

  return {
    content: lines.join('\n'),
    metadata
  };
}

// Generate code lenses for virtual document sections
export function generateVirtualDocumentCodeLenses(
  metadata: VirtualDocumentSection[], 
  groupId: string, 
  originalSQL: string
): vscode.CodeLens[] {
  const codeLenses: vscode.CodeLens[] = [];

  metadata.forEach(({ startLine, endLine, variant }) => {
    const range = new vscode.Range(startLine - 1, 0, startLine - 1, 0);
    
    // Locations lens
    const locationCount = variant.locations.length;
    
    // Position peek at the bottom of the variant code
    const peekPosition = new vscode.Position(endLine, 0);
    
    const locationsLens = new vscode.CodeLens(range, {
      title: `→ Peek ${locationCount} locations`,
      command: 'sql-refinery.peekLocations',
      arguments: [{
        locations: variant.locations,
        groupId: groupId,
        position: peekPosition
      }],
      tooltip: 'Peek at all locations where this variation appears'
    });
    codeLenses.push(locationsLens);

    // Show native diff lens
    const diffLens = new vscode.CodeLens(range, {
      title: '↔ Show diff',
      command: 'sql-refinery.showNativeDiff',
      arguments: [{ 
        variant, 
        originalSQL,
        groupId,
        variantIndex: variant.variantIndex
      }],
      tooltip: 'Show differences in native diff editor'
    });
    codeLenses.push(diffLens);
    
    // Apply variation lens
    const applyLens = new vscode.CodeLens(range, {
      title: '✓ Apply',
      command: 'sql-refinery.applyVariation',
      arguments: [{ variant, groupId: groupId }],
      tooltip: 'Replace current SQL with this variation'
    });
    codeLenses.push(applyLens);
  });

  return codeLenses;
}