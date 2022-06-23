#!/usr/bin/python3

"""Module Docstring.
This module demostrates how to create a node of a singly linked list.

"""


class Node:
    """Defines a Node
    Args:
        No parameters
    Attributes:
        No attributes

    """
    def __init__(self, data, next_node=None):
        """Initializes attributes of a node
        Args:
            data (int): size of the square
            next_node: pointer to next node or None
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """function to get the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """function to assign value to data
            Args:
                value (int): value to be assigned to data
        """

        if not type(value) is int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Get the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value for the next node """
        self.__next_node = value

        if not self.value == None or self.value == Node:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self, head):
        """Initializes the class"""
        self.__head = head

    def sorted_insert(self, value):
        """Inserts a new node in sorted order"""
