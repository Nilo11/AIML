import pandas as pd

# 1. Create a DataFrame with missing values (None / NaN)
data = {
    'Name': ['Nilofar', 'Priya', 'Rahul', 'Sneha', 'Vikram'],
    'Age': [20, None, 19, 20, None],          # Priya and Vikram have missing Ages
    'Marks': [85, 92, None, 88, None]          # Rahul and Vikram have missing Marks
}
df = pd.DataFrame(data)

print("--- Original DataFrame with Missing Values ---")
print(df)
print("\n")

# 2. Find missing values (Returns True where data is missing)
print("--- Missing Values Map (True indicates missing) ---")
print(df.isnull())
print("\n")

# Count how many missing values are in each column
print("--- Count of Missing Values per Column ---")
print(df.isnull().sum())
print("\n")

# 3. Replace missing values in the Marks column with 0
# FIX: Using explicit assignment instead of inplace=True to prevent warnings
df['Marks'] = df['Marks'].fillna(0)

print("--- DataFrame After Replacing Missing Marks with 0 ---")
print(df)

 
