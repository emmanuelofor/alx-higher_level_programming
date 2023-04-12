#!/usr/bin/python3
"""Verifies if object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """if object is an instance of a class, returns true
    or a class that is inherited from the class in question
    """
    return (isinstance(obj, a_class))
