-- 1. Total sales
SELECT SUM(sales_amount) AS total_sales FROM sales;

-- 2. Top 5 products by revenue
SELECT product_name, SUM(sales_amount) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 5;

-- 3. Sales by region
SELECT region, SUM(sales_amount) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- 4. Monthly sales
SELECT DATE_TRUNC('month', order_date)::date AS sales_month,
       SUM(sales_amount) AS total_sales
FROM sales
GROUP BY sales_month
ORDER BY sales_month;

-- 5. Products with sales greater than 10000
SELECT product_name, SUM(sales_amount) AS total_sales
FROM sales
GROUP BY product_name
HAVING SUM(sales_amount) > 10000
ORDER BY total_sales DESC;
