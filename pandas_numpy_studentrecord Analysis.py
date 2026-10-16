import pandas as pd
import numpy as np

# 1. Creating the students.csv file with complete data
data = {
    'RollNo': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Nilofar Momin', 'Diya Patel', 'Ishaan Verma', 'Ananya Iyer', 'Kabir Rao',
             'Meera Joshi', 'Rohan Das', 'Sanya Gupta', 'Arjun Nair', 'Neha Kapoor'],
    'Python': [85, 38, 72, 45, 90, 30, 78, 95, 88, 76],
    'Java': [78, 42, 65, 38, 85, 35, 82, 91, 79, 70],
    'DBMS': [80, 35, 70, 42, 88, 40, 84, 90, 85, 75]
}
df_initial = pd.DataFrame(data)
df_initial.to_csv('students.csv', index=False)

# =====================================================================
# 2. Pandas Operations
# =====================================================================
df = pd.read_csv('students.csv')

# a) Display complete dataset
print("--- a) Complete Dataset ---")
print(df)

# b) Display first 5 records
print("\n--- b) First 5 Records ---")
print(df.head(5))

# c) Calculate Total Marks
df['Total'] = df['Python'] + df['Java'] + df['DBMS']

# d) Calculate Percentage
df['Percentage'] = (df['Total'] / 300) * 100

# e) Add a Result column
df['Result'] = np.where(df['Percentage'] >= 40, 'Pass', 'Fail')

# f) Highest percentage student
highest_student = df.loc[df['Percentage'].idxmax()]
print(f"\n--- f) Highest Scorer ---\n{highest_student['Name']} ({highest_student['Percentage']:.2f}%)")

# g) Average percentage
avg_percentage = df['Percentage'].mean()
print(f"\n--- g) Average Percentage ---\n{avg_percentage:.2f}%")

# h) Students > 75%
print("\n--- h) Students scoring > 75% ---")
print(df[df['Percentage'] > 75][['RollNo', 'Name', 'Percentage']])

# i) Sort according to percentage in descending order
df_sorted = df.sort_values(by='Percentage', ascending=False)
print("\n--- i) Sorted Dataset (Descending) ---")
print(df_sorted)

# j) Save to student_result.csv
df_sorted.to_csv('student_result.csv', index=False)
print("\n--- j) File 'student_result.csv' successfully saved! ---")
