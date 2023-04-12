#!/usr/bin/python3
"""A file-writing function is defined by this module"""


def write_file(filename="", text=""):
    """A string to a UTF8 text file is written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
