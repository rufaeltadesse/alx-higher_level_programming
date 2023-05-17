#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    newlist = set(my_list)
    for i in newlist:
        count = count + i
    return count
