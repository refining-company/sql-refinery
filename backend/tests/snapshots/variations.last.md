# Session: variations

## Internal Pipeline

### src.sql.parse (call 1)

```json
[
  { "@root (source_file at 1:1) = -- FOUNDATIONAL TABL": [
      { "@query (query_expr at 26:1) = SELECT *, revenue / ": [
          { "@columns (select_list at 27:5) = *, revenue / contrac": [
              { "@alias (identifier at 28:41) = revenue_day": [] },
              { "@expression (binary_expression at 28:5) = revenue / contract_d": [
                  { "@column (identifier at 28:15) = contract_duration_da": [] },
                  { "@column (identifier at 28:5) = revenue": [] } ] },
              { "@alias (identifier at 29:46) = revenue_core_day": [] },
              { "@expression (binary_expression at 29:5) = revenue_core / contr": [
                  { "@column (identifier at 29:20) = contract_duration_da": [] },
                  { "@column (identifier at 29:5) = revenue_core": [] } ] },
              { "@alias (identifier at 30:45) = revenue_aux_day": [] },
              { "@expression (binary_expression at 30:5) = revenue_aux / contra": [
                  { "@column (identifier at 30:19) = contract_duration_da": [] },
                  { "@column (identifier at 30:5) = revenue_aux": [] } ] },
              { "@column (select_all at 27:5) = *": [] } ] },
          { "@sources (from_clause at 31:1) = FROM ( SELECT d.deal": [
              { "@alias (identifier at 45:6) = t": [] },
              { "@query (query_expr at 32:5) = SELECT d.deal_id, d.": [
                  { "@columns (select_list at 33:9) = d.deal_id, d.account": [
                      { "@alias (identifier at 37:82) = contract_duration_da": [] },
                      { "@expression (binary_expression at 37:9) = julianday(d.contract": [
                          { "@column (identifier at 37:19) = d.contract_end_date": [] },
                          { "@column (identifier at 37:52) = d.contract_start_dat": [] } ] },
                      { "@alias (identifier at 38:110) = revenue_core": [] },
                      { "@expression (function_call at 38:9) = SUM(CASE WHEN o.prod": [
                          { "@column (identifier at 38:23) = o.product": [] },
                          { "@column (identifier at 38:87) = o.value": [] } ] },
                      { "@alias (identifier at 39:91) = revenue_aux": [] },
                      { "@expression (function_call at 39:9) = SUM(CASE WHEN o.prod": [
                          { "@column (identifier at 39:23) = o.product": [] },
                          { "@column (identifier at 39:68) = o.value": [] } ] },
                      { "@alias (identifier at 40:25) = revenue": [] },
                      { "@expression (function_call at 40:9) = SUM(o.value)": [
                          { "@column (identifier at 40:13) = o.value": [] } ] },
                      { "@column (identifier at 33:9) = d.deal_id": [] },
                      { "@column (identifier at 34:9) = d.account_id": [] },
                      { "@column (identifier at 35:9) = d.contract_start_dat": [] },
                      { "@column (identifier at 36:9) = d.contract_end_date": [] } ] },
                  { "@filter (where_clause at 43:5) = WHERE d.stage = 4": [
                      { "@column (identifier at 43:11) = d.stage": [] } ] },
                  { "@grouping (group_by_clause at 44:5) = GROUP BY d.deal_id, ": [
                      { "@column (identifier at 44:14) = d.deal_id": [] },
                      { "@column (identifier at 44:25) = d.account_id": [] },
                      { "@column (identifier at 44:39) = d.contract_start_dat": [] },
                      { "@column (identifier at 44:62) = d.contract_end_date": [] } ] },
                  { "@sources (from_clause at 41:5) = FROM orders o JOIN d": [
                      { "@alias (identifier at 41:17) = o": [] },
                      { "@table (identifier at 41:10) = orders": [] },
                      { "@alias (identifier at 42:20) = d": [] },
                      { "@table (identifier at 42:14) = deals": [] },
                      { "@join (join_condition at 42:22) = USING (deal_id, orde": [
                          { "@column (identifier at 42:29) = deal_id": [] },
                          { "@column (identifier at 42:38) = order_id": [] } ] } ] } ] } ] } ] },
      { "@query (query_expr at 51:1) = SELECT t.date_month,": [
          { "@columns (select_list at 52:5) = t.date_month, t.acco": [
              { "@alias (identifier at 54:21) = deals": [] },
              { "@expression (function_call at 54:5) = AVG(t.deals)": [
                  { "@column (identifier at 54:9) = t.deals": [] } ] },
              { "@alias (identifier at 55:28) = revenue_core": [] },
              { "@expression (function_call at 55:5) = SUM(t.revenue_core)": [
                  { "@column (identifier at 55:9) = t.revenue_core": [] } ] },
              { "@alias (identifier at 56:27) = revenue_aux": [] },
              { "@expression (function_call at 56:5) = SUM(t.revenue_aux)": [
                  { "@column (identifier at 56:9) = t.revenue_aux": [] } ] },
              { "@alias (identifier at 57:23) = revenue": [] },
              { "@expression (function_call at 57:5) = SUM(t.revenue)": [
                  { "@column (identifier at 57:9) = t.revenue": [] } ] },
              { "@column (identifier at 52:5) = t.date_month": [] },
              { "@column (identifier at 53:5) = t.account_id": [] } ] },
          { "@grouping (group_by_clause at 72:1) = GROUP BY account_id,": [
              { "@column (identifier at 72:10) = account_id": [] },
              { "@column (identifier at 72:22) = date_month": [] } ] },
          { "@sources (from_clause at 58:1) = FROM ( SELECT dr.dat": [
              { "@alias (identifier at 71:42) = t": [] },
              { "@query (query_expr at 59:5) = SELECT dr.date_day, ": [
                  { "@columns (select_list at 60:9) = dr.date_day, DATE(da": [
                      { "@alias (identifier at 61:45) = date_month": [] },
                      { "@expression (function_call at 61:9) = DATE(date_day, 'star": [
                          { "@column (identifier at 61:14) = date_day": [] } ] },
                      { "@alias (identifier at 63:30) = deals": [] },
                      { "@expression (function_call at 63:9) = COUNT(ds.deal_id)": [
                          { "@column (identifier at 63:15) = ds.deal_id": [] } ] },
                      { "@alias (identifier at 64:37) = revenue_core": [] },
                      { "@expression (function_call at 64:9) = SUM(ds.revenue_core_": [
                          { "@column (identifier at 64:13) = ds.revenue_core_day": [] } ] },
                      { "@alias (identifier at 65:36) = revenue_aux": [] },
                      { "@expression (function_call at 65:9) = SUM(ds.revenue_aux_d": [
                          { "@column (identifier at 65:13) = ds.revenue_aux_day": [] } ] },
                      { "@alias (identifier at 66:32) = revenue": [] },
                      { "@expression (function_call at 66:9) = SUM(ds.revenue_day)": [
                          { "@column (identifier at 66:13) = ds.revenue_day": [] } ] },
                      { "@column (identifier at 60:9) = dr.date_day": [] },
                      { "@column (identifier at 62:9) = ds.account_id": [] } ] },
                  { "@grouping (group_by_clause at 71:5) = GROUP BY dr.date_day": [
                      { "@column (identifier at 71:14) = dr.date_day": [] },
                      { "@column (identifier at 71:27) = ds.account_id": [] } ] },
                  { "@sources (from_clause at 67:5) = FROM date_ranges dr ": [
                      { "@alias (identifier at 67:22) = dr": [] },
                      { "@table (identifier at 67:10) = date_ranges": [] },
                      { "@alias (identifier at 68:32) = ds": [] },
                      { "@table (identifier at 68:19) = deals_signed": [] },
                      { "@join (join_condition at 69:13) = ON dr.date_day >= da": [
                          { "@expression (binary_expression at 69:17) = dr.date_day >= date(": [
                              { "@column (identifier at 69:37) = ds.contract_start_da": [] },
                              { "@column (identifier at 69:17) = dr.date_day": [] },
                              { "@column (identifier at 70:37) = ds.contract_end_date": [] },
                              { "@column (identifier at 70:17) = dr.date_day": [] } ] } ] } ] } ] } ] } ] },
      { "@query (query_expr at 79:1) = SELECT t.*, CASE WHE": [
          { "@columns (select_list at 80:5) = t.*, CASE WHEN t.rev": [
              { "@alias (identifier at 86:12) = account_size": [] },
              { "@expression (casewhen_expression at 81:5) = CASE WHEN t.revenue_": [
                  { "@column (identifier at 82:14) = t.revenue_12m": [] },
                  { "@column (identifier at 83:14) = t.revenue_12m": [] },
                  { "@column (identifier at 83:38) = t.revenue_12m": [] },
                  { "@column (identifier at 84:14) = t.revenue_12m": [] } ] },
              { "@column (select_all at 80:5) = t.*": [] } ] },
          { "@sources (from_clause at 87:1) = FROM ( SELECT accoun": [
              { "@alias (identifier at 112:6) = t": [] },
              { "@query (query_expr at 88:5) = SELECT account_id, d": [
                  { "@columns (select_list at 89:9) = account_id, date_mon": [
                      { "@alias (identifier at 102:16) = region_cluster": [] },
                      { "@expression (casewhen_expression at 98:9) = CASE WHEN c.region I": [
                          { "@column (identifier at 100:18) = c.region": [] },
                          { "@column (identifier at 99:18) = c.region": [] } ] },
                      { "@alias (identifier at 108:14) = revenue_12m": [] },
                      { "@expression (function_call at 104:9) = SUM(revenue) OVER ( ": [
                          { "@column (identifier at 104:13) = revenue": [] },
                          { "@column (identifier at 105:26) = account_id": [] },
                          { "@ordering (order_by_clause at 106:13) = ORDER BY date_month": [
                              { "@column (identifier at 106:22) = date_month": [] } ] } ] },
                      { "@column (identifier at 103:9) = accounts.priority": [] },
                      { "@column (identifier at 89:9) = account_id": [] },
                      { "@column (identifier at 90:9) = date_month": [] },
                      { "@column (identifier at 91:9) = revenue": [] },
                      { "@column (identifier at 92:9) = revenue_core": [] },
                      { "@column (identifier at 93:9) = revenue_aux": [] },
                      { "@column (identifier at 94:9) = deals": [] },
                      { "@column (identifier at 95:9) = accounts.name": [] },
                      { "@column (identifier at 96:9) = accounts.industry": [] },
                      { "@column (identifier at 97:9) = accounts.country": [] } ] },
                  { "@sources (from_clause at 109:5) = FROM accounts_revenu": [
                      { "@alias (identifier at 111:29) = c": [] },
                      { "@table (identifier at 111:19) = countries": [] },
                      { "@table (identifier at 109:10) = accounts_revenue": [] },
                      { "@table (identifier at 110:14) = accounts": [] },
                      { "@join (join_condition at 110:23) = USING (account_id)": [
                          { "@column (identifier at 110:30) = account_id": [] } ] },
                      { "@join (join_condition at 111:31) = USING (country)": [
                          { "@column (identifier at 111:38) = country": [] } ] } ] } ] } ] } ] },
      { "@scope (query_expr at 7:1) = WITH RECURSIVE date_": [
          { "@columns (select_list at 18:5) = date_day": [
              { "@column (identifier at 18:5) = date_day": [] } ] },
          { "@grouping (group_by_clause at 20:1) = GROUP BY date_day": [
              { "@column (identifier at 20:10) = date_day": [] } ] },
          { "@sources (from_clause at 19:1) = FROM date_ranges": [
              { "@table (identifier at 19:6) = date_ranges": [] } ] },
          { "@scope (query_expr at 8:5) = SELECT date(MIN(CASE": [
              { "@query (query_expr at 12:5) = SELECT date(date_day": [
                  { "@columns (select_list at 13:9) = date(date_day, '+1 d": [
                      { "@expression (function_call at 13:9) = date(date_day, '+1 d": [
                          { "@column (identifier at 13:14) = date_day": [] } ] } ] },
                  { "@filter (where_clause at 15:5) = WHERE date_day < (SE": [
                      { "@query (query_expr at 15:23) = SELECT date(MAX(CASE": [
                          { "@columns (select_list at 15:30) = date(MAX(CASE WHEN d": [
                              { "@expression (function_call at 15:30) = date(MAX(CASE WHEN d": [
                                  { "@column (identifier at 15:114) = d.stage_date": [] },
                                  { "@column (identifier at 15:49) = d.contract_end_date": [] },
                                  { "@column (identifier at 15:71) = d.stage_date": [] },
                                  { "@column (identifier at 15:89) = d.contract_end_date": [] } ] } ] },
                          { "@sources (from_clause at 15:133) = FROM deals d": [
                              { "@alias (identifier at 15:144) = d": [] },
                              { "@table (identifier at 15:138) = deals": [] } ] } ] },
                      { "@column (identifier at 15:11) = date_day": [] } ] },
                  { "@sources (from_clause at 14:5) = FROM date_ranges": [
                      { "@table (identifier at 14:10) = date_ranges": [] } ] } ] },
              { "@query (query_expr at 8:5) = SELECT date(MIN(CASE": [
                  { "@columns (select_list at 9:9) = date(MIN(CASE WHEN d": [
                      { "@alias (identifier at 9:119) = date_month": [] },
                      { "@expression (function_call at 9:9) = date(MIN(CASE WHEN d": [
                          { "@column (identifier at 9:28) = d.stage_date": [] },
                          { "@column (identifier at 9:43) = d.contract_start_dat": [] },
                          { "@column (identifier at 9:70) = d.stage_date": [] },
                          { "@column (identifier at 9:88) = d.contract_start_dat": [] } ] } ] },
                  { "@sources (from_clause at 10:5) = FROM deals d": [
                      { "@alias (identifier at 10:16) = d": [] },
                      { "@table (identifier at 10:10) = deals": [] } ] } ] } ] } ] } ] } ]
```

### src.sql.parse (call 2)

```json
[
  { "@root (source_file at 1:1) = -- REVENUE REPORTS -": [
      { "@query (query_expr at 30:1) = SELECT accounts.name": [
          { "@columns (select_list at 31:5) = accounts.name, regio": [
              { "@alias (identifier at 37:12) = cluster": [] },
              { "@expression (casewhen_expression at 33:5) = CASE WHEN c.region I": [
                  { "@column (identifier at 34:14) = c.region": [] },
                  { "@column (identifier at 35:14) = c.region": [] } ] },
              { "@alias (identifier at 38:26) = industry": [] },
              { "@column (identifier at 38:5) = accounts.industry": [] },
              { "@alias (identifier at 39:75) = industry_tech": [] },
              { "@expression (function_call at 39:5) = IIF(accounts.industr": [
                  { "@column (identifier at 39:9) = accounts.industry": [] } ] },
              { "@alias (identifier at 45:12) = account_size": [] },
              { "@expression (casewhen_expression at 40:5) = CASE WHEN SUM(accoun": [
                  { "@column (identifier at 41:18) = accounts_revenue.rev": [] },
                  { "@column (identifier at 42:18) = accounts_revenue.rev": [] },
                  { "@column (identifier at 42:58) = accounts_revenue.rev": [] },
                  { "@column (identifier at 43:18) = accounts_revenue.rev": [] } ] },
              { "@alias (identifier at 46:38) = revenue_12m": [] },
              { "@expression (function_call at 46:5) = SUM(accounts_revenue": [
                  { "@column (identifier at 46:9) = accounts_revenue.rev": [] } ] },
              { "@column (identifier at 31:5) = accounts.name": [] },
              { "@column (identifier at 32:5) = region": [] } ] },
          { "@filter (where_clause at 50:1) = WHERE accounts_reven": [
              { "@column (identifier at 50:7) = accounts_revenue.dat": [] } ] },
          { "@grouping (group_by_clause at 51:1) = GROUP BY accounts.na": [
              { "@column (identifier at 51:10) = accounts.name": [] },
              { "@column (identifier at 51:25) = region": [] },
              { "@column (identifier at 51:33) = accounts.industry": [] } ] },
          { "@sources (from_clause at 47:1) = FROM accounts LEFT J": [
              { "@alias (identifier at 49:25) = c": [] },
              { "@table (identifier at 49:15) = countries": [] },
              { "@table (identifier at 47:6) = accounts": [] },
              { "@table (identifier at 48:15) = accounts_revenue": [] },
              { "@join (join_condition at 48:32) = USING (account_id)": [
                  { "@column (identifier at 48:39) = account_id": [] } ] },
              { "@join (join_condition at 49:27) = USING (country)": [
                  { "@column (identifier at 49:34) = country": [] } ] } ] } ] },
      { "@query (query_expr at 5:1) = SELECT date(date_mon": [
          { "@columns (select_list at 6:5) = date(date_month, 'st": [
              { "@alias (identifier at 11:12) = region_cluster": [] },
              { "@expression (casewhen_expression at 7:5) = CASE WHEN c.region I": [
                  { "@column (identifier at 8:14) = c.region": [] },
                  { "@column (identifier at 9:14) = c.region": [] } ] },
              { "@alias (identifier at 16:12) = industry_cluster": [] },
              { "@expression (casewhen_expression at 12:5) = CASE WHEN a.industry": [
                  { "@column (identifier at 13:14) = a.industry": [] },
                  { "@column (identifier at 14:14) = a.industry": [] } ] },
              { "@alias (identifier at 18:24) = revenue": [] },
              { "@expression (function_call at 18:5) = SUM(ar.revenue)": [
                  { "@column (identifier at 18:9) = ar.revenue": [] } ] },
              { "@alias (identifier at 19:38) = accounts": [] },
              { "@expression (function_call at 19:5) = COUNT(DISTINCT ar.ac": [
                  { "@column (identifier at 19:20) = ar.account_id": [] } ] },
              { "@alias (identifier at 20:56) = revenue_per_account": [] },
              { "@expression (binary_expression at 20:5) = SUM(ar.revenue) / CO": [
                  { "@column (identifier at 20:38) = ar.account_id": [] },
                  { "@column (identifier at 20:9) = ar.revenue": [] } ] },
              { "@alias (identifier at 6:42) = date_year": [] },
              { "@expression (function_call at 6:5) = date(date_month, 'st": [
                  { "@column (identifier at 6:10) = date_month": [] } ] },
              { "@column (identifier at 17:5) = a360.account_size": [] } ] },
          { "@grouping (group_by_clause at 25:1) = GROUP BY date_year, ": [
              { "@column (identifier at 25:10) = date_year": [] },
              { "@column (identifier at 25:21) = region_cluster": [] },
              { "@column (identifier at 25:37) = industry_cluster": [] },
              { "@column (identifier at 25:55) = a360.account_size": [] } ] },
          { "@sources (from_clause at 21:1) = FROM accounts_revenu": [
              { "@alias (identifier at 21:23) = ar": [] },
              { "@table (identifier at 21:6) = accounts_revenue": [] },
              { "@alias (identifier at 22:24) = a": [] },
              { "@table (identifier at 22:15) = accounts": [] },
              { "@join (join_condition at 22:26) = USING (account_id)": [
                  { "@column (identifier at 22:33) = account_id": [] } ] },
              { "@alias (identifier at 23:25) = c": [] },
              { "@table (identifier at 23:15) = countries": [] },
              { "@join (join_condition at 23:27) = USING (country)": [
                  { "@column (identifier at 23:34) = country": [] } ] },
              { "@alias (identifier at 24:28) = a360": [] },
              { "@table (identifier at 24:15) = accounts_360": [] },
              { "@join (join_condition at 24:33) = USING (account_id, d": [
                  { "@column (identifier at 24:40) = account_id": [] },
                  { "@column (identifier at 24:52) = date_month": [] } ] } ] },
          { "@ordering (order_by_clause at 26:1) = ORDER BY date_year, ": [
              { "@column (identifier at 26:10) = date_year": [] },
              { "@column (identifier at 26:21) = region_cluster": [] },
              { "@column (identifier at 26:37) = industry_cluster": [] } ] } ] } ] } ]
```

