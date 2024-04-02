#!/usr/bin/python3
"""
MagicClass module matching exactly a bytecode
"""

import math


class MagicClass:
    """circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        params:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: Area of the square.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Computes the circumference of the square.

        Returns:
            int: The circumference of the MagicClass
        """
        return (2 * math.pi * self.__radius)
