# Testing Pipeline

# STEP: src.sql.parse 1

```json
[
  { "@root (source_file at 1:1) = -- FOUNDATIONAL TABL": [
      { "@scope (query_expr at 7:1) = WITH RECURSIVE date_": [
          { "@scope (query_expr at 8:5) = SELECT date(MIN(CASE": [
              { "@query (query_expr at 8:5) = SELECT date(MIN(CASE": [
                  { "@columns (select_list at 9:9) = date(MIN(CASE WHEN d": [
                      { "@expression (function_call at 9:9) = date(MIN(CASE WHEN d": [
                          { "@column (identifier at 9:28) = d.stage_date": [] },
                          { "@column (identifier at 9:43) = d.contract_start_dat": [] },
                          { "@column (identifier at 9:70) = d.stage_date": [] },
                          { "@column (identifier at 9:88) = d.contract_start_dat": [] } ] },
                      { "@alias (identifier at 9:119) = date_month": [] } ] },
                  { "@sources (from_clause at 10:5) = FROM deals d": [
                      { "@table (identifier at 10:10) = deals": [] },
                      { "@alias (identifier at 10:16) = d": [] } ] } ] },
              { "@query (query_expr at 12:5) = SELECT date(date_day": [
                  { "@columns (select_list at 13:9) = date(date_day, '+1 d": [
                      { "@expression (function_call at 13:9) = date(date_day, '+1 d": [
                          { "@column (identifier at 13:14) = date_day": [] } ] } ] },
                  { "@sources (from_clause at 14:5) = FROM date_ranges": [
                      { "@table (identifier at 14:10) = date_ranges": [] } ] },
                  { "@filter (where_clause at 15:5) = WHERE date_day < (SE": [
                      { "@column (identifier at 15:11) = date_day": [] },
                      { "@query (query_expr at 15:23) = SELECT date(MAX(CASE": [
                          { "@columns (select_list at 15:30) = date(MAX(CASE WHEN d": [
                              { "@expression (function_call at 15:30) = date(MAX(CASE WHEN d": [
                                  { "@column (identifier at 15:49) = d.contract_end_date": [] },
                                  { "@column (identifier at 15:71) = d.stage_date": [] },
                                  { "@column (identifier at 15:89) = d.contract_end_date": [] },
                                  { "@column (identifier at 15:114) = d.stage_date": [] } ] } ] },
                          { "@sources (from_clause at 15:133) = FROM deals d": [
                              { "@table (identifier at 15:138) = deals": [] },
                              { "@alias (identifier at 15:144) = d": [] } ] } ] } ] } ] } ] },
          { "@columns (select_list at 18:5) = date_day": [
              { "@column (identifier at 18:5) = date_day": [] } ] },
          { "@sources (from_clause at 19:1) = FROM date_ranges": [
              { "@table (identifier at 19:6) = date_ranges": [] } ] },
          { "@grouping (group_by_clause at 20:1) = GROUP BY date_day": [
              { "@column (identifier at 20:10) = date_day": [] } ] } ] },
      { "@query (query_expr at 26:1) = SELECT *, revenue / ": [
          { "@columns (select_list at 27:5) = *, revenue / contrac": [
              { "@column (select_all at 27:5) = *": [] },
              { "@expression (binary_expression at 28:5) = revenue / contract_d": [
                  { "@column (identifier at 28:5) = revenue": [] },
                  { "@column (identifier at 28:15) = contract_duration_da": [] } ] },
              { "@alias (identifier at 28:41) = revenue_day": [] },
              { "@expression (binary_expression at 29:5) = revenue_core / contr": [
                  { "@column (identifier at 29:5) = revenue_core": [] },
                  { "@column (identifier at 29:20) = contract_duration_da": [] } ] },
              { "@alias (identifier at 29:46) = revenue_core_day": [] },
              { "@expression (binary_expression at 30:5) = revenue_aux / contra": [
                  { "@column (identifier at 30:5) = revenue_aux": [] },
                  { "@column (identifier at 30:19) = contract_duration_da": [] } ] },
              { "@alias (identifier at 30:45) = revenue_aux_day": [] } ] },
          { "@sources (from_clause at 31:1) = FROM ( SELECT d.deal": [
              { "@query (query_expr at 32:5) = SELECT d.deal_id, d.": [
                  { "@columns (select_list at 33:9) = d.deal_id, d.account": [
                      { "@column (identifier at 33:9) = d.deal_id": [] },
                      { "@column (identifier at 34:9) = d.account_id": [] },
                      { "@column (identifier at 35:9) = d.contract_start_dat": [] },
                      { "@column (identifier at 36:9) = d.contract_end_date": [] },
                      { "@expression (binary_expression at 37:9) = julianday(d.contract": [
                          { "@column (identifier at 37:19) = d.contract_end_date": [] },
                          { "@column (identifier at 37:52) = d.contract_start_dat": [] } ] },
                      { "@alias (identifier at 37:82) = contract_duration_da": [] },
                      { "@expression (function_call at 38:9) = SUM(CASE WHEN o.prod": [
                          { "@column (identifier at 38:23) = o.product": [] },
                          { "@column (identifier at 38:87) = o.value": [] } ] },
                      { "@alias (identifier at 38:110) = revenue_core": [] },
                      { "@expression (function_call at 39:9) = SUM(CASE WHEN o.prod": [
                          { "@column (identifier at 39:23) = o.product": [] },
                          { "@column (identifier at 39:68) = o.value": [] } ] },
                      { "@alias (identifier at 39:91) = revenue_aux": [] },
                      { "@expression (function_call at 40:9) = SUM(o.value)": [
                          { "@column (identifier at 40:13) = o.value": [] } ] },
                      { "@alias (identifier at 40:25) = revenue": [] } ] },
                  { "@sources (from_clause at 41:5) = FROM orders o JOIN d": [
                      { "@table (identifier at 41:10) = orders": [] },
                      { "@alias (identifier at 41:17) = o": [] },
                      { "@table (identifier at 42:14) = deals": [] },
                      { "@alias (identifier at 42:20) = d": [] },
                      { "@join (join_condition at 42:22) = USING (deal_id, orde": [
                          { "@column (identifier at 42:29) = deal_id": [] },
                          { "@column (identifier at 42:38) = order_id": [] } ] } ] },
                  { "@filter (where_clause at 43:5) = WHERE d.stage = 4": [
                      { "@column (identifier at 43:11) = d.stage": [] } ] },
                  { "@grouping (group_by_clause at 44:5) = GROUP BY d.deal_id, ": [
                      { "@column (identifier at 44:14) = d.deal_id": [] },
                      { "@column (identifier at 44:25) = d.account_id": [] },
                      { "@column (identifier at 44:39) = d.contract_start_dat": [] },
                      { "@column (identifier at 44:62) = d.contract_end_date": [] } ] } ] },
              { "@alias (identifier at 45:6) = t": [] } ] } ] },
      { "@query (query_expr at 51:1) = SELECT t.date_month,": [
          { "@columns (select_list at 52:5) = t.date_month, t.acco": [
              { "@column (identifier at 52:5) = t.date_month": [] },
              { "@column (identifier at 53:5) = t.account_id": [] },
              { "@expression (function_call at 54:5) = AVG(t.deals)": [
                  { "@column (identifier at 54:9) = t.deals": [] } ] },
              { "@alias (identifier at 54:21) = deals": [] },
              { "@expression (function_call at 55:5) = SUM(t.revenue_core)": [
                  { "@column (identifier at 55:9) = t.revenue_core": [] } ] },
              { "@alias (identifier at 55:28) = revenue_core": [] },
              { "@expression (function_call at 56:5) = SUM(t.revenue_aux)": [
                  { "@column (identifier at 56:9) = t.revenue_aux": [] } ] },
              { "@alias (identifier at 56:27) = revenue_aux": [] },
              { "@expression (function_call at 57:5) = SUM(t.revenue)": [
                  { "@column (identifier at 57:9) = t.revenue": [] } ] },
              { "@alias (identifier at 57:23) = revenue": [] } ] },
          { "@sources (from_clause at 58:1) = FROM ( SELECT dr.dat": [
              { "@query (query_expr at 59:5) = SELECT dr.date_day, ": [
                  { "@columns (select_list at 60:9) = dr.date_day, DATE(da": [
                      { "@column (identifier at 60:9) = dr.date_day": [] },
                      { "@expression (function_call at 61:9) = DATE(date_day, 'star": [
                          { "@column (identifier at 61:14) = date_day": [] } ] },
                      { "@alias (identifier at 61:45) = date_month": [] },
                      { "@column (identifier at 62:9) = ds.account_id": [] },
                      { "@expression (function_call at 63:9) = COUNT(ds.deal_id)": [
                          { "@column (identifier at 63:15) = ds.deal_id": [] } ] },
                      { "@alias (identifier at 63:30) = deals": [] },
                      { "@expression (function_call at 64:9) = SUM(ds.revenue_core_": [
                          { "@column (identifier at 64:13) = ds.revenue_core_day": [] } ] },
                      { "@alias (identifier at 64:37) = revenue_core": [] },
                      { "@expression (function_call at 65:9) = SUM(ds.revenue_aux_d": [
                          { "@column (identifier at 65:13) = ds.revenue_aux_day": [] } ] },
                      { "@alias (identifier at 65:36) = revenue_aux": [] },
                      { "@expression (function_call at 66:9) = SUM(ds.revenue_day)": [
                          { "@column (identifier at 66:13) = ds.revenue_day": [] } ] },
                      { "@alias (identifier at 66:32) = revenue": [] } ] },
                  { "@sources (from_clause at 67:5) = FROM date_ranges dr ": [
                      { "@table (identifier at 67:10) = date_ranges": [] },
                      { "@alias (identifier at 67:22) = dr": [] },
                      { "@table (identifier at 68:19) = deals_signed": [] },
                      { "@alias (identifier at 68:32) = ds": [] },
                      { "@join (join_condition at 69:13) = ON dr.date_day >= da": [
                          { "@expression (binary_expression at 69:17) = dr.date_day >= date(": [
                              { "@column (identifier at 69:17) = dr.date_day": [] },
                              { "@column (identifier at 69:37) = ds.contract_start_da": [] },
                              { "@column (identifier at 70:17) = dr.date_day": [] },
                              { "@column (identifier at 70:37) = ds.contract_end_date": [] } ] } ] } ] },
                  { "@grouping (group_by_clause at 71:5) = GROUP BY dr.date_day": [
                      { "@column (identifier at 71:14) = dr.date_day": [] },
                      { "@column (identifier at 71:27) = ds.account_id": [] } ] } ] },
              { "@alias (identifier at 71:42) = t": [] } ] },
          { "@grouping (group_by_clause at 72:1) = GROUP BY account_id,": [
              { "@column (identifier at 72:10) = account_id": [] },
              { "@column (identifier at 72:22) = date_month": [] } ] } ] },
      { "@query (query_expr at 79:1) = SELECT t.*, CASE WHE": [
          { "@columns (select_list at 80:5) = t.*, CASE WHEN t.rev": [
              { "@column (select_all at 80:5) = t.*": [] },
              { "@expression (casewhen_expression at 81:5) = CASE WHEN t.revenue_": [
                  { "@column (identifier at 82:14) = t.revenue_12m": [] },
                  { "@column (identifier at 83:14) = t.revenue_12m": [] },
                  { "@column (identifier at 83:38) = t.revenue_12m": [] },
                  { "@column (identifier at 84:14) = t.revenue_12m": [] } ] },
              { "@alias (identifier at 86:12) = account_size": [] } ] },
          { "@sources (from_clause at 87:1) = FROM ( SELECT accoun": [
              { "@query (query_expr at 88:5) = SELECT account_id, d": [
                  { "@columns (select_list at 89:9) = account_id, date_mon": [
                      { "@column (identifier at 89:9) = account_id": [] },
                      { "@column (identifier at 90:9) = date_month": [] },
                      { "@column (identifier at 91:9) = revenue": [] },
                      { "@column (identifier at 92:9) = revenue_core": [] },
                      { "@column (identifier at 93:9) = revenue_aux": [] },
                      { "@column (identifier at 94:9) = deals": [] },
                      { "@column (identifier at 95:9) = accounts.name": [] },
                      { "@column (identifier at 96:9) = accounts.industry": [] },
                      { "@column (identifier at 97:9) = accounts.country": [] },
                      { "@expression (casewhen_expression at 98:9) = CASE WHEN c.region I": [
                          { "@column (identifier at 99:18) = c.region": [] },
                          { "@column (identifier at 100:18) = c.region": [] } ] },
                      { "@alias (identifier at 102:16) = region_cluster": [] },
                      { "@column (identifier at 103:9) = accounts.priority": [] },
                      { "@expression (function_call at 104:9) = SUM(revenue) OVER ( ": [
                          { "@column (identifier at 104:13) = revenue": [] },
                          { "@column (identifier at 105:26) = account_id": [] },
                          { "@ordering (order_by_clause at 106:13) = ORDER BY date_month": [
                              { "@column (identifier at 106:22) = date_month": [] } ] } ] },
                      { "@alias (identifier at 108:14) = revenue_12m": [] } ] },
                  { "@sources (from_clause at 109:5) = FROM accounts_revenu": [
                      { "@table (identifier at 109:10) = accounts_revenue": [] },
                      { "@table (identifier at 110:14) = accounts": [] },
                      { "@join (join_condition at 110:23) = USING (account_id)": [
                          { "@column (identifier at 110:30) = account_id": [] } ] },
                      { "@table (identifier at 111:19) = countries": [] },
                      { "@alias (identifier at 111:29) = c": [] },
                      { "@join (join_condition at 111:31) = USING (country)": [
                          { "@column (identifier at 111:38) = country": [] } ] } ] } ] },
              { "@alias (identifier at 112:6) = t": [] } ] } ] } ] } ]
```

