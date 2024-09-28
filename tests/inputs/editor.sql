-- CASE: Different groupings or thresholds applied to columns

SELECT 
    date(date_month, 'start of year') AS date_year,
    CASE -- Logical error #1
        WHEN c.region IN ('Americas') THEN 'AMER'
        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'
        WHEN c.region = 'Asia' THEN 'APAC'
        ELSE NULL
    END AS macro_region,
    IIF(a.industry = 'Information Technology','IT', 'Non-IT') -- Logical error #2
    AS industry_it,
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