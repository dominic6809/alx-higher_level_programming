#!/usr/bin/python3
"""
Defines a Square class
"""


class Square:
    """Constructor for a square"""
    def __init__(self, size):
        """initialize new square
        params:
        size(int): size of new square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for size attribute.

        Returns:
            int: Size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.

        Args:
            value (int): Size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        """
        Print the square with the character '#' to stdout.
        """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