### src.sql.parse (call 3)

```json
[
  { "@root (source_file at 1:1) = -- FOUNDATIONAL TABL": [
      { "@query (query_expr at 26:1) = SELECT *, revenue / ": [
          { "@columns (select_list at 27:5) = *, revenue / contrac": [
              { "@alias (identifier at 28:41) = revenue_day": [] },
              { "@expression (binary_expression at 28:5) = revenue / contract_d": [
                  { "@column (identifier at 28:15) = contract_duration_da": [] },
                  { "@column (identifier at 28:5) = revenue": [] } ] },
              { "@alias (identifier at 29:46) = revenue_core_day": [] },
              { "@expression (binary_expression at 29:5) = revenue_core / contr": [
                  { "@column (identifier at 29:20) = contract_duration_da": [] },
                  { "@column (identifier at 29:5) = revenue_core": [] } ] },
              { "@alias (identifier at 30:45) = revenue_aux_day": [] },
              { "@expression (binary_expression at 30:5) = revenue_aux / contra": [
                  { "@column (identifier at 30:19) = contract_duration_da": [] },
                  { "@column (identifier at 30:5) = revenue_aux": [] } ] },
              { "@column (select_all at 27:5) = *": [] } ] },
          { "@sources (from_clause at 31:1) = FROM ( SELECT d.deal": [
              { "@alias (identifier at 45:6) = t": [] },
              { "@query (query_expr at 32:5) = SELECT d.deal_id, d.": [
                  { "@columns (select_list at 33:9) = d.deal_id, d.account": [
                      { "@alias (identifier at 37:82) = contract_duration_da": [] },
                      { "@expression (binary_expression at 37:9) = julianday(d.contract": [
                          { "@column (identifier at 37:19) = d.contract_end_date": [] },
                          { "@column (identifier at 37:52) = d.contract_start_dat": [] } ] },
                      { "@alias (identifier at 38:110) = revenue_core": [] },
                      { "@expression (function_call at 38:9) = SUM(CASE WHEN o.prod": [
                          { "@column (identifier at 38:23) = o.product": [] },
                          { "@column (identifier at 38:87) = o.value": [] } ] },
                      { "@alias (identifier at 39:91) = revenue_aux": [] },
                      { "@expression (function_call at 39:9) = SUM(CASE WHEN o.prod": [
                          { "@column (identifier at 39:23) = o.product": [] },
                          { "@column (identifier at 39:68) = o.value": [] } ] },
                      { "@alias (identifier at 40:25) = revenue": [] },
                      { "@expression (function_call at 40:9) = SUM(o.value)": [
                          { "@column (identifier at 40:13) = o.value": [] } ] },
                      { "@column (identifier at 33:9) = d.deal_id": [] },
                      { "@column (identifier at 34:9) = d.account_id": [] },
                      { "@column (identifier at 35:9) = d.contract_start_dat": [] },
                      { "@column (identifier at 36:9) = d.contract_end_date": [] } ] },
                  { "@filter (where_clause at 43:5) = WHERE d.stage = 4": [
                      { "@column (identifier at 43:11) = d.stage": [] } ] },
                  { "@grouping (group_by_clause at 44:5) = GROUP BY d.deal_id, ": [
                      { "@column (identifier at 44:14) = d.deal_id": [] },
                      { "@column (identifier at 44:25) = d.account_id": [] },
                      { "@column (identifier at 44:39) = d.contract_start_dat": [] },
                      { "@column (identifier at 44:62) = d.contract_end_date": [] } ] },
                  { "@sources (from_clause at 41:5) = FROM orders o JOIN d": [
                      { "@alias (identifier at 41:17) = o": [] },
                      { "@table (identifier at 41:10) = orders": [] },
                      { "@alias (identifier at 42:20) = d": [] },
                      { "@table (identifier at 42:14) = deals": [] },
                      { "@join (join_condition at 42:22) = USING (deal_id, orde": [
                          { "@column (identifier at 42:29) = deal_id": [] },
                          { "@column (identifier at 42:38) = order_id": [] } ] } ] } ] } ] } ] },
      { "@query (query_expr at 51:1) = SELECT t.date_month,": [
          { "@columns (select_list at 52:5) = t.date_month, t.acco": [
              { "@alias (identifier at 54:21) = deals": [] },
              { "@expression (function_call at 54:5) = AVG(t.deals)": [
                  { "@column (identifier at 54:9) = t.deals": [] } ] },
              { "@alias (identifier at 55:28) = revenue_core": [] },
              { "@expression (function_call at 55:5) = SUM(t.revenue_core)": [
                  { "@column (identifier at 55:9) = t.revenue_core": [] } ] },
              { "@alias (identifier at 56:27) = revenue_aux": [] },
              { "@expression (function_call at 56:5) = SUM(t.revenue_aux)": [
                  { "@column (identifier at 56:9) = t.revenue_aux": [] } ] },
              { "@alias (identifier at 57:23) = revenue": [] },
              { "@expression (function_call at 57:5) = SUM(t.revenue)": [
                  { "@column (identifier at 57:9) = t.revenue": [] } ] },
              { "@column (identifier at 52:5) = t.date_month": [] },
              { "@column (identifier at 53:5) = t.account_id": [] } ] },
          { "@grouping (group_by_clause at 72:1) = GROUP BY account_id,": [
              { "@column (identifier at 72:10) = account_id": [] },
              { "@column (identifier at 72:22) = date_month": [] } ] },
          { "@sources (from_clause at 58:1) = FROM ( SELECT dr.dat": [
              { "@alias (identifier at 71:42) = t": [] },
              { "@query (query_expr at 59:5) = SELECT dr.date_day, ": [
                  { "@columns (select_list at 60:9) = dr.date_day, DATE(da": [
                      { "@alias (identifier at 61:45) = date_month": [] },
                      { "@expression (function_call at 61:9) = DATE(date_day, 'star": [
                          { "@column (identifier at 61:14) = date_day": [] } ] },
                      { "@alias (identifier at 63:30) = deals": [] },
                      { "@expression (function_call at 63:9) = COUNT(ds.deal_id)": [
                          { "@column (identifier at 63:15) = ds.deal_id": [] } ] },
                      { "@alias (identifier at 64:37) = revenue_core": [] },
                      { "@expression (function_call at 64:9) = SUM(ds.revenue_core_": [
                          { "@column (identifier at 64:13) = ds.revenue_core_day": [] } ] },
                      { "@alias (identifier at 65:36) = revenue_aux": [] },
                      { "@expression (function_call at 65:9) = SUM(ds.revenue_aux_d": [
                          { "@column (identifier at 65:13) = ds.revenue_aux_day": [] } ] },
                      { "@alias (identifier at 66:32) = revenue": [] },
                      { "@expression (function_call at 66:9) = SUM(ds.revenue_day)": [
                          { "@column (identifier at 66:13) = ds.revenue_day": [] } ] },
                      { "@column (identifier at 60:9) = dr.date_day": [] },
                      { "@column (identifier at 62:9) = ds.account_id": [] } ] },
                  { "@grouping (group_by_clause at 71:5) = GROUP BY dr.date_day": [
                      { "@column (identifier at 71:14) = dr.date_day": [] },
                      { "@column (identifier at 71:27) = ds.account_id": [] } ] },
                  { "@sources (from_clause at 67:5) = FROM date_ranges dr ": [
                      { "@alias (identifier at 67:22) = dr": [] },
                      { "@table (identifier at 67:10) = date_ranges": [] },
                      { "@alias (identifier at 68:32) = ds": [] },
                      { "@table (identifier at 68:19) = deals_signed": [] },
                      { "@join (join_condition at 69:13) = ON dr.date_day >= da": [
                          { "@expression (binary_expression at 69:17) = dr.date_day >= date(": [
                              { "@column (identifier at 69:37) = ds.contract_start_da": [] },
                              { "@column (identifier at 69:17) = dr.date_day": [] },
                              { "@column (identifier at 70:37) = ds.contract_end_date": [] },
                              { "@column (identifier at 70:17) = dr.date_day": [] } ] } ] } ] } ] } ] } ] },
      { "@query (query_expr at 79:1) = SELECT t.*, CASE WHE": [
          { "@columns (select_list at 80:5) = t.*, CASE WHEN t.rev": [
              { "@alias (identifier at 86:12) = account_size": [] },
              { "@expression (casewhen_expression at 81:5) = CASE WHEN t.revenue_": [
                  { "@column (identifier at 82:14) = t.revenue_12m": [] },
                  { "@column (identifier at 83:14) = t.revenue_12m": [] },
                  { "@column (identifier at 83:38) = t.revenue_12m": [] },
                  { "@column (identifier at 84:14) = t.revenue_12m": [] } ] },
              { "@column (select_all at 80:5) = t.*": [] } ] },
          { "@sources (from_clause at 87:1) = FROM ( SELECT accoun": [
              { "@alias (identifier at 112:6) = t": [] },
              { "@query (query_expr at 88:5) = SELECT account_id, d": [
                  { "@columns (select_list at 89:9) = account_id, date_mon": [
                      { "@alias (identifier at 102:16) = region_cluster": [] },
                      { "@expression (casewhen_expression at 98:9) = CASE WHEN c.region I": [
                          { "@column (identifier at 100:18) = c.region": [] },
                          { "@column (identifier at 99:18) = c.region": [] } ] },
                      { "@alias (identifier at 108:14) = revenue_12m": [] },
                      { "@expression (function_call at 104:9) = SUM(revenue) OVER ( ": [
                          { "@column (identifier at 104:13) = revenue": [] },
                          { "@column (identifier at 105:26) = account_id": [] },
                          { "@ordering (order_by_clause at 106:13) = ORDER BY date_month": [
                              { "@column (identifier at 106:22) = date_month": [] } ] } ] },
                      { "@column (identifier at 103:9) = accounts.priority": [] },
                      { "@column (identifier at 89:9) = account_id": [] },
                      { "@column (identifier at 90:9) = date_month": [] },
                      { "@column (identifier at 91:9) = revenue": [] },
                      { "@column (identifier at 92:9) = revenue_core": [] },
                      { "@column (identifier at 93:9) = revenue_aux": [] },
                      { "@column (identifier at 94:9) = deals": [] },
                      { "@column (identifier at 95:9) = accounts.name": [] },
                      { "@column (identifier at 96:9) = accounts.industry": [] },
                      { "@column (identifier at 97:9) = accounts.country": [] } ] },
                  { "@sources (from_clause at 109:5) = FROM accounts_revenu": [
                      { "@alias (identifier at 111:29) = c": [] },
                      { "@table (identifier at 111:19) = countries": [] },
                      { "@table (identifier at 109:10) = accounts_revenue": [] },
                      { "@table (identifier at 110:14) = accounts": [] },
                      { "@join (join_condition at 110:23) = USING (account_id)": [
                          { "@column (identifier at 110:30) = account_id": [] } ] },
                      { "@join (join_condition at 111:31) = USING (country)": [
                          { "@column (identifier at 111:38) = country": [] } ] } ] } ] } ] } ] },
      { "@scope (query_expr at 7:1) = WITH RECURSIVE date_": [
          { "@columns (select_list at 18:5) = date_day": [
              { "@column (identifier at 18:5) = date_day": [] } ] },
          { "@grouping (group_by_clause at 20:1) = GROUP BY date_day": [
              { "@column (identifier at 20:10) = date_day": [] } ] },
          { "@sources (from_clause at 19:1) = FROM date_ranges": [
              { "@table (identifier at 19:6) = date_ranges": [] } ] },
          { "@scope (query_expr at 8:5) = SELECT date(MIN(CASE": [
              { "@query (query_expr at 12:5) = SELECT date(date_day": [
                  { "@columns (select_list at 13:9) = date(date_day, '+1 d": [
                      { "@expression (function_call at 13:9) = date(date_day, '+1 d": [
                          { "@column (identifier at 13:14) = date_day": [] } ] } ] },
                  { "@filter (where_clause at 15:5) = WHERE date_day < (SE": [
                      { "@query (query_expr at 15:23) = SELECT date(MAX(CASE": [
                          { "@columns (select_list at 15:30) = date(MAX(CASE WHEN d": [
                              { "@expression (function_call at 15:30) = date(MAX(CASE WHEN d": [
                                  { "@column (identifier at 15:114) = d.stage_date": [] },
                                  { "@column (identifier at 15:49) = d.contract_end_date": [] },
                                  { "@column (identifier at 15:71) = d.stage_date": [] },
                                  { "@column (identifier at 15:89) = d.contract_end_date": [] } ] } ] },
                          { "@sources (from_clause at 15:133) = FROM deals d": [
                              { "@alias (identifier at 15:144) = d": [] },
                              { "@table (identifier at 15:138) = deals": [] } ] } ] },
                      { "@column (identifier at 15:11) = date_day": [] } ] },
                  { "@sources (from_clause at 14:5) = FROM date_ranges": [
                      { "@table (identifier at 14:10) = date_ranges": [] } ] } ] },
              { "@query (query_expr at 8:5) = SELECT date(MIN(CASE": [
                  { "@columns (select_list at 9:9) = date(MIN(CASE WHEN d": [
                      { "@alias (identifier at 9:119) = date_month": [] },
                      { "@expression (function_call at 9:9) = date(MIN(CASE WHEN d": [
                          { "@column (identifier at 9:28) = d.stage_date": [] },
                          { "@column (identifier at 9:43) = d.contract_start_dat": [] },
                          { "@column (identifier at 9:70) = d.stage_date": [] },
                          { "@column (identifier at 9:88) = d.contract_start_dat": [] } ] } ] },
                  { "@sources (from_clause at 10:5) = FROM deals d": [
                      { "@alias (identifier at 10:16) = d": [] },
                      { "@table (identifier at 10:10) = deals": [] } ] } ] } ] } ] } ] } ]
```

### src.sql.parse (call 4)

