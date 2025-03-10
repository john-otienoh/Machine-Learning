from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import datasets

iris = datasets.load_iris()
X, y = iris.data,iris.target

standardizer = StandardScaler()
x_std = standardizer.fit_transform(X)
knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1).fit(x_std, y)
new_observations = [
    [0.75, 0.75, 0.75, 0.75],
    [1, 1, 1, 1]
]

print(knn.predict(new_observations))
print(knn.predict_proba(new_observations))
