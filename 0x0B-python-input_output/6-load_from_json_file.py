#!/usr/bin/python3
"""
function that creates an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    params:
        filename (str): The name of the JSON file
        to load the object from.

    Returns:
        object: The object loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        # Load the JSON string from the file
        json_str = file.read()
        return json.loads(json_str)
