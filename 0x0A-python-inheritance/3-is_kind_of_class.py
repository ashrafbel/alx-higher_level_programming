#!/usr/bin/python3
"Module featuring the is_kind_of_class function."


def is_kind_of_class(obj, a_class):
    "Determines whether an object is a subclass of a specified class."
    a = isinstance(obj, a_class)
    return a
