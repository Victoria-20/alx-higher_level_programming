#!/usr/bin/python3
""" JSON serialisation of an object """


def class_to_json(obj):
    """Returns a dictionary object"""
    return obj.__dict__