```json
[
  { "@root (source_file at 1:1) = -- REVENUE REPORTS -": [
      { "@query (query_expr at 30:1) = SELECT accounts.name": [
          { "@columns (select_list at 31:5) = accounts.name, regio": [
              { "@alias (identifier at 37:12) = cluster": [] },
              { "@expression (casewhen_expression at 33:5) = CASE WHEN c.region I": [
                  { "@column (identifier at 34:14) = c.region": [] },
                  { "@column (identifier at 35:14) = c.region": [] } ] },
              { "@alias (identifier at 38:26) = industry": [] },
              { "@column (identifier at 38:5) = accounts.industry": [] },
              { "@alias (identifier at 39:75) = industry_tech": [] },
              { "@expression (function_call at 39:5) = IIF(accounts.industr": [
                  { "@column (identifier at 39:9) = accounts.industry": [] } ] },
              { "@alias (identifier at 45:12) = account_size": [] },
              { "@expression (casewhen_expression at 40:5) = CASE WHEN SUM(accoun": [
                  { "@column (identifier at 41:18) = accounts_revenue.rev": [] },
                  { "@column (identifier at 42:18) = accounts_revenue.rev": [] },
                  { "@column (identifier at 42:58) = accounts_revenue.rev": [] },
                  { "@column (identifier at 43:18) = accounts_revenue.rev": [] } ] },
              { "@alias (identifier at 46:38) = revenue_12m": [] },
              { "@expression (function_call at 46:5) = SUM(accounts_revenue": [
                  { "@column (identifier at 46:9) = accounts_revenue.rev": [] } ] },
              { "@column (identifier at 31:5) = accounts.name": [] },
              { "@column (identifier at 32:5) = region": [] } ] },
          { "@filter (where_clause at 50:1) = WHERE accounts_reven": [
              { "@column (identifier at 50:7) = accounts_revenue.dat": [] } ] },
          { "@grouping (group_by_clause at 51:1) = GROUP BY accounts.na": [
              { "@column (identifier at 51:10) = accounts.name": [] },
              { "@column (identifier at 51:25) = region": [] },
              { "@column (identifier at 51:33) = accounts.industry": [] } ] },
          { "@sources (from_clause at 47:1) = FROM accounts LEFT J": [
              { "@alias (identifier at 49:25) = c": [] },
              { "@table (identifier at 49:15) = countries": [] },
              { "@table (identifier at 47:6) = accounts": [] },
              { "@table (identifier at 48:15) = accounts_revenue": [] },
              { "@join (join_condition at 48:32) = USING (account_id)": [
                  { "@column (identifier at 48:39) = account_id": [] } ] },
              { "@join (join_condition at 49:27) = USING (country)": [
                  { "@column (identifier at 49:34) = country": [] } ] } ] } ] },
      { "@query (query_expr at 5:1) = SELECT date(date_mon": [
          { "@columns (select_list at 6:5) = date(date_month, 'st": [
              { "@alias (identifier at 11:12) = region_cluster": [] },
              { "@expression (casewhen_expression at 7:5) = CASE WHEN c.region I": [
                  { "@column (identifier at 8:14) = c.region": [] },
                  { "@column (identifier at 9:14) = c.region": [] } ] },
              { "@alias (identifier at 16:12) = industry_cluster": [] },
              { "@expression (casewhen_expression at 12:5) = CASE WHEN a.industry": [
                  { "@column (identifier at 13:14) = a.industry": [] },
                  { "@column (identifier at 14:14) = a.industry": [] } ] },
              { "@alias (identifier at 18:24) = revenue": [] },
              { "@expression (function_call at 18:5) = SUM(ar.revenue)": [
                  { "@column (identifier at 18:9) = ar.revenue": [] } ] },
              { "@alias (identifier at 19:38) = accounts": [] },
              { "@expression (function_call at 19:5) = COUNT(DISTINCT ar.ac": [
                  { "@column (identifier at 19:20) = ar.account_id": [] } ] },
              { "@alias (identifier at 20:56) = revenue_per_account": [] },
              { "@expression (binary_expression at 20:5) = SUM(ar.revenue) / CO": [
                  { "@column (identifier at 20:38) = ar.account_id": [] },
                  { "@column (identifier at 20:9) = ar.revenue": [] } ] },
              { "@alias (identifier at 6:42) = date_year": [] },
              { "@expression (function_call at 6:5) = date(date_month, 'st": [
                  { "@column (identifier at 6:10) = date_month": [] } ] },
              { "@column (identifier at 17:5) = a360.account_size": [] } ] },
          { "@grouping (group_by_clause at 25:1) = GROUP BY date_year, ": [
              { "@column (identifier at 25:10) = date_year": [] },
              { "@column (identifier at 25:21) = region_cluster": [] },
              { "@column (identifier at 25:37) = industry_cluster": [] },
              { "@column (identifier at 25:55) = a360.account_size": [] } ] },
          { "@sources (from_clause at 21:1) = FROM accounts_revenu": [
              { "@alias (identifier at 21:23) = ar": [] },
              { "@table (identifier at 21:6) = accounts_revenue": [] },
              { "@alias (identifier at 22:24) = a": [] },
              { "@table (identifier at 22:15) = accounts": [] },
              { "@join (join_condition at 22:26) = USING (account_id)": [
                  { "@column (identifier at 22:33) = account_id": [] } ] },
              { "@alias (identifier at 23:25) = c": [] },
              { "@table (identifier at 23:15) = countries": [] },
              { "@join (join_condition at 23:27) = USING (country)": [
                  { "@column (identifier at 23:34) = country": [] } ] },
              { "@alias (identifier at 24:28) = a360": [] },
              { "@table (identifier at 24:15) = accounts_360": [] },
              { "@join (join_condition at 24:33) = USING (account_id, d": [
                  { "@column (identifier at 24:40) = account_id": [] },
                  { "@column (identifier at 24:52) = date_month": [] } ] } ] },
          { "@ordering (order_by_clause at 26:1) = ORDER BY date_year, ": [
              { "@column (identifier at 26:10) = date_year": [] },
              { "@column (identifier at 26:21) = region_cluster": [] },
              { "@column (identifier at 26:37) = industry_cluster": [] } ] } ] } ] } ]
```

### src.sql.parse (call 5)

```json
[
  { "@root (source_file at 1:1) = -- CASE: Different g": [
      { "@query (query_expr at 3:1) = SELECT date(date_mon": [
          { "@columns (select_list at 4:5) = date(date_month, 'st": [
              { "@alias (identifier at 11:12) = macro_region": [] },
              { "@expression (casewhen_expression at 6:5) = CASE WHEN c.region I": [
                  { "@column (identifier at 7:14) = c.region": [] },
                  { "@column (identifier at 8:14) = c.region": [] },
                  { "@column (identifier at 9:14) = c.region": [] } ] },
              { "@alias (identifier at 13:67) = industry_it": [] },
              { "@expression (function_call at 13:5) = IIF(a.industry = 'In": [
                  { "@column (identifier at 13:9) = a.industry": [] } ] },
              { "@alias (identifier at 14:24) = revenue": [] },
              { "@expression (function_call at 14:5) = SUM(ar.revenue)": [
                  { "@column (identifier at 14:9) = ar.revenue": [] } ] },
              { "@alias (identifier at 15:38) = accounts": [] },
              { "@expression (function_call at 15:5) = COUNT(DISTINCT ar.ac": [
                  { "@column (identifier at 15:20) = ar.account_id": [] } ] },
              { "@alias (identifier at 16:56) = revenue_per_account": [] },
              { "@expression (binary_expression at 16:5) = SUM(ar.revenue) / CO": [
                  { "@column (identifier at 16:38) = ar.account_id": [] },
                  { "@column (identifier at 16:9) = ar.revenue": [] } ] },
              { "@alias (identifier at 4:42) = date_year": [] },
              { "@expression (function_call at 4:5) = date(date_month, 'st": [
                  { "@column (identifier at 4:10) = date_month": [] } ] } ] },
          { "@filter (where_clause at 20:1) = WHERE -- This is app": [
              { "@column (identifier at 22:5) = a.industry": [] },
              { "@column (identifier at 24:9) = date_month": [] } ] },
          { "@grouping (group_by_clause at 25:1) = GROUP BY date_year, ": [
              { "@column (identifier at 25:10) = date_year": [] },
              { "@column (identifier at 25:21) = macro_region": [] },
              { "@column (identifier at 25:35) = industry_it": [] } ] },
          { "@sources (from_clause at 17:1) = FROM accounts_revenu": [
              { "@alias (identifier at 17:23) = ar": [] },
              { "@table (identifier at 17:6) = accounts_revenue": [] },
              { "@alias (identifier at 18:24) = a": [] },
              { "@table (identifier at 18:15) = accounts": [] },
              { "@join (join_condition at 18:26) = USING (account_id)": [
                  { "@column (identifier at 18:33) = account_id": [] } ] },
              { "@alias (identifier at 19:25) = c": [] },
              { "@table (identifier at 19:15) = countries": [] },
              { "@join (join_condition at 19:27) = USING (country)": [
                  { "@column (identifier at 19:34) = country": [] } ] } ] } ] } ] } ]
```

### src.code.ingest_file (call 1)

```json
{
  "Tree(./tests/inputs/codebase/0-accounts.sql)": {
    "files": {
      "./tests/inputs/codebase/0-accounts.sql": [
        { "Query(./tests/inputs/codebase/0-accounts.sql:25:0-44:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
                  "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                        "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                        "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                        "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [ "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                        "sql": "SUM(o.value)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
                  "alias": "revenue_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
                  "sql": "revenue / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
                  "alias": "revenue_core_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
                  "sql": "revenue_core / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
                  "alias": "revenue_aux_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
                  "sql": "revenue_aux / contract_duration_days" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:25:0-44:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:50:0-71:31)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
                  "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [ "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                        "sql": "DATE(date_day, 'start of month')" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [ "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                        "sql": "COUNT(ds.deal_id)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                        "sql": "SUM(ds.revenue_core_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                        "sql": "SUM(ds.revenue_aux_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                        "sql": "SUM(ds.revenue_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                        "alias": null,
                        "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                        "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [ "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
                  "sql": "AVG(t.deals)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [ "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
                  "sql": "SUM(t.revenue_core)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [ "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
                  "sql": "SUM(t.revenue_aux)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [ "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
                  "sql": "SUM(t.revenue)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:50:0-71:31" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:78:0-111:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
                  "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [ "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                        "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                        "alias": "revenue_12m",
                        "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                        "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
                  "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:78:0-111:6" } } ] },
    "index": {
      "<Column>": [ "Column(?.?.*)", "Column(?.?.account_id)", "Column(?.?.contract_duration_days)", "Column(?.?.date_day)", "Column(?.?.date_month)", "Column(?.?.deal_id)", "Column(?.?.order_id)", "Column(?.?.revenue)", "Column(?.?.revenue_aux)", "Column(?.?.revenue_core)", "Column(?.accounts.account_id)", "Column(?.accounts.country)", "Column(?.accounts.date_month)", "Column(?.accounts.deals)", "Column(?.accounts.industry)", "Column(?.accounts.name)", "Column(?.accounts.priority)", "Column(?.accounts.revenue)", "Column(?.accounts.revenue_aux)", "Column(?.accounts.revenue_core)", "Column(?.countries.region)", "Column(?.date_ranges.date_day)", "Column(?.deals.account_id)", "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)", "Column(?.deals.deal_id)", "Column(?.deals.stage)", "Column(?.deals_signed.account_id)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)", "Column(?.deals_signed.deal_id)", "Column(?.deals_signed.revenue_aux_day)", "Column(?.deals_signed.revenue_core_day)", "Column(?.deals_signed.revenue_day)", "Column(?.orders.product)", "Column(?.orders.value)", "Column(?.t.*)", "Column(?.t.account_id)", "Column(?.t.date_month)", "Column(?.t.deals)", "Column(?.t.revenue)", "Column(?.t.revenue_12m)", "Column(?.t.revenue_aux)", "Column(?.t.revenue_core)" ],
      "<Expression>": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
      "<Table>": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)", "Table(?.date_ranges as dr)", "Table(?.deals as d)", "Table(?.deals_signed as ds)", "Table(?.orders as o)" ],
      "<Query>": [
        { "Query(./tests/inputs/codebase/0-accounts.sql:25:0-44:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
                  "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                        "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                        "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                        "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [ "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                        "sql": "SUM(o.value)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
                  "alias": "revenue_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
                  "sql": "revenue / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
                  "alias": "revenue_core_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
                  "sql": "revenue_core / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
                  "alias": "revenue_aux_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
                  "sql": "revenue_aux / contract_duration_days" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:25:0-44:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
            "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                  "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                  "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                  "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                  "alias": "contract_duration_days",
                  "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                  "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                  "columns": [ "Column(?.orders.value)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                  "sql": "SUM(o.value)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:50:0-71:31)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
                  "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [ "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                        "sql": "DATE(date_day, 'start of month')" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [ "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                        "sql": "COUNT(ds.deal_id)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                        "sql": "SUM(ds.revenue_core_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                        "sql": "SUM(ds.revenue_aux_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                        "sql": "SUM(ds.revenue_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                        "alias": null,
                        "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                        "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [ "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
                  "sql": "AVG(t.deals)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [ "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
                  "sql": "SUM(t.revenue_core)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [ "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
                  "sql": "SUM(t.revenue_aux)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [ "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
                  "sql": "SUM(t.revenue)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:50:0-71:31" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
            "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                  "columns": [ "Column(?.?.date_day)" ],
                  "alias": "date_month",
                  "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                  "sql": "DATE(date_day, 'start of month')" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                  "columns": [ "Column(?.deals_signed.deal_id)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                  "sql": "COUNT(ds.deal_id)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                  "sql": "SUM(ds.revenue_core_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                  "sql": "SUM(ds.revenue_aux_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_day)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                  "sql": "SUM(ds.revenue_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                  "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                  "alias": null,
                  "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                  "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:78:0-111:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
                  "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [ "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                        "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                        "alias": "revenue_12m",
                        "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                        "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
                  "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:78:0-111:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
            "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                  "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                  "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                  "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ] },
    "map_key_to_expr": {
      "('Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue_core)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue_aux)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } } ],
      "('Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))', ['Column(?.deals.contract_end_date)', 'Column(?.deals.contract_start_date)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))\", ['Column(?.orders.product)', 'Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))\", ['Column(?.orders.product)', 'Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.orders.value))))', ['Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.deals))))', ['Column(?.t.deals)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))', ['Column(?.t.revenue_core)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))', ['Column(?.t.revenue_aux)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))', ['Column(?.t.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))\", ['Column(?.?.date_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))', ['Column(?.deals_signed.deal_id)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))', ['Column(?.deals_signed.revenue_core_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))', ['Column(?.deals_signed.revenue_aux_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))', ['Column(?.deals_signed.revenue_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } } ],
      "('Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))', ['Column(?.date_ranges.date_day)', 'Column(?.deals_signed.contract_end_date)', 'Column(?.deals_signed.contract_start_date)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))\", ['Column(?.t.revenue_12m)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))\", ['Column(?.countries.region)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))', ['Column(?.accounts.account_id)', 'Column(?.accounts.date_month)', 'Column(?.accounts.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ] },
    "map_file_to_expr": {
      "./tests/inputs/codebase/0-accounts.sql": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ] } } }
```

### src.code.ingest_file (call 2)

