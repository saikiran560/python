import numpy as np

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Summing along axis 0 (columns)
sum_along_columns = np.sum(arr_2d, axis=0)

# Summing along axis 1 (rows)
sum_along_rows = np.sum(arr_2d, axis=0)

print("Original 2D Array:")
print(arr_2d)

print("\nSum Along Columns:")
print(sum_along_columns)

print("\nSum Along Rows:")
print(sum_along_rows)
