class Vector:
    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls,dim):
        """返回一个dim维的零向量
        zero_vec = Vector.zero(2)"""
        return cls([0] * dim)

    def __add__(self, other):
        """向量加法，返回结果向量
        print("{}+{}={}".format(vec1, vec2, vec1 + vec2))"""
        assert len(self) == len(other), \
            "Error in adding.Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """向量减法，返回结果向量
        print("{}-{}={}".format(vec1, vec2, vec1 - vec2))"""
        assert len(self) == len(other), \
            "Error in subtracting. Length of vectors must be same"
        return Vector([a - b for a, b in zip(self, other)])

    # mul是定义了一个左乘的数学运算
    def __mul__(self, k):
        """向量的数量乘法，返回结果向量：
        print("{}*{}={}".format(vec1, 3, vec1*3))"""
        return Vector([k * a for a in self])

    # rmul是定义了一个右乘的数学运算
    def __rmul__(self, k):
        """返回数量乘法的结果向量
        print("{}*{}={}".format(3, vec1, 3 * vec1))
        """
        return self * k

    def __pos__(self):
        """返回向量取正的结果向量
        print("{}".format(+vec1))
        """
        return self

    def __neg__(self):
        """返回向量取负的结果向量
        print("{}".format(-vec1))"""
        return -1 * self

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __len__(self):
        """返回向量长度（有多少个元素）
        print(len(vec1))"""
        return len(self._values)

    def __getitem__(self, index):
        """取向量的第index个元素
        print(vec1[index])"""
        return self._values[index]

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

# if __name__ == '__main__':
#     vt = Vector([1,3,5])
#     print(vt)
