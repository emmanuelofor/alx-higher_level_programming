#!/usr/bin/python3
"""A string-to-JSON function is defined by this module"""
import json


def to_json_string(my_obj):
    """Returns representation of a string object in JSON"""
    return json.dumps(my_obj)
