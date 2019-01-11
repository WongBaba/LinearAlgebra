from .Matrix import Matrix
from .Vector import Vector
from ._global import is_zero


class LinearSystem(object):

    # 构建增广矩阵(argument matrix),增广矩阵结构为:Matix|Vector
    def __init__(self, A, b):
        assert A.row_num() == len(b), \
            "row number of A must be equal to the length of b"
        # 记录矩阵的行数和列数
        self._r = A.row_num()
        self._c = A.col_num()
        self.pivots = []
        if isinstance(b, Vector):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) for i in range(self._r)]
        elif isinstance(b, Matrix):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list()) for i in range(self._r)]

    def _max_row(self, row, col):
        """返回元素往下所在列中的最大元素的下标"""
        max_value, ret = self.Ab[row][col], row
        for i in range(row + 1, self._r):
            if self.Ab[i][col] > max_value:
                max_value, ret = self.Ab[i][col], i
        return ret

    def _forward(self):
        row = 0
        col = 0
        while row < self._r and col < self._c:
            max_row = self._max_row(row, col)
            if is_zero(self.Ab[max_row][col]):
                col += 1
                continue
            self.Ab[row], self.Ab[max_row] = self.Ab[max_row], self.Ab[row]

            # 主元归1
            self.Ab[row] /= self.Ab[row][col]
            self.pivots.append([row, col])
            for i in range(row + 1, self._r):
                self.Ab[i] -= self.Ab[row] * self.Ab[i][col]

            row += 1

    def _backward(self):

        for n in range(len(self.pivots) - 1, -1, -1):
            for i in range(0, self.pivots[n][0]):
                self.Ab[i] -= self.Ab[self.pivots[n][0]] * self.Ab[i][self.pivots[n][1]]

    def gauss_jordan_elimination(self):
        """如果有解返回True;如果没解,返回False"""
        self._forward()
        self._backward()

        for i in range(len(self.pivots),self._r):
            if not is_zero(self.Ab[i][self._c]):
                return False
        return True

    def fancy_print(self):
        print()
        for i in range(self._r):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._c)), end=" ")
            print("|", self.Ab[i][self._c])


def inv(A):

    n = A.row_num()
    if n!= A.col_num():
        return None

    ls = LinearSystem(A, Matrix.identity(n))
    if not ls.gauss_jordan_elimination():
        return None

    invA = [row[n:] for row in ls.Ab]
    return Matrix(invA)