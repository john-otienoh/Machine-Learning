from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import datasets

iris = datasets.load_iris()
features,target = iris.data, iris.target

standardizer = StandardScaler()
features_standardizer = standardizer.fit_transform(features)
rnn = RadiusNeighborsClassifier(radius=.5, n_jobs=-1).fit(features_standardizer, target)
new_observations = [[1, 1, 1, 1]]
print(rnn.predict(new_observations))
print(rnn.predict_proba(new_observations))
