#!/usr/bin/python3
"""This function divide a matrix"""


def matrix_divided(matrix, div):
    """The divided matrix returns"""

    typeError = 'matrix must be a matrix (list of lists) of integers/floats'
    new_matrix = []
    if isinstance(matrix, (list, float, int)) is not True:
        raise TypeError(typeError)
    elif isinstance(div, (int, float)) is not True:
        raise TypeError('div must be a number')
    elif len(set([len(row) for row in matrix])) != 1:
        raise TypeError('Each row of the matrix must have the same size')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    else:
        for i in matrix:
            new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
        return(new_matrix)
