import pandas as pd

# Define data with clear variable names
people_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

# Create a DataFrame with the data
df = pd.DataFrame(people_data)

# Print the DataFrame
print(df)