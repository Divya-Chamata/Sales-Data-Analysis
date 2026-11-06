-- PostgreSQL table for the practice sales dataset
CREATE TABLE sales (
    order_id VARCHAR(20),
    order_date DATE,
    product_name VARCHAR(100),
    category VARCHAR(100),
    quantity INTEGER,
    unit_price NUMERIC(12,2),
    region VARCHAR(50),
    sales_amount NUMERIC(14,2)
);

-- After creating the table, import data/sales_cleaned.csv using your SQL tool's import feature.
