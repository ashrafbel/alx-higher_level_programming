#!/usr/bin/python3
"""Defines a function that adds attributes"""


def add_attribute(obj, at, val):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, at, val)
