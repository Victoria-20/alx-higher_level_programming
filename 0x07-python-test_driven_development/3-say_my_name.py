#!/usr/bin/python3
"""
prints strings
"""


def say_my_name(first_name, last_name=""):
    """ Prints first_name and last_name """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    elif not type(last_name) is str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
