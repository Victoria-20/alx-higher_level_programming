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
