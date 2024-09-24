from fpdf import FPDF
import pandas as pd

# Create a PDF instance
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

df = pd.read_excel('10003-2023.1.18.xlsx'
                   , sheet_name='Sheet 1')
# Sample data for the table
header = list(df.columns)

# Read the Excel file into a DataFrame
# Ensure the correct path and sheet name are used

# Add the header
pdf.set_font('Arial', 'B', 12)
for col_title in header:
    pdf.cell(40, 10, col_title, 1)  # Cell width = 40 mm, height = 10 mm
pdf.ln()  # Line break

# Add data rows
pdf.set_font('Arial', '', 12)  # Use regular font for data rows
for index, row in df.iterrows():
    pdf.cell(40, 10, str(row['product_id']), 1)
    pdf.cell(40, 10, str(row['product_name']), 1)
    pdf.cell(40, 10, str(row['amount_purchased']), 1)
    pdf.cell(40, 10, str(row['price_per_unit']), 1)
    pdf.cell(40, 10, str(row['total_price']), 1)
    pdf.ln()  # Line break for each row

# Save the PDF to a file
filename = "report.pdf"
pdf.output(f'invoice_pdf/{filename}')

print(f"PDF created: {filename}")