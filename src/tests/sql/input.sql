================================================================================
ANALYTIC FUNCTIOIN:
================================================================================

SELECT book, LAST_VALUE(item) OVER (ORDER BY year) FROM Library;
SELECT ROW_NUMBER() OVER (PARTITION BY author ORDER BY ts) as seq FROM Library;
SELECT book, LAST_VALUE(item)
  OVER (
    ORDER BY year
    RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
FROM Library;

--------------------------------------------------------------------------------

================================================================================
ANALYTIC FUNCTIOIN: With WINDOW clause
================================================================================

SELECT item, purchases, category, LAST_VALUE(item)
  OVER (
      item_window
      ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
      ) AS most_popular
  FROM Produce
  WINDOW item_window AS (
      PARTITION BY category1, category2
      ORDER BY purchases)

--------------------------------------------------------------------------------
