#!/usr/bin/python3
"""
A python script that adds all arguments to a Python List.
"""
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
import sys


def main():
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    main()
