import matplotlib.pyplot as plt
from playLA.Matrix import Matrix
from playLA.Vector import Vector


def plot_matrix(*args):
    for P in args:
        plt.plot([i for i in P.row_vector(0)], [i for i in P.row_vector(1)])


if __name__ == '__main__':
    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
              [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    # region 绘制图形以及设置绘制参数
    # 设置绘制窗口大小(单位是5英尺)
    plt.figure(figsize=(5, 5))
    # 设置x轴坐标区间是-10到10
    plt.xlim(-10, 10)
    # 设置y轴坐标区间是-10到10
    plt.ylim(-10, 10)

    # 绘制
    plt.plot(x, y)
    # endregion

    P = Matrix(points)

    # 设置变换函数
    #   T1:x轴放大2倍,y轴放大1.5倍
    T1 = Matrix([[2, 0], [0, 1.5]])
    #   T2:所有点沿x轴翻转
    T2 = Matrix([[1, 0], [0, -1]])
    #   T3:所有点沿y轴翻转
    T3 = Matrix([[-1, 0], [0, 1]])
    #   T4:所有点沿远点对称
    T4 = Matrix([[-1, 0], [0, -1]])

    P1 = T1.dot(P.T())
    P2 = T2.dot(P.T())
    P3 = T3.dot(P.T())
    P4 = T4.dot(P.T())

    # 批量plot绘制矩阵
    plot_matrix(P1, P2, P3, P4)

    plt.show()
