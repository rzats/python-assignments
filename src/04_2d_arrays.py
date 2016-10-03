matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
print (matrix)

# Find the smallest element of each row and column in a matrix (i.e. 2d array / list of lists).

min_rows = [min(row) for row in matrix]
print (min_rows)
min_cols = [min(col) for col in zip(*matrix)]
print (min_cols)

# Rotate a matrix by 90 degrees.

rotated = [list(row) for row in list(zip(*matrix[::-1]))]
print (rotated)

# Check if a matrix is symmetric.

matrix_s = [[1, 2, 3],
            [2, 2, 3],
            [3, 3, 4]]
print (matrix_s)
symmetric = ([tuple(row) for row in matrix_s] == list(zip(*matrix_s)))
print (symmetric)
