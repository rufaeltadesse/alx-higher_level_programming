#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    keys = a_dictionary.keys()
    found = 0
    for i in keys:
        if i == key:
            a_dictionary[i] = value
            found = 1
    if found == 0:
        a_dictionary[key] = value
    return a_dictionary
