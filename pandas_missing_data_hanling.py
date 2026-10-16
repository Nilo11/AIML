import pandas as pd
import numpy as np

# Creating the sample employee_data.csv with missing values
data = {
    'EmpID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Aarav Sharma', 'Priya Patel', 'Rohan Gupta', 'Ananya Iyer', 'Vikram Singh', 
             'Neha Verma', 'Karan Mehta', 'Divya Nair', 'Amit Kumar', 'Sneha Joshi'],
    'Age': [28, 34, np.nan, 41, 29, 35, np.nan, 38, 26, 32],
    'Department': ['IT', 'HR', 'Finance', np.nan, 'IT', 'Marketing', 'HR', np.nan, 'Finance', 'IT'],
    'Salary': [65000, 52000, 78000, 60000, np.nan, 55000, 62000, 71000, np.nan, 48000]
}
df = pd.DataFrame(data)
df.to_csv('employee_data.csv', index=False)

# a) Read the CSV file
df = pd.read_csv('employee_data.csv')

# b) Display the complete dataset
print("--- Complete Dataset (Original) ---")
print(df)

# c) Check whether the dataset contains missing values
has_missing = df.isnull().values.any()
print(f"\nc) Dataset contains missing values: {has_missing}")

# d) Count the number of missing values in each column
missing_counts = df.isnull().sum()
print("\nd) Missing values count per column:")
print(missing_counts)

# e) Replace missing Age values with the average age
avg_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(avg_age)

# f) Replace missing Salary values with 0
df['Salary'] = df['Salary'].fillna(0)

# g) Replace missing Department values with "Not Assigned"
df['Department'] = df['Department'].fillna("Not Assigned")

# h) Display the updated DataFrame
print("\nh) Updated DataFrame:")
print(df)

# i) Sort employees according to salary (sorted in descending order here)
df_sorted = df.sort_values(by='Salary', ascending=False)
print("\ni) Employees Sorted by Salary:")
print(df_sorted[['EmpID', 'Name', 'Salary']])

# j) Save the cleaned data into cleaned_employee_data.csv
df_sorted.to_csv('cleaned_employee_data.csv', index=False)
print("\nj) Cleaned data saved successfully to 'cleaned_employee_data.csv'!")
