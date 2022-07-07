#!/usr/bin/python3
"""Module for inserting line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text when searched string is found """
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            if search_string in line:
                f.write(line + new_string)
            else:
                f.write(line)
