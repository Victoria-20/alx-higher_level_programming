#!/usr/bin/python3

"""Description: Defines a class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

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
        """ sets the width
            Args:
                value (int): value to be assigned to height
        """
        self.__width = value

    @property
    def x(self):
        """ Retrieves x
            Returns:
                x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the x value
            Args:
                value (int): value to be assigned to x
        """
        self.__width = value

    @property
    def y(self):
        """ Retrieves the y value
            Returns:
                y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the y value
            Args:
                value (int): value to be assigned to y
        """
        self.__width = value
