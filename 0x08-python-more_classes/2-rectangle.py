#!/usr/bin/python3
"""
Defines a Rectangle class module
"""


class Rectangle:
    """
    Defines a rectangle class module with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance

        params:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.

        params:
            value (int): The value to set as width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.

        params:
            value (int): The value to set as height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)  
