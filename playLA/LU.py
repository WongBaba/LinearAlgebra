from playLA.Matrix import Matrix
from playLA._global import is_zero

"""对方阵进行LU分解"""


def lu(matrix):
    assert matrix.row_num() == matrix.col_num(), "Matrix must be a square matrix"
    n = matrix.row_num()
    A = [matrix.row_vector(i) for i in range(n)]
    L = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

    for i in range(n):
        if is_zero(A[i][i]):
            return None, None
        for j in range(i+1, n):
            L[j][i] += (A[j][i] / A[i][i])*L[i][i]
            A[j] -= A[i] * (A[j][i] / A[i][i])

    return L, A


if __name__ == '__main__':
    L, U = lu(Matrix([[1, 2, 3], [4, 5, 6], [3, -3, 5]]))
    print(L,U)
    print(Matrix(L).dot(U))
