#!/usr/bin/python3


def matrix_divided(matrix, div):
    sum_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if len(i) != len(matrix[0]):
           raise TypeError("Each row of the matrix must have the sane size")
        for n in i:
           if not isinstance(n, (int, float)):
              raise TypeError("matrix bust be a matrix (list of lists)"
                            " of integers/floats")
        sum = list(map(lambda x: round(x / div, 2), i))
        sum_matrix.append(sum)
    return sum_matrix
