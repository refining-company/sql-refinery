# Test: variations

## Step: 1. File opened with diagnostics and code lenses
### Open Editors (1):
0. editor.sql (column 1) (active)

### Active Editor: editor.sql
```sql
-- CASE: Different groupings or thresholds applied to columns

SELECT 
    date(date_month, 'start of year') AS date_year,
    -- This should cause an error
    CASE
        WHEN c.region IN ('Americas') THEN 'AMER'
        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'
        WHEN c.region = 'Asia' THEN 'APAC'
        ELSE NULL
    END AS macro_region,
    -- This should case an error
    IIF(a.industry = 'Information Technology', 'IT', 'Non-IT') AS industry_it,
    SUM(ar.revenue) AS revenue,
    COUNT(DISTINCT ar.account_id) AS accounts,
    SUM(ar.revenue) / COUNT(DISTINCT ar.account_id) AS revenue_per_account
FROM accounts_revenue ar
    LEFT JOIN accounts a USING (account_id)
    LEFT JOIN countries c USING (country)
WHERE
    -- This is appropriate, user can do ad-hoc filters for any subsets
    a.industry IN ('Information Technology', 'Telecommunication Services')
    -- This is appropriate, user can take any period
    AND date_month BETWEEN DATE('now', '-24 months') AND DATE('now')
GROUP BY date_year, macro_region, industry_it
```

#### Diagnostics (2):

##### 0. Variations found: 4 with 75% similarity
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 0
- **Range**: 5:4-10:8
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END `
- **Related Information** (3):
  - 0-accounts.sql:97:8-102:12 - Location 1
    ``
  - 1-revenue.sql:6:4-11:8 - Location 2
    `    WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END AS macro_region,\n    -- T`
  - 1-revenue.sql:32:4-37:8 - Location 3
    ``


##### 1. Variations found: 2 with 82% similarity
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 1
- **Range**: 12:4-12:60
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT`
- **Related Information** (1):
  - 1-revenue.sql:38:4-38:60 - Location 1
    ``


#### Code Lenses (4):

0. **→ Show 4 variations**
   - **Range**: 5:4-10:8
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END `
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"uri":{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},"id":0,"targetRange":[{"line":5,"character":4},{"line":10,"character":8}]}]

1. **× Ignore**
   - **Range**: 5:4-10:8
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END `
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: [{"uri":{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},"id":0,"targetRange":[{"line":5,"character":4},{"line":10,"character":8}]}]

2. **→ Show 2 variations**
   - **Range**: 12:4-12:60
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"uri":{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},"id":1,"targetRange":[{"line":12,"character":4},{"line":12,"character":60}]}]

3. **× Ignore**
   - **Range**: 12:4-12:60
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: [{"uri":{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},"id":1,"targetRange":[{"line":12,"character":4},{"line":12,"character":60}]}]




## Step: 2. Showed variations for first inconsistency (CASE statement)
### Open Editors (2):
0. editor.sql (column 1)
1. sql-refinery-explorer:/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql/variation-0 (column 2) (active)

### Active Editor: sql-refinery-explorer:/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql/variation-0
```sql
-- SQL-Refinery
-- Expression variations found in the codebase

-- Variation 0
CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END

-- Variation 1
CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END

-- Variation 2
CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END

```

#### Diagnostics (0):

#### Code Lenses (9):

0. **→ Peek locations**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.peek`
   - **Arguments**: undefined

1. **↔ Show diff**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.diff`
   - **Arguments**: undefined

2. **✓ Apply**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.apply`
   - **Arguments**: undefined

3. **→ Peek locations**
   - **Range**: 11:0-11:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.peek`
   - **Arguments**: undefined

4. **↔ Show diff**
   - **Range**: 11:0-11:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.diff`
   - **Arguments**: undefined

5. **✓ Apply**
   - **Range**: 11:0-11:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.apply`
   - **Arguments**: undefined

6. **→ Peek locations**
   - **Range**: 18:0-18:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.peek`
   - **Arguments**: undefined

7. **↔ Show diff**
   - **Range**: 18:0-18:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.diff`
   - **Arguments**: undefined

