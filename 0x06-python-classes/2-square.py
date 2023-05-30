#!/usr/bin/python3
"""Defining a square class"""


class Square:
    """Defining class attributes"""

    def __init__(self, size=0):
        """Initializing constructurs"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
