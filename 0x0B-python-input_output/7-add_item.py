#!/usr/bin/python3
"""
A python script that adds all arguments to a Python List.
"""


import sys
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file

def main():
    try:
        items_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items_list = []

    items_list.extend(sys.argv[1:])

    save_to_json_file(items_list, "add_item.json")

if __name__ == "__main__":
    main()
