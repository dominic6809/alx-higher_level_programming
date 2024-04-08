#!/usr/bin/python3
"""
Defines Rectangle class module
"""


class Rectangle:
    """
    defines a rectangle class  with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance

        paramss:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width attribute."""
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
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rect = []
            for i in range(self.__height):
                [rect.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    rect.append("\n")
            return("".join(rect))
