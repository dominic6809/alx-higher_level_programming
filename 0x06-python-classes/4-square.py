#!/usr/bin/python3
"""
Defines a square class attribute
"""


class Square:
    def __init__(self, size=0):
        """
        Constructor for Square class.

        params:
            size (int): Size of the square. (Defaults to 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for size attribute.

        Returns:
            int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.

        params:
            value (int): Size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
