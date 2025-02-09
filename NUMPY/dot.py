import numpy as np
arr = np.eye(3)
arr1 =np.ones((3,3))*6
result= arr.dot(arr1).dot(arr1)
print(result)
print(arr)