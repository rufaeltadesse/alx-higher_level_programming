#!/usr/bin/python3
"""Defining a reactangle class."""


class Rectangle:
    """Rectangle class rep."""

    def __init__(self, width=0, height=0):
        """Initialize new rect.

        Args:
            width (int): width of the new rectangle
            height (int): height of the new rect
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rect"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of rect """
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """Return the area of rect"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of rect."""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
