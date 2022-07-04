#!/usr/bin/python3
""" Module that defines MyList"""


class MyList(list):
    """ MyList class"""

    def print_sorted(self):
        """ Prints a sorted list"""
        list.sort()
        print(list)
