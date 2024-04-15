#!/usr/bin/python3
"""Module the is_same_class method"""


def is_same_class(obj, a_class):
    "Verify whether an object belongs to a specified class"
    return type(obj) == a_class
