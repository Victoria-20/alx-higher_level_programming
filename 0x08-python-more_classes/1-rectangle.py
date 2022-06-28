#!/usr/bin/python3

"""Module Docstring.
This module demostrates how to create an empty class named Rectangle
that defines a rectangle.
"""


class Rectangle:
    """Defines an empty Rectangle
    Args:
        No parameters
    Attributes:
        No attributes
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves the width
            Returns:
                width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width
            Args:
                value (int): value to be assigned to width
        """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves the height
            Returns:
                height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height
            Args:
                value (int): value to be assigned to height
        """
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
