#!/usr/bin/python3
"""Create a function that adds an attribute to an object if it's feasible."""


def add_attribute(obj, attr, val):
    """Add attr if possible else raise TypeError with "can't add" message"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
