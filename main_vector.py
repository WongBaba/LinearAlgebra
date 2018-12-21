from playLA.Vector import Vector

if __name__ == '__main__':
    vec1 = Vector([5, 2])
    vec2 = Vector([2, 5])
    print("{}+{}={}".format(vec1, vec2, vec1 + vec2))
    print("{}-{}={}".format(vec1, vec2, vec1 - vec2))

    print("{}*{}={}".format(vec1, 3, vec1 * 3))
    print("{}*{}={}".format(3, vec1, 3 * vec1))
    print("{}".format(+vec1))
    print("{}".format(-vec1))
    zero_vec = Vector.zero(2)
    print(Vector.zero(8))
    print("{}+{}={}".format(zero_vec, vec1, zero_vec + vec1))
