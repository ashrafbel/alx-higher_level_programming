#!/usr/bin/python3
"""Def function JSONsTR"""
import json


def to_json_string(my_obj):
    "Provide the JSON representation of a string object."
    return json.dumps(my_obj)
