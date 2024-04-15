#!/usr/bin/python3
"""
function to Define a function that adds attributes to objects.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible.

    params:
    obj: The object to which the attribute should be added.
    attr (str): The name of the attribute.
    value: The value of the attribute.

    Raises:
    TypeError: If the object cannot have a new attribute.
    """
    if isinstance(obj, dict):
        obj[attr_name] = attr_value
    else:
        raise TypeError("can't add a new attribute")
