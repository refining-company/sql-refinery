-- REVENUE REPORTS

-- Revenue by region, cluster, account size
-- REVENUE REPORTS

-- Revenue by region, cluster, account size

SELECT 
    date(date_month, 'start of year') AS date_year,
    -- Error 1: alternative
    CASE
        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'
        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'
        ELSE NULL
    END AS region_cluster,
    CASE 
        WHEN a.industry = 'Information Technology' THEN 'Tech'
        WHEN a.industry IS NULL THEN NULL
        ELSE 'Other'
    END AS industry_cluster,
    a360.account_size,
    SUM(ar.revenue) AS revenue,
    COUNT(DISTINCT ar.account_id) AS accounts,
    SUM(ar.revenue) / COUNT(DISTINCT ar.account_id) AS revenue_per_account
FROM accounts_revenue ar
    LEFT JOIN accounts a USING (account_id)
    LEFT JOIN countries c USING (country)
    LEFT JOIN accounts_360 a360 USING (account_id, date_month)
GROUP BY date_year, region_cluster, industry_cluster, a360.account_size
ORDER BY date_year, region_cluster, industry_cluster;

-- Accounts snapshot performance

SELECT
    accounts.name,
    region,
    -- Error 1: alternative
    CASE
        WHEN countries.region IN ('Americas', 'Europe') THEN 'North-West'
        WHEN countries.region IN ('Americas', 'Oceania') THEN 'North-East'
        WHEN countries.region IN ('Americas', 'Tanzia') THEN 'East'
        WHEN countries.region IN ('Africa', 'Asia') THEN 'South-East'
        ELSE NULL
    END AS cluster,
    accounts.industry AS industry,
    IIF(accounts.industry = 'Information Technology', 'Tech', 'Other') AS industry_tech,
    CASE 
        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'
        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'
        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'
        ELSE NULL
    END AS account_size,
    SUM(accounts_revenue.revenue) AS revenue_12m
FROM accounts
    LEFT JOIN accounts_revenue USING (account_id)
    LEFT JOIN countries c USING (country)
WHERE accounts_revenue.date_month BETWEEN DATE('now', '-12 months') AND DATE('now')
GROUP BY accounts.name, region, accounts.industry;