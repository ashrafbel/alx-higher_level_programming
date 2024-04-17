#!/usr/bin/python3
"""Def function ReeadFile json"""
import json


def load_from_json_file(filename):
    "generate a Python object from a JSON file."
    with open(filename) as f_l:
        J = json.load(f_l)
        return J