# STEP: src.sql.parse 2

```json
[
  { "@root (source_file at 1:1) = -- REVENUE REPORTS -": [
      { "@query (query_expr at 5:1) = SELECT date(date_mon": [
          { "@columns (select_list at 6:5) = date(date_month, 'st": [
              { "@expression (function_call at 6:5) = date(date_month, 'st": [
                  { "@column (identifier at 6:10) = date_month": [] } ] },
              { "@alias (identifier at 6:42) = date_year": [] },
              { "@expression (casewhen_expression at 7:5) = CASE WHEN c.region I": [
                  { "@column (identifier at 8:14) = c.region": [] },
                  { "@column (identifier at 9:14) = c.region": [] } ] },
              { "@alias (identifier at 11:12) = region_cluster": [] },
              { "@expression (casewhen_expression at 12:5) = CASE WHEN a.industry": [
                  { "@column (identifier at 13:14) = a.industry": [] },
                  { "@column (identifier at 14:14) = a.industry": [] } ] },
              { "@alias (identifier at 16:12) = industry_cluster": [] },
              { "@column (identifier at 17:5) = a360.account_size": [] },
              { "@expression (function_call at 18:5) = SUM(ar.revenue)": [
                  { "@column (identifier at 18:9) = ar.revenue": [] } ] },
              { "@alias (identifier at 18:24) = revenue": [] },
              { "@expression (function_call at 19:5) = COUNT(DISTINCT ar.ac": [
                  { "@column (identifier at 19:20) = ar.account_id": [] } ] },
              { "@alias (identifier at 19:38) = accounts": [] },
              { "@expression (binary_expression at 20:5) = SUM(ar.revenue) / CO": [
                  { "@column (identifier at 20:9) = ar.revenue": [] },
                  { "@column (identifier at 20:38) = ar.account_id": [] } ] },
              { "@alias (identifier at 20:56) = revenue_per_account": [] } ] },
          { "@sources (from_clause at 21:1) = FROM accounts_revenu": [
              { "@table (identifier at 21:6) = accounts_revenue": [] },
              { "@alias (identifier at 21:23) = ar": [] },
              { "@table (identifier at 22:15) = accounts": [] },
              { "@alias (identifier at 22:24) = a": [] },
              { "@join (join_condition at 22:26) = USING (account_id)": [
                  { "@column (identifier at 22:33) = account_id": [] } ] },
              { "@table (identifier at 23:15) = countries": [] },
              { "@alias (identifier at 23:25) = c": [] },
              { "@join (join_condition at 23:27) = USING (country)": [
                  { "@column (identifier at 23:34) = country": [] } ] },
              { "@table (identifier at 24:15) = accounts_360": [] },
              { "@alias (identifier at 24:28) = a360": [] },
              { "@join (join_condition at 24:33) = USING (account_id, d": [
                  { "@column (identifier at 24:40) = account_id": [] },
                  { "@column (identifier at 24:52) = date_month": [] } ] } ] },
          { "@grouping (group_by_clause at 25:1) = GROUP BY date_year, ": [
              { "@column (identifier at 25:10) = date_year": [] },
              { "@column (identifier at 25:21) = region_cluster": [] },
              { "@column (identifier at 25:37) = industry_cluster": [] },
              { "@column (identifier at 25:55) = a360.account_size": [] } ] },
          { "@ordering (order_by_clause at 26:1) = ORDER BY date_year, ": [
              { "@column (identifier at 26:10) = date_year": [] },
              { "@column (identifier at 26:21) = region_cluster": [] },
              { "@column (identifier at 26:37) = industry_cluster": [] } ] } ] },
      { "@query (query_expr at 30:1) = SELECT accounts.name": [
          { "@columns (select_list at 31:5) = accounts.name, regio": [
              { "@column (identifier at 31:5) = accounts.name": [] },
              { "@column (identifier at 32:5) = region": [] },
              { "@expression (casewhen_expression at 33:5) = CASE WHEN c.region I": [
                  { "@column (identifier at 34:14) = c.region": [] },
                  { "@column (identifier at 35:14) = c.region": [] } ] },
              { "@alias (identifier at 37:12) = cluster": [] },
              { "@column (identifier at 38:5) = accounts.industry": [] },
              { "@alias (identifier at 38:26) = industry": [] },
              { "@expression (function_call at 39:5) = IIF(accounts.industr": [
                  { "@column (identifier at 39:9) = accounts.industry": [] } ] },
              { "@alias (identifier at 39:75) = industry_tech": [] },
              { "@expression (casewhen_expression at 40:5) = CASE WHEN SUM(accoun": [
                  { "@column (identifier at 41:18) = accounts_revenue.rev": [] },
                  { "@column (identifier at 42:18) = accounts_revenue.rev": [] },
                  { "@column (identifier at 42:58) = accounts_revenue.rev": [] },
                  { "@column (identifier at 43:18) = accounts_revenue.rev": [] } ] },
              { "@alias (identifier at 45:12) = account_size": [] },
              { "@expression (function_call at 46:5) = SUM(accounts_revenue": [
                  { "@column (identifier at 46:9) = accounts_revenue.rev": [] } ] },
              { "@alias (identifier at 46:38) = revenue_12m": [] } ] },
          { "@sources (from_clause at 47:1) = FROM accounts LEFT J": [
              { "@table (identifier at 47:6) = accounts": [] },
              { "@table (identifier at 48:15) = accounts_revenue": [] },
              { "@join (join_condition at 48:32) = USING (account_id)": [
                  { "@column (identifier at 48:39) = account_id": [] } ] },
              { "@table (identifier at 49:15) = countries": [] },
              { "@alias (identifier at 49:25) = c": [] },
              { "@join (join_condition at 49:27) = USING (country)": [
                  { "@column (identifier at 49:34) = country": [] } ] } ] },
          { "@filter (where_clause at 50:1) = WHERE accounts_reven": [
              { "@column (identifier at 50:7) = accounts_revenue.dat": [] } ] },
          { "@grouping (group_by_clause at 51:1) = GROUP BY accounts.na": [
              { "@column (identifier at 51:10) = accounts.name": [] },
              { "@column (identifier at 51:25) = region": [] },
              { "@column (identifier at 51:33) = accounts.industry": [] } ] } ] } ] } ]
```