```json
{
  "Tree(./tests/inputs/codebase/0-accounts.sql, ./tests/inputs/codebase/1-revenue.sql)": {
    "files": {
      "./tests/inputs/codebase/0-accounts.sql": [
        { "Query(./tests/inputs/codebase/0-accounts.sql:25:0-44:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
                  "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                        "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                        "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                        "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [ "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                        "sql": "SUM(o.value)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
                  "alias": "revenue_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
                  "sql": "revenue / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
                  "alias": "revenue_core_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
                  "sql": "revenue_core / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
                  "alias": "revenue_aux_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
                  "sql": "revenue_aux / contract_duration_days" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:25:0-44:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:50:0-71:31)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
                  "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [ "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                        "sql": "DATE(date_day, 'start of month')" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [ "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                        "sql": "COUNT(ds.deal_id)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                        "sql": "SUM(ds.revenue_core_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                        "sql": "SUM(ds.revenue_aux_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                        "sql": "SUM(ds.revenue_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                        "alias": null,
                        "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                        "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [ "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
                  "sql": "AVG(t.deals)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [ "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
                  "sql": "SUM(t.revenue_core)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [ "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
                  "sql": "SUM(t.revenue_aux)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [ "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
                  "sql": "SUM(t.revenue)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:50:0-71:31" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:78:0-111:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
                  "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [ "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                        "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                        "alias": "revenue_12m",
                        "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                        "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
                  "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:78:0-111:6" } } ],
      "./tests/inputs/codebase/1-revenue.sql": [
        { "Query(./tests/inputs/codebase/1-revenue.sql:29:0-50:49)": {
            "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_tech",
                  "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
                  "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
                  "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
                  "sql": "SUM(accounts_revenue.revenue)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:29:0-50:49" } },
        { "Query(./tests/inputs/codebase/1-revenue.sql:4:0-25:52)": {
            "sources": [ "Table(?.accounts as a)", "Table(?.accounts_360 as a360)", "Table(?.accounts_revenue as ar)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
                  "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [ "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
                  "sql": "date(date_month, 'start of year')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
                  "sql": "SUM(ar.revenue)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
                  "sql": "COUNT(DISTINCT ar.account_id)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_per_account",
                  "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
                  "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:4:0-25:52" } } ] },
    "index": {
      "<Column>": [ "Column(?.?.*)", "Column(?.?.account_id)", "Column(?.?.account_id)", "Column(?.?.contract_duration_days)", "Column(?.?.country)", "Column(?.?.date_day)", "Column(?.?.date_month)", "Column(?.?.date_month)", "Column(?.?.date_year)", "Column(?.?.deal_id)", "Column(?.?.industry_cluster)", "Column(?.?.order_id)", "Column(?.?.region_cluster)", "Column(?.?.revenue)", "Column(?.?.revenue_aux)", "Column(?.?.revenue_core)", "Column(?.accounts.account_id)", "Column(?.accounts.country)", "Column(?.accounts.date_month)", "Column(?.accounts.deals)", "Column(?.accounts.industry)", "Column(?.accounts.industry)", "Column(?.accounts.industry)", "Column(?.accounts.name)", "Column(?.accounts.name)", "Column(?.accounts.priority)", "Column(?.accounts.revenue)", "Column(?.accounts.revenue_aux)", "Column(?.accounts.revenue_core)", "Column(?.accounts_360.account_size)", "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.country)", "Column(?.accounts_revenue.date_month)", "Column(?.accounts_revenue.region)", "Column(?.accounts_revenue.revenue)", "Column(?.accounts_revenue.revenue)", "Column(?.countries.region)", "Column(?.countries.region)", "Column(?.countries.region)", "Column(?.date_ranges.date_day)", "Column(?.deals.account_id)", "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)", "Column(?.deals.deal_id)", "Column(?.deals.stage)", "Column(?.deals_signed.account_id)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)", "Column(?.deals_signed.deal_id)", "Column(?.deals_signed.revenue_aux_day)", "Column(?.deals_signed.revenue_core_day)", "Column(?.deals_signed.revenue_day)", "Column(?.orders.product)", "Column(?.orders.value)", "Column(?.t.*)", "Column(?.t.account_id)", "Column(?.t.date_month)", "Column(?.t.deals)", "Column(?.t.revenue)", "Column(?.t.revenue_12m)", "Column(?.t.revenue_aux)", "Column(?.t.revenue_core)" ],
      "<Expression>": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
            "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
            "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
            "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
            "sql": "date(date_month, 'start of year')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
            "sql": "SUM(ar.revenue)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
            "sql": "SUM(accounts_revenue.revenue)" } } ],
      "<Table>": [ "Table(?.accounts as a)", "Table(?.accounts)", "Table(?.accounts)", "Table(?.accounts_360 as a360)", "Table(?.accounts_revenue as ar)", "Table(?.accounts_revenue)", "Table(?.accounts_revenue)", "Table(?.countries as c)", "Table(?.countries as c)", "Table(?.countries as c)", "Table(?.date_ranges as dr)", "Table(?.deals as d)", "Table(?.deals_signed as ds)", "Table(?.orders as o)" ],
      "<Query>": [
        { "Query(./tests/inputs/codebase/0-accounts.sql:25:0-44:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
                  "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                        "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                        "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                        "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [ "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                        "sql": "SUM(o.value)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
                  "alias": "revenue_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
                  "sql": "revenue / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
                  "alias": "revenue_core_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
                  "sql": "revenue_core / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
                  "alias": "revenue_aux_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
                  "sql": "revenue_aux / contract_duration_days" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:25:0-44:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
            "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                  "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                  "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                  "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                  "alias": "contract_duration_days",
                  "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                  "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                  "columns": [ "Column(?.orders.value)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                  "sql": "SUM(o.value)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:50:0-71:31)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
                  "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [ "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                        "sql": "DATE(date_day, 'start of month')" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [ "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                        "sql": "COUNT(ds.deal_id)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                        "sql": "SUM(ds.revenue_core_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                        "sql": "SUM(ds.revenue_aux_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                        "sql": "SUM(ds.revenue_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                        "alias": null,
                        "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                        "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [ "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
                  "sql": "AVG(t.deals)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [ "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
                  "sql": "SUM(t.revenue_core)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [ "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
                  "sql": "SUM(t.revenue_aux)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [ "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
                  "sql": "SUM(t.revenue)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:50:0-71:31" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
            "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                  "columns": [ "Column(?.?.date_day)" ],
                  "alias": "date_month",
                  "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                  "sql": "DATE(date_day, 'start of month')" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                  "columns": [ "Column(?.deals_signed.deal_id)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                  "sql": "COUNT(ds.deal_id)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                  "sql": "SUM(ds.revenue_core_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                  "sql": "SUM(ds.revenue_aux_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_day)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                  "sql": "SUM(ds.revenue_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                  "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                  "alias": null,
                  "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                  "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:78:0-111:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
                  "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [ "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                        "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                        "alias": "revenue_12m",
                        "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                        "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
                  "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:78:0-111:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
            "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                  "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                  "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                  "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } },
        { "Query(./tests/inputs/codebase/1-revenue.sql:29:0-50:49)": {
            "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_tech",
                  "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
                  "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
                  "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
                  "sql": "SUM(accounts_revenue.revenue)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:29:0-50:49" } },
        { "Query(./tests/inputs/codebase/1-revenue.sql:4:0-25:52)": {
            "sources": [ "Table(?.accounts as a)", "Table(?.accounts_360 as a360)", "Table(?.accounts_revenue as ar)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
                  "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [ "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
                  "sql": "date(date_month, 'start of year')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
                  "sql": "SUM(ar.revenue)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
                  "sql": "COUNT(DISTINCT ar.account_id)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_per_account",
                  "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
                  "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:4:0-25:52" } } ] },
    "map_key_to_expr": {
      "('Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue_core)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue_aux)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } } ],
      "('Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))', ['Column(?.deals.contract_end_date)', 'Column(?.deals.contract_start_date)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))\", ['Column(?.orders.product)', 'Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))\", ['Column(?.orders.product)', 'Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.orders.value))))', ['Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.deals))))', ['Column(?.t.deals)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))', ['Column(?.t.revenue_core)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))', ['Column(?.t.revenue_aux)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))', ['Column(?.t.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))\", ['Column(?.?.date_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))', ['Column(?.deals_signed.deal_id)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))', ['Column(?.deals_signed.revenue_core_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))', ['Column(?.deals_signed.revenue_aux_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))', ['Column(?.deals_signed.revenue_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } } ],
      "('Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))', ['Column(?.date_ranges.date_day)', 'Column(?.deals_signed.contract_end_date)', 'Column(?.deals_signed.contract_start_date)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))\", ['Column(?.t.revenue_12m)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))\", ['Column(?.countries.region)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))', ['Column(?.accounts.account_id)', 'Column(?.accounts.date_month)', 'Column(?.accounts.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))\", ['Column(?.?.date_month)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
            "sql": "date(date_month, 'start of year')" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))\", ['Column(?.accounts.industry)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
            "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))', ['Column(?.accounts_revenue.revenue)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
            "sql": "SUM(ar.revenue)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
            "sql": "SUM(accounts_revenue.revenue)" } } ],
      "('Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))', ['Column(?.accounts_revenue.account_id)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } } ],
      "('Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))', ['Column(?.accounts_revenue.account_id)', 'Column(?.accounts_revenue.revenue)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
      "(\"Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))\", ['Column(?.accounts.industry)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
            "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))\", ['Column(?.accounts_revenue.revenue)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
            "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ] },
    "map_file_to_expr": {
      "./tests/inputs/codebase/0-accounts.sql": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
      "./tests/inputs/codebase/1-revenue.sql": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
            "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
            "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
            "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
            "sql": "date(date_month, 'start of year')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
            "sql": "SUM(ar.revenue)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
            "sql": "SUM(accounts_revenue.revenue)" } } ] } } }
```

### src.code.ingest_file (call 3)

```json
{
  "Tree(./tests/inputs/codebase/0-accounts.sql)": {
    "files": {
      "./tests/inputs/codebase/0-accounts.sql": [
        { "Query(./tests/inputs/codebase/0-accounts.sql:25:0-44:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
                  "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                        "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                        "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                        "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [ "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                        "sql": "SUM(o.value)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
                  "alias": "revenue_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
                  "sql": "revenue / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
                  "alias": "revenue_core_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
                  "sql": "revenue_core / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
                  "alias": "revenue_aux_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
                  "sql": "revenue_aux / contract_duration_days" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:25:0-44:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:50:0-71:31)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
                  "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [ "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                        "sql": "DATE(date_day, 'start of month')" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [ "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                        "sql": "COUNT(ds.deal_id)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                        "sql": "SUM(ds.revenue_core_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                        "sql": "SUM(ds.revenue_aux_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                        "sql": "SUM(ds.revenue_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                        "alias": null,
                        "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                        "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [ "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
                  "sql": "AVG(t.deals)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [ "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
                  "sql": "SUM(t.revenue_core)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [ "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
                  "sql": "SUM(t.revenue_aux)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [ "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
                  "sql": "SUM(t.revenue)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:50:0-71:31" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:78:0-111:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
                  "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [ "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                        "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                        "alias": "revenue_12m",
                        "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                        "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
                  "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:78:0-111:6" } } ] },
    "index": {
      "<Column>": [ "Column(?.?.*)", "Column(?.?.account_id)", "Column(?.?.contract_duration_days)", "Column(?.?.date_day)", "Column(?.?.date_month)", "Column(?.?.deal_id)", "Column(?.?.order_id)", "Column(?.?.revenue)", "Column(?.?.revenue_aux)", "Column(?.?.revenue_core)", "Column(?.accounts.account_id)", "Column(?.accounts.country)", "Column(?.accounts.date_month)", "Column(?.accounts.deals)", "Column(?.accounts.industry)", "Column(?.accounts.name)", "Column(?.accounts.priority)", "Column(?.accounts.revenue)", "Column(?.accounts.revenue_aux)", "Column(?.accounts.revenue_core)", "Column(?.countries.region)", "Column(?.date_ranges.date_day)", "Column(?.deals.account_id)", "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)", "Column(?.deals.deal_id)", "Column(?.deals.stage)", "Column(?.deals_signed.account_id)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)", "Column(?.deals_signed.deal_id)", "Column(?.deals_signed.revenue_aux_day)", "Column(?.deals_signed.revenue_core_day)", "Column(?.deals_signed.revenue_day)", "Column(?.orders.product)", "Column(?.orders.value)", "Column(?.t.*)", "Column(?.t.account_id)", "Column(?.t.date_month)", "Column(?.t.deals)", "Column(?.t.revenue)", "Column(?.t.revenue_12m)", "Column(?.t.revenue_aux)", "Column(?.t.revenue_core)" ],
      "<Expression>": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
      "<Table>": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)", "Table(?.date_ranges as dr)", "Table(?.deals as d)", "Table(?.deals_signed as ds)", "Table(?.orders as o)" ],
      "<Query>": [
        { "Query(./tests/inputs/codebase/0-accounts.sql:25:0-44:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
                  "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                        "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                        "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                        "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [ "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                        "sql": "SUM(o.value)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
                  "alias": "revenue_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
                  "sql": "revenue / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
                  "alias": "revenue_core_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
                  "sql": "revenue_core / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
                  "alias": "revenue_aux_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
                  "sql": "revenue_aux / contract_duration_days" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:25:0-44:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
            "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                  "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                  "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                  "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                  "alias": "contract_duration_days",
                  "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                  "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                  "columns": [ "Column(?.orders.value)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                  "sql": "SUM(o.value)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:50:0-71:31)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
                  "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [ "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                        "sql": "DATE(date_day, 'start of month')" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [ "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                        "sql": "COUNT(ds.deal_id)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                        "sql": "SUM(ds.revenue_core_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                        "sql": "SUM(ds.revenue_aux_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                        "sql": "SUM(ds.revenue_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                        "alias": null,
                        "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                        "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [ "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
                  "sql": "AVG(t.deals)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [ "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
                  "sql": "SUM(t.revenue_core)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [ "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
                  "sql": "SUM(t.revenue_aux)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [ "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
                  "sql": "SUM(t.revenue)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:50:0-71:31" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
            "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                  "columns": [ "Column(?.?.date_day)" ],
                  "alias": "date_month",
                  "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                  "sql": "DATE(date_day, 'start of month')" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                  "columns": [ "Column(?.deals_signed.deal_id)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                  "sql": "COUNT(ds.deal_id)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                  "sql": "SUM(ds.revenue_core_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                  "sql": "SUM(ds.revenue_aux_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_day)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                  "sql": "SUM(ds.revenue_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                  "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                  "alias": null,
                  "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                  "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:78:0-111:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
                  "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [ "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                        "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                        "alias": "revenue_12m",
                        "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                        "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
                  "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:78:0-111:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
            "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                  "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                  "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                  "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ] },
    "map_key_to_expr": {
      "('Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue_core)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue_aux)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } } ],
      "('Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))', ['Column(?.deals.contract_end_date)', 'Column(?.deals.contract_start_date)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))\", ['Column(?.orders.product)', 'Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))\", ['Column(?.orders.product)', 'Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.orders.value))))', ['Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.deals))))', ['Column(?.t.deals)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))', ['Column(?.t.revenue_core)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))', ['Column(?.t.revenue_aux)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))', ['Column(?.t.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))\", ['Column(?.?.date_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))', ['Column(?.deals_signed.deal_id)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))', ['Column(?.deals_signed.revenue_core_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))', ['Column(?.deals_signed.revenue_aux_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))', ['Column(?.deals_signed.revenue_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } } ],
      "('Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))', ['Column(?.date_ranges.date_day)', 'Column(?.deals_signed.contract_end_date)', 'Column(?.deals_signed.contract_start_date)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))\", ['Column(?.t.revenue_12m)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))\", ['Column(?.countries.region)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))', ['Column(?.accounts.account_id)', 'Column(?.accounts.date_month)', 'Column(?.accounts.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ] },
    "map_file_to_expr": {
      "./tests/inputs/codebase/0-accounts.sql": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ] } } }
```

### src.code.ingest_file (call 4)

