from sklearn.datasets import make_blobs, make_classification, make_regression
import matplotlib.pyplot as plt

features, target = make_blobs(
    n_samples=100,n_features=2,centers=3,
    cluster_std=0.5,shuffle=True,random_state=1
)
print('Clustering feature matrix\n', features[:3])
print('Clustering target Vector\n', target[:3])
print()
features, target = make_classification(
    n_samples=100,n_features=3,n_informative=3,n_redundant=0,
    n_classes=2,weights=[.25, .75],random_state=1
)
print('Classification feature matrix\n', features[:3])
print('Classification target Vector\n', target[:3])
print()
features, target, coefficients = make_regression(
    n_samples=100,n_features=3,n_informative=3,n_targets=1,
    noise=0.0,coef=True,random_state=1
)
print('Regression feature matrix\n', features[:3])
print('Regression target Vector\n', target[:3])

plt.scatter(features[:,0], features[:,1], c=target)
plt.show()
