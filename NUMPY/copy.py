import numpy as np
x = np.array([[0, 1, ], [2, 3]]) 
print("x is:\n", x) 

# copying x to y 
y = x.copy() 

# filling x with 1
x.fill(1) 
print("\n Now x is : \n", x) 

print("\n y is: \n", y)
