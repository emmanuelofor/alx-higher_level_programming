#!/usr/bin/python3
"""A file-appending function is defined by this module"""


def append_write(filename="", text=""):
    """A string to the end of a UTF8 text file is appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
