#!/usr/bin/python3
"""
    The list of available attributes are returned by this module
    and methods of an object are also returned
"""


def lookup(obj):
    """This functions looks out for all attributes and methods of an object"""
    return dir(obj)
