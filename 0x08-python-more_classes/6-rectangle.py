#!/usr/bin/python3
"""Defines a Rect ."""


class Rectangle:
    """Represent a rect.

    Attributes:
        number_of_instances (int): number of rect instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Init a new Rect

        Args:
            width (int): width of the new rect
            height (int): Height of the new rect.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rect ."""
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
        """Get/set the height of the rect."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rect."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rect."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable rep of the rect.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recta = []
        for i in range(self.__height):
            [recta.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                recta.append("\n")
        return ("".join(recta))

    def __repr__(self):
        """Return the string repr of the rect."""
        recta = "Rectangle(" + str(self.__width)
        recta += ", " + str(self.__height) + ")"
        return (recta)

    def __del__(self):
        """Print a message for every deletion of a rect."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