# STEP: src.sql.parse 3

```json
[
  { "@root (source_file at 1:1) = -- CASE: Different g": [
      { "@query (query_expr at 3:1) = SELECT date(date_mon": [
          { "@columns (select_list at 4:5) = date(date_month, 'st": [
              { "@expression (function_call at 4:5) = date(date_month, 'st": [
                  { "@column (identifier at 4:10) = date_month": [] } ] },
              { "@alias (identifier at 4:42) = date_year": [] },
              { "@expression (casewhen_expression at 6:5) = CASE WHEN c.region I": [
                  { "@column (identifier at 7:14) = c.region": [] },
                  { "@column (identifier at 8:14) = c.region": [] },
                  { "@column (identifier at 9:14) = c.region": [] } ] },
              { "@alias (identifier at 11:12) = macro_region": [] },
              { "@expression (function_call at 13:5) = IIF(a.industry = 'In": [
                  { "@column (identifier at 13:9) = a.industry": [] } ] },
              { "@alias (identifier at 13:67) = industry_it": [] },
              { "@expression (function_call at 14:5) = SUM(ar.revenue)": [
                  { "@column (identifier at 14:9) = ar.revenue": [] } ] },
              { "@alias (identifier at 14:24) = revenue": [] },
              { "@expression (function_call at 15:5) = COUNT(DISTINCT ar.ac": [
                  { "@column (identifier at 15:20) = ar.account_id": [] } ] },
              { "@alias (identifier at 15:38) = accounts": [] },
              { "@expression (binary_expression at 16:5) = SUM(ar.revenue) / CO": [
                  { "@column (identifier at 16:9) = ar.revenue": [] },
                  { "@column (identifier at 16:38) = ar.account_id": [] } ] },
              { "@alias (identifier at 16:56) = revenue_per_account": [] } ] },
          { "@sources (from_clause at 17:1) = FROM accounts_revenu": [
              { "@table (identifier at 17:6) = accounts_revenue": [] },
              { "@alias (identifier at 17:23) = ar": [] },
              { "@table (identifier at 18:15) = accounts": [] },
              { "@alias (identifier at 18:24) = a": [] },
              { "@join (join_condition at 18:26) = USING (account_id)": [
                  { "@column (identifier at 18:33) = account_id": [] } ] },
              { "@table (identifier at 19:15) = countries": [] },
              { "@alias (identifier at 19:25) = c": [] },
              { "@join (join_condition at 19:27) = USING (country)": [
                  { "@column (identifier at 19:34) = country": [] } ] } ] },
          { "@filter (where_clause at 20:1) = WHERE -- This is app": [
              { "@column (identifier at 22:5) = a.industry": [] },
              { "@column (identifier at 24:9) = date_month": [] } ] },
          { "@grouping (group_by_clause at 25:1) = GROUP BY date_year, ": [
              { "@column (identifier at 25:10) = date_year": [] },
              { "@column (identifier at 25:21) = macro_region": [] },
              { "@column (identifier at 25:35) = industry_it": [] } ] } ] } ] } ]
```

# STEP: src.code.ingest_file 1

