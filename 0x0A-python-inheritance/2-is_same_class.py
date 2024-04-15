#!/usr/bin/python3
"Module with the is_same_class function."



def is_same_class(obj, a_class):
    """Verify whether an object belongs to a specified class."""
    return type(obj) == a_class
