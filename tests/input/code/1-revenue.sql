
DROP TABLE IF EXISTS revenue;
CREATE TABLE revenue AS
SELECT 
    date(date_month, 'start of year') AS date_year,
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
    SUM(a360.revenue_12m) / COUNT(DISTINCT ar.account_id) AS revenue_12m_p_account
FROM accounts_revenue ar
    LEFT JOIN accounts a USING (account_id)
    LEFT JOIN countries c USING (country)
    LEFT JOIN accounts_360 a360 USING (account_id, date_month)
GROUP BY date_year, region_cluster, industry_cluster, a360.account_size
ORDER BY date_year, region_cluster, industry_cluster;

SELECT * FROM revenue;