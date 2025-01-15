def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    """function that calculates the mean of a matrix either by row or by column, based on a given mode.
    The function should take a matrix (list of lists) and a mode ('row' or 'column') as input
    and return a list of means according to the specified mode."""
    means = []
    if mode == 'row':
        for i in matrix:
            means.append(sum(i) / len(i))
    elif mode == 'column':
        b = []
        for i, _ in enumerate(matrix[0]):
            value = [matrix[j][i] for j,_ in enumerate(matrix)]
            b.append(value)
        for i in b:
            means.append(sum(i) / len(i))
    return means

matrix, mode = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'column'

print(calculate_matrix_mean(matrix, mode))
