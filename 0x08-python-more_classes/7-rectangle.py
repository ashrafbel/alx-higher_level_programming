#!/usr/bin/python3
"""Defines regtangele class"""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        "Create rectangle with the option to specify its width and height"

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        "Assign a value to the width of the rectangle."
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        "Retrieve the perimeter of the rectangle."
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return a string rectangle repreentation"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

        S_tr = []
        for X in range(self.__height):
            [S_tr.append('#') for Y in range(self.__width)]
            if X != self.__height - 1:
                S_tr.append("\n")
        return ("".join(S_tr))

    def __repr__(self):
        """Generate a string representation for the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """print a message when a Rectangle instance is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

