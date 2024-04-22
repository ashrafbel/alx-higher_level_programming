#!/usr/bin/python3
"Module defining rect class"
from models.base import Base


class Rectangle(Base):
    "class rect"
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        "width of rect"
        W = self.__width
        return W

    @width.setter
    def width(self, val):
        "setter of width"
        self.valid_int_("width", val, False)
        self.__width = val

    @property
    def height(self):
        "height of rect"
        H = self.__height
        return H

    @height.setter
    def height(self, val):
        "setter height"
        self.valid_int_("height", val, False)
        self.__height = val

    @property
    def x(self):
        "x of rect"
        X = self.__x
        return X

    @x.setter
    def x(self, val):
        "setter x"
        self.valid_int_("x", val)
        self.__x = val

    @property
    def y(self):
        "y of rect"
        Y = self.__y
        return Y

    @y.setter
    def y(self, val):
        self.valid_int_("y", val)
        "seter y"
        self.__y = val

    def valid_int_(self, name_att, val, equal=True):
        "Function to validate the input value."
        if not isinstance(val, int):
            raise TypeError("{} must be an integer".format(name_att))
        if not equal and val <= 0:
            raise ValueError("{} must be > 0".format(name_att))
        if equal and val < 0:
            raise ValueError("{} must be >= 0".format(name_att))

    def area(self):
        "determin the area"
        Area = self.width * self.height
        return Area
