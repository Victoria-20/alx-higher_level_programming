#!/usr/bin/python3
"""Module to check if an object is an instance"""


def is_same_class(obj, a_class):
    """ Return True if object is instance otherwise False """

    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False
