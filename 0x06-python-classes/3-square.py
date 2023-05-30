#!/usr/bin/python3
"""Defining a square"""


class Square:
    """Defining class attribues"""

    def __init__(self, size=0):
        """initializing class constructors"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returs current area"""
        return (self.__size * self.__size)
