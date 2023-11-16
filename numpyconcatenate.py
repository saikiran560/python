import numpy as np

# Creating two 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenating along axis 0 (vertical)
concatenated_arr = np.concatenate((arr1, arr2))
# or concatenated_arr = np.hstack((arr1, arr2))

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

print("\nConcatenated Array:")
print(concatenated_arr)
