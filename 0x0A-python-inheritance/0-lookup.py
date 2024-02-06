#!/usr/bin/python3
"""DEF LOOKUP"""


def lookup(obj):
    """Lookup method
    Args:
        obj:Listing the object

    Returns:
        The List of attrubutes
    """
    return dir(obj())
