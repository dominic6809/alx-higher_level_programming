#!/usr/bin/python3
"""
Defines Square class attribute
"""


class Square:
    """Constructor for square class."""

    def __init__(self, size=0):
        """
            Initializes a new Square instance with an optional size.
            params:
                size (int): The size of the square (default is 0).
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
            Getter method to retrieve the size attribute.
            Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            Returns current square area.
            Returns:
                int: The area of the square.
        """
        return self.__size * self.__size
