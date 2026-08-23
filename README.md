# Sales Data Analysis

A small Python project that loads sales data from a CSV file, calculates total sales per product using pandas, and exports the results into multiple file formats (CSV, JSON, Excel).

## What it does

1. Loads sales data from `data/sales.csv` into a pandas DataFrame
2. Displays the raw data and its shape (rows/columns)
3. Calculates a `total` column for each product (`quantity * price`)
4. Exports the results into three formats inside the `output/` folder:
   - `sales_results.csv`
   - `sales_results.json`
   - `sales_results.xlsx`
5. Confirms in the console which files were successfully saved

## Tech used

- `pandas` — loading, processing, and exporting the data
- `openpyxl` — required by pandas to write `.xlsx` files
- `os` — creating the output directory and checking saved files

## How to run

```bash
pip install pandas openpyxl
python sales_analysis.py
```

Make sure `data/sales.csv` exists with at least `quantity` and `price` columns before running.

## Output

- `output/sales_results.csv` — sales data with the added `total` column
- `output/sales_results.json` — same data in JSON format
- `output/sales_results.xlsx` — same data in Excel format
- Console output showing the data, its shape, and save confirmations

## What I learned

- Loading and inspecting tabular data with pandas (`shape`, column access)
- Creating derived columns from existing data
- Exporting the same DataFrame into multiple file formats (CSV, JSON, Excel)
- Creating directories programmatically and checking whether files were saved successfully
