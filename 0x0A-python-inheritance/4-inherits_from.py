#!/usr/bin/python3
"""sub class def"""


def inherits_from(obj, a_class):
    """checking instance of a class

    Args:
        obj (any): obj to be checked
        a_class (type): Class type to be checked
    Returns:
        result of operation
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
