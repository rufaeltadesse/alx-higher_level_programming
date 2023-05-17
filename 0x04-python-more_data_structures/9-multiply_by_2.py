#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {}
    keys = a_dictionary.keys()
    for i in keys:
        b_dictionary[i] = a_dictionary[i] * 2
    return b_dictionary
