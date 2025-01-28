import numpy as np 
iterable = (a*a for a in range(8))
arr = np.fromiter(iterable,int)
print(arr)