import tensorflow as tf

scalar = tf.constant(5)
print(scalar)


vector = tf.constant([1.0, 2.0, 3.0])
print(vector)

# Matrix (2D)
matrix = tf.constant([[1, 2], [3, 4]])
print(matrix)

# Tensor (3D)
tensor3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tensor3d)
print("Shape:", matrix.shape)      # (2, 2)
print("Rank:", tf.rank(matrix))    # 2
print("Data Type:", matrix.dtype)  # int32
