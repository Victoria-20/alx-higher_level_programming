#!/usr/bin/python3
""" Module to check object instance"""


def inherits_from(obj, a_class):
    """Returns True if"""
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    else:
        return False
