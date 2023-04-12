#!/usr/bin/python3
"""A text file-reading function is defined by this module"""


def read_file(filename=""):
    """The contents of a UTF8 text file are printed"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
