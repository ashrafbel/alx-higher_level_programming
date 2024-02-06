#!/usr/bin/python3
""""Module featuring Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass representing a rectangle.'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Method that returns the area of the rectangle.'''
        return self.__width * self.__height

    def __str__(self):
        '''Method for creating a string representation.'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
