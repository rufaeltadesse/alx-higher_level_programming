#!/usr/bin/python3
"""Writing a file"""


def write_file(filename="", text=""):
    """ File writing
    Args:
        filename: name of the file."".
        text: text to write"".
    Returns:
        int: character count
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """writes char to file"""
        return f.write(text)
