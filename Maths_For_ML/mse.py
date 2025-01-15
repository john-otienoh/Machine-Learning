import numpy as np

def mean_squared_error(y_true, y_pred):
    """calculation of mean squared error (MSE) loss"""
    return np.mean((y_true - y_pred) ** 2)

y_true_array = np.array([1, 2, 3, 4, 5])
y_pred_array = np.array([1.1, 2.2, 2.8, 3.9, 5.1])
mse_loss = mean_squared_error(y_true_array, y_pred_array)
print(f"Mean Squared Error is {mse_loss}")
