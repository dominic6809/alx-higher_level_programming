#!usr/bin/python3
"""
print square module
"""


def print_square(size):
    """
    Program to print a square with the character #.

    params:
        size (int): Length of the square's side.

    Raises:
        TypeError: If size is not an integer or if size is float < 0.
        ValueError: If size is < 0.
    """
    # Check if size is an integer or a float less than 0
    if isinstance(size, float) and size < 0.0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
