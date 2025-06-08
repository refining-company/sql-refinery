import * as vscode from 'vscode';

// Mock data simulating what the backend LSP would provide
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

export interface MockDiffLine {
  type: 'common' | 'deletion' | 'addition';
  content: string;
  lineNumber: number;
}

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
      'Variant 1'
    ),
    new vscode.DiagnosticRelatedInformation(
      new vscode.Location(
        vscode.Uri.file('/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql'),
        new vscode.Range(6, 4, 11, 8)
      ),
      'Variant 1'
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
      'Variant 1'
    )
  ];
  diagnostics.push(industryDiagnostic);
  
  return diagnostics;
}

// Mock variants data as if provided by backend LSP
export function getVariantsForGroup(groupId: string): MockVariant[] {
  if (groupId === 'region-clustering') {
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
  } else if (groupId === 'industry-classification') {
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

// Mock diff data as if computed by backend
export function getMockDiffLines(originalSql: string, variantSql: string): MockDiffLine[] {
  // This simulates what the backend would provide
  // In reality, this would come from the LSP server
  const diffLines: MockDiffLine[] = [
    { type: 'common', content: 'CASE', lineNumber: 0 },
    { type: 'deletion', content: "  WHEN countries.region = 'Americas' THEN 'AMER'", lineNumber: 1 },
    { type: 'deletion', content: "  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'", lineNumber: 2 },
    { type: 'deletion', content: "  WHEN countries.region = 'Asia' THEN 'APAC'", lineNumber: 3 },
    { type: 'addition', content: "  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'", lineNumber: 1 },
    { type: 'addition', content: "  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'", lineNumber: 2 },
    { type: 'common', content: '  ELSE NULL', lineNumber: 4 },
    { type: 'common', content: 'END', lineNumber: 5 }
  ];
  return diffLines;
}