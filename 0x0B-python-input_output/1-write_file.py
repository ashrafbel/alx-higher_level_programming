#!/usr/bin/python3
"""Def function WriteFile"""


def write_file(filename="", text=""):
    "Save a string to a text file using UTF-8 encoding"
    with open(filename, "w", encoding="utf-8") as Fl:
        return Fl.write(text)
