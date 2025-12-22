import random


class Matrix:
    def __init__(self, data):
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same length")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same shape for addition")

        result = [
            [
                self.data[i][j] + other.data[i][j]
                for j in range(self.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same shape for element-wise multiplication")

        result = [
            [
                self.data[i][j] * other.data[i][j]
                for j in range(self.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "For matrix multiplication, number of columns of the first matrix "
                "must equal number of rows of the second"
            )

        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                s = 0
                for k in range(self.cols):
                    s += self.data[i][k] * other.data[k][j]
                row.append(s)
            result.append(row)

        return Matrix(result)

    def to_file(self, filename):
        with open(filename, "w") as f:
            for row in self.data:
                f.write(" ".join(map(str, row)) + "\n")

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.data)