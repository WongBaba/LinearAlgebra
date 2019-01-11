from playLA.Matrix import Matrix, Vector

if __name__ == '__main__':
    matrix = Matrix([[1, 2], [3, 4]])
    print("1 matrix={}".format(matrix))
    print("2 matrix.shape={}".format(matrix.shape()))
    print("3 row_num={},col_num={}".format(matrix.row_num(), matrix.col_num()))
    print("4 len(matrix)={}".format(len(matrix)))
    print("5 matrix.size={}".format(matrix.size()))
    print("6 matrix[1][1]={}".format(matrix[1, 1]))
    print("7 matrix.row_vector(1)={}".format(matrix.row_vector(1)))
    print("8 matrix.col_vector(1)={}".format(matrix.col_vector(1)))
    matrix2 = Matrix([[5, 6], [7, 8]])
    print("9 {}+{}={}".format(matrix, matrix2, matrix + matrix2))
    print("9 {}-{}={}".format(matrix, matrix2, matrix - matrix2))
    print("10 {}*{}={}".format(6, matrix, 3 * matrix * 2))
    print("11 {}/{}={}".format(matrix2, 2, matrix2 / 2))
    zero_matrix = Matrix.zero(2, 3)
    print("12 zero_matrix of 2,3:{}".format(zero_matrix))
    # 矩阵乘以向量
    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print("13 {}.dot({})={}".format(T, p, T.dot(p)))
    # 矩阵和矩阵相乘
    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print("14 {}.dot({})={}".format(T, P, T.dot(P)))

    print("15 A.dot(B)={}".format(matrix.dot(matrix2)))
    print("16 B.dot(A)={}".format(matrix2.dot(matrix)))

    print("17 {}.T()={}".format(P, P.T()))

    # 生成一个单位矩阵
    I = Matrix.identity(2)
    print(I)
    print("18 {}.dot({})={}".format(matrix, I, matrix.dot(I)))
    print("19 {}.dot({})={}".format(I, matrix, I.dot(matrix)))
