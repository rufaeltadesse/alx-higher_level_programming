#!/usr/bin/python3
"""Defining a list."""


class MyList(list):
    """Defining class attributes"""

    def print_sorted(self):
        """Sorting list"""
        print(sorted(self))
