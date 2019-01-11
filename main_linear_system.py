from playLA.LinearSystem import LinearSystem, inv
from playLA.Matrix import Matrix
from playLA.Vector import Vector

M1 = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
V1 = Vector([7, -11, 1])
A_M1 = LinearSystem(M1, V1)

print(A_M1.gauss_jordan_elimination())
A_M1.fancy_print()

M2 = Matrix([[1, -1, 2, 0, 3], [-1, 1, 0, 2, -5], [1, -1, 4, 2, 4], [-2, 2, -5, -1, -3]])
V2 = Vector([1, 5, 13, -1])
A_M2 = LinearSystem(M2, V2)

print(A_M2.gauss_jordan_elimination())
A_M2.fancy_print()

M3 = Matrix([[2, 1, -1, 1, 1], [1, 2, 1, -1, 2], [1, 1, 2, 1, 3]])
V3 = Vector([0, 0, 0])
A_M3 = LinearSystem(M3, V3)

print(A_M3.gauss_jordan_elimination())
A_M3.fancy_print()

M4 = Matrix([[2, 2], [2, 1], [1, 2]])
V4 = Vector([3, 2.5, 7])
A_M4 = LinearSystem(M4, V4)
print(A_M4.gauss_jordan_elimination())
A_M4.fancy_print()

M5 = Matrix([[1, 3, 0, 0], [2, 4, 0, 0], [0, 0, 1, 3], [0, 0, 2, 4]])
V5 = Vector([1, 0, 0, 1])
A_M5 = LinearSystem(M5, V5)
print(A_M5.gauss_jordan_elimination())
A_M5.fancy_print()

M5 = Matrix([[1, 2], [3, 4]])
inv5 = inv(M5)
print(inv5.dot(M5))
