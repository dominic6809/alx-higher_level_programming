#!/usr/bin/python3
"""Defines a string-to-JSON function."""


import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    params:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    # Use json.dumps to convert the object to JSON string
    return json.dumps(my_obj)
