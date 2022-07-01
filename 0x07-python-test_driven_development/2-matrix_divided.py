#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divides all the values of the matrix"""
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(matrix_error)

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    results_matrix = []
    for list in matrix:
        if type(list) != list:
            raise TypeError(matrix_error)

        if len(list) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        c_resList = []
        for item in list:
            if type(item) != int and type(item) != float:
                raise TypeError(matrix_error)
            c_resList.append(round(item/div, 2))
        results_matrix.append(c_resList)
    return results_matrix
