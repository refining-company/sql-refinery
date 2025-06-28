# Test: alternatives

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

##### 0. 4 variations found (75% similar)
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 1
- **Range**: 5:4-10:8
- **Snippet**: `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END `
- **Related Information** (4):
  - editor.sql:5:4-10:8 - Variation 1: macro_region
    `CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END `
  - 0-accounts.sql:97:8-102:12 - Variation 2: region_cluster
    ``
  - 1-revenue.sql:6:4-11:8 - Variation 3: region_cluster
    `    WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END AS macro_region,\n    -- T`
  - 1-revenue.sql:32:4-37:8 - Variation 4: cluster
    ``


##### 1. 2 variations found (82% similar)
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 2
- **Range**: 12:4-12:60
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT`
- **Related Information** (2):
  - editor.sql:12:4-12:60 - Variation 1: industry_it
    `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT`
  - 1-revenue.sql:38:4-38:60 - Variation 2: industry_tech
    ``


#### Code Lenses (4):

0. **→ Show 4 alternatives**
   - **Range**: 5:0-5:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showVariantsEditor`
   - **Arguments**: [{"groupId":"1","currentRange":[{"line":5,"character":4},{"line":10,"character":8}]}]

1. **× Ignore**
   - **Range**: 5:0-5:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.ignoreVariant`
   - **Arguments**: [{"groupId":"1","diagnosticRange":[{"line":5,"character":4},{"line":10,"character":8}]}]

2. **→ Show 2 alternatives**
   - **Range**: 12:0-12:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showVariantsEditor`
   - **Arguments**: [{"groupId":"2","currentRange":[{"line":12,"character":4},{"line":12,"character":60}]}]

3. **× Ignore**
   - **Range**: 12:0-12:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.ignoreVariant`
   - **Arguments**: [{"groupId":"2","diagnosticRange":[{"line":12,"character":4},{"line":12,"character":60}]}]




## Step: 2. Showed alternatives for first inconsistency (CASE statement)
### Open Editors (2):
0. editor.sql (column 1)
1. sql-refinery-inconsistencies:editor.sql%3Ainconsistency-1 (column 2) (active)

### Active Editor: sql-refinery-inconsistencies:editor.sql%3Ainconsistency-1
```sql
-- SQL-Refinery
-- Inconsistent query: alternative variants found in the codebase

-- Alternative 1
CASE
  WHEN countries.region = 'Americas' THEN 'AMER'
  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'
  WHEN countries.region = 'Asia' THEN 'APAC'
  ELSE NULL
END


-- Alternative 2
CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END


```

#### Diagnostics (0):

#### Code Lenses (6):

0. **→ Peek 1 locations**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.peekLocations`
   - **Arguments**: [{"locations":[{"file":"Current file","line":6,"alias":"macro_region","sql":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":5,"character":4},{"line":10,"character":8}]}],"groupId":"1","position":{"line":9,"character":0}}]

1. **↔ Show diff**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showNativeDiff`
   - **Arguments**: [{"variant":{"sql":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","locations":[{"file":"Current file","line":6,"alias":"macro_region","sql":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":5,"character":4},{"line":10,"character":8}]}],"variantIndex":1},"originalSQL":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","groupId":"1","variantIndex":1}]

2. **✓ Apply**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.applyVariant`
   - **Arguments**: [{"variant":{"sql":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","locations":[{"file":"Current file","line":6,"alias":"macro_region","sql":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":5,"character":4},{"line":10,"character":8}]}],"variantIndex":1},"groupId":"1"}]

3. **→ Peek 3 locations**
   - **Range**: 12:0-12:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.peekLocations`
   - **Arguments**: [{"locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql","line":98,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":97,"character":8},{"line":102,"character":12}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":7,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":6,"character":4},{"line":11,"character":8}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":33,"alias":"cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":32,"character":4},{"line":37,"character":8}]}],"groupId":"1","position":{"line":17,"character":0}}]

4. **↔ Show diff**
   - **Range**: 12:0-12:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showNativeDiff`
   - **Arguments**: [{"variant":{"sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql","line":98,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":97,"character":8},{"line":102,"character":12}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":7,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":6,"character":4},{"line":11,"character":8}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":33,"alias":"cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":32,"character":4},{"line":37,"character":8}]}],"variantIndex":2},"originalSQL":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","groupId":"1","variantIndex":2}]

