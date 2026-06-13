-- Revenue and Profit by Region

SELECT
    region,
    ROUND(SUM(sales),2) AS revenue,
    ROUND(SUM(profit),2) AS profit
FROM superstore
GROUP BY region
ORDER BY revenue DESC;

-- Revenue and Profit by State

SELECT
    state,
    ROUND(SUM(sales),2) AS revenue,
    ROUND(SUM(profit),2) AS profit
FROM superstore
GROUP BY state
ORDER BY revenue DESC;