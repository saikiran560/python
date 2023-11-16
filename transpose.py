import numpy as np

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Transposing the array
arr_transposed = np.transpose(arr_2d)
# or arr_transposed = arr_2d.T

print("Original 2D Array:")
print(arr_2d)

print("\nTransposed Array:")
print(arr_transposed)
