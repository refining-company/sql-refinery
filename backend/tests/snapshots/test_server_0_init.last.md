# Testing Server

## client->server
```json
{
  "id": "f777359b-ef50-47d3-97c1-ca221c8c4716",
  "params": {
    "capabilities": {},
    "processId": 68056,
    "rootPath": null,
    "rootUri": null,
    "workspaceFolders": [
      { "uri": "file://${workspaceFolder}/tests/inputs/codebase",
        "name": "codebase" } ] },
  "method": "initialize",
  "jsonrpc": "2.0" }
```

## server->client
```json
{
  "id": "f777359b-ef50-47d3-97c1-ca221c8c4716",
  "jsonrpc": "2.0",
  "result": {
    "capabilities": {
      "positionEncoding": "utf-16",
      "textDocumentSync": {
        "openClose": true,
        "change": 2,
        "save": false },
      "codeLensProvider": {},
      "executeCommandProvider": { "commands": [] },
      "workspace": {
        "workspaceFolders": {
          "supported": true,
          "changeNotifications": true },
        "fileOperations": {} } },
    "serverInfo": {
      "name": "sql-refinery-server",
      "version": "0.1-dev" } } }
```

## client->server
```json
{
  "params": {},
  "method": "initialized",
  "jsonrpc": "2.0" }
```

## client->server
```json
{
  "params": {
    "textDocument": {
      "uri": "file://${workspaceFolder}/tests/inputs/editor.sql",
      "languageId": "sql",
      "version": 1,
      "text": "-- CASE: Different groupings or thresholds applied to columns\n\nSELECT \n    date(date_month, 'start of year') AS date_year,\n    -- This should cause an error\n    CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END AS macro_region,\n    -- This should case an error\n    IIF(a.industry = 'Information Technology', 'IT', 'Non-IT') AS industry_it,\n    SUM(ar.revenue) AS revenue,\n    COUNT(DISTINCT ar.account_id) AS accounts,\n    SUM(ar.revenue) / COUNT(DISTINCT ar.account_id) AS revenue_per_account\nFROM accounts_revenue ar\n    LEFT JOIN accounts a USING (account_id)\n    LEFT JOIN countries c USING (country)\nWHERE\n    -- This is appropriate, user can do ad-hoc filters for any subsets\n    a.industry IN ('Information Technology', 'Telecommunication Services')\n    -- This is appropriate, user can take any period\n    AND date_month BETWEEN DATE('now', '-24 months') AND DATE('now')\nGROUP BY date_year, macro_region, industry_it" } },
  "method": "textDocument/didOpen",
  "jsonrpc": "2.0" }
```

## server->client
```json
{
  "params": {
    "uri": "file://${workspaceFolder}/tests/inputs/editor.sql",
    "diagnostics": [
      { "range": {
          "start": {
            "line": 5,
            "character": 4 },
          "end": {
            "line": 10,
            "character": 7 } },
        "message": "Variation expressions found in the codebase",
        "severity": 3,
        "code": "Variation" },
      { "range": {
          "start": {
            "line": 12,
            "character": 4 },
          "end": {
            "line": 12,
            "character": 62 } },
        "message": "Variation expressions found in the codebase",
        "severity": 3,
        "code": "Variation" } ] },
  "method": "textDocument/publishDiagnostics",
  "jsonrpc": "2.0" }
```

## client->server
```json
{
  "id": "1f509425-1f72-48ee-8f43-69c097b63d8d",
  "params": {
    "textDocument": { "uri": "file://${workspaceFolder}/tests/inputs/editor.sql" } },
  "method": "textDocument/codeLens",
  "jsonrpc": "2.0" }
```

## server->client
```json
{
  "id": "1f509425-1f72-48ee-8f43-69c097b63d8d",
  "jsonrpc": "2.0",
  "result": [
    { "range": {
        "start": {
          "line": 5,
          "character": 4 },
        "end": {
          "line": 10,
          "character": 7 } },
      "command": {
        "title": "Variations found: 3",
        "command": "sqlRefinery.peekLocations",
        "arguments": [
          "file://${workspaceFolder}/tests/inputs/editor.sql",
          { "line": 10,
            "character": 7 },
          [
            { "uri": "file://${workspaceFolder}/tests/inputs/codebase/0-accounts.sql",
              "position": {
                "line": 97,
                "character": 8 },
              "range": {
                "start": {
                  "line": 97,
                  "character": 8 },
                "end": {
                  "line": 101,
                  "character": 11 } } },
            { "uri": "file://${workspaceFolder}/tests/inputs/codebase/1-revenue.sql",
              "position": {
                "line": 6,
                "character": 4 },
              "range": {
                "start": {
                  "line": 6,
                  "character": 4 },
                "end": {
                  "line": 10,
                  "character": 7 } } },
            { "uri": "file://${workspaceFolder}/tests/inputs/codebase/1-revenue.sql",
              "position": {
                "line": 32,
                "character": 4 },
              "range": {
                "start": {
                  "line": 32,
                  "character": 4 },
                "end": {
                  "line": 36,
                  "character": 7 } } } ],
          "peek" ] } },
    { "range": {
        "start": {
          "line": 12,
          "character": 4 },
        "end": {
          "line": 12,
          "character": 62 } },
      "command": {
        "title": "Variations found: 1",
        "command": "sqlRefinery.peekLocations",
        "arguments": [
          "file://${workspaceFolder}/tests/inputs/editor.sql",
          { "line": 12,
            "character": 62 },
          [
            { "uri": "file://${workspaceFolder}/tests/inputs/codebase/1-revenue.sql",
              "position": {
                "line": 38,
                "character": 4 },
              "range": {
                "start": {
                  "line": 38,
                  "character": 4 },
                "end": {
                  "line": 38,
                  "character": 70 } } } ],
          "peek" ] } } ] }
```

## client->server
```json
{
  "id": "102ccca5-36c3-4595-bf16-48131b44116b",
  "method": "shutdown",
  "jsonrpc": "2.0",
  "params": {} }
```

## server->client
```json
{
  "id": "102ccca5-36c3-4595-bf16-48131b44116b",
  "jsonrpc": "2.0",
  "result": null }
```
