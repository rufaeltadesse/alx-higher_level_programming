#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newlist = set_1.difference(set_2)
    newlis2 = set_2.difference(set_1)
    newlist3 = newlist.union(newlis2)
    return newlist3