5. **✓ Apply**
   - **Range**: 12:0-12:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.applyVariant`
   - **Arguments**: [{"variant":{"sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql","line":98,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":97,"character":8},{"line":102,"character":12}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":7,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":6,"character":4},{"line":11,"character":8}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":33,"alias":"cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":32,"character":4},{"line":37,"character":8}]}],"variantIndex":2},"groupId":"1"}]




## Step: 3. Peek locations opened for first alternative
### Open Editors (2):
0. editor.sql (column 1)
1. sql-refinery-inconsistencies:editor.sql%3Ainconsistency-1 (column 2) (active)

### Active Editor: sql-refinery-inconsistencies:editor.sql%3Ainconsistency-1
```sql
-- SQL-Refinery
-- Inconsistent query: alternative variants found in the codebase

-- Alternative 1
CASE
  WHEN countries.region = 'Americas' THEN 'AMER'
  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'
  WHEN countries.region = 'Asia' THEN 'APAC'
  ELSE NULL
END


-- Alternative 2
CASE
  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
  ELSE NULL
END


```

#### Diagnostics (0):

#### Code Lenses (6):

0. **→ Peek 1 locations**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.peekLocations`
   - **Arguments**: [{"locations":[{"file":"Current file","line":6,"alias":"macro_region","sql":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":5,"character":4},{"line":10,"character":8}]}],"groupId":"1","position":{"line":9,"character":0}}]

1. **↔ Show diff**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showNativeDiff`
   - **Arguments**: [{"variant":{"sql":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","locations":[{"file":"Current file","line":6,"alias":"macro_region","sql":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":5,"character":4},{"line":10,"character":8}]}],"variantIndex":1},"originalSQL":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","groupId":"1","variantIndex":1}]

2. **✓ Apply**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.applyVariant`
   - **Arguments**: [{"variant":{"sql":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","locations":[{"file":"Current file","line":6,"alias":"macro_region","sql":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":5,"character":4},{"line":10,"character":8}]}],"variantIndex":1},"groupId":"1"}]

3. **→ Peek 3 locations**
   - **Range**: 12:0-12:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.peekLocations`
   - **Arguments**: [{"locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql","line":98,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":97,"character":8},{"line":102,"character":12}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":7,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":6,"character":4},{"line":11,"character":8}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":33,"alias":"cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":32,"character":4},{"line":37,"character":8}]}],"groupId":"1","position":{"line":17,"character":0}}]

4. **↔ Show diff**
   - **Range**: 12:0-12:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showNativeDiff`
   - **Arguments**: [{"variant":{"sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql","line":98,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":97,"character":8},{"line":102,"character":12}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":7,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":6,"character":4},{"line":11,"character":8}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":33,"alias":"cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":32,"character":4},{"line":37,"character":8}]}],"variantIndex":2},"originalSQL":"CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nEND","groupId":"1","variantIndex":2}]

5. **✓ Apply**
   - **Range**: 12:0-12:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.applyVariant`
   - **Arguments**: [{"variant":{"sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql","line":98,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":97,"character":8},{"line":102,"character":12}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":7,"alias":"region_cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":6,"character":4},{"line":11,"character":8}]},{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":33,"alias":"cluster","sql":"CASE\n  WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'\n  WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'\n  ELSE NULL\nEND","occurrences":1,"range":[{"line":32,"character":4},{"line":37,"character":8}]}],"variantIndex":2},"groupId":"1"}]




## Step: 4. Applied first alternative (CASE statement replaced)
### Open Editors (1):
0. editor.sql (column 1) (active)

### Active Editor: editor.sql
```sql
-- CASE: Different groupings or thresholds applied to columns

SELECT 
    date(date_month, 'start of year') AS date_year,
    -- This should cause an error
    CASE
  WHEN countries.region = 'Americas' THEN 'AMER'
  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'
  WHEN countries.region = 'Asia' THEN 'APAC'
  ELSE NULL
ENDAS macro_region,
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

