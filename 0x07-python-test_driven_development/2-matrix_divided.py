#!/usr/bin/python3
"""Module matrix devie"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.
    Args:
        matrix: list of lists of integers or floats
        div: number integer or float
    Returns:
        new matrix with elements rounded to 2 decimal places after division
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for r in matrix:
        if not isinstance(r, list) or len(r) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(r) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    res = [[round(a / div, 2) for a in r] for r in matrix]

    return res


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
