#!/usr/bin/python3
"""Obj from JSOn file"""
import json


def load_from_json_file(filename):
    """obj create from json
    Args:
        filename: file name.
    Returns:
        object: object.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
