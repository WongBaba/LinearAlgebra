import numpy as np


def printf(arg, title=""):
    if title:
        print(title, "\n", arg, end="\n-----------\n")
    else:
        print(arg, end="\n-----------\n")


if __name__ == '__main__':
    # 1.矩阵的创建
    A = np.array([[1, 2], [3, 4]])
    printf(A, "创建矩阵A")

    # 2.矩阵的属性
    printf(A.shape, "矩阵的形状")
    printf(A.T, "矩阵的转置矩阵")

    # 3.获取矩阵中的元素
    printf(A[1, 1], "获取指定单个元素")
    printf(A[0], "获取指定行元素")
    printf(A[:, 0], "获取指定列元素")

    # 4.矩阵的基本运算
    B = np.array([[5, 6], [7, 8]])
    printf(A + B, "矩阵的加法")
    printf(A - B, "矩阵的减法")
    printf(10 * A, "矩阵的数值左乘")
    printf(A * 10, "矩阵的数值右乘")
    printf(A * B, "numpy中的矩阵乘法指的是逐元素相乘")
    printf(A.dot(B), "矩阵和矩阵的点乘")

    # 5.矩阵和向量的运算
    p = np.array([10, 100])
    printf(A + p, "矩阵与向量的加法")
    printf(A + 1, "矩阵与数值的加法")
    printf(A.dot(p), "矩阵与向量的点乘")

    # 6.单位矩阵
    I = np.identity(2)
    printf(A.dot(I), "单位矩阵与向量相乘(A.dot(I))")
    printf(I.dot(A), "单位矩阵与向量相乘(I.dot(A))")

    # 使用逆矩阵
    invA = np.linalg.inv(A)
    printf(invA, "A的逆矩阵")
    printf(A.dot(invA), "A与A的逆矩阵相乘")
    printf(invA.dot(A), "A的逆矩阵与A相乘")