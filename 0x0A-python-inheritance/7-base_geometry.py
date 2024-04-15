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

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.

        params:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
