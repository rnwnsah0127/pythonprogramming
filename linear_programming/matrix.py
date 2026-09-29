import numpy as np

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

diagonal_sum = matrix[0][0] + matrix[1][1] + matrix[2][2]

print("대각합:",diagonal_sum)

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("대각합:", np.trace(matrix))