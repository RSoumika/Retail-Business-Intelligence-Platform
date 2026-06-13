-- Discount Impact

SELECT
    discount,
    ROUND(AVG(profit),2) AS avg_profit,
    COUNT(*) AS transactions
FROM superstore
GROUP BY discount
ORDER BY discount;

-- Yearly Sales Trend

SELECT
    YEAR(order_date_clean) AS year,
    ROUND(SUM(sales),2) AS revenue,
    ROUND(SUM(profit),2) AS profit
FROM superstore
GROUP BY YEAR(order_date_clean)
ORDER BY year;