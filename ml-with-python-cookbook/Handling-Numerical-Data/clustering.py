import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

features, _ = make_blobs(n_samples = 50,
n_features = 2,
centers = 3,
random_state = 1)
# Create DataFrame
dataframe = pd.DataFrame(features, columns=["feature_1", "feature_2"])
clusterer = KMeans(3, random_state=0)
clusterer.fit(features)
dataframe["group"] = clusterer.predict(features)
print(dataframe.head(5))
