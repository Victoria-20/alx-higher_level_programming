#!/usr/bin/python3

"""Module Docstring.
This module demostrates how to create a class named Square
that defines a square.

"""


class Square:
    """Defines a square
    Args:
        No parameters
    Attributes:
        No attributes

    """
    def __init__(self, size=0):
        """Initializes a new square
        Args:
            size (int): size of the square"""
        self.__size = size
        if not type(self.__size) is int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """ getter function to set the size
            Returns:
                size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function to assign value to size
            Args:
                value (int): value to be assigned to size
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the current square area
        Args:
        Returns:
        Examples:
        """
        return self.__size ** 2
