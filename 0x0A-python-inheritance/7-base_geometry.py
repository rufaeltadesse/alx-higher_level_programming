#!/usr/bin/python3
"""Defining a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsenting base geometry."""

    def area(self):
        """Un implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating function

        Args:
            name (str): name rep
            value (int): value rep
        Raises:
            TypeError: if mismatch
            ValueError: if value is negative
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
