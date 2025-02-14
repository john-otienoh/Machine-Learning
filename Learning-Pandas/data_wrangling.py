import pandas as pd

data = pd.read_csv('./passenger_data.csv')

# Show DataFrame
print(data.head())

# Show dimensions
print(data.shape)

# Show statistics
print(data.describe())

# Show info
print(data.info())

# Show counts
print(data.count())
