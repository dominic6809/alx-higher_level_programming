#!/usr/bin/python3
"""
Function to define square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Rectangle unherited by square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor for square class
        params:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter for size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return the print() and str() representation of a Square
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """
        update attributes using either args or kwargs
        params:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if args:
            args_names = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
            }
