def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    """function that multiplies a matrix by a scalar and returns the result."""
    result = []
    for i in matrix:
        value = [i[j] * scalar for j, _ in enumerate(i)]
        result.append(value)
    return result
matrix, scalar = [[1,2], [3,4]], 2
print(scalar_multiply(matrix, scalar))
