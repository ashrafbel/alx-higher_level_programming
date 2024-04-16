#!/usr/bin/python3
"""Define BaseGeometry class"""


class BaseGeometry:
    """class empy"""
    def area(self):
        "Determinates the area."
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for cheking th value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
