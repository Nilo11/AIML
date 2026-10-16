import pandas as pd
import numpy as np

# Creating placement.csv with student records (selected and not selected)
data = {
    'Name': ['Nilofar Momin', 'Sneha Patil', 'Amit Verma', 'Pooja Nair', 'Karan Joshi', 
             'Neha Kulkarni', 'Rohit Deshmukh', 'Ananya Iyer', 'Vikram Shinde', 'Priya Deshpande'],
    'Branch': ['Computer Science', 'Information Technology', 'Electronics', 'Computer Science', 'Mechanical',
               'Information Technology', 'Computer Science', 'Electronics', 'Mechanical', 'Computer Science'],
    'Company': ['TCS', 'Infosys', 'None', 'Wipro', 'None', 
                'Cognizant', 'Google', 'Accenture', 'None', 'Microsoft'],
    'Package': [4.5, 3.6, 0.0, 5.0, 0.0, 4.2, 18.0, 6.5, 0.0, 12.0],
    'Status': ['Selected', 'Selected', 'Not Selected', 'Selected', 'Not Selected', 
               'Selected', 'Selected', 'Selected', 'Not Selected', 'Selected']
}
df = pd.DataFrame(data)
df.to_csv('placement.csv', index=False)

# a) Read the CSV file
df = pd.read_csv('placement.csv')

# b) Display all student records
print("--- All Student Records ---")
print(df)

# c) Display only selected students
selected_df = df[df['Status'] == 'Selected']
print("\n--- Selected Students ---")
print(selected_df)

# d) Count the total number of selected students
total_selected = len(selected_df)
print(f"\nd) Total Selected Students: {total_selected}")

# e) Find the highest package
highest_pkg = df['Package'].max()
print(f"e) Highest Package: {highest_pkg} LPA")

# f) Find the lowest package among selected students
lowest_selected_pkg = selected_df['Package'].min()
print(f"f) Lowest Package Among Selected: {lowest_selected_pkg} LPA")

# g) Calculate the average package of selected students
avg_selected_pkg = selected_df['Package'].mean()
print(f"g) Average Package of Selected Students: {avg_selected_pkg:.2f} LPA")

# h) Display students having a package greater than 4 LPA
pkg_gt_4 = df[df['Package'] > 4.0]
print("\nh) Students with Package > 4 LPA:")
print(pkg_gt_4[['Name', 'Package', 'Status']])

# i) Sort selected students according to package in descending order
sorted_selected = selected_df.sort_values(by='Package', ascending=False)
print("\ni) Selected Students Sorted by Package (Descending):")
print(sorted_selected[['Name', 'Company', 'Package']])

# j) Find the number of students selected by each company using groupby()
company_counts = selected_df.groupby('Company')['Name'].count()
print("\nj) Students Selected by Each Company:")
print(company_counts)

# k) Save the selected-student data into selected_students.csv
sorted_selected.to_csv('selected_students.csv', index=False)
print("\nk) Selected student data saved to 'selected_students.csv' successfully!")
