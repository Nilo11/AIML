import pandas as pd

# Create the initial student DataFrame
data = {
    'Name': ['Nilofar', 'Priya', 'Rahul', 'Sneha', 'Vikram'],
    'Age':[25,26,24,23,21],
    'Marks': [85, 92, 78, 88, 95]
}
df = pd.DataFrame(data)

# 1. Sort by Marks in ascending order (lowest to highest)
df_ascending = df.sort_values(by='Marks')

print("--- Sorted by Marks (Ascending) ---")
print(df_ascending)
print("\n")

# 2. Sort by Marks in descending order (highest to lowest)
df_descending = df.sort_values(by='Marks', ascending=False)

print("--- Sorted by Marks (Descending) ---")
print(df_descending)
