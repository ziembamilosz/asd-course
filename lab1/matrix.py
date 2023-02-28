#!/usr/bin/python
# -*- coding: utf-8 -*-


class Matrix:

    def __init__(self, entrance, fill_value=0):
        if isinstance(entrance, tuple):
            self.matrix = [[fill_value]*entrance[1] for _ in range(entrance[0])]
        else:
            self.matrix = entrance

    def __str__(self):
        rows, cols = self.size()
        result = ""
        for i in range(rows):
            result += "| "
            for j in range(cols):
                result += str(self.matrix[i][j]) + " "
            result += "|\n"
        return result

    def __add__(self, other):
        if self.size() == other.size():
            rows, cols = self.size()
            result = Matrix((rows, cols))
            for i in range(rows):
                for j in range(cols):
                    result[i][j] = self.matrix[i][j] + other[i][j]
            return result
        else:
            return None

    def __mul__(self, other):
        rows_other, cols_other = other.size()
        rows_self, cols_self = self.size()
        if cols_self == rows_other:
            result = Matrix((rows_self, cols_other))
            for i in range(rows_self):
                for j in range(cols_other):
                    for k in range(rows_other):
                        result[i][j] += self.matrix[i][k] * other[k][j]
            return Matrix(result)
        else:
            return None

    def __getitem__(self, item):
        return self.matrix[item]

    def __len__(self):
        return len(self.matrix)

    def size(self):
        return len(self.matrix), len(self.matrix[0])


def transpose(matrix: Matrix) -> Matrix:
    rows, cols = matrix.size()
    transposed_matrix = Matrix((cols, rows))
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


if __name__ == "__main__":

    m1 = Matrix([[1, 0, 2], [-1, 3, 1]])
    m2 = Matrix((2, 3), fill_value=1)
    m3 = Matrix([[3, 1], [2, 1], [1, 0]])

    print(transpose(m1))
    print(m1+m2)
    print(m1*m3)