```json
{
  "Tree(./tests/inputs/codebase/0-accounts.sql, ./tests/inputs/codebase/1-revenue.sql)": {
    "files": {
      "./tests/inputs/codebase/0-accounts.sql": [
        { "Query(./tests/inputs/codebase/0-accounts.sql:25:0-44:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
                  "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                        "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                        "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                        "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [ "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                        "sql": "SUM(o.value)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
                  "alias": "revenue_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
                  "sql": "revenue / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
                  "alias": "revenue_core_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
                  "sql": "revenue_core / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
                  "alias": "revenue_aux_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
                  "sql": "revenue_aux / contract_duration_days" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:25:0-44:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:50:0-71:31)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
                  "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [ "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                        "sql": "DATE(date_day, 'start of month')" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [ "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                        "sql": "COUNT(ds.deal_id)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                        "sql": "SUM(ds.revenue_core_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                        "sql": "SUM(ds.revenue_aux_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                        "sql": "SUM(ds.revenue_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                        "alias": null,
                        "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                        "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [ "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
                  "sql": "AVG(t.deals)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [ "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
                  "sql": "SUM(t.revenue_core)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [ "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
                  "sql": "SUM(t.revenue_aux)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [ "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
                  "sql": "SUM(t.revenue)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:50:0-71:31" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:78:0-111:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
                  "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [ "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                        "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                        "alias": "revenue_12m",
                        "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                        "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
                  "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:78:0-111:6" } } ],
      "./tests/inputs/codebase/1-revenue.sql": [
        { "Query(./tests/inputs/codebase/1-revenue.sql:29:0-50:49)": {
            "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_tech",
                  "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
                  "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
                  "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
                  "sql": "SUM(accounts_revenue.revenue)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:29:0-50:49" } },
        { "Query(./tests/inputs/codebase/1-revenue.sql:4:0-25:52)": {
            "sources": [ "Table(?.accounts as a)", "Table(?.accounts_360 as a360)", "Table(?.accounts_revenue as ar)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
                  "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [ "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
                  "sql": "date(date_month, 'start of year')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
                  "sql": "SUM(ar.revenue)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
                  "sql": "COUNT(DISTINCT ar.account_id)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_per_account",
                  "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
                  "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:4:0-25:52" } } ] },
    "index": {
      "<Column>": [ "Column(?.?.*)", "Column(?.?.account_id)", "Column(?.?.account_id)", "Column(?.?.contract_duration_days)", "Column(?.?.country)", "Column(?.?.date_day)", "Column(?.?.date_month)", "Column(?.?.date_month)", "Column(?.?.date_year)", "Column(?.?.deal_id)", "Column(?.?.industry_cluster)", "Column(?.?.order_id)", "Column(?.?.region_cluster)", "Column(?.?.revenue)", "Column(?.?.revenue_aux)", "Column(?.?.revenue_core)", "Column(?.accounts.account_id)", "Column(?.accounts.country)", "Column(?.accounts.date_month)", "Column(?.accounts.deals)", "Column(?.accounts.industry)", "Column(?.accounts.industry)", "Column(?.accounts.industry)", "Column(?.accounts.name)", "Column(?.accounts.name)", "Column(?.accounts.priority)", "Column(?.accounts.revenue)", "Column(?.accounts.revenue_aux)", "Column(?.accounts.revenue_core)", "Column(?.accounts_360.account_size)", "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.country)", "Column(?.accounts_revenue.date_month)", "Column(?.accounts_revenue.region)", "Column(?.accounts_revenue.revenue)", "Column(?.accounts_revenue.revenue)", "Column(?.countries.region)", "Column(?.countries.region)", "Column(?.countries.region)", "Column(?.date_ranges.date_day)", "Column(?.deals.account_id)", "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)", "Column(?.deals.deal_id)", "Column(?.deals.stage)", "Column(?.deals_signed.account_id)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)", "Column(?.deals_signed.deal_id)", "Column(?.deals_signed.revenue_aux_day)", "Column(?.deals_signed.revenue_core_day)", "Column(?.deals_signed.revenue_day)", "Column(?.orders.product)", "Column(?.orders.value)", "Column(?.t.*)", "Column(?.t.account_id)", "Column(?.t.date_month)", "Column(?.t.deals)", "Column(?.t.revenue)", "Column(?.t.revenue_12m)", "Column(?.t.revenue_aux)", "Column(?.t.revenue_core)" ],
      "<Expression>": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
            "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
            "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
            "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
            "sql": "date(date_month, 'start of year')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
            "sql": "SUM(ar.revenue)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
            "sql": "SUM(accounts_revenue.revenue)" } } ],
      "<Table>": [ "Table(?.accounts as a)", "Table(?.accounts)", "Table(?.accounts)", "Table(?.accounts_360 as a360)", "Table(?.accounts_revenue as ar)", "Table(?.accounts_revenue)", "Table(?.accounts_revenue)", "Table(?.countries as c)", "Table(?.countries as c)", "Table(?.countries as c)", "Table(?.date_ranges as dr)", "Table(?.deals as d)", "Table(?.deals_signed as ds)", "Table(?.orders as o)" ],
      "<Query>": [
        { "Query(./tests/inputs/codebase/0-accounts.sql:25:0-44:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
                  "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                        "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                        "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                        "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [ "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                        "sql": "SUM(o.value)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
                  "alias": "revenue_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
                  "sql": "revenue / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
                  "alias": "revenue_core_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
                  "sql": "revenue_core / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
                  "alias": "revenue_aux_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
                  "sql": "revenue_aux / contract_duration_days" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:25:0-44:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
            "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                  "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                  "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                  "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                  "alias": "contract_duration_days",
                  "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                  "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                  "columns": [ "Column(?.orders.value)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                  "sql": "SUM(o.value)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:50:0-71:31)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
                  "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [ "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                        "sql": "DATE(date_day, 'start of month')" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [ "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                        "sql": "COUNT(ds.deal_id)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                        "sql": "SUM(ds.revenue_core_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                        "sql": "SUM(ds.revenue_aux_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                        "sql": "SUM(ds.revenue_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                        "alias": null,
                        "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                        "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [ "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
                  "sql": "AVG(t.deals)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [ "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
                  "sql": "SUM(t.revenue_core)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [ "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
                  "sql": "SUM(t.revenue_aux)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [ "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
                  "sql": "SUM(t.revenue)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:50:0-71:31" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
            "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                  "columns": [ "Column(?.?.date_day)" ],
                  "alias": "date_month",
                  "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                  "sql": "DATE(date_day, 'start of month')" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                  "columns": [ "Column(?.deals_signed.deal_id)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                  "sql": "COUNT(ds.deal_id)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                  "sql": "SUM(ds.revenue_core_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                  "sql": "SUM(ds.revenue_aux_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_day)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                  "sql": "SUM(ds.revenue_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                  "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                  "alias": null,
                  "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                  "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:78:0-111:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
                  "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [ "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                        "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                        "alias": "revenue_12m",
                        "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                        "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
                  "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:78:0-111:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
            "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                  "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                  "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                  "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } },
        { "Query(./tests/inputs/codebase/1-revenue.sql:29:0-50:49)": {
            "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_tech",
                  "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
                  "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
                  "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
                  "sql": "SUM(accounts_revenue.revenue)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:29:0-50:49" } },
        { "Query(./tests/inputs/codebase/1-revenue.sql:4:0-25:52)": {
            "sources": [ "Table(?.accounts as a)", "Table(?.accounts_360 as a360)", "Table(?.accounts_revenue as ar)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
                  "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [ "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
                  "sql": "date(date_month, 'start of year')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
                  "sql": "SUM(ar.revenue)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
                  "sql": "COUNT(DISTINCT ar.account_id)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_per_account",
                  "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
                  "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:4:0-25:52" } } ] },
    "map_key_to_expr": {
      "('Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue_core)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue_aux)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } } ],
      "('Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))', ['Column(?.deals.contract_end_date)', 'Column(?.deals.contract_start_date)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))\", ['Column(?.orders.product)', 'Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))\", ['Column(?.orders.product)', 'Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.orders.value))))', ['Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.deals))))', ['Column(?.t.deals)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))', ['Column(?.t.revenue_core)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))', ['Column(?.t.revenue_aux)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))', ['Column(?.t.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))\", ['Column(?.?.date_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))', ['Column(?.deals_signed.deal_id)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))', ['Column(?.deals_signed.revenue_core_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))', ['Column(?.deals_signed.revenue_aux_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))', ['Column(?.deals_signed.revenue_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } } ],
      "('Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))', ['Column(?.date_ranges.date_day)', 'Column(?.deals_signed.contract_end_date)', 'Column(?.deals_signed.contract_start_date)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))\", ['Column(?.t.revenue_12m)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))\", ['Column(?.countries.region)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))', ['Column(?.accounts.account_id)', 'Column(?.accounts.date_month)', 'Column(?.accounts.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))\", ['Column(?.?.date_month)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
            "sql": "date(date_month, 'start of year')" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))\", ['Column(?.accounts.industry)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
            "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))', ['Column(?.accounts_revenue.revenue)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
            "sql": "SUM(ar.revenue)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
            "sql": "SUM(accounts_revenue.revenue)" } } ],
      "('Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))', ['Column(?.accounts_revenue.account_id)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } } ],
      "('Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))', ['Column(?.accounts_revenue.account_id)', 'Column(?.accounts_revenue.revenue)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
      "(\"Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))\", ['Column(?.accounts.industry)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
            "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))\", ['Column(?.accounts_revenue.revenue)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
            "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ] },
    "map_file_to_expr": {
      "./tests/inputs/codebase/0-accounts.sql": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
      "./tests/inputs/codebase/1-revenue.sql": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
            "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
            "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
            "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
            "sql": "date(date_month, 'start of year')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
            "sql": "SUM(ar.revenue)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
            "sql": "SUM(accounts_revenue.revenue)" } } ] } } }
```

### src.code.ingest_file (call 5)

