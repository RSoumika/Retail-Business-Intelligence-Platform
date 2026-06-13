-- Top Products by Revenue

SELECT
    product_name,
    ROUND(SUM(sales),2) AS revenue,
    ROUND(SUM(profit),2) AS profit
FROM superstore
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;

-- Top Products by Profit

SELECT
    product_name,
    ROUND(SUM(profit),2) AS total_profit
FROM superstore
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 10;