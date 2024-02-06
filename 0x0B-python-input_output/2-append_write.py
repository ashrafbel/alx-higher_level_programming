#!/usr/bin/python3
"""Def funtion AppendFile"""


def append_write(filename="", text=""):
    "Adds a string to the conclusion of a UTF-8 encoded text file."
    with open(filename, "a", encoding="utf-8") as Fl:
        return Fl.write(text)
