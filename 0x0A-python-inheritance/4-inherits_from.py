#!/usr/bin/python3
"Module featuring the inherits_from function."


def inherits_from(obj, a_class):
    """check if an object is a true subclass of a class"""
    a = isinstance(obj, a_class) and type(obj) != a_class
    return a
