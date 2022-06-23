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
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square
        Args:
            size (int): size of the square
            position (int tuple): position of the square"""
        self.__size = size
        self.__position = position
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

    @property
    def position(self):
        """ getter function for private attribuet position
            Returns:
                position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            setter function for private attribute position
            Args:
                value: position value to set to
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the current square area
        Args:
        Returns:
        Examples:
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
