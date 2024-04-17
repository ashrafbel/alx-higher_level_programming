#!/usr/bin/python3
"Def json_string"
import json


def to_json_string(my_obj):
    "Json representation of a string object."
    J = json.dumps(my_obj)
    return J