```json
{
  "Tree(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql) = Tree(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql)": {
    "files": {
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql": [
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5)": {
                  "sources": [
                    "Table(?.orders as o)",
                    "Table(?.deals as d)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [
                          "Column(?.deals.contract_end_date)",
                          "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [
                          "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_core)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_core_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_aux)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_aux_day",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5)": {
                  "sources": [
                    "Table(?.date_ranges as dr)",
                    "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [
                          "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [
                          "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [
                          "Column(?.date_ranges.date_day)",
                          "Column(?.deals_signed.contract_start_date)",
                          "Column(?.deals_signed.contract_end_date)" ],
                        "alias": null,
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [
                    "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [
                    "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [
                    "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [
                    "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5)": {
                  "sources": [
                    "Table(?.accounts_revenue)",
                    "Table(?.accounts)",
                    "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [
                          "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [
                          "Column(?.accounts.revenue)",
                          "Column(?.accounts.account_id)",
                          "Column(?.accounts.date_month)" ],
                        "alias": "revenue_12m",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "<Location>" } } ] } } ] },
    "index": {
      "<Column>": [
        "Column(?.?.*)",
        "Column(?.?.revenue)",
        "Column(?.?.contract_duration_days)",
        "Column(?.?.revenue_core)",
        "Column(?.?.revenue_aux)",
        "Column(?.deals.deal_id)",
        "Column(?.deals.account_id)",
        "Column(?.deals.contract_start_date)",
        "Column(?.deals.contract_end_date)",
        "Column(?.orders.product)",
        "Column(?.orders.value)",
        "Column(?.?.deal_id)",
        "Column(?.?.order_id)",
        "Column(?.deals.stage)",
        "Column(?.t.date_month)",
        "Column(?.t.account_id)",
        "Column(?.t.deals)",
        "Column(?.t.revenue_core)",
        "Column(?.t.revenue_aux)",
        "Column(?.t.revenue)",
        "Column(?.?.account_id)",
        "Column(?.?.date_month)",
        "Column(?.date_ranges.date_day)",
        "Column(?.?.date_day)",
        "Column(?.deals_signed.account_id)",
        "Column(?.deals_signed.deal_id)",
        "Column(?.deals_signed.revenue_core_day)",
        "Column(?.deals_signed.revenue_aux_day)",
        "Column(?.deals_signed.revenue_day)",
        "Column(?.deals_signed.contract_start_date)",
        "Column(?.deals_signed.contract_end_date)",
        "Column(?.t.*)",
        "Column(?.t.revenue_12m)",
        "Column(?.accounts.account_id)",
        "Column(?.accounts.date_month)",
        "Column(?.accounts.revenue)",
        "Column(?.accounts.revenue_core)",
        "Column(?.accounts.revenue_aux)",
        "Column(?.accounts.deals)",
        "Column(?.accounts.name)",
        "Column(?.accounts.industry)",
        "Column(?.accounts.country)",
        "Column(?.countries.region)",
        "Column(?.accounts.priority)" ],
      "<Expression>": [
        { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_core)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_core_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_aux)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_aux_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [
              "Column(?.deals.contract_end_date)",
              "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [
              "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [
              "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [
              "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [
              "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [
              "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [
              "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [
              "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [
              "Column(?.date_ranges.date_day)",
              "Column(?.deals_signed.contract_start_date)",
              "Column(?.deals_signed.contract_end_date)" ],
            "alias": null,
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [
              "Column(?.accounts.revenue)",
              "Column(?.accounts.account_id)",
              "Column(?.accounts.date_month)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } } ],
      "<Table>": [
        "Table(?.orders as o)",
        "Table(?.deals as d)",
        "Table(?.date_ranges as dr)",
        "Table(?.deals_signed as ds)",
        "Table(?.accounts_revenue)",
        "Table(?.accounts)",
        "Table(?.countries as c)" ],
      "<Query>": [
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5)": {
            "sources": [
              "Table(?.orders as o)",
              "Table(?.deals as d)" ],
            "expressions": [
              { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                  "columns": [
                    "Column(?.deals.contract_end_date)",
                    "Column(?.deals.contract_start_date)" ],
                  "alias": "contract_duration_days",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [
                    "Column(?.orders.product)",
                    "Column(?.orders.value)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [
                    "Column(?.orders.product)",
                    "Column(?.orders.value)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                  "columns": [
                    "Column(?.orders.value)" ],
                  "alias": "revenue",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5)": {
                  "sources": [
                    "Table(?.orders as o)",
                    "Table(?.deals as d)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [
                          "Column(?.deals.contract_end_date)",
                          "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [
                          "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_core)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_core_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_aux)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_aux_day",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5)": {
            "sources": [
              "Table(?.date_ranges as dr)",
              "Table(?.deals_signed as ds)" ],
            "expressions": [
              { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                  "columns": [
                    "Column(?.?.date_day)" ],
                  "alias": "date_month",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                  "columns": [
                    "Column(?.deals_signed.deal_id)" ],
                  "alias": "deals",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                  "columns": [
                    "Column(?.deals_signed.revenue_core_day)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                  "columns": [
                    "Column(?.deals_signed.revenue_aux_day)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                  "columns": [
                    "Column(?.deals_signed.revenue_day)" ],
                  "alias": "revenue",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                  "columns": [
                    "Column(?.date_ranges.date_day)",
                    "Column(?.deals_signed.contract_start_date)",
                    "Column(?.deals_signed.contract_end_date)" ],
                  "alias": null,
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5)": {
                  "sources": [
                    "Table(?.date_ranges as dr)",
                    "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [
                          "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [
                          "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [
                          "Column(?.date_ranges.date_day)",
                          "Column(?.deals_signed.contract_start_date)",
                          "Column(?.deals_signed.contract_end_date)" ],
                        "alias": null,
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [
                    "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [
                    "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [
                    "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [
                    "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5)": {
            "sources": [
              "Table(?.accounts_revenue)",
              "Table(?.accounts)",
              "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                  "columns": [
                    "Column(?.accounts.revenue)",
                    "Column(?.accounts.account_id)",
                    "Column(?.accounts.date_month)" ],
                  "alias": "revenue_12m",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5)": {
                  "sources": [
                    "Table(?.accounts_revenue)",
                    "Table(?.accounts)",
                    "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [
                          "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [
                          "Column(?.accounts.revenue)",
                          "Column(?.accounts.account_id)",
                          "Column(?.accounts.date_month)" ],
                        "alias": "revenue_12m",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "<Location>" } } ] } } ] },
    "map_key_to_expr": {
      "('Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))', ('Column(?.?.contract_duration_days)', 'Column(?.?.revenue)'))": [
        { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_day",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))', ('Column(?.?.contract_duration_days)', 'Column(?.?.revenue_core)'))": [
        { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_core)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_core_day",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))', ('Column(?.?.contract_duration_days)', 'Column(?.?.revenue_aux)'))": [
        { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_aux)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_aux_day",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))', ('Column(?.deals.contract_end_date)', 'Column(?.deals.contract_start_date)'))": [
        { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [
              "Column(?.deals.contract_end_date)",
              "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))\", ('Column(?.orders.product)', 'Column(?.orders.value)'))": [
        { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))\", ('Column(?.orders.product)', 'Column(?.orders.value)'))": [
        { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.orders.value))))', ('Column(?.orders.value)',))": [
        { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [
              "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.deals))))', ('Column(?.t.deals)',))": [
        { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [
              "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))', ('Column(?.t.revenue_core)',))": [
        { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [
              "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))', ('Column(?.t.revenue_aux)',))": [
        { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [
              "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))', ('Column(?.t.revenue)',))": [
        { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [
              "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))\", ('Column(?.?.date_day)',))": [
        { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [
              "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))', ('Column(?.deals_signed.deal_id)',))": [
        { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [
              "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))', ('Column(?.deals_signed.revenue_core_day)',))": [
        { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))', ('Column(?.deals_signed.revenue_aux_day)',))": [
        { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))', ('Column(?.deals_signed.revenue_day)',))": [
        { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))', ('Column(?.date_ranges.date_day)', 'Column(?.deals_signed.contract_end_date)', 'Column(?.deals_signed.contract_start_date)'))": [
        { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [
              "Column(?.date_ranges.date_day)",
              "Column(?.deals_signed.contract_start_date)",
              "Column(?.deals_signed.contract_end_date)" ],
            "alias": null,
            "location": "<Location>" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))\", ('Column(?.t.revenue_12m)',))": [
        { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "<Location>" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))\", ('Column(?.countries.region)',))": [
        { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))', ('Column(?.accounts.account_id)', 'Column(?.accounts.date_month)', 'Column(?.accounts.revenue)'))": [
        { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [
              "Column(?.accounts.revenue)",
              "Column(?.accounts.account_id)",
              "Column(?.accounts.date_month)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } } ] },
    "map_file_to_expr": {
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql": [
        { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_core)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_core_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_aux)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_aux_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [
              "Column(?.deals.contract_end_date)",
              "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [
              "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [
              "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [
              "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [
              "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [
              "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [
              "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [
              "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [
              "Column(?.date_ranges.date_day)",
              "Column(?.deals_signed.contract_start_date)",
              "Column(?.deals_signed.contract_end_date)" ],
            "alias": null,
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [
              "Column(?.accounts.revenue)",
              "Column(?.accounts.account_id)",
              "Column(?.accounts.date_month)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } } ] } } }
```

# STEP: src.code.ingest_file 2

