#!/usr/bin/python3
"""Module to create an object from JSON file """
import json


def load_from_json_file(filename):
    """ Writes an object to a text file
        using JSON representation
    """
    with open(filename, 'r') as f:
        return json.load(f)
