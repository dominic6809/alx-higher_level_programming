#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Executes a function safely and returns the result.
    If an exception occurs during execution, prints the error message
    to stderr and returns None.
    :param fct: function to execute
    :param args: Arguments to pass to the function
    :return: The result of the function, or None if an exception occurs
    """
    try:
        result = fct(*args)
        return result
    except Exception as error:
        print("Exception:", error, file=sys.stderr)
        return None
