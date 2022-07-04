#!/usr/bin/python3
""" Module to define Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a class Rectangle
       Args:
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    integer_validator()
