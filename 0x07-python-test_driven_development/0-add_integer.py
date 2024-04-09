#!/usr/bin/python3
"""add integer addition method"""


def add_integer(a, b=98):
    """return two integer a,b.

    Raises:
        TypeError: If  a or b is not integer and float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
