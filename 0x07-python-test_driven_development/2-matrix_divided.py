#!/usr/bin/python3
"""
returning new matrix
"""


def matrix_divided(matrix, div):
    """
    handling errors
    """
    if isinstance(matrix, list) == False:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    for x in matrix:
        for y in x:
            if isinstance(y, (int, float)) == False:
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats\
                        ')
        if len(x) != len(matrix[0]):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    if isinstance(div, (int, float)) == False:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(y / div, 2) for y in x] for x in matrix]
