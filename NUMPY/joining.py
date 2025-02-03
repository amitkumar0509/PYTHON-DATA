import numpy as np 
  
array_1 = np.array([[1, 2], [3, 4]]) 
array_2 = np.array([[5, 6], [7, 8]]) 
  
array_new = np.concatenate((array_1, array_2), axis=0) 
print(array_new) 



# stack
import numpy as np 

array_1 = np.array([1, 2, 3, 4]) 
array_2 = np.array([5, 6, 7, 8]) 

array_new = np.stack((array_1, array_2), axis=1) 
print(array_new) 

# block
import numpy as np 

block_1 = np.array([[1, 1], [1, 1]]) 
block_2 = np.array([[2, 2, 2], [2, 2, 2]]) 
block_3 = np.array([[3, 3], [3, 3], [3, 3]]) 
block_4 = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]]) 

block_new = np.block([ 
	[block_1, block_2], 
	[block_3, block_4] 
]) 

print(block_new) 
