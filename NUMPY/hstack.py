import numpy as np
in_arr =  np.array([[1,2,3],[4,5,6]])
print("1st input array:\n",in_arr)

in_arr2 =np.array([[4,5,6],[-4,-5,-6]])
print("\n2nd input array:\n",in_arr2)

Output_arr = np.hstack((in_arr,in_arr2))
print("\nOutput array:\n",Output_arr)