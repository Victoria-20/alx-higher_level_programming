#!/usr/bin/python3
""" Module to calculate a Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a class Square
       Args:
    """

    def __init__(self, size):
        """Validates size """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
