import * as vscode from 'vscode';

// Domain objects matching Python backend structure
export interface Location {
  file: string;
  range: vscode.Range;
}

export interface Column {
  dataset: string | null;
  table: string | null;
  column: string | null;
}

export interface Expression {
  location: Location;
  columns: Column[];
  alias: string | null;
  sql: string;  // The actual SQL text of the expression
}

export interface Alternative {
  this: Expression;
  others: Expression[];
  reliability: number;
  similarity: number;
}

// Frontend-specific extended Alternative with additional UI metadata
export interface UIAlternative extends Alternative {
  groupId: string;  // Unique identifier for this inconsistency group
  currentFileSQL?: string;  // SQL text from the current file for comparison
  isIgnored?: boolean;  // Whether user has ignored this inconsistency
  metadata?: {
    totalOccurrences?: number;  // Total times this pattern appears
    filesAffected?: number;  // Number of files with this pattern
    lastModified?: Date;  // When was this pattern last changed
    category?: string;  // Type of inconsistency (e.g., "naming", "logic", "format")
  };
}

// Legacy interfaces for gradual migration
export interface MockVariant {
  file: string;
  line: number;
  alias: string;
  occurrences: number;
  range: vscode.Range;
  sql: string;
}

export interface MockDiagnostic {
  range: vscode.Range;
  groupId: string;
  variants: MockVariant[];
}

/*
// OLD MOCK DATA - COMMENTED OUT
// Mock diagnostics as if provided by backend LSP
export function createMockDiagnostics(document: vscode.TextDocument): vscode.Diagnostic[] {
  const diagnostics: vscode.Diagnostic[] = [];
  
  // Mock diagnostic 1: Region clustering CASE statement
  const caseRange = new vscode.Range(5, 4, 10, 8);
  const caseDiagnostic = new vscode.Diagnostic(
    caseRange,
    'Inconsistent query: alternative variants found in the codebase',
    vscode.DiagnosticSeverity.Warning
  );
  caseDiagnostic.code = 'inconsistency';
  caseDiagnostic.source = 'sql-refinery';
  caseDiagnostic.relatedInformation = [
    new vscode.DiagnosticRelatedInformation(
      new vscode.Location(
        vscode.Uri.file('/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql'),
        new vscode.Range(97, 8, 102, 12)
      ),
      'Alternative 1'
    ),
    new vscode.DiagnosticRelatedInformation(
      new vscode.Location(
        vscode.Uri.file('/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql'),
        new vscode.Range(6, 4, 11, 8)
      ),
      'Alternative 1'
    )
  ];
  diagnostics.push(caseDiagnostic);
  
  // Mock diagnostic 2: IT/Tech industry classification
  const industryRange = new vscode.Range(12, 4, 12, 60);
  const industryDiagnostic = new vscode.Diagnostic(
    industryRange,
    'Inconsistent query: alternative variants found in the codebase',
    vscode.DiagnosticSeverity.Warning
  );
  industryDiagnostic.code = 'inconsistency';
  industryDiagnostic.source = 'sql-refinery';
  industryDiagnostic.relatedInformation = [
    new vscode.DiagnosticRelatedInformation(
      new vscode.Location(
        vscode.Uri.file('/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql'),
        new vscode.Range(38, 4, 38, 60)
      ),
      'Alternative 1'
    )
  ];
  diagnostics.push(industryDiagnostic);
  
  return diagnostics;
}

// Mock variants data as if provided by backend LSP
export function getVariantsForGroup(groupId: string): MockVariant[] {
  if (groupId === '1') {
    return [
      {
        file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql',
        line: 98,
        alias: 'region_cluster',
        occurrences: 1,
        range: new vscode.Range(97, 8, 102, 12),
        sql: `CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END`
      },
      {
        file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql',
        line: 7,
        alias: 'region_cluster',
        occurrences: 1,
        range: new vscode.Range(6, 4, 11, 8),
        sql: `CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END`
      },
      {
        file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql',
        line: 33,
        alias: 'cluster',
        occurrences: 1,
        range: new vscode.Range(32, 4, 37, 8),
        sql: `CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END`
      },
      {
        file: 'Current file',
        line: 6,
        alias: 'macro_region',
        occurrences: 1,
        range: new vscode.Range(5, 4, 10, 8),
        sql: `CASE
  WHEN countries.region = 'Americas' THEN 'AMER'
  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'
  WHEN countries.region = 'Asia' THEN 'APAC'
  ELSE NULL
END`
      }
    ];
  } else if (groupId === '2') {
    return [
      {
        file: 'Current file',
        line: 13,
        alias: 'industry_it',
        occurrences: 1,
        range: new vscode.Range(12, 4, 12, 60),
        sql: `IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')`
      },
      {
        file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql',
        line: 39,
        alias: 'industry_tech',
        occurrences: 1,
        range: new vscode.Range(38, 4, 38, 60),
        sql: `IF(accounts.industry = 'Information Technology', 'Tech', 'Other')`
      }
    ];
  }
  return [];
}
*/

