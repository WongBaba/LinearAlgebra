from .Vector import Vector


class Matrix(object):
    def __init__(self, list2d):
        # 矩阵数据有效性校验
        for row in list2d:
            for value in row:
                assert type(value) in [int, float], \
                    "Matrix init error,value in Matrix must be integer"

            assert len(row) == len(list2d[0]), \
                "Matrix init error,Length of rows in matrix must be same"

        self._values = [row[:] for row in list2d]

    @classmethod
    def zero(cls, r, c):
        """返回一个r行c列的零矩阵"""
        return cls([[0] * c for _ in range(r)])

    @classmethod
    def identity(cls, n):
        """返回一个n行n列的单位矩阵"""
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)

    def T(self):
        return Matrix([self.col_vector(i) for i in range(self.col_num())])

    def dot(self, other):
        """返回矩阵乘法的结果"""
        if isinstance(other, Vector):
            # 矩阵和向量的乘法
            assert self.col_num() == len(other), \
                "Error in Matrix-Vector Multiplication,Length of vector must same with matrix's column length"
            return Vector([other.dot(self.row_vector(i)) for i in range(self.row_num())])

        elif isinstance(other, Matrix):
            # 矩阵和矩阵的乘法
            assert self.col_num() == other.row_num(), \
                "Error in Matrix-Matrix Multiplication."
            # return Matrix([self.dot(other.col_vector(i)) for i in range(other.col_num())])
            return Matrix([[self.row_vector(i).dot(other.col_vector(j))
                            for j in range(other.col_num())] for i in range(self.row_num())])

    def __add__(self, other):
        """返回两个矩阵的加法结果"""
        assert self.shape() == other.shape(), \
            "Error in adding. Shape of matrix must be same."
        return Matrix([[(a + b) for a, b in zip(self.row_vector(i), other.row_vector(i))]
                       for i in range(self.row_num())])

    def __sub__(self, other):
        """返回两个矩阵的减法结果"""
        assert self.shape() == other.shape(), \
            "Error in adding. Shape of matrix must be same."
        return Matrix([[(a - b) for a, b in zip(self.row_vector(i), other.row_vector(i))]
                       for i in range(self.row_num())])

    def __mul__(self, k):
        """返回矩阵的数量右乘结果:self*k"""
        return Matrix([[k * a for a in self.row_vector(i)] for i in range(self.row_num())])

    def __rmul__(self, k):
        """返回矩阵的数量右乘结果:self*k"""
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果矩阵:self/k"""
        return 1 / k * self

    def __pos__(self):
        """返回矩阵取正的结果"""
        return self * 1

    def __neg__(self):
        """返回矩阵取负的结果"""
        return self * -1

    def row_vector(self, index):
        """返回矩阵pos位置的第index个行向量"""
        assert index < self.row_num(), \
            "Index error,out of Matrix row index"
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵pos位置的第index个行向量"""
        assert index < self.col_num(), \
            "Index error,out of Matrix column index"
        return Vector([row[index] for row in self._values])

    def __getitem__(self, pos):
        """返回矩阵pos位置的元素"""
        r, c = pos
        return self._values[r][c]

    def size(self):
        """返回矩阵的元素个数"""
        shape = self.shape()
        return shape[0] * shape[1]

    def row_num(self):
        """返回矩阵的行数"""
        return self.shape()[0]

    __len__ = row_num

    def col_num(self):
        """返回矩阵的列数"""
        return self.shape()[1]

    def shape(self):
        """返回矩阵的形状:(行数,列数)"""
        return len(self._values), len(self._values[0])

    def __repr__(self):
        return "Matrix({})".format(self._values)

    def __str__(self):
        return "Matrix({})".format(self._values)
