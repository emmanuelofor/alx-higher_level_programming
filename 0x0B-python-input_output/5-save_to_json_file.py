#!/usr/bin/python3
"""A JSON file-writing function is defined by this module"""
import json


def save_to_json_file(my_obj, filename):
    """An object to a text file using JSON format is written by this function"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
