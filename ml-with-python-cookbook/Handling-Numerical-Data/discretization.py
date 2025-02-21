import numpy as np
from sklearn.preprocessing import Binarizer

age = np.array([[6],
[12],
[20],
[36],
[65]])
binarizer = Binarizer(threshold=18)
binarizer.fit_transform(age)

# Bin feature
np.digitize(age, bins=[20,30,64])