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

#### Diagnostics (4):

##### 0. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 0
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 1. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 1
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


##### 2. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 2
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 3. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 3
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


#### Code Lenses (8):

0. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},0]

1. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

2. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},2]

3. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

4. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},1]

5. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

6. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},3]

7. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined




## Step: 2. Showed variations for first inconsistency (CASE statement)
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

#### Diagnostics (4):

##### 0. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 0
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 1. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 1
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


##### 2. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 2
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 3. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 3
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


#### Code Lenses (8):

0. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},0]

1. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

2. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},2]

3. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

4. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},1]

5. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

6. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},3]

7. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined




## Step: 3. Peek locations opened for first variation
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

#### Diagnostics (4):

##### 0. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 0
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 1. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 1
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


##### 2. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 2
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 3. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 3
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


#### Code Lenses (8):

0. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},0]

1. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

2. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},2]

3. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

4. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},1]

5. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

6. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},3]

7. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined




## Step: 4. Applied first variation (CASE statement replaced)
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

#### Diagnostics (4):

##### 0. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 0
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 1. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 1
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


##### 2. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 2
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 3. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 3
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


#### Code Lenses (8):

0. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},0]

1. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

2. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},2]

3. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

4. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},1]

5. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

6. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},3]

7. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined




## Step: 5. Showed variations for second inconsistency (IIF statement)
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

#### Diagnostics (4):

##### 0. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 0
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 1. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 1
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


##### 2. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 2
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 3. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 3
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


#### Code Lenses (8):

0. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},0]

1. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

2. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},2]

3. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

4. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},1]

5. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

6. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},3]

7. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined




## Step: 6. Final state - workflow completed
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

#### Diagnostics (4):

##### 0. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 0
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 1. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 1
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


##### 2. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 2
- **Range**: 5:4-10:7
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`


##### 3. 1 variation found
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 3
- **Range**: 12:4-12:62
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`


#### Code Lenses (8):

0. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},0]

1. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

2. **→ Show 1 variation**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},2]

3. **× Ignore**
   - **Range**: 5:4-10:7
   - **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

4. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},1]

5. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined

6. **→ Show 1 variation**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.show`
   - **Arguments**: [{"$mid":1,"fsPath":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","external":"file:///Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","path":"/Users/ilyakochik/Developer/refining-company/sql-refinery/frontend-vscode/src/test/inputs/editor.sql","scheme":"file"},3]

7. **× Ignore**
   - **Range**: 12:4-12:62
   - **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`
   - **Command**: `sql-refinery.variations.ignore`
   - **Arguments**: undefined



