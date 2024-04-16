#!/usr/bin/python3
"""
function that writes an Object to a text file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    params:
        my_obj: The object to be written to the file.
        filename (str): The name of the file to write the
        JSON representation to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False, indent=4)
