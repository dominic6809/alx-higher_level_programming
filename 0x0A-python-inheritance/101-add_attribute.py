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
    if hasattr(obj, '__dict__') or hasattr(type(obj), '__slots__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
