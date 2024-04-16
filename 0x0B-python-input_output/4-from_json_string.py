#!/usr/bin/python3
"""
function that returns an object by JSON string
"""


import json


def from_json_string(my_str):
    """
    Returns a Python data structure represented by a JSON string.

    params:
        my_str (str): The JSON string to be converted
        to a Python data structure.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
