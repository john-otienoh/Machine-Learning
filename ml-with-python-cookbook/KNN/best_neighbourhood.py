from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import datasets

iris = datasets.load_iris()
features, target = iris.data, iris.target
standardizer = StandardScaler()
knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1)
features_standardized = standardizer.fit_transform(features)
pipe = Pipeline([("standardizer", standardizer), ("knn", knn)])
search_space = [{"knn__n_neighbors": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}]
classifier = GridSearchCV(pipe, search_space, cv=5, verbose=0).fit(features_standardized, target)
# Best neighbourhood size (k)
print(classifier.best_estimator_.get_params()['knn__n_neighbors'])
