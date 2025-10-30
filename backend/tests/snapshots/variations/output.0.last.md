# 0-accounts.sql

## Expression at 0-accounts.sql:37:8-37:105: 1 variations

`SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)`

Variation 1: similarity 0.89, frequency 1 (0-accounts.sql:38:8-38:86)
`SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)`

## Expression at 0-accounts.sql:38:8-38:86: 1 variations

`SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)`

Variation 1: similarity 0.89, frequency 1 (0-accounts.sql:37:8-37:105)
`SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)`
