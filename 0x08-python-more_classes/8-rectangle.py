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
        number_of_instances (int)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """string representation of rectangle"""
        total = ""
        if self.__height == 0 or self.__width == 0:
            return total
        for i in range(self.__height):
            total += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        """string representation of the rectangle
           recreates a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete object instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')

        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
