import pandas as pd

marks_series = pd.Series([85, 92, 78, 90, 88], name="Student Marks")

# Display the Series
print("--- Pandas Series ---")
print(marks_series)

# Display its index
print("\n--- Series Index ---")
print(marks_series.index)
