#!/usr/bin/python3
"""Introduces a class with restricted attribute modification."""


class LockedClass:
    """
    Ensure that users are restricted from creating new attributes
    in LockedClass except for
    those specifically named 'first_name'.
    """

    __slots__ = ["first_name"]
