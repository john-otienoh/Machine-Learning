import numpy as np

num_array = np.random.randint(1, 20, 6)
text_array = np.array(['blue', 'red', 'white', 'black'])
bool_array = np.array([False, True, True, False, False, True, False, True])
td_array = np.random.randint(1, 20, size=(4, 6))
# Sorting Arrays in Ascending Order
print(np.sort(num_array))
print(np.sort(text_array))
print(np.sort(bool_array))
print(np.sort(td_array))

# Sorting Arrays in Descending order
print(np.flipud(np.sort(num_array)))

# Reshaping Arrays

print(num_array.reshape(2, 3))
print(np.reshape(num_array, (2,3)))

# 2D arrays
print(np.reshape(td_array, (3, 4, 2)))
print(td_array.reshape(3, 4, 2))

# 2D Lower to higher
print(np.reshape(td_array, 24))
print(td_array.reshape(24))
print(td_array.reshape(-1))
print(np.reshape(td_array, -1))

print(td_array[1:,1:])

#Broadcasting a Numpy Array
scaler_array = np.array([10]) # Each item is added a 10
print(num_array+scaler_array)
print(td_array+scaler_array)
print("hello")
print(td_array+num_array)

print(td_array[3:,2:])

# Statistical Operation  with Python
print(f"The mean of {num_array} is {np.mean(num_array)}")
print(f"The mean of rows of array {td_array} is {np.mean(td_array, axis=0)}")
print(f"The mean of rows of array {td_array} is {np.mean(td_array, axis=1)}")

print(np.max(num_array))
