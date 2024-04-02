#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """
    params:
        Size (int): size of square
    """

    def __init__(self, size=0):
        """Initialize the Square.

        The __init__ method initializes the size value of the square.

        parameters:
            size (int, optional): The size of the square.

        Raises:
            TypeError: If size type is not int.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Return current square area.
        Returns:
            int: The area of the square
        """
        return self.__size ** 2
