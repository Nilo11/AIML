import pandas as pd

# 1. Create a dictionary 
data = {
    'Name': ['Nilofar', 'Priya', 'Rahul', 'Sneha', 'Vikram'],
    'Age': [25,23,22,24,21],
    'Marks': [85, 92, 78, 88, 95]
}

# 2. Create the DataFrame
df = pd.DataFrame(data)

# 3. Display the DataFrame
print(df)
