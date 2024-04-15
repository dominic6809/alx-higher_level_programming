#!/usr/bin/python3
"""
function to Define a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A class representing an integer with
    inverted equality and inequality operators.
    """

    def __eq__(self, other):
        """
        Check if self is not equal to other.

        params:
        other: The object to compare with.

        Returns:
        bool: True if self is not equal to other; otherwise False.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Check if self is equal to other.

        params:
        other: The object to compare with.

        Returns:
        bool: True if self is equal to other; otherwise False.
        """
        return super().__eq__(other)
