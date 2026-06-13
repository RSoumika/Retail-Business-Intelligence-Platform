-- Category Analysis

SELECT
    category,
    ROUND(SUM(sales),2) AS revenue,
    ROUND(SUM(profit),2) AS profit
FROM superstore
GROUP BY category
ORDER BY revenue DESC;