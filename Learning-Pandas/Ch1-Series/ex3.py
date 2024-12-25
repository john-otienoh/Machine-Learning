import pandas as pd
import numpy as np
# In this exercise, I want you to generate 10 random integers in the range 0 to 100.
# Create a series containing those numbers tens digits. 
# Thus, if our series contains 10, 25, 32, we want the series 1, 2, 3.
s = pd.Series(np.random.randint(0, 100, 10))
print(s)
s //= 10
print(s)
