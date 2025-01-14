def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """function that computes the transpose of a given matrix."""
    b = []
    for i, _ in enumerate(a[0]):
        value = []
        for j,_ in enumerate(a):
            value.append(a[j][i])
        b.append(value)
    return b

matrix = [[1,2,3], [4,5,6]]
print(transpose_matrix(matrix))
