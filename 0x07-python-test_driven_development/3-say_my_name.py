#!/usr/bin/python3
"""
name-print-module
"""


def say_my_name(first_name, last_name=""):
    """
    Function that Prints first name and last name

    params:
        first_name (str): First name.
        last_name (str, optional): Last name.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