```json
{
  "Tree(./tests/inputs/codebase/0-accounts.sql, ./tests/inputs/codebase/1-revenue.sql, ./tests/inputs/editor.sql)": {
    "files": {
      "./tests/inputs/codebase/0-accounts.sql": [
        { "Query(./tests/inputs/codebase/0-accounts.sql:25:0-44:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
                  "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                        "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                        "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                        "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [ "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                        "sql": "SUM(o.value)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
                  "alias": "revenue_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
                  "sql": "revenue / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
                  "alias": "revenue_core_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
                  "sql": "revenue_core / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
                  "alias": "revenue_aux_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
                  "sql": "revenue_aux / contract_duration_days" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:25:0-44:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:50:0-71:31)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
                  "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [ "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                        "sql": "DATE(date_day, 'start of month')" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [ "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                        "sql": "COUNT(ds.deal_id)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                        "sql": "SUM(ds.revenue_core_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                        "sql": "SUM(ds.revenue_aux_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                        "sql": "SUM(ds.revenue_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                        "alias": null,
                        "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                        "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [ "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
                  "sql": "AVG(t.deals)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [ "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
                  "sql": "SUM(t.revenue_core)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [ "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
                  "sql": "SUM(t.revenue_aux)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [ "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
                  "sql": "SUM(t.revenue)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:50:0-71:31" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:78:0-111:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
                  "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [ "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                        "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                        "alias": "revenue_12m",
                        "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                        "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
                  "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:78:0-111:6" } } ],
      "./tests/inputs/codebase/1-revenue.sql": [
        { "Query(./tests/inputs/codebase/1-revenue.sql:29:0-50:49)": {
            "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_tech",
                  "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
                  "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
                  "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
                  "sql": "SUM(accounts_revenue.revenue)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:29:0-50:49" } },
        { "Query(./tests/inputs/codebase/1-revenue.sql:4:0-25:52)": {
            "sources": [ "Table(?.accounts as a)", "Table(?.accounts_360 as a360)", "Table(?.accounts_revenue as ar)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
                  "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [ "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
                  "sql": "date(date_month, 'start of year')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
                  "sql": "SUM(ar.revenue)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
                  "sql": "COUNT(DISTINCT ar.account_id)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_per_account",
                  "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
                  "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:4:0-25:52" } } ],
      "./tests/inputs/editor.sql": [
        { "Query(./tests/inputs/editor.sql:2:0-24:45)": {
            "sources": [ "Table(?.accounts as a)", "Table(?.accounts_revenue as ar)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/editor.sql:12:4-12:62) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_it",
                  "location": "./tests/inputs/editor.sql:12:4-12:62",
                  "sql": "IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')" } },
              { "Expression(./tests/inputs/editor.sql:3:4-3:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [ "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "./tests/inputs/editor.sql:3:4-3:37",
                  "sql": "date(date_month, 'start of year')" } },
              { "Expression(./tests/inputs/editor.sql:5:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "macro_region",
                  "location": "./tests/inputs/editor.sql:5:4-10:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/editor.sql:13:4-13:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/editor.sql:13:4-13:19",
                  "sql": "SUM(ar.revenue)" } },
              { "Expression(./tests/inputs/editor.sql:14:4-14:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "./tests/inputs/editor.sql:14:4-14:33",
                  "sql": "COUNT(DISTINCT ar.account_id)" } },
              { "Expression(./tests/inputs/editor.sql:15:4-15:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_per_account",
                  "location": "./tests/inputs/editor.sql:15:4-15:51",
                  "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
            "location": "./tests/inputs/editor.sql:2:0-24:45" } } ] },
    "index": {
      "<Column>": [ "Column(?.?.*)", "Column(?.?.account_id)", "Column(?.?.account_id)", "Column(?.?.account_id)", "Column(?.?.contract_duration_days)", "Column(?.?.country)", "Column(?.?.country)", "Column(?.?.date_day)", "Column(?.?.date_month)", "Column(?.?.date_month)", "Column(?.?.date_month)", "Column(?.?.date_year)", "Column(?.?.date_year)", "Column(?.?.deal_id)", "Column(?.?.industry_cluster)", "Column(?.?.industry_it)", "Column(?.?.macro_region)", "Column(?.?.order_id)", "Column(?.?.region_cluster)", "Column(?.?.revenue)", "Column(?.?.revenue_aux)", "Column(?.?.revenue_core)", "Column(?.accounts.account_id)", "Column(?.accounts.country)", "Column(?.accounts.date_month)", "Column(?.accounts.deals)", "Column(?.accounts.industry)", "Column(?.accounts.industry)", "Column(?.accounts.industry)", "Column(?.accounts.industry)", "Column(?.accounts.name)", "Column(?.accounts.name)", "Column(?.accounts.priority)", "Column(?.accounts.revenue)", "Column(?.accounts.revenue_aux)", "Column(?.accounts.revenue_core)", "Column(?.accounts_360.account_size)", "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.country)", "Column(?.accounts_revenue.date_month)", "Column(?.accounts_revenue.region)", "Column(?.accounts_revenue.revenue)", "Column(?.accounts_revenue.revenue)", "Column(?.accounts_revenue.revenue)", "Column(?.countries.region)", "Column(?.countries.region)", "Column(?.countries.region)", "Column(?.countries.region)", "Column(?.date_ranges.date_day)", "Column(?.deals.account_id)", "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)", "Column(?.deals.deal_id)", "Column(?.deals.stage)", "Column(?.deals_signed.account_id)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)", "Column(?.deals_signed.deal_id)", "Column(?.deals_signed.revenue_aux_day)", "Column(?.deals_signed.revenue_core_day)", "Column(?.deals_signed.revenue_day)", "Column(?.orders.product)", "Column(?.orders.value)", "Column(?.t.*)", "Column(?.t.account_id)", "Column(?.t.date_month)", "Column(?.t.deals)", "Column(?.t.revenue)", "Column(?.t.revenue_12m)", "Column(?.t.revenue_aux)", "Column(?.t.revenue_core)" ],
      "<Expression>": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
            "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
            "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
            "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
            "sql": "date(date_month, 'start of year')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/editor.sql:12:4-12:62) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_it",
            "location": "./tests/inputs/editor.sql:12:4-12:62",
            "sql": "IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')" } },
        { "Expression(./tests/inputs/editor.sql:3:4-3:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/editor.sql:3:4-3:37",
            "sql": "date(date_month, 'start of year')" } },
        { "Expression(./tests/inputs/editor.sql:5:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "macro_region",
            "location": "./tests/inputs/editor.sql:5:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
            "sql": "SUM(ar.revenue)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
            "sql": "SUM(accounts_revenue.revenue)" } },
        { "Expression(./tests/inputs/editor.sql:13:4-13:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/editor.sql:13:4-13:19",
            "sql": "SUM(ar.revenue)" } },
        { "Expression(./tests/inputs/editor.sql:14:4-14:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/editor.sql:14:4-14:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/editor.sql:15:4-15:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/editor.sql:15:4-15:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
      "<Table>": [ "Table(?.accounts as a)", "Table(?.accounts as a)", "Table(?.accounts)", "Table(?.accounts)", "Table(?.accounts_360 as a360)", "Table(?.accounts_revenue as ar)", "Table(?.accounts_revenue as ar)", "Table(?.accounts_revenue)", "Table(?.accounts_revenue)", "Table(?.countries as c)", "Table(?.countries as c)", "Table(?.countries as c)", "Table(?.countries as c)", "Table(?.date_ranges as dr)", "Table(?.deals as d)", "Table(?.deals_signed as ds)", "Table(?.orders as o)" ],
      "<Query>": [
        { "Query(./tests/inputs/codebase/0-accounts.sql:25:0-44:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
                  "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                        "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                        "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                        "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                        "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                        "alias": "contract_duration_days",
                        "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                        "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                        "columns": [ "Column(?.orders.value)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                        "sql": "SUM(o.value)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
                  "alias": "revenue_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
                  "sql": "revenue / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
                  "alias": "revenue_core_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
                  "sql": "revenue_core / contract_duration_days" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
                  "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
                  "alias": "revenue_aux_day",
                  "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
                  "sql": "revenue_aux / contract_duration_days" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:25:0-44:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:31:4-43:80)": {
            "sources": [ "Table(?.deals as d)", "Table(?.orders as o)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                  "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                  "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                  "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
                  "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
                  "alias": "contract_duration_days",
                  "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
                  "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
                  "columns": [ "Column(?.orders.value)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
                  "sql": "SUM(o.value)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:31:4-43:80" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:50:0-71:31)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
                  "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                        "columns": [ "Column(?.?.date_day)" ],
                        "alias": "date_month",
                        "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                        "sql": "DATE(date_day, 'start of month')" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                        "columns": [ "Column(?.deals_signed.deal_id)" ],
                        "alias": "deals",
                        "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                        "sql": "COUNT(ds.deal_id)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                        "alias": "revenue_core",
                        "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                        "sql": "SUM(ds.revenue_core_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                        "alias": "revenue_aux",
                        "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                        "sql": "SUM(ds.revenue_aux_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                        "columns": [ "Column(?.deals_signed.revenue_day)" ],
                        "alias": "revenue",
                        "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                        "sql": "SUM(ds.revenue_day)" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                        "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                        "alias": null,
                        "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                        "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
                  "columns": [ "Column(?.t.deals)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
                  "sql": "AVG(t.deals)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
                  "columns": [ "Column(?.t.revenue_core)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
                  "sql": "SUM(t.revenue_core)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
                  "columns": [ "Column(?.t.revenue_aux)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
                  "sql": "SUM(t.revenue_aux)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
                  "columns": [ "Column(?.t.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
                  "sql": "SUM(t.revenue)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:50:0-71:31" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:58:4-70:39)": {
            "sources": [ "Table(?.date_ranges as dr)", "Table(?.deals_signed as ds)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
                  "columns": [ "Column(?.?.date_day)" ],
                  "alias": "date_month",
                  "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
                  "sql": "DATE(date_day, 'start of month')" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
                  "columns": [ "Column(?.deals_signed.deal_id)" ],
                  "alias": "deals",
                  "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
                  "sql": "COUNT(ds.deal_id)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
                  "alias": "revenue_core",
                  "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
                  "sql": "SUM(ds.revenue_core_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
                  "alias": "revenue_aux",
                  "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
                  "sql": "SUM(ds.revenue_aux_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
                  "columns": [ "Column(?.deals_signed.revenue_day)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
                  "sql": "SUM(ds.revenue_day)" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
                  "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
                  "alias": null,
                  "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
                  "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:58:4-70:39" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:78:0-111:6)": {
            "sources": [
              { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
                  "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
                  "expressions": [
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                        "columns": [ "Column(?.countries.region)" ],
                        "alias": "region_cluster",
                        "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                        "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
                    { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                        "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                        "alias": "revenue_12m",
                        "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                        "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
                  "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } } ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.t.revenue_12m)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
                  "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:78:0-111:6" } },
        { "Query(./tests/inputs/codebase/0-accounts.sql:87:4-110:45)": {
            "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                  "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
              { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
                  "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
                  "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
            "location": "./tests/inputs/codebase/0-accounts.sql:87:4-110:45" } },
        { "Query(./tests/inputs/codebase/1-revenue.sql:29:0-50:49)": {
            "sources": [ "Table(?.accounts)", "Table(?.accounts_revenue)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_tech",
                  "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
                  "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "account_size",
                  "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
                  "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_12m",
                  "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
                  "sql": "SUM(accounts_revenue.revenue)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:29:0-50:49" } },
        { "Query(./tests/inputs/codebase/1-revenue.sql:4:0-25:52)": {
            "sources": [ "Table(?.accounts as a)", "Table(?.accounts_360 as a360)", "Table(?.accounts_revenue as ar)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
                  "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [ "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
                  "sql": "date(date_month, 'start of year')" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "region_cluster",
                  "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
                  "sql": "SUM(ar.revenue)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
                  "sql": "COUNT(DISTINCT ar.account_id)" } },
              { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_per_account",
                  "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
                  "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
            "location": "./tests/inputs/codebase/1-revenue.sql:4:0-25:52" } },
        { "Query(./tests/inputs/editor.sql:2:0-24:45)": {
            "sources": [ "Table(?.accounts as a)", "Table(?.accounts_revenue as ar)", "Table(?.countries as c)" ],
            "expressions": [
              { "Expression(./tests/inputs/editor.sql:12:4-12:62) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
                  "columns": [ "Column(?.accounts.industry)" ],
                  "alias": "industry_it",
                  "location": "./tests/inputs/editor.sql:12:4-12:62",
                  "sql": "IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')" } },
              { "Expression(./tests/inputs/editor.sql:3:4-3:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
                  "columns": [ "Column(?.?.date_month)" ],
                  "alias": "date_year",
                  "location": "./tests/inputs/editor.sql:3:4-3:37",
                  "sql": "date(date_month, 'start of year')" } },
              { "Expression(./tests/inputs/editor.sql:5:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
                  "columns": [ "Column(?.countries.region)" ],
                  "alias": "macro_region",
                  "location": "./tests/inputs/editor.sql:5:4-10:7",
                  "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } },
              { "Expression(./tests/inputs/editor.sql:13:4-13:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
                  "columns": [ "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue",
                  "location": "./tests/inputs/editor.sql:13:4-13:19",
                  "sql": "SUM(ar.revenue)" } },
              { "Expression(./tests/inputs/editor.sql:14:4-14:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)" ],
                  "alias": "accounts",
                  "location": "./tests/inputs/editor.sql:14:4-14:33",
                  "sql": "COUNT(DISTINCT ar.account_id)" } },
              { "Expression(./tests/inputs/editor.sql:15:4-15:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
                  "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
                  "alias": "revenue_per_account",
                  "location": "./tests/inputs/editor.sql:15:4-15:51",
                  "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
            "location": "./tests/inputs/editor.sql:2:0-24:45" } } ] },
    "map_key_to_expr": {
      "('Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue_core)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } } ],
      "('Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))', ['Column(?.?.contract_duration_days)', 'Column(?.?.revenue_aux)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } } ],
      "('Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))', ['Column(?.deals.contract_end_date)', 'Column(?.deals.contract_start_date)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))\", ['Column(?.orders.product)', 'Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } } ],
      "(\"Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))\", ['Column(?.orders.product)', 'Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.orders.value))))', ['Column(?.orders.value)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.deals))))', ['Column(?.t.deals)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))', ['Column(?.t.revenue_core)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))', ['Column(?.t.revenue_aux)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))', ['Column(?.t.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))\", ['Column(?.?.date_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))', ['Column(?.deals_signed.deal_id)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))', ['Column(?.deals_signed.revenue_core_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))', ['Column(?.deals_signed.revenue_aux_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))', ['Column(?.deals_signed.revenue_day)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } } ],
      "('Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))', ['Column(?.date_ranges.date_day)', 'Column(?.deals_signed.contract_end_date)', 'Column(?.deals_signed.contract_start_date)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))\", ['Column(?.t.revenue_12m)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))\", ['Column(?.countries.region)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))', ['Column(?.accounts.account_id)', 'Column(?.accounts.date_month)', 'Column(?.accounts.revenue)'])": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } } ],
      "(\"Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))\", ['Column(?.?.date_month)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
            "sql": "date(date_month, 'start of year')" } },
        { "Expression(./tests/inputs/editor.sql:3:4-3:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/editor.sql:3:4-3:37",
            "sql": "date(date_month, 'start of year')" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))\", ['Column(?.accounts.industry)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
            "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } } ],
      "('Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))', ['Column(?.accounts_revenue.revenue)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
            "sql": "SUM(ar.revenue)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
            "sql": "SUM(accounts_revenue.revenue)" } },
        { "Expression(./tests/inputs/editor.sql:13:4-13:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/editor.sql:13:4-13:19",
            "sql": "SUM(ar.revenue)" } } ],
      "('Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))', ['Column(?.accounts_revenue.account_id)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/editor.sql:14:4-14:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/editor.sql:14:4-14:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } } ],
      "('Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))', ['Column(?.accounts_revenue.account_id)', 'Column(?.accounts_revenue.revenue)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/editor.sql:15:4-15:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/editor.sql:15:4-15:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ],
      "(\"Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))\", ['Column(?.accounts.industry)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
            "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))\", ['Column(?.accounts_revenue.revenue)'])": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
            "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } } ],
      "(\"Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))\", ['Column(?.countries.region)'])": [
        { "Expression(./tests/inputs/editor.sql:5:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "macro_region",
            "location": "./tests/inputs/editor.sql:5:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } } ],
      "(\"Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))\", ['Column(?.accounts.industry)'])": [
        { "Expression(./tests/inputs/editor.sql:12:4-12:62) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_it",
            "location": "./tests/inputs/editor.sql:12:4-12:62",
            "sql": "IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')" } } ] },
    "map_file_to_expr": {
      "./tests/inputs/codebase/0-accounts.sql": [
        { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
            "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
            "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:60:8-60:40) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_day)), Argument('start of month')))": {
            "columns": [ "Column(?.?.date_day)" ],
            "alias": "date_month",
            "location": "./tests/inputs/codebase/0-accounts.sql:60:8-60:40",
            "sql": "DATE(date_day, 'start of month')" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:80:4-85:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Column(?.t.revenue_12m), 300), 'Small'), Casewhen_clause(And(>(Column(?.t.revenue_12m), 300), <=(Column(?.t.revenue_12m), 600)), 'Medium'), Casewhen_clause(>(Column(?.t.revenue_12m), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.t.revenue_12m)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/0-accounts.sql:80:4-85:7",
            "sql": "CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
            "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:103:8-107:9) = Expression(Function_call(Identifier, Argument(Column(?.accounts.revenue)), Analytics_clause(Over_clause(Window_specification(Window_partition_clause(Partition_expression(Column(?.accounts.account_id))), Order_by_clause(Order_by_clause_body(Column(?.accounts.date_month))), Window_frame_clause(Rows_range(), Window_frame_between(Between_from(11), Between_to(Keyword_current_row()))))))))": {
            "columns": [ "Column(?.accounts.account_id)", "Column(?.accounts.date_month)", "Column(?.accounts.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/0-accounts.sql:103:8-107:9",
            "sql": "SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        )" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:27:4-27:36) = Expression(Binary_expression(Column(?.?.revenue), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue)" ],
            "alias": "revenue_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:27:4-27:36",
            "sql": "revenue / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:28:4-28:41) = Expression(Binary_expression(Column(?.?.revenue_core), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_core)" ],
            "alias": "revenue_core_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:28:4-28:41",
            "sql": "revenue_core / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:29:4-29:40) = Expression(Binary_expression(Column(?.?.revenue_aux), Column(?.?.contract_duration_days)))": {
            "columns": [ "Column(?.?.contract_duration_days)", "Column(?.?.revenue_aux)" ],
            "alias": "revenue_aux_day",
            "location": "./tests/inputs/codebase/0-accounts.sql:29:4-29:40",
            "sql": "revenue_aux / contract_duration_days" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:36:8-36:77) = Expression(Binary_expression(-(Julianday(Column(?.deals.contract_end_date)), Julianday(Column(?.deals.contract_start_date))), 1))": {
            "columns": [ "Column(?.deals.contract_end_date)", "Column(?.deals.contract_start_date)" ],
            "alias": "contract_duration_days",
            "location": "./tests/inputs/codebase/0-accounts.sql:36:8-36:77",
            "sql": "julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:39:8-39:20) = Expression(Function_call(Identifier, Argument(Column(?.orders.value))))": {
            "columns": [ "Column(?.orders.value)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:39:8-39:20",
            "sql": "SUM(o.value)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:53:4-53:16) = Expression(Function_call(Identifier, Argument(Column(?.t.deals))))": {
            "columns": [ "Column(?.t.deals)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:53:4-53:16",
            "sql": "AVG(t.deals)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:54:4-54:23) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_core))))": {
            "columns": [ "Column(?.t.revenue_core)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:54:4-54:23",
            "sql": "SUM(t.revenue_core)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:55:4-55:22) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue_aux))))": {
            "columns": [ "Column(?.t.revenue_aux)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:55:4-55:22",
            "sql": "SUM(t.revenue_aux)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:56:4-56:18) = Expression(Function_call(Identifier, Argument(Column(?.t.revenue))))": {
            "columns": [ "Column(?.t.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:56:4-56:18",
            "sql": "SUM(t.revenue)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:62:8-62:25) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.deal_id))))": {
            "columns": [ "Column(?.deals_signed.deal_id)" ],
            "alias": "deals",
            "location": "./tests/inputs/codebase/0-accounts.sql:62:8-62:25",
            "sql": "COUNT(ds.deal_id)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:63:8-63:32) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_core_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_core_day)" ],
            "alias": "revenue_core",
            "location": "./tests/inputs/codebase/0-accounts.sql:63:8-63:32",
            "sql": "SUM(ds.revenue_core_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:64:8-64:31) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_aux_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_aux_day)" ],
            "alias": "revenue_aux",
            "location": "./tests/inputs/codebase/0-accounts.sql:64:8-64:31",
            "sql": "SUM(ds.revenue_aux_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:65:8-65:27) = Expression(Function_call(Identifier, Argument(Column(?.deals_signed.revenue_day))))": {
            "columns": [ "Column(?.deals_signed.revenue_day)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/0-accounts.sql:65:8-65:27",
            "sql": "SUM(ds.revenue_day)" } },
        { "Expression(./tests/inputs/codebase/0-accounts.sql:68:16-69:57) = Expression(Binary_expression(>=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_start_date))), <=(Column(?.date_ranges.date_day), Date(Column(?.deals_signed.contract_end_date)))))": {
            "columns": [ "Column(?.date_ranges.date_day)", "Column(?.deals_signed.contract_end_date)", "Column(?.deals_signed.contract_start_date)" ],
            "alias": null,
            "location": "./tests/inputs/codebase/0-accounts.sql:68:16-69:57",
            "sql": "dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)" } } ],
      "./tests/inputs/codebase/1-revenue.sql": [
        { "Expression(./tests/inputs/codebase/1-revenue.sql:11:4-15:7) = Expression(Casewhen_expression(Casewhen_clause(=(Column(?.accounts.industry), 'Information Technology'), 'Tech'), Casewhen_clause(Unary_expression(Column(?.accounts.industry), Null()), Null()), Caseelse_clause('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:11:4-15:7",
            "sql": "CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_tech",
            "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
            "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:39:4-44:7) = Expression(Casewhen_expression(Casewhen_clause(<=(Sum(Column(?.accounts_revenue.revenue)), 300), 'Small'), Casewhen_clause(And(>(Sum(Column(?.accounts_revenue.revenue)), 300), <=(Sum(Column(?.accounts_revenue.revenue)), 600)), 'Medium'), Casewhen_clause(>(Sum(Column(?.accounts_revenue.revenue)), 600), 'Large'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "account_size",
            "location": "./tests/inputs/codebase/1-revenue.sql:39:4-44:7",
            "sql": "CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:5:4-5:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/codebase/1-revenue.sql:5:4-5:37",
            "sql": "date(date_month, 'start of year')" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "region_cluster",
            "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:17:4-17:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/codebase/1-revenue.sql:17:4-17:19",
            "sql": "SUM(ar.revenue)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:18:4-18:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/codebase/1-revenue.sql:18:4-18:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:19:4-19:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/codebase/1-revenue.sql:19:4-19:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/codebase/1-revenue.sql:45:4-45:33) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_12m",
            "location": "./tests/inputs/codebase/1-revenue.sql:45:4-45:33",
            "sql": "SUM(accounts_revenue.revenue)" } } ],
      "./tests/inputs/editor.sql": [
        { "Expression(./tests/inputs/editor.sql:12:4-12:62) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
            "columns": [ "Column(?.accounts.industry)" ],
            "alias": "industry_it",
            "location": "./tests/inputs/editor.sql:12:4-12:62",
            "sql": "IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')" } },
        { "Expression(./tests/inputs/editor.sql:3:4-3:37) = Expression(Function_call(Identifier(), Argument(Column(?.?.date_month)), Argument('start of year')))": {
            "columns": [ "Column(?.?.date_month)" ],
            "alias": "date_year",
            "location": "./tests/inputs/editor.sql:3:4-3:37",
            "sql": "date(date_month, 'start of year')" } },
        { "Expression(./tests/inputs/editor.sql:5:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
            "columns": [ "Column(?.countries.region)" ],
            "alias": "macro_region",
            "location": "./tests/inputs/editor.sql:5:4-10:7",
            "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } },
        { "Expression(./tests/inputs/editor.sql:13:4-13:19) = Expression(Function_call(Identifier, Argument(Column(?.accounts_revenue.revenue))))": {
            "columns": [ "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue",
            "location": "./tests/inputs/editor.sql:13:4-13:19",
            "sql": "SUM(ar.revenue)" } },
        { "Expression(./tests/inputs/editor.sql:14:4-14:33) = Expression(Function_call(Identifier, Distinct(), Argument(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)" ],
            "alias": "accounts",
            "location": "./tests/inputs/editor.sql:14:4-14:33",
            "sql": "COUNT(DISTINCT ar.account_id)" } },
        { "Expression(./tests/inputs/editor.sql:15:4-15:51) = Expression(Binary_expression(Sum(Column(?.accounts_revenue.revenue)), Count(Column(?.accounts_revenue.account_id))))": {
            "columns": [ "Column(?.accounts_revenue.account_id)", "Column(?.accounts_revenue.revenue)" ],
            "alias": "revenue_per_account",
            "location": "./tests/inputs/editor.sql:15:4-15:51",
            "sql": "SUM(ar.revenue) / COUNT(DISTINCT ar.account_id)" } } ] } } }
```

### src.variations.get_variations (call 1)

```json
[
  { "ExpressionVariations(0-accounts.sql:38:9, 1 variations)": {
      "this": {
        "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
          "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
          "alias": "revenue_core",
          "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
          "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
      "others": [
        { "ExpressionVariation(group=ExpressionGroup(reliability=1, Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86)), similarity=0.90)": {
            "group": {
              "ExpressionGroup(reliability=1, Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86))": {
                "expressions": [
                  { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                      "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                      "alias": "revenue_aux",
                      "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                      "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } } ],
                "repr": "Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))",
                "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                "reliability": 1 } },
            "similarity": 0.9 } } ] } },
  { "ExpressionVariations(0-accounts.sql:39:9, 1 variations)": {
      "this": {
        "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
          "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
          "alias": "revenue_aux",
          "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
          "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
      "others": [
        { "ExpressionVariation(group=ExpressionGroup(reliability=1, Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105)), similarity=0.90)": {
            "group": {
              "ExpressionGroup(reliability=1, Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105))": {
                "expressions": [
                  { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                      "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                      "alias": "revenue_core",
                      "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                      "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } } ],
                "repr": "Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))",
                "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                "reliability": 1 } },
            "similarity": 0.9 } } ] } } ]
```

### src.variations.get_variations (call 2)

```json
[]
```

### src.variations.get_variations (call 3)

