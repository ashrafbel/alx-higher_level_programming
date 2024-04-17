#!/usr/bin/python3
"""Def fuction SaveToJsonFile"""
import json


def save_to_json_file(my_obj, filename):
    "Save an object to a text file by utilizing its JSON representation."
    with open(filename, "w") as F_l:
        J = json.dump(my_obj, F_l)
        return J
