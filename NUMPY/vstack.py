# Python program explaining 
# vstack() function 

import numpy as np

# input array 
in_arr1 =np.array([[ 1, 2, 3], [ -1, -2, -3]] ) 
print ("1st Input array : \n", in_arr1) 

in_arr2 = np.array([[ 4, 5, 6], [ -4, -5, -6]] ) 
print ("2nd Input array : \n", in_arr2) 

# Stacking the two arrays vertically 
out_arr =np.vstack((in_arr1, in_arr2)) 
print ("Output stacked array :\n ", out_arr) 
