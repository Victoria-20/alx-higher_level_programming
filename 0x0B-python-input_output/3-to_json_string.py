#!/usr/bin/python3
"""Module to return JSON representation """
import json


def to_json_string(my_obj):
    """ Returns the JSON reprensenation of an object"""
    return json.dumps(my_obj)
