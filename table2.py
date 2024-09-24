
from prettytable import PrettyTable

# Create a PrettyTable
table = PrettyTable()

# Add column names
table.field_names = ['Name', 'Age', 'City']

# Add data to the table
table.add_row(['John', 25, 'New York'])
table.add_row(['Jane', 30, 'London'])
table.add_row(['Bob', 35, 'Paris'])
table.add_row(['Alice', 40, 'Tokyo'])

# Print the table
print(table)
