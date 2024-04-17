#!/usr/bin/python3
"""Def function from JsonnToObject """
import json


def from_json_string(my_str):
    """return from json to object"""
    return json.loads(my_str)
