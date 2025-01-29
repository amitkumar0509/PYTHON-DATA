import numpy as np
arr = np.arange(10,dtype=np.int64)
print(arr)  # prints [0 1 2 3 4 5 6
v = arr.view(dtype=np.int64 )
print(v)  # prints [0 1 2 3 4 5 6
v+=2
print("after view :\n",arr)