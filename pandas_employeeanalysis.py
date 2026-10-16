
import pandas as pd

# 1. Automatically create the employees.csv file with complete data
# Storing the numbers explicitly as text strings so they never get hidden or skipped!
emp_ids = "101,102,103,104,105,106,107,108,109,110"
salaries = "45000,32000,55000,38000,60000,28000,48000,52000,35000,42000"
experience_years = "5,2,7,3,8,1,4,6,2,4"

data = {
    'EmpID': [int(x) for x in emp_ids.split(',')],
    'Name': ['Nilofar Momin', 'Priya Sharma', 'Rajesh Patel', 'Sunita Rao', 'Vikram Singh',
             'Karan Johar', 'Neha Gupta', 'Rahul Verma', 'Sneha Reddy', 'Anil Kapoor'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [int(x) for x in salaries.split(',')],
    'Experience': [int(x) for x in experience_years.split(',')]
}

# Save initial dataset to CSV
df_initial = pd.DataFrame(data)
df_initial.to_csv('employees.csv', index=False)

# =====================================================================
# 2. Pandas Operations
# =====================================================================

# a) Read the CSV file
df = pd.read_csv('employees.csv')

# b) Display all employees
print("--- b) All Employees ---")
print(df)

# c) Display employees whose salary is greater than ₹40,000
print("\n--- c) Employees with Salary > ₹40,000 ---")
print(df[df['Salary'] > 40000])

# d) Find the highest salary
highest_sal = df['Salary'].max()
print(f"\n--- d) Highest Salary: ₹{highest_sal} ---")

# e) Find the lowest salary
lowest_sal = df['Salary'].min()
print(f"\n--- e) Lowest Salary: ₹{lowest_sal} ---")

# f) Calculate the average salary
avg_sal = df['Salary'].mean()
print(f"\n--- f) Average Salary: ₹{avg_sal:.2f} ---")

# g) Find the average salary of each department using groupby()
print("\n--- g) Average Salary by Department ---")
print(df.groupby('Department')['Salary'].mean())

# h) Display employees having more than 3 years of experience
print("\n--- h) Employees with Experience > 3 Years ---")
print(df[df['Experience'] > 3])

# i) Sort employees by salary in descending order
df_sorted = df.sort_values(by='Salary', ascending=False)
print("\n--- i) Employees Sorted by Salary (Descending) ---")
print(df_sorted)

# j) Save the result into employee_analysis.csv
df_sorted.to_csv('employee_analysis.csv', index=False)
print("\n--- j) Results successfully saved to 'employee_analysis.csv'! ---")
