#!/usr/bin/python3
"""
function to return list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    It returns the list of available attributes and methods.

    params:
	  obj (object): object.
    """
    return dir(obj)
