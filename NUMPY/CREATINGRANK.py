import numpy as np
#creating rank1 array
arr =np.array([1,2,3,4])
print(f"Array of Rank 1 is \n{arr}")
#creating rank2 array
arr= np.array([[1,2,3,4],
              [4,5,6,7]])
print(f"Array of Rank 2 is \n{arr}")
#creating array with tuple instead of using list
arr=np.array((1,2,3,4,5))
print("Array by using tuple\n",arr)