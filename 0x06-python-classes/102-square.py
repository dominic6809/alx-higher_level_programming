#!/usr/bin/python3
"""Class to define a square"""


class Square:
    def __init__(self, size=0):
        """initializes the square
        params:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """compute the square's area
        Returns:
            number: Area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            number: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        params:
            value (number): Size value to set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def __lt__(self, other):
        """
        Less than comparator.

        params:
            other (Square): Another Square object.

        Returns:
            bool: True if area is less, False otherwise.
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Less than or equal comparator.

        params:
            other (Square): Another Square object.

        Returns:
            bool: True if area is less than or equal, False otherwise.
        """
        return self.size <= other.size

    def __eq__(self, other):
        """
        Equal comparison.

        params:
            other (Square): Another Square object.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Not equal comparison operator.

        params:
            other (Square): Another Square object.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.size != other.size

    def __ge__(self, other):
        """
        Greater than or equal comparison operator.

        params:
            other (Square): Another Square object.

        Returns:
            bool: True if area is greater than or equal, False otherwise.
        """
        return self.size >= other.size

     def __gt__(self, other):
        """
        Greater than comparator.

        params:
            other (Square): Another Square object.

        Returns:
            bool: True if area is greater, False otherwise.
        """
        return self.size > other.size
