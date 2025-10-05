import numpy as np

A = np.array([1,2],[3,4])
B = np.array([5,6], [7,8])
print(A+B)

# Numpy or numerical python: A .py lib for fast mathematical and scientific computing
# Can be used for linear algebra....
# Has the speed of C/C++ while retaining python syntax...
# Numpy is fast and memory efficient

#  Scalar Matrix... multiplying a matrix with an integer
print(2 * A)
# Transpose matrix: Rows become columns, columns become rows...
print(A.T)
# Multiplication of matrix
print(A.dot(B))
# Determinant: Single number summarizing properties of s square matrix...
print(np.linalg.det(A))
# Inverse Matrix: Matrix (A ^ -1) such that A.(A ^ -1) = 1
# (To find A^-1 matrix, find the det of A, then inverse it and then multiply it by A)
print(np.linalg.inv(A))
# #
