-- FOUNDATIONAL TABLES

-- Calendar scaffolding: one day per row

DROP TABLE IF EXISTS date_ranges;
CREATE TABLE date_ranges AS
WITH RECURSIVE date_ranges(date_day) AS (
    SELECT 
        date(MIN(CASE WHEN d.stage_date < d.contract_start_date THEN d.stage_date ELSE d.contract_start_date END)) AS date_month
    FROM deals d
    UNION ALL
    SELECT 
        date(date_day, '+1 day')
    FROM date_ranges
    WHERE date_day < (SELECT date(MAX(CASE WHEN d.contract_end_date > d.stage_date THEN d.contract_end_date ELSE d.stage_date END)) FROM deals d)
)
SELECT 
    date_day
FROM date_ranges
GROUP BY date_day;

-- Currently active signed deals (stage=4) and daily revenue

DROP TABLE IF EXISTS deals_signed;
CREATE TABLE deals_signed AS
SELECT 
    *,
    revenue / contract_duration_days AS revenue_day,
    revenue_core / contract_duration_days AS revenue_core_day,
    revenue_aux / contract_duration_days AS revenue_aux_day
FROM (
    SELECT 
        d.deal_id,
        d.account_id,
        d.contract_start_date,
        d.contract_end_date,
        julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1 AS contract_duration_days,
        SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END) AS revenue_core,
        SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END) AS revenue_aux,
        SUM(o.value) AS revenue
    FROM orders o
        JOIN deals d USING (deal_id, order_id)
    WHERE d.stage = 4
    GROUP BY d.deal_id, d.account_id, d.contract_start_date, d.contract_end_date
) AS t;

-- Revenue per account per month

DROP TABLE IF EXISTS accounts_revenue;
CREATE TABLE accounts_revenue AS
SELECT 
    t.date_month,
    t.account_id,
    AVG(t.deals) AS deals,
    SUM(t.revenue_core) AS revenue_core,
    SUM(t.revenue_aux) AS revenue_aux,
    SUM(t.revenue) AS revenue
FROM (
    SELECT 
        dr.date_day,
        DATE(date_day, 'start of month') AS date_month,
        ds.account_id,
        COUNT(ds.deal_id) AS deals,
        SUM(ds.revenue_core_day) AS revenue_core,
        SUM(ds.revenue_aux_day) AS revenue_aux,
        SUM(ds.revenue_day) AS revenue
    FROM date_ranges dr
        LEFT JOIN deals_signed ds 
            ON  dr.date_day >= date(ds.contract_start_date)
            AND dr.date_day <= date(ds.contract_end_date)
    GROUP BY dr.date_day, ds.account_id) t
GROUP BY account_id, date_month;


-- Key information by account as of now

DROP TABLE IF EXISTS accounts_360;
CREATE TABLE accounts_360 AS
SELECT 
    t.*,
    CASE 
        WHEN t.revenue_12m <= 300 THEN 'Small'
        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'
        WHEN t.revenue_12m > 600 THEN 'Large'
        ELSE NULL
    END AS account_size
FROM (
    SELECT 
        account_id,
        date_month,
        revenue,
        revenue_core,
        revenue_aux,
        deals,
        accounts.name,
        accounts.industry,
        accounts.country,
        -- Error 1: alternative
        CASE
            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'
            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'
            ELSE NULL
        END AS region_cluster,
        accounts.priority,
        SUM(revenue) OVER (
            PARTITION BY account_id 
            ORDER BY date_month 
            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW
        ) AS revenue_12m
    FROM accounts_revenue
        JOIN accounts USING (account_id)
        LEFT JOIN countries c USING (country)
) AS t;