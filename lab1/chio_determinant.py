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

    def swap_rows(self, i, j):
        self.matrix[i], self.matrix[j] = self.matrix[j], self.matrix[i]


def determinant_for_2x2(matrix: Matrix) -> float:
    return matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]


def eliminate_zero_from_a11(matrix: Matrix) -> Matrix:
    rows, _ = matrix.size()
    for i in range(1, rows):
        if matrix[i][0] != 0:
            matrix.swap_rows(0, i)
            break
    return matrix


def recursive_chio(matrix: Matrix, multiplier: float) -> float:

    if matrix.size() == (2, 2):
        return multiplier*determinant_for_2x2(matrix)

    rows, cols = matrix.size()
    reduced_matrix = Matrix((rows-1, cols-1))

    if matrix[0][0] == 0:
        matrix = eliminate_zero_from_a11(matrix)
        multiplier *= -1

    for i in range(1, rows):
        for j in range(1, cols):
            matrix_2x2 = [[matrix[0][0], matrix[0][j]], [matrix[i][0], matrix[i][j]]]
            reduced_matrix[i-1][j-1] = determinant_for_2x2(Matrix(matrix_2x2))
    return recursive_chio(reduced_matrix, multiplier*(1/matrix[0][0]**(rows-2)))


def chio_determinant(matrix: Matrix):
    rows, cols = matrix.size()
    if rows != cols:
        return None
    return recursive_chio(matrix, 1)


if __name__ == "__main__":

    m1 = Matrix([
    [5, 1, 1, 2, 3],
    [4, 2, 1, 7, 3],
    [2, 1, 2, 4, 7],
    [9, 1, 0, 7, 0],
    [1, 4, 7, 2, 2]])

    # przy liczeniu tego wyznacznika trzeba zamienić kolejność wierszy tak by element a11 nie był zerem,
    # a nastepnie pomnozyc wyznacznik przez -1 (z wlasnosci wyznacznikow), w tym celu zaimplementowalem
    # metode klasy Matrix swap_rows() do zamiany wierszy oraz funkcje eliminate_zero_from_a11() ktora dokonuje
    # odpowiedniej zamiany wtedy gdy jest to potrzebne

    m2 = Matrix([
    [0, 1, 1, 2, 3],
    [4, 2, 1, 7, 3],
    [2, 1, 2, 4, 7],
    [9, 1, 0, 7, 0],
    [1, 4, 7, 2, 2]
    ])

    print(chio_determinant(m1))
    print(chio_determinant(m2))
