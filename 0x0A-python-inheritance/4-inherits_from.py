#!/usr/bin/python3
"""Defining an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    function that checks if object is excactly an instane of
    a specified class.

    params:
    obj: The object to check.
    a_class: The class to check against.

    Return:
    bool: True if instance is same otherwise False
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