```json
{
  "Tree(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql, /Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql) = Tree(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql, /Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql)": {
    "files": {
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql": [
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5)": {
                  "sources": [
                    "Table(?.orders as o)",
                    "Table(?.deals as d)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [
                          "Column(?.deals.contract_end_date)",
                          "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [
                          "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_core)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_core_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_aux)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_aux_day",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5)": {
                  "sources": [
                    "Table(?.date_ranges as dr)",
                    "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [
                          "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [
                          "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [
                          "Column(?.date_ranges.date_day)",
                          "Column(?.deals_signed.contract_start_date)",
                          "Column(?.deals_signed.contract_end_date)" ],
                        "alias": null,
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [
                    "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [
                    "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [
                    "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [
                    "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5)": {
                  "sources": [
                    "Table(?.accounts_revenue)",
                    "Table(?.accounts)",
                    "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [
                          "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [
                          "Column(?.accounts.revenue)",
                          "Column(?.accounts.account_id)",
                          "Column(?.accounts.date_month)" ],
                        "alias": "revenue_12m",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "<Location>" } } ] } } ],
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql": [
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:5:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:5:1)": {
            "sources": [
              "Table(?.accounts_revenue as ar)",
              "Table(?.accounts as a)",
              "Table(?.countries as c)",
              "Table(?.accounts_360 as a360)" ],
            "expressions": [
              { "Expression(1-revenue.sql:6:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [
                    "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:7:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:12:5) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
                  "columns": [
                    "Column(?.accounts.industry)" ],
                  "alias": "industry_cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:18:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:19:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:20:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)",
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "revenue_per_account",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:30:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:30:1)": {
            "sources": [
              "Table(?.accounts)",
              "Table(?.accounts_revenue)",
              "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(1-revenue.sql:33:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:39:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                  "columns": [
                    "Column(?.accounts.industry)" ],
                  "alias": "industry_tech",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:40:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "account_size",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:46:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "<Location>" } } ] } } ] },
    "index": {
      "<Column>": [
        "Column(?.?.*)",
        "Column(?.?.revenue)",
        "Column(?.?.contract_duration_days)",
        "Column(?.?.revenue_core)",
        "Column(?.?.revenue_aux)",
        "Column(?.deals.deal_id)",
        "Column(?.deals.account_id)",
        "Column(?.deals.contract_start_date)",
        "Column(?.deals.contract_end_date)",
        "Column(?.orders.product)",
        "Column(?.orders.value)",
        "Column(?.?.deal_id)",
        "Column(?.?.order_id)",
        "Column(?.deals.stage)",
        "Column(?.t.date_month)",
        "Column(?.t.account_id)",
        "Column(?.t.deals)",
        "Column(?.t.revenue_core)",
        "Column(?.t.revenue_aux)",
        "Column(?.t.revenue)",
        "Column(?.?.account_id)",
        "Column(?.?.date_month)",
        "Column(?.date_ranges.date_day)",
        "Column(?.?.date_day)",
        "Column(?.deals_signed.account_id)",
        "Column(?.deals_signed.deal_id)",
        "Column(?.deals_signed.revenue_core_day)",
        "Column(?.deals_signed.revenue_aux_day)",
        "Column(?.deals_signed.revenue_day)",
        "Column(?.deals_signed.contract_start_date)",
        "Column(?.deals_signed.contract_end_date)",
        "Column(?.t.*)",
        "Column(?.t.revenue_12m)",
        "Column(?.accounts.account_id)",
        "Column(?.accounts.date_month)",
        "Column(?.accounts.revenue)",
        "Column(?.accounts.revenue_core)",
        "Column(?.accounts.revenue_aux)",
        "Column(?.accounts.deals)",
        "Column(?.accounts.name)",
        "Column(?.accounts.industry)",
        "Column(?.accounts.country)",
        "Column(?.countries.region)",
        "Column(?.accounts.priority)",
        "Column(?.?.date_month)",
        "Column(?.countries.region)",
        "Column(?.accounts.industry)",
        "Column(?.accounts_360.account_size)",
        "Column(?.accounts_revenue.revenue)",
        "Column(?.accounts_revenue.account_id)",
        "Column(?.?.account_id)",
        "Column(?.?.country)",
        "Column(?.?.date_year)",
        "Column(?.?.region_cluster)",
        "Column(?.?.industry_cluster)",
        "Column(?.accounts.name)",
        "Column(?.accounts_revenue.region)",
        "Column(?.countries.region)",
        "Column(?.accounts.industry)",
        "Column(?.accounts_revenue.revenue)",
        "Column(?.accounts_revenue.account_id)",
        "Column(?.accounts_revenue.country)",
        "Column(?.accounts_revenue.date_month)" ],
      "<Expression>": [
        { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_core)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_core_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_aux)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_aux_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [
              "Column(?.deals.contract_end_date)",
              "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [
              "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [
              "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [
              "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [
              "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [
              "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [
              "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [
              "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [
              "Column(?.date_ranges.date_day)",
              "Column(?.deals_signed.contract_start_date)",
              "Column(?.deals_signed.contract_end_date)" ],
            "alias": null,
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [
              "Column(?.accounts.revenue)",
              "Column(?.accounts.account_id)",
              "Column(?.accounts.date_month)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:6:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [
              "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:7:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:12:5) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:18:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:19:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:20:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)",
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "revenue_per_account",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:33:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:39:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:40:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:46:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } } ],
      "<Table>": [
        "Table(?.orders as o)",
        "Table(?.deals as d)",
        "Table(?.date_ranges as dr)",
        "Table(?.deals_signed as ds)",
        "Table(?.accounts_revenue)",
        "Table(?.accounts)",
        "Table(?.countries as c)",
        "Table(?.accounts_revenue as ar)",
        "Table(?.accounts as a)",
        "Table(?.countries as c)",
        "Table(?.accounts_360 as a360)",
        "Table(?.accounts)",
        "Table(?.accounts_revenue)",
        "Table(?.countries as c)" ],
      "<Query>": [
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5)": {
            "sources": [
              "Table(?.orders as o)",
              "Table(?.deals as d)" ],
            "expressions": [
              { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                  "columns": [
                    "Column(?.deals.contract_end_date)",
                    "Column(?.deals.contract_start_date)" ],
                  "alias": "contract_duration_days",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [
                    "Column(?.orders.product)",
                    "Column(?.orders.value)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [
                    "Column(?.orders.product)",
                    "Column(?.orders.value)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                  "columns": [
                    "Column(?.orders.value)" ],
                  "alias": "revenue",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5)": {
                  "sources": [
                    "Table(?.orders as o)",
                    "Table(?.deals as d)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [
                          "Column(?.deals.contract_end_date)",
                          "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [
                          "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_core)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_core_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_aux)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_aux_day",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5)": {
            "sources": [
              "Table(?.date_ranges as dr)",
              "Table(?.deals_signed as ds)" ],
            "expressions": [
              { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                  "columns": [
                    "Column(?.?.date_day)" ],
                  "alias": "date_month",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                  "columns": [
                    "Column(?.deals_signed.deal_id)" ],
                  "alias": "deals",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                  "columns": [
                    "Column(?.deals_signed.revenue_core_day)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                  "columns": [
                    "Column(?.deals_signed.revenue_aux_day)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                  "columns": [
                    "Column(?.deals_signed.revenue_day)" ],
                  "alias": "revenue",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                  "columns": [
                    "Column(?.date_ranges.date_day)",
                    "Column(?.deals_signed.contract_start_date)",
                    "Column(?.deals_signed.contract_end_date)" ],
                  "alias": null,
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5)": {
                  "sources": [
                    "Table(?.date_ranges as dr)",
                    "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [
                          "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [
                          "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [
                          "Column(?.date_ranges.date_day)",
                          "Column(?.deals_signed.contract_start_date)",
                          "Column(?.deals_signed.contract_end_date)" ],
                        "alias": null,
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [
                    "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [
                    "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [
                    "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [
                    "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5)": {
            "sources": [
              "Table(?.accounts_revenue)",
              "Table(?.accounts)",
              "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                  "columns": [
                    "Column(?.accounts.revenue)",
                    "Column(?.accounts.account_id)",
                    "Column(?.accounts.date_month)" ],
                  "alias": "revenue_12m",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5)": {
                  "sources": [
                    "Table(?.accounts_revenue)",
                    "Table(?.accounts)",
                    "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [
                          "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [
                          "Column(?.accounts.revenue)",
                          "Column(?.accounts.account_id)",
                          "Column(?.accounts.date_month)" ],
                        "alias": "revenue_12m",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:5:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:5:1)": {
            "sources": [
              "Table(?.accounts_revenue as ar)",
              "Table(?.accounts as a)",
              "Table(?.countries as c)",
              "Table(?.accounts_360 as a360)" ],
            "expressions": [
              { "Expression(1-revenue.sql:6:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [
                    "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:7:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:12:5) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
                  "columns": [
                    "Column(?.accounts.industry)" ],
                  "alias": "industry_cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:18:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:19:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:20:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)",
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "revenue_per_account",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:30:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:30:1)": {
            "sources": [
              "Table(?.accounts)",
              "Table(?.accounts_revenue)",
              "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(1-revenue.sql:33:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:39:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                  "columns": [
                    "Column(?.accounts.industry)" ],
                  "alias": "industry_tech",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:40:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "account_size",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:46:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "<Location>" } } ] } } ] },
    "map_key_to_expr": {
      "('Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))', ('Column(?.?.contract_duration_days)', 'Column(?.?.revenue)'))": [
        { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_day",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))', ('Column(?.?.contract_duration_days)', 'Column(?.?.revenue_core)'))": [
        { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_core)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_core_day",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))', ('Column(?.?.contract_duration_days)', 'Column(?.?.revenue_aux)'))": [
        { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_aux)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_aux_day",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))', ('Column(?.deals.contract_end_date)', 'Column(?.deals.contract_start_date)'))": [
        { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [
              "Column(?.deals.contract_end_date)",
              "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))\", ('Column(?.orders.product)', 'Column(?.orders.value)'))": [
        { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))\", ('Column(?.orders.product)', 'Column(?.orders.value)'))": [
        { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.orders.value))))', ('Column(?.orders.value)',))": [
        { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [
              "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.deals))))', ('Column(?.t.deals)',))": [
        { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [
              "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))', ('Column(?.t.revenue_core)',))": [
        { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [
              "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))', ('Column(?.t.revenue_aux)',))": [
        { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [
              "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))', ('Column(?.t.revenue)',))": [
        { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [
              "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))\", ('Column(?.?.date_day)',))": [
        { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [
              "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))', ('Column(?.deals_signed.deal_id)',))": [
        { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [
              "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))', ('Column(?.deals_signed.revenue_core_day)',))": [
        { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))', ('Column(?.deals_signed.revenue_aux_day)',))": [
        { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))', ('Column(?.deals_signed.revenue_day)',))": [
        { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))', ('Column(?.date_ranges.date_day)', 'Column(?.deals_signed.contract_end_date)', 'Column(?.deals_signed.contract_start_date)'))": [
        { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [
              "Column(?.date_ranges.date_day)",
              "Column(?.deals_signed.contract_start_date)",
              "Column(?.deals_signed.contract_end_date)" ],
            "alias": null,
            "location": "<Location>" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))\", ('Column(?.t.revenue_12m)',))": [
        { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "<Location>" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))\", ('Column(?.countries.region)',))": [
        { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:7:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:33:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))', ('Column(?.accounts.account_id)', 'Column(?.accounts.date_month)', 'Column(?.accounts.revenue)'))": [
        { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [
              "Column(?.accounts.revenue)",
              "Column(?.accounts.account_id)",
              "Column(?.accounts.date_month)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))\", ('Column(?.?.date_month)',))": [
        { "Expression(1-revenue.sql:6:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [
              "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "<Location>" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))\", ('Column(?.accounts.industry)',))": [
        { "Expression(1-revenue.sql:12:5) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))', ('Column(?.accounts_revenue.revenue)',))": [
        { "Expression(1-revenue.sql:18:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:46:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))', ('Column(?.accounts_revenue.account_id)',))": [
        { "Expression(1-revenue.sql:19:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))', ('Column(?.accounts_revenue.account_id)', 'Column(?.accounts_revenue.revenue)'))": [
        { "Expression(1-revenue.sql:20:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)",
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "revenue_per_account",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))\", ('Column(?.accounts.industry)',))": [
        { "Expression(1-revenue.sql:39:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "<Location>" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))\", ('Column(?.accounts_revenue.revenue)',))": [
        { "Expression(1-revenue.sql:40:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "<Location>" } } ] },
    "map_file_to_expr": {
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql": [
        { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_core)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_core_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_aux)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_aux_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [
              "Column(?.deals.contract_end_date)",
              "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [
              "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [
              "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [
              "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [
              "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [
              "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [
              "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [
              "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [
              "Column(?.date_ranges.date_day)",
              "Column(?.deals_signed.contract_start_date)",
              "Column(?.deals_signed.contract_end_date)" ],
            "alias": null,
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [
              "Column(?.accounts.revenue)",
              "Column(?.accounts.account_id)",
              "Column(?.accounts.date_month)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } } ],
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql": [
        { "Expression(1-revenue.sql:6:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [
              "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:7:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:12:5) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:18:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:19:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:20:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)",
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "revenue_per_account",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:33:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:39:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:40:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:46:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } } ] } } }
```

