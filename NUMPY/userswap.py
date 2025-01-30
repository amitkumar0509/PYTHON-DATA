# Importing Module
import numpy as np


# Creating array
my_array = np.arange(12).reshape(4, 3)
print("Original Array : ")
print(my_array)
# creating function for swap

def Swap(arr, start_index, last_index):
	arr[:, [start_index, last_index]] = arr[:, [last_index, start_index]]

# user input
# passing parameter into the function

start_index = int(input("Enter the first column to swap: "))
last_index = int(input("Enter the last column to swap: "))
Swap(my_array, start_index,last_index)
print(" After Swapping :")
print(my_array)
