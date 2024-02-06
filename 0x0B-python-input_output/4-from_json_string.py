#!/usr/bin/python3
"""Def function from JsonnToObject """
import json


def from_json_string(my_str):
    """Return JSON str"""
    return json.loads(my_str)