# STEP: src.code.ingest_file 3

```json
{
  "Tree(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql, /Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql, /Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/editor.sql) = Tree(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql, /Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql, /Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/editor.sql)": {
    "files": {
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql": [
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5)": {
                  "sources": [
                    "Table(?.orders as o)",
                    "Table(?.deals as d)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [
                          "Column(?.deals.contract_end_date)",
                          "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [
                          "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_core)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_core_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_aux)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_aux_day",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5)": {
                  "sources": [
                    "Table(?.date_ranges as dr)",
                    "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [
                          "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [
                          "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [
                          "Column(?.date_ranges.date_day)",
                          "Column(?.deals_signed.contract_start_date)",
                          "Column(?.deals_signed.contract_end_date)" ],
                        "alias": null,
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [
                    "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [
                    "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [
                    "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [
                    "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5)": {
                  "sources": [
                    "Table(?.accounts_revenue)",
                    "Table(?.accounts)",
                    "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [
                          "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [
                          "Column(?.accounts.revenue)",
                          "Column(?.accounts.account_id)",
                          "Column(?.accounts.date_month)" ],
                        "alias": "revenue_12m",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "<Location>" } } ] } } ],
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql": [
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:5:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:5:1)": {
            "sources": [
              "Table(?.accounts_revenue as ar)",
              "Table(?.accounts as a)",
              "Table(?.countries as c)",
              "Table(?.accounts_360 as a360)" ],
            "expressions": [
              { "Expression(1-revenue.sql:6:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [
                    "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:7:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:12:5) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
                  "columns": [
                    "Column(?.accounts.industry)" ],
                  "alias": "industry_cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:18:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:19:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:20:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)",
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "revenue_per_account",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:30:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:30:1)": {
            "sources": [
              "Table(?.accounts)",
              "Table(?.accounts_revenue)",
              "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(1-revenue.sql:33:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:39:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                  "columns": [
                    "Column(?.accounts.industry)" ],
                  "alias": "industry_tech",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:40:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "account_size",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:46:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "<Location>" } } ] } } ],
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/editor.sql": [
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/editor.sql:3:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/editor.sql:3:1)": {
            "sources": [
              "Table(?.accounts_revenue as ar)",
              "Table(?.accounts as a)",
              "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(editor.sql:4:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [
                    "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "<Location>" } },
              { "Expression(editor.sql:6:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "macro_region",
                  "location": "<Location>" } },
              { "Expression(editor.sql:13:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
                  "columns": [
                    "Column(?.accounts.industry)" ],
                  "alias": "industry_it",
                  "location": "<Location>" } },
              { "Expression(editor.sql:14:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } },
              { "Expression(editor.sql:15:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "<Location>" } },
              { "Expression(editor.sql:16:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)",
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "revenue_per_account",
                  "location": "<Location>" } } ] } } ] },
    "index": {
      "<Column>": [
        "Column(?.?.*)",
        "Column(?.?.revenue)",
        "Column(?.?.contract_duration_days)",
        "Column(?.?.revenue_core)",
        "Column(?.?.revenue_aux)",
        "Column(?.deals.deal_id)",
        "Column(?.deals.account_id)",
        "Column(?.deals.contract_start_date)",
        "Column(?.deals.contract_end_date)",
        "Column(?.orders.product)",
        "Column(?.orders.value)",
        "Column(?.?.deal_id)",
        "Column(?.?.order_id)",
        "Column(?.deals.stage)",
        "Column(?.t.date_month)",
        "Column(?.t.account_id)",
        "Column(?.t.deals)",
        "Column(?.t.revenue_core)",
        "Column(?.t.revenue_aux)",
        "Column(?.t.revenue)",
        "Column(?.?.account_id)",
        "Column(?.?.date_month)",
        "Column(?.date_ranges.date_day)",
        "Column(?.?.date_day)",
        "Column(?.deals_signed.account_id)",
        "Column(?.deals_signed.deal_id)",
        "Column(?.deals_signed.revenue_core_day)",
        "Column(?.deals_signed.revenue_aux_day)",
        "Column(?.deals_signed.revenue_day)",
        "Column(?.deals_signed.contract_start_date)",
        "Column(?.deals_signed.contract_end_date)",
        "Column(?.t.*)",
        "Column(?.t.revenue_12m)",
        "Column(?.accounts.account_id)",
        "Column(?.accounts.date_month)",
        "Column(?.accounts.revenue)",
        "Column(?.accounts.revenue_core)",
        "Column(?.accounts.revenue_aux)",
        "Column(?.accounts.deals)",
        "Column(?.accounts.name)",
        "Column(?.accounts.industry)",
        "Column(?.accounts.country)",
        "Column(?.countries.region)",
        "Column(?.accounts.priority)",
        "Column(?.?.date_month)",
        "Column(?.countries.region)",
        "Column(?.accounts.industry)",
        "Column(?.accounts_360.account_size)",
        "Column(?.accounts_revenue.revenue)",
        "Column(?.accounts_revenue.account_id)",
        "Column(?.?.account_id)",
        "Column(?.?.country)",
        "Column(?.?.date_year)",
        "Column(?.?.region_cluster)",
        "Column(?.?.industry_cluster)",
        "Column(?.accounts.name)",
        "Column(?.accounts_revenue.region)",
        "Column(?.countries.region)",
        "Column(?.accounts.industry)",
        "Column(?.accounts_revenue.revenue)",
        "Column(?.accounts_revenue.account_id)",
        "Column(?.accounts_revenue.country)",
        "Column(?.accounts_revenue.date_month)",
        "Column(?.?.date_month)",
        "Column(?.countries.region)",
        "Column(?.accounts.industry)",
        "Column(?.accounts_revenue.revenue)",
        "Column(?.accounts_revenue.account_id)",
        "Column(?.?.account_id)",
        "Column(?.?.country)",
        "Column(?.?.date_year)",
        "Column(?.?.macro_region)",
        "Column(?.?.industry_it)" ],
      "<Expression>": [
        { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_core)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_core_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_aux)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_aux_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [
              "Column(?.deals.contract_end_date)",
              "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [
              "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [
              "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [
              "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [
              "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [
              "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [
              "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [
              "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [
              "Column(?.date_ranges.date_day)",
              "Column(?.deals_signed.contract_start_date)",
              "Column(?.deals_signed.contract_end_date)" ],
            "alias": null,
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [
              "Column(?.accounts.revenue)",
              "Column(?.accounts.account_id)",
              "Column(?.accounts.date_month)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:6:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [
              "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:7:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:12:5) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:18:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:19:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:20:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)",
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "revenue_per_account",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:33:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:39:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:40:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:46:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } },
        { "Expression(editor.sql:4:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [
              "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "<Location>" } },
        { "Expression(editor.sql:6:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "macro_region",
            "location": "<Location>" } },
        { "Expression(editor.sql:13:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_it",
            "location": "<Location>" } },
        { "Expression(editor.sql:14:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(editor.sql:15:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "<Location>" } },
        { "Expression(editor.sql:16:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)",
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "revenue_per_account",
            "location": "<Location>" } } ],
      "<Table>": [
        "Table(?.orders as o)",
        "Table(?.deals as d)",
        "Table(?.date_ranges as dr)",
        "Table(?.deals_signed as ds)",
        "Table(?.accounts_revenue)",
        "Table(?.accounts)",
        "Table(?.countries as c)",
        "Table(?.accounts_revenue as ar)",
        "Table(?.accounts as a)",
        "Table(?.countries as c)",
        "Table(?.accounts_360 as a360)",
        "Table(?.accounts)",
        "Table(?.accounts_revenue)",
        "Table(?.countries as c)",
        "Table(?.accounts_revenue as ar)",
        "Table(?.accounts as a)",
        "Table(?.countries as c)" ],
      "<Query>": [
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5)": {
            "sources": [
              "Table(?.orders as o)",
              "Table(?.deals as d)" ],
            "expressions": [
              { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                  "columns": [
                    "Column(?.deals.contract_end_date)",
                    "Column(?.deals.contract_start_date)" ],
                  "alias": "contract_duration_days",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [
                    "Column(?.orders.product)",
                    "Column(?.orders.value)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [
                    "Column(?.orders.product)",
                    "Column(?.orders.value)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                  "columns": [
                    "Column(?.orders.value)" ],
                  "alias": "revenue",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:26:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:32:5)": {
                  "sources": [
                    "Table(?.orders as o)",
                    "Table(?.deals as d)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [
                          "Column(?.deals.contract_end_date)",
                          "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [
                          "Column(?.orders.product)",
                          "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [
                          "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_core)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_core_day",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [
                    "Column(?.?.revenue_aux)",
                    "Column(?.?.contract_duration_days)" ],
                  "alias": "revenue_aux_day",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5)": {
            "sources": [
              "Table(?.date_ranges as dr)",
              "Table(?.deals_signed as ds)" ],
            "expressions": [
              { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                  "columns": [
                    "Column(?.?.date_day)" ],
                  "alias": "date_month",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                  "columns": [
                    "Column(?.deals_signed.deal_id)" ],
                  "alias": "deals",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                  "columns": [
                    "Column(?.deals_signed.revenue_core_day)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                  "columns": [
                    "Column(?.deals_signed.revenue_aux_day)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                  "columns": [
                    "Column(?.deals_signed.revenue_day)" ],
                  "alias": "revenue",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                  "columns": [
                    "Column(?.date_ranges.date_day)",
                    "Column(?.deals_signed.contract_start_date)",
                    "Column(?.deals_signed.contract_end_date)" ],
                  "alias": null,
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:51:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:59:5)": {
                  "sources": [
                    "Table(?.date_ranges as dr)",
                    "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [
                          "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [
                          "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [
                          "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [
                          "Column(?.date_ranges.date_day)",
                          "Column(?.deals_signed.contract_start_date)",
                          "Column(?.deals_signed.contract_end_date)" ],
                        "alias": null,
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [
                    "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [
                    "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [
                    "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [
                    "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5)": {
            "sources": [
              "Table(?.accounts_revenue)",
              "Table(?.accounts)",
              "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "<Location>" } },
              { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                  "columns": [
                    "Column(?.accounts.revenue)",
                    "Column(?.accounts.account_id)",
                    "Column(?.accounts.date_month)" ],
                  "alias": "revenue_12m",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:79:1)": {
            "sources": [
              { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql:88:5)": {
                  "sources": [
                    "Table(?.accounts_revenue)",
                    "Table(?.accounts)",
                    "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [
                          "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "<Location>" } },
                    { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [
                          "Column(?.accounts.revenue)",
                          "Column(?.accounts.account_id)",
                          "Column(?.accounts.date_month)" ],
                        "alias": "revenue_12m",
                        "location": "<Location>" } } ] } } ],
            "expressions": [
              { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:5:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:5:1)": {
            "sources": [
              "Table(?.accounts_revenue as ar)",
              "Table(?.accounts as a)",
              "Table(?.countries as c)",
              "Table(?.accounts_360 as a360)" ],
            "expressions": [
              { "Expression(1-revenue.sql:6:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [
                    "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:7:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:12:5) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
                  "columns": [
                    "Column(?.accounts.industry)" ],
                  "alias": "industry_cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:18:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:19:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:20:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)",
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "revenue_per_account",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:30:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql:30:1)": {
            "sources": [
              "Table(?.accounts)",
              "Table(?.accounts_revenue)",
              "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(1-revenue.sql:33:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "cluster",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:39:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                  "columns": [
                    "Column(?.accounts.industry)" ],
                  "alias": "industry_tech",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:40:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "account_size",
                  "location": "<Location>" } },
              { "Expression(1-revenue.sql:46:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "<Location>" } } ] } },
        { "Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/editor.sql:3:1) = Query(/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/editor.sql:3:1)": {
            "sources": [
              "Table(?.accounts_revenue as ar)",
              "Table(?.accounts as a)",
              "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(editor.sql:4:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [
                    "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "<Location>" } },
              { "Expression(editor.sql:6:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
                  "columns": [
                    "Column(?.countries.region)" ],
                  "alias": "macro_region",
                  "location": "<Location>" } },
              { "Expression(editor.sql:13:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
                  "columns": [
                    "Column(?.accounts.industry)" ],
                  "alias": "industry_it",
                  "location": "<Location>" } },
              { "Expression(editor.sql:14:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "<Location>" } },
              { "Expression(editor.sql:15:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "<Location>" } },
              { "Expression(editor.sql:16:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [
                    "Column(?.accounts_revenue.revenue)",
                    "Column(?.accounts_revenue.account_id)" ],
                  "alias": "revenue_per_account",
                  "location": "<Location>" } } ] } } ] },
    "map_key_to_expr": {
      "('Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))', ('Column(?.?.contract_duration_days)', 'Column(?.?.revenue)'))": [
        { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_day",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))', ('Column(?.?.contract_duration_days)', 'Column(?.?.revenue_core)'))": [
        { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_core)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_core_day",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))', ('Column(?.?.contract_duration_days)', 'Column(?.?.revenue_aux)'))": [
        { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_aux)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_aux_day",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))', ('Column(?.deals.contract_end_date)', 'Column(?.deals.contract_start_date)'))": [
        { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [
              "Column(?.deals.contract_end_date)",
              "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))\", ('Column(?.orders.product)', 'Column(?.orders.value)'))": [
        { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))\", ('Column(?.orders.product)', 'Column(?.orders.value)'))": [
        { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.orders.value))))', ('Column(?.orders.value)',))": [
        { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [
              "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.deals))))', ('Column(?.t.deals)',))": [
        { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [
              "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))', ('Column(?.t.revenue_core)',))": [
        { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [
              "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))', ('Column(?.t.revenue_aux)',))": [
        { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [
              "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))', ('Column(?.t.revenue)',))": [
        { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [
              "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))\", ('Column(?.?.date_day)',))": [
        { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [
              "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))', ('Column(?.deals_signed.deal_id)',))": [
        { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [
              "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))', ('Column(?.deals_signed.revenue_core_day)',))": [
        { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))', ('Column(?.deals_signed.revenue_aux_day)',))": [
        { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))', ('Column(?.deals_signed.revenue_day)',))": [
        { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))', ('Column(?.date_ranges.date_day)', 'Column(?.deals_signed.contract_end_date)', 'Column(?.deals_signed.contract_start_date)'))": [
        { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [
              "Column(?.date_ranges.date_day)",
              "Column(?.deals_signed.contract_start_date)",
              "Column(?.deals_signed.contract_end_date)" ],
            "alias": null,
            "location": "<Location>" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))\", ('Column(?.t.revenue_12m)',))": [
        { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "<Location>" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))\", ('Column(?.countries.region)',))": [
        { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:7:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:33:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))', ('Column(?.accounts.account_id)', 'Column(?.accounts.date_month)', 'Column(?.accounts.revenue)'))": [
        { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [
              "Column(?.accounts.revenue)",
              "Column(?.accounts.account_id)",
              "Column(?.accounts.date_month)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))\", ('Column(?.?.date_month)',))": [
        { "Expression(1-revenue.sql:6:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [
              "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "<Location>" } },
        { "Expression(editor.sql:4:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [
              "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "<Location>" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))\", ('Column(?.accounts.industry)',))": [
        { "Expression(1-revenue.sql:12:5) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))', ('Column(?.accounts_revenue.revenue)',))": [
        { "Expression(1-revenue.sql:18:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:46:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } },
        { "Expression(editor.sql:14:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } } ],
      "('Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))', ('Column(?.accounts_revenue.account_id)',))": [
        { "Expression(1-revenue.sql:19:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "<Location>" } },
        { "Expression(editor.sql:15:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "<Location>" } } ],
      "('Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))', ('Column(?.accounts_revenue.account_id)', 'Column(?.accounts_revenue.revenue)'))": [
        { "Expression(1-revenue.sql:20:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)",
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "revenue_per_account",
            "location": "<Location>" } },
        { "Expression(editor.sql:16:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)",
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "revenue_per_account",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))\", ('Column(?.accounts.industry)',))": [
        { "Expression(1-revenue.sql:39:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "<Location>" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))\", ('Column(?.accounts_revenue.revenue)',))": [
        { "Expression(1-revenue.sql:40:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "<Location>" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))\", ('Column(?.countries.region)',))": [
        { "Expression(editor.sql:6:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "macro_region",
            "location": "<Location>" } } ],
      "(\"Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))\", ('Column(?.accounts.industry)',))": [
        { "Expression(editor.sql:13:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_it",
            "location": "<Location>" } } ] },
    "map_file_to_expr": {
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/0-accounts.sql": [
        { "Expression(0-accounts.sql:28:5) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:29:5) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_core)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_core_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:30:5) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [
              "Column(?.?.revenue_aux)",
              "Column(?.?.contract_duration_days)" ],
            "alias": "revenue_aux_day",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:37:9) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [
              "Column(?.deals.contract_end_date)",
              "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:38:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:39:9) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [
              "Column(?.orders.product)",
              "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:40:9) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [
              "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:54:5) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [
              "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:55:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [
              "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:56:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [
              "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:57:5) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [
              "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:61:9) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [
              "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:63:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [
              "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:64:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:65:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:66:9) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [
              "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:69:17) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [
              "Column(?.date_ranges.date_day)",
              "Column(?.deals_signed.contract_start_date)",
              "Column(?.deals_signed.contract_end_date)" ],
            "alias": null,
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:81:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(0-accounts.sql:104:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [
              "Column(?.accounts.revenue)",
              "Column(?.accounts.account_id)",
              "Column(?.accounts.date_month)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } } ],
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/codebase/1-revenue.sql": [
        { "Expression(1-revenue.sql:6:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [
              "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:7:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:12:5) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:18:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:19:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:20:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)",
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "revenue_per_account",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:33:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:39:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:40:5) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "<Location>" } },
        { "Expression(1-revenue.sql:46:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "<Location>" } } ],
      "/Users/ilyakochik/Developer/refining-company/sql-refinery/backend/tests/inputs/editor.sql": [
        { "Expression(editor.sql:4:5) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [
              "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "<Location>" } },
        { "Expression(editor.sql:6:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
            "columns": [
              "Column(?.countries.region)" ],
            "alias": "macro_region",
            "location": "<Location>" } },
        { "Expression(editor.sql:13:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
            "columns": [
              "Column(?.accounts.industry)" ],
            "alias": "industry_it",
            "location": "<Location>" } },
        { "Expression(editor.sql:14:5) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "<Location>" } },
        { "Expression(editor.sql:15:5) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "<Location>" } },
        { "Expression(editor.sql:16:5) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [
              "Column(?.accounts_revenue.revenue)",
              "Column(?.accounts_revenue.account_id)" ],
            "alias": "revenue_per_account",
            "location": "<Location>" } } ] } } }
```

