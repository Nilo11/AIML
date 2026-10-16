import pandas as pd

# a) Read the CSV file
df = pd.read_csv('sales.csv')

# b) Display all products
print("--- All Products ---")
print(df)

# c & d) Create a new column Total_Sales (Price * Quantity)
df['Total_Sales'] = df['Price'] * df['Quantity']

# e) Find the product with the highest total sales
highest_sales_row = df.loc[df['Total_Sales'].idxmax()]
print(f"\ne) Product with Highest Total Sales: {highest_sales_row['Product']} (${highest_sales_row['Total_Sales']:.2f})")

# f) Find the total sales of all products
total_store_sales = df['Total_Sales'].sum()
print(f"\nf) Total Sales of All Products: ${total_store_sales:.2f}")

# g) Find the average product price
avg_price = df['Price'].mean()
print(f"\ng) Average Product Price: ${avg_price:.2f}")

# h) Display products where quantity is greater than 10
filtered_qty = df[df['Quantity'] > 10]
print("\nh) Products with Quantity > 10:")
print(filtered_qty[['Product', 'Quantity']])

# i) Find total sales category-wise using groupby()
category_sales = df.groupby('Category')['Total_Sales'].sum()
print("\ni) Total Sales Category-wise:")
print(category_sales)

# j) Sort products according to Total_Sales in descending order
df_sorted = df.sort_values(by='Total_Sales', ascending=False)
print("\nj) Products Sorted by Total Sales (Descending):")
print(df_sorted[['Product', 'Total_Sales']])

# k) Save the updated DataFrame into sales_analysis.csv
df_sorted.to_csv('sales_analysis.csv', index=False)
print("\nk) Updated DataFrame successfully saved to 'sales_analysis.csv'!")
