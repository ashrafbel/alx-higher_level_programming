#!/usr/bin/python3
"Include all provided arguments in a Python list and store them in a file."
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

lisAr = list(sys.argv[1:])
try:
    List_ = load_from_json_file("add_item.json")
except Exception:
    List_ = []
    
List_.extend(lisAr)
save_to_json_file(List_, "add_item.json")
