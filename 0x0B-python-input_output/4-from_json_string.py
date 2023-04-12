#!/usr/bin/python3
"""A JSON-to-object function is defined by this module"""


import json


def from_json_string(my_str):
    """The Python object representation of a JSON string is returned"""
    return json.loads(my_str)
