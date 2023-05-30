#!/usr/bin/python3
"""Defining a square class"""


class Square:
    """Defining the class attributes"""

    def __init__(self, size=0):
        """initializing class constructors"""
        self.size = size

    @property
    def size(self):
        """getting current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returing area"""
        return (self.__size * self.__size)
