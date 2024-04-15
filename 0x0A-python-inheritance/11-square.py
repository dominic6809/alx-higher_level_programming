#!/usr/bin/python3
"""
function to Define a Rectangle subclass Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        A class representing a square,
        inheriting from Rectangle.
        Attributes:
            size (int): side of the square
        Methods:
            __init__ - initialises the square
    """
    def __init__(self, size):
        """
        Initialize a square with given size.

        Args:
        size (int): The size of the square.
        """
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        square description return function
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
