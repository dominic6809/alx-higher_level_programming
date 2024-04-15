#!/usr/bin/python3
"""
function to Define  Rectangle class
that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing base geometry.
    """
    def __init__(self, width, height):
        """
        Initialize a rectangle with given width and height.

        params:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
