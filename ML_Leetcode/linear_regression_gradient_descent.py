import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros((n, 1))
    for _ in range(iterations):
        prediction = X @ theta
        errors = prediction - y.reshape(-1, 1)
        updates = X.T @ errors / m
        theta -= updates*alpha

    return np.round(theta.flatten(), 4)

X, y = np.array([[1, 1], [1, 2], [1, 3]]), np.array([1, 2, 3]), 
alpha, iterations = 0.01, 1000
print(linear_regression_gradient_descent(X,y,alpha,iterations))
