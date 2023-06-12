#!/usr/bin/python3
"""Checking if obj is instance of a class"""


def is_kind_of_class(obj, a_class):
    """Instance of a class.

    Args:
        obj (any): Obj to be checked
        a_class (type): class type
    Returns:
        returns comparision of values
    """
    if isinstance(obj, a_class):
        return True
    return False