```json
[
  { "ExpressionVariations(0-accounts.sql:38:9, 1 variations)": {
      "this": {
        "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
          "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
          "alias": "revenue_core",
          "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
          "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } },
      "others": [
        { "ExpressionVariation(group=ExpressionGroup(reliability=1, Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86)), similarity=0.90)": {
            "group": {
              "ExpressionGroup(reliability=1, Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86))": {
                "expressions": [
                  { "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                      "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                      "alias": "revenue_aux",
                      "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
                      "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } } ],
                "repr": "Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))",
                "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                "reliability": 1 } },
            "similarity": 0.9 } } ] } },
  { "ExpressionVariations(0-accounts.sql:39:9, 1 variations)": {
      "this": {
        "Expression(./tests/inputs/codebase/0-accounts.sql:38:8-38:86) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))": {
          "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
          "alias": "revenue_aux",
          "location": "./tests/inputs/codebase/0-accounts.sql:38:8-38:86",
          "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } },
      "others": [
        { "ExpressionVariation(group=ExpressionGroup(reliability=1, Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105)), similarity=0.90)": {
            "group": {
              "ExpressionGroup(reliability=1, Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105))": {
                "expressions": [
                  { "Expression(./tests/inputs/codebase/0-accounts.sql:37:8-37:105) = Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))": {
                      "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                      "alias": "revenue_core",
                      "location": "./tests/inputs/codebase/0-accounts.sql:37:8-37:105",
                      "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } } ],
                "repr": "Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))",
                "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
                "reliability": 1 } },
            "similarity": 0.9 } } ] } },
  { "ExpressionVariations(0-accounts.sql:98:9, 1 variations)": {
      "this": {
        "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
          "columns": [ "Column(?.countries.region)" ],
          "alias": "region_cluster",
          "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
          "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
      "others": [
        { "ExpressionVariation(group=ExpressionGroup(reliability=1, Expression(./tests/inputs/editor.sql:5:4-10:7)), similarity=0.78)": {
            "group": {
              "ExpressionGroup(reliability=1, Expression(./tests/inputs/editor.sql:5:4-10:7))": {
                "expressions": [
                  { "Expression(./tests/inputs/editor.sql:5:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
                      "columns": [ "Column(?.countries.region)" ],
                      "alias": "macro_region",
                      "location": "./tests/inputs/editor.sql:5:4-10:7",
                      "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } } ],
                "repr": "Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))",
                "columns": [ "Column(?.countries.region)" ],
                "reliability": 1 } },
            "similarity": 0.78 } } ] } } ]
```

### src.variations.get_variations (call 4)

```json
[
  { "ExpressionVariations(1-revenue.sql:33:5, 1 variations)": {
      "this": {
        "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
          "columns": [ "Column(?.countries.region)" ],
          "alias": "cluster",
          "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
          "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
      "others": [
        { "ExpressionVariation(group=ExpressionGroup(reliability=1, Expression(./tests/inputs/editor.sql:5:4-10:7)), similarity=0.78)": {
            "group": {
              "ExpressionGroup(reliability=1, Expression(./tests/inputs/editor.sql:5:4-10:7))": {
                "expressions": [
                  { "Expression(./tests/inputs/editor.sql:5:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
                      "columns": [ "Column(?.countries.region)" ],
                      "alias": "macro_region",
                      "location": "./tests/inputs/editor.sql:5:4-10:7",
                      "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } } ],
                "repr": "Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))",
                "columns": [ "Column(?.countries.region)" ],
                "reliability": 1 } },
            "similarity": 0.78 } } ] } },
  { "ExpressionVariations(1-revenue.sql:39:5, 1 variations)": {
      "this": {
        "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
          "columns": [ "Column(?.accounts.industry)" ],
          "alias": "industry_tech",
          "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
          "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } },
      "others": [
        { "ExpressionVariation(group=ExpressionGroup(reliability=1, Expression(./tests/inputs/editor.sql:12:4-12:62)), similarity=0.95)": {
            "group": {
              "ExpressionGroup(reliability=1, Expression(./tests/inputs/editor.sql:12:4-12:62))": {
                "expressions": [
                  { "Expression(./tests/inputs/editor.sql:12:4-12:62) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
                      "columns": [ "Column(?.accounts.industry)" ],
                      "alias": "industry_it",
                      "location": "./tests/inputs/editor.sql:12:4-12:62",
                      "sql": "IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')" } } ],
                "repr": "Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))",
                "columns": [ "Column(?.accounts.industry)" ],
                "reliability": 1 } },
            "similarity": 0.95 } } ] } },
  { "ExpressionVariations(1-revenue.sql:7:5, 1 variations)": {
      "this": {
        "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
          "columns": [ "Column(?.countries.region)" ],
          "alias": "region_cluster",
          "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
          "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
      "others": [
        { "ExpressionVariation(group=ExpressionGroup(reliability=1, Expression(./tests/inputs/editor.sql:5:4-10:7)), similarity=0.78)": {
            "group": {
              "ExpressionGroup(reliability=1, Expression(./tests/inputs/editor.sql:5:4-10:7))": {
                "expressions": [
                  { "Expression(./tests/inputs/editor.sql:5:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
                      "columns": [ "Column(?.countries.region)" ],
                      "alias": "macro_region",
                      "location": "./tests/inputs/editor.sql:5:4-10:7",
                      "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } } ],
                "repr": "Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))",
                "columns": [ "Column(?.countries.region)" ],
                "reliability": 1 } },
            "similarity": 0.78 } } ] } } ]
```

### src.variations.get_variations (call 5)

```json
[
  { "ExpressionVariations(editor.sql:13:5, 1 variations)": {
      "this": {
        "Expression(./tests/inputs/editor.sql:12:4-12:62) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))": {
          "columns": [ "Column(?.accounts.industry)" ],
          "alias": "industry_it",
          "location": "./tests/inputs/editor.sql:12:4-12:62",
          "sql": "IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')" } },
      "others": [
        { "ExpressionVariation(group=ExpressionGroup(reliability=1, Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70)), similarity=0.95)": {
            "group": {
              "ExpressionGroup(reliability=1, Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70))": {
                "expressions": [
                  { "Expression(./tests/inputs/codebase/1-revenue.sql:38:4-38:70) = Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))": {
                      "columns": [ "Column(?.accounts.industry)" ],
                      "alias": "industry_tech",
                      "location": "./tests/inputs/codebase/1-revenue.sql:38:4-38:70",
                      "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } } ],
                "repr": "Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))",
                "columns": [ "Column(?.accounts.industry)" ],
                "reliability": 1 } },
            "similarity": 0.95 } } ] } },
  { "ExpressionVariations(editor.sql:6:5, 1 variations)": {
      "this": {
        "Expression(./tests/inputs/editor.sql:5:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))": {
          "columns": [ "Column(?.countries.region)" ],
          "alias": "macro_region",
          "location": "./tests/inputs/editor.sql:5:4-10:7",
          "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } },
      "others": [
        { "ExpressionVariation(group=ExpressionGroup(reliability=3, Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11), Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7), Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7)), similarity=0.78)": {
            "group": {
              "ExpressionGroup(reliability=3, Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11), Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7), Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7))": {
                "expressions": [
                  { "Expression(./tests/inputs/codebase/0-accounts.sql:97:8-101:11) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                      "columns": [ "Column(?.countries.region)" ],
                      "alias": "region_cluster",
                      "location": "./tests/inputs/codebase/0-accounts.sql:97:8-101:11",
                      "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" } },
                  { "Expression(./tests/inputs/codebase/1-revenue.sql:32:4-36:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                      "columns": [ "Column(?.countries.region)" ],
                      "alias": "cluster",
                      "location": "./tests/inputs/codebase/1-revenue.sql:32:4-36:7",
                      "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } },
                  { "Expression(./tests/inputs/codebase/1-revenue.sql:6:4-10:7) = Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))": {
                      "columns": [ "Column(?.countries.region)" ],
                      "alias": "region_cluster",
                      "location": "./tests/inputs/codebase/1-revenue.sql:6:4-10:7",
                      "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } } ],
                "repr": "Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))",
                "columns": [ "Column(?.countries.region)" ],
                "reliability": 3 } },
            "similarity": 0.78 } } ] } } ]
```

## Client-Server Exchange

### client->server: initialize

```json
{
  "id": 0,
  "params": {
    "capabilities": {
      "workspace": {
        "applyEdit": true,
        "workspaceEdit": {
          "documentChanges": true,
          "resourceOperations": [ "create", "delete", "rename" ],
          "failureHandling": "textOnlyTransactional",
          "normalizesLineEndings": true,
          "changeAnnotationSupport": { "groupsOnLabel": true } },
        "didChangeConfiguration": { "dynamicRegistration": true },
        "didChangeWatchedFiles": {
          "dynamicRegistration": true,
          "relativePatternSupport": true },
        "symbol": {
          "dynamicRegistration": true,
          "symbolKind": {
            "valueSet": [ 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 3, 4, 5, 6, 7, 8, 9 ] },
          "tagSupport": {
            "valueSet": [ 1 ] },
          "resolveSupport": {
            "properties": [ "location.range" ] } },
        "executeCommand": { "dynamicRegistration": true },
        "workspaceFolders": true,
        "configuration": true,
        "semanticTokens": { "refreshSupport": true },
        "codeLens": { "refreshSupport": true },
        "fileOperations": {
          "dynamicRegistration": true,
          "didCreate": true,
          "willCreate": true,
          "didRename": true,
          "willRename": true,
          "didDelete": true,
          "willDelete": true },
        "inlineValue": { "refreshSupport": true },
        "inlayHint": { "refreshSupport": true },
        "diagnostics": { "refreshSupport": true },
        "foldingRange": { "refreshSupport": true } },
      "textDocument": {
        "synchronization": {
          "dynamicRegistration": true,
          "willSave": true,
          "willSaveWaitUntil": true,
          "didSave": true },
        "completion": {
          "dynamicRegistration": true,
          "completionItem": {
            "snippetSupport": true,
            "commitCharactersSupport": true,
            "documentationFormat": [ "markdown", "plaintext" ],
            "deprecatedSupport": true,
            "preselectSupport": true,
            "tagSupport": {
              "valueSet": [ 1 ] },
            "insertReplaceSupport": true,
            "resolveSupport": {
              "properties": [ "additionalTextEdits", "detail", "documentation" ] },
            "insertTextModeSupport": {
              "valueSet": [ 1, 2 ] },
            "labelDetailsSupport": true },
          "completionItemKind": {
            "valueSet": [ 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 3, 4, 5, 6, 7, 8, 9 ] },
          "insertTextMode": 2,
          "contextSupport": true,
          "completionList": {
            "itemDefaults": [ "commitCharacters", "data", "editRange", "insertTextFormat", "insertTextMode" ] } },
        "hover": {
          "dynamicRegistration": true,
          "contentFormat": [ "markdown", "plaintext" ] },
        "signatureHelp": {
          "dynamicRegistration": true,
          "signatureInformation": {
            "documentationFormat": [ "markdown", "plaintext" ],
            "parameterInformation": { "labelOffsetSupport": true },
            "activeParameterSupport": true },
          "contextSupport": true },
        "declaration": {
          "dynamicRegistration": true,
          "linkSupport": true },
        "definition": {
          "dynamicRegistration": true,
          "linkSupport": true },
        "typeDefinition": {
          "dynamicRegistration": true,
          "linkSupport": true },
        "implementation": {
          "dynamicRegistration": true,
          "linkSupport": true },
        "references": { "dynamicRegistration": true },
        "documentHighlight": { "dynamicRegistration": true },
        "documentSymbol": {
          "dynamicRegistration": true,
          "symbolKind": {
            "valueSet": [ 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 3, 4, 5, 6, 7, 8, 9 ] },
          "hierarchicalDocumentSymbolSupport": true,
          "tagSupport": {
            "valueSet": [ 1 ] },
          "labelSupport": true },
        "codeAction": {
          "dynamicRegistration": true,
          "codeActionLiteralSupport": {
            "codeActionKind": {
              "valueSet": [ "", "quickfix", "refactor", "refactor.extract", "refactor.inline", "refactor.rewrite", "source", "source.organizeImports" ] } },
          "isPreferredSupport": true,
          "disabledSupport": true,
          "dataSupport": true,
          "resolveSupport": {
            "properties": [ "edit" ] },
          "honorsChangeAnnotations": true },
        "codeLens": { "dynamicRegistration": true },
        "documentLink": {
          "dynamicRegistration": true,
          "tooltipSupport": true },
        "colorProvider": { "dynamicRegistration": true },
        "formatting": { "dynamicRegistration": true },
        "rangeFormatting": {
          "dynamicRegistration": true,
          "rangesSupport": true },
        "onTypeFormatting": { "dynamicRegistration": true },
        "rename": {
          "dynamicRegistration": true,
          "prepareSupport": true,
          "prepareSupportDefaultBehavior": 1,
          "honorsChangeAnnotations": true },
        "foldingRange": {
          "dynamicRegistration": true,
          "rangeLimit": 5000,
          "lineFoldingOnly": true,
          "foldingRangeKind": {
            "valueSet": [ "comment", "imports", "region" ] },
          "foldingRange": { "collapsedText": false } },
        "selectionRange": { "dynamicRegistration": true },
        "publishDiagnostics": {
          "relatedInformation": true,
          "tagSupport": {
            "valueSet": [ 1, 2 ] },
          "versionSupport": false,
          "codeDescriptionSupport": true,
          "dataSupport": true },
        "callHierarchy": { "dynamicRegistration": true },
        "semanticTokens": {
          "requests": {
            "range": true,
            "full": { "delta": true } },
          "tokenTypes": [ "class", "comment", "decorator", "enum", "enumMember", "event", "function", "interface", "keyword", "macro", "method", "modifier", "namespace", "number", "operator", "parameter", "property", "regexp", "string", "struct", "type", "typeParameter", "variable" ],
          "tokenModifiers": [ "abstract", "async", "declaration", "defaultLibrary", "definition", "deprecated", "documentation", "modification", "readonly", "static" ],
          "formats": [ "relative" ],
          "dynamicRegistration": true,
          "overlappingTokenSupport": false,
          "multilineTokenSupport": false,
          "serverCancelSupport": true,
          "augmentsSyntaxTokens": true },
        "linkedEditingRange": { "dynamicRegistration": true },
        "typeHierarchy": { "dynamicRegistration": true },
        "inlineValue": { "dynamicRegistration": true },
        "inlayHint": {
          "dynamicRegistration": true,
          "resolveSupport": {
            "properties": [ "label.command", "label.location", "label.tooltip", "textEdits", "tooltip" ] } },
        "diagnostic": {
          "dynamicRegistration": true,
          "relatedDocumentSupport": false } },
      "notebookDocument": {
        "synchronization": {
          "dynamicRegistration": true,
          "executionSummarySupport": true } },
      "window": {
        "workDoneProgress": true,
        "showMessage": {
          "messageActionItem": { "additionalPropertiesSupport": true } },
        "showDocument": { "support": true } },
      "general": {
        "staleRequestSupport": {
          "cancel": true,
          "retryOnContentModified": [ "textDocument/semanticTokens/full", "textDocument/semanticTokens/full/delta", "textDocument/semanticTokens/range" ] },
        "regularExpressions": {
          "engine": "ECMAScript",
          "version": "ES2020" },
        "markdown": {
          "parser": "marked",
          "version": "1.1.0" },
        "positionEncodings": [ "utf-16" ] } },
    "processId": 77807,
    "rootPath": "./tests/inputs/codebase",
    "rootUri": "file://./tests/inputs/codebase",
    "workspaceFolders": [
      { "uri": "file://./tests/inputs/codebase",
        "name": "codebase" } ],
    "clientInfo": {
      "name": "Visual Studio Code",
      "version": "1.100.2" },
    "locale": "en",
    "trace": "off" },
  "method": "initialize",
  "jsonrpc": "2.0" }
```

### client->server: initialized

```json
{
  "params": {},
  "method": "initialized",
  "jsonrpc": "2.0" }
```

### client->server: textDocument/didOpen

```json
{
  "params": {
    "textDocument": {
      "uri": "file://./tests/inputs/editor.sql",
      "languageId": "sql",
      "version": 1,
      "text": "-- CASE: Different groupings or thresholds applied to columns\n\nSELECT \n    date(date_month, 'start of year') AS date_year,\n    -- This should cause an error\n    CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END AS macro_region,\n    -- This should case an error\n    IIF(a.industry = 'Information Technology', 'IT', 'Non-IT') AS industry_it,\n    SUM(ar.revenue) AS revenue,\n    COUNT(DISTINCT ar.account_id) AS accounts,\n    SUM(ar.revenue) / COUNT(DISTINCT ar.account_id) AS revenue_per_account\nFROM accounts_revenue ar\n    LEFT JOIN accounts a USING (account_id)\n    LEFT JOIN countries c USING (country)\nWHERE\n    -- This is appropriate, user can do ad-hoc filters for any subsets\n    a.industry IN ('Information Technology', 'Telecommunication Services')\n    -- This is appropriate, user can take any period\n    AND date_month BETWEEN DATE('now', '-24 months') AND DATE('now')\nGROUP BY date_year, macro_region, industry_it" } },
  "method": "textDocument/didOpen",
  "jsonrpc": "2.0" }
```

### server->client: sql-refinery/variations (notification)

