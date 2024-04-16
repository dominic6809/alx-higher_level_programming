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
    # Use json.dumps to convert the object to a JSON string
    json_str = json.dumps(my_obj)

    # Open the file for writing using 'with' statement
    with open(filename, 'w') as file:
        file.write(json_str)
