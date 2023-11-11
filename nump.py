import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3])
print("1D Array:")
print(arr_1d)

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr_2d)

# Creating an array with zeros
zeros_array = np.zeros((3, 4))
print("\nArray with Zeros:")
print(zeros_array)

# Creating an array with ones
ones_array = np.ones((2, 3))
print("\nArray with Ones:")
print(ones_array)

# Creating an identity matrix
identity_matrix = np.eye(3)
print("\nIdentity Matrix:")
print(identity_matrix)





# Element-wise addition
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
addition_result = arr1 + arr2
print("Element-wise Addition:")
print(addition_result)

# Element-wise multiplication
multiplication_result = arr1 * arr2
print("\nElement-wise Multiplication:")
print(multiplication_result)

# Matrix multiplication
matrix_multiply_result = np.dot(arr1, arr2)
print("\nMatrix Multiplication:")
print(matrix_multiply_result)




# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slicing rows and columns
sliced_rows = arr_2d[1:, :]
sliced_cols = arr_2d[:, 1:3]

print("Original 2D Array:")
print(arr_2d)
print("\nSliced Rows:")
print(sliced_rows)
print("\nSliced Columns:")
print(sliced_cols)
