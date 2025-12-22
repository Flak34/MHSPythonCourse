import numpy as np
from hw3.matrix_mixin import Matrix

np.random.seed(0)

A = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
B = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

C_add = A + B
C_sub = A - B
C_mul = A * B

C_add.to_file("artifacts/matrix_mixin+.txt")
C_sub.to_file("artifacts/matrix_mixin-.txt")
C_mul.to_file("artifacts/matrix_mixin*.txt")