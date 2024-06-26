#!/usr/bin/python3
"""Module featuring the inherits_from function."""


def inherits_from(obj, a_class):
    """check if an object is a true subclass of a class"""
    b = isinstance(obj, a_class) and type(obj) is not a_class
    return b
