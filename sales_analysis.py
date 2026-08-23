import pandas as pd
import json
import openpyxl
import os

# Load the sales data from a CSV file and display its shape
df = pd.read_csv('data/sales.csv')
print('Data:')
print(df)
print(f'\nShape: {df.shape[0]} rows, {df.shape[1]} columns')


# Calculate the total sales for each product and display the results
df['total'] = df['quantity'] * df['price']
print('\nTotal Sales for Each Product:')
print(df)

# Creating output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Saving with different formats
# Save the DataFrame to a CSV file
df.to_csv('output/sales_results.csv', index=False)
# Save the DataFrame to a JSON file
df.to_json('output/sales_results.json', orient='records', lines=True, indent=4)
# Save the DataFrame to an Excel file
df.to_excel('output/sales_results.xlsx', index=False)

if os.path.exists('output/sales_results.csv'):
    print('\nResults saved to output/sales_results.csv')
if os.path.exists('output/sales_results.json'):
    print('Results saved to output/sales_results.json')
if os.path.exists('output/sales_results.xlsx'):
    print('Results saved to output/sales_results.xlsx')
    

    
