#!/usr/bin/python3

""" Integer validator"""


class BaseGeometry:
    """Integer validator
       Args:
    """

    def area(self):
        """ Raises an ``Exception`` if area not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Raises ``TypeError`` & ``ValueError`` """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
