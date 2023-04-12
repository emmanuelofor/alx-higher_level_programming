#!/usr/bin/python3
"""verifies if object is an instance of a class that
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """If object is an instance of a class that is inherited, Return true
    otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
