"""Rectangle Cls"""


class Rectangle:
    """Represent rectangle"""

    def __init__(self, width=0, height=0):
        "intialize cls"

        self.width = width
        self.height = height

    @property
    def width(self):
        """getter width react"""
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
        "getter height rect"
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area Rect"""
        return (self.__width * self.__height)

    def perimeter(self):
        "return perimeter rect"
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
