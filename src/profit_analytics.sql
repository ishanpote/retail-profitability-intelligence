-- ====================================================================
-- RETAIL PERFORMANCE & PROFITABILITY ANALYTICAL QUERIES
-- ====================================================================

-- Query 1: The Corporate Profitability Matrix
-- Objective: Rank categories and sub-categories by overall Profit Ratio (Profit / Sales)
SELECT 
    category,
    sub_category,
    ROUND(SUM(sales), 2) AS gross_revenue,
    ROUND(SUM(profit), 2) AS net_profit,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_ratio_percentage
FROM orders_fact
GROUP BY category, sub_category
ORDER BY profit_ratio_percentage DESC;


-- Query 2: The Discount Leak Analysis Matrix
-- Objective: Evaluate if high discount rates are destroying regional margins
SELECT 
    region,
    ROUND(AVG(discount) * 100, 2) AS average_discount_given,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS regional_profit_ratio
FROM orders_fact
GROUP BY region
ORDER BY regional_profit_ratio ASC;