##### 0. 4 variations found (75% similar)
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 1
- **Range**: 5:4-10:8
- **Snippet**: `CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nENDAS ma`
- **Related Information** (4):
  - editor.sql:5:4-10:8 - Variation 1: macro_region
    `CASE\n  WHEN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nENDAS ma`
  - 0-accounts.sql:97:8-102:12 - Variation 2: region_cluster
    ``
  - 1-revenue.sql:6:4-11:8 - Variation 3: region_cluster
    `EN countries.region = 'Americas' THEN 'AMER'\n  WHEN countries.region IN ('Europe', 'Africa') THEN 'EMEA'\n  WHEN countries.region = 'Asia' THEN 'APAC'\n  ELSE NULL\nENDAS macro_region,\n    -- T`
  - 1-revenue.sql:32:4-37:8 - Variation 4: cluster
    ``


##### 1. 2 variations found (82% similar)
- **Source**: sql-refinery
- **Severity**: Information
- **Code**: 2
- **Range**: 12:4-12:60
- **Snippet**: `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT`
- **Related Information** (2):
  - editor.sql:12:4-12:60 - Variation 1: industry_it
    `IIF(a.industry = 'Information Technology', 'IT', 'Non-IT`
  - 1-revenue.sql:38:4-38:60 - Variation 2: industry_tech
    ``


#### Code Lenses (4):

0. **→ Show 4 alternatives**
   - **Range**: 5:0-5:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showVariantsEditor`
   - **Arguments**: [{"groupId":"1","currentRange":[{"line":5,"character":4},{"line":10,"character":8}]}]

1. **× Ignore**
   - **Range**: 5:0-5:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.ignoreVariant`
   - **Arguments**: [{"groupId":"1","diagnosticRange":[{"line":5,"character":4},{"line":10,"character":8}]}]

2. **→ Show 2 alternatives**
   - **Range**: 12:0-12:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showVariantsEditor`
   - **Arguments**: [{"groupId":"2","currentRange":[{"line":12,"character":4},{"line":12,"character":60}]}]

3. **× Ignore**
   - **Range**: 12:0-12:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.ignoreVariant`
   - **Arguments**: [{"groupId":"2","diagnosticRange":[{"line":12,"character":4},{"line":12,"character":60}]}]




## Step: 5. Showed alternatives for second inconsistency (IIF statement)
### Open Editors (2):
0. editor.sql (column 1)
1. sql-refinery-inconsistencies:editor.sql%3Ainconsistency-2 (column 2) (active)

### Active Editor: sql-refinery-inconsistencies:editor.sql%3Ainconsistency-2
```sql
-- SQL-Refinery
-- Inconsistent query: alternative variants found in the codebase

-- Alternative 1
IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')


-- Alternative 2
IF(accounts.industry = 'Information Technology', 'Tech', 'Other')


```

#### Diagnostics (0):

#### Code Lenses (6):

0. **→ Peek 1 locations**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.peekLocations`
   - **Arguments**: [{"locations":[{"file":"Current file","line":13,"alias":"industry_it","sql":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","occurrences":1,"range":[{"line":12,"character":4},{"line":12,"character":60}]}],"groupId":"2","position":{"line":4,"character":0}}]

1. **↔ Show diff**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showNativeDiff`
   - **Arguments**: [{"variant":{"sql":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","locations":[{"file":"Current file","line":13,"alias":"industry_it","sql":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","occurrences":1,"range":[{"line":12,"character":4},{"line":12,"character":60}]}],"variantIndex":1},"originalSQL":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","groupId":"2","variantIndex":1}]

2. **✓ Apply**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.applyVariant`
   - **Arguments**: [{"variant":{"sql":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","locations":[{"file":"Current file","line":13,"alias":"industry_it","sql":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","occurrences":1,"range":[{"line":12,"character":4},{"line":12,"character":60}]}],"variantIndex":1},"groupId":"2"}]

3. **→ Peek 1 locations**
   - **Range**: 7:0-7:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.peekLocations`
   - **Arguments**: [{"locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":39,"alias":"industry_tech","sql":"IF(accounts.industry = 'Information Technology', 'Tech', 'Other')","occurrences":1,"range":[{"line":38,"character":4},{"line":38,"character":60}]}],"groupId":"2","position":{"line":8,"character":0}}]

