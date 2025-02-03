import numpy as np
arr = np.array([1,3,4,5,6])
arr2 = np.array_split(arr,3)
print(arr2)

import numpy as np

# Creating a 2D array
array = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])

# Splitting the array into 3 equal parts along the second axis (axis=1)
result = np.split(array, 3, axis=1)

print("2D Array:")
print(array)
print("\nResult after numpy.split() along axis=1:")
print(result)
