#!/usr/bin/python3
"""Rectangle Cls"""


class Rectangle:
    """Rectangel Empty"""
    def __init__(self, width=0, height=0):
        """intialize cls"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter width react"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width rect"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter height rect"""
        return self.__height

    def height(self, value):
        """setter height rect"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
