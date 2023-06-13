#!/usr/bin/python3
"""Appending to file"""


def append_write(filename="", text=""):
    """File appending
    Args:
        filename: Name of file"".
        text: string of text"".
    Returns:
        int: character count.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        """appending to file"""
        return f.write(text)
