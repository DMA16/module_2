def get_matrix(n, m, value):
    matrix = []

    if value <= 0:
        return matrix

    for i in range(n):
        matrix.append([])

        for j in range(m):
            matrix[i].append(value)

    return matrix

print(get_matrix(3, 0, 4))