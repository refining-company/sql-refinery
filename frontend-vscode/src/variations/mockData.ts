import * as vscode from 'vscode';

// Core interfaces matching Python backend structure
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
  locations?: Location[]; // Additional locations where this exact expression appears
  columns: Column[];
  alias: string | null;
  sql: string; // The actual SQL text of the expression
}

export interface Variation {
  this: Expression;
  others: Expression[];
  reliability: number;
  similarity: number;
}

// Mock data generation for testing
export function getMockVariations(document: vscode.TextDocument): Variation[] {
  const variations: Variation[] = [];

  // Variation 1: Region clustering CASE statement
  const var1: Variation = {
    this: {
      location: {
        file: document.uri.fsPath,
        range: new vscode.Range(5, 4, 10, 7),
      },
      columns: [{ dataset: null, table: 'countries', column: 'region' }],
      alias: 'macro_region',
      sql: `CASE
    WHEN c.region = 'Americas' THEN 'AMER'
    WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'
    WHEN c.region = 'Asia' THEN 'APAC'
    ELSE NULL
END`,
    },
    others: [
      {
        location: {
          file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql',
          range: new vscode.Range(97, 1, 102, 12),
        },
        locations: [
          {
            file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql',
            range: new vscode.Range(97, 8, 102, 12),
          },
          {
            file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql',
            range: new vscode.Range(6, 4, 10, 7),
          },
          {
            file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql',
            range: new vscode.Range(32, 4, 36, 7),
          },
        ],
        columns: [{ dataset: null, table: 'countries', column: 'region' }],
        alias: 'region_cluster',
        sql: `CASE
    WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'
    WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'
    ELSE NULL
END`,
      },
    ],
    reliability: 3,
    similarity: 0.75,
  };

  // Variation 2: IT/Tech industry classification
  const var2: Variation = {
    this: {
      location: {
        file: document.uri.fsPath,
        range: new vscode.Range(12, 4, 12, 62),
      },
      columns: [{ dataset: null, table: 'accounts', column: 'industry' }],
      alias: 'industry_it',
      sql: `IIF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')`,
    },
    others: [
      {
        location: {
          file: '/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql',
          range: new vscode.Range(38, 4, 38, 60),
        },
        columns: [{ dataset: null, table: 'accounts', column: 'industry' }],
        alias: 'industry_tech',
        sql: `IF(accounts.industry = 'Information Technology', 'Tech', 'Other')`,
      },
    ],
    reliability: 1,
    similarity: 0.82,
  };

  variations.push(var1, var2);
  return variations;
}
