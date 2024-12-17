import numpy as np

# Solve the following system of three linear equations and find the values of
# the variables x, y, and z:
# 3x + 4y + 2z = 17
# 5x + 2y + 3z = 23
# 4x + 3y + 2z = 19

# 1. Convert the equation to matrix and vectors
matrix = np.array(
    [
        [3, 4, 2],
        [5, 2, 3],
        [4, 3, 2]
    ]
)
vector = np.array([[17], [23], [19]])

# 2. Find inverse of the matrix
inverse_matrix = np.linalg.inv(matrix)

# 3. Find dot product
dot_product = np.dot(inverse_matrix, vector)

print(f"""
    The value of x = {dot_product[0]}
    The value of y = {dot_product[1]}
    The value of z = {dot_product[2]}
      """)
