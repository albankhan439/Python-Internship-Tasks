import pandas as pd
from fpdf import FPDF

# Step 1: Load the data
df = pd.read_csv('sales_data.csv')
df['Total'] = df['Quantity'] * df['Price']

# Step 2: Create summary
total_sales = df['Total'].sum()
total_items = df['Quantity'].sum()

# Step 3: Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')
pdf.ln(10)

# Add summary
pdf.cell(200, 10, txt=f"Total Items Sold: {total_items}", ln=True)
pdf.cell(200, 10, txt=f"Total Sales: Rs. {total_sales}", ln=True)


# Add table headers
pdf.ln(10)
pdf.cell(40, 10, "Date", 1)
pdf.cell(50, 10, "Product", 1)
pdf.cell(30, 10, "Quantity", 1)
pdf.cell(30, 10, "Price", 1)
pdf.cell(40, 10, "Total", 1)
pdf.ln()

# Add table rows
for i, row in df.iterrows():
    pdf.cell(40, 10, row['Date'], 1)
    pdf.cell(50, 10, row['Product'], 1)
    pdf.cell(30, 10, str(row['Quantity']), 1)
    pdf.cell(30, 10, str(row['Price']), 1)
    pdf.cell(40, 10, str(row['Total']), 1)
    pdf.ln()

pdf.output("sales_report.pdf")
