#!/usr/bin/python3
"""Class to define a square."""


class Square:
    """square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        params:
            size (int): The size of the square.
            position (tuple): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
      """Sets the size of the square.

        params:
            value (int): Size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
      """Sets the position of the square.

        params:
            value (tuple): Position value to set.

        Raises:
            TypeError: If value != tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for p in range(0, self.__position[1])]
        for p in range(0, self.__size):
            [print(" ", end="") for q in range(0, self.__position[0])]
            [print("#", end="") for r in range(0, self.__size)]
            print("")

    def __str__(self):
        """String representation of the square.

        Returns:
            str: String representation of the square.
        """
        if self.__size != 0:
            [print("") for p in range(0, self.__position[1])]
        for p in range(0, self.__size):
            [print(" ", end="") for q in range(0, self.__position[0])]
            [print("#", end="") for r in range(0, self.__size)]
            if p != self.__size - 1:
                print("")
        return ("")
