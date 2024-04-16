#!/usr/bin/python3
"""Create a function that adds an attribute to an object if it's feasible."""


def add_attribute(obj_, attr_b, val):
    """Add attr if possible else raise TypeError with "can't add" message"""

    if not hasattr(obj_, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj_, attr_, val)
