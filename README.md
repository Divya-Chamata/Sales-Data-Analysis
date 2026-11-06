# Sales Data Analysis (Python, SQL and Excel)

## Project overview
This is a self-driven practice project using a **synthetic sample sales dataset**. It demonstrates basic data cleaning and analysis workflows. It does not contain company or customer data.

## Project structure
- `data/sales_raw.csv` — sample raw sales data with an intentional duplicate and missing region value
- `excel/sales_analysis.xlsx` — workbook with raw, cleaned, monthly, product and region analysis sheets
- `python/clean_data.py` — removes duplicate rows and rows with a missing region
- `python/analyze_sales.py` — calculates total, product, regional and monthly sales
- `sql/schema.sql` — PostgreSQL table definition
- `sql/analysis_queries.sql` — example SQL analysis queries
- `requirements.txt` — Python dependencies

## Run the Python scripts
1. Install Python.
2. Open a terminal in the project root.
3. Install dependencies: `pip install -r requirements.txt`
4. Run cleaning: `python python/clean_data.py`
5. Run analysis: `python python/analyze_sales.py`

## SQL practice
1. Create a database in PostgreSQL.
2. Run `sql/schema.sql`.
3. Import `data/sales_cleaned.csv` into the `sales` table using your SQL client's CSV import feature.
4. Run the queries in `sql/analysis_queries.sql`.

## Excel
Open `excel/sales_analysis.xlsx`. It contains separate sheets for raw data, cleaned data, monthly sales, product sales and region sales.

## Skills practised
Excel data review and summaries, Python with pandas, SQL aggregation and filtering, and basic data interpretation.

## Interview description
"I created this self-driven Sales Data Analysis practice project to improve my data analysis skills. I used a sample dataset, checked missing and duplicate records, and practised summarising sales by product, region and month using Excel, Python and SQL."

**Note:** Describe tools as hands-on project experience only after you have personally run and understood the relevant scripts and queries.
