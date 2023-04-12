#!/usr/bin/python3
"""a function that adds attributes to objects is defined by this module"""


def add_attribute(obj, att, value):
    """new attribute is added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
