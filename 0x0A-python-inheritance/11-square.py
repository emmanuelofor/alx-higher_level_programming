#!/usr/bin/python3
"""A Rectangle subclass Square is defined by this module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """a new square is initialized
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
