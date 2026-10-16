import pandas as pd

 
data = {
    'Name': ['Nilofar', 'Priya', 'Rahul', 'Sneha', 'Vikram', 'Jaya'],   
    'Marks': [85,     92,      65,      88,      55,       78]      
}

# This will now run without errors
df = pd.DataFrame(data)

# Filter rows where Marks are greater than 70
filtered_df = df[df['Marks'] > 70]

print("--- Students with Marks > 70 ---")
print(filtered_df)
