#!/usr/bin/python3
'''Module featuring Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representing a rectangle.'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''determnated area of square'''
        return self.__size ** self.__size
