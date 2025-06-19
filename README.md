# Task 2 – Automated Report Generation 🧾

This task is part of the Python Developer Internship by ELiteTEch.

## 📝 Objective

Develop a Python script that:
- Reads data from a CSV file
- Analyzes the data (e.g., total sales, quantity sold)
- Generates a formatted PDF report using the `fpdf` library

## 📁 Files Included

- `sales_data.csv`: Sample sales data containing product, quantity, and price
- `task2_report_generator.py`: Python script that analyzes the data and generates a PDF
- `sales_report.pdf`: Final report generated from the script

## 🛠 Technologies Used

- Python 3
- pandas
- fpdf

## 🔍 How It Works

1. The script reads data from `sales_data.csv`
2. It calculates:
   - Total items sold
   - Total sales (Quantity × Price)
3. It creates a structured PDF report with tabular data and summary
4. Output is saved as `sales_report.pdf`

## ▶️ How to Run

1. Install dependencies:

```bash
pip install pandas fpdf
