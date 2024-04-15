#!/usr/bin/python3
"""
add attribute module
"""


def add_attribute(obj, attr_name, attr_value):
    """
    function that adds an attribute to an object
    """
    if isinstance(obj, dict):
        obj[attr_name] = attr_value
    else:
        raise TypeError("can't add a new attribute")
