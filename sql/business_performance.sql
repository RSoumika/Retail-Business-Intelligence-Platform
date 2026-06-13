-- Total Revenue, Profit and Orders

SELECT
    ROUND(SUM(sales),2) AS total_revenue,
    ROUND(SUM(profit),2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders
FROM superstore;

-- Profit Margin

SELECT
    ROUND((SUM(profit)/SUM(sales))*100,2) AS profit_margin
FROM superstore;