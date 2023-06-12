#!/usr/bin/python3
"""Defining a class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing a rectangle """

    def __init__(self, width, height):
        """Intializing

        Args:
            width (int): width
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returnarea"""
        return self.__width * self.__height

    def __str__(self):
        """Str method"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