// New functions for Alternative-based data structure
export function getMockAlternatives(document: vscode.TextDocument): UIAlternative[] {
  const alternatives: UIAlternative[] = [];
  
  // Alternative 1: Region clustering CASE statement
  const alt1: UIAlternative = {
    this: {
      location: {
        file: document.uri.fsPath,
        range: new vscode.Range(5, 4, 10, 8)
      },
      columns: [
        { dataset: null, table: 'countries', column: 'region' }
      ],
      alias: 'macro_region',
      sql: `CASE
  WHEN countries.region = 'Americas' THEN 'AMER'
  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'
  WHEN countries.region = 'Asia' THEN 'APAC'
  ELSE NULL
END`
    },
    others: [
      {
        location: {
          file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql',
          range: new vscode.Range(97, 8, 102, 12)
        },
        columns: [
          { dataset: null, table: 'countries', column: 'region' }
        ],
        alias: 'region_cluster',
        sql: `CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END`
      },
      {
        location: {
          file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql',
          range: new vscode.Range(6, 4, 11, 8)
        },
        columns: [
          { dataset: null, table: 'countries', column: 'region' }
        ],
        alias: 'region_cluster',
        sql: `CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END`
      },
      {
        location: {
          file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql',
          range: new vscode.Range(32, 4, 37, 8)
        },
        columns: [
          { dataset: null, table: 'countries', column: 'region' }
        ],
        alias: 'cluster',
        sql: `CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END`
      }
    ],
    reliability: 3,
    similarity: 0.75,
    groupId: '1',
    metadata: {
      totalOccurrences: 4,
      filesAffected: 3,
      category: 'naming'
    }
  };
  
  // Alternative 2: IT/Tech industry classification
  const alt2: UIAlternative = {
    this: {
      location: {
        file: document.uri.fsPath,
        range: new vscode.Range(12, 4, 12, 60)
      },
      columns: [
        { dataset: null, table: 'accounts', column: 'industry' }
      ],
      alias: 'industry_it',
      sql: `IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')`
    },
    others: [
      {
        location: {
          file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql',
          range: new vscode.Range(38, 4, 38, 60)
        },
        columns: [
          { dataset: null, table: 'accounts', column: 'industry' }
        ],
        alias: 'industry_tech',
        sql: `IF(accounts.industry = 'Information Technology', 'Tech', 'Other')`
      }
    ],
    reliability: 1,
    similarity: 0.82,
    groupId: '2',
    metadata: {
      totalOccurrences: 2,
      filesAffected: 2,
      category: 'naming'
    }
  };
  
  // Set currentFileSQL after objects are created
  alt1.currentFileSQL = alt1.this.sql;
  alt2.currentFileSQL = alt2.this.sql;
  
  alternatives.push(alt1, alt2);
  return alternatives;
}

// Helper function to convert Alternative to legacy format for gradual migration
export function alternativeToMockVariants(alt: Alternative | UIAlternative): MockVariant[] {
  const variants: MockVariant[] = [];
  
  // Add the current expression
  variants.push({
    file: 'Current file',
    line: alt.this.location.range.start.line + 1,
    alias: alt.this.alias || '',
    occurrences: 1,
    range: alt.this.location.range,
    sql: alt.this.sql
  });
  
  // Add all other expressions
  for (const other of alt.others) {
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

// Helper function to create diagnostics from UIAlternatives
export function alternativesToDiagnostics(alternatives: UIAlternative[]): vscode.Diagnostic[] {
  const diagnostics: vscode.Diagnostic[] = [];
  
  for (const alt of alternatives) {
    const totalVariants = alt.others.length + 1; // +1 for the current expression
    const diagnostic = new vscode.Diagnostic(
      alt.this.location.range,
      `Inconsistent expression: ${totalVariants} variant${totalVariants > 1 ? 's' : ''} found (${Math.round(alt.similarity * 100)}% similar)`,
      vscode.DiagnosticSeverity.Information
    );
    
    diagnostic.code = alt.groupId;
    diagnostic.source = 'sql-refinery';
    
    // Add related information for all variant locations (including current)
    const allExpressions = [alt.this, ...alt.others];
    diagnostic.relatedInformation = allExpressions.map((expr, index) => 
      new vscode.DiagnosticRelatedInformation(
        new vscode.Location(
          vscode.Uri.file(expr.location.file),
          expr.location.range
        ),
        `Variant ${index + 1}: ${expr.alias || 'unnamed'}`
      )
    );
    
    diagnostics.push(diagnostic);
  }
  
  return diagnostics;
}

// Get alternatives for a specific group ID
export function getAlternativeByGroupId(groupId: string, alternatives: UIAlternative[]): UIAlternative | undefined {
  return alternatives.find(alt => alt.groupId === groupId);
}
