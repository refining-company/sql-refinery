# {cwd}/tests/inputs/codebase/0-accounts.sql

## Expression at {cwd}/tests/inputs/codebase/0-accounts.sql:37:8-37:105: 1 variations

`SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)`

Variation 1: similarity 0.89, frequency 1 ({cwd}/tests/inputs/codebase/0-accounts.sql:38:8-38:86)
`SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)`

## Expression at {cwd}/tests/inputs/codebase/0-accounts.sql:38:8-38:86: 1 variations

`SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)`

Variation 1: similarity 0.89, frequency 1 ({cwd}/tests/inputs/codebase/0-accounts.sql:37:8-37:105)
`SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)`

## Expression at {cwd}/tests/inputs/codebase/0-accounts.sql:97:8-101:11: 1 variations

`CASE WHEN c.region IN ('Americas', 'Europe') THEN 'North-West' WHEN c.region IN ('Africa', 'Asia') THEN 'South-East' ELSE NULL END`

Variation 1: similarity 0.76, frequency 1 ({cwd}/tests/inputs/editor.sql:5:4-10:7)
`CASE WHEN c.region IN ('Americas') THEN 'AMER' WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA' WHEN c.region = 'Asia' THEN 'APAC' ELSE NULL END`

# {cwd}/tests/inputs/codebase/1-revenue.sql

## Expression at {cwd}/tests/inputs/codebase/1-revenue.sql:6:4-10:7: 1 variations

`CASE WHEN c.region IN ('Americas', 'Europe') THEN 'North-West' WHEN c.region IN ('Africa', 'Asia') THEN 'South-East' ELSE NULL END`

Variation 1: similarity 0.76, frequency 1 ({cwd}/tests/inputs/editor.sql:5:4-10:7)
`CASE WHEN c.region IN ('Americas') THEN 'AMER' WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA' WHEN c.region = 'Asia' THEN 'APAC' ELSE NULL END`

## Expression at {cwd}/tests/inputs/codebase/1-revenue.sql:32:4-36:7: 1 variations

`CASE WHEN c.region IN ('Americas', 'Europe') THEN 'North-West' WHEN c.region IN ('Africa', 'Asia') THEN 'South-East' ELSE NULL END`

Variation 1: similarity 0.76, frequency 1 ({cwd}/tests/inputs/editor.sql:5:4-10:7)
`CASE WHEN c.region IN ('Americas') THEN 'AMER' WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA' WHEN c.region = 'Asia' THEN 'APAC' ELSE NULL END`

## Expression at {cwd}/tests/inputs/codebase/1-revenue.sql:38:4-38:70: 1 variations

`IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')`

Variation 1: similarity 0.94, frequency 1 ({cwd}/tests/inputs/editor.sql:12:4-12:62)
`IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`

# {cwd}/tests/inputs/editor.sql

## Expression at {cwd}/tests/inputs/editor.sql:5:4-10:7: 1 variations

`CASE WHEN c.region IN ('Americas') THEN 'AMER' WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA' WHEN c.region = 'Asia' THEN 'APAC' ELSE NULL END`

Variation 1: similarity 0.76, frequency 3 ({cwd}/tests/inputs/codebase/0-accounts.sql:97:8-101:11, {cwd}/tests/inputs/codebase/1-revenue.sql:32:4-36:7, {cwd}/tests/inputs/codebase/1-revenue.sql:6:4-10:7)
`CASE WHEN c.region IN ('Americas', 'Europe') THEN 'North-West' WHEN c.region IN ('Africa', 'Asia') THEN 'South-East' ELSE NULL END`

## Expression at {cwd}/tests/inputs/editor.sql:12:4-12:62: 1 variations

`IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')`

Variation 1: similarity 0.94, frequency 1 ({cwd}/tests/inputs/codebase/1-revenue.sql:38:4-38:70)
`IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')`
