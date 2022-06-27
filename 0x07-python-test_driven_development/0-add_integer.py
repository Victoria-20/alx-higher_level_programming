#!/usr/bin/python3
""" Calculation module """

def add_integer(a, b=98):
    """ function to return sum of two integers """

    test_a = type(a) in [int, float]
    test_b = type(b) in [int, float]

    if test_a and test_b:
        return a + b
    elif test_a:
        raise TypeError("a must be an integer")
    elif test_b:
        raise TypeError("b must be an integer")
