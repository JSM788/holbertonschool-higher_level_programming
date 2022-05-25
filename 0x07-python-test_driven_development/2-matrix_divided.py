#!/usr/bin/python3
"""This function divide a matrix"""


def matrix_divided(matrix, div):
    """The divided matrix returns"""

    new_matrix = []
    if div == 0:
        raise ZeroDivisionError('division by zero')
    else:
        for i in matrix:
            new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
        return(new_matrix)
