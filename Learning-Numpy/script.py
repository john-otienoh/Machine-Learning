import numpy as np

a = np.array([[6, 3], [2, 4]])
b = np.array([[42], [32]])

c = np.dot(np.linalg.inv(a), b)
print(c)
