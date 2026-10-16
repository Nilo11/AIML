import pandas as pd

# 1. Create the initial DataFrame
data = {
    'Name': ['Nilofar', 'Priya', 'Rahul', 'Sneha', 'Vikram'],
    'Age':[25,25,22,26,23],
    'City': ['Mumbai', 'Delhi', 'Pune', 'Bangalore', 'Chennai'],
    'Marks':[96,95,90,88,87]
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print("\n")

# 2. Delete the 'City' column
 
df.drop('City', axis=1, inplace=True)

print("--- DataFrame After Deleting 'City' ---")
print(df)
