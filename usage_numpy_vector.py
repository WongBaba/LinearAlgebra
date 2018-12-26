import numpy as np
"""
numpy包中关于向量的基本使用方法
"""
if __name__ == '__main__':
    print(np.__version__)

    # np.array的创建
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5, 666.))

    # np.array的基本属性
    vec = np.array([1, 2, 3])
    print(type(vec), vec)
    print("size=", vec.size)
    print("size=", len(vec))
    print(vec[1], vec[-1], vec[1:3])

    # np.array的基本运算
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])
    print("{}+{}={}".format(vec1, vec2, vec1 + vec2))
    print("{}-{}={}".format(vec2, vec1, vec2 - vec1))
    print("{}*{}={}".format(5, vec1, 5 * vec1))
    print("{}*{}={}".format(vec1, 5, vec1*5))
    #     向量的逐元素相乘
    print("{}*{}={}".format(vec1, vec2, vec1*vec2))
    #     向量的点乘
    print("{}.dot({})={}".format(vec1, vec2, vec1.dot(vec2)))
    #     向量的模
    print(np.linalg.norm(vec))
    #     向量的单位向量
    print(vec / np.linalg.norm(vec))
    print(np.linalg.norm(vec / np.linalg.norm(vec)))


