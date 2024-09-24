import fpdf
import pandas as pd
import glob
from pathlib import Path
from invoicefxns import create_time, home_dir, FOLDER_NAME

from openpyxl.styles.builtins import styles

filepaths = glob.glob("text/*.xlsx")
print(filepaths)
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    filename = Path(filepath).stem

    pdf = fpdf.FPDF(orientation="P", unit='mm', format= 'A4')
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style='B')
    pdf.cell(w=50, h=8, txt= f"Invoice No:{filename.split('-')[0]}"
             , border=1, ln=1, align='L')
    pdf.cell(w=50, h=8, txt=f"{create_time()}", border=1, ln=1)

    pdf.output(f"{FOLDER_NAME}/{filename}.pdf")

