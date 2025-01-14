def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    """Function that takes the dot product of a matrix and a vector.
    return -1 if the matrix could not be dotted with the vector.
"""
    if len(a[0]) != len(b):
        return -1
    vals = []
    for i in a:
        hold = 0
        for j, _ in enumerate(i):
            hold+=(i[j] * b[j])
        vals.append(hold)

    return vals	
matrix = [[1, 2], [2,4], [5, 6]]
vector = [1, 2]

print(matrix_dot_vector(matrix, vector))
