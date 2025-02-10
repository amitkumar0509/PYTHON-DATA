# Define two 3x3 matrices
matrix1 = [[12, 7, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[5, 8, 1],
           [6, 7, 3],
           [4, 5, 9]]

# Initialize result matrix with zeros
res = [[0 for x in range(3)] for y in range(3)] 

# Perform matrix multiplication
for i in range(len(matrix1)):           # Loop over rows of matrix1
    for j in range(len(matrix2[0])):     # Loop over columns of matrix2
        for k in range(len(matrix2)):    # Loop over rows of matrix2
            res[i][j] += matrix1[i][k] * matrix2[k][j]  # Multiplication & summation

# Print the resulting matrix
print(res)
