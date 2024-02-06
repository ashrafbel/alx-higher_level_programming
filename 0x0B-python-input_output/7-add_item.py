#!/usr/bin/python3
"Include all provided arguments in a Python list and store them in a file."
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, "add_item.json")
