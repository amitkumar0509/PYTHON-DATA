                                                                                                                                                                                                                                                                                                                                                                                                                                                    # import library
import numpy as np

# Create a 2D numpy array
arr2D = np.array([[11, 11, 12, 11],
					[13, 11, 12, 11],
					[16, 11, 12, 11],
					[11, 11, 12, 11]])

print('Original Array :' ,
	arr2D, sep = '\n')

uniqueRows = np.unique(arr2D)
						

# print the output result
print('Unique Rows:',
	uniqueRows, sep = '\n')






# import library
import numpy as np
 
# Create a 2D numpy array
arr2D = np.array([[11, 11, 12, 11],
                     [13, 11, 12, 11],
                     [16, 11, 12, 11],
                     [11, 11, 12, 11]])
 
uniqueRows = np.unique(arr2D, axis=1) #0 or 1 axis
                        
 
# print the output result
print('Unique Rows:',
      uniqueRows, sep = '\n')




# import library
import numpy as np

# Create a 2D numpy array
arr2D = np.array([[11, 11, 12, 11],
					[13, 11, 12, 11],
					[16, 11, 12, 11],
					[11, 11, 12, 11]])

uniqueRows = np.unique(arr2D, return_index=True)
						

# print the output result
print('Unique Rows:',
	uniqueRows, sep = '\n')


# Unique Rows:
# (array([11, 12, 13, 16]), array([0, 2, 4, 8]))

