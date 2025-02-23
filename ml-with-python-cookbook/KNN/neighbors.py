from sklearn import datasets
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
features = iris.data
standardizer = StandardScaler()
features_standardized = standardizer.fit_transform(features)
nearest_neighbours = NearestNeighbors(n_neighbors=2).fit(features_standardized)
new_observation = [1, 1, 1 , 1]
distance,indices = nearest_neighbours.kneighbors([new_observation])
print(features_standardized[indices])

# Set the Metric Parameter.
nn_euclidean = NearestNeighbors(n_neighbors=3, metric='euclidean').fit(features_standardized)
distance, indices = nn_euclidean.kneighbors([new_observation])
print(features_standardized[indices])

# Find each observation's nearest neighbours
nn_with_self = nn_euclidean.kneighbors_graph(features_standardized).toarray()
for i, x in enumerate(nn_with_self):
    x[i] = 0
print(nn_with_self[0])

