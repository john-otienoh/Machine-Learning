def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    """function that reshapes a given matrix into a specified shape."""
    a, reshaped_matrix = [j for i in a for j in i], []
    count = 0
    for _ in range(new_shape[0]):
        value = []
        for i in range(new_shape[1]):
            value.append(a[count])
            count += 1

        reshaped_matrix.append(value)
    return reshaped_matrix

new_shapes  = (4, 2)
matrix =[[1,2,3,4], [5,6,7,8]]
print(reshape_matrix(matrix, new_shapes))
