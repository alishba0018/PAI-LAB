def matrix_addition(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    return result
def matrix_multiplication(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must equal number of rows in B")
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8, 9],
     [10, 11, 12]]
C = [[1, 2],
     [3, 4],
     [5, 6]]
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("\nAddition of A and B:")
print(matrix_addition(A, B))
print("\nMultiplication of A and C:")
print(matrix_multiplication(A, C))
