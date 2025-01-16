def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    """function to calculate the covariance matrix for a given set of vectors.
    The function should take a list of lists, where each inner list represents a feature with its observations, 
    and return a covariance matrix as a list of lists. """
    result = []
    for i in vectors:
        mean = sum(i) / len(i)
        for j, _ in enumerate(i):
            value = [i[j] - mean for j,_ in enumerate(i)]
        result.append(sum(value) / (len(value) - 1))
    return result

vector = [[1, 2, 3], [4, 5, 6]]
print(calculate_covariance_matrix(vector))
