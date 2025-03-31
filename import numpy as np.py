import numpy as np

# Create a 2D array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Display the array
print("Original Array:")
print(array)

# Accessing elements
print("\nElement at (0, 1):", array[0, 1])  # Access element at row 0, column 1

# Slicing the array
print("\nSliced Array (first two rows and columns):")
print(array[:2, :2])

# Adding a scalar to the array
print("\nArray after adding 10:")
print(array + 10)

# Transposing the array
print("\nTransposed Array:")
print(array.T)

# Sum of all elements
print("\nSum of all elements:", np.sum(array))

# Row-wise sum
print("\nRow-wise sum:", np.sum(array, axis=1))

# Column-wise sum
print("\nColumn-wise sum:", np.sum(array, axis=0))

# Element-wise multiplication
print("\nElement-wise multiplication:")
print(array * array)