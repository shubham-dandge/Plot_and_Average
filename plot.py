import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# load dataset & rename it to 'df': data frame
#df = '/content/healthcare_dataset.csv'
df = r'C:\Users\SDE77\Desktop\Healthcare_Data\Q1\healthcare_dataset.csv'

df = pd.read_csv(df)
# inspecting number of rows & columns
df.shape
# inspect data types
df.info()
# Pivot the data
pivot_data = df.pivot_table(index='Blood Group Type', columns=['Gender', 'Medical Condition'], aggfunc='size', fill_value=0)

# Plotting
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_data, annot=True, cmap='coolwarm', fmt='d')
plt.title('Blood Group Type vs Gender vs Medical Condition')
plt.xlabel('Gender, Medical Condition')
plt.ylabel('Blood Group Type')
plt.show()