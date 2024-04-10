#!/usr/bin/python3
"""Method sy my name"""


def say_my_name(first_name, last_name=""):
    """first and last name printed
    Args:
        first_name: the first name str
        last_name: the last name str
    Raises:
        TypeError: if two args first & last not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    x = "My name is {:s} {:s}".format(first_name, last_name)
    print(x)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
