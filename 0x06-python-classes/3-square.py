#!/usr/bin/python3

"""Class Square."""


class Square:
    """Define square."""

    def __init__(self, size=0):
        """Initialize new square.

        Argements:
            size (int): Size square.

        Raises:
            typeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area sqiared.
        Rerun:
        size squared
        """
        return self.__size ** 2