```json
{
  "uri": "file://./tests/inputs/editor.sql",
  "variations": [
    { "this": {
        "columns": [
          { "dataset": null,
            "table": "accounts",
            "column": "industry" } ],
        "alias": "industry_it",
        "location": {
          "file": "./tests/inputs/editor.sql",
          "range": {
            "start_line": 12,
            "start_char": 4,
            "end_line": 12,
            "end_char": 62 } },
        "sql": "IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')" },
      "others": [
        { "group": {
            "expressions": [
              { "columns": [
                  { "dataset": null,
                    "table": "accounts",
                    "column": "industry" } ],
                "alias": "industry_tech",
                "location": {
                  "file": "./tests/inputs/codebase/1-revenue.sql",
                  "range": {
                    "start_line": 38,
                    "start_char": 4,
                    "end_line": 38,
                    "end_char": 70 } },
                "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" } ],
            "repr": "Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('Tech'), Argument('Other')))",
            "columns": [ "Column(?.accounts.industry)" ],
            "reliability": 1 },
          "similarity": 0.95 } ] },
    { "this": {
        "columns": [
          { "dataset": null,
            "table": "countries",
            "column": "region" } ],
        "alias": "macro_region",
        "location": {
          "file": "./tests/inputs/editor.sql",
          "range": {
            "start_line": 5,
            "start_char": 4,
            "end_line": 10,
            "end_char": 7 } },
        "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" },
      "others": [
        { "group": {
            "expressions": [
              { "columns": [
                  { "dataset": null,
                    "table": "countries",
                    "column": "region" } ],
                "alias": "cluster",
                "location": {
                  "file": "./tests/inputs/codebase/1-revenue.sql",
                  "range": {
                    "start_line": 32,
                    "start_char": 4,
                    "end_line": 36,
                    "end_char": 7 } },
                "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" },
              { "columns": [
                  { "dataset": null,
                    "table": "countries",
                    "column": "region" } ],
                "alias": "region_cluster",
                "location": {
                  "file": "./tests/inputs/codebase/0-accounts.sql",
                  "range": {
                    "start_line": 97,
                    "start_char": 8,
                    "end_line": 101,
                    "end_char": 11 } },
                "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" },
              { "columns": [
                  { "dataset": null,
                    "table": "countries",
                    "column": "region" } ],
                "alias": "region_cluster",
                "location": {
                  "file": "./tests/inputs/codebase/1-revenue.sql",
                  "range": {
                    "start_line": 6,
                    "start_char": 4,
                    "end_line": 10,
                    "end_char": 7 } },
                "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" } ],
            "repr": "Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), Struct('Americas', 'Europe')), 'North-West'), Casewhen_clause(In(Column(?.countries.region), Struct('Africa', 'Asia')), 'South-East'), Caseelse_clause(Null())))",
            "columns": [ "Column(?.countries.region)" ],
            "reliability": 3 },
          "similarity": 0.78 } ] } ] }
```

### client->server: textDocument/didOpen

```json
{
  "params": {
    "textDocument": {
      "uri": "file://./tests/inputs/codebase/1-revenue.sql",
      "languageId": "sql",
      "version": 1,
      "text": "-- REVENUE REPORTS\n\n-- Revenue by region, cluster, account size\n\nSELECT \n    date(date_month, 'start of year') AS date_year,\n    CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END AS region_cluster,\n    CASE \n        WHEN a.industry = 'Information Technology' THEN 'Tech'\n        WHEN a.industry IS NULL THEN NULL\n        ELSE 'Other'\n    END AS industry_cluster,\n    a360.account_size,\n    SUM(ar.revenue) AS revenue,\n    COUNT(DISTINCT ar.account_id) AS accounts,\n    SUM(ar.revenue) / COUNT(DISTINCT ar.account_id) AS revenue_per_account\nFROM accounts_revenue ar\n    LEFT JOIN accounts a USING (account_id)\n    LEFT JOIN countries c USING (country)\n    LEFT JOIN accounts_360 a360 USING (account_id, date_month)\nGROUP BY date_year, region_cluster, industry_cluster, a360.account_size\nORDER BY date_year, region_cluster, industry_cluster;\n\n-- Accounts snapshot performance\n\nSELECT\n    accounts.name,\n    region,\n    CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END AS cluster,\n    accounts.industry AS industry,\n    IIF(accounts.industry = 'Information Technology', 'Tech', 'Other') AS industry_tech,\n    CASE \n        WHEN SUM(accounts_revenue.revenue) <= 300 THEN 'Small'\n        WHEN SUM(accounts_revenue.revenue) > 300 AND SUM(accounts_revenue.revenue) <= 600 THEN 'Medium'\n        WHEN SUM(accounts_revenue.revenue) > 600 THEN 'Large'\n        ELSE NULL\n    END AS account_size,\n    SUM(accounts_revenue.revenue) AS revenue_12m\nFROM accounts\n    LEFT JOIN accounts_revenue USING (account_id)\n    LEFT JOIN countries c USING (country)\nWHERE accounts_revenue.date_month BETWEEN DATE('now', '-12 months') AND DATE('now')\nGROUP BY accounts.name, region, accounts.industry;" } },
  "method": "textDocument/didOpen",
  "jsonrpc": "2.0" }
```

### server->client: sql-refinery/variations (notification)

```json
{
  "uri": "file://./tests/inputs/codebase/1-revenue.sql",
  "variations": [
    { "this": {
        "columns": [
          { "dataset": null,
            "table": "accounts",
            "column": "industry" } ],
        "alias": "industry_tech",
        "location": {
          "file": "./tests/inputs/codebase/1-revenue.sql",
          "range": {
            "start_line": 38,
            "start_char": 4,
            "end_line": 38,
            "end_char": 70 } },
        "sql": "IIF(accounts.industry = 'Information Technology', 'Tech', 'Other')" },
      "others": [
        { "group": {
            "expressions": [
              { "columns": [
                  { "dataset": null,
                    "table": "accounts",
                    "column": "industry" } ],
                "alias": "industry_it",
                "location": {
                  "file": "./tests/inputs/editor.sql",
                  "range": {
                    "start_line": 12,
                    "start_char": 4,
                    "end_line": 12,
                    "end_char": 62 } },
                "sql": "IIF(a.industry = 'Information Technology', 'IT', 'Non-IT')" } ],
            "repr": "Expression(Function_call(Identifier, Argument(=(Column(?.accounts.industry), 'Information Technology')), Argument('IT'), Argument('Non-IT')))",
            "columns": [ "Column(?.accounts.industry)" ],
            "reliability": 1 },
          "similarity": 0.95 } ] },
    { "this": {
        "columns": [
          { "dataset": null,
            "table": "countries",
            "column": "region" } ],
        "alias": "cluster",
        "location": {
          "file": "./tests/inputs/codebase/1-revenue.sql",
          "range": {
            "start_line": 32,
            "start_char": 4,
            "end_line": 36,
            "end_char": 7 } },
        "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" },
      "others": [
        { "group": {
            "expressions": [
              { "columns": [
                  { "dataset": null,
                    "table": "countries",
                    "column": "region" } ],
                "alias": "macro_region",
                "location": {
                  "file": "./tests/inputs/editor.sql",
                  "range": {
                    "start_line": 5,
                    "start_char": 4,
                    "end_line": 10,
                    "end_char": 7 } },
                "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } ],
            "repr": "Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))",
            "columns": [ "Column(?.countries.region)" ],
            "reliability": 1 },
          "similarity": 0.78 } ] },
    { "this": {
        "columns": [
          { "dataset": null,
            "table": "countries",
            "column": "region" } ],
        "alias": "region_cluster",
        "location": {
          "file": "./tests/inputs/codebase/1-revenue.sql",
          "range": {
            "start_line": 6,
            "start_char": 4,
            "end_line": 10,
            "end_char": 7 } },
        "sql": "CASE\n        WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n        WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n        ELSE NULL\n    END" },
      "others": [
        { "group": {
            "expressions": [
              { "columns": [
                  { "dataset": null,
                    "table": "countries",
                    "column": "region" } ],
                "alias": "macro_region",
                "location": {
                  "file": "./tests/inputs/editor.sql",
                  "range": {
                    "start_line": 5,
                    "start_char": 4,
                    "end_line": 10,
                    "end_char": 7 } },
                "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } ],
            "repr": "Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))",
            "columns": [ "Column(?.countries.region)" ],
            "reliability": 1 },
          "similarity": 0.78 } ] } ] }
```

### client->server: textDocument/didOpen

```json
{
  "params": {
    "textDocument": {
      "uri": "file://./tests/inputs/codebase/0-accounts.sql",
      "languageId": "sql",
      "version": 1,
      "text": "-- FOUNDATIONAL TABLES\n\n-- Calendar scaffolding: one day per row\n\nDROP TABLE IF EXISTS date_ranges;\nCREATE TABLE date_ranges AS\nWITH RECURSIVE date_ranges(date_day) AS (\n    SELECT \n        date(MIN(CASE WHEN d.stage_date < d.contract_start_date THEN d.stage_date ELSE d.contract_start_date END)) AS date_month\n    FROM deals d\n    UNION ALL\n    SELECT \n        date(date_day, '+1 day')\n    FROM date_ranges\n    WHERE date_day < (SELECT date(MAX(CASE WHEN d.contract_end_date > d.stage_date THEN d.contract_end_date ELSE d.stage_date END)) FROM deals d)\n)\nSELECT \n    date_day\nFROM date_ranges\nGROUP BY date_day;\n\n-- Currently active signed deals (stage=4) and daily revenue\n\nDROP TABLE IF EXISTS deals_signed;\nCREATE TABLE deals_signed AS\nSELECT \n    *,\n    revenue / contract_duration_days AS revenue_day,\n    revenue_core / contract_duration_days AS revenue_core_day,\n    revenue_aux / contract_duration_days AS revenue_aux_day\nFROM (\n    SELECT \n        d.deal_id,\n        d.account_id,\n        d.contract_start_date,\n        d.contract_end_date,\n        julianday(d.contract_end_date) - julianday(d.contract_start_date) + 1 AS contract_duration_days,\n        SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END) AS revenue_core,\n        SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END) AS revenue_aux,\n        SUM(o.value) AS revenue\n    FROM orders o\n        JOIN deals d USING (deal_id, order_id)\n    WHERE d.stage = 4\n    GROUP BY d.deal_id, d.account_id, d.contract_start_date, d.contract_end_date\n) AS t;\n\n-- Revenue per account per month\n\nDROP TABLE IF EXISTS accounts_revenue;\nCREATE TABLE accounts_revenue AS\nSELECT \n    t.date_month,\n    t.account_id,\n    AVG(t.deals) AS deals,\n    SUM(t.revenue_core) AS revenue_core,\n    SUM(t.revenue_aux) AS revenue_aux,\n    SUM(t.revenue) AS revenue\nFROM (\n    SELECT \n        dr.date_day,\n        DATE(date_day, 'start of month') AS date_month,\n        ds.account_id,\n        COUNT(ds.deal_id) AS deals,\n        SUM(ds.revenue_core_day) AS revenue_core,\n        SUM(ds.revenue_aux_day) AS revenue_aux,\n        SUM(ds.revenue_day) AS revenue\n    FROM date_ranges dr\n        LEFT JOIN deals_signed ds \n            ON  dr.date_day >= date(ds.contract_start_date)\n            AND dr.date_day <= date(ds.contract_end_date)\n    GROUP BY dr.date_day, ds.account_id) t\nGROUP BY account_id, date_month;\n\n\n-- Key information by account as of now\n\nDROP TABLE IF EXISTS accounts_360;\nCREATE TABLE accounts_360 AS\nSELECT \n    t.*,\n    CASE \n        WHEN t.revenue_12m <= 300 THEN 'Small'\n        WHEN t.revenue_12m > 300 AND t.revenue_12m <= 600 THEN 'Medium'\n        WHEN t.revenue_12m > 600 THEN 'Large'\n        ELSE NULL\n    END AS account_size\nFROM (\n    SELECT \n        account_id,\n        date_month,\n        revenue,\n        revenue_core,\n        revenue_aux,\n        deals,\n        accounts.name,\n        accounts.industry,\n        accounts.country,\n        CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END AS region_cluster,\n        accounts.priority,\n        SUM(revenue) OVER (\n            PARTITION BY account_id \n            ORDER BY date_month \n            ROWS BETWEEN 11 PRECEDING AND CURRENT ROW\n        ) AS revenue_12m\n    FROM accounts_revenue\n        JOIN accounts USING (account_id)\n        LEFT JOIN countries c USING (country)\n) AS t;" } },
  "method": "textDocument/didOpen",
  "jsonrpc": "2.0" }
```

### server->client: sql-refinery/variations (notification)

```json
{
  "uri": "file://./tests/inputs/codebase/0-accounts.sql",
  "variations": [
    { "this": {
        "columns": [
          { "dataset": null,
            "table": "countries",
            "column": "region" } ],
        "alias": "region_cluster",
        "location": {
          "file": "./tests/inputs/codebase/0-accounts.sql",
          "range": {
            "start_line": 97,
            "start_char": 8,
            "end_line": 101,
            "end_char": 11 } },
        "sql": "CASE\n            WHEN c.region IN ('Americas', 'Europe') THEN 'North-West'\n            WHEN c.region IN ('Africa', 'Asia') THEN 'South-East'\n            ELSE NULL\n        END" },
      "others": [
        { "group": {
            "expressions": [
              { "columns": [
                  { "dataset": null,
                    "table": "countries",
                    "column": "region" } ],
                "alias": "macro_region",
                "location": {
                  "file": "./tests/inputs/editor.sql",
                  "range": {
                    "start_line": 5,
                    "start_char": 4,
                    "end_line": 10,
                    "end_char": 7 } },
                "sql": "CASE\n        WHEN c.region IN ('Americas') THEN 'AMER'\n        WHEN c.region IN ('Europe', 'Africa') THEN 'EMEA'\n        WHEN c.region = 'Asia' THEN 'APAC'\n        ELSE NULL\n    END" } ],
            "repr": "Expression(Casewhen_expression(Casewhen_clause(In(Column(?.countries.region), 'Americas'), 'AMER'), Casewhen_clause(In(Column(?.countries.region), Struct('Europe', 'Africa')), 'EMEA'), Casewhen_clause(=(Column(?.countries.region), 'Asia'), 'APAC'), Caseelse_clause(Null())))",
            "columns": [ "Column(?.countries.region)" ],
            "reliability": 1 },
          "similarity": 0.78 } ] },
    { "this": {
        "columns": [
          { "dataset": null,
            "table": "orders",
            "column": "product" },
          { "dataset": null,
            "table": "orders",
            "column": "value" } ],
        "alias": "revenue_aux",
        "location": {
          "file": "./tests/inputs/codebase/0-accounts.sql",
          "range": {
            "start_line": 38,
            "start_char": 8,
            "end_line": 38,
            "end_char": 86 } },
        "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" },
      "others": [
        { "group": {
            "expressions": [
              { "columns": [
                  { "dataset": null,
                    "table": "orders",
                    "column": "product" },
                  { "dataset": null,
                    "table": "orders",
                    "column": "value" } ],
                "alias": "revenue_core",
                "location": {
                  "file": "./tests/inputs/codebase/0-accounts.sql",
                  "range": {
                    "start_line": 37,
                    "start_char": 8,
                    "end_line": 37,
                    "end_char": 105 } },
                "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" } ],
            "repr": "Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Subscription Base', 'Subscription Premium')), Column(?.orders.value)), Caseelse_clause(0)))))",
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "reliability": 1 },
          "similarity": 0.9 } ] },
    { "this": {
        "columns": [
          { "dataset": null,
            "table": "orders",
            "column": "product" },
          { "dataset": null,
            "table": "orders",
            "column": "value" } ],
        "alias": "revenue_core",
        "location": {
          "file": "./tests/inputs/codebase/0-accounts.sql",
          "range": {
            "start_line": 37,
            "start_char": 8,
            "end_line": 37,
            "end_char": 105 } },
        "sql": "SUM(CASE WHEN o.product IN ('Subscription Base', 'Subscription Premium') THEN o.value ELSE 0 END)" },
      "others": [
        { "group": {
            "expressions": [
              { "columns": [
                  { "dataset": null,
                    "table": "orders",
                    "column": "product" },
                  { "dataset": null,
                    "table": "orders",
                    "column": "value" } ],
                "alias": "revenue_aux",
                "location": {
                  "file": "./tests/inputs/codebase/0-accounts.sql",
                  "range": {
                    "start_line": 38,
                    "start_char": 8,
                    "end_line": 38,
                    "end_char": 86 } },
                "sql": "SUM(CASE WHEN o.product IN ('Training', 'Consulting') THEN o.value ELSE 0 END)" } ],
            "repr": "Expression(Function_call(Identifier, Argument(Casewhen_expression(Casewhen_clause(In(Column(?.orders.product), Struct('Training', 'Consulting')), Column(?.orders.value)), Caseelse_clause(0)))))",
            "columns": [ "Column(?.orders.product)", "Column(?.orders.value)" ],
            "reliability": 1 },
          "similarity": 0.9 } ] } ] }
```

### client->server: textDocument/didClose

```json
{
  "params": {
    "textDocument": { "uri": "file://./tests/inputs/codebase/0-accounts.sql" } },
  "method": "textDocument/didClose",
  "jsonrpc": "2.0" }
```

### client->server: textDocument/didClose

```json
{
  "params": {
    "textDocument": { "uri": "file://./tests/inputs/editor.sql" } },
  "method": "textDocument/didClose",
  "jsonrpc": "2.0" }
```

### client->server: textDocument/didClose

```json
{
  "params": {
    "textDocument": { "uri": "file://./tests/inputs/codebase/1-revenue.sql" } },
  "method": "textDocument/didClose",
  "jsonrpc": "2.0" }
```

### client->server: shutdown

```json
{
  "id": 5,
  "method": "shutdown",
  "jsonrpc": "2.0" }
```

### client->server: exit

```json
{
  "method": "exit",
  "jsonrpc": "2.0" }
```
