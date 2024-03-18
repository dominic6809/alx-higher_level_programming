#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all occurrences of 'c' and 'C' from the string.

    Args:
        my_string (str): The input string.

    Returns:
        str: The modified string with all 'c' and 'C' removed.
    """
    new_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