8. **✓ Apply**
   - **Range**: 18:0-18:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.apply`
   - **Arguments**: undefined




## Step: 3. Peek locations opened for first variation
### Open Editors (2):
0. editor.sql (column 1)
1. sql-refinery-explorer:/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql/variation-0 (column 2) (active)

### Active Editor: sql-refinery-explorer:/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql/variation-0
```sql
-- SQL-Refinery
-- Expression variations found in the codebase

-- Variation 0
CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END

-- Variation 1
CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END

-- Variation 2
CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END

```

#### Diagnostics (0):

#### Code Lenses (9):

0. **→ Peek locations**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.peek`
   - **Arguments**: undefined

1. **↔ Show diff**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.diff`
   - **Arguments**: undefined

2. **✓ Apply**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.apply`
   - **Arguments**: undefined

3. **→ Peek locations**
   - **Range**: 11:0-11:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.peek`
   - **Arguments**: undefined

4. **↔ Show diff**
   - **Range**: 11:0-11:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.diff`
   - **Arguments**: undefined

5. **✓ Apply**
   - **Range**: 11:0-11:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.apply`
   - **Arguments**: undefined

6. **→ Peek locations**
   - **Range**: 18:0-18:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.peek`
   - **Arguments**: undefined

7. **↔ Show diff**
   - **Range**: 18:0-18:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.diff`
   - **Arguments**: undefined

8. **✓ Apply**
   - **Range**: 18:0-18:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.apply`
   - **Arguments**: undefined




## Step: 4. Applied first variation (CASE statement replaced)
### Open Editors (2):
0. editor.sql (column 1)
1. sql-refinery-explorer:/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql/variation-0 (column 2) (active)

### Active Editor: sql-refinery-explorer:/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql/variation-0
```sql
-- SQL-Refinery
-- Expression variations found in the codebase

-- Variation 0
CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END

-- Variation 1
CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END

-- Variation 2
CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END

```

#### Diagnostics (0):

#### Code Lenses (9):

0. **→ Peek locations**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.peek`
   - **Arguments**: undefined

1. **↔ Show diff**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.diff`
   - **Arguments**: undefined

2. **✓ Apply**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.apply`
   - **Arguments**: undefined

3. **→ Peek locations**
   - **Range**: 11:0-11:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.peek`
   - **Arguments**: undefined

4. **↔ Show diff**
   - **Range**: 11:0-11:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.diff`
   - **Arguments**: undefined

5. **✓ Apply**
   - **Range**: 11:0-11:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.apply`
   - **Arguments**: undefined

6. **→ Peek locations**
   - **Range**: 18:0-18:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.peek`
   - **Arguments**: undefined

7. **↔ Show diff**
   - **Range**: 18:0-18:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.diff`
   - **Arguments**: undefined

8. **✓ Apply**
   - **Range**: 18:0-18:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.apply`
   - **Arguments**: undefined




## Step: 5. Showed variations for second inconsistency (IIF statement)
### Open Editors (3):
0. editor.sql (column 1)
1. editor.sql (column 2)
2. sql-refinery-explorer:/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql/variation-1 (column 3) (active)

### Active Editor: sql-refinery-explorer:/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql/variation-1
```sql
-- SQL-Refinery
-- Expression variations found in the codebase

-- Variation 0
IF(accounts.industry = 'Information Technology', 'Tech', 'Other')

```

#### Diagnostics (0):

#### Code Lenses (3):

0. **→ Peek locations**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.peek`
   - **Arguments**: undefined

1. **↔ Show diff**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.diff`
   - **Arguments**: undefined

2. **✓ Apply**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.apply`
   - **Arguments**: undefined




## Step: 6. Final state - workflow completed
### Open Editors (3):
0. editor.sql (column 1)
1. editor.sql (column 2)
2. sql-refinery-explorer:/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql/variation-1 (column 3) (active)

### Active Editor: sql-refinery-explorer:/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql/variation-1
```sql
-- SQL-Refinery
-- Expression variations found in the codebase

-- Variation 0
IF(accounts.industry = 'Information Technology', 'Tech', 'Other')

```

#### Diagnostics (0):

#### Code Lenses (3):

0. **→ Peek locations**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.peek`
   - **Arguments**: undefined

1. **↔ Show diff**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.diff`
   - **Arguments**: undefined

2. **✓ Apply**
   - **Range**: 4:0-4:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.variations.explorer.apply`
   - **Arguments**: undefined



