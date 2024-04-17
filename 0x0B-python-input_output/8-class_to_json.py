#!/usr/bin/python3
"""Def function ClassToJson"""


def class_to_json(obj):
    "Get dictionary from simple data structure."
    return obj.__dict__
