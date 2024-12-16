import numpy as np
import matplotlib.pyplot as plt 
# import matplotlib.pyplotasplt
import math

x_vals = np.linspace(0, 20, 20)
print(x_vals)
y_vals = [math.sqrt(i) for i in x_vals]
plt.plot(x_vals, y_vals)

td_ar = np.random.randint(1, 20, size=(3, 4))
plt.imshow(td_ar)
plt.show()
