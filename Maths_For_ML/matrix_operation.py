import numpy as np

A = np.array([[1, 2], [4, 5]])
B = np.array([[3, 6], [7, 8]])
eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"Addition of matrix {A} and {B} = {A+B}")
print(f"Subtraction of matrix {A} and {B} = {A-B}")
print(f"Multiplication of matrix {A} and {B} = {np.matmul(A,B)}")
print(f"Multiplication of matrix {A} and {B} = {A@B}")

print(eigenvalues)
print(eigenvectors)
