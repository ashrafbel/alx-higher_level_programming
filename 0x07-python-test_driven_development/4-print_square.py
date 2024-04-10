#!/usr/bin/python3
"""Module method to print square"""


def print_square(size):
    """method print square
    Args:
        size: The int size of the square's side.

    Raises:
        TypeError: If size is not an int.
        ValueError: If size is < 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    squarzo = ("#" * size + "\n") * size
    print(squarzo, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
