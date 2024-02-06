#!/usr/bin/python3
"""Def function ReadFile"""


def read_file(filename=""):
    """Reads a UTF-8 encoded text file and displays
    its content on the standard output.
    """
    with open(filename, encoding="utf-8") as Fl:
        print(Fl.read(), end="")
