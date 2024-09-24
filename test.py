#This was to test how to access the field names of any csv file
import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_excel('10003-2023.1.18.xlsx'
                   , sheet_name='Sheet 1')
field_names = list(df.columns)

print(field_names)
