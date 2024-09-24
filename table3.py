# Create a PDF instance
from fpdf import FPDF
import pandas as pd
#import glob

pdf = FPDF(orientation='P', unit='mm', format= 'A4')
pdf.add_page()

# Sample data for the table
header = ['product_id', 'product_name'
    , 'amount_purchase','price_oer_unit', 'total_price']
#filepaths = glob.glob('text/*.xlsx')

df = pd.read_excel('invoice//text/10003-2003.1.18.xlsx', sheet_name='Sheet 1')

print(df)

# Add a title and table
#pdf.chapter_title("Table Example")
#pdf.create_table([header] + data)

# Save the PDF to a file
#pdf_file = "example_table_fpdf.pdf"
#pdf.output(pdf_file)

#print(f"PDF created with table: {pdf_file}")