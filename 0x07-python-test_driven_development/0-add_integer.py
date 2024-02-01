#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    - a : first number.
    - b : second number (default is 98)

    Returns:
    sum of a and b integers

    Raises:
    - TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    x = int(a)
    y = int(b)

    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
