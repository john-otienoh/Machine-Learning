import numpy as np

# Generate a NumPy array of shape 5 x 7, 
# containing random integers between 1 and 50. 
# Find the mean, median, and minimum and maximum values across columns and rows.


td_array = np.random.randint(1, 50, size=(5, 7))
print(td_array)
print("Rows:")

# Mean of rows
print(f"The mean of rows is {np.mean(td_array, axis=1)}")
# Median of rows
print(f"The median of rows is {np.median(td_array, axis=1)}")
# Maximum values of rows
print(f"The maximum value of each row is {np.amax(td_array, axis=1)}")
# Minimum values of rows
print(f"The minimum value ofeach row is {np.amin(td_array, axis=1)}")

print("Columns:")

# Mean of columns
print(f"The mean of columns is {np.mean(td_array, axis=0)}")
# Median of columns
print(f"The median of columns is {np.median(td_array, axis=0)}")
# Maximum values of columns
print(f"The maximum value of each column is {np.amax(td_array, axis=0)}")
# Minimum values of coulmns
print(f"The minimum value of each column is {np.amin(td_array, axis=0)}")
