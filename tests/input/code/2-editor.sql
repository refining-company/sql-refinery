--Test: 1

SELECT 
    date(date_month, 'start of year') AS date_year,
    CASE
        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'
        WHEN c.region IN ('Asia') THEN 'Asia'
        WHEN c.region IN ('Africa') THEN 'South-East'
        ELSE NULL
    END AS region_cluster,
    CASE 
        WHEN a.industry in ('Information Technology', 'Telco') THEN 'Tech'
        WHEN a.industry IS NULL THEN NULL
        ELSE 'Other'
    END AS industry_cluster,
FROM accounts_revenue ar
    LEFT JOIN accounts a USING (account_id)