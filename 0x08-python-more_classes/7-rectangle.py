#!/usr/bin/python3
"""
Rectangle class module
"""


class Rectangle:
    """
    defines a rectangle with width and height attributes.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance

        params:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.
        """
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
        return self.width * self.height

    def perimeter(self):
        if 0 in (self.__height, self.__width):
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) *
                 self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """
        Returns a string representation of the rectangle to recreate it.
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
