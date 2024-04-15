#!/usr/bin/python3
"""
same class instance module
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    params:
    obj: The object to check.
    a_class: The class to check against.

    Returns:
    True if the object is exactly an instance of the specified class;
    otherwise False.
    """
    return type(obj) is a_class
