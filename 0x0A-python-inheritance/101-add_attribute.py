#!/usr/bin/python3
"""
function to Define a function that adds attributes to objects.
"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if it's possible.

    params:
    obj: The object to which the attribute should be added.
    attr (str): The name of the attribute.
    value: The value of the attribute.

    Raises:
    TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
