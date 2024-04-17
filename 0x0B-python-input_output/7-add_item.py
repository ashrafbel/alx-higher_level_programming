#!/usr/bin/python3
"""Include all provided arguments in a Python list and store them in a file."""
import sys


from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

lisAr = list(sys.argv[1:])
try:
    List_ = load_from_json_file("add_item.json")
except FileNotFoundError:
    List_ = []

List_.extend(lisAr)
save_to_json_file(List_, "add_item.json")
