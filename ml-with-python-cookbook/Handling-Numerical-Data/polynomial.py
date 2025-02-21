import numpy as np
from sklearn.preprocessing import PolynomialFeatures

features = np.array([[2, 3],
[2, 3],
[2, 3]])
polynomial_interaction = PolynomialFeatures(degree=2, include_bias=False)
polynomial_interaction.fit_transform(features)