# STEP: src.variations.get_variations 1

```json
[
  { "ExpressionVariations(editor.sql:6:5, similarity=0.78, other=ExpressionGroup(reliability=3, Expression(0-accounts.sql:98:9), Expression(1-revenue.sql:7:5), Expression(1-revenue.sql:33:5))) = ExpressionVariations(editor.sql:6:5, similarity=0.78, other=ExpressionGroup(reliability=3, Expression(0-accounts.sql:98:9), Expression(1-revenue.sql:7:5), Expression(1-revenue.sql:33:5)))": {
      "this": {
        "Expression(editor.sql:6:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
          "columns": [
            "Column(?.countries.region)" ],
          "alias": "macro_region",
          "location": "<Location>" } },
      "other": {
        "ExpressionGroup(reliability=3, Expression(0-accounts.sql:98:9), Expression(1-revenue.sql:7:5), Expression(1-revenue.sql:33:5)) = ExpressionGroup(reliability=3, Expression(0-accounts.sql:98:9), Expression(1-revenue.sql:7:5), Expression(1-revenue.sql:33:5))": {
          "expressions": [
            { "Expression(0-accounts.sql:98:9) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                "columns": [
                  "Column(?.countries.region)" ],
                "alias": "region_cluster",
                "location": "<Location>" } },
            { "Expression(1-revenue.sql:7:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                "columns": [
                  "Column(?.countries.region)" ],
                "alias": "region_cluster",
                "location": "<Location>" } },
            { "Expression(1-revenue.sql:33:5) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                "columns": [
                  "Column(?.countries.region)" ],
                "alias": "cluster",
                "location": "<Location>" } } ],
          "repr": "Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))",
          "columns": [
            "Column(?.countries.region)" ],
          "reliability": 3 } },
      "similarity": 0.78 } },
  { "ExpressionVariations(editor.sql:13:5, similarity=0.95, other=ExpressionGroup(reliability=1, Expression(1-revenue.sql:39:5))) = ExpressionVariations(editor.sql:13:5, similarity=0.95, other=ExpressionGroup(reliability=1, Expression(1-revenue.sql:39:5)))": {
      "this": {
        "Expression(editor.sql:13:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
          "columns": [
            "Column(?.accounts.industry)" ],
          "alias": "industry_it",
          "location": "<Location>" } },
      "other": {
        "ExpressionGroup(reliability=1, Expression(1-revenue.sql:39:5)) = ExpressionGroup(reliability=1, Expression(1-revenue.sql:39:5))": {
          "expressions": [
            { "Expression(1-revenue.sql:39:5) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                "columns": [
                  "Column(?.accounts.industry)" ],
                "alias": "industry_tech",
                "location": "<Location>" } } ],
          "repr": "Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))",
          "columns": [
            "Column(?.accounts.industry)" ],
          "reliability": 1 } },
      "similarity": 0.95 } } ]
```
