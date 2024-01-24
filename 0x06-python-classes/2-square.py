#!/usr/bin/python3
"""Class Square"""


class Square:
    def __init__(self, size=0):
        """Initialize new square
        argument:
            size (int): size of square
        Raises:
            typeeerror if size not integer
            valueerror if size less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
