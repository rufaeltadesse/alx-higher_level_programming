#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keys = a_dictionary.keys()
    found = 0
    for i in keys:
        if i == key:
            found = 1
            break
    if found is 1:
        del a_dictionary[key]
    return a_dictionary
