import pandas as pd

# 1. Create the initial DataFrame
data = {
    'Name': ['Nilofar', 'Sanju', 'Rahul', 'Sneha', 'Vikram'],
    'Maths':[91, 80, 82, 94, 91],
    'Science': [90, 89, 82, 94, 91]
}
df = pd.DataFrame(data)

df['Total'] = df['Maths'] + df['Science']

print(df)
