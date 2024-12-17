import numpy as np
# Create a random Numpy array of four rows and five columns
# Then, using array indexing and slicing, 
# display the items from row 3 to end and column 2 to the end

random_array = np.random.randint(1, 20, size=(4, 5))

print(random_array)
print("After Slicing")
print(random_array[2:,1:])
