#!/usr/bin/python3
"""
function to Define a base geometry class BaseGeometry.
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
        Exception: If the area calculation is not implemented.
        """
        raise Exception("area() is not implemented")
