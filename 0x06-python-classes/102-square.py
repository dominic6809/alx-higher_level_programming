#!/usr/bin/python3
"""Class to define a square"""


class Square:
    """square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        params:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """computes the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Retrieves the size of the square
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square
        params:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def __lt__(self, other):
        """Less than comparator
        params:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """Less than or equal comparator
        params:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Equal comparator
        params:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Not equal comparator
        params:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """Greater than or equal comparator
        params:
            other (Square): square to compare against
        Returns:
            bool: True if area is greater than or equal, False otherwise
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Greater than comparator
        params:
            other (Square): square to compare against
        Returns:
            bool: True if area is greater than or equal, False otherwise
        """
        return self.size > other.size
