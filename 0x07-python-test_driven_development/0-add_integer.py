#!/usr/bin/python3
"""

 Module to calculate the sum of integers

 """


def add_integer(a, b=98):
    """
    Function to return sum of two integers

    """

    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b is None:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