4. **↔ Show diff**
   - **Range**: 7:0-7:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showNativeDiff`
   - **Arguments**: [{"variant":{"sql":"IF(accounts.industry = 'Information Technology', 'Tech', 'Other')","locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":39,"alias":"industry_tech","sql":"IF(accounts.industry = 'Information Technology', 'Tech', 'Other')","occurrences":1,"range":[{"line":38,"character":4},{"line":38,"character":60}]}],"variantIndex":2},"originalSQL":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","groupId":"2","variantIndex":2}]

5. **✓ Apply**
   - **Range**: 7:0-7:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.applyVariant`
   - **Arguments**: [{"variant":{"sql":"IF(accounts.industry = 'Information Technology', 'Tech', 'Other')","locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":39,"alias":"industry_tech","sql":"IF(accounts.industry = 'Information Technology', 'Tech', 'Other')","occurrences":1,"range":[{"line":38,"character":4},{"line":38,"character":60}]}],"variantIndex":2},"groupId":"2"}]




## Step: 6. Final state - workflow completed
### Open Editors (2):
0. editor.sql (column 1)
1. sql-refinery-inconsistencies:editor.sql%3Ainconsistency-2 (column 2) (active)

### Active Editor: sql-refinery-inconsistencies:editor.sql%3Ainconsistency-2
```sql
-- SQL-Refinery
-- Inconsistent query: alternative variants found in the codebase

-- Alternative 1
IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')


-- Alternative 2
IF(accounts.industry = 'Information Technology', 'Tech', 'Other')


```

#### Diagnostics (0):

#### Code Lenses (6):

0. **→ Peek 1 locations**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.peekLocations`
   - **Arguments**: [{"locations":[{"file":"Current file","line":13,"alias":"industry_it","sql":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","occurrences":1,"range":[{"line":12,"character":4},{"line":12,"character":60}]}],"groupId":"2","position":{"line":4,"character":0}}]

1. **↔ Show diff**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showNativeDiff`
   - **Arguments**: [{"variant":{"sql":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","locations":[{"file":"Current file","line":13,"alias":"industry_it","sql":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","occurrences":1,"range":[{"line":12,"character":4},{"line":12,"character":60}]}],"variantIndex":1},"originalSQL":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","groupId":"2","variantIndex":1}]

2. **✓ Apply**
   - **Range**: 3:0-3:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.applyVariant`
   - **Arguments**: [{"variant":{"sql":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","locations":[{"file":"Current file","line":13,"alias":"industry_it","sql":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","occurrences":1,"range":[{"line":12,"character":4},{"line":12,"character":60}]}],"variantIndex":1},"groupId":"2"}]

3. **→ Peek 1 locations**
   - **Range**: 7:0-7:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.peekLocations`
   - **Arguments**: [{"locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":39,"alias":"industry_tech","sql":"IF(accounts.industry = 'Information Technology', 'Tech', 'Other')","occurrences":1,"range":[{"line":38,"character":4},{"line":38,"character":60}]}],"groupId":"2","position":{"line":8,"character":0}}]

4. **↔ Show diff**
   - **Range**: 7:0-7:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.showNativeDiff`
   - **Arguments**: [{"variant":{"sql":"IF(accounts.industry = 'Information Technology', 'Tech', 'Other')","locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":39,"alias":"industry_tech","sql":"IF(accounts.industry = 'Information Technology', 'Tech', 'Other')","occurrences":1,"range":[{"line":38,"character":4},{"line":38,"character":60}]}],"variantIndex":2},"originalSQL":"IF(accounts.industry = 'Information Technology', 'IT', 'Non-IT')","groupId":"2","variantIndex":2}]

5. **✓ Apply**
   - **Range**: 7:0-7:0
   - **Snippet**: ``
   - **Command**: `sql-refinery.applyVariant`
   - **Arguments**: [{"variant":{"sql":"IF(accounts.industry = 'Information Technology', 'Tech', 'Other')","locations":[{"file":"/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql","line":39,"alias":"industry_tech","sql":"IF(accounts.industry = 'Information Technology', 'Tech', 'Other')","occurrences":1,"range":[{"line":38,"character":4},{"line":38,"character":60}]}],"variantIndex":2},"groupId":"2"}]



