from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np

# user_X, user_y = int(input("Enter Height: ")), int(input("Enter Weight: "))
data = pd.read_csv('./bmi.csv')

X, y = np.array(data.height), np.array(data.weight)

standardizer = StandardScaler()
features_standardized = standardizer.fit_transform(X)
nearest_neighbours = NearestNeighbors(n_neighbors=2).fit(features_standardized)
# new_observation = [1, 1, 1 , 1]
distance,indices = nearest_neighbours.kneighbors([167])
print(features_standardized[indices])

print(X)
