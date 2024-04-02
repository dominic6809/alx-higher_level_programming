#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    Print an int and return True if successful, otherwise, False
    and print an error message to stderr.
    :param value: Value to print
    :return: True if value has correctly printed as an int, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as error:
        print("Exception:", error, file=sys.stderr)
        return False
