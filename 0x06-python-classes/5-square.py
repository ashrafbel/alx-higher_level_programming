#!/usr/bin/python3

"""class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Arguments:
            size (int) size new square.
        """
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """Initialize new square
        Raises:
            typeeerror if size not integer
            valueerror if size less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        for S in range(0, self.__size):
            [print("#", end="") for K in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
