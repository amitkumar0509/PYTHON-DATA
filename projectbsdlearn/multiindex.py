import pandas as pd
import numpy as np

# Example: Creating a MultiIndex from lists of arrays
arrays = [
    ['A', 'A', 'B', 'B', 'C', 'C'],
    [1, 2, 1, 2, 1, 2]
]

index = pd.MultiIndex.from_arrays(arrays, names=('Letter', 'Number'))
df = pd.DataFrame(np.random.randn(6, 4), index=index)
print(df)
# In this example, we create a with two levels: 'Letter' and 'Number'.
# The pd.MultiIndex.from_arrays function takes a list of arrays and assigns names to each level using the names parameter. The resulting DataFrame df has a hierarchical row index.
# Example: Creating a MultiIndex from a list of tuples
tuples = [
    ('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1), ('C', 2)
]

index = pd.MultiIndex.from_tuples(tuples, names=('Letter', 'Number'))
df = pd.DataFrame(np.random.randn(6, 4), index=index)
print(df)
# Example: Basic indexing with loc
arrays = [
    ['A', 'A', 'B', 'B', 'C', 'C'],
    [1, 2, 1, 2, 1, 2]
]

index = pd.MultiIndex.from_arrays(arrays, names=('Letter', 'Number'))
df = pd.DataFrame(np.random.randn(6, 4), index=index)

# Accessing a specific row
print(df.loc[('A', 1)])

# Accessing all rows with Letter 'A'
print(df.loc['A'])

# When using loc, you can pass a tuple to specify the index values for each level.
# If you only specify the index value for the first level, it will return all rows with that value in the first level.