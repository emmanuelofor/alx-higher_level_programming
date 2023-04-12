#!/usr/bin/python3
"""Verify if object is an instance of a class"""


def is_same_class(obj, a_class):
    """if object is an instance of the class, return true
    otherwise return false
    """
    return (type(obj) == a_class)
