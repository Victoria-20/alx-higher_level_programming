#!/usr/bin/python3
""" Module to check if same class or inherited """


def is_kind_of_class(obj, a_class):
    """Return True if object is an instance otherwise False """
    if isinstance(obj, a_class):
        return True
    else:
        return False
