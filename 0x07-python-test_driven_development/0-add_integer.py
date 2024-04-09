#!/usr/bin/python3
"""
 function that adds 2 integers.
 """


def add_integer(a, b=98):
    """
    Returns:
        int: Sum of a and b.

    params:
        a (int or float): First integer or float.
        b (int or float): Second integer or float. Defaults to 98.
        
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not(isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
