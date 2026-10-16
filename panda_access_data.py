import pandas as pd

# Create the student DataFrame
data = {
    'Name': ['Nilofar', 'Priya', 'Rahul', 'Sneha', 'Vikram'],
    'Age':[25,24,22,21,22],
    'Marks': [85, 92, 78, 88, 95]
}
df = pd.DataFrame(data)

# 1. Display only the Name column
print("--- Name Column Only ---")
print(df['Name'])
print("\n")

# 2. Display the first 3 rows
print("--- First 3 Rows ---")
print(df.head(3))
print("\n")

# 3. Display the last 2 rows
print("--- Last 2 Rows ---")
print(df.tail(2))
