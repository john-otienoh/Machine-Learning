# You need to rescale the values of a numerical feature to be between two values.
import numpy as np
from sklearn import preprocessing

x = np.array([[-1000.1],
[-200.2],
[500.5],
[600.6],
[9000.9]])
scaler = preprocessing.StandardScaler()
standardized = scaler.fit_transform(x)
print(standardized)
