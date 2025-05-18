# Testing Server
## STEP 0: Initialise
Initialize with workspace folders: `codebase`


## STEP 1: Open document
Document opened: `editor.sql`
Found 2 diagnostics:
- `editor.sql:5:4-10:7` Alternative expressions found in the codebase 
  ```sql
    CASE
        WHEN c.region IN ('Americas') THEN 'AMER'
        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'
        WHEN c.region = 'Asia' THEN 'APAC'
        ELSE NULL
    END AS macro_region,
  ```

- `editor.sql:12:4-12:62` Alternative expressions found in the codebase 
  ```sql
    IIF(a.industry = 'Information Technology', 'IT', 'Non-IT') AS industry_it,
  ```



## STEP 2: Get code lenses
Code lens requested for: `editor.sql`
Found 2 code lenses:
- `editor.sql:5:4-10:7` Alternatives found: 3
  ```sql
    CASE
        WHEN c.region IN ('Americas') THEN 'AMER'
        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'
        WHEN c.region = 'Asia' THEN 'APAC'
        ELSE NULL
    END AS macro_region,
  ```

  - `0-accounts.sql:97:8`
    ```sql
        CASE
            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'
            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'
            ELSE NULL
        END AS region_cluster,
        accounts.priority,
    ```

  - `1-revenue.sql:6:4`
    ```sql
    CASE
        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'
        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'
        ELSE NULL
    END AS region_cluster,
    CASE 
    ```

  - `1-revenue.sql:32:4`
    ```sql
    CASE
        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'
        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'
        ELSE NULL
    END AS cluster,
    accounts.industry AS industry,
    ```

- `editor.sql:12:4-12:62` Alternatives found: 1
  ```sql
    IIF(a.industry = 'Information Technology', 'IT', 'Non-IT') AS industry_it,
  ```

  - `1-revenue.sql:38:4`
    ```sql
    IIF(accounts.industry = 'Information Technology', 'Tech', 'Other') AS industry_tech,
    ```



## STEP 3: Get final document
`editor.sql`
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

