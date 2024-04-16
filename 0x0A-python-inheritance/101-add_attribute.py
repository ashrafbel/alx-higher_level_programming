#!/usr/bin/python3
"""Defines a function that adds attributes"""


def add_attribute(ob, at, val):
    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, at, val)
