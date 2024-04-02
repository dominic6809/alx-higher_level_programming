#!/usr/bin/python3
"""
Defines a Square class
"""


class Square:
    def __init__(self, size=0):
        """
        Constructor for Square class.

        params:
            size: Size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
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
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#' to stdout.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
