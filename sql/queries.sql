SELECT *
FROM aum_by_fund_house
ORDER BY aum_cr DESC
LIMIT 5;

SELECT
strftime('%Y-%m',date) month,
AVG(nav)
FROM nav_history
GROUP BY 1;

SELECT
month,
AVG(yoy_growth_pct)
FROM monthly_sip_inflows
GROUP BY month;

SELECT
state,
COUNT(*)
FROM investor_transactions
GROUP BY state
ORDER BY 2 DESC;

SELECT
scheme_name,
expense_ratio
FROM scheme_performance
WHERE expense_ratio < 1;

SELECT *
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

SELECT *
FROM scheme_performance
ORDER BY return_5y DESC
LIMIT 10;

SELECT
risk_grade,
COUNT(*)
FROM fund_master
GROUP BY risk_grade;

SELECT
AVG(amount)
FROM investor_transactions;

SELECT *
FROM category_inflows
ORDER BY inflow_cr DESC;

