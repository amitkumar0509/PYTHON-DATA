import numpy as np 
my_arr =np.arange(25).reshape(5,5)
print(my_arr)
#swapping
my_arr[:,[3,0]]=my_arr[:,[0,3]]
print("After swapping the column :")
print(my_arr)