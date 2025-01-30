# Appending a single value to a 1darray
import numpy as np

# creating an array
arr = np.array([1, 8, 3, 3, 5])
print('Original Array : ', arr)

# appending to the array
arr = np.append(arr, [7])
print('Array after appending : ', arr)

# Appending another array at the end of 1darray

# importing the module
import numpy as np
 
# creating an array
arr1 = np.array([1, 2, 3])
print('First array is : ', arr1)
 
# creating another array
arr2 = np.array([4, 5, 6])
print('Second array is : ', arr2)
 
# appending arr2 to arr1
arr = np.append(arr1, arr2)
print('Array after appending : ', arr)


# Appending Values at the End Using Concatenation


# importing the module
import numpy as np
 
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
 
combined = np.concatenate((arr1, arr2), axis=0)
print(combined)

# Appending with a Different Array Type

# importing the module
import numpy as np

arr = np.array([1, 2, 3])
arr_float = np.array([4.0, 5.0])

combined = np.append(arr, arr_float)
print(combined) # Output: [1. 2. 3. 4. 5.]

# Appending Using List Comprehension and numpy.concatenate

# importing the module
import numpy as np
 
arr = np.array([1, 2, 3, 4, 5])
values_to_append = [np.array([6, 7]), np.array([8, 9])]
combined = np.concatenate([arr] + values_to_append)
print(combined)


# Appending Values at the End of the N-Dimensional Array

# importing the module
import numpy as np

# create an array
arr = np.arange(1, 13).reshape(2, 6)
print('Original Array')
print(arr, '\n')

# create another array which is
# to be appended column-wise
col = np.arange(5, 11).reshape(1, 6)
print('Array to be appended column wise')
print(col)
arr_col = np.append(arr, col, axis=0)
print('Array after appending the values column wise')
print(arr_col, '\n')

# create an array which is
# to be appended row wise
row = np.array([1, 2]).reshape(2, 1)
print('Array to be appended row wise')
print(row)
arr_row = np.append(arr, row, axis=1)
print('Array after appending the values row wise')
print(arr_row)



