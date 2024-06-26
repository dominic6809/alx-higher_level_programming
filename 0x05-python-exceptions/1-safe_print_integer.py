#!/usr/bin/python3
def safe_print_integer(value):
    """
    Print an integer with "{:d}".format().

    :param value: Value to print (can be any type)
    :return: True if value has correctly printed as an int, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
