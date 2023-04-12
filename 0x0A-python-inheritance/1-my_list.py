#!/usr/bin/python3
"""The list class is inherited by this module"""


class MyList(list):
    """The list is inherinted by the class"""
    def print_sorted(self):
        """A sorted list is printed"""
        print(sorted(self))
