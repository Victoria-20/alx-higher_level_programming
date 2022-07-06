#!/usr/bin/python3
""" Module to read a file"""


def read_file(filename=""):
    """ Reads a file and print to stdout """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
