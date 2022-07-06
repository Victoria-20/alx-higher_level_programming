#!/usr/bin/python3
""" Module for Student Class"""


class Student:
    """ Defines a student:
        Attrs:
            first_name (str): student firstname
            last_name (str): student surname
            age (int): student age
        Methods:
            __init__ - initializes the Student instance
            to_json - retrieves dictionary desc of Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialiss Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation of Student
            Args:
                attr (list): attribute names that are to be retrieved
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
