import * as vscode from 'vscode';
import { Variation, Expression } from './mockData';

// UI-specific metadata for variations
export interface VariationMetadata {
  groupId: string;
  totalOccurrences: number;
  filesAffected: number;
  category?: string;
}

// Helper type for internal use
interface VariationWithMetadata extends Variation {
  metadata: VariationMetadata;
}

// Generate unique group ID for a variation
function generateGroupId(variation: Variation, index: number): string {
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

// Create code lens for a variation
export function createVariationCodeLens(variation: Variation, groupId: string): vscode.CodeLens {
  const range = variation.this.location.range;
  const title = `${variation.others.length} variation${variation.others.length !== 1 ? 's' : ''} found`;
  
  const otherLocations = variation.others.map(other => ({
    uri: other.location.file,
    position: new vscode.Position(other.location.range.start.line, other.location.range.start.character),
    range: other.location.range
  }));
  
  return new vscode.CodeLens(
    range,
    {
      title,
      command: 'sqlRefinery.peekLocations',
      arguments: [variation.this.location.file, range.end, otherLocations, 'peek']
    }
  );
}

// Enrich variations with metadata for UI display
export function enrichVariationsWithMetadata(variations: Variation[]): VariationWithMetadata[] {
  return variations.map((variation, index) => {
    const allExpressions = [variation.this, ...variation.others];
    const uniqueFiles = new Set(allExpressions.map(expr => expr.location.file));
    
    return {
      ...variation,
      metadata: {
        groupId: generateGroupId(variation, index),
        totalOccurrences: allExpressions.length,
        filesAffected: uniqueFiles.size,
        category: determineVariationCategory(variation)
      }
    };
  });
}

// Determine the category of variation (naming, logic, format, etc.)
function determineVariationCategory(variation: Variation): string {
  // Simple heuristic - can be enhanced
  const thisAlias = variation.this.alias?.toLowerCase() || '';
  const otherAliases = variation.others.map(o => o.alias?.toLowerCase() || '');
  
  // Check if it's primarily a naming difference
  const hasDifferentAliases = otherAliases.some(alias => alias && alias !== thisAlias);
  if (hasDifferentAliases) {
    return 'naming';
  }
  
  // Check if it's a logic difference (different SQL content)
  const thisSqlNormalized = variation.this.sql.replace(/\s+/g, ' ').trim();
  const hasDifferentLogic = variation.others.some(
    other => other.sql.replace(/\s+/g, ' ').trim() !== thisSqlNormalized
  );
  if (hasDifferentLogic) {
    return 'logic';
  }
  
  return 'format';
}