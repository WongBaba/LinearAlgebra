from playLA.Vector import Vector

if __name__ == '__main__':
    vec1 = Vector([5, 2])
    vec2 = Vector([3, 1])
    zero = Vector([0,0])
    print("{}+{}={}".format(vec1, vec2, vec1 + vec2))
    print("{}-{}={}".format(vec1, vec2, vec1 - vec2))

    print("{}*{}={}".format(vec1, 3, vec1 * 3))
    print("{}*{}={}".format(3, vec1, 3 * vec1))
    print("{}".format(+vec1))
    print("{}".format(-vec1))
    zero_vec = Vector.zero(2)
    print(Vector.zero(8))
    print("{}+{}={}".format(zero_vec, vec1, zero_vec + vec1))
    # 向量的模
    print("norm({}) = {}".format(vec1, vec1.norm()))
    print("norm({}) = {}".format(vec2, vec2.norm()))
    # 单位向量
    print("normalize({}) = {}".format(vec1, vec1.normalize()))
    try:
        zero.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}.".format(zero))
    # 点乘
    print("{}*{}={}".format(vec1,vec2,vec1.dot(vec2)))
