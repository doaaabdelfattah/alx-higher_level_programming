#!/usr/bin/python3
""" matrix_divided Function Module
"""


def matrix_divided(matrix, div):
    """
    matrix_divided function that divides all elements of a matrix.
    + Parameters:
        matrix: list of lists of integers or floats
        div: number.
    + Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    + Returns:
        new_matrix
    """
    # Check if matrix is a list and list of lists
    if not isinstance(matrix, list) or \
            not (all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a \
                        matrix (list of lists) of integers/floats")
    # Check if all list element is integer or float
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a \
                matrix (list of lists) of integers/floats")
    # Check that each row of matrix is the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # div checks
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Use nested list comprehension to perform the division and rounding
    new_matrix=[[round(element / div, 2)for element in row] for row in matrix]
    return (new_matrix)
