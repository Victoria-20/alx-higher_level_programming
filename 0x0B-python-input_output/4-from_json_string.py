#!/usr/bin/python3
"""Module to return JSON representation """
import json


def from_json_string(my_str):
    """ Returns the JSON reprensenation of an object"""
    return json.loads(my_str)
