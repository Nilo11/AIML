import pandas as pd

# Creating the DataFrame with employee details
data = {
    'Name': ['Amit Sharma', 'Priya Verma', 'Rahul Gupta', 'Neha Singh', 'Vikram Joshi', 
             'Ananya Nair', 'Karan Patel', 'Sneha Deshmukh', 'Rohit Kumar', 'Divya Iyer'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'Finance', 'HR', 'IT', 'Marketing', 'Marketing', 'Finance'],
    'Salary': [65000, 48000, 72000, 55000, 49000, 60000, 85000, 45000, 53000, 90000],
    'Experience': [4, 2, 5, 3, 2, 4, 6, 1, 3, 7],
    'City': ['Pune', 'Mumbai', 'Pune', 'Bangalore', 'Mumbai', 'Bangalore', 'Pune', 'Mumbai', 'Bangalore', 'Pune']
}
df = pd.DataFrame(data)

# a) Display employees with salary > ₹50,000
salary_gt_50k = df[df['Salary'] > 50000]
print("--- a) Employees with Salary > ₹50,000 ---")
print(salary_gt_50k[['Name', 'Salary']])

# b) Find the average salary
avg_salary = df['Salary'].mean()
print(f"\nb) Average Salary: ₹{avg_salary:,.2f}")

# c) Find the highest salary
highest_salary = df['Salary'].max()
print(f"c) Highest Salary: ₹{highest_salary:,.2f}")

# d) Find employees with more than 3 years of experience
exp_gt_3 = df[df['Experience'] > 3]
print("\n--- d) Employees with > 3 Years Experience ---")
print(exp_gt_3[['Name', 'Experience']])

# e) Count employees city-wise
city_counts = df['City'].value_counts()
print("\n--- e) City-wise Employee Count ---")
print(city_counts)

# f) Calculate average salary department-wise
dept_avg_salary = df.groupby('Department')['Salary'].mean()
print("\n--- f) Department-wise Average Salary ---")
print(dept_avg_salary)

# g) Sort employees by salary (descending order)
df_sorted = df.sort_values(by='Salary', ascending=False)
print("\n--- g) Employees Sorted by Salary ---")
print(df_sorted[['Name', 'Department', 'Salary']])

# h) Save the final DataFrame as a CSV file
df_sorted.to_csv('department_analysis.csv', index=False)
print("\nh) Final DataFrame successfully saved to 'department_analysis.csv'!")
