#!/usr/bin/python3
""" Define a class """


class LockedClass:
    """prevents user from creating dynamic attributes
    """
    __slots__ = ['first_name']
