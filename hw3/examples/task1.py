import numpy as np
from hw3.matrix import Matrix


def main():
    np.random.seed(0)

    A_np = np.random.randint(0, 10, (10, 10))
    B_np = np.random.randint(0, 10, (10, 10))

    A = Matrix(A_np.tolist())
    B = Matrix(B_np.tolist())

    C_add = A + B
    C_mul = A * B
    C_matmul = A @ B

    C_add.to_file("artifacts/matrix+.txt")
    C_mul.to_file("artifacts/matrix*.txt")
    C_matmul.to_file("artifacts/matrix@.txt")


if __name__ == "__main__":
    main()
