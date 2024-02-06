#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Verify whether an object belongs to a specified class."""
    if type(obj) == a_class:
        return True
    else:
        return False
