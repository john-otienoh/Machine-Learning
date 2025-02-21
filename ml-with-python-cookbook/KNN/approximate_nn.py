from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn import datasets
import numpy as np
import annoy
import faiss

iris = datasets.load_iris()
features, target = iris.data, iris.target
standardizer = StandardScaler()
features_standardized = standardizer.fit_transform(features)

n_features, n_list, k = features_standardizer.shape[1], 3, 2

# Create an IVF index
quantizer = faiss.IndexFlatIP(n_features)
index = faiss.IndexIVFFlat(quantizer, n_features, nlist)
# Train the index and add feature vectors
index.train(features_standardized)
index.add(features_standardized)
# Create an observation
new_observation = np.array([[ 1,1,1,1]])
# Search the index for the 2 nearest neighbors
distances, indices = index.search(new_observation, k)
# Show the feature vectors for the two nearest neighbors
np.array([list(features_standardized[i]) for i in indices[0]])
