import pandas as pd
# load dataset & rename it to 'df': data frame
#df = '/content/healthcare_dataset.csv'
df = r'C:\Users\SDE77\Desktop\Healthcare_Data\Q1\healthcare_dataset.csv'
df = pd.read_csv(df)
# inspecting number of rows & columns
df.shape
# Pivot the data
pivot_data = df.pivot_table(index='Blood Group Type', columns=['Medical Condition'], aggfunc='size', fill_value=0)
# Grouping by 'Medical Condition' and calculating the average billing amount
average_billing_amount = df.groupby('Medical Condition')['Billing Amount'].mean()

print(average_billing_amount)
