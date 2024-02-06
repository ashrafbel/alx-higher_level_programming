#!/usr/bin/python3
"""Def function ReeadFile json"""
import json


def load_from_json_file(filename):
    "Generate a Python object from a JSON file."
    with open(filename) as Fl:
        return json.load(Fl)
